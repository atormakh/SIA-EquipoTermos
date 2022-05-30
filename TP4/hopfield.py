import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculateWeights(patterns):
    W=np.zeros((25,25))
    for pattern in patterns:
        w_aux=np.dot(np.transpose(np.matrix(pattern)),np.matrix(pattern))
        W=W + w_aux
    division = np.vectorize(lambda m:m/25)
    W= division(W)
    return W

def propagatePattern(W,pattern):
    results = []
    energies = []
    prevResult = sgn(np.matmul(W,pattern))
    currentResult=None
    results.append(prevResult)
    energies.append(calculateEnergy(W,np.transpose(pattern)))
    energies.append(calculateEnergy(W,np.transpose(prevResult)))
    while currentResult is None or  not (prevResult==currentResult).all():
        if currentResult is not  None:
            prevResult=currentResult
        currentResult=sgn(np.matmul(prevResult,W))
        energies.append(calculateEnergy(W,np.transpose(currentResult)))
        results.append(currentResult)
    return (results,energies)

def sgn(pattern):
    sgn = lambda x: -1 if x<=0 else 1
    sgn_v= np.vectorize(sgn)
    return sgn_v(pattern)


def addNoise(probability,pattern):
    return np.vectorize(lambda x: x*-1 if np.random.random() < probability else x)(pattern.copy())

def printLetter(alphabetASCII,index):
    output=[]
    for i in range(0,5):
        output.append(f"{''.join(alphabetASCII[index][i*5:i*5+5])}\n")
    return "".join(output)
def printLetterBipolar(alphabetASCIIBipolar,index):
    output=[]
    for i in range(0,5):
        output.append(f"{''.join(str(alphabetASCIIBipolar[index][i*5:i*5+5]))}\n")
    return "".join(output)
def printLetterBipolarMatrix(alphabet):
    output=[]
    for i in range(0,5):
        output.append(f"{''.join(str(alphabet.A[0][i*5:i*5+5]))}\n")
    return "".join(output)

def plotLetterMap(letter_arr,axes=None):
    if axes is None:
        sns.heatmap(data=np.reshape(letter_arr,(5,5)),cmap=sns.color_palette("Greens"))
    else:
        sns.heatmap(ax=axes,data=np.reshape(letter_arr,(5,5)),cmap=sns.color_palette("Greens"))

def plotEnergy(energies,patternLetters):
    energyData = {
        'energy':[], 
        'iterations':[],
        'letters':[]
    }

    for i in range(0,len(patternLetters)):
        letterEnergies= energies[i]
        for j in range(0,len(letterEnergies)):
            energyData["energy"].append(letterEnergies[j])
            energyData["iterations"].append(j)
            energyData["letters"].append(patternLetters[i])

    energyDataDF = pd.DataFrame(energyData)

    plt.figure(figsize = (15,9))
    plt.title(f"Energia vs Iteraciones")
    sns.lineplot(data=energyDataDF, x="iterations", y="energy",hue="letters")


def plotSpuriousStatesCountPerNoiseProbability(patterns_letters,noiseProbabilities,spuriousStatesCount):
    data = {
        'patterns':[],
        'Probabilidad de ruido':[],
        'Proporcion de estados espureos':[]
    }

    for p in range(0,len(patterns_letters)):
        pattern="".join(patterns_letters[p])
        for i in range(0,len(noiseProbabilities)):
            data['Proporcion de estados espureos'].append(spuriousStatesCount[p][i]*100)
            data['Probabilidad de ruido'].append(noiseProbabilities[i])
            data['patterns'].append(pattern)

    spuriousStatesCountDataDF = pd.DataFrame(data)

    plt.figure(figsize = (15,9))
    plt.title(f"Proporcion de estados espureos (%) vs Probabilidad de ruido")
    plt.ylabel("Proporcion de estados espureos (%)")
    sns.lineplot(data=spuriousStatesCountDataDF, x="Probabilidad de ruido", y="Proporcion de estados espureos",hue="patterns")



def calculateEnergy(W,state):
    energy = 0
    for (rowIndex,row) in enumerate(W):
        currentEnergy = (np.dot(row,state)*state[rowIndex])
        energy += currentEnergy.item((0, 0))
    return (-0.5) * energy


def isPattern(currentPattern,savedPatterns):
    aux = np.array(currentPattern)
    for i in range(0,len(savedPatterns)):
        if((aux==savedPatterns[i]).all()):
            return True
    return False