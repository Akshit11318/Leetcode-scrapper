## Number of Self-Divisible Permutations
**Problem Link:** https://leetcode.com/problems/number-of-self-divisible-permutations/description

**Problem Statement:**
- Input: A positive integer `n`.
- Output: The number of permutations of numbers from 1 to `n` that are self-divisible, meaning for each permutation, every prefix of the permutation is divisible by the number of digits in the prefix.
- Key requirements and edge cases to consider: Handling cases where `n` is small (e.g., 1, 2) and understanding what constitutes a self-divisible permutation.
- Example test cases: For `n = 1`, there's only 1 permutation: `[1]`, which is self-divisible. For `n = 2`, permutations are `[1,2]` and `[2,1]`, both of which are self-divisible.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all permutations of numbers from 1 to `n`, then check each permutation to see if it's self-divisible.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of numbers from 1 to `n`.
  2. For each permutation, iterate through its prefixes.
  3. For each prefix, check if the number formed by the prefix is divisible by the length of the prefix.
  4. If all prefixes pass this check, the permutation is self-divisible.
- Why this approach comes to mind first: It directly addresses the problem statement without requiring optimization techniques.

```cpp
#include <iostream>
#include <vector>

using namespace std;

void backtrack(vector<int>& nums, int start, vector<vector<int>>& permutations) {
    if (start == nums.size()) {
        permutations.push_back(nums);
        return;
    }
    for (int i = start; i < nums.size(); i++) {
        swap(nums[start], nums[i]);
        backtrack(nums, start + 1, permutations);
        swap(nums[start], nums[i]);
    }
}

bool isSelfDivisible(const vector<int>& permutation) {
    int num = 0;
    for (int i = 0; i < permutation.size(); i++) {
        num = num * 10 + permutation[i];
        if (num % (i + 1) != 0) {
            return false;
        }
    }
    return true;
}

int numPermsDISequence(int n) {
    vector<int> nums;
    for (int i = 1; i <= n; i++) {
        nums.push_back(i);
    }
    vector<vector<int>> permutations;
    backtrack(nums, 0, permutations);
    int count = 0;
    for (const auto& permutation : permutations) {
        if (isSelfDivisible(permutation)) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n)$, where $n!$ is the time to generate all permutations and $n$ is the time to check each permutation.
> - **Space Complexity:** $O(n! \cdot n)$, for storing all permutations.
> - **Why these complexities occur:** Generating all permutations and then checking each one for the self-divisible property results in these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all permutations and then checking, use a depth-first search (DFS) approach that builds the permutation while checking for the self-divisible condition. This allows for pruning branches that will not lead to a self-divisible permutation.
- Detailed breakdown of the approach:
  1. Start with an empty permutation and the set of numbers from 1 to `n`.
  2. At each step, try to add a number to the current permutation if doing so would keep the permutation self-divisible.
  3. Use DFS to explore all possible permutations that can be formed under this constraint.
- Proof of optimality: This approach ensures that only valid self-divisible permutations are counted, avoiding the unnecessary generation and checking of invalid permutations.

```cpp
int numPermsDISequence(int n) {
    int count = 0;
    vector<int> permutation;
    vector<bool> used(n + 1, false);
    function<void(int)> dfs = [&](int depth) {
        if (depth == n) {
            count++;
            return;
        }
        int num = 0;
        for (int i = 1; i <= depth; i++) {
            num = num * 10 + permutation[i - 1];
            if (num % i != 0) {
                return;
            }
        }
        for (int i = 1; i <= n; i++) {
            if (!used[i]) {
                permutation.push_back(i);
                used[i] = true;
                dfs(depth + 1);
                permutation.pop_back();
                used[i] = false;
            }
        }
    };
    dfs(0);
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, as in the worst case, we might still explore all permutations, but with the benefit of pruning.
> - **Space Complexity:** $O(n)$, for the recursion stack and the permutation being built.
> - **Optimality proof:** This approach is optimal because it directly constructs valid permutations without generating all possible permutations, thus avoiding unnecessary work.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search, permutation generation, and pruning based on problem constraints.
- Problem-solving patterns identified: Constructing solutions incrementally and using constraints to prune the search space.
- Optimization techniques learned: Avoiding unnecessary computation by checking for validity at each step of the construction process.
- Similar problems to practice: Other permutation and sequence problems with constraints that can be used to prune the search space.

**Mistakes to Avoid:**
- Common implementation errors: Not properly handling the base case of recursion or not correctly updating the search space.
- Edge cases to watch for: Small values of `n` and ensuring that the algorithm correctly handles these cases without running into unnecessary complexity.
- Performance pitfalls: Failing to prune the search space effectively, leading to exploring too many invalid permutations.
- Testing considerations: Ensure that the algorithm is tested with a variety of inputs, including small and large values of `n`, to verify its correctness and performance.