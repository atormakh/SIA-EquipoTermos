import numpy as np
import matplotlib.pyplot as plt

def getPrincipalComponent(pcIndex,pcCoeficients,countryValues):
    return np.dot(pcCoeficients[pcIndex],countryValues)

def biplot2D(score,coeff,labels=None, marker_labels = None):
    xs = score[:,0]
    ys = score[:,1]
    n = coeff.shape[0]
    scalex = 1.0/(xs.max() - xs.min())
    scaley = 1.0/(ys.max() - ys.min())
    fig, ax = plt.subplots(figsize=(28,28))
    ax.scatter(xs * scalex,ys * scaley,color='orange')
    for i in range(n):
        plt.arrow(0, 0, coeff[i,0], coeff[i,1],color = 'b',alpha = 0.5)
        if labels is None:
            plt.text(coeff[i,0]* 1.05, coeff[i,1] * 1.05, "Var"+str(i+1), color = 'g', ha = 'center', va = 'center',fontsize=12)
        else:
            plt.text(coeff[i,0]* 1.05, coeff[i,1] * 1.05, labels[i], color = 'g', ha = 'center', va = 'center',fontsize=25)

    if marker_labels is not None:
        for i, txt in enumerate(marker_labels):
            ax.annotate(txt, (xs[i]* scalex, scaley * ys[i]), fontsize=20)


    plt.xlim(-.6,.6)
    plt.ylim(-.6,.7)
    plt.xlabel("PC{}".format(1),fontsize=20)
    plt.ylabel("PC{}".format(2),fontsize=20)

    plt.grid()