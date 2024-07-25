import pygame

# Init
pygame.init()
# Variable running game
isRun = True

# membuat display surface object
window_panjang = 500
window_lebar = 500
window = pygame.display.set_mode((window_panjang, window_lebar))

# object game
# position
x = 250
y = 250

# size
panjang = 20
lebar = 20

# kecepatan gerak
speed = 10

while isRun:
    pygame.time.delay(10)
    # user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    # ambil semua keyboard press
    keys = pygame.key.get_pressed()

    # ambil ke kiri
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    # ambil ke kanan
    if keys[pygame.K_RIGHT] and x < window_lebar-lebar:
        x += speed
    # ambil ke bawah
    if keys[pygame.K_DOWN] and y < window_panjang-panjang:
        y += speed
    # ambil ke atas
    if keys[pygame.K_UP] and y > 0:
        y -= speed

    # update asset
    window.fill(('tomato'))
    pygame.draw.rect(window, (255, 250, 0), (x, y, lebar, panjang))
    # render ke display
    pygame.display.update()

pygame.quit()
