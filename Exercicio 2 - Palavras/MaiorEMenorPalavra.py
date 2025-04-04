palavras = ["jorge", "joao", "Maria", "Julia", "Médico", "Otorrinolaringologista", "até"]

def primeiraPalavra(palavras):
  if(len(palavras) == 0):
    return ""
  return palavras[0]

def maiorPalavraDaLista(palavras):
  maiorPalavraDaLista = primeiraPalavra(palavras)
  tamanhoMaiorPalavraDaLista = len(maiorPalavraDaLista)
  for palavra in palavras:
    if len(palavra) > tamanhoMaiorPalavraDaLista:
      tamanhoMaiorPalavraDaLista = len(palavra)
      maiorPalavraDaLista = palavra
  return tamanhoMaiorPalavraDaLista, maiorPalavraDaLista
  
def menorPalavraDaLista(palavras):
  menorPalavraDaLista = primeiraPalavra(palavras)
  tamanhoMenorPalavraDaLista = len(menorPalavraDaLista)
  for palavra in palavras:
    if len(palavra) < tamanhoMenorPalavraDaLista:
      tamanhoMenorPalavraDaLista = len(palavra)
      menorPalavraDaLista = palavra
  return tamanhoMenorPalavraDaLista, menorPalavraDaLista

print(maiorPalavraDaLista(palavras))
print(menorPalavraDaLista(palavras))
