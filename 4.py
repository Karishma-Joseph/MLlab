import numpy as np
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([.92], [.86], [.89]), dtype=float)
X = X/np.amax(X, axis=0)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def der_sigmoid(x):
    return x * (1 - x)


epoch = 5000
lr = 0.01
i_layer_neurons = 2
h_layer_neurons = 3
o_layer_neurons = 1

weight_h = np.random.uniform(size=(i_layer_neurons, h_layer_neurons))
bias_h = np.random.uniform(size=(1, h_layer_neurons))
weight_o = np.random.uniform(size=(h_layer_neurons, o_layer_neurons))
bias_o = np.random.uniform(size=(1, o_layer_neurons))

for i in range(epoch):
    inp_h = np.dot(X, weight_h) + bias_h
    out_h = sigmoid(inp_h)

    inp_o = np.dot(out_h, weight_o) + bias_o
    out_o = sigmoid(inp_o)

    err_o = y - out_o
    gradient_o = der_sigmoid(out_o)
    delta_o = err_o * gradient_o

    err_h = delta_o.dot(weight_o.T)
    gradient_h = der_sigmoid(out_h)
    delta_h = err_h * gradient_h

    weight_o += out_h.T.dot(delta_o) * lr
    weight_h += X.T.dot(delta_h) * lr

print('Input: ', X)
print('Actual: ', y)
print('Predicted: ', out_o)
