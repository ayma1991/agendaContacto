agenda=[]
while True:
    print("""MENU DE OPCIONES:
          [1] Agregar contactos.
          [2] Borrar contactos.
          [3] Modificar contactos.
          [4] Mostrar contactos.
          [5] Salir.
          
           """)
    opcion=input("Seleccione una opcion:")
    if opcion == "1":
       while True: 
           nombre=input("Ingrese el nombre del contacto: ")
           if nombre.strip():
              telefono=int(input("Ingrese el numero: ")) 
              nuevo_contacto = {"nombre":nombre, "numero":telefono}
              agenda.append(nuevo_contacto)    
              print("Contancto agregado con exito.")
              break
           else: 
              print("Ingrese un nombre valido")    
    if opcion == "2": 
       contacto_eliminar=input("Ingrese el nombre del contacto que quiera eliminar: ") 
       for contacto in agenda:
          if contacto.get('nombre') == contacto_eliminar:
             agenda.remove(contacto)
             print("Contacto borrado con exito. ")
          else:
            print("El contacto no existe. ")
    if opcion == "3":
       modificar_contacto=input("Ingrese el nombre del contacto que quiera modificar: ")
       for contacto in agenda:
          if contacto.get('nombre')==modificar_contacto:
            nuevo_numero=input("Ingrese el numero numero: ") 
            print("El contacto ha sido modificado con exito. ")
          else:
           print("El nombre ingresado es invalido. ")  
    if opcion == "4":
       if len(agenda) == 0:
          print("La lista de contactos se encuentra vacia.")
       else:
        for contacto in agenda:
            print("Nombre: " + contacto['nombre'] + " --- " + "Numero: " + str(contacto['numero']))        
    elif opcion == "5":
       print("Saliendo...")
       break
   
   
       

    
    
    
    
    
      
       
      
          
   
