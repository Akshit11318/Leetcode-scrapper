## Most Profit Assigning Work
**Problem Link:** https://leetcode.com/problems/most-profit-assigning-work/description

**Problem Statement:**
- Input: Two integer arrays `profit` and `difficulty`, where `profit[i]` denotes the profit gained and `difficulty[i]` denotes the difficulty of the `i-th` work. Also, an integer `worker`, representing the worker's ability.
- Output: The maximum possible profit that can be achieved.
- Key requirements and edge cases to consider: 
  - The length of `profit` and `difficulty` arrays will be the same.
  - `1 <= difficulty.length <= 100`.
  - `1 <= difficulty[i], profit[i] <= 10^5`.
  - `1 <= worker <= 10^8`.
- Example test cases with explanations:
  - Given `profit = [1,2,4,5,7,8]`, `difficulty = [7,3,2,2,5,10]`, and `worker = 4`, the maximum profit is `5`.
  - Given `profit = [5]`, `difficulty = [2]`, and `worker = 200`, the maximum profit is `5`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of works and calculate the profit for each combination that the worker can complete.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of the works.
  2. For each subset, calculate the total difficulty and profit.
  3. Check if the worker can complete the works in the subset (total difficulty <= worker).
  4. If the worker can complete the works, update the maximum profit.
- Why this approach comes to mind first: It's a straightforward way to consider all possibilities, but it's inefficient due to the exponential number of subsets.

```cpp
#include <vector>
#include <algorithm>

int maxProfitAssignment(std::vector<int>& profit, std::vector<int>& difficulty, int worker) {
    int maxProfit = 0;
    for (int i = 0; i < profit.size(); i++) {
        if (difficulty[i] <= worker) {
            maxProfit = std::max(maxProfit, profit[i]);
        }
    }
    return maxProfit;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of works. This is because we are scanning the works once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum profit.
> - **Why these complexities occur:** The time complexity is linear because we only need to iterate through the works once, and the space complexity is constant because we only use a fixed amount of space to store the result.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can sort the works by difficulty and then iterate through the sorted works to find the maximum profit that the worker can achieve.
- Detailed breakdown of the approach:
  1. Sort the works by difficulty.
  2. Initialize the maximum profit to 0.
  3. Iterate through the sorted works. For each work, if the worker can complete it, update the maximum profit if the current work's profit is higher.
- Proof of optimality: This approach is optimal because it considers all possible works that the worker can complete and chooses the one with the highest profit.

```cpp
#include <vector>
#include <algorithm>

int maxProfitAssignment(std::vector<int>& profit, std::vector<int>& difficulty, int worker) {
    std::vector<std::pair<int, int>> works;
    for (int i = 0; i < profit.size(); i++) {
        works.push_back({difficulty[i], profit[i]});
    }
    std::sort(works.begin(), works.end());
    int maxProfit = 0;
    for (auto& work : works) {
        if (work.first <= worker) {
            maxProfit = std::max(maxProfit, work.second);
        }
    }
    return maxProfit;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of works. This is because we are sorting the works.
> - **Space Complexity:** $O(n)$, as we are storing the works in a new vector.
> - **Optimality proof:** This approach is optimal because it considers all possible works that the worker can complete and chooses the one with the highest profit, and it does so in the most efficient way possible.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, iteration, and comparison.
- Problem-solving patterns identified: The problem can be solved by iterating through the works and keeping track of the maximum profit.
- Optimization techniques learned: Sorting the works by difficulty allows us to find the maximum profit in a more efficient way.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the worker can complete a work before updating the maximum profit.
- Edge cases to watch for: The worker's ability being less than the difficulty of all works.
- Performance pitfalls: Not sorting the works by difficulty, which would result in a less efficient solution.
- Testing considerations: Test the function with different inputs, including edge cases, to ensure it works correctly.