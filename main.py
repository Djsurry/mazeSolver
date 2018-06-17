from PIL import Image
import random, sys, time
imName = sys.argv[1]
try:
    im = Image.open(imName )
except:
    print('image loading failed.')
    quit()
print(im.size)
im = im.convert('RGB')
width, height = im.size
pix = im.load()
array = []
for y in range(height):
    row = []
    for x in range(width):
        row.append(0) if pix[x,y] == (0,0,0) else row.append(1)
    array.append(row)
   

def possibleMoves(x, y, checkedSpots):
    adj = []
    if y != height-1:
        adj.append((x, y+1))
    if y != 0:
        adj.append((x, y-1))
    if x != width:
        adj.append((x+1, y))
    if x != 0:
        adj.append((x-1, y))
    moves = []
    
  
    for n, k in adj:
        if pix[n,k] == (255, 255, 255):
            if (n, k) not in checkedSpots:
                moves.append((n,k))
        
    return moves

def checkMaze():
    good = []
    good2 = []
    for x in range(width):
        
        good.append(pix[x,0])
        good.append(pix[x,height-1])
        
    if (255, 255, 255) not in good:
        print('neither the top or bottom rows have white pixels')
        return 0
       
    good.remove((255, 255, 255))
    try:
        good.remove((255, 255, 255))
    except:
        print('top or bottom row doesnt have a white pixel')
        return 0
    if (255, 255, 255) in good:
        print('more than one white pixel in one of the top or bottom rows')
        return 0
    edges = [pix[0, n] for n in range(height)]
    edges += [pix[width-1, n] for n in range(height)]
    if (255, 255, 255) in edges:
        print('there is a white pixel on one of the edges')
        return 0
    good = True
    for i in range(height):
        for j in range(width):
            if pix[i,j] != (255, 255, 255) and pix[i,j] != (0, 0, 0):
               
                print('pixel', i + ',', j, 'doesnt have and rgb value of 255, 255, 255, or 0,0,0')
                return 0
    
    return 1

def makeFinalImage(path, starter, last, imTitle):
    
    
    
    for spot in path:
        pix[spot] = (255,0,0)
    pix[starter[0], starter[1]] = (255,0,0)
    if last != None:
        pix[last[0], last[1]] = (255,0,0)

    im.save(imTitle + '_solved.png')
    return imTitle + '_solved.png'
if not checkMaze():
    print('maze is not up to code. refer to readme.md for more info')
    quit()
checkedSpots = []
choiceMade = []
path = []
s = time.time()
for x in range(width):
    spot = (x, 0)  
    if pix[spot] == (255, 255, 255):
        currentSpot = spot
        starter = spot
        break
print('working')
while currentSpot[1] != height-1:
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
        if choiceMade[-1] == currentSpot:
            choiceMade.remove(currentSpot)
        currentSpot = choiceMade[-1]
        index = path.index(currentSpot)
        del path[index:]
    else:

        move = random.choice(pm)
        if len(pm) > 1:
            choiceMade.append(currentSpot)
        currentSpot = move
    print(currentSpot)
t = time.time() - s

print('solved !!!')
print('it took', str(round(t, 2)), ' seconds to solve ' + imName)
imTitle = imName.split('.')[0]
name = makeFinalImage(path, starter, currentSpot, imTitle)
img = Image.open(name)
img.show()

    












