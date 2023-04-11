import pygame
import random
from comet import Comet

#créer une classe pour gérer cet évenement

class CometFallEvent:

    #lors du chargement -> créer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 6
        self.game = game
        self.fall_mode = False

        #définir un groupe de sprite pour stocjer nos comètes
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):

        #nombre max comètes
        nbr_cometes = random.randint(5,10)
        #boucle pour les valeurs entre 1 et 10
        for i in range(1, nbr_cometes):

            #apparaître une première boule de feu
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        #la jauge d'évenement est totalement chargé
        if ((self.is_full_loaded()) and (len(self.game.all_monsters) ==0)):
            print("pluie de comètes!!")
            self.meteor_fall()
            self.fall_mode = True #activer l'évenement 

    def update_bar(self, surface):

        #ajouter du pourcentage à la bar
        self.add_percent()

        #barre noire (en arrière plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0, #l'axe des X
            surface.get_height() -20, #l'axe des Y
            surface.get_width(), #la longeur de la fenêtre
            10 #épaisseur de la barre
        ])
        #barre rouge (jauge d'event)
        pygame.draw.rect(surface, (187, 11, 11), [
            0, #l'axe des x
            surface.get_height() -20, #l'axe des Y
            (surface.get_width() / 100)*self.percent, #la longeur de la fenêtre
            10 #épaisseur de la barre
        ])