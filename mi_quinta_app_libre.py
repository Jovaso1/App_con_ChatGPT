import streamlit as st
# Autor de la aplicación
st.markdown("**Autor:** Esta app fue elaborada por Joseph Vargas")

# Lista de libros con detalles
libros = [
    {
        'titulo': 'Cien años de soledad',
        'autor': 'Gabriel García Márquez',
        'genero': 'Realismo Mágico',
        'anio': 1967,
        'resumen': 'Una novela que narra la historia de la familia Buendía en el pueblo ficticio de Macondo.',
        'paginas': 417,
        'idioma': 'Español'
    },
    {
        'titulo': 'Don Quijote de la Mancha',
        'autor': 'Miguel de Cervantes',
        'genero': 'Novela de caballería',
        'anio': 1605,
        'resumen': 'Las aventuras de un caballero que decide convertirse en justiciero, acompañado de su fiel escudero Sancho Panza.',
        'paginas': 1024,
        'idioma': 'Español'
    },
    {
        'titulo': '1984',
        'autor': 'George Orwell',
        'genero': 'Distopía',
        'anio': 1949,
        'resumen': 'Una novela que describe un futuro totalitario donde el gobierno controla todos los aspectos de la vida humana.',
        'paginas': 328,
        'idioma': 'Inglés'
    },
    {
        'titulo': 'Orgullo y prejuicio',
        'autor': 'Jane Austen',
        'genero': 'Romántico',
        'anio': 1813,
        'resumen': 'La historia de Elizabeth Bennet y su relación con el aristócrata Darcy, explorando temas como la clase social y el matrimonio.',
        'paginas': 432,
        'idioma': 'Inglés'
    }
]

# Título de la app
st.title('Biblioteca de Libros')

# Descripción de la app
st.markdown("""
    Esta es una app que te permite explorar una selección de libros.
    Puedes ver detalles sobre cada libro como el título, autor, género, año de publicación, número de páginas y un pequeño resumen.
""")

# Mostrar los libros disponibles en una lista desplegable
opciones_libros = [libro['titulo'] for libro in libros]
seleccion = st.selectbox('Selecciona un libro', opciones_libros)

# Buscar el libro seleccionado
libro_seleccionado = next(libro for libro in libros if libro['titulo'] == seleccion)

# Mostrar detalles del libro seleccionado
st.subheader(libro_seleccionado['titulo'])
st.write(f"**Autor:** {libro_seleccionado['autor']}")
st.write(f"**Género:** {libro_seleccionado['genero']}")
st.write(f"**Año de publicación:** {libro_seleccionado['anio']}")
st.write(f"**Número de páginas:** {libro_seleccionado['paginas']}")
st.write(f"**Idioma:** {libro_seleccionado['idioma']}")
st.write(f"**Resumen:** {libro_seleccionado['resumen']}")
