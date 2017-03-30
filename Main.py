import time,sys,random
from fightengine import fight,fichaGen

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def print_fast(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
##
def recuphp():
	return

insperdex = [0]
insperdex.append(["Bulbasauro", "Planta", 6, 1.29, 6, 1.61, 6, 1.29, 6, 1.61, 12, 2.21, 6, 1.21, 101])
insperdex.append(["Squirtle", "Planta", 6, 1.27, 6, 1.31, 6, 1.61, 6, 1.59, 6, 2.19, 6, 1.17, 101])


poke1 = fichaGen(insperdex[1],1,20,[0,3,6,5])

playerchoice = input("Deseja jogar?\n")

if playerchoice.lower() == "sim":
	
	print_slow("loading . . . . . .\n")

	while playerchoice.lower() == "sim":
		ato1 = input("Voce deseja passear ou dormir?\n")
		if ato1.lower() == "dormir":
			print_slow("Voce esta dormindo . . . . . .\n")
			print_fast("Voce acordou!!")
		elif ato1.lower() == "passear":
			fightou = random.randint(1,2)
			if fightou == 1:
				print_fast("Voce nao encontrou nada . . .\n")
			if fightou == 2:
				# pokemonrandom = randint(0,len(<pokedex>))
				print_fast("Um wild " + insperdex[2][0] + " apareceu!!\n")
				fight(poke1,fichaGen(insperdex[2],2,20,[1,2,4,7]))#<identificador do pokemon do jogador>, <identificador do pokemon random>)
		elif ato1.lower() == "sair":
			break

# if playerchoice == "sim":
# 	for i in range(10):
# 		print(".")
# 		time.sleep(0.5)
	# while 
