from sklearn import datasets
iris = datasets.load_iris()
data = iris.data
print(data.shape)

digits = datasets.load_digits()
print(digits.images.shape)

import pylab as pl
print(pl.imshow(digits.images[-1], cmap=pl.cm.gray_r))

#To use this dataset with the scikit, we transform each 8x8 image into a feature vector of length 64
data = digits.images.reshape((digits.images.shape[0], -1))