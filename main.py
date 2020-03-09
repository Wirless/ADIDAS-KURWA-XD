#########
# Itens Catcher
# portal basket
#
#
#
#


import pygame

from ball import Ball

def main():
    pygame.init()
    window = (800,800)
    screen = pygame.display.set_mode(window)
    pygame.display.set_caption("Catch!")
    spritez = pygame.sprite.Group()
    clock = pygame.time.Clock()
    faller = Ball((255,255,255), (10, 10), (55, 55))
    faller2 = Ball((255,255,255), (10, 10), (75, 55))
    faller3 = Ball((255,255,255), (10, 10), (95, 55))
    spritez.add(faller,faller2,faller3)
    val = "Adidas"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
                # exit game with p
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    carryOn = False
                #might just make variable or something.
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    
        spritez.update()
        spritez.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        font = pygame.font.Font(None, 50)
        text = font.render(str("Adidas"), 1, (255,255,255))
        screen.blit(text, (200, 250))
        
    
    
    
    
    
    
if __name__ == "__main__":
    main()