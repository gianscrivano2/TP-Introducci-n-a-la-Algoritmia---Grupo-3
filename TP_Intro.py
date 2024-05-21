def lista_clientes(clientes, cant_horas, precio, precio_promedio): #Pide DNI, llama a funcion "dni_repetido" y despues llama a las otras funciones para pedir el timepo y calcular los valores

    dni=int(input("Ingrese DNI o -1 para finalizar: "))
    while dni!=-1:
        if dni>=5000000 and dni<=99000000: #Chequea que DNI este dentro de los valores aceptados
            repetido, pos=dni_repetido(clientes, dni) #Llamamos a la 
            if repetido:
                cant_horas, precio, precio_promedio=valores_repetidos(pos, cant_horas, precio, precio_promedio)
                dni=int(input("Ingrese DNI o -1 para finalizar: "))
            else:
                clientes.append(dni)
                cant_horas, precio, precio_promedio=pedir_hora_y_calcular_valor(cant_horas, precio, precio_promedio)
                dni=int(input("Ingrese DNI o -1 para finalizar: "))
        else:
            dni=int(input("DNI inválido. Ingrese DNI válido: "))
        
    
    return clientes, cant_horas, precio, precio_promedio

def pedir_hora_y_calcular_valor(cant_horas, precio, precio_promedio): #Ingresa cantidad de horas que se quedo en el estacionamiento y calcula los valores

    hrs=float(input("Ingrese cantidad de horas que se quedó: "))
    if hrs!=int(hrs):
        hrs=int(hrs)+1   #Esto convierte a los float en enteros y los redondea para arriba
    while hrs<1 or hrs>24: #Cheque que el valor esté entre 1 y 24
        hrs=float(input("Ingrese una cantidad de horas válida: "))
        if hrs!=int(hrs):
            hrs=int(hrs)+1 #Convierte a los float en enteros y los redondea para arriba
    cant_horas.append(hrs) #Añade a la lista cant_horas
    
    if hrs==1:
        valor=300
    elif hrs>1 and hrs<5:
        valor=(hrs*200)+100 #El +100 es xq la primera hora sale 300
    else:
        valor=800
    precio.append(valor) #Añade el valor a la lista precio 
    prom_por_hora=valor/hrs #Calcula el promedio
    precio_promedio.append(prom_por_hora) #Añade el promedio a la lista

    return cant_horas, precio, precio_promedio

def dni_repetido(clientes, dni): #Devuelve True si el dni ingresado ya esta en la lista, False si no lo está

    for i in range(len(clientes)):    
            if clientes[i]==dni:
                    return True, i    #Cheque si hay un dni repetido y nos devuelve en que posicion se encuentra
            
    return False, 0                   #El 0 es para que no salte error

def valores_repetidos(pos, cant_horas, precio, precio_promedio): #Funcion para aquellos dnis que ya fueron ingresados

    hrs=float(input("Ingrese cantidad de horas que se quedó: "))
    if hrs!=int(hrs):
        hrs=int(hrs)+1
    while hrs<1 or hrs>24:
        hrs=float(input("Ingrese una cantidad de horas válida: "))
        if hrs!=int(hrs):
            hrs=int(hrs)+1
    cant_horas[pos]+=hrs

    hrs=cant_horas[pos]
    if hrs==1:
        hrs=300
    elif hrs>1 and hrs<5:
        valor=(hrs*200)+100+100 #Se le suman 100 mas debido a que cuanto ingresa de nuevo no se tienen en cuenta los 300 de la primera hora
    else:
        valor=800
    
    precio[pos]=valor
    prom_por_hora=valor/hrs
    precio_promedio[pos]=prom_por_hora

    return cant_horas, precio, precio_promedio

def  ordenar_por_valor(clientes, cant_horas, precio, precio_promedio): #Ordena todas las listas en base de la lista precio

    desordenado=True                           #Usamos el metodo de burbujeo en las 4 listas en simultaneo
    while desordenado:
        desordenado=False
        for i in range(len(precio)-1):
            if precio[i]<precio[i+1]:
                aux=precio[i]
                precio[i]=precio[i+1]
                precio[i+1]=aux

                aux=clientes[i]
                clientes[i]=clientes[i+1]
                clientes[i+1]=aux

                aux=cant_horas[i]
                cant_horas[i]=cant_horas[i+1]
                cant_horas[i+1]=aux

                aux=precio_promedio[i]
                precio_promedio[i]=precio_promedio[i+1]
                precio_promedio[i+1]=aux

                desordenado=True

    return clientes, cant_horas, precio, precio_promedio

def imprimir(clientes, cant_horas, precio, precio_promedio): #Imprime todos los valores
    for i in range(len(clientes)):
        print(f"DNI: {clientes[i]}. Cantidad de horas: {cant_horas[i]}. Precio total: {precio[i]}. Promedio por hora: {precio_promedio[i]}.")

clientes=[]
cant_horas=[]
precio=[]
precio_promedio=[]

clientes, cant_horas, precio, precio_promedio=lista_clientes(clientes, cant_horas, precio, precio_promedio)
clientes, cant_horas, precio, precio_promedio=ordenar_por_valor(clientes, cant_horas, precio, precio_promedio)
imprimir(clientes, cant_horas, precio, precio_promedio)


            






















