words = ["jorge", "joao", "Maria", "Julia", "Médico", "Otorrinolaringologista", "até"]

def firstWord(words):
  if(len(words) == 0):
    return ""
  return words[0]

def biggestWordList(words):
  biggestWord = firstWord(words)
  for word in words:
    if len(word) > len(biggestWord):
      biggestWord = word
  return biggestWord
  
def smallerWordList(words):
  smallerWord = firstWord(words)
  for word in words:
    if len(word) < len(smallerWord):
      smallerWord = word
  return smallerWord

print(biggestWordList(words))
print(smallerWordList(words))
