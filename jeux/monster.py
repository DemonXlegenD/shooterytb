import pygame
import random
import animation

class Monster(animation.AnimationSprite):

    def __init__(self, game, name, size, offset = 0):
        super().__init__(name, size)
        self.game = game
        self.max_health = 100
        self.health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1100 + random.randint(0,300)
        self.rect.y = 540 - offset
        self.loot_amount = 10
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1,2)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        #infliger les dégats
        self.health -= amount

        #vérifier si son nouveau nombre de points de vie est inférieur ou égal à 0
        if (self.health <= 0):
            # Reapparaitre comme un nouveau monstre
            self.rect.x = 1100 + random.randint(0,300)
            self.health = self.max_health
            self.velocity = random.randint(1, self.default_speed)
            
            #ajouter le nombre de points
            self.game.add_score(self.loot_amount)

            #si la barre d'évenemenet est chargée à son maximum
            if (self.game.comet_event.is_full_loaded()):
                #retirer du jeu
                self.game.all_monsters.remove(self)

                #appel de la méthode pour essayer de déclencher la pluie de comètes
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop = True)

    def update_health_bar(self, surface):
        #définir une couleur pour notre jauge de vie (vert clair)
        bar_color = (111, 210, 46)

        #définir une couleur pour l'arrière plan de la jauge (gris foncé)
        back_bar_color = (60, 63, 60)

        #définir la position de notre jauge de vie ainsi que sa largeur et son épaisseur
        bar_position = [self.rect.x, self.rect.y, self.health, 5]

        #définir la position de l'arrière plan de notre jauge de vie
        back_bar_position = [self.rect.x, self.rect.y, self.max_health, 5]

        #dessiner notre barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)
        

    def forward(self):
        #le déplacement ne se fait que si il n'y a pas de collision avec un groupe de joueurs
        if not(self.game.check_collision(self, self.game.all_players)):
            self.rect.x -= self.velocity
        
        #si le monstre est en collision avec le joueur
        else:
            #infliger des dégats
            self.game.player.damage(self.attack)

#définir une classe pour la momie
class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_loot_amount(20)

#définir une classe pour l'alien
class Alien(Monster):

    def __init__(self, game):
        super().__init__(game, "alien", (250, 250), 100)
        self.health = 250
        self.max_health = 250
        self.attack = 0.8
        self.set_speed(1)
        self.set_loot_amount(80)