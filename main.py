
import json
import pygame
from game import Game
import time

pygame.mixer.init()
pygame.mixer.music.load("after_fight.mp3")

print("몬스터가 나타났습니다!")
pygame.mixer.music.play()
time.sleep(3)

if __name__ == "__main__":
    game = Game()
    game.run()
