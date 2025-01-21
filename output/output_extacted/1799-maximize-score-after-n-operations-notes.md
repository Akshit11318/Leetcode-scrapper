## Maximize Score After N Operations
**Problem Link:** https://leetcode.com/problems/maximize-score-after-n-operations/description

**Problem Statement:**
- Input: `int n`, an integer representing the number of operations to perform, and `vector<int>& nums`, a vector of integers representing the scores.
- Constraints: `1 <= n <= 10^4`, `1 <= nums.size() <= 12`.
- Expected Output: The maximum score that can be obtained after `n` operations.
- Key Requirements:
  - The `n` operations are choosing two distinct numbers from `nums`, multiplying them, and adding the product to the score.
  - The goal is to maximize the score after `n` such operations.
- Example Test Cases:
  - `n = 3`, `nums = [1, 2, 3]`: The maximum score can be obtained by choosing `1` and `2`, then `1` and `3`, and finally `2` and `3`, resulting in a score of `1*2 + 1*3 + 2*3 = 11`.
  - `n = 5`, `nums = [1, 2, 3, 4, 5]`: The maximum score involves choosing pairs that maximize the product in each step.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of pairs from `nums` for `n` operations.
- This approach involves generating all permutations of choosing two numbers from `nums` for `n` times and calculating the score for each permutation.
- This comes to mind first because it guarantees exploring all possible operations, but it's inefficient due to the large number of combinations.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int maximizeScoreAfterNOperations(int n, vector<int>& nums) {
    int maxScore = 0;
    vector<bool> visited(nums.size(), false);
    vector<int> currentNums;
    
    function<void(int, int)> backtrack = [&](int step, int score) {
        if (step == n) {
            maxScore = max(maxScore, score);
            return;
        }
        
        for (int i = 0; i < nums.size(); ++i) {
            if (visited[i]) continue;
            for (int j = i + 1; j < nums.size(); ++j) {
                if (visited[j]) continue;
                visited[i] = true;
                visited[j] = true;
                score += nums[i] * nums[j];
                backtrack(step + 1, score);
                score -= nums[i] * nums[j];
                visited[i] = false;
                visited[j] = false;
            }
        }
    };
    
    backtrack(0, 0);
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n^2)$, where $n$ is the number of operations and also the number of elements in `nums` in the worst case. This is because for each operation, we potentially explore all pairs of numbers, leading to exponential growth.
> - **Space Complexity:** $O(n)$, due to the recursive call stack and the space needed to store the visited status of each number.
> - **Why these complexities occur:** The brute force approach explores all possible combinations of operations, leading to an exponential number of steps. The space complexity is linear due to the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to recognize that the order of choosing the pairs does not matter; what matters is the set of pairs chosen.
- This problem can be modeled as a graph problem where each number in `nums` is a node, and each edge represents a potential pair. The goal is to find the maximum-weight matching in this graph, where the weight of each edge is the product of the two numbers it connects.
- However, directly applying graph algorithms may not be straightforward due to the complexity of calculating all possible pair products and the need to select `n` pairs.
- A more practical approach involves using bit manipulation to represent all possible subsets of `nums` and then iterating through these subsets to find the optimal set of pairs that maximizes the score.
- Given the constraint that `1 <= nums.size() <= 12`, we can explore all possible subsets of `nums` efficiently.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int maximizeScoreAfterNOperations(int n, vector<int>& nums) {
    int maxScore = 0;
    int totalSubsets = 1 << nums.size(); // 2^nums.size()
    
    for (int subset = 1; subset < totalSubsets; ++subset) {
        int currentScore = 0;
        vector<int> currentSubset;
        
        for (int i = 0; i < nums.size(); ++i) {
            if ((subset & (1 << i)) != 0) {
                currentSubset.push_back(nums[i]);
            }
        }
        
        if (currentSubset.size() % 2 == 0 && currentSubset.size() / 2 == n) {
            for (int i = 0; i < currentSubset.size(); i += 2) {
                currentScore += currentSubset[i] * currentSubset[i + 1];
            }
            maxScore = max(maxScore, currentScore);
        }
    }
    
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{nums.size()} \cdot nums.size())$, where `nums.size()` is at most 12. This is because we explore all possible subsets of `nums`.
> - **Space Complexity:** $O(nums.size())$, for storing the current subset of numbers.
> - **Optimality proof:** This approach is optimal because it explores all possible subsets of `nums` that could lead to the maximum score after `n` operations, given the constraint on `nums.size()`. It ensures that we consider all potential sets of pairs that could maximize the score.

---

### Final Notes

**Learning Points:**
- The importance of recognizing the problem's structure and applying appropriate algorithms or techniques.
- How to approach problems involving combinatorics and optimization.
- The use of bit manipulation to efficiently explore subsets of a set.

**Mistakes to Avoid:**
- Not considering the constraints of the problem and their implications on the solution's complexity.
- Failing to recognize the problem as an optimization problem that requires exploring all possible solutions.
- Not optimizing the solution for the given constraints, leading to inefficient code.