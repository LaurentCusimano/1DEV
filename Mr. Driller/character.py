from os import path
import pygame
from level import render


class Character:        # Important : directions list : Up = 1; Right = 2; Down = 3; Left = 4
    """Character class"""

    def __init__(self, posX, posY, currentBotLine):
        self.__posX = posX
        self.__posY = posY
        self.__blocksFallen = 0
        self.__currentBotLine = currentBotLine
        self.__texturePath = path.join("Assets", "Textures", "Character", "testpink.png")

    def updCurrBotLine(self, currentBotLine):
        self.__currentBotLine = currentBotLine

    def blocksFallenAcc(self):
        return self.__blocksFallen

    def display(self, surface):

        image = pygame.image.load(self.__texturePath)
        surface.blit(image, (self.__posX * 64 + 26, (self.__posY * 64 + 12) - self.__blocksFallen * 64))

    def move(self, surface, direction, level):

        if direction == 1 and self.__posY > 0:                         # Up
            level[self.__posY][self.__posX].display(surface, 0, self.__blocksFallen)
            self.__posY -= 1
            self.__blocksFallen -= 1
            print(self.__posX, self.__posY)
            self.display(surface)

        elif direction == 2 and self.__posX < len(level[0])-1:        # Right
            level[self.__posY][self.__posX].display(surface, 0, self.__blocksFallen)
            self.__posX += 1
            self.display(surface)

        elif direction == 3 and self.__posX > 0:                      # Left
            level[self.__posY][self.__posX].display(surface, 0, self.__blocksFallen)
            self.__posX -= 1
            self.display(surface)

        elif direction == 4:
            level[self.__posY][self.__posX].display(surface, 0, self.__blocksFallen)
            self.__posY += 1
            self.display(surface)

    def breakBlock(self, surface, direction, level, currentBotLine):

        if direction == 1 \
                and self.__posY > 0 \
                and level[self.__posY-self.__blocksFallen-2][self. __posX].hpAccess() > 0:
            level[self.__posY-self.__blocksFallen-2][self. __posX].hit(surface)             # Up
            print("Char is in", self.__posX, ", ", self.__posY, "break")

        elif direction == 2 \
                and self.__posX < len(level[0])-1 \
                and level[self.__posY][self. __posX+1].hpAccess() > 0:
            level[self.__posY-self.__blocksFallen][self. __posX+1].hit(surface)             # Right

        elif direction == 3 \
                and self.__posY < currentBotLine \
                and level[self.__posY+1][self. __posX].hpAccess() > 0:
            level[self.__posY+1][self. __posX].hit(surface)             # Down

        elif direction == 4 \
                and self.__posX > 0 \
                and level[self.__posY][self. __posX-1].hpAccess() > 0:
            level[self.__posY-self.__blocksFallen][self. __posX-1].hit(surface)             # Left

    def fall(self, surface, level):

        if self.__posY < len(level)-2 and level[self.__posY+1][self.__posX].hpAccess() == 0:
            self.__blocksFallen += 1
            self.__posY += 1

            render(surface, level, self.__currentBotLine, self.__blocksFallen)

            self.display(surface)


