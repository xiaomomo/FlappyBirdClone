import sys, pygame

pygame.init()

width = 320
height = 240
speed = [2, 2]

screen = pygame.display.set_mode([width, height])

ball = pygame.image.load("../assets/sprites/ball.gif")
ball_rect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ball_rect = ball_rect.move(speed)
    print(ball_rect.left, ball_rect.right, ball_rect.top, ball_rect.bottom)

    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]

    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill([0, 0, 0])
    screen.blit(ball, ball_rect)
    pygame.display.flip()
