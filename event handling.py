import pygame
pygame.init()

# Creating game window
gameWindow = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Nitin")

# Game specific variable
exit_game = False
game_over = False

# Creating a Game loop
while not exit_game:
    for event in pygame.event.get():
        print(event)

pygame.quit()
quit()