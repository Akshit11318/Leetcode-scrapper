## Fizz Buzz
**Problem Link:** [https://leetcode.com/problems/fizz-buzz/description](https://leetcode.com/problems/fizz-buzz/description)

**Problem Statement:**
- Input format and constraints: Given an integer `n`, return a list of strings from 1 to `n` where:
  - For multiples of 3, replace the number with the string "Fizz".
  - For multiples of 5, replace the number with the string "Buzz".
  - For numbers which are multiples of both 3 and 5, replace the number with the string "FizzBuzz".
- Expected output format: A list of strings.
- Key requirements and edge cases to consider:
  - Handling multiples of 3 and 5.
  - Handling numbers that are not multiples of 3 or 5.
- Example test cases with explanations:
  - For `n = 5`, the output should be `["1", "2", "Fizz", "4", "Buzz"]`.
  - For `n = 3`, the output should be `["1", "2", "Fizz"]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over all numbers from 1 to `n` and check each number for divisibility by 3 and 5.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store the result.
  2. Loop through each number from 1 to `n`.
  3. For each number, check if it is divisible by both 3 and 5. If so, append "FizzBuzz" to the result list.
  4. If the number is only divisible by 3, append "Fizz" to the result list.
  5. If the number is only divisible by 5, append "Buzz" to the result list.
  6. If the number is not divisible by either 3 or 5, append the number as a string to the result list.
- Why this approach comes to mind first: It directly follows the problem statement's requirements and is straightforward to implement.

```cpp
vector<string> fizzBuzz(int n) {
    vector<string> result;
    for (int i = 1; i <= n; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            result.push_back("FizzBuzz");
        } else if (i % 3 == 0) {
            result.push_back("Fizz");
        } else if (i % 5 == 0) {
            result.push_back("Buzz");
        } else {
            result.push_back(to_string(i));
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we are looping through each number from 1 to `n` once.
> - **Space Complexity:** $O(n)$ because we are storing each result in a list.
> - **Why these complexities occur:** The loop iterates `n` times, and each iteration performs constant time operations. The space complexity is due to storing `n` results.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved by iterating over the range of numbers and applying the rules for "Fizz", "Buzz", and "FizzBuzz" directly. This is the same insight as the brute force approach because the problem is inherently linear and does not benefit from more complex algorithms like dynamic programming or divide and conquer.
- Detailed breakdown of the approach: This remains the same as the brute force approach because the optimal solution for this problem is to directly apply the rules for each number in the range.
- Proof of optimality: This solution is optimal because it only requires a single pass through the numbers from 1 to `n`, and it must check each number at least once to determine whether it should be "Fizz", "Buzz", "FizzBuzz", or the number itself.
- Why further optimization is impossible: Further optimization is impossible because the problem requires checking each number in the range at least once, making the time complexity $O(n)$.

```cpp
vector<string> fizzBuzz(int n) {
    vector<string> result;
    for (int i = 1; i <= n; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            result.push_back("FizzBuzz");
        } else if (i % 3 == 0) {
            result.push_back("Fizz");
        } else if (i % 5 == 0) {
            result.push_back("Buzz");
        } else {
            result.push_back(to_string(i));
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we are looping through each number from 1 to `n` once.
> - **Space Complexity:** $O(n)$ because we are storing each result in a list.
> - **Optimality proof:** This is the most efficient solution because it only checks each number once and must do so to produce the correct output.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Direct iteration and conditional checks.
- Problem-solving patterns identified: The importance of understanding the problem's requirements and directly applying them.
- Optimization techniques learned: Recognizing that sometimes the most straightforward approach is also the most efficient.
- Similar problems to practice: Other problems that involve iterating over a range and applying specific rules based on conditions.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling the conditions for "Fizz", "Buzz", and "FizzBuzz".
- Edge cases to watch for: Handling the cases where `n` is less than 1 or not an integer.
- Performance pitfalls: Unnecessarily complex solutions that do not improve upon the simple iterative approach.
- Testing considerations: Ensuring that the solution works correctly for a variety of inputs, including edge cases.