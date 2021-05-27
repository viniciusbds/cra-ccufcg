# coding: utf-8

'''
Script que armazena as notas das disciplinas e calcula o cra durante graduação de Ciência da Computação - UFCG
'''

S1 = {"p1": (-1, 60), "lp1": (-1, 60), "calculo1": (-1, 60), "vetorial": (-1, 60), "lpt": (-1, 60), "ic": (-1, 60)}

S2 = {"p2": (-1, 60), "lp2": (-1, 60), "calculo2": (-1, 60), "fmcc2": (-1, 60), "grafos": (-1, 60),"fmcc1": (-1, 60), "l.port": (-1, 60)}

S3 = {"eda": (-1, 60), "leda": (-1, 60), "logica": (-1, 60), "a.linear": (-1, 60)}

S4 = {"psoft": (-1, 60), "bd": (-1, 60), "oac": (-1, 60), "loac": (-1, 60), "prob": (-1, 60)}

S5 = {"plp": (-1, 60),  "so": (-1, 60), "proj.so": (-1, 60), "eng.software": (-1, 60), "direito": (-1, 60)}

S6 = { "tc": (-1, 60), "as":(-1, 60), "redes": (-1, 60), "estatistica": (-1, 60), "concorrente": (-1, 60), "didatica-p2": (0, 30)}

S7 = {"atal": (-1, 60), "met.cientifica": (-1, 60), "i.a": (-1, 60), "segurança": (-1,60)}

S8 = {
	"compiladores": (-1, 60),
	"projeto1": (-1, 60),
	"optativa1": (-1, 60),
	"optativa2": (-1, 60),
	"optativa.geral": (-1, 60),
	"didatica": (-1, 30)
}

S9 = {
	"projeto TCC": (-1, 60),
	"projeto2.b3": (-1, 60),
	"AA2": (-1, 60),
	"optativa2": (-1, 60)
}

S10 = {
	"TCC": (-1, 60),
	"AA3": (-1, 60),
	"optativa2": (-1, 60),
	"optativa3": (-1, 60)
}


def cra(semestres):
	produto = 0.0
	horas = 0.0
	for semestre in semestres:
		for nome in semestre.keys():
			disciplina = semestre[nome]
			nota, carga  = disciplina[0],  disciplina[1]
			if (nota >= 0): # disciplinas com notas iguais a zero são ignoradas, ou seja, ainda não foram cursadas
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

semestres = [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10]

print("## Informações Acadêmicas ##\n")
print("CADEIRAS PAGAS: %d / 51" % progresso(semestres))
print("CRA: %.2f" % cra(semestres))
