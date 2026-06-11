import pygame
import random

pygame.init()

# Screen
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Star Catcher")

fps = 60
timer = pygame.time.Clock()

# Fonts
font = pygame.font.Font("freesansbold.ttf", 30)

# Colors
WHITE = (255, 255, 255)

# Game states
main_menu = True
game_over_state = False

# Basket
basket_width = 100
basket_height = 20
basket_x = (WIDTH - basket_width) // 2
basket_y = HEIGHT - basket_height - 20
basket_speed = 7

# Star (planet)
planet_width = 40
planet_height = 40
planet_x = random.randint(0, WIDTH - planet_width)
planet_y = -planet_height
planet_speed = 5

# Score
score = 0

# Load star image
star_image = pygame.image.load("star.png")
star_image = pygame.transform.scale(star_image, (planet_width, planet_height))


def draw_menu():
    title_font = pygame.font.Font("freesansbold.ttf", 48)

    title = title_font.render("Star Catcher", True, WHITE)
    screen.blit(title, (WIDTH // 2 - 150, HEIGHT // 3))

    text = font.render("Press SPACE to start", True, WHITE)
    screen.blit(text, (WIDTH // 2 - 160, HEIGHT // 2))


def draw_basket():
    pygame.draw.rect(screen, (0, 0, 255),
                     (basket_x, basket_y, basket_width, basket_height))


def draw_planet():
    screen.blit(star_image, (planet_x, planet_y))


def draw_score():
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))
    level = score // 10 + 1
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(level_text, (10, 40))



def draw_game_over():
    text = font.render("GAME OVER", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
    screen.blit(text, text_rect)

    text2 = font.render("Press R to restart", True, WHITE)
    text2_rect = text2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
    screen.blit(text2, text2_rect)


run = True

while run:
    timer.tick(fps)

    # EVENTS
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:

            if main_menu and event.key == pygame.K_SPACE:
                main_menu = False

            if game_over_state and event.key == pygame.K_r:
                score = 0

                basket_x = (WIDTH - basket_width) // 2

                planet_x = random.randint(0, WIDTH - planet_width)
                planet_y = -planet_height

                game_over_state = False
                main_menu = True


    if main_menu:
        screen.fill((135, 206, 235))
        draw_menu()

    elif game_over_state:
        screen.fill((0, 0, 50))
        draw_game_over()

    else:
        screen.fill((0, 0, 50))

        # Movement
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            basket_x -= basket_speed
        if keys[pygame.K_RIGHT]:
            basket_x += basket_speed

        # Keep basket on screen
        basket_x = max(0, min(WIDTH - basket_width, basket_x))

        # Move star
        planet_y += planet_speed

        # Catch logic
        if (planet_y + planet_height > basket_y and
                basket_x < planet_x < basket_x + basket_width):
            score += 1
            planet_x = random.randint(0, WIDTH - planet_width)
            planet_y = -planet_height

        # Missed star
        if planet_y > HEIGHT:
            game_over_state = True

        # Draw game
        draw_planet()
        draw_basket()
        draw_score()

    pygame.display.flip()

pygame.quit()