import pygame
from pygame import font
import time
import os
import random
from window import window
from default import dir_path
from default import fps
from default import running
from interface import scoreBox
import match
from match import player1Char, player2Char, stage
from character import rosterFrame
from character import player1, player2
from character import no_char, michael, bell, gus
from interface import hp_1, hp_2
from character import rosterFrame
from interface import scoreBox
from camera import camera
from map import stage

pygame.mouse.set_visible(False)

running = True

clock = pygame.time.Clock()

cursor = pygame.transform.scale(pygame.image.load(f"{dir_path}/cursor.gif").convert_alpha(), (25,25))

cursorClick = pygame.transform.scale(pygame.image.load(f"{dir_path}/cursorClick.gif").convert_alpha(), (25,25))

title = pygame.transform.scale(pygame.image.load(f"{dir_path}/Title.gif").convert_alpha(), (300,150))

cursorSprite = None

button = pygame.transform.scale(pygame.image.load(f"{dir_path}/score inbetween hps.gif").convert_alpha(),(292,60))

current_character_1 = no_char
current_character_2 = no_char

match.player1Char = no_char
match.player2Char = no_char

#########################
# SCENES
#########################

scene = None

class main_menu:
    def handle():
        #window.blit(pygame.transform.scale(pygame.image.load(f"{dir_path}/background.gif").convert_alpha(), (1366,768)),(0,0))
        window.fill((50,50,50))
        window.blit(title, (10, 10))
        window.blit(button, (10, 220))
        play = text(size=36,text="Join")
        play.render(20, 240)
        global scene
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < 10 + 584 and
            pygame.mouse.get_pos()[0] > 10 and
            pygame.mouse.get_pos()[1] < 220 + 60 and
            pygame.mouse.get_pos()[1] > 220):
                scene = roster
                
        window.blit(button, (10,280))
        play = text(size=36,text="Host")
        play.render(20,300)
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < 10 + 584 and
            pygame.mouse.get_pos()[0] > 10 and
            pygame.mouse.get_pos()[1] < 280 + 60 and
            pygame.mouse.get_pos()[1] > 280):
                scene = roster
                
        window.blit(button, (10,340))
        play = text(size=36,text="Training")
        play.render(20,360)
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < 10 + 584 and
            pygame.mouse.get_pos()[0] > 10 and
            pygame.mouse.get_pos()[1] < 340 + 60 and
            pygame.mouse.get_pos()[1] > 340):
                scene = roster
                

class roster:
    def handle():
        global current_character_1
        global current_character_2
        global scene
        #window.blit(pygame.transform.scale(pygame.image.load(f"{dir_path}/background.gif").convert_alpha(), (1366,768)),(0,0))
        window.fill((50,50,50))
        window.blit(button, (10, 10))
        play = text(size=36,text="Back")
        play.render(30, 30)
        if pygame.mouse.get_pressed()[0]:
            if ((pygame.mouse.get_pos()[0] + 20) < 10 + 584 and
            pygame.mouse.get_pos()[0] > 10 and
            pygame.mouse.get_pos()[1] < 10 + 60 and
            pygame.mouse.get_pos()[1] > 10):
                scene = main_menu

        window.blit(michael.sprites.roster, (3 * 120,.5 * 120))
        window.blit(rosterFrame, (3 * 120,.5 * 120))
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < 3 * 120 + 100 and
            pygame.mouse.get_pos()[0] > 3 * 120 and
            pygame.mouse.get_pos()[1] < .5 * 120 + 100 and
            pygame.mouse.get_pos()[1] > .5 * 120):
                #print("clicked mike")
                current_character_1 = michael
                match.player1Char = "michael"
        if pygame.mouse.get_pressed()[2]:
            if (pygame.mouse.get_pos()[0] < 3 * 120 + 100 and
            pygame.mouse.get_pos()[0] > 3 * 120 and
            pygame.mouse.get_pos()[1] < .5 * 120 + 100 and
            pygame.mouse.get_pos()[1] > .5 * 120):
                #print("clicked mike")
                current_character_2 = michael
                match.player2Char = "michael"

        window.blit(bell.sprites.roster, (4 * 120,.5 * 120))
        window.blit(rosterFrame, (4 * 120,.5 * 120))
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < 4 * 120 + 100 and
            pygame.mouse.get_pos()[0] > 4 * 120 and
            pygame.mouse.get_pos()[1] < .5 * 120 + 100 and
            pygame.mouse.get_pos()[1] > .5 * 120):
                #print("clicked bell")
                current_character_1 = bell
                match.player1Char = "bell"
        if pygame.mouse.get_pressed()[2]:
            if (pygame.mouse.get_pos()[0] < 4 * 120 + 100 and
            pygame.mouse.get_pos()[0] > 4 * 120 and
            pygame.mouse.get_pos()[1] < .5 * 120 + 100 and
            pygame.mouse.get_pos()[1] > .5 * 120):
                #print("clicked bell")
                current_character_2 = bell
                match.player2Char = "bell"

        window.blit(gus.sprites.roster, (5 * 120,.5 * 120))
        window.blit(rosterFrame, (5 * 120,.5 * 120))
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < 5 * 120 + 100 and
            pygame.mouse.get_pos()[0] > 5 * 120 and
            pygame.mouse.get_pos()[1] < .5 * 120 + 100 and
            pygame.mouse.get_pos()[1] > .5 * 120):
                #print("clicked gus")
                current_character_1 = gus
                match.player1Char = "gus"
        if pygame.mouse.get_pressed()[2]:
            if (pygame.mouse.get_pos()[0] < 5 * 120 + 100 and
            pygame.mouse.get_pos()[0] > 5 * 120 and
            pygame.mouse.get_pos()[1] < .5 * 120 + 100 and
            pygame.mouse.get_pos()[1] > .5 * 120):
                #print("clicked gus")
                current_character_2 = gus
                match.player2Char = "gus"

        window.blit(rosterFrame, (6 * 120,.5 * 120))

        window.blit(rosterFrame, (7 * 120,.5 * 120))

        window.blit(rosterFrame, (8 * 120,.5 * 120))

        window.blit(pygame.transform.scale(current_character_1.sprites.idle_right,(100,100)),(3 * 120, pygame.display.Info().current_h - 250))
        window.blit(pygame.transform.scale(current_character_1.hat,(50,50)),((3 * 120) + 50, pygame.display.Info().current_h - 292))
        window.blit(button, (3 * 120, pygame.display.Info().current_h - 150))
        play = text(size=36,text=f"{current_character_1.name}")
        play.render((3 * 120) + 10, (pygame.display.Info().current_h - 150) + 10)

        window.blit(pygame.transform.scale(current_character_2.sprites.idle_right,(100,100)),(7 * 120, pygame.display.Info().current_h - 250))
        window.blit(pygame.transform.scale(current_character_2.hat,(50,50)),((7 * 120) + 50, pygame.display.Info().current_h - 292))
        window.blit(button, (7 * 120, pygame.display.Info().current_h - 150))
        play = text(size=36,text=f"{current_character_2.name}")
        play.render((7 * 120) + 10, (pygame.display.Info().current_h - 150) + 10)

        window.blit(button, (pygame.display.Info().current_w - 302, pygame.display.Info().current_h - 70))
        play = text(size=36,text="Start")
        play.render(pygame.display.Info().current_w - 292, pygame.display.Info().current_h - 60)
        if pygame.mouse.get_pressed()[0]:
            if (pygame.mouse.get_pos()[0] < pygame.display.Info().current_w - 292 + 292 and
            pygame.mouse.get_pos()[0] > pygame.display.Info().current_w - 292 and
            pygame.mouse.get_pos()[1] < pygame.display.Info().current_h - 60 + 60 and
            pygame.mouse.get_pos()[1] > pygame.display.Info().current_h - 60):
                scene = game

