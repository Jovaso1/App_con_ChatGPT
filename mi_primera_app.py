import streamlit as st

# Título de la aplicación
st.title("Mi primera app")

# Autor de la aplicación
st.markdown("**Autor:** Esta app fue elaborada por Joseph")

# Entrada del usuario para preguntar el nombre
nombre_usuario = st.text_input("¿Cómo te llamas?", "")

# Mostrar mensaje de bienvenida si el usuario escribe su nombre
if nombre_usuario:
    st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.")
