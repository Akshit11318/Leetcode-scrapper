## Guess Number Higher or Lower
**Problem Link:** https://leetcode.com/problems/guess-number-higher-or-lower/description

**Problem Statement:**
- Input: `n`, an integer representing the number to guess, and `pick`, a function that takes a guess and returns `-1` if the guess is too high, `1` if the guess is too low, and `0` if the guess is correct.
- Constraints: `1 <= n <= 2^31 - 1`
- Expected output: The number `n` that satisfies the conditions.
- Key requirements: Find `n` in as few guesses as possible.
- Example test cases:
  - `n = 6`, `pick(2)` returns `-1`, `pick(3)` returns `1`, `pick(5)` returns `-1`, `pick(6)` returns `0`.
  - `n = 1`, `pick(1)` returns `0`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try every possible number from `1` to `2^31 - 1`.
- Step-by-step breakdown:
  1. Initialize a variable `guess` to `1`.
  2. While `guess` is less than or equal to `2^31 - 1`, call `pick(guess)` and check the return value.
  3. If `pick(guess)` returns `0`, return `guess`.
  4. If `pick(guess)` returns `-1`, decrement `guess` and try again.
  5. If `pick(guess)` returns `1`, increment `guess` and try again.
- Why this approach comes to mind first: It's a simple, straightforward approach that guarantees finding the correct number.

```cpp
int guessNumber(int n) {
    for (int i = 1; i <= n; i++) {
        if (pick(i) == 0) {
            return i;
        }
    }
    return -1; // This line should never be reached
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, because in the worst case, we might have to try every number up to `n`.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store our guess.
> - **Why these complexities occur:** The brute force approach tries every possible number, resulting in linear time complexity. The space complexity is constant because we only use a fixed amount of space to store our current guess.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: We can use a binary search approach to find the number in fewer guesses.
- Detailed breakdown:
  1. Initialize two variables, `low` and `high`, to `1` and `n`, respectively.
  2. While `low` is less than or equal to `high`, calculate the midpoint `mid`.
  3. Call `pick(mid)` and check the return value.
  4. If `pick(mid)` returns `0`, return `mid`.
  5. If `pick(mid)` returns `-1`, update `high` to `mid - 1`.
  6. If `pick(mid)` returns `1`, update `low` to `mid + 1`.
- Proof of optimality: Binary search has a time complexity of $O(\log n)$, which is the best possible time complexity for this problem.

```cpp
int guessNumber(int n) {
    int low = 1;
    int high = n;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        int res = pick(mid);
        if (res == 0) {
            return mid;
        } else if (res == -1) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return -1; // This line should never be reached
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, because we divide the search space in half with each guess.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store our current guess and the bounds of the search space.
> - **Optimality proof:** The binary search approach has a time complexity of $O(\log n)$, which is the best possible time complexity for this problem. This is because we are essentially finding the correct number in a sorted list, and binary search is the most efficient algorithm for this task.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, iterative approach.
- Problem-solving patterns identified: Using a more efficient algorithm to solve a problem.
- Optimization techniques learned: Reducing the number of guesses by using a more efficient search strategy.
- Similar problems to practice: Other problems that involve searching for a target value in a sorted list.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the search bounds correctly.
- Edge cases to watch for: The case where `n` is `1`.
- Performance pitfalls: Using a brute force approach instead of a more efficient algorithm.
- Testing considerations: Make sure to test the function with different values of `n` to ensure it works correctly.