#!/usr/bin/env python
# coding: utf-8

# In[ ]:

arq = open('antartica.txt', 'w+')

#Parâmetros para o fitoplanton
float fitoplanton = 100
float fotossintese = 2.0
float temp_agua_aumento = 0.03

#Valores iniciais dos animais
float camarao = 15.0
float pinguim = 15.0
float peixe = 15.0
float foca = 15.0

#Taxa de infecção da foca por poluição
float poluicao = 1.9

float v[14] #Definindo vetor que armazena os parâmetros
float deltaT = 0.01 #Variação de deltaT
int i
float tempo
float dFitoplanton, dCamarao, dPinguim, dfoca, dPeixe
float K = 100.0 #Capacidade de suporte ao meio

v[0] = 0.02
v[1] = 0.01
v[2] = 0.094
v[3] = 0.01
v[4] = 0.01
v[5] = 0.09
v[6] = 0.01
v[7] = 0.01
v[8] = 0.04
v[9] = 0.06
v[10] = 0.01
v[11] = 0.02
v[12] = 0.03
v[13] = 0.009

#gravar os dois
#print("Tempo Fitoplanton Camarao Peixe Pinguim Foca \n", tempo, fitoplanton, camarao, peixe, pinguim, foca);
arq.write("Tempo Fitoplanton Camarao Peixe Pinguim Foca \n")
#print("%.2f  %f   %f  %f  %f  %f\n", tempo, fitoplanton, camarao,peixe , pinguim, foca);
arq.write("{}  {}   {}  {}  {}  {}\n".format("%.2f" % tempo, fitoplanton, camarao,peixe , pinguim, foca))

for tempo in range(0,300,deltaT):
        #Taxa de variação de cada em espécie em função das equações de Lotka-Volterra
    dFitoplanton = fitoplanton * (fotossintese - fotossintese*fitoplanton/K - v[0]*camarao - v[1]*peixe - temp_agua_aumento) * deltaT
    dCamarao = camarao * (v[2]*fitoplanton - v[3]*pinguim - v[4]*foca) * deltaT
    dPeixe = peixe * (v[5]*fitoplanton - v[6]*pinguim - v[7]*foca) * deltaT
    dPinguim = pinguim * (v[8]*camarao + v[9]*peixe - v[10]*foca) * deltaT
    dFoca = foca * (v[11]*camarao + v[12]*peixe + v[13]*pinguim - poluicao) * deltaT

    espinossauro += dEspinossauro
    camarao += dCamarao
    pinguim += dPinguim
    foca += dFoca
    fitoplanto += dFitoplanton
    peixe += dPeixe

    #print(analise, "%.2f  %f   %f  %f  %f  %f  %f\n", tempo, fitoplanton, camarao, peixe, pinguim, foca)
    arq.write("{}  {}   {}  {}  {}  {}\n".format("%.2f" % tempo, fitoplanton, camarao,peixe , pinguim, foca))
