import streamlit as st
import pandas as pd

# Título de la app
st.title("Cálculo del PAPA")

# Autor de la aplicación
st.markdown("**Autor:** Esta app fue elaborada por Joseph Vargas")

# Descripción
st.markdown(
    """
    Esta aplicación permite calcular tu PAPA (Promedio Académico Ponderado Acumulado) 
    a partir de las materias vistas, sus calificaciones, créditos y tipologías. 
    Puedes calcular tanto el PAPA global como el PAPA por tipología de asignatura.
    """
)

# Inicialización de la base de datos
if "materias" not in st.session_state:
    st.session_state.materias = pd.DataFrame(
        columns=["Materia", "Calificación", "Créditos", "Tipología"]
    )

# Función para agregar una materia
def agregar_materia(materia, calificacion, creditos, tipologia):
    nueva_materia = {
        "Materia": materia,
        "Calificación": calificacion,
        "Créditos": creditos,
        "Tipología": tipologia,
    }
    st.session_state.materias = pd.concat(
        [st.session_state.materias, pd.DataFrame([nueva_materia])], ignore_index=True
    )

# Sección de ingreso de datos
st.header("Registro de materias")

with st.form("registro_materias"):
    materia = st.text_input("Nombre de la materia")
    calificacion = st.number_input(
        "Calificación (0.0 - 5.0)", min_value=0.0, max_value=5.0, step=0.1, format="%.1f"
    )
    creditos = st.number_input("Número de créditos", min_value=1, step=1)
    tipologia = st.selectbox(
        "Tipología de la asignatura", ["Disciplinar optativa", "Disciplinar obligatoria", "Libre elección", "Fundamental obligatoria", "Fundamental optativa"]
    )
    submit = st.form_submit_button("Agregar materia")

    if submit:
        agregar_materia(materia, calificacion, creditos, tipologia)
        st.success(f"Matteria '{materia}' agregada exitosamente.")

# Mostrar materias registradas
st.header("Materias registradas")
if not st.session_state.materias.empty:
    st.dataframe(st.session_state.materias)
else:
    st.info("Aún no has registrado materias.")

# Cálculo del PAPA global y por tipología
st.header("Cálculo del PAPA")

if not st.session_state.materias.empty:
    materias = st.session_state.materias.copy()
    
    # Cálculo del PAPA global
    materias["Ponderación"] = materias["Calificación"] * materias["Créditos"]
    papa_global = materias["Ponderación"].sum() / materias["Créditos"].sum()
    st.subheader("PAPA Global")
    st.success(f"Tu PAPA global es: {papa_global:.2f}")

    # Cálculo del PAPA por tipología
    st.subheader("PAPA por Tipología")
    papa_tipologia = (
        materias.groupby("Tipología").apply(
            lambda df: (df["Calificación"] * df["Créditos"]).sum() / df["Créditos"].sum()
        )
    )
    st.dataframe(papa_tipologia.reset_index().rename(columns={0: "PAPA"}))
else:
    st.info("Registra materias para calcular el PAPA.")
#Ayuda de ChatGPT
