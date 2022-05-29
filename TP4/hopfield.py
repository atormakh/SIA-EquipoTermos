import seaborn as sns
import numpy as np

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