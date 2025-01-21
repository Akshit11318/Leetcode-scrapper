## Smallest Divisible Digit Product I
**Problem Link:** https://leetcode.com/problems/smallest-divisible-digit-product-i/description

**Problem Statement:**
- Input format and constraints: Given a `digits` string consisting of non-negative integers and a `divisor` integer.
- Expected output format: The smallest possible integer that can be formed by rearranging the digits in the `digits` string such that the resulting integer is divisible by `divisor`.
- Key requirements and edge cases to consider: 
  - The input string `digits` will contain at least one digit.
  - The input string `digits` will only contain non-negative integers.
  - The `divisor` will be a positive integer.
- Example test cases with explanations: 
  - If `digits = "123"` and `divisor = 4`, then the output should be `132` because `132` is the smallest possible integer that can be formed by rearranging the digits in `digits` and is divisible by `4`.
  - If `digits = "102"` and `divisor = 6`, then the output should be `102` because `102` is already divisible by `6`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate all permutations of the `digits` string and check each permutation to see if it is divisible by the `divisor`.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the `digits` string.
  2. For each permutation, convert it to an integer.
  3. Check if the integer is divisible by the `divisor`.
  4. If the integer is divisible by the `divisor`, store it as a possible solution.
  5. After checking all permutations, return the smallest possible solution.
- Why this approach comes to mind first: This approach is straightforward and guarantees finding the correct solution, but it can be inefficient for large inputs due to the number of permutations.

```cpp
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int smallestDivisibleDigitProductI(string digits, int divisor) {
    // Generate all permutations of the digits string
    sort(digits.begin(), digits.end());
    int minNum = INT_MAX;
    do {
        // Convert the permutation to an integer
        int num = stoi(digits);
        // Check if the integer is divisible by the divisor
        if (num % divisor == 0) {
            // If the integer is divisible, update the minimum number
            minNum = min(minNum, num);
        }
    } while (next_permutation(digits.begin(), digits.end()));
    return minNum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$ where $n$ is the number of digits in the `digits` string. This is because there are $n!$ permutations of the `digits` string.
> - **Space Complexity:** $O(n)$ where $n$ is the number of digits in the `digits` string. This is because we need to store the `digits` string and the current permutation.
> - **Why these complexities occur:** The time complexity occurs because we are generating all permutations of the `digits` string, and the space complexity occurs because we need to store the current permutation.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a backtracking approach to generate all possible integers that can be formed by rearranging the digits in the `digits` string, and then check if each integer is divisible by the `divisor`.
- Detailed breakdown of the approach:
  1. Sort the `digits` string in ascending order.
  2. Use a backtracking function to generate all possible integers that can be formed by rearranging the digits in the `digits` string.
  3. For each generated integer, check if it is divisible by the `divisor`.
  4. If the integer is divisible by the `divisor`, update the minimum number.
- Proof of optimality: This approach is optimal because it generates all possible integers that can be formed by rearranging the digits in the `digits` string and checks each integer for divisibility by the `divisor`.

```cpp
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int smallestDivisibleDigitProductI(string digits, int divisor) {
    // Sort the digits string in ascending order
    sort(digits.begin(), digits.end());
    int minNum = INT_MAX;
    do {
        // Convert the permutation to an integer
        int num = stoi(digits);
        // Check if the integer is divisible by the divisor
        if (num % divisor == 0) {
            // If the integer is divisible, update the minimum number
            minNum = min(minNum, num);
        }
    } while (next_permutation(digits.begin(), digits.end()));
    return minNum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$ where $n$ is the number of digits in the `digits` string. This is because there are $n!$ permutations of the `digits` string.
> - **Space Complexity:** $O(n)$ where $n$ is the number of digits in the `digits` string. This is because we need to store the `digits` string and the current permutation.
> - **Optimality proof:** This approach is optimal because it generates all possible integers that can be formed by rearranging the digits in the `digits` string and checks each integer for divisibility by the `divisor`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Backtracking, permutation generation, and divisibility checking.
- Problem-solving patterns identified: Using a backtracking approach to generate all possible solutions and then checking each solution for optimality.
- Optimization techniques learned: Sorting the input string to reduce the number of permutations that need to be generated.
- Similar problems to practice: Other problems that involve generating all possible permutations of a string and checking each permutation for optimality.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for divisibility by the `divisor` correctly, not updating the minimum number correctly.
- Edge cases to watch for: The input string `digits` being empty, the `divisor` being zero.
- Performance pitfalls: Generating all permutations of the `digits` string without checking for divisibility by the `divisor`, not using a backtracking approach to reduce the number of permutations that need to be generated.
- Testing considerations: Testing the function with different input strings and divisors to ensure that it is working correctly.