class game:
    def handle():
        global scene
        if player1.character.stock <= 0:
            #print("player2 Wins!!!")
            scene = main_menu
            player1.character.stock = 3
            player2.character.stock = 3
            camera.shake_frame = 0
        if player2.character.stock <= 0:
            #print("player1 Wins!!!")
            scene = main_menu
            player1.character.stock = 3
            player2.character.stock = 3
            camera.shake_frame = 0
            
        #print(camera.shake_frame)
        
        ##print(midpoint(player1.character.x,player1.character.y - 200,player2.character.x,player2.character.y - 200))
        #x_mid = ((stage.x + stage.w / 2) + player1.character.x + player2.character.x) / 3
        #y_mid = (stage.y + player1.character.y + player2.character.y) / 3
        #camera.x, camera.y = midpoint(player1.character.x,player1.character.y - 200,player2.character.x,player2.character.y - 200)
        #camera.x, camera.y = x_mid - (pygame.display.Info().current_w / 2), y_mid - (100) - (pygame.display.Info().current_h / 2)
        
        stage.render()
        if camera.shake_frame > 0:
            pygame.draw.rect(window, (0,0,0), (0, 0, pygame.display.Info().current_w, random.randint(1,25)))
            pygame.draw.rect(window, (0,0,0), (0, pygame.display.Info().current_h - random.randint(1,25), pygame.display.Info().current_w, 20))
            camera.x += random.randint(-10, 10)
            camera.y += random.randint(-10, 10)

            pygame.display.update

            time.sleep(.02)

            camera.shake_frame -= 1
        if camera.shake_frame <= 0:
            camera.x, camera.y = ((stage.x + stage.w) / 2) - (pygame.display.Info().current_w / 2), (stage.y - (pygame.display.Info().current_w / 2)) + 200
        hp_1.w = player1.character.health
        hp_1.render()
    # hp_2.x, hp_2.empty.x = pygame.display.Info().current_w - 610,pygame.display.Info().current_w - 610
        hp_2.w = player2.character.health
        hp_2.render()
        player2.handleCharacter()
        player1.handleCharacter()
        window.blit(rosterFrame, (10,10))
        window.blit(rosterFrame, (pygame.display.Info().current_w - 110,10))
        window.blit(scoreBox, ((pygame.display.Info().current_w - 146) / 2,10))
        score = text(size=36,text=f"{player1.character.stock}/{player2.character.stock}")
        score.render((pygame.display.Info().current_w - score.text.get_width()) / 2, 13)


class text:
    def __init__(self, size, text):
        self.font = pygame.font.Font(f"{dir_path}/font.fon",size)
        self.text = self.font.render(text, True, (255,255,255))
    def render(self,x,y):
        window.blit(self.text,(x,y))

scene = main_menu

cursorSprite = cursor

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(fps)
    scene.handle()
    window.blit(cursorSprite, pygame.mouse.get_pos())
    pygame.display.update()

pygame.quit