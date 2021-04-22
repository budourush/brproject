import numpy as np

random_state = 1

X = [1, 2, 3, 4, 5, 6]

rgen = np.random.RandomState(random_state)
print(rgen)
w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + len(X))
print(w_)

from sklearn import datasets
import numpy as np

iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
print(X)