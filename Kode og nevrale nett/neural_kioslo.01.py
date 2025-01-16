"""
Jeg vil ha et nevralt nettverk som er slik at * det er noen , la oss si to mennesker som melder fra til deg om det brenner eller ikke * det er "input" i det nevrale nettverket * Disse menneskene har ulike egenskaper: den en lyver alltid, den andre snakker random sant eller ikke den tredje snakker ofte sant DU skal vurderer om det er brann Gi meg python-kode for dette med tensorflow
"""
import numpy as np
import tensorflow as tf
from tensorflow import keras

# Generere treningsdata
# Dataformat: [Person 1, Person 2, Person 3] -> [Brann (1), Ingen brann (0)]
# Person 1 lyver alltid, Person 2 snakker tilfeldig, Person 3 snakker oftest sant
def generate_data(num_samples):
    data = []
    labels = []
    
    for _ in range(num_samples):
        # Generer meldinger
        is_fire = np.random.randint(2)  # 0 eller 1
        person1 = 1 - is_fire  # Person 1 lyver alltid
        person2 = np.random.randint(2)  # Person 2 random
        person3 = np.random.choice([is_fire, is_fire, is_fire, 1-is_fire])  # Person 3 snakker oftest sant
        
        # Lag input og output
        data.append([person1, person2, person3])
        labels.append(is_fire)
    
    return np.array(data, dtype=float), np.array(labels)

# Generere dataene
X_train, y_train = generate_data(1000)
X_test, y_test = generate_data(200)

# Bygge det nevrale nettverket
model = keras.Sequential([
    keras.layers.Dense(4, activation='relu', input_shape=(3,)),  # 3 input features
    keras.layers.Dense(4, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')  # Output layer for binary classification
])

# Kompilere modellen
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Trene modellen
model.fit(X_train, y_train, epochs=50, batch_size=10, validation_split=0.2)

# Evaluere modellen
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test accuracy: {accuracy:.4f}')

# Predikere nye data
# Eksempel på nye meldinger fra de tre personene
new_data = np.array([[1, 0, 1]])  # Person 1 sier det brenner, Person 2 sier det er klart, Person 3 sier det faktisk brenner
prediction = model.predict(new_data)
print(f'Prediksjon (brann): {prediction[0][0]:.4f}')