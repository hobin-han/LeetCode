import Foundation

// MARK: - 0. Print & Comment

print("Hello, world!")

// hihi
/*
 hell
 hi
 */

// MARK: - 1. String

let str1 = "Hello"
let str2 = "hi"
let str3 = String(repeating: "Hi", count: 3) // HiHiHi

let sentence = "Hihi hello I am hobin."

// Indexing
let firstChar = sentence.first!     // "H"
let slice = sentence.prefix(4)      // "Hihi"
let lastFive = sentence.suffix(5)   // "obin."

// Upper / Lower
let upper = sentence.uppercased()
let lower = sentence.lowercased()

// Length
let len = sentence.count   // 22

// Replace
let replaced = sentence.replacingOccurrences(of: "I am", with: "I'm")

// Contains / Index
let hasI = sentence.contains("I")
let idx = sentence.firstIndex(of: "h")  // Optional index

// MARK: - 2. Boolean

print(5 > 10)        // false
print(true)          // true
print(!true)         // false
print(!(5 > 10))     // true

// MARK: - 3. Variable

var name = "Hobin"
var age = 20
let isAdult = age >= 19

print("Hi I am \(name)! And I'm \(age) years old.")
// Hi I am Hobin! And I'm 20 years old.

// MARK: - 4. Operator

print(1 + 1)   // 2
print(3 - 2)   // 1
print(5 * 2)   // 10
print(6 / 3)   // 2
print(2 % 3)   // 2

var number = 10
number += 2  // 12
number *= 2  // 24

// MARK: - 5. Math

abs(-5)           // 5
pow(4.0, 2.0)     // 16.0
sqrt(16.0)        // 4.0
max(5, 12)        // 12
min(5, 12)        // 5
round(3.14)       // 3.0
floor(4.99)       // 4.0
ceil(4.01)        // 5.0

Int.random(in: 1...45)  // 1~45 무작위 정수

// MARK: - 6. Array

var nums = [10, 20, 30]

nums.append(40)         // [10,20,30,40]
nums.insert(50, at: 1)  // [10,50,20,30,40]

nums.popLast()          // remove last
nums.remove(at: 1)      // remove index

nums.count              // length
nums.contains(20)       // true

nums.sort()             // 오름차순
nums.reverse()          // 뒤집기

// MARK: - 7. Dictionay

var dict = [3: "hihi", 100: "hello"]

dict[3]              // "hihi"
dict[5]              // nil (안전)
dict[5, default: "unknown"]  // "unknown"

dict[3] = "hi"
dict[7] = "new"

dict.removeValue(forKey: 3)

for (key, value) in dict {
    print(key, value)
}

// MARK: - 8. Set

var mySet: Set<Int> = [1, 2, 3, 3]   // {1,2,3}
mySet.insert(5)       // {1,2,3,5}

let set1: Set = [1, 2, 3]
let set2: Set = [2, 10]

set1.union(set2)            // {1,2,3,10}
set1.intersection(set2)     // {2}
set1.subtracting(set2)      // {1,3}

// MARK: - 9. Tuple

let greet = ("hi", "hello")
greet.0    // "hi"
greet.1    // "hello"

// MARK: - 10. Condition

if age >= 19 {
    print("Adult")
} else {
    print("Child")
}

// MARK: - 11. Loop

for i in 1...5 { // 1 ≤ n ≤ 5
//    print(i)
}
for i in 1..<5 { // 1 ≤ n < 5
//    print(i)
}

for i in stride(from: 0, to: 10, by: 2) {
    print("stride \(i)")
}

var count = 0
while count < 3 {
    print(count)
    count += 1
}

// MARK: - 12. Function

func add(a: Int, b: Int) -> Int {
    return a + b
}
add(a: 1, b: 2) // 3

func greet(name: String, age: Int = 20) {
    print("Hi I am \(name). I am \(age) years old.")
}
greet(name: "Hobin")          // default age 20
greet(name: "Hobin", age: 30) // custom age


// MARK: - 13. Swap Values

var a = 2
var b = 5
swap(&a, &b)
print("swap \(a) \(b)")


// MARK: - 14. Reverse / Sort

let str = "abcd"
let reversed = String(str.reversed())   // "dcba"

var arr = [3,1,4,2]
arr.sort()         // [1,2,3,4]
arr.sort(by: >)    // [4,3,2,1]
