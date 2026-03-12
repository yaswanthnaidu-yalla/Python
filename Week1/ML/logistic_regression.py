import numpy as np

x = np.array([1, 2, 3, 4, 5, 6], dtype=float)
y = np.array([0, 0, 0, 1, 1, 1], dtype=float)

m, b = 0.0, 0.0
learning_rate = 0.5
epochs = 1000
n = len(x)

for i in range(epochs):
    z = m * x + b
    y_pred = 1 / (1 + np.exp(-z))
    loss = -np.mean(y * np.log(y_pred + 1e-9) + (1 - y) * np.log(1 - y_pred + 1e-9))

    dm = (1/n) * np.dot(x, (y_pred - y))
    db = (1/n) * np.sum(y_pred - y)

    m=m-(learning_rate*dm)
    b=b-(learning_rate*db)


    if i % 100 == 0:
        print(f"Epoch {i}: Loss {loss:.4f}")

print(f"\nFinal Model: Probability = Sigmoid({m:.2f}x + {b:.2f})")


#1,2,3 as fail, 4,5,6 as pass. the data in x is study hours.
#from the output , we find that the tipping point/decision boundary is 3.45 hrs.