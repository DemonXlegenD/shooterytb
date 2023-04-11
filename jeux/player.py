import pygame
from projectile import Projectile
import animation

#créer une première classe qui va représenter notre joueur
class Player(animation.AnimationSprite):

    def __init__(self, game):
        super().__init__("player") #initialise sprite
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 15
        self.velocity = 2
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if (self.health - amount > amount) :
            self.health -= amount
        else:
            #si le joueur n'a plus de point de vie
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        #dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x +50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x +50, self.rect.y + 20, self.health, 7])

    def launch_projectile(self):

        #créer une nouvelle instance de la classe Projectile
        self.all_projectiles.add(Projectile(self))

        #démarer l'animation lancé
        self.start_animation()

    def move_right(self):

        #si le joueur n'est pas en collision avec les monstres
        if not (self.game.check_collision(self, self.game.all_monsters)):
            self.rect.x += self.velocity

    def move_left(self):

        #si le joueur n'est pas en collision avec les monstres
        self.rect.x -= self.velocity