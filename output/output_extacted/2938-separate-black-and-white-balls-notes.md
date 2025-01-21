## Separate the Digit 1
**Problem Link:** https://leetcode.com/problems/separate-black-and-white-balls/description

**Problem Statement:**
- Input format and constraints: Given a number of white and black balls, return the number of ways to order them such that no two black balls are adjacent.
- Expected output format: Integer value representing the number of ways.
- Key requirements and edge cases to consider: The number of black and white balls, and the constraint that no two black balls can be adjacent.
- Example test cases with explanations:
  - Input: `n = 3, k = 2`
  - Output: `6`
  - Explanation: The six ways to order the balls are `BBW`, `BWB`, `WBB`, `BBWW`, `BWBW`, `WBBW`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all permutations of the balls and count the ones where no two black balls are adjacent.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the balls.
  2. For each permutation, check if any two black balls are adjacent.
  3. If not, increment the count.
- Why this approach comes to mind first: It's a straightforward way to solve the problem, but it's not efficient.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int countWays(int n, int k) {
    vector<char> balls(n, 'W');
    for (int i = 0; i < k; i++) {
        balls[i] = 'B';
    }

    int count = 0;
    do {
        bool valid = true;
        for (int i = 0; i < n - 1; i++) {
            if (balls[i] == 'B' && balls[i + 1] == 'B') {
                valid = false;
                break;
            }
        }
        if (valid) {
            count++;
        }
    } while (next_permutation(balls.begin(), balls.end()));

    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the total number of balls. This is because we're generating all permutations of the balls.
> - **Space Complexity:** $O(n)$, where $n$ is the total number of balls. This is because we're storing the balls in a vector.
> - **Why these complexities occur:** The brute force approach generates all permutations of the balls, which has a time complexity of $O(n!)$.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use combinatorics to solve the problem. Specifically, we can use the concept of "stars and bars" to count the number of ways to arrange the black balls among the white balls.
- Detailed breakdown of the approach:
  1. Calculate the number of ways to choose $k$ positions for the black balls among the $n - k + 1$ positions (including the ends and between the white balls).
  2. The number of ways to arrange the black balls is equal to the number of ways to choose these positions.
- Proof of optimality: This approach is optimal because it avoids generating all permutations of the balls, which has a high time complexity.

```cpp
#include <iostream>

using namespace std;

int countWays(int n, int k) {
    int result = 1;
    for (int i = 1; i <= k; i++) {
        result = result * (n - k + 1 - i + 1) / i;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k)$, where $k$ is the number of black balls. This is because we're using a simple loop to calculate the result.
> - **Space Complexity:** $O(1)$, because we're only using a constant amount of space.
> - **Optimality proof:** This approach is optimal because it has a much lower time complexity than the brute force approach, and it avoids generating all permutations of the balls.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Combinatorics, stars and bars.
- Problem-solving patterns identified: Using combinatorics to solve problems involving arrangements.
- Optimization techniques learned: Avoiding brute force approaches and using combinatorial formulas instead.

**Mistakes to Avoid:**
- Common implementation errors: Not considering the ends and between the white balls as positions for the black balls.
- Edge cases to watch for: When $k = 0$ or $k = n$, the problem becomes trivial.
- Performance pitfalls: Using brute force approaches for large inputs.
- Testing considerations: Test the function with different inputs, including edge cases.