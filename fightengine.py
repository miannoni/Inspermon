import random,math
from levelup import GainEXP

#Extração dos DataBases
#insperdex[] = [nome,tipo,atqi,atqm,atqEi,atqEm,defi,defm,defEi,defEm, HPi , HPm ,veli,velm,nvEVO]
#				0    1    2   3     4     5     6    7    8    9      10    11   12   13    14

#ficha = [nome,tag,atq,atqE,res,resE,HPmax,HPatual,vel, nv ,exp,[skills]]
#			0   1   2   3    4    5    6     7       8  9    10    11


def fichaGen(dex,tag,nv,skills):
	nome = dex[0]
	atq = dex[2] + dex[3]*nv
	atqE = dex[4] + dex[5]*nv
	res = dex[6] + dex[7]*nv
	resE = dex[8] + dex[9]*nv
	HPmax = dex[10] + dex[11]*nv
	HPatual = HPmax
	vel = dex[12] + dex[13]*nv
	ficha = [nome,tag,atq,atqE,res,resE,HPmax,HPatual,vel,nv,0, skills]
	return ficha

skill_lista = [1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8]
insperdex = [0]
insperdex.append(["Bulbasauro", "Planta", 6, 1.29, 6, 1.61, 6, 1.29, 6, 1.61, 12, 2.21, 6, 1.21, 101])
insperdex.append(["Squirtle", "Planta", 6, 1.27, 6, 1.31, 6, 1.61, 6, 1.59, 6, 2.19, 6, 1.17, 101])

def multiplyDMG(pokeAtack,pokeDefend):
	multiply = 1
	if insperdex[pokeAtack[1]][1] == "Planta": #Planta atacando
	 	if insperdex[pokeDefend[1]][1] == "Fogo": #Fogo defendendo
	 		multiply += -0.25*multiply
	 		print(pokeAtack[0] + " não é muito eficiente contra " + pokeDefend[0])
	 	elif insperdex[pokeDefend[1]][1] == "Agua": #Agua defendendo
	 		multiply += 0.5*multiply
	 		print(pokeAtack[0] + " é muito eficiente contra " + pokeDefend[0])

	elif insperdex[pokeAtack[1]][1] == "Fogo": #Fogo atacando
	 	if insperdex[pokeDefend[1]][1] == "Agua": #Agua defendendo
	 		multiply += -0.25*multiply
	 		print(pokeAtack[0] + " não é muito eficiente contra " + pokeDefend[0])
	 	elif insperdex[pokeDefend[1]][1] == "Planta": #Planta defendendo
	 		multiply += 0.5*multiply
	 		print(pokeAtack[0] + " é muito eficiente contra " + pokeDefend[0])

	elif insperdex[pokeAtack[1]][1] == "Agua": #Agua atacando
	 	if insperdex[pokeDefend[1]][1] == "Planta": #Planta defendendo
	 		multiply += -0.25*multiply
	 		print(pokeAtack[0] + " não é muito eficiente contra " + pokeDefend[0])
	 	elif insperdex[pokeDefend[1]][1] == "Fogo": #Fogo defendendo
	 		multiply += 0.5*multiply
	 		print(pokeAtack[0] + " é muito eficiente contra " + pokeDefend[0])

	luck = random.randint(1,20)
	if luck >= 19: #Critico
		multiply += 1*multiply
		print(pokeAtack[0] + " Critou!!")
	return multiply


def declaraHP(pokemon1,pokemon2):
	print(pokemon1[0] + " tem " + str(math.ceil(pokemon1[7])) + " de HP")
	print(pokemon2[0] + " tem " + str(math.ceil(pokemon2[7])) + " de HP\n")
	return 0

def turnoUser(pokemon1,pokemon2,atk):
	userdmg = pokemon1[2]*skill_lista[pokemon1[11][atk - 1]]
	userdmg =userdmg * multiplyDMG(pokemon1,pokemon2)
	cpures = pokemon2[4]
	if userdmg > cpures:
		userdmg += - cpures
	else:
		userdmg = 0
	pokemon2[7] += - userdmg
	print(pokemon1[0] + " causou " + str(math.ceil(userdmg)) + " de dano")
	print()
	return pokemon2

def turnoCPU(pokemon1,pokemon2):
	cpudmg = pokemon2[2]*(skill_lista[random.randint(1,4) - 1])
	userres = pokemon1[4]
	cpudmg = cpudmg * multiplyDMG(pokemon2,pokemon1)
	if cpudmg > userres:
		cpudmg += - userres
	else:
		cpudmg = 0
	pokemon1[7] += - cpudmg
	print(pokemon2[0] + " causou " + str(math.ceil(cpudmg)) + " de dano")
	print()
	return pokemon1

def VictUser(pokemon1,pokemon2):
	pokemon1 = GainEXP(pokemon1,(pokemon2[9]*5))
	return pokemon1

def VictCPU(pokemon1,pokemon2):
	print(pokemon2[0] + " ganhou!!\n")
	pokemon1[7] = 0
	return pokemon1

def fight(pokemon1,pokemon2):
	declaraHP(pokemon1,pokemon2)
	while (pokemon1[7] > 0) and (pokemon2[7] > 0):
		move = input("lutar ou correr?\n")
		#Combate
		if move.lower() == "lutar":
			atk = int(input("\nQual ataque usar (de 1 a 4)?\n")) #Escolhendo Skill
			print()
			#Primeiro Turno = Player
			if (pokemon1[8] > pokemon2[8]): #Comparando Speed
				pokemon2 = turnoUser(pokemon1,pokemon2,atk)
				if pokemon2[7] <= 0:#CPU morreu?
					VictUser(pokemon1,pokemon2)
					break
				pokemon1 = turnoCPU(pokemon1,pokemon2)
				if pokemon1[7] <= 0:#Player Morreu?
					VictCPU(pokemon1,pokemon2)
					break
				declaraHP(pokemon1,pokemon2)
			#Primeiro Turno = CPU
			else:
				pokemon1 = turnoCPU(pokemon1,pokemon2)
				if pokemon1[7] <= 0:#Player Morreu?
					VictCPU(pokemon1,pokemon2)
					break
				pokemon2 = turnoUser(pokemon1,pokemon2,atk)
				if pokemon2[7] <= 0:#CPU Morreu?
					VictUser(pokemon1,pokemon2)
					break
				declaraHP(pokemon1,pokemon2)

		#Correr
		if move.lower() == "correr":
			#Sucesso na Fuga
			if random.randint(1,4) == 2:
				print("\nVoce correu com sucesso!\n")
				break
			#Falha na Fuga
			else:
				print("\nNao foi possivel correr!\n")
				pokemon1 = turnoCPU(pokemon1,pokemon2)
				if pokemon1[7] <= 0: #Player Morreu?
					VictCPU(pokemon1,pokemon2)
					break
				declaraHP(pokemon1,pokemon2)
	return pokemon1
