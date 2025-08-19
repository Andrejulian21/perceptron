import streamlit as st
import joblib
import numpy as np

# ---------------------------
#  Título y descripción
# ---------------------------
st.title("📘 Predicción de Graduación Universitaria")
st.write("""
Este modelo utiliza un perceptrón simple para predecir si un estudiante logrará **graduarse** 
en función de dos factores de entrada (valores entre 0 y 1).
""")

# ---------------------------
# Imagen alusiva
# ---------------------------
st.image("graduacion.jpg", caption="¡Meta alcanzada!", use_container_width=True)

# ---------------------------
# Cargar modelo
# ---------------------------
modelo = joblib.load("primermillon.joblib")  # asegúrate que este nombre coincida con tu archivo en GitHub

# ---------------------------
# Sliders de entrada
# ---------------------------
st.subheader("Ingresa los datos del estudiante")
x1 = st.slider("📊 Nota IA", 0.0, 1.0, 0.5, 0.1)
x2 = st.slider("📊 PGA", 0.0, 1.0, 0.5, 0.1)

# ---------------------------
# Predicción
# ---------------------------
if st.button("🔮 Predecir"):
    entrada = np.array([[x1, x2]])
    prediccion = modelo.predict(entrada)[0]

    if prediccion == 1:
        st.success("🎓 ¡Sí se graduará!")
    else:
        st.error("❌ No se graduará")
