## 🖨️ How to Print a Log?

```java
System.out.println("Hello, world!"); // system output
```

</br>

## 1. Data Types and Variables

### 🔹 Primitive Data Types

`int`, `float`, `double`, `long`, `boolean`, `char`

### 🔸 Reference Data Type

`String`

### 🔹 Variable Declaration

```java
String name = "hi";
int hour = 15;
double score = 90.5;
char grade = 'A';
boolean pass = true;

// You can declare a variable first and assign a value later.
String name;
name = "hello";
```

**Naming Rules**:

* Can include lowercase letters, underscores, and numbers
* Cannot contain spaces
* Case-sensitive

### 🔸 Constant

```java
final int hour = 15;
hour = 20; // ❌ Error: cannot assign a value to a final variable
```

### 🔹 Type Casting

```java
int score = 93;

// Explicit type casting
float scoreF = (float) score;
double scoreD = (double) 93;

// Implicit type casting (automatic promotion)
float scoreF = score;     // (float) is optional
double scoreD = 93;       // (double) is optional

// Explicit downcasting
double scoreD = 98.8;
int score = (int) scoreD; // must be explicitly cast
```

</br>

## 2. Operators

### 🔹 Arithmetic Operators

`+`, `-`, `*`, `/`, `%`, `++`, `--`

```java
++num; --num;   // Prefix
num++; num--;   // Postfix
```

### 🔸 Assignment Operators

`=`, `+=`, `-=`, `*=`, `/=`, `%=`

### 🔹 Comparison Operators

`>`, `>=`, `<`, `<=`, `==`, `!=`

### 🔸 Logical Operators

`&&`, `||`, `!`

### 🔹 Ternary (Conditional) Operator

```java
int max = (x > y) ? x : y;
```

</br>

## 3. Strings

```java
String s = "I like Java";
s.length();              // 11
s.toUpperCase();         // "I LIKE JAVA"
s.toLowerCase();         // "i like java"
s.contains("Java");      // true
s.indexOf("Java");       // 7
s.lastIndexOf("a");      // 10
s.startsWith("I like");  // true
s.endsWith(".");         // false
s.replace("like", "love"); // "I love Java"
s.substring(7);          // "Java"
s.trim();                // removes leading/trailing whitespace
s.concat(" and Python"); // "I like Java and Python"
```

### 🔸 String Comparison (⚠️ Don't use `==`)

```java
String s1 = "Java";
String s2 = "Java";
System.out.println(s1 == s2); // true (but not recommended)
```

```java
String s1 = new String("Java");
String s2 = new String("Java");
System.out.println(s1 == s2); // false
```

✅ Use `equals()` instead:

```java
System.out.println(s1.equals(s2)); // true
```

### 🔹 Special Characters

`\n`, `\t`, `\\`, `\"`, `\'`

</br>

## 4. Control Statements

### 🔹 Conditional Statements

```java
if (condition) {
    // ...
} else if (anotherCondition) {
    // ...
} else {
    // ...
}
```

```java
switch (condition) {
    case value1:
        // ...
        break;
    case value2:
        // ...
        break;
    default:
        // ...
}
```

### 🔸 Loops

#### `for`

```java
for (int i = 0; i < 5; i++) {
    // ...
}

for (int i = 0; i < 5; i++) {
    if (i == 3) continue;
    // ...
}
```

#### `while`

```java
while (i < 5) {
    System.out.println("hi");
    i++;
}

while (true) {
    if (i == 3) break;
    i++;
}
```

#### `do-while`

```java
do {
    // ...
} while (condition);
```

</br>

## 5. Arrays

### 🔹 Declaration

```java
int[] numbers = new int[3];
String[] names = new String[5];
names[2] = "Hobin";
```

### 🔸 Initialization

```java
int numbers[] = new int[3]; // also valid
String[] names = new String[] {"hi", "hello"};
String[] names = {"hi", "hello"}; // shorthand
```

### 🔹 Traversal

```java
for (int i = 0; i < numbers.length; i++) {
    int number = numbers[i];
}

for (int number : numbers) {
    // ...
}
```

