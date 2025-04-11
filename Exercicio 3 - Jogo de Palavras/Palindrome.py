firstWord = "Roma"
secondWord = "Amor"
thirdWord = "Amoeba"
fourthWord = "Texto"

def reverseWord(word):
  if type(word) != str:
    raise Exception('Word is not a string')
  if len(word) == 0:
    return "Empty string"
  return word[::-1]

def isPalindrome(firstWord, secondWord):
  formatedReversedFirstWord = reverseWord(firstWord.lower().replace(" ", ""))
  formatedSecondWord = secondWord.lower().replace(" ", "")
  return formatedReversedFirstWord == formatedSecondWord

print(isPalindrome(firstWord, secondWord))
print(isPalindrome(thirdWord, fourthWord))
