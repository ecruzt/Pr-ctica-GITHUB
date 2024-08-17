## Función para validar entradas del usuario
def readUserInput(output, dataType):
    '''
    Description:
        Función para validar las entradas del usuario.

    parameters:
        - output: str (mensaje para solicitar la entrada del usuario)
        - dataType: type (tipo de dato esperado para la entrada del usuario)

    return:
        - result: dataType (entrada del usuario convertida al tipo de dato especificado)
    '''
    while True:
        user_input = input(output)
        try: 
            result = dataType(user_input)
            break
        except ValueError:
            print(f"Error: '{user_input}' no es un valor válido para {dataType.__name__}. Por favor, intenta de nuevo.")
    return result


class Paciente:
    def __init__(self):
        self.nombre = ""
        self.cedula = 0
        self.genero = ""
        self.servicio = ""

    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula

    def asignarNombre(self,n):
        self.__nombre = n
    def asignarServicio(self,s):
        self.__servicio = s
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

class Sistema:
    def __init__(self):
    #lista contenedora de pacientes
        self.__lista_pacientes=[]
        #Dependera del tamano no modificable con metodo asignar
        self.__numero_pacientes = len(self.__lista_pacientes)

    #1. solicitar informacion
    def ingresarPacientes(self):
        name = readUserInput("Ingrese el nombre: ", str)
        id = readUserInput("Ingrese la cédula: ", int)
        genero = readUserInput("Ingrese el genero: ", str)
        servicio = readUserInput("Ingre el servicio: ", str)
    #2. crear objeto paciente y asignar los datos
        p = Paciente()
        p.asignarNombre(name)
        p.asignarCedula(id)
        p.asignarGenero(genero)
        p.asignarServicio(servicio)
    #3. guardar en la lisra de pacientes
        self.__lista_pacientes.append(p)
    #4. actualizar cantidad de pacientes en el sistema
        self.__numero_pacientes = len(self.__lista_pacientes)
    
    def verNumeroPacientes(self):
        return self.__numero_pacientes
    
    def verDatosPaciente(self):
        cedula = readUserInput("Ingrese la cedula a buscar: ", int)
    #cedula in self. lista_pacientes: no sirve porque en la lista

        for paciente in self .__lista_pacientes:
            if cedula == paciente.verCedula():
    #si coincide la cedula del paciente con la buscada
    # muestro los datos
                print("Nombre: " + paciente.verNombre())
                print("Cedula: "+ str(paciente.verCedula()))
                print("Genero: "+ paciente.verGenero())
                print("Servicio: "+ paciente.verServicio())


#cuando creamos las clases podemos generar objetos de esas clases y con esos objetos
#acceder a las funcionalidades o metodos
mi_sistema = Sistema() # Se Crea una instancia de la clase Sistema.

#ciclo infinito
while True:
    opcion = readUserInput("\n1. Nuevo Paciente\n2. Numero de Pacientes\n3. Datos Paciente\n4. Salir\n", int)
    if opcion == 1:
        mi_sistema.ingresarPacientes()
    elif opcion == 2:
        print("Ahora hay: "+ str(mi_sistema. verNumeroPacientes()))
    elif opcion == 3:
        mi_sistema.verDatosPaciente()
    elif opcion == 4:
        break
    else:
        print("Opcion invalida")

