control12_P3.py
```python
palabras = []

while True:
  palabra = input("Ingrese una palabra (o presione Enter para finalizar): ")
  if palabra == "":
    break
  palabras.append(palabra)

palabra_mas_larga = max(palabras, key=len)
cantidad_caracteres = len(palabra_mas_larga)

print(f"La palabra con más caracteres es '{palabra_mas_larga}' y tiene {cantidad_caracteres} caracteres.")
```