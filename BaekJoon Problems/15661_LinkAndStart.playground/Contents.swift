// https://www.acmicpc.net/problem/15661

import Foundation

func solution(n: Int, array: [[Int]]) -> Int {
    var minDiff = Int.max
    let allPeople = Array(1...n)
    
    for t1Count in 1...n/2 {
        for t1 in getAvailableArrays(n: n, count: t1Count) {
            let t2 = remove(from: allPeople, with: t1)
            let diff = getSum(t1, array: array) - getSum(t2, array: array)
            minDiff = min(minDiff, abs(diff))
        }
    }
    return minDiff
}

func remove(from a: [Int], with b: [Int]) -> [Int] {
    var result = [Int]()
    for i in a {
        if !b.contains(i) {
            result.append(i)
        }
    }
    return result
}

func getAvailableArrays(n: Int, count: Int) -> [[Int]] {
    var result = [[Int]]()
    if count == 1 {
        for i in 1...n {
            result.append([i])
        }
    } else {
        for arr in getAvailableArrays(n: n, count: count - 1) {
            let lastValue = arr.last!
            if lastValue < n {
                for i in (lastValue + 1)...n {
                    var newArr = arr
                    newArr.append(i)
                    result.append(newArr)
                }
            }
        }
    }
    return result
}

func getSum(_ t: [Int], array: [[Int]]) -> Int {
    var result = 0
    for p1 in t {
        for p2 in t {
            let a = array[p1 - 1][p2 - 1]
            result += a
        }
    }
    return result
}

let s1 = solution(n: 6, array: [
    [0, 1, 2, 3, 4, 5],
    [1, 0, 2, 3, 4, 5],
    [1, 2, 0, 3, 4, 5],
    [1, 2, 3, 0, 4, 5],
    [1, 2, 3, 4, 0, 5],
    [1, 2, 3, 4, 5, 0],
])
print(s1 == 2)

let s2 = solution(n: 8, array: [
    [0, 5, 4, 5, 4, 5, 4, 5],
    [4, 0, 5, 1, 2, 3, 4, 5],
    [9, 8, 0, 1, 2, 3, 1, 2],
    [9, 9, 9, 0, 9, 9, 9, 9],
    [1, 1, 1, 1, 0, 1, 1, 1],
    [8, 7, 6, 5, 4, 0, 3, 2],
    [9, 1, 9, 1, 9, 1, 0, 9],
    [6, 5, 4, 3, 2, 1, 9, 0]
])
print(s2 == 1)

let s3 = solution(n: 5, array: [
    [0, 3, 1, 1, 1],
    [3, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0],
])
print(s3 == 0)

