-- DROP DATABASE IF EXISTS projeto_EducacaoFinanceira;
CREATE DATABASE IF NOT EXISTS projeto_EducacaoFinanceira CHARACTER SET utf8 COLLATE utf8_general_ci;
USE projeto_EducacaoFinanceira;

CREATE TABLE IF NOT EXISTS Login (
    usuario VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    PRIMARY KEY (usuario)
);
SELECT * FROM Login;