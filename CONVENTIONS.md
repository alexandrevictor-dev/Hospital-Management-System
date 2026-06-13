# Diretrizes e Convenções do Projeto

Este documento registra as boas práticas, padrões de projeto e conceitos de engenharia backend adotados na reconstrução do Sistema de Gestão Hospitalar.

---

## 📁 1. Padronização de Arquivos e Pastas

* **Tudo em minúsculo (snake_case):** Os nomes de todas as pastas e arquivos devem ser escritos em letras minúsculas, utilizando sublinhado (`_`) para separar palavras (ex: `models.py`, `database_config.py`).
* **Por que?** O Windows ignora maiúsculas (trata `Main.py` e `main.py` como o mesmo arquivo), mas o Linux (onde a maioria dos servidores backend rodam de verdade) diferencia. Escrever tudo em minúsculo evita bugs de importação e crash do sistema ao mover o código para o servidor.

---

## 🛠️ 2. Arquitetura e Separação de Conceitos

O projeto utiliza uma **Arquitetura em Camadas** para garantir que cada parte do código tenha uma única responsabilidade (Single Responsibility Principle).

* **Camada de Interface (UI/CLI):** * **CLI** significa *Command Line Interface* (Interface de Linha de Comando). É o termo técnico para programas que rodam puramente dentro do terminal.
  * **Regra de Ouro:** Toda interação com o teclado (`input()`) e exibição em tela (`print()`) deve ficar **exclusivamente** na pasta `ui/`. Nenhum outro arquivo do sistema (como banco de dados ou regras de negócio) pode usar esses comandos. Isso limpa o código e permite mudar a interface no futuro (ex: para Web ou API) sem tocar na inteligência do sistema.
* **Camada de Banco de Dados (Infrastructure/Repositories):** * Substitui o antigo padrão DAO. É responsável estritamente por executar comandos SQL no banco de dados e retornar dados puros (dicionários ou objetos). Ela não sabe o que o usuário digitou e nem como o resultado será exibido na tela.

---

## 🛡️ 3. Tratamento de Erros e Robustez

* **Falha Graciosa:** Loops principais do sistema e conexões externas devem prever falhas de hardware ou interrupções do usuário.
* **Captura de `KeyboardInterrupt`:** O menu principal deve capturar quando o usuário pressiona `Ctrl+C` no terminal, encerrando o programa de forma limpa (`sys.exit(0)`) com uma mensagem amigável, em vez de estourar um erro de rastreamento (traceback) na tela.

---

## ⚙️ 4. Gerenciamento de Dependências

* **Controle de Versão com `requirements.txt`:** Todas as bibliotecas externas devem ter suas versões controladas usando operadores como `>=` (maior ou igual). Isso garante que o projeto use recursos modernos, mas avise o desenvolvedor se ele tentar rodar o código com uma biblioteca antiga e defasada.