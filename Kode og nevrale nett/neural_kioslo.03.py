"""
Ledetekst: Forrige ledetekst var:
Jeg vil ha et nevralt nettverk som med 1 input-node, to i skjult lag og en output-node
Nettverket skal tilpasses et datasett som er slik at input er mellom 0 og 1 og output skal teoretisk sett være lik 4x(x-1). Jeg trenger et program der jeg kan finne vekter og bias og stille inn for denne situasjonen. Python, tensorflow

Jeg sa videre "The program stops befofre doing anything, it does ot terminate" til forrige kode og fikk dette
"""
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt

# Generate dataset
def generate_data(samples=1000):
    X = np.linspace(0, 1, num=samples).reshape(-1, 1)  # Input between 0 and 1, reshape for compatibility
    y = 4 * X * (X - 1)  # Output = 4x(x-1)
    return X, y

# Create training data
X, y = generate_data()

# Define the neural network model
model = keras.Sequential([
    layers.Input(shape=(1,)),             # 1 input node
    layers.Dense(10, activation='relu'),    # First hidden layer with 10 nodes
    layers.Dense(10, activation='relu'),    # Second hidden layer with 10 nodes
    layers.Dense(1)                         # 1 output node
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X, y, epochs=1000, verbose=1)  # Set verbose=1 to see training progress

# Predict values to see how the model performs
predictions = model.predict(X)

# Compare with actual values
plt.figure(figsize=(10, 5))
plt.scatter(X, y, label='Actual Values', color='red')
plt.scatter(X, predictions, label='Predictions', color='blue', alpha=0.5)
plt.title('Neural Network Predictions vs Actual Values')
plt.xlabel('Input (x)')
plt.ylabel('Output (4x(x-1))')
plt.legend()
plt.grid()
plt.show()