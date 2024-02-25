#GRAVITATIONAL ACCELERATION X
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data_trial1_11-19.xlsx')

df['Timestamp'] = df['Timestamp'].astype(str)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df['Timestamp'], df['GravitationalAccelerationX'], marker='o', linestyle='-')
plt.xticks(df['Timestamp'][::50])
plt.xlabel('Timestamp')
plt.ylabel('Gravitational Acceleration X')
plt.title('Gravitational Acceleration X plotted over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#GRAVITATIONAL ACCELERATION Y
df = pd.read_excel('data_trial1_11-19.xlsx')

df['Timestamp'] = df['Timestamp'].astype(str)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df['Timestamp'], df['GravitationalAccelerationY'], marker='o', linestyle='-')
plt.xticks(df['Timestamp'][::50])
plt.xlabel('Timestamp')
plt.ylabel('Gravitational Acceleration Y')
plt.title('Gravitational Acceleration Y plotted over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



#GRAVITATIONAL ACCELERATION Z
df = pd.read_excel('data_trial1_11-19.xlsx')

df['Timestamp'] = df['Timestamp'].astype(str)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df['Timestamp'], df['GravitationalAccelerationZ'], marker='o', linestyle='-')
plt.xticks(df['Timestamp'][::50])
plt.xlabel('Timestamp')
plt.ylabel('Gravitational Acceleration Z')
plt.title('Gravitational Acceleration Z plotted over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



#ROTATION X
df = pd.read_excel('data_trial1_11-19.xlsx')

df['Timestamp'] = df['Timestamp'].astype(str)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df['Timestamp'], df['RotationX'], marker='o', linestyle='-')
plt.xticks(df['Timestamp'][::50])
plt.xlabel('Timestamp')
plt.ylabel('Rotation X')
plt.title('Rotation X plotted over Time')
plt.xticks(rotation=45) 
plt.tight_layout()
plt.show()



#ROTATION Y
df = pd.read_excel('data_trial1_11-19.xlsx')

df['Timestamp'] = df['Timestamp'].astype(str)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df['Timestamp'], df['RotationY'], marker='o', linestyle='-')
plt.xticks(df['Timestamp'][::50])
plt.xlabel('Timestamp')
plt.ylabel('Rotation Y')
plt.title('Rotation Y plotted over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



#ROTATION Z
df = pd.read_excel('data_trial1_11-19.xlsx')

df['Timestamp'] = df['Timestamp'].astype(str)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df['Timestamp'], df['RotationZ'], marker='o', linestyle='-')
plt.xticks(df['Timestamp'][::50])
plt.xlabel('Timestamp')
plt.ylabel('Rotation Z')
plt.title('Rotation Z plotted over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()