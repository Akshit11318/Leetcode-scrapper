## Beautiful Arrangement

**Problem Link:** https://leetcode.com/problems/beautiful-arrangement/description

**Problem Statement:**
- Input format: An integer `n` representing the number of positions to fill.
- Constraints: `1 <= n <= 15`.
- Expected output format: The number of beautiful arrangements that can be made.
- Key requirements: A beautiful arrangement is one where for every `i`, either `i` is divisible by the number at position `i`, or the number at position `i` is divisible by `i`.
- Example test cases:
  - For `n = 3`, the beautiful arrangements are `[1, 2, 3]`, `[1, 3, 2]`, `[2, 1, 3]`, `[2, 3, 1]`, `[3, 1, 2]`, and `[3, 2, 1]`. So, the output should be `3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To generate all permutations of numbers from `1` to `n` and check each permutation to see if it satisfies the condition for a beautiful arrangement.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of numbers from `1` to `n`.
  2. For each permutation, check if for every `i`, either `i` is divisible by the number at position `i`, or the number at position `i` is divisible by `i`.
  3. Count the number of permutations that satisfy the condition.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int countArrangement(int n) {
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        nums[i] = i + 1;
    }
    int count = 0;
    
    do {
        bool valid = true;
        for (int i = 0; i < n; i++) {
            if (nums[i] % (i + 1) != 0 && (i + 1) % nums[i] != 0) {
                valid = false;
                break;
            }
        }
        if (valid) {
            count++;
        }
    } while (next_permutation(nums.begin(), nums.end()));
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, because we generate all permutations of `n` numbers, and checking each permutation takes $O(n)$ time.
> - **Space Complexity:** $O(n)$, for storing the permutation.
> - **Why these complexities occur:** The brute force approach involves generating all possible permutations and checking each one, leading to exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: To use backtracking to efficiently explore the search space of possible arrangements, rather than generating all permutations.
- Detailed breakdown of the approach:
  1. Initialize an empty vector to represent the current arrangement.
  2. Use a recursive function to try placing each number from `1` to `n` in the current position.
  3. Before placing a number, check if it satisfies the condition for a beautiful arrangement at the current position.
  4. If it does, place the number and recursively try to fill the rest of the positions.
  5. If a valid arrangement is found, increment the count.
  6. Backtrack by removing the last placed number and trying the next possible number.

```cpp
#include <iostream>
#include <vector>

using namespace std;

int countArrangement(int n) {
    vector<bool> visited(n + 1, false);
    int count = 0;
    
    function<void(int)> backtrack = [&](int pos) {
        if (pos > n) {
            count++;
            return;
        }
        for (int i = 1; i <= n; i++) {
            if (!visited[i] && (i % pos == 0 || pos % i == 0)) {
                visited[i] = true;
                backtrack(pos + 1);
                visited[i] = false;
            }
        }
    };
    
    backtrack(1);
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$ in the worst case, but the backtracking approach prunes the search space more efficiently than generating all permutations.
> - **Space Complexity:** $O(n)$, for the recursion stack and the visited array.
> - **Optimality proof:** This approach is optimal because it explores the search space in a way that minimizes the number of invalid arrangements that need to be checked, without missing any valid arrangements.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Backtracking, recursion, and pruning the search space.
- Problem-solving patterns identified: Using a recursive function to explore a large search space efficiently.
- Optimization techniques learned: Pruning the search space by checking the condition for a beautiful arrangement before recursively exploring further.
- Similar problems to practice: Other problems involving backtracking and recursion, such as the N-Queens problem.

**Mistakes to Avoid:**
- Common implementation errors: Failing to reset the visited state after backtracking, or not checking the condition for a beautiful arrangement correctly.
- Edge cases to watch for: Handling the base case of the recursion correctly, and ensuring that the backtracking process explores all possible arrangements.
- Performance pitfalls: Using an inefficient data structure to store the visited state, or not pruning the search space effectively.
- Testing considerations: Thoroughly testing the function with different inputs, including edge cases, to ensure that it produces the correct output.