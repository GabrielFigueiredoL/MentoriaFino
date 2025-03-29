palavras = ["python", "programação", "fino", "tecnologia"]

def maiorPalavraDaLista(palavras):
  maiorPalavraDaLista = palavras[0]
  tamanhoMaiorPalavraDaLista = len(palavras[0])
  for palavra in palavras:
    if len(palavra) > tamanhoMaiorPalavraDaLista:
      tamanhoMaiorPalavraDaLista = len(palavra)
      maiorPalavraDaLista = palavra
  return tamanhoMaiorPalavraDaLista, maiorPalavraDaLista
  
def menorPalavraDaLista(palavras):
  menorPalavraDaLista = palavras[0]
  tamanhoMenorPalavraDaLista = len(palavras[0])
  for palavra in palavras:
    if len(palavra) < tamanhoMenorPalavraDaLista:
      tamanhoMenorPalavraDaLista = len(palavra)
      menorPalavraDaLista = palavra
  return tamanhoMenorPalavraDaLista, menorPalavraDaLista

print(maiorPalavraDaLista(palavras))
print(menorPalavraDaLista(palavras))
