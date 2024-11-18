import streamlit as st
import pandas as pd
from datetime import datetime

# Título de la app
st.title("Registro de Finanzas Personales")

# Autor de la aplicación
st.markdown("**Autor:** Esta app fue elaborada por Joseph Vargas")

# Descripción
st.markdown(
    """
    Bienvenido/a a tu registro de finanzas personales. 
    Aquí puedes llevar un control de tus ingresos, gastos, presupuestos y metas de ahorro, 
    además de generar reportes semanales y mensuales.
    """
)

# Inicialización de las bases de datos
if "finanzas" not in st.session_state:
    st.session_state.finanzas = pd.DataFrame(
        columns=["Fecha", "Tipo", "Categoría", "Monto", "Presupuesto"]
    )

if "metas" not in st.session_state:
    st.session_state.metas = pd.DataFrame(columns=["Meta", "Monto objetivo", "Fecha límite", "Progreso"])

# Función para agregar un registro financiero
def agregar_registro(fecha, tipo, categoria, monto, presupuesto):
    nuevo_registro = {
        "Fecha": fecha,
        "Tipo": tipo,
        "Categoría": categoria,
        "Monto": monto,
        "Presupuesto": presupuesto,
    }
    st.session_state.finanzas = pd.concat(
        [st.session_state.finanzas, pd.DataFrame([nuevo_registro])], ignore_index=True
    )

# Función para agregar una meta de ahorro
def agregar_meta(meta, monto_objetivo, fecha_limite):
    nueva_meta = {
        "Meta": meta,
        "Monto objetivo": monto_objetivo,
        "Fecha límite": fecha_limite,
        "Progreso": 0,
    }
    st.session_state.metas = pd.concat(
        [st.session_state.metas, pd.DataFrame([nueva_meta])], ignore_index=True
    )

# Sección de ingreso de datos
st.header("Registro de ingresos y gastos")

with st.form("registro_finanzas"):
    fecha = st.date_input("Fecha", datetime.today())
    tipo = st.selectbox("Tipo", ["Ingreso", "Gasto"])
    categoria = st.text_input("Categoría", "Ejemplo: Alquiler, Sueldo, Comida")
    monto = st.number_input("Monto ($)", min_value=0.0, step=0.01, format="%.2f")
    presupuesto = st.number_input(
        "Presupuesto asociado ($)", min_value=0.0, step=0.01, format="%.2f"
    )
    submit = st.form_submit_button("Agregar")

    if submit:
        agregar_registro(fecha, tipo, categoria, monto, presupuesto)
        st.success("Registro agregado exitosamente.")

# Sección de metas de ahorro
st.header("Metas de ahorro")

with st.form("registro_metas"):
    meta = st.text_input("Nombre de la meta")
    monto_objetivo = st.number_input("Monto objetivo ($)", min_value=0.0, step=0.01, format="%.2f")
    fecha_limite = st.date_input("Fecha límite")
    submit_meta = st.form_submit_button("Agregar meta")

    if submit_meta:
        agregar_meta(meta, monto_objetivo, fecha_limite)
        st.success("Meta agregada exitosamente.")

# Visualización de reportes
st.header("Reportes")

# Resumen semanal y mensual
st.subheader("Resumen semanal y mensual")
finanzas = st.session_state.finanzas.copy()

# Calcular diferencias entre lo presupuestado y lo real
finanzas["Diferencia"] = finanzas["Presupuesto"] - finanzas["Monto"]
finanzas["Semana"] = pd.to_datetime(finanzas["Fecha"]).dt.isocalendar().week
finanzas["Mes"] = pd.to_datetime(finanzas["Fecha"]).dt.month

# Reporte semanal
if not finanzas.empty:
    reporte_semanal = finanzas.groupby("Semana")[["Monto", "Presupuesto", "Diferencia"]].sum()
    reporte_mensual = finanzas.groupby("Mes")[["Monto", "Presupuesto", "Diferencia"]].sum()

    st.write("**Reporte semanal**")
    st.dataframe(reporte_semanal)

    st.write("**Reporte mensual**")
    st.dataframe(reporte_mensual)
else:
    st.info("No hay datos disponibles para generar reportes.")

# Mostrar metas de ahorro
st.subheader("Progreso de metas de ahorro")
if not st.session_state.metas.empty:
    metas = st.session_state.metas.copy()
    st.dataframe(metas)
else:
    st.info("No hay metas de ahorro registradas.")

#App hecha con ayuda de chatGPT
