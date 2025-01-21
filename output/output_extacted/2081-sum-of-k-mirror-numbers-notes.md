## Sum of K-Mirror Numbers
**Problem Link:** https://leetcode.com/problems/sum-of-k-mirror-numbers/description

**Problem Statement:**
- Input: An integer `k`.
- Output: The sum of all `k`-mirror numbers.
- Key requirements: A `k`-mirror number is a number whose numeral is a rotation of the numeral of its `k`-th power.
- Edge cases: `k` is in the range `[1, 10]`.

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate all numbers up to a certain limit, calculate their `k`-th power, and check if the numeral is a rotation of the original number.
- Step-by-step breakdown:
  1. Define a function to check if a number is a `k`-mirror number.
  2. Iterate over all numbers up to a certain limit.
  3. For each number, calculate its `k`-th power.
  4. Check if the numeral of the number is a rotation of the numeral of its `k`-th power.
  5. If it is, add the number to the sum.
- Why this approach comes to mind first: It is a straightforward approach that checks all possible numbers.

```cpp
#include <iostream>
#include <string>

bool isKMirror(int num, int k) {
    long long power = 1;
    for (int i = 0; i < k; i++) {
        power *= num;
    }
    std::string numStr = std::to_string(num);
    std::string powerStr = std::to_string(power);
    for (int i = 0; i < numStr.size(); i++) {
        bool isRotation = true;
        for (int j = 0; j < numStr.size(); j++) {
            if (numStr[(i + j) % numStr.size()] != powerStr[j]) {
                isRotation = false;
                break;
            }
        }
        if (isRotation) {
            return true;
        }
    }
    return false;
}

int sumOfKMirror(int k) {
    int sum = 0;
    for (int i = 1; i <= 100000; i++) {
        if (isKMirror(i, k)) {
            sum += i;
        }
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m^2)$, where $n$ is the limit of numbers and $m$ is the average number of digits in a number.
> - **Space Complexity:** $O(m)$, where $m$ is the maximum number of digits in a number.
> - **Why these complexities occur:** The time complexity is due to the nested loops in the `isKMirror` function, and the space complexity is due to the conversion of numbers to strings.

### Optimal Approach (Required)
**Explanation:**
- Key insight: We only need to check numbers up to $10^k$, as the number of digits in the `k`-th power of a number cannot exceed $k$.
- Detailed breakdown:
  1. Define a function to check if a number is a `k`-mirror number.
  2. Iterate over all numbers up to $10^k$.
  3. For each number, calculate its `k`-th power.
  4. Check if the numeral of the number is a rotation of the numeral of its `k`-th power.
  5. If it is, add the number to the sum.
- Proof of optimality: We have reduced the number of iterations from $n$ to $10^k$, which is a significant improvement.

```cpp
#include <iostream>
#include <string>

bool isKMirror(int num, int k) {
    long long power = 1;
    for (int i = 0; i < k; i++) {
        power *= num;
    }
    std::string numStr = std::to_string(num);
    std::string powerStr = std::to_string(power);
    for (int i = 0; i < numStr.size(); i++) {
        bool isRotation = true;
        for (int j = 0; j < numStr.size(); j++) {
            if (numStr[(i + j) % numStr.size()] != powerStr[j]) {
                isRotation = false;
                break;
            }
        }
        if (isRotation) {
            return true;
        }
    }
    return false;
}

int sumOfKMirror(int k) {
    int sum = 0;
    for (int i = 1; i <= pow(10, k); i++) {
        if (isKMirror(i, k)) {
            sum += i;
        }
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(10^k \cdot m^2)$, where $m$ is the average number of digits in a number.
> - **Space Complexity:** $O(m)$, where $m$ is the maximum number of digits in a number.
> - **Optimality proof:** We have reduced the number of iterations from $n$ to $10^k$, which is a significant improvement.

### Final Notes

**Learning Points:**
- Key algorithmic concepts: iteration, string manipulation, and modular arithmetic.
- Problem-solving patterns: reducing the number of iterations and using efficient data structures.
- Optimization techniques: reducing the number of iterations and using efficient algorithms.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases and not optimizing the algorithm.
- Edge cases to watch for: numbers with leading zeros and numbers with more than $k$ digits.
- Performance pitfalls: using inefficient algorithms and not optimizing the code.
- Testing considerations: testing the code with different inputs and edge cases.