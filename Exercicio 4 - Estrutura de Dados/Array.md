An `array` is a data structure used to store multiple elements in a single variable, organized in a specific order. In most programming languages, elements in an array are stored in contiguous (adjacent) memory locations.
An array its used when its needed to access items quickly by index, the items is in a specific order and the number of elements is mostly fixed or not changing a lot.
![[arrayImage.png]]
### Java:
```java
int[] numbers = {1, 2, 3, 4}; // ✅
int[] numbers = {1, "data", 3, 4} // ❌
```

> [!IMPORTANT]
> In Java, an array can only store elements of a single data type, such as strings, numbers, or objects, etc.
### Python
```python
array = [1, 2, 3, 4] # ✅
array = [1, 2, "data", 3] # ✅
```

> [!NOTE]
> The python code above actually generates a python `List` data type.
