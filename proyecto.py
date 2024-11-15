import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de estilo para los gráficos
sns.set(style="whitegrid")

# Título de la aplicación
st.title("Análisis de Datos de Rendimiento del Sistema")

# Cargar el Conjunto de Datos
data = pd.read_csv("archivo_logs.csv")  # Reemplaza con la ruta de tu archivo de datos
st.write("### Primeros registros del conjunto de datos")
st.write(data.head())  # Mostrar los primeros registros en la interfaz

# Exploración Inicial
st.write("### Información del conjunto de datos")
st.write(data.info())
st.write("### Estadísticas descriptivas del conjunto de datos")
st.write(data.describe())

# Manejo de Valores Faltantes
# Rellenar valores faltantes en 'cpu_usage' con la media de la columna
data['cpu_usage'].fillna(data['cpu_usage'].mean(), inplace=True)

# Conversión de Fechas y Tiempos
# Convertir la columna 'timestamp' al tipo datetime
data['timestamp'] = pd.to_datetime(data['timestamp'])
data['hour'] = data['timestamp'].dt.hour

# Análisis Exploratorio de Datos (EDA)

# Gráfico 1: Distribución del Uso de CPU
st.write("### Distribución de Uso de CPU")
fig1, ax1 = plt.subplots()
sns.histplot(data['cpu_usage'], kde=True, ax=ax1)
ax1.set_title("Distribución de uso de CPU")
ax1.set_xlabel("Uso de CPU (%)")
ax1.set_ylabel("Frecuencia")
st.pyplot(fig1)

# Gráfico 2: Uso de CPU a lo largo del tiempo
st.write("### Uso de CPU a lo largo del tiempo")
fig2, ax2 = plt.subplots()
sns.lineplot(data=data, x="timestamp", y="cpu_usage", ax=ax2)
ax2.set_title("Uso de CPU a lo largo del tiempo")
ax2.set_xlabel("Tiempo")
ax2.set_ylabel("Uso de CPU (%)")
st.pyplot(fig2)

# Gráfico 3: Promedio de uso de CPU por hora
st.write("### Promedio de Uso de CPU por Hora")
fig3, ax3 = plt.subplots()
avg_cpu_by_hour = data.groupby('hour')['cpu_usage'].mean()
avg_cpu_by_hour.plot(kind="bar", ax=ax3)
ax3.set_title("Promedio de uso de CPU por hora")
ax3.set_xlabel("Hora del día")
ax3.set_ylabel("Promedio de uso de CPU (%)")
st.pyplot(fig3)

# Gráfico 4: Relación entre Uso de Memoria y Tiempo de Respuesta
st.write("### Relación entre Uso de Memoria y Tiempo de Respuesta")
fig4, ax4 = plt.subplots()
sns.scatterplot(data=data, x="memory_usage", y="response_time", ax=ax4)
ax4.set_title("Relación entre uso de memoria y tiempo de respuesta")
ax4.set_xlabel("Uso de Memoria (%)")
ax4.set_ylabel("Tiempo de Respuesta (ms)")
st.pyplot(fig4)

# Reflexión sobre el análisis
st.write("### Reflexión sobre el análisis")
st.write("""
1. La distribución del uso de CPU muestra un comportamiento típico, pero observamos algunos picos.
2. El uso de CPU varía a lo largo del día, siendo mayor en ciertas horas.
3. La relación entre uso de memoria y tiempo de respuesta sugiere que a mayor uso de memoria, el tiempo de respuesta podría incrementarse, indicando un posible cuello de botella.
""")
