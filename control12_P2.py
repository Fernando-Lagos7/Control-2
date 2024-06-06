control12_P2.py
```phyton
nombres = []

# Ingrese 7 nombres
for i in range(7):
  nombre = input(f"Ingrese el nombre {i+1}: ")
  nombres.append(nombre)

# Eliminar nombres que no terminan en "a"
nombres_filtrados = [nombre for nombre in nombres if nombre.endswith("a")]

# Mostrar la lista resultante
print("Lista de nombres que terminan en 'a':", nombres_filtrados)
```