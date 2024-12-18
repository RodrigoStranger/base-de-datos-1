import os
from backend_users import *

def limpiar_pantalla(): os.system('cls' if os.name == 'nt' else 'clear')

def menu_gestion_personal():
    while True:
        limpiar_pantalla()
        print("=== Gestión de Personal ===")
        print("1. Gestión de Vendedores")
        print("2. Gestión de Asesores")
        print("3. Salir al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_gestion_vendedores()
        elif opcion == "2":
            menu_asesores()
        elif opcion == "3":
            print("Volviendo a la ventana principal...")
            input("Presione Enter para continuar...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def menu_gestion_vendedores():
    while True:
        limpiar_pantalla()
        print("=== Gestión de Vendedores ===")
        print("1. Agregar un vendedor")
        print("2. Editar datos de un vendedor")
        print("3. Inhabilitar o habilitar a un vendedor")
        print("4. Observar estadisticas generales")
        print("5. Volver a la Gestión de Personal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_vendedor_menu()
        elif opcion == "2":
            editar_vendedor_menu()
        elif opcion == "3":
            estado_vendedor_menu()
        elif opcion == "4":
            menu_estadisticas_vendedores()
        elif opcion == "5":
            print("Volviendo a la Gestión principal...")
            input("Presione Enter para continuar...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def agregar_vendedor_menu():
    limpiar_pantalla()
    print("=== Agregar un Vendedor ===")
    while True:
        dni = input("Ingrese el dni del nuevo vendedor: ")
        if len(dni) == 8 and dni.isdigit():
            if not persona_existe(dni):
                break
            else:
                print(f"El vendedor con dni {dni} ya existe en la base de datos. Intente nuevamente.")
        else:
            print("El dni debe tener exactamente 8 dígitos numéricos. Intente nuevamente.")
    while True:
        telefono = input("Ingrese el teléfono del nuevo vendedor: ")
        if len(telefono) == 9 and telefono.isdigit():
            if not telefono_existe(telefono):
                break
            else:
                print(f"El teléfono {telefono} ya existe en la base de datos. Intente nuevamente.")
        else:
            print("El teléfono debe tener exactamente 9 dígitos numéricos. Intente nuevamente.")
    rol = input("Ingrese el rol del vendedor (deje en blanco no asignar un rol): ").strip()
    if rol == "":
        rol = None
    insertar_vendedor(dni, telefono, rol)
    input("Presione Enter para continuar...")

def editar_vendedor_menu():
    limpiar_pantalla()
    print("=== Editar a un Vendedor ===")
    print("Vendedores disponibles:")
    mostrar_vendedores()
    while True:
        dni = input("Ingrese el DNI del vendedor: ")
        if len(dni) == 8 and dni.isdigit():
            if persona_existe(dni):
                break
            else:
                print(f"El vendedor con dni {dni} no existe en la base de datos. Intente nuevamente.")
        else:
            print("El dni debe tener exactamente 8 dígitos numéricos. Intente nuevamente.")
    while True:
        limpiar_pantalla()
        print(f"=== Vendedor {dni} ===")
        print("1. Editar teléfono actual")
        print("2. Editar dirección actual")
        print("3. Editar rol actual")
        print("4. Regresar a la Gestión de Vendedores")
        opcion_edicion = input("Seleccione una opción: ")
        if opcion_edicion == "1":
            while True:
                telefono_nuevo = input("Ingrese el nuevo teléfono: ")
                if len(telefono_nuevo) == 9 and telefono_nuevo.isdigit():
                    if not telefono_existe(telefono_nuevo):
                        editar_telefono(dni, telefono_nuevo)
                        break
                    else:
                        print(f"El teléfono {telefono_nuevo} ya existe en la base de datos. Intente nuevamente.")
                else:
                    print("El teléfono debe tener exactamente 9 dígitos numéricos. Intente nuevamente.")
        elif opcion_edicion == "2":
            direccion_nueva = input("Ingrese la nueva dirección: ")
            editar_direccion(dni, direccion_nueva)
        elif opcion_edicion == "3":
            rol_nuevo = input("Ingrese el nuevo rol del vendedor (deje en blanco si se requiere quitar el rol): ")
            if rol_nuevo.strip() == "":
                editar_rol_vendedor(dni, None)
            else:
                editar_rol_vendedor(dni, rol_nuevo)
        elif opcion_edicion == "4":
            print("Regresando a la Gestión de Vendedores...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
        input("Presione Enter para continuar...")

def estado_vendedor_menu():
    limpiar_pantalla()
    print("=== Inhabilitar o habilitar a un Vendedor ===")
    print("Vendedores disponibles:")
    mostrar_vendedores()
    print("Importante: el vendedor debe tener un contrato asosiado para poder modificar su estado.")
    while True:
        dni = input("Ingrese el dni del vendedor: ")
        if len(dni) == 8 and dni.isdigit():
            if persona_existe(dni):
                break
            else:
                print(f"El vendedor con dni {dni} no existe en la base de datos. Intente nuevamente.")
        else:
            print("El dni debe tener exactamente 8 dígitos numéricos. Intente nuevamente.")
    while True:
        limpiar_pantalla()
        print(f"=== Seleccione el nuevo estado del Vendedor {dni} ===")
        print("1. Habilitar (Activo)")
        print("2. Inhabilitar (Inactivo)")
        print("3. Regresar a la Gestión de Vendedores")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            cambiar_estado_vendedor(dni, 'activo')
            break
        elif opcion == "2":
            cambiar_estado_vendedor(dni, 'inactivo')
            break
        elif opcion == "3":
            print("Regresando a la Gestión de Vendedores...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
    input("Presione Enter para continuar...")

def menu_asesores():
    while True:
        limpiar_pantalla()
        print("=== Gestión de Asesores ===")
        print("1. Agregar un Asesor")
        print("2. Editar datos de un Asesor")
        print("3. Inhabilitar o habilitar a un Asesor")
        print("4. Observar estadisticas generales")
        print("5. Volver a la Gestión de Personal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_asesor_menu()
        elif opcion == "2":
            editar_asesor_menu()
        elif opcion == "3":
            estado_asesor_menu()
        elif opcion == "4":
            menu_estadisticas_asesores()
        elif opcion == "5":
            print("Volviendo a la Gestión principal...")
            input("Presione Enter para continuar...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            input("Presione Enter para continuar...")

def agregar_asesor_menu():
    limpiar_pantalla()
    print("=== Agregar un Asesor ===")
    while True:
        dni = input("Ingrese el dni del nuevo asesor: ")
        if len(dni) == 8 and dni.isdigit():
            if not persona_existe(dni):
                break
            else:
                print(f"El asesor con dni {dni} ya existe en la base de datos. Intente nuevamente.")
        else:
            print("El dni debe tener exactamente 8 dígitos numéricos. Intente nuevamente.")
    while True:
        telefono = input("Ingrese el teléfono del nuevo asesor: ")
        if len(telefono) == 9 and telefono.isdigit():
            if not telefono_existe(telefono):
                break
            else:
                print(f"El teléfono {telefono} ya existe en la base de datos. Intente nuevamente.")
        else:
            print("El teléfono debe tener exactamente 9 dígitos numéricos. Intente nuevamente.")
    while True:
        try:
            experiencia = int(input("Ingrese los años de experiencia del Asesor (debe ser mayor a 0): "))
            if experiencia > 0:
                break
            else:
                print("La experiencia debe ser un número mayor a 0. Intente nuevamente.")
        except ValueError:
            print("La experiencia debe ser un número válido. Intente nuevamente.")
    while True:
        especialidad = input("Ingrese la especialidad del Asesor: ").strip()
        if especialidad:
            break
        else:
            print("La especialidad no puede estar vacía. Intente nuevamente.")
    insertar_asesor(dni, telefono, experiencia, especialidad)
    input("Presione Enter para continuar...")

def editar_asesor_menu():
    limpiar_pantalla()
    print("=== Editar un Asesor ===")
    print("Asesores disponibles:")
    mostrar_asesores()
    while True:
        dni = input("Ingrese el dni del asesor: ")
        if len(dni) == 8 and dni.isdigit():
            if persona_existe(dni):
                break
            else:
                print(f"El asesor con dni {dni} no existe en la base de datos. Intente nuevamente.")
        else:
            print("El dni debe tener exactamente 8 dígitos numéricos. Intente nuevamente.")
    while True:
        limpiar_pantalla()
        print(f"=== Asesor {dni} ===")
        print("1. Editar teléfono")
        print("2. Editar dirección")
        print("3. Editar especialidad")
        print("4. Editar experiencia")
        print("5. Regresar a la Gestión de Asesores")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            while True:
                telefono_nuevo = input("Ingrese el nuevo teléfono: ")
                if len(telefono_nuevo) == 9 and telefono_nuevo.isdigit():
                    if not telefono_existe(telefono_nuevo):
                        editar_telefono(dni, telefono_nuevo)
                        print(f"Teléfono actualizado correctamente para el asesor con DNI {dni}.")
                        break
                    else: print(f"El teléfono {telefono_nuevo} ya existe en la base de datos. Intente nuevamente.")
                else: print("El teléfono debe tener exactamente 9 dígitos numéricos. Intente nuevamente.")
        elif opcion == "2":
            direccion_nueva = input("Ingrese la nueva dirección: ").strip()
            if direccion_nueva:
                editar_direccion(dni, direccion_nueva)
            else:
                print("La dirección no puede estar vacía. Intente nuevamente.")
        elif opcion == "3":
            especialidad_nueva = input("Ingrese la nueva especialidad: ").strip()
            if especialidad_nueva:
                editar_especialidad_asesor(dni, especialidad_nueva)
            else:
                print("La especialidad no puede estar vacía. Intente nuevamente.")
        elif opcion == "4":
            while True:
                try:
                    experiencia_nueva = int(input("Ingrese la nueva experiencia (años, debe ser mayor a 0): "))
                    if experiencia_nueva > 0:
                        editar_experiencia_asesor(dni, experiencia_nueva)
                        break
                    else:
                        print("La experiencia debe ser un número mayor a 0. Intente nuevamente.")
                except ValueError:
                    print("La experiencia debe ser un número válido. Intente nuevamente.")
        elif opcion == "5":
            print("Regresando al menú principal...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
        input("Presione Enter para continuar...")

def estado_asesor_menu():
    limpiar_pantalla()
    print("=== Inhabilitar o habilitar a un Asesor ===")
    print("Asesores disponibles:")
    mostrar_asesores()
    print("Importante: el asesor debe tener un contrato asosiado para poder modificar su estado.")
    while True:
        dni = input("Ingrese el dni del asesor: ")
        if len(dni) == 8 and dni.isdigit():
            if persona_existe(dni):
                break
            else: print(f"El asesor con dni {dni} no existe en la base de datos. Intente nuevamente.")
        else: print("El dni debe tener exactamente 8 dígitos numéricos. Intente nuevamente.")
    while True:
        limpiar_pantalla()
        print(f"=== Seleccione el nuevo estado del Asesor {dni} ===")
        print("1. Habilitar (Activo)")
        print("2. Inhabilitar (Inactivo)")
        print("3. Regresar a la Gestión de Asesores")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            cambiar_estado_asesor(dni, 'activo')
            break
        elif opcion == "2":
            cambiar_estado_asesor(dni, 'inactivo')
            break
        elif opcion == "3":
            print("Regresando la Gestión de Asesores...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
    input("Presione Enter para continuar...")

def menu_estadisticas_vendedores():
    while True:
        limpiar_pantalla()
        print("=== Estadísticas de Vendedores ===")
        print("1. Mostrar los vendedores con más ventas")
        print("2. Mostrar los vendedores con menos ventas")
        print("3. Mostrar los productos más vendidos por cada vendedor")
        print("4. Mostrar la cantidad de clientes atendidos por cada vendedor")
        print("5. Salir a la Gestión de Vendedores")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_top_vendedores()
        elif opcion == "2":
            mostrar_vendedores_con_menos_ventas()
        elif opcion == "3":
            mostrar_productos_mas_vendidos_por_vendedor()
        elif opcion == "4":
            mostrar_clientes_atendidos_por_vendedor()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
        input("Presione Enter para continuar...")

def menu_estadisticas_asesores():
    while True:
        limpiar_pantalla()
        print("=== Gestión de Estadísticas para Asesores ===")
        print("1. Ver asesores con más clientes atendidos")
        print("2. Ver ingresos generados por asesores")
        print("3. Ver productos más recomendados por asesores")
        print("4. Evaluar el impacto de la experiencia de asesores")
        print("5. Salir a la Gestión de Asesores")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_asesores_con_mas_clientes()
        elif opcion == "2":
            mostrar_ingresos_generados_por_asesores()
        elif opcion == "3":
            mostrar_productos_mas_recomendados_por_asesores()
        elif opcion == "4":
            mostrar_impacto_experiencia_asesores()
        elif opcion == "5":
            print("Saliendo del menú de estadísticas para asesores...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
        input("Presione Enter para continuar...")