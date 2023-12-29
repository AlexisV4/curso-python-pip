import random

opciones = ("piedra", "papel", "tijera")

computer_wins= 0
user_wins = 0

rondas = 1

while True:
  print('*' * 10)
  print('RONDA', rondas)
  print('*' * 20)
  print()

  print("Computer wins = ", computer_wins)
  print('*' * 20)
  print("User wins = ", user_wins)
  print()
  

  opcion_usuario = input("piedra, papel o tijera: ")
  print("---------------------------------")
  opcion_usuario = opcion_usuario.lower()
  
  rondas += 1
  
  if not opcion_usuario in opciones:
    print("La opción no es valida.")
    continue
    print()
    
  opcion_computador = random.choice(opciones)
  
  print("Opcion_Usuario = ", opcion_usuario)
  print("Opcion_Computadora= ", opcion_computador)
  print()
  print()
  
  if opcion_usuario == opcion_computador:
    print("Empate!")
  elif opcion_usuario == "piedra":
    if opcion_computador == "tijera":
      print("piedra vence a tijera!")
      print("El usuario gana!")
      user_wins += 1
    else:
      print("Papel vence a piedra")
      print("Computadora ha ganado")
      computer_wins += 1
  elif opcion_usuario == "papel":
    if opcion_computador == "piedra":
      print("papel gana a piedra")
      print("usuario ganó")
      user_wins += 1
    else:
      print("tijera gana a papel")
      print("computador ganó")
      computer_wins += 1
  elif opcion_usuario == "tijera":
    if opcion_computador == "papel":
      print("tijera gana a papel")
      print("usuario ganó")
      user_wins += 1
    else:
      print("piedra gana a tijera")
      print("computadora ganó")
      computer_wins += 1

  if computer_wins == 2:
    print("El computador ha ganado el juego")
    break

  if user_wins == 2:
    print("El usuario ha ganado el juego")
    break
    
  
    