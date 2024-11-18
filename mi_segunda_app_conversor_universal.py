import streamlit as st

# Título de la app
st.title("Convertidor Universal")

# Seleccionar categoría
categoria = st.selectbox(
    "Selecciona una categoría",
    [
        "Conversiones de temperatura",
        "Conversiones de longitud",
        "Conversiones de peso/masa",
        "Conversiones de volumen",
        "Conversiones de tiempo",
        "Conversiones de velocidad",
        "Conversiones de área",
        "Conversiones de energía",
        "Conversiones de presión",
        "Conversiones de tamaño de datos"
    ]
)

# Diccionario con opciones de conversión y sus funciones
conversiones = {
    "Conversiones de temperatura": {
        "Celsius a Fahrenheit": lambda c: c * 9 / 5 + 32,
        "Fahrenheit a Celsius": lambda f: (f - 32) * 5 / 9,
        "Celsius a Kelvin": lambda c: c + 273.15,
        "Kelvin a Celsius": lambda k: k - 273.15
    },
    "Conversiones de longitud": {
        "Pies a metros": lambda ft: ft * 0.3048,
        "Metros a pies": lambda m: m / 0.3048,
        "Pulgadas a centímetros": lambda in_: in_ * 2.54,
        "Centímetros a pulgadas": lambda cm: cm / 2.54
    },
    "Conversiones de peso/masa": {
        "Libras a kilogramos": lambda lb: lb * 0.453592,
        "Kilogramos a libras": lambda kg: kg / 0.453592,
        "Onzas a gramos": lambda oz: oz * 28.3495,
        "Gramos a onzas": lambda g: g / 28.3495
    },
    "Conversiones de volumen": {
        "Galones a litros": lambda gal: gal * 3.78541,
        "Litros a galones": lambda l: l / 3.78541,
        "Pulgadas cúbicas a centímetros cúbicos": lambda cu_in: cu_in * 16.3871,
        "Centímetros cúbicos a pulgadas cúbicas": lambda cu_cm: cu_cm / 16.3871
    },
    "Conversiones de tiempo": {
        "Horas a minutos": lambda hr: hr * 60,
        "Minutos a segundos": lambda min_: min_ * 60,
        "Días a horas": lambda d: d * 24,
        "Semanas a días": lambda wk: wk * 7
    },
    "Conversiones de velocidad": {
        "Millas por hora a kilómetros por hora": lambda mph: mph * 1.60934,
        "Kilómetros por hora a metros por segundo": lambda kph: kph / 3.6,
        "Nudos a millas por hora": lambda knots: knots * 1.15078,
        "Metros por segundo a pies por segundo": lambda mps: mps * 3.28084
    },
    "Conversiones de área": {
        "Metros cuadrados a pies cuadrados": lambda m2: m2 * 10.7639,
        "Pies cuadrados a metros cuadrados": lambda ft2: ft2 / 10.7639,
        "Kilómetros cuadrados a millas cuadradas": lambda km2: km2 * 0.386102,
        "Millas cuadradas a kilómetros cuadrados": lambda mi2: mi2 / 0.386102
    },
    "Conversiones de energía": {
        "Julios a calorías": lambda j: j / 4.184,
        "Calorías a kilojulios": lambda cal: cal * 0.004184,
        "Kilovatios-hora a megajulios": lambda kwh: kwh * 3.6,
        "Megajulios a kilovatios-hora": lambda mj: mj / 3.6
    },
    "Conversiones de presión": {
        "Pascales a atmósferas": lambda pa: pa / 101325,
        "Atmósferas a pascales": lambda atm: atm * 101325,
        "Barras a libras por pulgada cuadrada": lambda bar: bar * 14.5038,
        "Libras por pulgada cuadrada a bares": lambda psi: psi / 14.5038
    },
    "Conversiones de tamaño de datos": {
        "Megabytes a gigabytes": lambda mb: mb / 1024,
        "Gigabytes a Terabytes": lambda gb: gb / 1024,
        "Kilobytes a megabytes": lambda kb: kb / 1024,
        "Terabytes a petabytes": lambda tb: tb / 1024
    }
}

# Seleccionar tipo de conversión
tipo_conversion = st.selectbox(
    "Selecciona un tipo de conversión",
    list(conversiones[categoria].keys())
)

# Introducir valor
valor = st.number_input(f"Introduce el valor para convertir ({tipo_conversion})", format="%.4f")

# Realizar conversión
if st.button("Convertir"):
    resultado = conversiones[categoria][tipo_conversion](valor)
    st.success(f"El resultado de la conversión es: {resultado:.4f}")

#App realizada por Joseph Vargas con chatGPT
