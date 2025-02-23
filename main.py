import pygame
from pygame.locals import *

# Configurações iniciais
pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.SRCALPHA)
pygame.display.set_caption("Xbox Controller Overlay - OBS")
font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()

# Configurar transparência
screen.set_alpha(200)

# Inicializar joystick
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Cores
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)
GREEN = (0, 255, 0, 255)
RED = (255, 0, 0, 255)
BLUE = (0, 150, 255, 255)
YELLOW = (255, 255, 0, 255)
GRAY = (100, 100, 100, 255)

# Posições baseadas no layout Xbox
POSITIONS = {
    'left_trigger': (200, 50),
    'right_trigger': (600, 50),
    'left_bumper': (150, 200),
    'right_bumper': (650, 200),
    'left_stick': (250, 350),
    'right_stick': (550, 450),
    'buttons': {
        'A': (650, 370),
        'B': (690, 330),
        'X': (610, 330),
        'Y': (650, 290)
    },
    'dpad': (150, 300),
    'menu': (400, 200)
}

def draw_button(label, pos, state, color=GREEN, size=25):
    # Botão circular com borda
    pygame.draw.circle(screen, WHITE if state else GRAY, pos, size+2)
    pygame.draw.circle(screen, color if state else GRAY, pos, size)
    text = font.render(label, True, WHITE if state else BLACK)
    text_rect = text.get_rect(center=pos)
    screen.blit(text, text_rect)

def draw_trigger(pos, value, color, vertical=True):
    # Gatilho com fundo e preenchimento
    if vertical:
        pygame.draw.rect(screen, color, (pos[0]-15, pos[1], 30, 100))
        pygame.draw.rect(screen, GRAY, (pos[0]-15, pos[1] + (100 - value*100), 30, value*100))
    else:
        pygame.draw.rect(screen, color, (pos[0], pos[1]-15, 100, 30))
        pygame.draw.rect(screen, GRAY, (pos[0] + (100 - value*100), pos[1]-15, value*100, 30))

def draw_joystick(pos, x, y, color=BLUE):
    # Analógico com movimento
    base_size = 40
    pygame.draw.circle(screen, GRAY, pos, base_size)
    pygame.draw.circle(screen, color, 
        (int(pos[0] + x*base_size), int(pos[1] + y*base_size)), 
        base_size//2)

def draw_bumper(pos, state, side='left'):
    # Botões L1/R1
    width, height = 80, 20
    color = BLUE if state else GRAY
    if side == 'left':
        points = [(pos[0], pos[1]), (pos[0]+width, pos[1]), 
                 (pos[0]+width-10, pos[1]+height), (pos[0]-10, pos[1]+height)]
    else:
        points = [(pos[0], pos[1]), (pos[0]-width, pos[1]), 
                 (pos[0]-width+10, pos[1]+height), (pos[0]+10, pos[1]+height)]
    
    pygame.draw.polygon(screen, color, points)

running = True
button_states = [False] * joystick.get_numbuttons()
axis_states = [0.0] * joystick.get_numaxes()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == JOYBUTTONDOWN:
            button_states[event.button] = True
        elif event.type == JOYBUTTONUP:
            button_states[event.button] = False
        elif event.type == JOYAXISMOTION:
            axis_states[event.axis] = event.value

    screen.fill((0, 0, 0, 0))  # Fundo transparente

    # Desenhar elementos do controle
    # Gatilhos
    draw_trigger(POSITIONS['left_trigger'], (1 - axis_states[4])/2, BLUE)
    draw_trigger(POSITIONS['right_trigger'], (1 - axis_states[5])/2, BLUE)

    # Botões frontais (L1/R1 - geralmente botões 4 e 5)
    draw_bumper(POSITIONS['left_bumper'], button_states[4], 'left')
    draw_bumper(POSITIONS['right_bumper'], button_states[5], 'right')

    # Botões principais
    draw_button("A", POSITIONS['buttons']['A'], button_states[0], GREEN)
    draw_button("B", POSITIONS['buttons']['B'], button_states[1], RED)
    draw_button("X", POSITIONS['buttons']['X'], button_states[2], BLUE)
    draw_button("Y", POSITIONS['buttons']['Y'], button_states[3], YELLOW)

    # Analógicos
    draw_joystick(POSITIONS['left_stick'], axis_states[0], axis_states[1])
    draw_joystick(POSITIONS['right_stick'], axis_states[2], axis_states[3])

    pygame.display.flip()
    clock.tick(30)

pygame.quit()