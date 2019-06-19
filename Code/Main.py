from DataGenerator import DataGenerator
from Config import Config
from FactoryAp import FactoryAp
from FactoryUser import FactoryUser
from Scenery import Scenery
from Graphics import Graphics
from TraceTxt import TraceTxt
from SupervisedData import SupervisedData

class Main(object):
    def main():
        go_file = TraceTxt()
        sce = Scenery()
        gra = Graphics()
        config = Config()
        fac_aps = FactoryAp()
        fac_users = FactoryUser()
        data_generator = DataGenerator()
        arq = go_file.abreArquivo('result.txt')
        arq_supervisioned = go_file.abreArquivo('supervisioned.txt')

        aps = fac_aps.createAps(config)
        users = fac_users.createUsers(config)
        dados = []
       

        sp = SupervisedData()

        valuesClean = sp.get_values(config,aps)
        
        #chama o gerador de ddos apssando a lista de usuarios e aps(com os tributs de localizacao)
        for i in range(0, config.ciclo):
            dados, users = data_generator.createData(aps,config, users)
            #gera grafico
            sce.gerarGrafico(users, aps, i, config, valuesClean)
            #gera arquivo
            go_file.escreveArquivoScenery(i, arq, dados)

        go_file.escreveArquivoSupervisionado(arq_supervisioned, valuesClean)
        
        gra.plotagemPower(valuesClean,config)
        gra.heatMaps(aps,config)
        #gra.heatMapSinr(aps,config)

        go_file.fechaArquivo(arq)
        
    if __name__== "__main__":
        main()

