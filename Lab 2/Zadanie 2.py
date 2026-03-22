import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Zadanie 2")

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(win, CZERWONY, (172, 155, 245, 10))
    pygame.draw.rect(win, CZERWONY, (174, 405, 245, 10))


    rect_surf = pygame.Surface((347, 10), pygame.SRCALPHA)
    rect_surf.fill(CZERWONY)

    rotated_surf = pygame.transform.rotate(rect_surf, 45)

    rect_center = (297, 284)
    new_rect = rotated_surf.get_rect(center=rect_center)

    win.blit(rotated_surf, new_rect.topleft)


    pygame.display.update()