import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('../data/plant_signals.csv')

# Plot electrical signals
plt.figure()
plt.plot(data['time'], data['electrical_signal'])
plt.title("Plant Electrical Signal Over Time")
plt.xlabel("Time")
plt.ylabel("Electrical Signal")
plt.show()

# Plot moisture vs temperature
plt.figure()
plt.scatter(data['moisture'], data['temperature'])
plt.title("Moisture vs Temperature")
plt.xlabel("Moisture")
plt.ylabel("Temperature")
plt.show()
