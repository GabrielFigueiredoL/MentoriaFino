ladosQuadrilatero = [5,5,5,5]
angulosQuadrilatero = [90,90,90,90]

def quadrilateroQuadrado(lados, angulos):
  if len(lados) != 4 or len(angulos) != 4:
    return False
  
  testeLados = len(set(lados)) == 1
  testeAngulos = len(set(angulos)) == 1
  
  return testeLados and testeAngulos

print(quadrilateroQuadrado(ladosQuadrilatero, angulosQuadrilatero))