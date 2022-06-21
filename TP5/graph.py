import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def plotErrorAgainstSteps(errors,steps):
    data = {
        'errors':[], 
        'steps':[]
    }

    for i in range(0,len(steps)):
        data["errors"].append(errors[i])
        data["steps"].append(steps[i])

    dataDF = pd.DataFrame(data)

    plt.figure(figsize = (15,9))
    plt.title(f"Error vs Steps")
    sns.lineplot(data=dataDF, x="steps", y="errors")

def plotErrorsAgainstSteps(autoencoderManagers,autoencoderManagersArchitectures):
    errorData = {
    'error':[], 
    'iterations':[],
    'architecture':[]
    }

    for i in range(0,len(autoencoderManagers)):
        for j in range(0,len(autoencoderManagers[i].errors)):
            errorData["error"].append(autoencoderManagers[i].errors[j])
            errorData["iterations"].append(j)
            errorData["architecture"].append(autoencoderManagersArchitectures[i])

    errorDataDF = pd.DataFrame(errorData)

    plt.figure(figsize = (15,9))
    plt.title(f"Errores vs Iteraciones")
    sns.lineplot(data=errorDataDF, x="iterations", y="error",hue="architecture")
