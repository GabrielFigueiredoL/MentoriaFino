firstWord = "Tom Marvolo Riddle"
secondWord = "I am Lord Voldemort"
thirdWord = "Pedra"
fourthWord = "Padre"
fifthWord = "Remo"
sixthWord = "Toma"

def countLetters(word):
  formattedWord = word.upper().replace(" ", "")
  wordDict = {}
  for letter in formattedWord:
    if wordDict.get(letter) == None:
      wordDict[letter] = 1
    else:
      wordDict[letter] = wordDict.get(letter) + 1
  return wordDict

def isAnagram(firstWord, secondWord):
  firstWordDict = countLetters(firstWord)
  secondWordDict = countLetters(secondWord)
  return firstWordDict == secondWordDict

print(isAnagram(firstWord, secondWord))
print(isAnagram(thirdWord, fourthWord))
print(isAnagram(fifthWord, sixthWord))
