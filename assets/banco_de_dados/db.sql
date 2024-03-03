-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema oficina
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema oficina
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `defaultdb` DEFAULT CHARACTER SET utf8 ;
USE `defaultdb` ;

-- -----------------------------------------------------
-- Table `oficina`.`Cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `defaultdb`.`Cliente` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(200) NOT NULL,
  `senha` VARCHAR(100) NOT NULL,
  `cidade` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `oficina`.`Funcionario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `defaultdb`.`Funcionario` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `senha` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `oficina`.`servico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `defaultdb`.`servico` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NULL,
  `preco` FLOAT NULL,
  `img` VARCHAR(200) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `oficina`.`carro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `defaultdb`.`carro` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(200) NOT NULL,
  `modelo` VARCHAR(200) NOT NULL,
  `descricao` TEXT NULL,
  `img` VARCHAR(300) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `oficina`.`contrato`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `defaultdb`.`contrato` (
  `Cliente_id` INT NOT NULL,
  `servico_id` INT NOT NULL,
  `carro_id` INT NOT NULL,
  `data` DATETIME NOT NULL,
  `forma_pagamento` VARCHAR(100) NOT NULL,
  `confirmacao_pagamento` TINYINT NOT NULL DEFAULT 0,
  `desconto` FLOAT NOT NULL,
  `aprovado` TINYINT NOT NULL DEFAULT 0,
  `contratocol` VARCHAR(45) NULL,
  `Funcionario_id` INT NULL,
  PRIMARY KEY (`Cliente_id`, `servico_id`, `carro_id`),
  INDEX `fk_contrato_servico1_idx` (`servico_id` ASC) VISIBLE,
  INDEX `fk_contrato_carro1_idx` (`carro_id` ASC) VISIBLE,
  INDEX `fk_contrato_Funcionario1_idx` (`Funcionario_id` ASC) VISIBLE,
  CONSTRAINT `fk_contrato_Cliente`
    FOREIGN KEY (`Cliente_id`)
    REFERENCES `defaultdb`.`Cliente` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_contrato_servico1`
    FOREIGN KEY (`servico_id`)
    REFERENCES `defaultdb`.`servico` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_contrato_carro1`
    FOREIGN KEY (`carro_id`)
    REFERENCES `defaultdb`.`carro` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_contrato_Funcionario1`
    FOREIGN KEY (`Funcionario_id`)
    REFERENCES `defaultdb`.`Funcionario` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
