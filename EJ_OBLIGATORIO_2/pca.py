import numpy as np

def getPrincipalComponent(pcIndex,pcCoeficients,countryValues):
    return np.dot(pcCoeficients[pcIndex],countryValues)