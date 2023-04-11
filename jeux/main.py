import pygame
import math
from game import Game

#définir une clock
clock = pygame.time.Clock()
FPS = 100

pygame.init()

#générer la fenêtre de notre jeu
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080, 720))

#importer de charger l'arrière plan de notre jeu
background = pygame.image.load('PygameAssets/bg.jpg')

#importer charger notre bannière
banner = pygame.image.load('PygameAssets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/4)

#importer charger notre bouton pour lancer la partie
play_button = pygame.image.load('PygameAssets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height()/1.7)


#charger notre jeu
game = Game()

running = True

#boucle tant que cette condition est vraie

while(running):

    #appliquer l'arrière plan de notre jeu
    screen.blit(background, (0, -200))  #1er argu = image, 2ème argu = (espace largeur, espace hauteur)

    #vérifier si le jeu a commencé ou non
    if (game.is_playing):
        #déclencher les isntructions de la partie
        game.update(screen)
    
    #vérifier si notre jeu n'a pas commencé
    else:
        #ajouter mon écran de bienvenue 
        screen.blit(banner, banner_rect)
        screen.blit(play_button, play_button_rect)

    #mettre à jour l'écran
    pygame.display.flip()

    #si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        # que l'évenement est fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")

        if event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #détecter si la touche espace est enclenchée pour lance notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif (event.type == pygame.MOUSEBUTTONDOWN):

            #vérification pour svaoir si la souris est en collision avec le bouton
            if (play_button_rect.collidepoint(event.pos)):

                #mettre le jeu en monde "lancé"
                game.start()

                #jouer le son
                # game.sound_manager.play('click')

    #fixer le nombre de fps sur ma clock
    clock.tick(FPS)
       

        
        
            