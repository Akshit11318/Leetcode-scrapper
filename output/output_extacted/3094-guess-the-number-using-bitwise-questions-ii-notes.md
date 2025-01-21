## Guess the Number Using Bitwise Questions II

**Problem Link:** https://leetcode.com/problems/guess-the-number-using-bitwise-questions-ii/description

**Problem Statement:**
- Input format and constraints: You are given a function `guess` that takes an integer `num` as input and returns a string indicating whether the guessed number is higher or lower than the secret number.
- Expected output format: The goal is to guess the secret number in as few calls to the `guess` function as possible.
- Key requirements and edge cases to consider: The secret number is between 1 and 2^31 - 1, and the `guess` function returns one of three possible strings: "Higher", "Lower", or "Equal".
- Example test cases with explanations: For example, if the secret number is 10, the `guess` function might return "Higher" for inputs 1-9 and "Lower" for inputs 11-2^31 - 1.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One possible approach is to try all numbers from 1 to 2^31 - 1 in sequence, using the `guess` function to determine whether each number is higher or lower than the secret number.
- Step-by-step breakdown of the solution: Start with the number 1 and call the `guess` function. If the result is "Higher", increment the number and repeat. If the result is "Lower", decrement the number and repeat. If the result is "Equal", return the current number.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient because it requires up to 2^31 - 1 calls to the `guess` function.

```cpp
class Solution {
public:
    int guessNumber(int n) {
        for (int i = 1; i <= n; i++) {
            if (guess(i) == 0) {
                return i;
            }
        }
        return -1; // Not found
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{31})$ because in the worst case, we need to try all numbers from 1 to 2^31 - 1.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the current number.
> - **Why these complexities occur:** The time complexity is high because we are trying all numbers in sequence, and the space complexity is low because we only need to store a single number.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a binary search approach to find the secret number in fewer calls to the `guess` function.
- Detailed breakdown of the approach: Start with the range [1, 2^31 - 1] and repeatedly divide the range in half. Call the `guess` function with the midpoint of the range. If the result is "Higher", update the range to [midpoint + 1, upper bound]. If the result is "Lower", update the range to [lower bound, midpoint - 1]. If the result is "Equal", return the midpoint.
- Proof of optimality: This approach is optimal because it reduces the search space by half with each call to the `guess` function, resulting in a logarithmic number of calls.
- Why further optimization is impossible: This approach is optimal because it uses the minimum number of calls to the `guess` function required to find the secret number.

```cpp
class Solution {
public:
    int guessNumber(int n) {
        int low = 1;
        int high = n;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            int result = guess(mid);
            if (result == 0) {
                return mid;
            } else if (result < 0) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return -1; // Not found
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log 2^{31}) = O(31)$ because we divide the search space in half with each call to the `guess` function.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the current range.
> - **Optimality proof:** The time complexity is optimal because we are using a binary search approach, which is the most efficient way to find an element in a sorted range.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search and divide-and-conquer approaches.
- Problem-solving patterns identified: Using a binary search approach to find an element in a sorted range.
- Optimization techniques learned: Reducing the search space by dividing it in half with each iteration.
- Similar problems to practice: Other problems that involve finding an element in a sorted range, such as finding the first occurrence of a number in a sorted array.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the search range correctly or not handling the base case correctly.
- Edge cases to watch for: Handling the case where the secret number is at the boundary of the search range.
- Performance pitfalls: Using a brute-force approach instead of a binary search approach.
- Testing considerations: Testing the solution with different secret numbers and ranges to ensure it works correctly.