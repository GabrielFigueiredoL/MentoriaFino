# Repositório Mentoria Fino
Repositório desenvolvido para a entrega das atividades propostas na mentoría do Fino.


## Atividade 1 - Mentoria Fino
Atividade desenvolvida para resolver 5 funções em python:
- Se o quadrilátero é um quadrado;
- Área do quadrilátero;
- Perímetro do quadrilátero;
- Área do triângulo;
- Perímetro do triângulo.

### Se o quadrilátero é um quadrado
Dado duas listas para uma função `squareQuadrilateral`( sidesQuadrilateral, anglesQuadrilateral ), ela retorna True caso seja um quadrado e False caso não seja.
```python
sidesQuadrilateral = [5,5,5,5]
anglesQuadrilateral = [90,90,90,90]
print(squareQuadrilateral(sidesQuadrilateral, anglesQuadrilateral)) # output -> True
```

### Área do quadrilátero
Dado dois números para uma função `areaQuadrilateral(5,5)`, ela retorna a área do quadrilátero.
```python
areaQuadrilateral(5,5) # output -> 25
```

### Perímetro do quadrilátero
Dado quatro números para uma função `PerimeterQuadrilateral(side1, side2, side3, side4)`, ela retorna o perímetro do quadrilátero.
```python
PerimeterQuadrilateral(5,5,4,4) # output -> 18
```

### Área do triângulo
Dado dois números para uma função `areaTriangle(10,5)`, ela retorna a área do triângulo.
```python
areaTriangle(10,5) # output -> 25
```

### Perímetro do triângulo
Dado três números para uma função `perimeterTriangle(5,5,5)`, ela retorna o perímetro do triângulo.
```python
perimeterTriangle(5,5,5) # output -> 15
```


## Atividade 2 - Mentoria Fino
Atividade desenvolvida para resolver 2 funções em python ao receber uma lista de palavras:
- retornar a maior palavra
- retornar a menor palavra

### Maior palavra
Dado uma lista de palavras para uma função biggestWordList(words), retornar a maior palavra da lista.
```python
words = ["Abracadabra", "Baralho", "Cartola", "Mágico", "Coelho"]
print(biggestWordList(words)) # output -> Abracadabra
```

### Menor palavra
Dado uma lista de palavras para uma função smallerWordList(words), retornar a menor palavra da lista.
```python
words = ["Abracadabra", "Baralho", "Cartola", "Mágico", "Coelho, Cor"]
print(smallerWordList(words)) # output -> Cor
```

## Atividade 3 - Mentoria Fino
Atividade desenvolvida para resolver 3 funções em python:
- Inverter uma palavra;
- Dado duas palavras, dizer se são palíndromos;
- Dado duas palavras, dizer se são anagramas.

### Inverter uma palavra
Dado uma palavra uma função reverseWord(word), retornar a palavra invertida.
```python
print(reverseWord("roma")) # output -> amor
```

### Dado duas palavras, dizer se são palíndromos
Dado duas palavras para uma função isPalindrome("amor", "roma"), retornar um booleano dizendo se as palavras são palíndromos.
```python
print(isPalindrome("roma", "amor")) # output -> True
print(isPalindrome("amarelo", "azul")) # output -> False
```

### Dado duas palavras, dizer se são anagramas
Dado duas palavras para uma função isAnagram("amor", "roma"), retornar um booleano dizendo se as palavras são anagramas.
```python
print(isAnagram("pedra", "padre")) # output -> True
print(isAnagram("remo", "toma")) # output -> False
```
