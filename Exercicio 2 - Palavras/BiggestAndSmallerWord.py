words = ["Abracadabra", "Baralho", "Cartola", "Mágico", "Coelho"]

def firstWord(words):  
  if type(words) != list:
    raise Exception('Words is not a List')
  
  if not words:
    raise Exception('List is empty')
  
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
