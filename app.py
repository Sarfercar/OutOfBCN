import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Mi Súper App", page_icon="👋", layout="centered")

# Título principal
st.title("Hey, IA 👋")

# Contenido principal
st.header("¡Bienvenido!")
nombre = st.text_input("¿Cómo te llamas?", key="nombre_input")

if nombre:
    st.success(f"¡Hola, {nombre}! Bienvenido/a a mi app.")
    st.balloons()  # ¡Efecto divertido!
