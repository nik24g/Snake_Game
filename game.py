import pygame
import random
import os

pygame.init()

# Creating game window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Nitin's Snake Game")

# Background Image
home_image = pygame.image.load("home_snake.png")
home_image = pygame.transform.scale(home_image, (700, 200)).convert_alpha()

back_image = pygame.image.load("seamless-grass-texture-free.jpg")
back_image = pygame.transform.scale(back_image, (screen_width, screen_height)).convert_alpha()

over_image = pygame.image.load("scarysnake.png")
over_image = pygame.transform.scale(over_image, (700, 200)).convert_alpha()

# colours
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (9, 99, 203)
dark_blue = (20, 17, 57)
green = (24, 162, 10)
dark_green = (59, 77, 17)
light_green = (124, 208, 103)
light_pink = (247, 224, 240)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Freestyle Script', 75)  # this is for font
fps = 60


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, (x, y))


def plot_snake(window, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(window, color, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(light_green)
        gameWindow.blit(home_image, (100, 50))
        text_screen("Welcome to Nitin's Snake Game", dark_green, 150, 275)
        text_screen("Enter to play", dark_green, 300, 350)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load("game_background.mp3")
                    pygame.mixer.music.play()
                    game_loop()
        pygame.display.update()  # display.update() method is used to update display after any change in display
        clock.tick(fps)


# Creating a Game loop
def game_loop():
    # Game specific variable
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 30

    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    score = 0
    snk_list = []
    snk_length = 1
    if not(os.path.exists("Highscore.txt")):
        with open("Highscore.txt", "w") as f:
            f.write("0")

    with open("Highscore.txt") as f:
        hiscore = f.read()
        hiscore = int(hiscore)

    food_x = random.randint(65, 800)
    food_y = random.randint(65, 500)

    while not exit_game:
        if game_over:
            with open("Highscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(light_green)
            gameWindow.blit(over_image, (100, 50))
            text_screen("Game Over", dark_green, 315, 275)
            text_screen(f"Score: {score} Highscore: {hiscore}", dark_green, 185, 350)
            text_screen("Press Enter to Play Again", dark_green, 190, 430)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
            # for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():  # this is for get events or event handling
                if event.type == pygame.QUIT:  # this is for quit the game by quit button at the top of the window
                    exit_game = True

                if event.type == pygame.KEYDOWN:  # pygame.KEYDOWN is used for any key pressed
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y = -init_velocity
                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = init_velocity

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 20 and abs(snake_y - food_y) < 10:
                food_x = random.randint(65, 800)
                food_y = random.randint(65, 500)
                score += 10
                snk_length += 5
                if score > hiscore:
                    hiscore = score

            # gameWindow.fill(light_pink)  # fill method is used to fill color in display
            gameWindow.blit(back_image, (0, 0))
            text_screen(f"Score: {str(score)} HighScore: {hiscore}", red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = [snake_x, snake_y]
            snk_list.append(head)
            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-2]:
                game_over = True
                pygame.mixer.music.load("game_over.mp3")
                pygame.mixer.music.play()

            if snake_x < 0 or snake_y < 0 or snake_x > screen_width or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load("game_over.mp3")
                pygame.mixer.music.play()

            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()  # display.update() method is used to update display after any change in display
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()
