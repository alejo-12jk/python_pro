import random


characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input("¿Qué longitud quieres que tenga la contraseña? "))
password = ""
for i in range(length):
    password += random.choice(characters)
print("Tu contraseña es:", password)