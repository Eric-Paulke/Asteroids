import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    FPS = pygame.time.Clock()
    dt = 0
   
# Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


# containers
    Shot.containers = (updatable, drawable, shots)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable


    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        updatable.update(dt)

        for asteroid in asteroids:
            
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()

            if asteroid.collision(player):
                print ("Game over!")
                sys.exit()

        screen.fill("black")   
        
        for obj in drawable:
            obj.draw(screen)


        pygame.display.flip()
        # Frame limit 60
        dt = FPS.tick(60) / 1000



if __name__ == "__main__":
    main()