import random

print("---> Üdvözöllek játékos <---")
print("----------------------------")
print("A játék célja, hogy átjuss három szobán az ajtókon keresztül.")
print("Minden szobában két ajtó van. Választanod kell közülük!")
print("Van olyan ajtó, ami mögött csapda van és ha azon belépsz 10 életpontot veszítesz.")
print("A játék célja, hogy átjuss mind a három szobán!")
print("Az ajtó választását az '1' vagy '2' gombbal teheted meg.")
print("----------------------------")
print("---> Kezdődjön a játék! <---")

elet = 30

print("----------------------------")
print("        Első szoba")
print("Az életerőd:", elet)
print("Melyik ajtót választod:",end=' ')
valasz = int(input())

csapda = random.randint(1, 2)
print("A csapda helye:", csapda)

if valasz == csapda:
    print("Sajnos csapdába léptél!")
    elet = elet - 10
else:
    print("Szerencséd volt, kikerülted a csapdát!")

print("----------------------------")

print("        Második szoba")
print("Az életerőd:", elet)
print("Melyik ajtót választod:",end=' ')
valasz = int(input())

csapda = random.randint(1, 2)
print("A csapda helye:", csapda)

if valasz == csapda:
    print("Sajnos csapdába léptél!")
    elet = elet - 10
else:
    print("Szerencséd volt, kikerülted a csapdát!")

print("----------------------------")

print("        Harmadik szoba")
print("Az életerőd:", elet)
print("Melyik ajtót választod:",end=' ')
valasz = int(input())

csapda = random.randint(1, 2)
print("A csapda helye:", csapda)

if valasz == csapda:
    print("Sajnos csapdába léptél!")
    elet = elet - 10
else:
    print("Szerencséd volt, kikerülted a csapdát!")

print("----------------------------")
