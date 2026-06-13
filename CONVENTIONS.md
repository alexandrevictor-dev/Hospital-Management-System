# Diretrizes e Convenções de Projeto

Este documento registra as boas práticas, padrões de projeto e anotações de engenharia backend adotados na reconstrução do Sistema de Gestão Hospitalar. Ele serve como guia de estilo e arquitetura.

---

## 📁 1. Padronização de Arquivos e Pastas

* **Tudo em minúsculo (snake_case):** Escrever os nomes de todas as pastas e arquivos em letras minúsculas, utilizando sublinhado (`_`) para separar palavras (ex: `models.py`, `database_config.py`).
* **Por que?** O Windows ignora maiúsculas (trata `Main.py` e `main.py` como iguais), mas o Linux (onde a maioria dos servidores backend rodam de verdade) diferencia. Escrever tudo em minúsculo previne bugs de importação e crash do sistema se eu mover o código para um servidor Linux.

---

## 🛠️ 2. Arquitetura e Separação de Conceitos

Para este novo sistema, evolui a estrutura usada no curso do SENAI. No projeto original, utilizavamos arquivos com o sufixo `DAO` (como `pacienteDAO.py`), mas as responsabilidades acabavam se misturando: uma única função pedia dados com `input()`, mostrava menus com `print()`, validava regras de negócio e rodava o SQL no MySQL. 

Se eu quisesse transformar aquele sistema em um site ou app de celular, teria que jogar o arquivo inteiro fora e reescrever do zero, porque telas web ou mobile não entendem comandos de terminal e o banco estava "preso" ali dentro.

Para evitar isso e aplicar o Princípio de Responsabilidade Única (Single Responsibility Principle), utilizarei a **Arquitetura em Camadas** com o **Padrão Repository**:

* **Camada de Interface (UI/CLI) — `ui/cli.py`:** * Criei esta camada para cuidar puramente da CLI (*Command Line Interface*), que é o termo para o programa rodar no terminal.
  * **Regra de Ouro:** Toda interação com o teclado (`input()`) e exibição em tela (`print()`) fica **exclusivamente** aqui. Nenhum outro arquivo de regra de negócio ou banco de dados pode usar esses comandos. Isso limpa meu código e me permite mudar a interface no futuro sem tocar na inteligência do sistema.
* **Camada Service (Regras de Negócio) — `core/services.py`:**
  * É o cérebro do sistema. Ela não sabe e não se importa se o dado veio do terminal, de um site ou de um app; ela apenas valida as regras de negócio.
  * *Exemplo:* Ela recebe o CPF e verifica se ele tem 11 dígitos ou se o paciente precisa de responsável. Se algo estiver errado, ela barra a operação antes de gastar processamento com o banco.
* **Camada Repository (Infraestrutura) — `infrastructure/repositories.py`:**
  * Esta camada substitui o antigo padrão DAO e funciona como o operário do banco de dados. Ela não faz `print`, não faz `input` e não valida regras humanas. Ela apenas recebe os dados limpos da camada Service, executa o comando SQL (como `INSERT INTO`) de forma segura no MySQL e devolve o resultado bruto.

---

## 🛡️ 3. Tratamento de Erros e Robustez

* **Falha Graciosa:** Desenvolve os loops principais do sistema e as conexões externas para preverem falhas abruptas. Se o programa tiver que falhar ou fechar por causa de um erro ou de uma ação externa, ele deve fazer isso de forma elegante, educada e controlada com uma mensagem.
* **Captura de `KeyboardInterrupt`:** O menu principal captura quando alguém pressiona `Ctrl+C` no terminal e isso permite encerrar o programa de forma limpa (`sys.exit(0)`) com uma mensagem amigável, em vez de estourar um erro de rastreamento (traceback) cheio de códigos e linhas na tela.

---

## ⚙️ 4. Gerenciamento de Dependências

* **Controle de Versão com `requirements.txt`:** Controla todas as bibliotecas externas do projeto usando operadores como `>=`. Isso garante que o projeto use recursos modernos, mas previne que o sistema tente rodar com uma biblioteca antiga e defasada se outra pessoa clonar o repositório.