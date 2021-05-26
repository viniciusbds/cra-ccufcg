# coding: utf-8

'''
Pequeno script que armazena as notas das disciplinas e calcula o meu cra durante graduação de Ciência da Computação - UFCG
2017.2 - 2022.1

@viniciusbds

'''
# 2017.2 p1
S1 = {"p1": (9.8, 60), "lp1": (9.8, 60), "calculo1": (9.9, 60), "vetorial": (9.6, 60), "lpt": (8.4, 60), "ic": (7.2, 60)}

# 2018.1 p2
S2 = {"p2": (9.0, 60), "lp2": (9.1, 60), "calculo2": (8.5, 60), "fmcc2": (8.6, 60), "grafos": (8.9, 60),"fmcc1": (9.9, 60), "l.port": (8.4, 60)}

# 2018.2 p3
S3 = {"eda": (8.5, 60), "leda": (8.0, 60), "logica": (9.5, 60), "a.linear": (9.5, 60)}

# 2019.1 p4
S4 = {"psoft": (8.8, 60), "bd": (8.3, 60), "oac": (8.2, 60), "loac": (8.4, 60), "prob": (9.0, 60)}

# 2019.2 p5
S5 = {"plp": (7.65, 60),  "so": (8.1, 60), "proj.so": (7.5, 60), "eng.software": (8.5, 60), "direito": (9.3, 60)}

# 2020.0 RAE (Regime Acadêmico Extraordinário)
S6 = { "tc": (8.5, 60), "as":(9.3, 60), "redes": (8.7, 60), "estatistica": (8.6, 60), "concorrente": (8.2, 60), "didatica-p2": (10, 30)}

# 2020.1 p6
S7 = {"atal": (8.9, 60), "met.cientifica": (9.4, 60), "i.a": (9.9, 60), "segurança": (9.17,60)}

# 2020.2 p7
S8 = {
	"compiladores": (10, 60),
	"projeto1": (10, 60),
	"optativa1": (10, 60),
	"optativa2": (10, 60),
	"optativa.geral": (10, 60),
	"didatica": (10, 30)
}

# 2021.1 p8
S9 = {
	"projeto TCC": (10, 60),
	"projeto2.b3": (9, 60),
	"AA2": (9, 60),
	"optativa2": (9, 60)
}

# 2021.2 p9
S10 = {
	"TCC": (9, 60),
	"AA3": (9, 60),
	"optativa2": (9, 60),
    "optativa3": (9, 60)
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
# print("SEMESTRES: 6 / 10")
print("CRA: %.2f" % cra(semestres))
