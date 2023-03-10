import re
import datetime
from tabulate import tabulate

patron_texto="^[A-Z ]{1,40}$"
patron_ISBN="^[0-9]{10}$"
patron_fecha="^([0-9]{2}[/][0-9]{2}[/][0-9]{4})|([0-9]{1}[/][0-9]{2}[/][0-9]{4})|([0-9]{2}[/][0-9]{1}[/][0-9]{4})|([0-9]{1}[/][0-9]{1}[/][0-9]{4})$"

#ejemplares={}
#FORMATO DE ejemplares={1:["Titulo","Autor","Genero","Año de publicacion",ISBN,"Fecha de adquisicion"]}
ejemplares={1: ['EL PRINCIPITO', 'ANTOINE', 'NOVELA CORTA', '6/4/1943', 4235436343, '5/1/2023'],
        2: ['FRANKENSTEIN', 'MARY', 'CIENCIA FICCION', '1/1/1818', 5877347832, '15/12/2022'],
        3: ['CREPUSCULO', 'STEPHENIE', 'FANTASIA', '5/10/2005', 3758296343, '1/1/2015']}
datos_tabla_libreria=[]

#FUNCION PARA CAPTURAR DATOS
def captura_ejemplar(Titulo="",Autor="",Genero="",f_publi="",Fecha_Publicacion="",isbn_="",ISBN="",f_adqui="",Fecha_Adquisicion=""):
    print("")
    while True:
        if(Titulo.strip() == ""):
                Titulo=input("Dame el titulo del libro: ")
                if(not(re.match(patron_texto,Titulo))):
                    print("Titulo no admitido")
                    Titulo=""
                    continue
        else:
            pass

        if(Autor.strip() == ""):
                Autor=input("Dame el autor del libro: ")
                if(not(re.match(patron_texto,Autor))):
                    print("Autor no admitido")
                    Autor=""
                    continue
        else:
            pass

        if(Genero.strip() == ""):
                Genero=input("Dame el genero del libro: ")
                if(not(re.match(patron_texto,Genero))):
                    print("Genero no admitido")
                    Genero=""
                    continue 
        else:
            pass

        if(f_publi.strip() == "" and Fecha_Publicacion.strip() == ""):
                f_publi=input("Dame la fecha de publicacion: ")
                if(not(re.match(patron_fecha,f_publi))):
                    print("Fecha no admitida.")
                    f_publi=""
                    Fecha_Publicacion=""
                    continue
                try:
                    Fecha_Publicacion = datetime.datetime.strptime(f_publi, "%d/%m/%Y").date()
                except:
                    print("La fecha proporcionada no es valida.")
                    f_publi=""
                    Fecha_Publicacion=""
                    continue
        else:
            pass


        if(isbn_.strip() == "" and ISBN.strip() == ""):
                isbn_=input("Dame el ISBN del libro: ")
                if(not(re.match(patron_ISBN,isbn_))):
                    print("Valor no admitido.")
                    isbn_=""
                    ISBN=""
                    continue
                ISBN=int(isbn_)
        else:
            pass

        if(f_adqui.strip() == "" and Fecha_Adquisicion.strip() == ""):
                f_adqui=input("Dame la fecha de Adquisicion: ")
                if(not(re.match(patron_fecha,f_adqui))):
                    print("Fecha no admitida.")
                    f_adqui=""
                    Fecha_Adquisicion=""
                    continue
                try:
                    Fecha_Adquisicion = datetime.datetime.strptime(f_adqui, "%d/%m/%Y").date()
                    
                except:
                    print("La fecha proporcionada no es valida.")
                    f_adqui=""
                    Fecha_Adquisicion=""
                    continue
        ejemplares[clave]=[Titulo,Autor,Genero,Fecha_Publicacion.strftime('%d/%m/%Y'),ISBN,Fecha_Adquisicion.strftime('%d/%m/%Y')]
        break

