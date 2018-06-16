from PIL import Image
import random
imName = input('input image name. dont add extension. only accepts pngs: ')
try:
    im = Image.open(imName + '.png')
except:
    print('image loading failed. Did you add extension? Are you in the right directory? Is it a .png image? Names are case sensitive')
    quit()
width, width = im.size
pix = im.load()
array = []
for y in range(width):
    row = []
    for x in range(width):
        row.append(0) if pix[x,y] == (0,0,0) else row.append(1)
    array.append(row)
   

def possibleMoves(x, y, checkedSpots):
    adj = []
    if y != width-1:
        adj.append((x, y+1))
    if y != 0:
        adj.append((x, y-1))
    if x != width:
        adj.append((x+1, y))
    if x != 0:
        adj.append((x-1, y))
    moves = []
    
  
    for n, k in adj:
        if array[k][n] == 1:
            if (n, k) not in checkedSpots:
                moves.append((n,k))
        
    return moves

def checkMaze():
    good = []
    good2 = []
    for x in range(width):
        good.append(0) if pix[x,0] == (0,0,0) else good.append(1)
        good2.append(0) if pix[x,width-1] == (0,0,0) else good2.append(1)
    if 1 not in good or 1 not in good2:
        return 0
    good.remove(1)
    good2.remove(1)
    if 1 in good or 1 in good2:
        return 0
    edges = [pix[0, n] for n in range(width)]
    edges += [pix[width-1, n] for n in range(width)]
    if (255, 255, 255) in edges:
        return 0
    good = True
    for i in range(width):
        for j in range(width):
            if pix[i,j] != (255,255,255) and pix[i,j] == (0,0,0):
                return 0
    return 1

def makeFinalImage(path, starter, last):
    for spot in path:
        pix[spot[0], spot[1]] = (255,0,0)
    pix[starter[0], starter[1]] = (255,0,0)
    if last != None:
        pix[last[0], last[1]] = (255,0,0)
    im.save(imName + '_solved.png')
if not checkMaze():
    print('maze is not up to code. refer to readme.md for more info')
    quit()
checkedSpots = []
choiceMade = []
path = []
for x in range(width):
    spot = (x, 0)  
    if pix[spot] == (255, 255, 255):
        currentSpot = spot
        starter = spot
        break

while currentSpot[1] != width-1:
    checkedSpots.append(currentSpot)
    pm = possibleMoves(currentSpot[0], currentSpot[1], checkedSpots)
    path.append(currentSpot)
    if len(pm) == 0:
        if len(choiceMade) == 0:
            print('not solveable')
            makeFinalImage(path, starter, None)
            img = Image.open(imName + '_solved.png')
            img.show()
            quit()
        currentSpot = choiceMade[-1]
        index = path.index(currentSpot)
        del path[index:]
    else:
        move = random.choice(pm)
        if len(pm) > 1:
            choiceMade.append(currentSpot)
        currentSpot = move
    print(currentSpot)

print('solved !!!')
makeFinalImage(path, starter, currentSpot)
img = Image.open(imName + '_solved.png')
img.show()

