import numpy as np

x= np.array([1,2,3,4,5])
y= np.array([2,4,6,8,10])

m, b = 0.0,0.0
learning_rate = 0.01
epochs = 1000
n= len(x)

for i in range(epochs):
    y_pred = m * x + b
    loss = np.mean((y-y_pred)**2)

    dm = (-2/n) * sum(x*(y-y_pred))
    db = (-2/n) * sum(y-y_pred)

    m = m- learning_rate*dm
    b = b- learning_rate*db

    if i % 100 == 0:
        print(f"Epoch {i}: Loss {loss:.4f}, m {m:.2f}, b{b:.2f}")

print(f"\nFinal result: y = {m: .2f}x + {b:.2f}")