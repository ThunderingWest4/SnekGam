import pygame
import random
import time
#https://www.geeksforgeeks.org/a-search-algorithm/

pygame.init()
pygame.font.init()

res = (960, 960)

MAX = 30
Goal = ()
def GoalInit():
    return (random.randint(0, (MAX - 1)), random.randint(0, (MAX - 1)))

Goal = GoalInit()
print(Goal)

screen = pygame.display.set_mode(res)

Grid = [[("s" if((i == 0) and (j == 0)) else "e" if ((i == Goal[0]) and (j == Goal[1])) else "n") for i in range(MAX)] for j in range(MAX)]

#Grid = start()
#begin()

#pygame.draw.rect(screen, color, pygame.Rect(XCoord, YCoord, Length, Width))


Start = (0, 0)
Blue = (0, 0, 255)
HeadCol = ((8*16), (8*16), 255)
GoalCol = (255, 215, 0)
Other = (0, 255, 0)
Red = (255, 0, 0)
run = True
#only one max val bc its a square

#Manhattan Distance –

#It is nothing but the sum of absolute values of differences in the goal’s x and y coordinates and the headent cell’s x and y coordinates respectively, i.e.,
# h = abs (headent_cell.x – goal.x) + 
#     abs (headent_cell.y – goal.y) 

targetfps = 60
 
clock = pygame.time.Clock()
head = Start

time.sleep(5)
snekBody = [head]
size = 1

while(run == True):
    #head = ()
    goal = (Goal[1], Goal[0])
    c = 0
    for col in Grid:
        v = 0
        for o in col:
            #if(o == "s"):
            #    pygame.draw.rect(screen, Blue, pygame.Rect((c*21), (v*21), 20, 20))
                #head = (c, v)
            if(o == "e"):
                pygame.draw.rect(screen, Red, pygame.Rect((c*(MAX+1)), (v*(MAX+1)), MAX, MAX))
            else:
                pygame.draw.rect(screen, Other, pygame.Rect((c*(MAX+1)), (v*(MAX+1)), MAX, MAX))



            v += 1

        c += 1
    for g in snekBody:
        pygame.draw.rect(screen, Blue, pygame.Rect((g[0]*(MAX+1)), (g[1]*(MAX+1)), MAX, MAX))
    pygame.draw.rect(screen, HeadCol, pygame.Rect((snekBody[len(snekBody)-1][0]*(MAX+1)), (snekBody[len(snekBody)-1][1]*(MAX+1)), MAX, MAX))

    if(not (head == goal)):
        #basically if we're not at the goal
        headH = abs(head[0] - goal[0]) + abs(head[1] - goal[1])
        print(headH)
        adjoining = []
        
        if((head[1] + 1) < MAX): adjoining.append((head[0], head[1] + 1)) #the block *above*
        if((head[1] - 1) >= 0): adjoining.append((head[0], head[1] - 1)) #the block *below*
        if((head[0] + 1) < MAX): adjoining.append((head[0] + 1, head[1])) #the block to the *right*
        if((head[0] - 1) >= 0): adjoining.append((head[0] - 1, head[1])) #the block to the *left*
        HDict = {}
        for obj in adjoining:
            HDict[obj] = (abs(obj[0] - goal[0]) + abs(obj[1] - goal[1]))
        #sort Heuristic Array by val
        #thanks @ https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
        getH = 0
        SmallestH = ()
        for key, value in sorted(HDict.items(), key=lambda item: item[1]):
            print("%s: %s" % (key, value))
            if(getH == 0):
                #SmallestH = HDict[i]
                SmallestH = key
            getH += 1

        #print(HDict)

        print(SmallestH, goal, Goal)
        
        #SmallestH is now the idealplace
        #Grid[SmallestH[1]][SmallestH[0]] = 's'
        head = SmallestH
        snekBody.append(SmallestH)
        snekBody.remove(snekBody[0])
        print(snekBody)

    else:
        print("Apple Reached")
        while(Goal in snekBody):
            Goal = GoalInit()
        #Grid = start()
        #begin()
        a = [[("s" if((f == head[0]) and (j == head[1])) else "e" if ((f == Goal[0]) and (j == Goal[1])) else "n") for f in range(MAX)] for j in range(MAX)]
        Grid = a
        #head = Start
        snekBody.append(head)
        snekBody.append(head)
        #time.sleep(3)
        #time.sleep(100)
    for event in pygame.event.get():
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.key.Q):
                pygame.quit()
        else:
            pass
                
    clock.tick(targetfps)
    pygame.display.flip()