-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema tienda_pair
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema tienda_pair
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `tienda_pair` ;
USE `tienda_pair` ;

-- -----------------------------------------------------
-- Table `tienda_pair`.`ventas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tienda_pair`.`ventas` (
  `id_venta` INT NOT NULL AUTO_INCREMENT,
  `id_producto` VARCHAR(45) NOT NULL,
  `id_cliente` INT NOT NULL,
  `fecha_venta` DATE NULL,
  `cantidad` INT NULL,
  `total` FLOAT NULL,
  PRIMARY KEY (`id_venta`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tienda_pair`.`clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tienda_pair`.`clientes` (
  `id_cliente` INT NOT NULL,
  `first_name` VARCHAR(100) NOT NULL,
  `last_name` VARCHAR(100) NOT NULL,
  `email` VARCHAR(200) NOT NULL,
  `gender` VARCHAR(15) CHARACTER SET 'ascii' NOT NULL,
  `city` VARCHAR(50) NOT NULL,
  `country` VARCHAR(45) NOT NULL,
  `adress` VARCHAR(200) NOT NULL,
  `ventas_id_venta` INT NOT NULL,
  PRIMARY KEY (`id_cliente`, `ventas_id_venta`),
  INDEX `fk_clientes_ventas1_idx` (`ventas_id_venta` ASC) VISIBLE,
  CONSTRAINT `fk_clientes_ventas1`
    FOREIGN KEY (`ventas_id_venta`)
    REFERENCES `tienda_pair`.`ventas` (`id_venta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tienda_pair`.`productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tienda_pair`.`productos` (
  `id_producto` VARCHAR(6) NOT NULL,
  `nombre_producto` VARCHAR(100) NOT NULL,
  `categoria` VARCHAR(100) NOT NULL,
  `precio` FLOAT NOT NULL,
  `origen` VARCHAR(50) NOT NULL,
  `descripcion` VARCHAR(500) NOT NULL,
  PRIMARY KEY (`id_producto`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tienda_pair`.`clientes_has_ventas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tienda_pair`.`clientes_has_ventas` (
)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tienda_pair`.`productos_has_ventas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tienda_pair`.`productos_has_ventas` (
  `productos_id_producto` VARCHAR(6) NOT NULL,
  `ventas_id_venta` INT NOT NULL,
  PRIMARY KEY (`productos_id_producto`, `ventas_id_venta`),
  INDEX `fk_productos_has_ventas_ventas1_idx` (`ventas_id_venta` ASC) VISIBLE,
  INDEX `fk_productos_has_ventas_productos1_idx` (`productos_id_producto` ASC) VISIBLE,
  CONSTRAINT `fk_productos_has_ventas_productos1`
    FOREIGN KEY (`productos_id_producto`)
    REFERENCES `tienda_pair`.`productos` (`id_producto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_productos_has_ventas_ventas1`
    FOREIGN KEY (`ventas_id_venta`)
    REFERENCES `tienda_pair`.`ventas` (`id_venta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
