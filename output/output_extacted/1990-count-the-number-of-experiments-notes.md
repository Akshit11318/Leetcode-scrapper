## Count the Number of Experiments
**Problem Link:** https://leetcode.com/problems/count-the-number-of-experiments/description

**Problem Statement:**
- Input format: An integer `n` representing the number of experiments and an array `experiments` where each element is an array of length `2` containing the `x` and `y` coordinates of a point.
- Constraints: `1 <= n <= 10^5`, `1 <= x, y <= 10^5`.
- Expected output format: The number of distinct experiments.
- Key requirements and edge cases to consider: Counting distinct experiments based on the points' coordinates, handling duplicate points, and optimizing the solution for large inputs.
- Example test cases with explanations:
  - For `n = 3` and `experiments = [[1,2],[2,1],[3,2]]`, the output should be `2` because there are two distinct experiments: `(1,2)` and `(2,1)` or `(3,2)`.
  - For `n = 5` and `experiments = [[1,1],[1,1],[1,1],[1,1],[1,1]]`, the output should be `1` because there is only one distinct experiment.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To count the number of distinct experiments, we can simply iterate through each experiment and compare it with every other experiment to check for duplicates.
- Step-by-step breakdown of the solution:
  1. Initialize a counter for distinct experiments.
  2. Iterate through each experiment.
  3. For each experiment, compare it with every other experiment.
  4. If an experiment is not found to be a duplicate, increment the counter.
- Why this approach comes to mind first: It's a straightforward approach that directly addresses the problem statement.

```cpp
#include <iostream>
#include <vector>

int countExperiments(std::vector<std::vector<int>>& experiments) {
    int distinctCount = 0;
    std::vector<bool> isDuplicate(experiments.size(), false);
    
    for (int i = 0; i < experiments.size(); ++i) {
        if (isDuplicate[i]) continue;
        
        bool foundDuplicate = false;
        for (int j = i + 1; j < experiments.size(); ++j) {
            if (experiments[i][0] == experiments[j][0] && experiments[i][1] == experiments[j][1]) {
                isDuplicate[j] = true;
                foundDuplicate = true;
            }
        }
        
        if (!foundDuplicate) distinctCount++;
    }
    
    return distinctCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of experiments. This is because for each experiment, we potentially compare it with every other experiment.
> - **Space Complexity:** $O(n)$, for storing the `isDuplicate` vector.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the nested loops, making it inefficient for large inputs.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Using a `std::set` to store unique experiments. This allows us to check for duplicates in constant time.
- Detailed breakdown of the approach:
  1. Initialize an empty `std::set` to store unique experiments.
  2. Iterate through each experiment.
  3. For each experiment, insert it into the set. If the experiment is already in the set (i.e., it's a duplicate), the set will not change.
  4. The size of the set at the end represents the number of distinct experiments.
- Proof of optimality: This approach is optimal because it minimizes the time complexity by avoiding unnecessary comparisons.

```cpp
#include <iostream>
#include <vector>
#include <set>

int countExperiments(std::vector<std::vector<int>>& experiments) {
    std::set<std::pair<int, int>> uniqueExperiments;
    
    for (const auto& experiment : experiments) {
        uniqueExperiments.insert({experiment[0], experiment[1]});
    }
    
    return uniqueExperiments.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of experiments. This is because inserting into a set takes constant time on average.
> - **Space Complexity:** $O(n)$, for storing the set of unique experiments.
> - **Optimality proof:** This solution is optimal because it achieves the best possible time complexity for this problem, which is linear with respect to the input size.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using sets for efficient duplicate detection.
- Problem-solving patterns identified: Optimizing solutions by reducing unnecessary comparisons.
- Optimization techniques learned: Leveraging data structures like sets for improved performance.
- Similar problems to practice: Problems involving duplicate detection or counting distinct elements.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases or not validating inputs.
- Edge cases to watch for: Handling empty inputs or inputs with all duplicates.
- Performance pitfalls: Using inefficient algorithms or data structures that lead to high time complexities.
- Testing considerations: Thoroughly testing with various inputs, including edge cases, to ensure correctness and performance.