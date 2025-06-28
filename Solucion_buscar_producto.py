productos = []


print("--- Menú ---")
print("")
print("")
print("1. Agregar producto")
print("2. Mostrar todos los productos")
print("3. Buscar producto")
print("4. Eliminar producto")
print("5. Salir")


while True:
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
                    producto = {
                        "nombre": nombre,
                        "categoria": categoria,
                        "precio": precio
                        }
                    productos.append(producto)
                    
                    print("\n--- Lista de productos actualizada ---")
                    for producto in productos:
                        print(f"Nombre del producto: {producto['nombre'].capitalize()}. Categoría: {producto['categoria'].title()}. Precio: ${producto['precio']}")
                        continue 
                
                else:
                           
                    print("\nDato no válido")
                    continue 
  
  #mostrar todos los productos ingresados                
        if int(select) == 2:
            if len(productos) == 0:
                print("No hay productos ingresados.")
                continue 
            
            print("\n--- Lista de productos ingresados ---")
            for producto in productos: 
                i = 0 
                print(f"Nombre del producto {i + 1}: {producto.get('nombre').capitalize()}. Categoría: {producto.get('categoria').title()}. Precio: ${producto.get('precio')}")
                continue  
            
                
  #buscar producto      
        if int(select) == 3:
            
            if len(productos) == 0:
                print("No hay productos ingresados.")
                continue 
                
            find = input("\nIngresá el nombre del producto que quieres visualizar: ").strip().lower()  
              
            if find.isdigit():
                print("❌ Dato no válido.")
                continue 
                
            if find.isdigit():
                print("❌ Dato no válido.")
                continue 
                
            if producto.get('nombre') != find:
                print("No se encontraron resultados.")
                continue     
                  
            for producto in productos:
                if producto.get('nombre') == find:
                    print(f"Nombre del producto: {producto['nombre'].title()} Categoría: {producto['categoria'].title()} Precio: ${producto['precio']}")
                    continue
                
              
                  
  #eliminar producto                
        if int(select) == 4:
            
            if len(productos) == 0:
                print("No hay productos ingresados.")
                continue 
                
            eliminar = input("\nIngresá el nombre del producto que quieres eliminar: ").strip().lower()
                
            if eliminar.isdigit():
                print("❌ Dato no válido.")
                continue 
            
            if eliminar == "":
                print ("❌ Dato no válido.")
                continue 
            
            for producto in productos:
                if producto.get('nombre') == eliminar:
                    productos.remove(eliminar)
                    print (f"El producto {eliminar} fue eliminado.")
                    print("\n--- Lista actualizada ---")
                    print(f"Nombre del producto: {producto['nombre'].title()} Categoría: {producto['categoria'].title()} Precio: ${producto['precio']}")
                    continue   
                else:
                    print("no se encontraron resultados.")
                    continue         
  #salir break                  
        if int(select) == 5:       
            
            if len(productos) == 0:
                print("\nGracias por usar la aplicación. Saliendo ...")
                break 
            
                
            print("\n--- Lista de productos actualizada ---")
            print(f"Nombre del producto: {producto['nombre'].title()} Categoría: {producto['categoria'].title()} Precio: ${producto['precio']}")
                      
            break 
    else: 
                       
        print("⚠️ Opción no encontrada.")     
        continue 
    