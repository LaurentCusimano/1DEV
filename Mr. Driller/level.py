from random import randint
import block

level = []


def generateLvl(colors, lines, width,pillP=5,PillPL=5,SoloP=20,UnbreakableP=5,DelayedP=0):    # This returns a 2D array of blocks [Y][X]
    #pillPL est le nombre de pill par level
    for i in range(lines+5):
        line = []

        if i in range(5):   # Override for first 5 lines -> generates empty blocks
            for j in range(width):
                newBlock = block.Classic(j, i, 1, 0)
                line.append(newBlock)

        elif i in range(lines):
            for j in range(width):

                PillRn = randint(0, 100)

                UnbreakableRn = randint(0,100)

                DelayedRn = randint(0, 100)

                SoloRn = randint(0, 100)


                if PillRn<pillP and PillPL !=0:
                    PillPL -=1
                    newBlock = block.Pill(j, i)
                    line.append(newBlock)

                elif SoloRn < SoloP:
                    newBlock = block.Solo(j, i)
                    line.append(newBlock)

                elif UnbreakableRn < UnbreakableP:
                    newBlock = block.Unbreakable(j, i)
                    line.append(newBlock)

                elif DelayedRn < DelayedP:
                    newBlock = block.Delayed(j, i)
                    line.append(newBlock)

                else:
                    newBlock = block.Classic(j, i, randint(1, colors), 1)
                    line.append(newBlock)
        else:
            for j in range(width):
                newBlock = block.End(j, i)
                line.append(newBlock)

        level.append(line)

    return level


def render(surface, level, currOffset):

    # init
    if currOffset == 0:
        for i in range(currOffset, currOffset + 9, 1):
            for element in level[i]:
                element.display(surface)

    # scroll up
    else:
        for i in range(currOffset, currOffset+9, 1):
            for element in level[i]:
                element.display(surface, 0, currOffset)







