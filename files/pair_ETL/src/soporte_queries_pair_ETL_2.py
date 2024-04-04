
query_creacion_bbdd = 'CREATE SCHEMA IF NOT EXISTS `tienda_pair` ;'


query_creacion_tabla_ventas = """CREATE TABLE IF NOT EXISTS `tienda_pair`.`ventas` (
                            `id_venta` INT NOT NULL AUTO_INCREMENT,
                            `id_producto` VARCHAR(45) NOT NULL,
                            `id_cliente` INT NOT NULL,
                            `fecha_venta` DATE NULL,
                            `cantidad` INT NULL,
                            `total` FLOAT NULL,
                            PRIMARY KEY (`id_venta`))
                            ENGINE = InnoDB;"""


query_creacion_tabla_clientes = """CREATE TABLE IF NOT EXISTS `tienda_pair`.`clientes` (
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
                                """

query_creacion_tabla_productos = """CREATE TABLE IF NOT EXISTS `tienda_pair`.`productos` (
                                `id_producto` VARCHAR(6) NOT NULL,
                                `nombre_producto` VARCHAR(100) NOT NULL,
                                `categoria` VARCHAR(100) NOT NULL,
                                `precio` FLOAT NOT NULL,
                                `origen` VARCHAR(50) NOT NULL,
                                `descripcion` VARCHAR(500) NOT NULL,
                                PRIMARY KEY (`id_producto`))
                                ENGINE = InnoDB;"""


query_creacion_productos_ventas = """CREATE TABLE IF NOT EXISTS `tienda_pair`.`productos_has_ventas` (
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
                                    ENGINE = InnoDB;"""

query_insertar_ventas = "INSERT INTO ventas (id_venta, id_producto, id_cliente, fecha_venta, cantidad, total) VALUES (%s, %s, %s, %s, %s, %s)"

query_insertar_clientes = "INSERT INTO clientes (id_cliente, first_name, last_name, email, gender, city, country, adress, ventas_id_venta) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

query_insertar_productos = "INSERT INTO productos (id_producto, nombre_producto, categoria, precio, origen, descripcion) VALUES (%s, %s, %s, %s, %s, %s)"

query_insertar_productos_ventas = "INSERT INTO productos_has_ventas(productos_id_producto, ventas_id_venta) VALUES (%s, %s)"