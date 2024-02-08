# Pre: Se presupone que el programa dara inicio a principios de año y de cada semana

# Comenzamos creando las variables que se crean necesarias


Semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

Meses = ["Enero", "Febrero", "Marzo", "Mayo", "Abril", "Julio", "Junio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

Enero = 31

Febrero = 29

Marzo = 31

Mayo = 30

Abril = 31

Julio = 30

Junio = 31

Agosto = 30

Septiembre = 31

Octubre = 30

Noviembre = 31

Diciembre = 30

Inicio_Año = ( 1, "de", "Enero")







# Primera parte del codigo: Creamos lo que sera el funcionamiento del menu.

while True:
    Temperatura_media = None
    Diferencia_max = None

    print("Bienvenido al registro de temperaturas")
    print()
    print("!RT!: Registrar temperatura semanal")
    print("!MJ!: Consultar temperatura media")
    print("!DF!: Consultar diferencia maxima")
    print("!FI!: Salir del programa")
    print()

    eleccion = str(input("Por favor selecciona una opcion >> "))
    eleccion = eleccion.lower() # Converitmos el string dado por el user a minusculas para que no sea keysensitive

    if eleccion == "rt": # Contenido de la opcion 1
        Temperaturas = input("Escribe las temperaturas de esta semana: ")        
        print()
        print(Temperaturas)
            
            
            
            
            
    elif eleccion == "mj": # Contenido de la opcion 2
    
        if Temperatura_media is None:
            print("No hay temperaturas registradas, por favor registrelas")






    elif eleccion == "df": # Contenido de la opcion 3 
        if Diferencia_max is None:
            print("No hay registros de temperatura")






    elif eleccion == "fi": # Contenido de la opcion 4
        print("Saliendo del programa...")
        
        
        
        
        
        
    else:
        print("Opcion no valida, por favor seleccione una opcion valida.")
        
    print(eleccion)