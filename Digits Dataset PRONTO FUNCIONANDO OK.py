from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
import numpy as np
import matplotlib.image as mimg
from sklearn.linear_model import LogisticRegression

base = datasets.load_digits()
entradas = base.data
saidas = base.target

plt.figure(figsize = (2,2))
plt.imshow(base.images[0],
           cmap = plt.cm.gray_r)

etreino,eteste,streino,steste = train_test_split(entradas,
                                                 saidas,
                                                 test_size = 0.1,
                                                 random_state = 2)
classificador = svm.SVC()
classificador.fit(etreino,streino)
previsor = classificador.predict(eteste)
margem_acerto = metrics.accuracy_score(steste, previsor)

imagem = mimg.imread('num2.png')

def rgb2gray(rgb):
    img_array = np.dot(rgb[...,:3],[0.299,0.587,0.114])
    img_array = (16 - (img_array * 16)).astype(int)
    img_array = img_array.flatten()
    return img_array

rgb2gray(imagem)

identificador = svm.SVC()
identificador.fit(entradas,saidas)
previsor_id = identificador.predict([rgb2gray(imagem)])
print(previsor_id)

logr = LogisticRegression()
logr.fit(etreino,streino)
previsor_logr = logr.predict(eteste)
acerto_logr = metrics.accuracy_score(steste, previsor_logr)
print(acerto_logr)

regressor = LogisticRegression()
regressor.fit(entradas,saidas)
previsor_regl = regressor.predict([rgb2gray(imagem)])
print(previsor_regl)