### 🔸 Multi-dimensional Arrays

```java
int[][] numbers = new int[2][5];
numbers[0][2] = 3;

int[][] numbers = {
    {1, 2, 3, 4, 5},
    {6, 7, 8, 9, 10}
};
```

### 🔹 ASCII Codes

* Digits: `'0'` (48) to `'9'` (57)
* Uppercase letters: `'A'` (65) to `'Z'` (90)
* Lowercase letters: `'a'` (97) to `'z'` (122)

</br>

## 6. Methods

### 🔹 Basic Method

```java
public static void print(int a) {
    System.out.println(a);
}

public static int add(int a, int b) {
    return a + b;
}

int addNum = add(1, 2); // 3
```

### 🔸 Method Overloading

```java
public static int add(int a, int b) { return a + b; }
public static int add(int a, int b, int c) { return a + b + c; }
public static double add(double a, double b) { return a + b; }
```

</br>

## 7. Classes

### 🔹 Basic Class

```java
class Person {
    String name;
    int age;
    static int personCount = 0;

    public void introduce() {
        System.out.println("name: " + name);
        System.out.println("age: " + age);
    }

    public static void printPersonCount() {
        System.out.println("person count: " + personCount);
    }
}

Person person = new Person();
person.name = "Hobin Han";
person.age = 123;
person.introduce();

Person.personCount = 10;
Person.printPersonCount();
```

### 🔸 `this` keyword

```java
class Person {
    String name;
    public void setName(String name) {
        this.name = name;
    }
}
```

### 🔹 Constructor

```java
class Person {
    String name;
    int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}

Person person = new Person("Hobin", 123);
```

### 🔸 Getter and Setter

```java
class Person {
    int age;
    public int getAge() {
        return age;
    }
    public void setAge(int age) {
        this.age = age;
    }
}
```

### 🔹 Access Modifiers

* `private`: accessible only in the same class
* `public`: accessible from anywhere
* *(default)*: accessible only within the same package
* `protected`: accessible in the same package, or in subclasses from different packages

## 🔸 Inheritance

```java
class Person {
    public void introduce() {
        System.out.println("Hi, I am a person");
    }
}

class Student extends Person {
    String school;
    public void introduce() {
        System.out.println("Hi, I am a student");
    }
}
```

### 🔹 Polymorphism

```java
Person person = new Person();
Person student = new Student();

person.introduce(); // "Hi, I am a person"
student.introduce(); // "Hi, I am a student"
```

### 🔸 `super` Keyword

```java
class Person {
    String name;
    int age;
    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}

class Student extends Person {
    String school;
    Student(String name, int age, String school) {
        super(name, age);
        this.school = school;
    }
}
```

### 🔹 Enum

```java
enum Gender {
    MALE,
    FEMALE
}

Gender gender = Gender.MALE;

switch (gender) {
    case MALE:
        // ...
        break;
    case FEMALE:
        // ...
        break;
}
```

</br>

## 8. Abstract Class & Interface

### 🔹 Abstract Class

```java
abstract class Shape {
    abstract double calculateArea();
}

class Square extends Shape {
    private double s;
    public Square(double s) {
        this.s = s;
    }
    double calculateArea() {
        return s * s;
    }
}

class Circle extends Shape {
    private double r;
    public Circle(double r) {
        this.r = r;
    }
    double calculateArea() {
        return Math.PI * r * r;
    }
}
```

### 🔸 Interface

```java
interface Shape {
    double calculateArea();
}

class Square implements Shape {
    private double s;
    public Square(double s) {
        this.s = s;
    }
    public double calculateArea() {
        return s * s;
    }
}

class Circle implements Shape {
    private double r;
    public Circle(double r) {
        this.r = r;
    }
    public double calculateArea() {
        return Math.PI * r * r;
    }
}
```

</br>

## ❌ Topics Not Covered

The following topics are out of scope for this document, as it focuses on Java review for coding tests:

* Generics
* Anonymous Classes & Lambda Expressions
* Exception Handling
* Multithreading
* I/O and File Handling
