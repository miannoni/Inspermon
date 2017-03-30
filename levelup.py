#insperdex[] = [nome,tipo,atqi,atqm,atqEi,atqEm,defi,defm,defEi,defEm, HPi , HPm ,veli,velm,nvEVO]
#				0    1    2   3     4     5     6    7    8    9      10    11   12   13    14

#ficha = [nome,tag,atq,atqE,res,resE,HPmax,HPatual,vel, nv ,exp,[skills]]
#			0   1   2   3    4    5    6     7       8  9    10    11
def Upando(ficha):
	ficha[2] += insperdex[ficha[1]][3]
	ficha[3] += insperdex[ficha[1]][5]
	ficha[4] += insperdex[ficha[1]][7]
	ficha[5] += insperdex[ficha[1]][9]
	ficha[6] += insperdex[ficha[1]][11]
	ficha[8] += insperdex[ficha[1][13]]
	return ficha

def Evoluindo(ficha):
	ficha[1] += 1
	ficha[0] = insperdex[ficha[1]][0]
	ficha[2] = insperdex[ficha[1]][2]
	ficha[3] = insperdex[ficha[1]][4]
	ficha[4] = insperdex[ficha[1]][6]
	ficha[5] = insperdex[ficha[1]][8]
	ficha[6] = insperdex[ficha[1]][10]
	ficha[8] = insperdex[ficha[1]][12]
	return ficha

def DeclaraAtts(ficha):
	print("Ataque: {0}    Ataque Especial: {1}".format(ficha[2],ficha[3]))
	print("Defesa: {0}    Defesa Especial: {1}".format(ficha[4],ficha[5]))
	print("HPmax:  {0}".format(ficha[6]))
	print("Velocidade: {0}".format(ficha[8]))
	print("Nivel: {0}     Experiencia: {1}".format(ficha[9],ficha[10]))
	return 0


def GainEXP(ficha,expRecebido):
	#Verificando se houve level up
	if ((ficha[10] + expRecebido) >= (4/5)*(ficha[8]**3)) and ficha[9]<100:		
		ficha[9] += 1
		ficha[10] += expRecebido - (4/5)*(ficha[9]**3)
		#Verificando se houve Evolução 
		if (ficha[9] >= insperdex[14]):
			OptEvoluir = int(input("{0} Esta evoluindo!\nClique 0 para impedir e 1 para permetir".format(ficha[0])))
			if OptEvoluir == 1:
				#Evoluindo
				ficha = Evoluindo(ficha)
				print("Uau!\n{0} acabou evoluir para um {1}".format(insperdex[(ficha[1]-1)][0],ficha[0]))
				DeclaraAtts(ficha)
			else:
				ficha = Upando(ficha)
				DeclaraAtts(ficha)
		#Upando
		else:
			ficha = Upando(ficha)
			DeclaraAtts(ficha)
	#Add Experiencia
	elif ficha[9]<100:
		ficha[10] += expRecebido
		print("{0} Recebeu {1} pontos de experiencia!".format(ficha[0],expRecebido))
	else:
		ficha[10] = 0

	return ficha
	
