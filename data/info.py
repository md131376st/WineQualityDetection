import matplotlib.pyplot as plt
import numpy as np


def LoadData():
    data = np.genfromtxt( './Train.txt', delimiter="," )
    return (data[:, -1].T, data[:, :-1].T)


L, D = LoadData()
featuresBadWine = D[:, L == 0]
featuresGoodWine = D[:, L == 1]
nameFeatures = ['fixed acidity',
                'volatile acidity',
                'citric acid',
                'residual sugar',
                'chlorides',
                'free sulfur dioxide',
                'total sulfur dioxide',
                'density',
                'pH',
                'sulphates',
                'alcohol']
plt.figure()
for f in range( 11 ):
    plt.hist( featuresBadWine[f], bins=20, density=True, alpha=0.4 )
    plt.hist( featuresGoodWine[f], bins=20, density=True, alpha=0.4 )
    plt.legend( ['Bad', 'Good'] )
    plt.xlabel( nameFeatures[f] )
    plt.show()
    plt.savefig( "plot/"+nameFeatures[f] )
