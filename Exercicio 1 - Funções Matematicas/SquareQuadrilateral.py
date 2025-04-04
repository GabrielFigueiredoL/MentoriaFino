sidesQuadrilateral = [5,5,5,5]
anglesQuadrilateral = [90,90,90,90]

def squareQuadrilateral(side, angle):
  if len(side) != 4 or len(angle) != 4:
    return False
  
  testRightAngle = sum(angle) == 360
  testSide = len(set(side)) == 1
  testeAngle = len(set(angle)) == 1
  
  return testSide and testeAngle and testRightAngle

print(squareQuadrilateral(sidesQuadrilateral, anglesQuadrilateral))