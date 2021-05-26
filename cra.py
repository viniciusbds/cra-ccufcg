# coding: utf-8

'''
Script que armazena as notas das disciplinas e calcula o cra durante graduação de Ciência da Computação - UFCG
'''

S1 = {"p1": (0, 60), "lp1": (0, 60), "calculo1": (0, 60), "vetorial": (0, 60), "lpt": (0, 60), "ic": (0, 60)}

S2 = {"p2": (0, 60), "lp2": (0, 60), "calculo2": (0, 60), "fmcc2": (0, 60), "grafos": (0, 60),"fmcc1": (0, 60), "l.port": (0, 60)}

S3 = {"eda": (0, 60), "leda": (0, 60), "logica": (0, 60), "a.linear": (0, 60)}

S4 = {"psoft": (0, 60), "bd": (0, 60), "oac": (0, 60), "loac": (0, 60), "prob": (0, 60)}

S5 = {"plp": (0, 60),  "so": (0, 60), "proj.so": (0, 60), "eng.software": (0, 60), "direito": (0, 60)}

S6 = { "tc": (0, 60), "as":(0, 60), "redes": (0, 60), "estatistica": (0, 60), "concorrente": (0, 60), "didatica-p2": (0, 30)}

S7 = {"atal": (0, 60), "met.cientifica": (0, 60), "i.a": (0, 60), "segurança": (0,60)}

S8 = {
	"compiladores": (0, 60),
	"projeto1": (0, 60),
	"optativa1": (0, 60),
	"optativa2": (0, 60),
	"optativa.geral": (0, 60),
	"didatica": (0, 30)
}

S9 = {
	"projeto TCC": (0, 60),
	"projeto2.b3": (0, 60),
	"AA2": (0, 60),
	"optativa2": (0, 60)
}

S10 = {
	"TCC": (0, 60),
	"AA3": (0, 60),
	"optativa2": (0, 60),
	"optativa3": (0, 60)
}


def cra(semestres):
	produto = 0.0
	horas = 0.0
	for semestre in semestres:
		for nome in semestre.keys():
			disciplina = semestre[nome]
			nota, carga  = disciplina[0],  disciplina[1]
			if (nota != 0): # disciplinas com notas iguais a zero são ignoradas, ou seja, ainda não foram cursadas
				produto += nota * carga
				horas += carga

	return (1.0 * produto) / horas


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
