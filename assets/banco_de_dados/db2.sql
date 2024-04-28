-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema defaultdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema defaultdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `defaultdb` DEFAULT CHARACTER SET utf8 ;
USE `defaultdb` ;

-- -----------------------------------------------------
-- Table `defaultdb`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `defaultdb`.`cliente` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(200) NOT NULL,
  `senha` VARCHAR(100) NOT NULL,
  `cidade` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `assiste_one_piece` TINYINT NOT NULL DEFAULT 0,
  `e_flamengo` TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `defaultdb`.`funcionario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `defaultdb`.`funcionario` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `senha` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `defaultdb`.`contrato`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `defaultdb`.`contrato` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `cliente_id` INT NOT NULL,
  `Cliente_id` INT NOT NULL,
  `data` DATETIME NOT NULL,
  `forma_pagamento` VARCHAR(100) NOT NULL,
  `confirmacao_pagamento` TINYINT NOT NULL DEFAULT 0,
  `desconto` FLOAT NOT NULL,
  `aprovado` TINYINT NOT NULL DEFAULT 0,
  `Funcionario_id` INT NULL,
  `status` INT NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`, `cliente_id`),
  INDEX `fk_contrato_Funcionario1_idx` (`Funcionario_id` ASC) VISIBLE,
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_contrato_cliente1_idx` (`cliente_id` ASC) VISIBLE,
  CONSTRAINT `fk_contrato_Funcionario1`
    FOREIGN KEY (`Funcionario_id`)
    REFERENCES `defaultdb`.`funcionario` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_contrato_cliente1`
    FOREIGN KEY (`cliente_id`)
    REFERENCES `defaultdb`.`cliente` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `defaultdb`.`servico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `defaultdb`.`servico` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `preco` FLOAT NOT NULL,
  `img` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `defaultdb`.`carro`
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
-- Table `defaultdb`.`atendimento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `defaultdb`.`atendimento` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `data_agendada` DATE NOT NULL,
  `cancelado` TINYINT NOT NULL DEFAULT 0,
  `placa` VARCHAR(45) NOT NULL,
  `contrato_Cliente_id` INT NOT NULL,
  `carro_id` INT NOT NULL,
  `servico_id` INT NOT NULL,
  PRIMARY KEY (`id`, `contrato_Cliente_id`, `carro_id`, `servico_id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_atendimento_contrato1_idx` (`contrato_Cliente_id` ASC) VISIBLE,
  INDEX `fk_atendimento_carro1_idx` (`carro_id` ASC) VISIBLE,
  INDEX `fk_atendimento_servico1_idx` (`servico_id` ASC) VISIBLE,
  CONSTRAINT `fk_atendimento_contrato1`
    FOREIGN KEY (`contrato_Cliente_id`)
    REFERENCES `defaultdb`.`contrato` (`Cliente_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_atendimento_carro1`
    FOREIGN KEY (`carro_id`)
    REFERENCES `defaultdb`.`carro` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_atendimento_servico1`
    FOREIGN KEY (`servico_id`)
    REFERENCES `defaultdb`.`servico` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `defaultdb`.`Pagamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `defaultdb`.`Pagamento` (
  `contrato_id` INT NOT NULL,
  `contrato_cliente_id` INT NOT NULL,
  `data` TIMESTAMP NULL,
  `valor` FLOAT NULL,
  `desconto` FLOAT NULL DEFAULT 0,
  `valor_total` FLOAT NULL,
  PRIMARY KEY (`contrato_id`, `contrato_cliente_id`),
  INDEX `fk_Pagamento_contrato1_idx` (`contrato_id` ASC, `contrato_cliente_id` ASC) VISIBLE,
  CONSTRAINT `fk_Pagamento_contrato1`
    FOREIGN KEY (`contrato_id` , `contrato_cliente_id`)
    REFERENCES `defaultdb`.`contrato` (`id` , `cliente_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `defaultdb`.`cartao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `defaultdb`.`cartao` (
  `confirmado` TINYINT NOT NULL,
  `Pagamento_contrato_id` INT NOT NULL,
  `Pagamento_contrato_cliente_id` INT NOT NULL,
  PRIMARY KEY (`Pagamento_contrato_id`, `Pagamento_contrato_cliente_id`),
  CONSTRAINT `fk_cartao_Pagamento1`
    FOREIGN KEY (`Pagamento_contrato_id` , `Pagamento_contrato_cliente_id`)
    REFERENCES `defaultdb`.`Pagamento` (`contrato_id` , `contrato_cliente_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `defaultdb`.`boleto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `defaultdb`.`boleto` (
  `confirmado` TINYINT NOT NULL,
  `Pagamento_contrato_id` INT NOT NULL,
  `Pagamento_contrato_cliente_id` INT NOT NULL,
  PRIMARY KEY (`Pagamento_contrato_id`, `Pagamento_contrato_cliente_id`),
  CONSTRAINT `fk_boleto_Pagamento1`
    FOREIGN KEY (`Pagamento_contrato_id` , `Pagamento_contrato_cliente_id`)
    REFERENCES `defaultdb`.`Pagamento` (`contrato_id` , `contrato_cliente_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `defaultdb`.`pix`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `defaultdb`.`pix` (
  `confirmado` TINYINT NOT NULL,
  `Pagamento_contrato_id` INT NOT NULL,
  `Pagamento_contrato_cliente_id` INT NOT NULL,
  PRIMARY KEY (`Pagamento_contrato_id`, `Pagamento_contrato_cliente_id`),
  CONSTRAINT `fk_pix_Pagamento1`
    FOREIGN KEY (`Pagamento_contrato_id` , `Pagamento_contrato_cliente_id`)
    REFERENCES `defaultdb`.`Pagamento` (`contrato_id` , `contrato_cliente_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `defaultdb`.`berries`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `defaultdb`.`berries` (
  `confirmado` TINYINT NOT NULL,
  `Pagamento_contrato_id` INT NOT NULL,
  `Pagamento_contrato_cliente_id` INT NOT NULL,
  PRIMARY KEY (`Pagamento_contrato_id`, `Pagamento_contrato_cliente_id`),
  CONSTRAINT `fk_berries_Pagamento1`
    FOREIGN KEY (`Pagamento_contrato_id` , `Pagamento_contrato_cliente_id`)
    REFERENCES `defaultdb`.`Pagamento` (`contrato_id` , `contrato_cliente_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
