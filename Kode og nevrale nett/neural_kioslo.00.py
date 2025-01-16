"""
give me python code for a simple neural networ with two inputs, three nodes in hidden layer and one output
"""
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Define the model
model = keras.Sequential([
    layers.Input(shape=(2,)),  # Input layer with 2 inputs
    layers.Dense(3, activation='relu'),  # Hidden layer with 3 nodes and ReLU activation
    layers.Dense(1, activation='sigmoid')  # Output layer with 1 output node and sigmoid activation
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Generate some dummy data for training
# Let's create a simple dataset (X) and labels (y)
# For example, we can use some arbitrary binary labels

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # 2 inputs
y = np.array([[0], [1], [1], [0]])  # Labels for XOR operation

# Train the model
model.fit(X, y, epochs=1000, verbose=0)

# Test the model
predictions = model.predict(X)
print("Predictions after training:")
print(predictions)