import seaborn as sns
import numpy as np

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
    prevResult = sgn(np.matmul(W,pattern))
    currentResult=None
    results.append(prevResult)
    while currentResult is None or  not (prevResult==currentResult).all() :
        if currentResult is not  None:
            prevResult=currentResult
        currentResult=sgn(np.matmul(prevResult,W))
        results.append(currentResult)
    return results

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