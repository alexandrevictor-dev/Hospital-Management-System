CREATE DATABASE IF NOT EXISTS hospital_management
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE hospital_management;


-- Estrutura da Tabela: patients ---
CREATE TABLE IF NOT EXISTS patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cpf CHAR(11) NOT NULL UNIQUE,
    rg VARCHAR(15) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    adress VARCHAR(200) NOT NULL,
    zip_code CHAR(8) NOT NULL,
    birth_date DATE NOT NULL,
    biological_sex TINYINT NOT NULL COMMENT '1: Masculino, 2: Feminino',
    pronouns TINYINT NOT NULL COMMENT '1: Ele/Dele, 2: Ela/Dela, 3: Elu/Delu, 4: Não Informar',
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL,
    guardian VARCHAR(100) DEFAULT NULL
) ENGINE=InnoDB;

-- Estrutura da Tabela: doctors
CREATE TABLE IF NOT EXISTS doctors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    crm VARCHAR(15) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL UNIQUE,
    rg VARCHAR(15) NOT NULL UNIQUE,
    cpf CHAR(11) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL,
    adress VARCHAR(200) NOT NULL,
    zip_code CHAR(8) NOT NULL,
    medical_specialty TINYINT NOT NULL COMMENT '1: Clínico, 2: Pediatria, 3: Ortopedia, 4: Cardiologia, 5:Psiquiatria, 6: Outros',
    hire_date DATE NOT NULL,
    termination_date DATE DEFAULT NULL, --Coluna virtual gerada automaticamente pelo MySQL caso haja data de desligamento
    status VARCHAR(10) GENERATED ALWAYS AS (
        CASE WHEN termination_date IS NULL THEN 'Activate' ELSE 'Inactivate' END
    ) STORED
) ENGINE=InnoDB;

-- Estrutura de Tabela: appointments
CREATE TABLE IF NOT EXISTS appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code CHAR(7) NOT NULL UNIQUE,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    price DECIMAL(6,2) NOT NULL, --O preço só pode ter 6 digitos e 2 para centavos (9999,99)
    doctor_id INT NOT NULL,
    patient_id INT NOT NULL,
    CONSTRAINT fk_appointments_doctor FOREIGN KEY (doctor_id) REFERENCES doctors (id) ON DELETE RESTRICT,
    CONSTRAINT fk_appointments_patient FOREIGN KEY (patient_id) REFERENCES patients (id) ON DELETE RESTRICT
) ENGINE=InnoDB;