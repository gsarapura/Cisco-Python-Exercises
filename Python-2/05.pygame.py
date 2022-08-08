import pygame

# Displays while True
run = True
# Display height and width.
width = 400
height = 300
# Environment initialization:
pygame.init()
# Set the screeen:
screen = pygame.display.set_mode((width, height))
# Set the font:
font = pygame.font.SysFont(None, 48)
# True = softened. 
text = font.render("Bienvenido a pygame", True, (255, 255, 255))
# Inset text into screen buffer:
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
# Buffers are inverted to show text:
pygame.display.flip()
while run:
    for event in pygame.event.get(): # List all pending events from pygame.
       # Ends loop or close windows in case of: 
        if event.type == pygame.QUIT\
        or event.type == pygame.MOUSEBUTTONUP\
        or event.type == pygame.KEYUP:
            run = False