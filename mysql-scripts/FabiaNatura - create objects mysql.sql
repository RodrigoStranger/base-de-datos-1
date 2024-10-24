USE FabiaNatura;

-- Tabla de personas
CREATE TABLE Personas (
    dni VARCHAR(8) NOT NULL PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    apellido_paterno VARCHAR(20) NOT NULL,
    apellido_materno VARCHAR(20) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    fecha_registro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Correos de personas
CREATE TABLE Correos_Persona (
    id_correo VARCHAR(10) NOT NULL PRIMARY KEY,
    dni VARCHAR(8) NOT NULL,
    correo VARCHAR(50),
    FOREIGN KEY (dni) REFERENCES Personas(dni) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Telefonos de personas
CREATE TABLE Telefonos_Persona (
	telefono VARCHAR(9) NOT NULL PRIMARY KEY,
    dni VARCHAR(8) NOT NULL,
    FOREIGN KEY (dni) REFERENCES Personas(dni) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Direcciones de personas
CREATE TABLE Direcciones_Persona (
    id_direccion VARCHAR(10) NOT NULL PRIMARY KEY,
    dni VARCHAR(8) NOT NULL,
    direccion VARCHAR(100),
    FOREIGN KEY (dni) REFERENCES Personas(dni) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Empleados, con codigo en formato VARCHAR (EMP0X)
CREATE TABLE Empleados (
    cod_empleado VARCHAR(10) PRIMARY KEY,
    dni VARCHAR(8) NOT NULL,
    FOREIGN KEY (dni) REFERENCES Personas(dni) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Contratos, con codigo en formato VARCHAR (CTR0X)
CREATE TABLE Contratos (
    cod_contrato VARCHAR(10) PRIMARY KEY,
    cod_empleado VARCHAR(10) NOT NULL UNIQUE,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE,
    salario_men FLOAT NOT NULL,
    observaciones TEXT,
    FOREIGN KEY (cod_empleado) REFERENCES Empleados(cod_empleado) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Vendedores, con codigo en formato VARCHAR (VEND0X)
CREATE TABLE Vendedores (
    cod_vendedor VARCHAR(10) PRIMARY KEY,
    cod_empleado VARCHAR(10) NOT NULL,
    rol VARCHAR(20),
    FOREIGN KEY (cod_empleado) REFERENCES Empleados(cod_empleado) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Asesores, con codigo en formato VARCHAR (ASE0X)
CREATE TABLE Asesores (
    cod_asesor VARCHAR(10) PRIMARY KEY,
    cod_empleado VARCHAR(10) NOT NULL,
    años_experiencia INT NOT NULL,
    especialidad VARCHAR(20) NOT NULL,
    FOREIGN KEY (cod_empleado) REFERENCES Empleados(cod_empleado) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Clientes
CREATE TABLE Clientes (
    dni VARCHAR(8) NOT NULL PRIMARY KEY,
    tipo_cliente VARCHAR(20),
    FOREIGN KEY (dni) REFERENCES Personas(dni) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Proveedores
CREATE TABLE Proveedores (
    ruc VARCHAR(15) NOT NULL PRIMARY KEY,
    nombre VARCHAR(50) UNIQUE NOT NULL,
    fecha_registro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Telefonos de proveedores
CREATE TABLE Telefonos_Proveedor (
    ruc VARCHAR(15) NOT NULL,
    telefono VARCHAR(15) NOT NULL PRIMARY KEY,
    FOREIGN KEY (ruc) REFERENCES Proveedores(ruc) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Direcciones de proveedores
CREATE TABLE Direcciones_Proveedor (
    id_direccion VARCHAR(10) NOT NULL PRIMARY KEY,
    ruc VARCHAR(15) NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    FOREIGN KEY (ruc) REFERENCES Proveedores(ruc) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Correos de proveedores
CREATE TABLE Correos_Proveedor (
    id_correo VARCHAR(10) NOT NULL PRIMARY KEY,
    ruc VARCHAR(15) NOT NULL,
    correo VARCHAR(50) NOT NULL,
    FOREIGN KEY (ruc) REFERENCES Proveedores(ruc) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Categorias, con codigo en formato VARCHAR (CAT0X)
CREATE TABLE Categorias (
    cod_categoria VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    descripcion TEXT,
    fecha_registro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Productos, con codigo en formato VARCHAR (PROD0X)
CREATE TABLE Productos (
    cod_producto VARCHAR(10) PRIMARY KEY,
    cod_categoria VARCHAR(10) NOT NULL,
    ruc VARCHAR(15) NOT NULL,
    nombre VARCHAR(100) UNIQUE NOT NULL,
    linea VARCHAR(100),
    descripcion TEXT,
    precio_compra FLOAT NOT NULL,
    precio_venta FLOAT NOT NULL,
    stock INT NOT NULL,
    fecha_registro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cod_categoria) REFERENCES Categorias(cod_categoria) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (ruc) REFERENCES Proveedores(ruc) ON UPDATE CASCADE ON DELETE NO ACTION
);

-- Facturas
CREATE TABLE Facturas (
    cod_factura VARCHAR(10) PRIMARY KEY,
    dni VARCHAR(8) NOT NULL,
    cod_vendedor VARCHAR(10) NOT NULL,
    cod_asesor VARCHAR(10),
    fecha_registro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (dni) REFERENCES Clientes(dni) ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY (cod_vendedor) REFERENCES Vendedores(cod_vendedor) ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY (cod_asesor) REFERENCES Asesores(cod_asesor) ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- Detalles de facturas
CREATE TABLE Det_Facturas (
    cod_factura VARCHAR(10) NOT NULL,
    cod_producto VARCHAR(10) NOT NULL,
    cantidad INT NOT NULL,
    PRIMARY KEY (cod_factura, cod_producto),
    FOREIGN KEY (cod_factura) REFERENCES Facturas(cod_factura) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (cod_producto) REFERENCES Productos(cod_producto) ON DELETE CASCADE ON UPDATE CASCADE
);