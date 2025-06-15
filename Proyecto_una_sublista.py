#Se usa una sub-lista 
#productos = [[nombre, categoria, precio], [nombre, categoria, precio]]
#Cada sub-lista ocupa una posición, conteniendo los valores del producto
#para eliminar por la posición usando.pop() se imprime una lista ordenada y numerada 
#con esa lista como guía, se solicita el ingreso de la ubicación, un número que va a ubicar a la sub-lista que contiene [nombre, categoria, precio] a borrar 


#falla. dar un mensaje avisando no se hallo el producto buscado 


productos = []



print("--- Menú ---")
print("")
print("")
print("1. Agregar producto")
print("2. Mostrar todos los productos")
print("3. Buscar producto")
print("4. Eliminar producto")
print("5. Salir")


movimiento = True 
while movimiento == True:
    select = input("\nIngresá el número de la opción elegida: ").strip()
    
#elige opción    
    if select.isdigit() and int(select) < 6 and int(select) > 0:
        
  #agregar producto: nombre, categoria, precio 
        if int(select) == 1:
 
    #nombre           
            nombre = input("\nIngresá el nombre del producto (sólo letras):").strip().lower()
                
            if nombre.isdigit() or nombre == "":
                print("\nDato no válido.")
                continue 
            if nombre not in productos:
                
      #categoria           
                categoria= input("\nIngresá la categoría (sólo letras): ").strip().lower()
                
                
                
                if categoria.isdigit():
                    print("Dato no válido")
                    continue 
                    
                if categoria == "":
                    print("Dato no válido")
                    continue 
        
        #precio          
                precio = input("\nIngresá el precio del producto (sólo números enteros positivos): $").strip()
                
                if precio.isdigit() and int(precio) >= 0 and precio != "":
                    #TRABAJAR CON SUB-LISTA
                    producto = [nombre, categoria, precio]
                    
                    
                    #Producto agregado
                    print("PRODUCTO AGREGADO")
                    print(producto)
                    
                    #AÑADIR A LISTA PRINCIPAL 
                    productos.append(producto)
                    
                    #Limpiar sub-lista
               #     producto.clear()
                    
                    #Mostrar lista actualizada 
                    print("\n--- Lista de productos actualizada ---")
                    print(productos)
                    continue 
                
                else:
                           
                    print("\nDato no válido")
                    continue 
  
  #mostrar todos los productos ingresados                
        if int(select) == 2:
            if len(productos) == 0:
                print("No hay productos ingresados.")
                continue 
            
            
            #Ordenar lista 
            productos.sort()
            print("\n--- Lista de productos ingresados ---")
            for i, producto in enumerate(productos, start=1):
                print(f"Nombre del producto {i}: {producto[0].title()}. Categoría: {producto[1].title()}. Precio: ${producto[2]}")
                continue  
            
                
  #buscar producto      
        if int(select) == 3:
            
            if len(productos) == 0:
                print("No hay productos ingresados.")
                continue 
            for i, producto in enumerate(productos, start=1):
                print(f"Nombre del producto {i:2}: {producto[0].title()}. Categoría: {producto[1].title()}. Precio: ${producto[2]}")
                continue      
                
                
            find = input("\nIngresá el nombre del producto que quieres visualizar: ").strip().lower()  
              
            if find.isdigit():
                print("❌ Dato no válido.")
                continue 
                
            if find.isdigit():
                print("❌ Dato no válido.")
                continue 


            

            for producto in productos:
                if producto[0] == find:
                    print("PRODUCTO ENCONTRADO")
                    print(f"Nombre del producto: {producto[0].title()} Categoría: {producto[1].title()} Precio: ${producto[2]}")
                    continue

                else:
                    print("🔍 Buscando ...")
                    continue       
            
                  
  #eliminar producto                
        if int(select) == 4:
            
            if len(productos) == 0:
                print("No hay productos ingresados.")
                continue 
                
            if productos:
                productos.sort()
                for i, producto in enumerate(productos, start=1):
                    print(f"{i:2}. Nombre del producto: {producto[0].title()} Categoría: {producto[1].title()} Precio: ${producto[2]}")
                 #en el print aparece "i:2" el ":2" marca una distancia de sangría al imprimir 
                number = input("número del producto a Eliminar:")
                
                if not number.isdigit():
                    print("❌ Dato no válido.")
                    continue 
                
                if not number:
                    print("❌ Dato no válido.")
                    continue      
                
                #se imprimen los productos numerados desde el 1, por eso se resta 1 al número seleccionado por el usuario, así va a coincidir con la posición (la posición inicia en cero)
                posicion_borrar = int(number) - 1
                
                #le di un nombre a la acción de borrar para usarla como orientación, así ubico con una posición en esta variable el nombre del producto para imprimirlo por pantalla 
                sublist_borrar = productos.pop(posicion_borrar)
                    
                print (f"El producto {sublist_borrar[0]} fue eliminado.\n")
                
                if len(productos) == 0:
                    print("No hay productos ingresados.")
                    continue 
            
            
                #Ordenar lista 
                productos.sort()
                print("\n--- Lista de productos ingresados ---")
                for i, producto in enumerate(productos, start=1):
                    print(f"Nombre del producto {i}: {producto[0].title()}. Categoría: {producto[1].title()}. Precio: ${producto[2]}")
                    continue  
                    
  #salir break                  
        if int(select) == 5:       
            
            if len(productos) == 0:
                print("\nGracias por usar la aplicación. Saliendo ...")
                break 
            
                
            #Ordenar lista 
            productos.sort()
            print("\n--- Lista de productos ingresados ---")
            for i, producto in enumerate(productos, start=1):
                print(f"Nombre del producto {i}: {producto[0].title()}. Categoría: {producto[1].title()}. Precio: ${producto[2]}")
                print()
                print()
                print("\nGracias por usar la aplicación. Saliendo ...")
               
                movimiento = False     
                
    else: 
        print("⚠️ Opción no encontrada.")     
        continue 
    