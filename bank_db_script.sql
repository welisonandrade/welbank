CREATE DATABASE IF NOT EXISTS bank_db;

USE bank_db;

CREATE TABLE IF NOT EXISTS bank_account(
cpf VARCHAR(11) PRIMARY KEY,
nome VARCHAR(16),
senha VARCHAR(15),
saldo VARCHAR(15),
nmr_conta VARCHAR(15)
);

/*CREATE TABLE IF NOT EXISTS bank_history(

);*/
SHOW DATABASES;
SHOW TABLES;
alter table bank_account ADD UNIQUE INDEX(cpf);
DROP TABLE bank_account;
INSERT INTO bank_account (cpf,nome,senha,saldo, nmr_conta) VALUES ('123', 'Welison', '321', '10.0', '9999');
SELECT * FROM bank_account
