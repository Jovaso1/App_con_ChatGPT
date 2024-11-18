pip install numpy pygame streamlit
import streamlit as st
import pygame
import numpy as np

# Inicializamos pygame
pygame.init()

# Dimensiones de la pantalla
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Inicialización de la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Definición de la clase del Tetris
class Tetris:
    def __init__(self):
        self.board = np.zeros((20, 10))  # Tablero de juego vacío
        self.game_over = False
        self.current_block = self.new_block()

    def new_block(self):
        """Genera un nuevo bloque"""
        block_type = np.random.choice([1, 2, 3, 4])  # Varias formas de bloques
        # Definimos una forma de bloque simple (por ejemplo, un bloque en forma de "T")
        if block_type == 1:
            return np.array([[1, 1, 1], [0, 1, 0]])
        elif block_type == 2:
            return np.array([[1, 1], [1, 1]])
        elif block_type == 3:
            return np.array([[1, 1, 0], [0, 1, 1]])
        elif block_type == 4:
            return np.array([[0, 1, 1], [1, 1, 0]])

    def move_block(self, direction):
        """Mueve el bloque"""
        if direction == 'down':
            self.current_block[1] += 1  # Mueve el bloque hacia abajo
        elif direction == 'left':
            self.current_block[0] -= 1  # Mueve el bloque hacia la izquierda
        elif direction == 'right':
            self.current_block[0] += 1  # Mueve el bloque hacia la derecha

    def rotate_block(self):
        """Rota el bloque"""
        self.current_block = np.rot90(self.current_block)

    def check_collision(self):
        """Verifica si el bloque choca con algo"""
        return False  # Simulamos que no hay colisión para simplificar el ejemplo

    def update(self):
        """Actualiza el estado del juego"""
        self.move_block('down')

        if self.check_collision():
            self.current_block = self.new_block()
            if self.check_collision():
                self.game_over = True


# Función para dibujar el tablero
def draw_board(board):
    for y in range(board.shape[0]):
        for x in range(board.shape[1]):
            if board[y, x]:
                pygame.draw.rect(screen, RED, pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


# Inicializamos el juego
game = Tetris()

# Función para jugar
def play_game():
    while not game.game_over:
        game.update()
        screen.fill(BLACK)  # Limpiamos la pantalla
        draw_board(game.board)  # Dibujamos el tablero

        # Mostrar el estado actual
        st.image(pygame.surfarray.array3d(screen), caption="Estado del Juego")
        
        pygame.time.delay(100)  # Controlamos la velocidad de actualización


# Iniciar el juego al hacer clic en el botón
if st.button('Iniciar Juego'):
    play_game()
