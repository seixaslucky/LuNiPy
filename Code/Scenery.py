import matplotlib.pyplot as plt
import pylab as pl
#plota o cenario
class Scenery(object):
    fig = None
    ax = None

    #plota os aps na posicao correta
    def plotagemAps(self, aps, ax, fig):
        #plota os APs como asteristico preto
        for i in range(0, len(aps)):
            #ax.add_artist(circle[i])
            ax.plot((aps[i].x), (aps[i].y), 'D', color='green', markersize=12)
            pl.text(
                (aps[i].x), (aps[i].y), aps[i].id, color="black", fontsize=8)

    #plota os usuarios como pontos vermelhos
    def plotagemUsers(self, users, ax, fig):

        for i in range(0, len(users)):
            ax.plot((users[i].x), (users[i].y), 'o', color='red')
            pl.text(
                (users[i].x), (users[i].y),
                users[i].id,
                color="black",
                fontsize=8)

    #gera o grafico
    def gerarGrafico(self, users, aps, i, config, valueClean):
        fig, ax = plt.subplots()
        fig.set_size_inches(7,6)
        ax = plt.gca()
        ax.cla()
        ax.set_xlim((config.lim_min_x, config.lim_max_x))
        ax.set_ylim((config.lim_min_y, config.lim_max_y))
        plot = Scenery()
        plot.plotagemAps(aps, ax, fig)
        plot.plotagemUsers(users, ax, fig)
        if (i < len(valueClean)):
            plot.plotagemSupervised(valueClean[i], ax, fig)
        #constroi o grafico
        plt.xlabel("Distance x (m)")
        plt.ylabel("Distance y (m)")
        nome = 'cenario.png'
        plt.title('Scenery ' + str(i))
        fig.savefig("./cenarios/" + str(i) + nome)
        plt.close()


    def plotagemSupervised(self, valueClean, ax, fig):
        ax.plot((valueClean.x), (valueClean.y), 'o', color='blue')
        pl.text(
            (valueClean.x), (valueClean.y),
            'supervised',
            color="black",
            fontsize=8)