## Guess the Number Using Bitwise Questions I

**Problem Link:** https://leetcode.com/problems/guess-the-number-using-bitwise-questions-i/description

**Problem Statement:**
- Input: `n` - the number to guess, which is a 32-bit signed integer.
- Output: The number of questions asked to guess the number.
- Key requirements and edge cases to consider: 
    - The number can be any 32-bit signed integer, including negative numbers and zero.
    - We can only ask questions in the form of a bitwise AND operation between our guess and the target number.
- Example test cases with explanations: 
    - For `n = 10`, the output should be 3 because we can ask the following questions: 
        1. Is the number odd? (i.e., `n & 1 == 1`)
        2. Is the number greater than 8? (i.e., `n & 8 == 8`)
        3. Is the number greater than or equal to 10? (i.e., `n & 2 == 2`)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can try all possible numbers from 0 to $2^{31}-1$ and check if each number is the target number by asking a series of bitwise AND questions.
- Step-by-step breakdown of the solution:
    1. Initialize a counter to keep track of the number of questions asked.
    2. Iterate through all possible numbers from 0 to $2^{31}-1$.
    3. For each number, ask a series of bitwise AND questions to check if it is the target number.
    4. If the number is the target number, return the counter value.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient because it requires a large number of questions.

```cpp
class Solution {
public:
    int guessNumber(int n) {
        int count = 0;
        for (int i = 0; i <= n; i++) {
            count++;
            if (i == n) {
                return count;
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the input number. This is because we are iterating through all possible numbers from 0 to $n$.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input number, making it constant.
> - **Why these complexities occur:** The time complexity is linear because we are checking each number individually, and the space complexity is constant because we only use a fixed amount of space to store the counter and the input number.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a binary search approach to find the target number. This is because the target number is a 32-bit signed integer, which means it can be represented using 32 bits. By asking bitwise AND questions, we can effectively perform a binary search on the range of possible numbers.
- Detailed breakdown of the approach:
    1. Initialize the low and high bounds of the search range to 0 and $2^{31}-1$, respectively.
    2. While the low bound is less than or equal to the high bound, calculate the mid point of the search range.
    3. Ask a bitwise AND question to check if the mid point is less than or equal to the target number.
    4. If the mid point is less than or equal to the target number, update the low bound to the mid point + 1. Otherwise, update the high bound to the mid point - 1.
    5. Repeat steps 2-4 until the low bound is greater than the high bound.
    6. The target number is the low bound.
- Proof of optimality: This approach is optimal because it uses the minimum number of questions required to find the target number. The number of questions is equal to the number of bits required to represent the target number, which is 32.

```cpp
class Solution {
public:
    int guessNumber(int n) {
        int count = 0;
        int low = 0;
        int high = n;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            count++;
            if (mid == n) {
                return count;
            } else if (mid < n) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(log n)$, where $n$ is the input number. This is because we are using a binary search approach to find the target number.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input number, making it constant.
> - **Optimality proof:** The time complexity is logarithmic because we are effectively performing a binary search on the range of possible numbers, and the space complexity is constant because we only use a fixed amount of space to store the low and high bounds, the mid point, and the counter.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, bitwise AND operation.
- Problem-solving patterns identified: Using a binary search approach to find a target value in a large range.
- Optimization techniques learned: Reducing the number of questions required to find the target number by using a binary search approach.
- Similar problems to practice: Other problems that involve finding a target value in a large range, such as finding an element in a sorted array.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the low and high bounds correctly, not checking for the base case where the low bound is greater than the high bound.
- Edge cases to watch for: The target number is 0, the target number is $2^{31}-1$, the input number is negative.
- Performance pitfalls: Using a linear search approach instead of a binary search approach, not using bitwise AND questions to reduce the number of questions required.
- Testing considerations: Testing the function with different input values, including edge cases, to ensure that it works correctly.