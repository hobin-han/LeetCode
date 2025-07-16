I Used Stack.

Fuctions
---
- String
	- s.toCharArray()
	- s.length()
- char
	- new String(charArray)

## Remove char element and make it String and replace it.
1. set empty character : `result[index] = '\u0000';`
2. replace it to empty string : `new String(result).replace("\u0000", "");`
