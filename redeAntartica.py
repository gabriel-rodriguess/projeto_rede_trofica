#!/usr/bin/env python
# coding: utf-8

# In[ ]:

arq = open('antartica.txt', 'w+')

#Parâmetros para o fitoplanton
fitoplanton = 100.0
fotossintese = 2.0
temp_agua_aumento = 0.03

#Valores iniciais dos animais
camarao = 15.0
pinguim = 15.0
peixe = 15.0
foca = 15.0

#Taxa de infecção da foca por poluição
poluicao = 1.9

v = [] #Definindo vetor que armazena os parâmetros
#deltaT = 0.01 #Variação de deltaT
deltaT = 0.01
K = 100.0 #Capacidade de suporte ao meio
tempo = 0.0

v.append(0.02)
v.append(0.01)
v.append(0.094)
v.append(0.01)
v.append(0.01)
v.append(0.09)
v.append(0.01)
v.append(0.01)
v.append(0.04)
v.append(0.06)
v.append(0.01)
v.append(0.02)
v.append(0.03)
v.append(0.009)

#gravar os dois
arq.write("Tempo Fitoplanton Camarao Peixe Pinguim Foca \n")
arq.write("{}  {}   {}  {}  {}  {}\n".format("%.2f" % tempo, fitoplanton, camarao,peixe , pinguim, foca))


while(tempo < 300):
    tempo += deltaT
    #Taxa de variação de cada em espécie em função das equações de Lotka-Volterra
    dFitoplanton = fitoplanton * (fotossintese - fotossintese*fitoplanton/K - v[0]*camarao - v[1]*peixe - temp_agua_aumento) * deltaT
    dCamarao = camarao * (v[2]*fitoplanton - v[3]*pinguim - v[4]*foca) * deltaT
    dPeixe = peixe * (v[5]*fitoplanton - v[6]*pinguim - v[7]*foca) * deltaT
    dPinguim = pinguim * (v[8]*camarao + v[9]*peixe - v[10]*foca) * deltaT
    dFoca = foca * (v[11]*camarao + v[12]*peixe + v[13]*pinguim - poluicao) * deltaT

    camarao += dCamarao
    pinguim += dPinguim
    foca += dFoca
    fitoplanton += dFitoplanton
    peixe += dPeixe


    arq.write("{}  {}   {}  {}  {}  {}\n".format("%.2f" % tempo, fitoplanton, camarao,peixe , pinguim, foca))
