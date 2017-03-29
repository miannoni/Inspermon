import random

lista_monsteste = [["Phelipe",2.2121,1.2929,1.2929,1.2121],["Matteo",2.5151,1.5555,1.5757,1.5151],["Delchi",2.4747,1.5959,1.4747,1.9191]]
skill_lista = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8]
poke1 = [0,20,[0,3,6,5]]
poke2 = [1,20,[1,2,4,7]]
def fight(pokemon1,pokemon2):
	vidauser = (pokemon1[1]*lista_monsteste[pokemon1[0]][1]) + 12
	vidacpu = (pokemon2[1]*lista_monsteste[pokemon2[0]][1]) + 12
	print(lista_monsteste[pokemon1[0]][0] + " tem " + str(vidauser))
	print(lista_monsteste[pokemon2[0]][0] + " tem " + str(vidacpu) + "\n")
	while (vidauser > 0) and (vidacpu > 0):
		move = input("lutar ou correr?\n")
		if move.lower() == "lutar":
			atk = int(input("\nQual ataque usar (de 1 a 4)?\n"))
			if (pokemon1[1]*lista_monsteste[pokemon1[0]][4] > pokemon2[1]*lista_monsteste[pokemon2[0]][4]):
				userdmg = pokemon1[1]*lista_monsteste[pokemon1[0]][2]*skill_lista[pokemon1[2][atk - 1]]
				vidacpu = vidacpu - userdmg
				if vidacpu <= 0:
					print(lista_monsteste[pokemon1[0]][0] + " ganhou!!\n")
					break
				cpudmg = pokemon2[1]*lista_monsteste[pokemon2[0]][2]*(skill_lista[random.randint(1,4) - 1])
				vidauser = vidauser - cpudmg
				if vidauser <= 0:
					print(lista_monsteste[pokemon2[0]][0] + " ganhou!!\n")
					break
				print("\n" + lista_monsteste[pokemon1[0]][0] + " causou " + str(userdmg) + " de dano")
				print(lista_monsteste[pokemon2[0]][0] + " causou " + str(cpudmg) + " de dano")
				print("\n" + lista_monsteste[pokemon1[0]][0] + " tem " + str(vidauser))
				print(lista_monsteste[pokemon2[0]][0] + " tem " + str(vidacpu) + "\n")
			else:
				cpudmg = pokemon2[1]*lista_monsteste[pokemon2[0]][2]*(skill_lista[random.randint(1,4) - 1])
				vidauser = vidauser - cpudmg
				print("\n" + lista_monsteste[pokemon2[0]][0] + " causou " + str(cpudmg) + " de dano")
				if vidauser < 0:
					print(lista_monsteste[pokemon2[0]][0] + " ganhou!!\n")
					break
				userdmg = pokemon1[1]*lista_monsteste[pokemon1[0]][2]*skill_lista[pokemon1[2][atk - 1]]
				vidacpu = vidacpu - userdmg
				print(lista_monsteste[pokemon1[0]][0] + " causou " + str(userdmg) + " de dano")
				if vidacpu < 0:
					print(lista_monsteste[pokemon1[0]][0] + " ganhou!!\n")
					break
				print("\n" + lista_monsteste[pokemon1[0]][0] + " tem " + str(vidauser))
				print(lista_monsteste[pokemon2[0]][0] + " tem " + str(vidacpu) + "\n")
		if move.lower() == "correr":
			if random.randint(1,4) == 2:
				print("\nVoce correu com sucesso!\n")
				break
			else:
				print("\nNao foi possivel correr!\n")
				cpudmg = pokemon2[1]*lista_monsteste[pokemon2[0]][2]*(skill_lista[random.randint(1,4) - 1])
				vidauser = vidauser - cpudmg
				print(lista_monsteste[pokemon2[0]][0] + " causou " + str(cpudmg) + " de dano\n")
				if vidauser <= 0:
					print(lista_monsteste[pokemon2[0]][0] + " ganhou!!\n")
					break
				print("\n" + lista_monsteste[pokemon1[0]][0] + " tem " + str(vidauser))
				print(lista_monsteste[pokemon2[0]][0] + " tem " + str(vidacpu) + "\n")

fight(poke1,poke2)