import pygame
import random

#définir une classe qui va s'occuper des animations
class AnimationSprite(pygame.sprite.Sprite):
    
    #définir les choses à faire à la création de l'entité

    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'PygameAssets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0 # commencer l'animation à l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    #définir une méthode pour démarrer l'animation
    def start_animation(self):
        self.animation = True

    #définir une méthode pour animer le sprite
    def animate(self, loop=False):
        
        #vérifier si l'animation est activée
        if (self.animation):

            #passer à l'image suivante
            self.current_image += random.randint(0,1)

            #vérifier si on a atteind la fin de l'animation
            if self.current_image >= len(self.images):

                #remettre l'animation au départ
                self.current_image = 0

                #si l'animation n'est pas en mode boucle

                if (loop is False):
                    #désactivation de l'animation
                    self.animation = False

            #modifier l'image précédente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)

#définir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):

    #charger les 24 images de ce sprite dans le dossier correspondant
    images = []

    #récuperer le chemin du dossier pour ce sprite
    path = f"PygameAssets/{sprite_name}/{sprite_name}"

    #boucler sur chaque image dans ce dossier
    for num in range(1, 24):
        image_path = path + str(num)+ '.png'
        images.append(pygame.image.load(image_path))

    #renvoyer le contenu de l'image
    return images


#définir un dictionnaire qui va contenir les images chargées de chaque sprite
#mummy -> [...mummy1.png, ...mummy2.png, ...]
#player -> [...player1.png, ...player2.png, ...]
animations = {
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player'),
    'alien': load_animation_images('alien')
}
