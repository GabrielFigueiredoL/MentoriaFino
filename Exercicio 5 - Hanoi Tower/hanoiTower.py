firstTower = [ 7, 6, 5, 4, 3, 2, 1]
secondTower = []
thirdTower = []
piecesCount = len(firstTower)

def changeTower(baseTower, targetTower):
  baseTowerPeek = baseTower[-1] if len(baseTower) != 0 else None
  targetTowerPeek = targetTower[-1] if len(targetTower) != 0 else None 
  if targetTowerPeek == None:
    targetTower.append(baseTower.pop()) 
  elif baseTowerPeek == None:
    baseTower.append(targetTower.pop())
  elif baseTowerPeek > targetTowerPeek:
    baseTower.append(targetTower.pop())
  else:
    targetTower.append(baseTower.pop())
  return 1

def checkTower(tower, piecesCount):
  if len(tower) != piecesCount:
    return False
  return True

def step(firstTower, secondTower, thirdTower, steps, piecesCount):
  if checkTower(secondTower, piecesCount) or checkTower(thirdTower, piecesCount):
    return steps, True
  if steps % 3 == 0:
    steps += changeTower(firstTower, secondTower)
  elif steps % 3 == 1:
    steps += changeTower(firstTower, thirdTower)
  elif steps % 3 == 2:
    steps += changeTower(secondTower, thirdTower)
  return steps, False

def hanoi(firstTower, secondTower, thirdTower, piecesCount):
  steps = 0
  stop = False
  while not stop:
    steps, stop = step(firstTower, secondTower, thirdTower, steps, piecesCount)
  return steps

print(hanoi(firstTower, secondTower, thirdTower, piecesCount))
print(firstTower)
print(secondTower)
print(thirdTower)
