pip install streamlit
import streamlit as st

# Datos de libros recomendados
libros = [
    {
        'titulo': 'Cien años de soledad',
        'autor': 'Gabriel García Márquez',
        'genero': 'Ficción',
        'duracion': 10,  # Duración estimada de lectura en horas
        'sinopsis': 'Una obra maestra que cuenta la historia de la familia Buendía en el ficticio pueblo de Macondo.',
        'imagen': 'https://via.placeholder.com/100x150.png?text=Cien+Años+de+Soledad'
    },
    {
        'titulo': '1984',
        'autor': 'George Orwell',
        'genero': 'Ciencia Ficción',
        'duracion': 8,
        'sinopsis': 'Una novela distópica que describe un mundo totalitario gobernado por el Partido, bajo la vigilancia constante de Big Brother.',
        'imagen': 'https://via.placeholder.com/100x150.png?text=1984'
    },
    {
        'titulo': 'La sombra del viento',
        'autor': 'Carlos Ruiz Zafón',
        'genero': 'Misterio',
        'duracion': 12,
        'sinopsis': 'Un joven descubre un libro olvidado en un cementerio de libros, lo que lo lleva a investigar un misterio relacionado con la historia del autor.',
        'imagen': 'https://via.placeholder.com/100x150.png?text=La+sombra+del+viento'
    },
    {
        'titulo': 'Sapiens: De animales a dioses',
        'autor': 'Yuval Noah Harari',
        'genero': 'No Ficción',
        'duracion': 15,
        'sinopsis': 'Un recorrido por la historia de la humanidad, desde la Edad de Piedra hasta la revolución moderna.',
        'imagen': 'https://via.placeholder.com/100x150.png?text=Sapiens'
    },
    {
        'titulo': 'El principito',
        'autor': 'Antoine de Saint-Exupéry',
        'genero': 'Ficción',
        'duracion': 2,
        'sinopsis': 'La historia de un niño que viaja por el universo y aprende valiosas lecciones sobre la vida y la amistad.',
        'imagen': 'https://via.placeholder.com/100x150.png?text=El+principito'
    },
    {
        'titulo': 'El código Da Vinci',
        'autor': 'Dan Brown',
        'genero': 'Misterio',
        'duracion': 8,
        'sinopsis': 'Un thriller de misterio en el que el profesor Robert Langdon debe resolver un enigma relacionado con el famoso cuadro de Da Vinci.',
        'imagen': 'https://via.placeholder.com/100x150.png?text=El+codigo+Da+Vinci'
    },
    {
        'titulo': 'Breves respuestas a las grandes preguntas',
        'autor': 'Stephen Hawking',
        'genero': 'No Ficción',
        'duracion': 4,
        'sinopsis': 'Stephen Hawking explora algunas de las cuestiones más fundamentales sobre el universo, la vida y el futuro.',
        'imagen': 'https://via.placeholder.com/100x150.png?text=Breves+respuestas'
    },
    {
        'titulo': 'El hobbit',
        'autor': 'J.R.R. Tolkien',
        'genero': 'Ficción',
        'duracion': 7,
        'sinopsis': 'La aventura de Bilbo Bolsón, un hobbit que se embarca en un viaje inesperado para recuperar un tesoro robado.',
        'imagen': 'https://via.placeholder.com/100x150.png?text=El+hobbit'
    }
]

# Función para recomendar libros en base al género y duración de lectura
def recomendar_libros(genero, duracion):
    libros_recomendados = []
    
    for libro in libros:
        if libro['genero'] == genero and libro['duracion'] <= duracion:
            libros_recomendados.append(libro)
    
    return libros_recomendados

# Título y descripción de la app
st.title('Recomendador de Libros')
st.markdown("""
    Selecciona un género y una duración de lectura para recibir recomendaciones de libros. 
    Puedes elegir el tipo de lectura que más te convenga según el tiempo que tengas disponible.
""")

# Selección de género de libro
genero = st.selectbox('Selecciona el género de libro', ['Ficción', 'No Ficción', 'Ciencia Ficción', 'Misterio'])

# Selección de duración de lectura
duracion = st.select_slider('Selecciona la duración de lectura (en horas)', 
                            options=[1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 15],
                            value=5)

# Botón para obtener recomendaciones
if st.button('Obtener Recomendaciones'):
    libros_recomendados = recomendar_libros(genero, duracion)
    
    if libros_recomendados:
        st.write(f"Libros recomendados para género '{genero}' y duración de lectura de hasta {duracion} horas:")
        
        # Mostrar libros recomendados
        for libro in libros_recomendados:
            st.image(libro['imagen'], width=100)
            st.subheader(libro['titulo'])
            st.write(f"**Autor:** {libro['autor']}")
            st.write(f"**Duración estimada de lectura:** {libro['duracion']} horas")
            st.write(f"**Sinopsis:** {libro['sinopsis']}")
            st.write("---")
    else:
        st.write("No hay libros recomendados que coincidan con tu selección.")