#FUNCIONES DE CONSULTA DE TITULO E ISBN
def busqueda_titulo():
    print("")
    B_Titulo=input("Que Titulo desea buscar: ")
    print("")
    encontrado = False
    for Clave,Titulo,Autor,Genero,Año_de_publicacion,ISBN,Fecha_de_adquisicion in datos_tabla_libreria:
        if (B_Titulo == Titulo):
            encontrado = True
            print("\tRegistro encontrado")
            print("-"*40)
            print(f"Clave             : {Clave}")
            print(f"Titulo            : {Titulo}")  
            print(f"Autor             : {Autor}")
            print(f"Genero            : {Genero}")
            print(f"Fecha Publicacion : {Año_de_publicacion}")
            print(f"ISBN              : {ISBN}")
            print(f"Fecha Adquisicion : {Fecha_de_adquisicion}")
            print("")
            break
    if (encontrado == False):
        print("LO BUSCADO NO ESTA REGISTRADO")

def busqueda_ISBN():
    print("")
    while True:
        try:
            B_ISBN=int(input("Que ISBN desea buscar: "))
            break
        except:
            print("El ISBN INGRESADO NO ES VALIDO (SOLO DIGITOS)")
    print("")
    encontrado = False
    for Clave,Titulo,Autor,Genero,Año_de_publicacion,ISBN,Fecha_de_adquisicion in datos_tabla_libreria:
        if (B_ISBN == ISBN):
            encontrado = True
            print("\tRegistro encontrado")
            print("-"*40)
            print(f"Clave             : {Clave}")
            print(f"Titulo            : {Titulo}")  
            print(f"Autor             : {Autor}")
            print(f"Genero            : {Genero}")
            print(f"Fecha Publicacion : {Año_de_publicacion}")
            print(f"ISBN              : {ISBN}")
            print(f"Fecha Adquisicion : {Fecha_de_adquisicion}")
            print("")
            break
    if (encontrado == False):
        print("LO BUSCADO NO ESTA REGISTRADO")
               
