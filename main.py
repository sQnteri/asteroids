import pygame
from constants import *
from logger import log_state
from player import Player

def main():
    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    #groups for updatable and drawable objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
   
    #add player class to updatable and drawable, create player object
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    
    #game loop
    while True:
        
        log_state()
        #quit if x is pressed in the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #background 
        screen.fill("black")
        
        updatable.update(dt)
        
        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
