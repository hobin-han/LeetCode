# HashSet
```java
Set<Integer> set = new HashSet<Integer>();

set.add(2);
set.add(2); // will be ignored
set.contains(3); // false
set.remove(2);
set.size(); // 0
set.isEmpty(); // true
```

# ArrayList
```java
List<Integer> list = new ArrayList<Integer>();

list.add(1);
list.add(2);
list.add(3);
list.add(1, 4); // [1, 4, 2, 3]

list.get(0); // 1

list.remove(1); // [1, 2, 3]
list.remove(Integer.valueOf(2)); // [1, 3] (value 2 removed)

Collections.sort(list, Collections.reverseOrder()); // [3, 1]

list.indexOf(3); // 0

list.size(); // 2
list.isEmpty(); // false
```

# HashMap
```java
Map<String, Integer> map = new HashMap<>();

map.put("banana", 3);
map.put("apple", 5);
map.put("banana", 7);

for (Map.Entry<String, Integer> entry : map.entrySet()) {
  entry.getKey();
  entry.getValue();
}

map.get("banana"); // 7
map.getOrDefault("kiwi", 0); // 0

map.remove("apple");
map.containsKey("apple"); // false
```

# String
```java
String str = "abc";
str += "def"; // "abcdef"

// use below rather than += String
StringBuilder sb = new StringBuilder();
sb.append("abc").append("def");
String result = sb.toString();

str.replace("cd", ""); // "abef"
```

# Type conversion
```java
// String to Numbers
String sNum = "123";

Integer.parseInt(sNum); // String -> Integer
Integer.valueOf(sNum); // String -> Integer
double d_num = Double.valueOf(sNum); // String -> Double
float f_num = Float.valueOf(sNum); // String -> Float
```

```java
// Numbers to String
int num = 123;

num + ""; // Integer -> String
Integer.toString(num); // Integer -> String
String.valueOf(num); // Integer -> String
```

```java
// Numbers to Numbers
int intNum = 123;
double dNum = (double)intNum;
float fNum = (float)intNum;
int iNum = (int)dNum;
```

```java
// Char to Integer(ASCII)
char c1 = 'A';
int ascii1 = (int)c1; // 65

char c2 = 'a';
int ascii2 = (int)c2; // 97
```

```java
// String to String Array
int number = 1234;
String[] digits = String.valueOf(number).split(""); // ["1", "2", "3", "4"]
```

# Math
| Category       | Method           | Return Type | Example                       | Notes                                   |
| -------------- | ---------------- | ----------- | ----------------------------- | --------------------------------------- |
| Absolute Value | `Math.abs(x)`    | int/double  | `Math.abs(-5)` → `5`          | Works with int and double               |
| Maximum        | `Math.max(a, b)` | int/double  | `Math.max(3, 7)` → `7`        |                                         |
| Minimum        | `Math.min(a, b)` | int/double  | `Math.min(3, 7)` → `3`        |                                         |
| Power          | `Math.pow(a, b)` | double      | `Math.pow(2, 3)` → `8.0`      | Returns double, cast if needed          |
| Square Root    | `Math.sqrt(x)`   | double      | `Math.sqrt(9)` → `3.0`        |                                         |
| Ceiling        | `Math.ceil(x)`   | double      | `Math.ceil(3.1)` → `4.0`      | Rounds up                               |
| Floor          | `Math.floor(x)`  | double      | `Math.floor(3.9)` → `3.0`     | Rounds down                             |
| Rounding       | `Math.round(x)`  | long        | `Math.round(3.6)` → `4`       | Returns `long`, cast to `int` if needed |
| Random         | `Math.random()`  | double      | `Math.random()` → `0.0 ~ 1.0` | Multiply and cast for integer range     |
