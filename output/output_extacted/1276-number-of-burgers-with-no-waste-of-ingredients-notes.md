## Number of Burgers with No Waste of Ingredients
**Problem Link:** https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/description

**Problem Statement:**
- Input: Two integers `tomatoSlices` and `cheeseSlices` representing the number of tomato slices and cheese slices available.
- Constraints: Both `tomatoSlices` and `cheeseSlices` are non-negative integers.
- Expected Output: The number of burgers that can be made with no waste of ingredients.
- Key Requirements: Each burger requires exactly 2 tomato slices and 1 cheese slice.
- Edge Cases: When there are not enough tomato slices or cheese slices to make any burgers.

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible combinations of burgers that can be made and check if there's any waste of ingredients.
- Step-by-step breakdown:
  1. Start from 0 burgers and incrementally try to make more burgers until we run out of either tomato slices or cheese slices.
  2. For each number of burgers, calculate the remaining tomato slices and cheese slices after making those burgers.
  3. If we find a scenario where there's no waste of ingredients (i.e., the remaining slices are exactly 0), return the number of burgers made in that scenario.

```cpp
int numOfBurgers(int tomatoSlices, int cheeseSlices) {
    for (int burgers = 0; burgers <= cheeseSlices; burgers++) {
        int remainingTomato = tomatoSlices - burgers * 2;
        if (remainingTomato == cheeseSlices - burgers) {
            return burgers;
        }
    }
    return -1; // No valid solution
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of cheese slices. This is because we potentially iterate over all possible numbers of burgers that can be made with the given cheese slices.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the variables.
> - **Why these complexities occur:** The iteration over possible numbers of burgers directly influences the time complexity. The space complexity is constant because we don't allocate any additional space that scales with input size.

### Optimal Approach (Required)
**Explanation:**
- Key insight: The problem can be solved using a simple mathematical equation based on the constraints given.
- Detailed breakdown: Let $x$ be the number of burgers with 2 slices of tomato and 1 slice of cheese, and $y$ be the number of burgers with 1 slice of tomato and 1 slice of cheese. The total number of tomato slices used is $2x + y$, and the total number of cheese slices used is $x + y$. Given that we have `tomatoSlices` tomato slices and `cheeseSlices` cheese slices, we can set up the following equations:
  1. $2x + y = tomatoSlices$
  2. $x + y = cheeseSlices$
- Solving these equations simultaneously will give us the values of $x$ and $y$. However, since we are only interested in the number of burgers with no waste of ingredients, and each burger must have 2 tomato slices and 1 cheese slice, the equation simplifies to finding $x$ such that $2x \leq tomatoSlices$ and $x \leq cheeseSlices$. The maximum $x$ that satisfies both conditions gives the number of burgers with no waste.

```cpp
int numOfBurgers(int tomatoSlices, int cheeseSlices) {
    if (tomatoSlices < 2 * cheeseSlices) return -1; // Not enough tomato slices
    int x = (tomatoSlices - cheeseSlices) / 2;
    if (x < 0 || x > cheeseSlices) return -1; // No valid solution
    return x;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, as we perform a constant number of operations regardless of the input size.
> - **Space Complexity:** $O(1)$, for the same reason as above.
> - **Optimality proof:** This solution is optimal because it directly calculates the result based on the given constraints without iterating over all possibilities, thus minimizing the time complexity to a constant.

### Final Notes

**Learning Points:**
- The importance of identifying key insights that simplify the problem.
- How to apply mathematical reasoning to solve problems more efficiently.
- The difference between brute force and optimal solutions in terms of time and space complexity.

**Mistakes to Avoid:**
- Not considering the constraints of the problem thoroughly.
- Failing to identify a simpler, more efficient solution.
- Not validating the inputs and edge cases properly.