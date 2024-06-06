control12_P1.py
def main():
  """phyton
  Programa para registrar y analizar puntajes diarios de un alumno en un curso de 15 días.
  """

  puntajes = []
  dias_bajos = []

  print("Ingrese el puntaje diario del alumno (1-100) para cada uno de los 15 días:")

  for dia in range(1, 16):
    while True:
      try:
        puntaje = int(input(f"Día {dia}: "))
        if 1 <= puntaje <= 100:
          puntajes.append(puntaje)
          break
        else:
          print("Puntaje inválido. Ingrese un valor entre 1 y 100.")
      except ValueError:
        print("Entrada inválida. Ingrese un número entero.")

  for i, puntaje in enumerate(puntajes):
    if puntaje < 60:
      dias_bajos.append(i + 1)

  print("\nDías con puntaje menor a 60:")
  if dias_bajos:
    for dia in dias_bajos:
      print(f"Día {dia}")
  else:
    print("No se encontraron días con puntaje menor a 60.")

if __name__ == "__main__":
  main()
