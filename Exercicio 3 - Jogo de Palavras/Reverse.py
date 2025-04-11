firstWord = "Amarelo"
emptyWord = ""
notAWord = 112233


def reverseWord(word):
  if type(word) != str:
    raise Exception('Word is not a string')
  if len(word) == 0:
    return "Empty string"
  return word[::-1]

print(reverseWord(firstWord))
print(reverseWord(emptyWord))
print(reverseWord(notAWord))
