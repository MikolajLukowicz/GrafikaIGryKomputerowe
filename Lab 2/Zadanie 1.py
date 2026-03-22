import pygame
import math

WIDTH, HEIGHT = 600, 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zadanie 1")

ZOLTY = (255, 255, 102)
NIEBIESKI = (102, 102, 255)

N = 12
PROMIEN = 150
SRODEK = (300, 300)

punkty_bazowe = []
for i in range(N):
    kat = i * (2 * math.pi / N)
    x = PROMIEN * math.cos(kat)
    y = PROMIEN * math.sin(kat)
    punkty_bazowe.append((x, y))


def transformuj(punkty, tryb):
    nowe = []
    for x, y in punkty:
        match tryb:
            case 1:
                nowe.append((x * 0.5, y * 0.5))

            case 2:
                rad = math.radians(45)
                nx = x * math.cos(rad) - y * math.sin(rad)
                ny = x * math.sin(rad) + y * math.cos(rad)
                nowe.append((nx, ny))

            case 3:
                nowe.append((-x, y))

            case 4:
                nowe.append((x + 0.5 * y, y))

            case 5:
                nowe.append((x, y * 0.5 - 150))

            case 6:
                nx = x
                ny = y + 0.5 * x
                nowe.append((nx, ny))

            case 7:
                nowe.append((-x, -y))

            case 8:
                rad = math.radians(-30)
                tx, ty = x * 0.4, y * 1.2
                nx = tx * math.cos(rad) - ty * math.sin(rad)
                ny = tx * math.sin(rad) + ty * math.cos(rad)
                nowe.append((nx, ny))

            case 9:
                nowe.append((x * 0.8 + 0.3 * y + 50, y * 0.8))

            case _:
                nowe.append((x, y))

    return [(nx + 300, ny + 300) for nx, ny in nowe]

aktualny_tryb = 0
running = True

while running:
    screen.fill(ZOLTY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if pygame.K_1 <= event.key <= pygame.K_9:
                aktualny_tryb = event.key - pygame.K_0
            elif event.key == pygame.K_0:
                aktualny_tryb = 0

    punkty_do_narysowania = transformuj(punkty_bazowe, aktualny_tryb)
    pygame.draw.polygon(screen, NIEBIESKI, punkty_do_narysowania)

    pygame.display.flip()

pygame.quit()