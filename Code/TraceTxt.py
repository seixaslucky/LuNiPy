#cria o arquivo txt com os resultados dos calculos
class TraceTxt(object):
    def abreArquivo(self,nome):
        arq = open("./result/"+ str(nome),"w")
        return arq

    def fechaArquivo(self, arq):
        arq.close()
        pass

    def escreveArquivoScenery(self, i, arq,resultados):
        texto = self.printCicle(resultados, i)
        arq.write(texto)

    def printCicle(self, resultados, i):
        x = "\nCiclo:\t" + str(i)
        ciclo = x + self.printUser(resultados)
        return ciclo

    def printUser(self,resultados):
        resultadoUser=''
        for i in range(0, len(resultados)):
            x = '\n\tUser:\t' + str(resultados[i].user.id) + '\n\t\tAp connected:\t' + str(resultados[i].ap_principal.id) + '\n\t\tDistance:\t' + str("{0:.2f}".format(resultados[i].distancia_principal)) + '\n\t\tPotencia:\t' + str("{0:.2f}".format(resultados[i].power_principal)) + '\n\t\tSinr:\t' + str(resultados[i].sinr) + '\n'
            resultadoUser =  resultadoUser + x
        return resultadoUser

    def escreveArquivoSupervisionado(self, arq,resultados):
        texto = self.printSupervisioned(resultados)
        arq.write(texto)

    def printSupervisioned(self, resultados):
       
        sup = "\tUser Supervised:\t"
        for i in range(0, len(resultados)):
            x ='\n\t\tDistance:\t' + str("{0:.2f}".format(resultados[i].dist)) + '\n\t\tPotencia:\t' + str("{0:.2f}".format(resultados[i].power)) + '\n\t\tSinr:\t' + str(resultados[i].sinr) + '\n________________________'
            sup =  sup + x
        return sup