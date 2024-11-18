import streamlit as st
from datetime import datetime, timedelta

# Inicializa una lista para almacenar los cumpleaños
if 'cumpleaños' not in st.session_state:
    st.session_state['cumpleaños'] = []

# Función para agregar un cumpleaños a la lista
def agregar_cumpleaños(nombre, fecha):
    cumpleaños = {'nombre': nombre, 'fecha': fecha}
    st.session_state['cumpleaños'].append(cumpleaños)

# Función para encontrar el cumpleaños más próximo
def obtener_cumpleaños_proximo():
    hoy = datetime.now()
    proximos_cumpleaños = []
    
    for cumple in st.session_state['cumpleaños']:
        # Calcula el próximo cumpleaños
        proximo_cumple = cumple['fecha'].replace(year=hoy.year)
        
        # Si el cumpleaños ya pasó este año, lo movemos al próximo
        if proximo_cumple < hoy:
            proximo_cumple = proximo_cumple.replace(year=hoy.year + 1)
        
        proximos_cumpleaños.append({'nombre': cumple['nombre'], 'fecha': proximo_cumple})
    
    # Ordena por la fecha del próximo cumpleaños
    proximos_cumpleaños.sort(key=lambda x: x['fecha'])
    
    return proximos_cumpleaños

# Título y descripción de la app
st.title('Registro de Cumpleaños')
st.markdown("""
    Esta aplicación te permite registrar cumpleaños y te muestra el próximo cumpleaños.
    Puedes agregar varios cumpleaños y la aplicación te indicará cuál es el siguiente en el calendario.
""")

# Formulario para agregar un cumpleaños
with st.form(key='form_cumpleaños'):
    nombre = st.text_input("Nombre del Cumpleañero")
    fecha = st.date_input("Fecha de Cumpleaños", min_value=datetime(1900, 1, 1))
    submit_button = st.form_submit_button(label="Agregar Cumpleaños")
    
    if submit_button:
        agregar_cumpleaños(nombre, fecha)
        st.success(f'Cumpleaños de {nombre} agregado correctamente!')

# Mostrar todos los cumpleaños registrados
if st.session_state['cumpleaños']:
    st.subheader('Cumpleaños registrados:')
    for cumple in st.session_state['cumpleaños']:
        st.write(f"{cumple['nombre']} - {cumple['fecha']}")

# Mostrar el cumpleaños más próximo
if st.session_state['cumpleaños']:
    proximos_cumpleaños = obtener_cumpleaños_proximo()
    st.subheader('Próximo Cumpleaños:')
    
    if proximos_cumpleaños:
        proximo = proximos_cumpleaños[0]
        st.write(f"El próximo cumpleaños es de {proximo['nombre']} el {proximo['fecha'].strftime('%d de %B, %Y')}.")
    else:
        st.write("No hay cumpleaños registrados aún.")
