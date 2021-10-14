# coding: utf-8

'''
Script que armazena as notas das disciplinas e calcula o cra durante graduação de Ciência da Computação - UFCG
'''

S1 = {"FMCCI": (-1, 60), "p1": (-1, 60), "lp1": (-1, 60), "IC": (-1, 60), "opt geral": (-1, 60)}

S2 = {"FMCCII": (-1, 60), "calculo1": (-1, 60), "p2": (-1, 60), "lp2": (-1, 60), "optativa geral": (-1, 60)}

S3 = {"a.linear": (-1, 60), "logica": (-1, 60), "calculo2": (-1, 60), "EDA": (-1, 60), "LEDA": (-1, 60), "grafos": (-1, 60)}

S4 = {"probabilidade": (-1, 60), "psoft": (-1, 60), "plp": (-1, 60), "Bd 1": (-1, 60), "OAC": (-1, 60), "LOAC": (-1, 60)}

S5 = {"estatistica": (-1, 60),  "AS": (-1, 60), "ES": (-1, 60), "redes": (-1, 60), "SO": (-1, 60), "TC": (-1, 60)}

S6 = {"MC": (-1, 60), "concorrente":(-1, 60), "IA": (-1, 60), "opt.especifica1": (-1, 60), "opt.especifica2": (-1, 60)}

S7 = {"ATAL": (-1, 60), "compiladores": (-1, 60), "opt.especifica1": (-1, 60), "opt.especifica2": (-1,60), "opt geral": (-1, 60)}

S8 = {"projeto1": (-1, 60), "PTCC": (-1, 60), "opt.especifica1": (-1, 60), "opt.especifica2": (-1,60), "opt geral": (-1, 60)}

S9 = {"projeto2": (-1, 60), "TCC": (-1, 60), "opt.especifica1": (-1, 60), "opt.especifica2": (-1,60), "opt.especifica3": (-1,60), "opt.especifica4": (-1, 60)}


semestres_cursados = []
semestre_atual = S1
semestres_matriculados = semestres_cursados.copy()
semestres_matriculados.append(semestre_atual)


def cra(semestres):
	produto = 0.0
	horas = 0.0
	for semestre in semestres:
		for nome in semestre.keys():
			disciplina = semestre[nome]
			nota, carga  = disciplina[0],  disciplina[1]
			if (nota >= 0): # disciplinas com nota = -1 são ignoradas, pois ainda não foram cursadas
				produto += nota * carga
				horas += carga

	result = 0
	if horas > 0:
		result = (1.0 * produto) / horas
	else:
		result = 0

	return result


def progresso(semestres):
	cadeiras_pagas = 0
	
	for semestre in semestres:
		for nome in semestre.keys():
			disciplina = semestre[nome]
			nota  = disciplina[0]
			if (nota != 0):
				cadeiras_pagas += 1

	return cadeiras_pagas


print("## Informações Acadêmicas ##\n")
print("CRA Atual")
print("CADEIRAS PAGAS: %d / 51" % progresso(semestres_cursados))
print("CRA: %.2f\n" % cra(semestres_cursados))

print("Previsão do CRA")
print("CADEIRAS PAGAS: %d / 51" % progresso(semestres_matriculados))
print("CRA: %.2f\n" % cra(semestres_matriculados))