while True:
    print("")
    print("*"*40)
    print("*******      Menu principal      *******")
    print("*"*40)
    print("1.-Registrar Nuevo Ejemplar\n2.-Consulta y Reportes\n3.-Salir")
    print("*"*40)
    
    try: 
        opcion_principal=int(input("¿Que opcion desea?: "))
    except:
        print("El valor ingresado no es entero")
        continue
        
    if (opcion_principal==1):
        clave=max(ejemplares,default=0)+1
        captura_ejemplar()

    if (opcion_principal==2):
        while True:
            print("")
            print("*"*40)
            print("*****  Menu Consultas y Reportes   *****")
            print("*"*40)
            print("1.-Consulta del titulo\n2.-Reportes\n3.-Volver al Menu principal")
            print("*"*40)
            try:
                opcion_consultas_Reportes=int(input("¿Que opcion desea?: "))
            except:
                print("El valor ingresado no es entero")
                continue
                
            if (opcion_consultas_Reportes==1):
                while True:
                    print("")
                    print("*"*40)
                    print("*******   Menu Consulta Titulo   *******")
                    print("*"*40)
                    print("1.-Por Titulo\n2.-Por ISBN\n3.-Volver al Menu principal")
                    print("*"*40)
                    try:
                        opcion_consulta_titulo=int(input("¿Que opcion desea?: "))
                    except:
                        print("El valor ingresado no es entero")
                        continue
                     
                    if (opcion_consulta_titulo==1):
                        datos_tabla_libreria=[[clave] + datos for clave,datos in ejemplares.items()]
                        busqueda_titulo()  
                        

                    if (opcion_consulta_titulo==2):
                        datos_tabla_libreria=[[clave] + datos for clave,datos in ejemplares.items()]
                        busqueda_ISBN()
                    
                    if (opcion_consulta_titulo==3):
                        break
                    
                    if (opcion_consulta_titulo>3 or opcion_consulta_titulo<1):
                        print("*"*40)
                        print("Opcion fuera del rango.")
                        continue
                
            if (opcion_consultas_Reportes==2):
                while True:
                    print("")
                    print("*"*40)
                    print("**********   Menu Reportes    **********")
                    print("*"*40)
                    print("1.-Catalogo Completo\n2.-Reporte por Autor\n3.-Reporte por genero\n4.-Reporte por Año de Publicacion\n5.-Volver al Menu principal")
                    print("*"*40)
                    
                    try:
                        opcion_reportes=int(input("¿Que opcion desea?: "))
                    except:
                        print("El valor ingresado no es entero")
                        continue
                    
                    if (opcion_reportes==1):
                        if(len(ejemplares)==0):
                            print("")
                            print("No hay registros.")
                            print("")
                            continue
                        else:
                            datos_tabla_libreria=[[clave] + datos for clave,datos in ejemplares.items()]
                            columnas=("Identificador","Titulo","Autor","Genero","Año de publicacion","ISBN","Fecha de adquisicion")
                            print(tabulate(datos_tabla_libreria,headers=columnas,tablefmt="grid")) 
                        
                    if (opcion_reportes==2):
                        if(len(ejemplares)==0):
                            print("")
                            print("No hay registros.")
                            print("")
                            continue
                        else:
                            buscar_autor=input("Dame el autor: ").upper()
                            datos_tabla_libreria=[[clave] + datos for clave,datos in ejemplares.items()]
                            datos_tabla_autor=[]

                            for Identificador,Titulo,Autor,Genero,Añodepublicacion,ISBN,Fechadeadquisicion in datos_tabla_libreria:
                                if buscar_autor == Autor:
                                    datos_tabla_autor.append([Autor,Titulo,Genero,Añodepublicacion,ISBN,Fechadeadquisicion])
                            if(len(datos_tabla_autor)==0):
                                print("NO HAY AUTORES QUE COINCIDA CON EL NOMBRE")
                            else:
                                columnas=("Autor","Titulo","Genero","Año de publicacion","ISBN","Fecha de adquisicion")
                                print(tabulate(datos_tabla_autor,headers=columnas,tablefmt="grid")) 
                    if (opcion_reportes==3):
                        if(len(ejemplares)==0):
                            print("")
                            print("No hay registros.")
                            print("")
                            continue
                        else:
                            buscar_genero=input("Dame el Genero: ").upper()
                            datos_tabla_libreria=[[clave] + datos for clave,datos in ejemplares.items()]
                            datos_tabla_genero=[]

                            for Identificador,Titulo,Autor,Genero,Añodepublicacion,ISBN,Fechadeadquisicion in datos_tabla_libreria:
                                if buscar_genero == Genero:
                                    datos_tabla_genero.append([Genero,Titulo,Autor,Añodepublicacion,ISBN,Fechadeadquisicion])
                            if(len(datos_tabla_genero)==0):
                                print("NO HAY GENEROS QUE COINCIDA CON EL NOMBRE")
                            else:
                                columnas=("Genero","Titulo","Autor","Año de publicacion","ISBN","Fecha de adquisicion")
                                print(tabulate(datos_tabla_genero,headers=columnas,tablefmt="grid")) 
                        
                    if (opcion_reportes==4):
                        if(len(ejemplares)==0):
                            print("")
                            print("No hay registros.")
                            print("")
                            continue
                        else:
                            buscar_Año_Publicacion=input("Dame el Año de Publicacion: ").upper()
                            datos_tabla_libreria=[[clave] + datos for clave,datos in ejemplares.items()]
                            datos_tabla_Año_Publicacion=[]

                            for Identificador,Titulo,Autor,Genero,Añodepublicacion,ISBN,Fechadeadquisicion in datos_tabla_libreria:
                                if buscar_Año_Publicacion == Añodepublicacion:
                                    datos_tabla_Año_Publicacion.append([Añodepublicacion,Titulo,Autor,Genero,ISBN,Fechadeadquisicion])
                            if(len(datos_tabla_Año_Publicacion)==0):
                                print("NO HAY AUTORES QUE COINCIDA CON EL NOMBRE")
                            else:
                                columnas=("Año Publicacion","Titulo","Autor","Genero","ISBN","Fecha de adquisicion")
                                print(tabulate(datos_tabla_Año_Publicacion,headers=columnas,tablefmt="grid")) 
                        
                    if (opcion_reportes==5):
                        break
                        
                    if (opcion_reportes>5 or opcion_reportes<1):
                        print("*"*40)
                        print("Opcion fuera del rango.")
                        continue
               
            if (opcion_consultas_Reportes==3):
                break   
            if (opcion_consultas_Reportes>3 or opcion_consultas_Reportes<1):
                print("*"*40)
                print("Opcion fuera del rango.")
                continue
      
    if (opcion_principal==3):
        break
     
    if (opcion_principal>3 or opcion_principal<1):
        print("*"*40)
        print("Opcion fuera del rango.")
        continue