firstWord = "Roma"
secondWord = "Amor"
thirdWord = "Amoeba"
fourthWord = "Texto"

def reverseWord(word):
  return word[::-1]

def isPalindrome(firstWord, secondWord):
  formatedReversedFirstWord = reverseWord(firstWord.lower().replace(" ", ""))
  formatedSecondWord = secondWord.lower().replace(" ", "")
  return formatedReversedFirstWord == formatedSecondWord

print(isPalindrome(firstWord, secondWord))
print(isPalindrome(thirdWord, fourthWord))
