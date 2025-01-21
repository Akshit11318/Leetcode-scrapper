## Maximize Score of Numbers in Ranges

**Problem Link:** https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/description

**Problem Statement:**
- Given a list of integers `nums` and a list of ranges `ranges`, the goal is to find the maximum score that can be achieved by selecting numbers from `nums` such that each number falls within at least one range in `ranges`. The score is the sum of the selected numbers.
- Input format: `nums` is a list of integers and `ranges` is a list of pairs, where each pair represents a range.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= ranges.length <= 10^5`, `1 <= nums[i] <= 10^5`, `1 <= ranges[i][0] <= 10^5`, and `1 <= ranges[i][1] <= 10^5`.
- Expected output format: The maximum score that can be achieved.
- Key requirements and edge cases to consider:
  - Handling duplicate numbers in `nums`.
  - Handling overlapping ranges in `ranges`.
  - Handling cases where no numbers in `nums` fall within any range in `ranges`.
- Example test cases with explanations:
  - For `nums = [1, 2, 3]` and `ranges = [[1, 3]]`, the maximum score is `6` because we can select all numbers.
  - For `nums = [1, 2, 3]` and `ranges = [[1, 2]]`, the maximum score is `3` because we can only select `1` and `2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of numbers and check if each number falls within at least one range.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of `nums`.
  2. For each subset, check if each number falls within at least one range in `ranges`.
  3. If a subset satisfies the condition, calculate its score by summing the numbers in the subset.
  4. Keep track of the maximum score found.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int maxScore(std::vector<int>& nums, std::vector<std::vector<int>>& ranges) {
    int maxScore = 0;
    int n = nums.size();
    
    // Generate all possible subsets
    for (int mask = 0; mask < (1 << n); mask++) {
        int score = 0;
        bool validSubset = true;
        
        // Check each number in the subset
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                bool inRange = false;
                
                // Check if the number falls within any range
                for (const auto& range : ranges) {
                    if (nums[i] >= range[0] && nums[i] <= range[1]) {
                        inRange = true;
                        break;
                    }
                }
                
                if (!inRange) {
                    validSubset = false;
                    break;
                }
                
                score += nums[i];
            }
        }
        
        // Update the maximum score if the subset is valid
        if (validSubset) {
            maxScore = std::max(maxScore, score);
        }
    }
    
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot m)$, where $n$ is the number of elements in `nums` and $m$ is the number of ranges. This is because we generate all possible subsets of `nums` and for each subset, we check each number against all ranges.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input, because we only use a constant amount of space to store the maximum score and other variables.
> - **Why these complexities occur:** The exponential time complexity comes from generating all possible subsets of `nums`, and the linear factors come from checking each number against all ranges.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Sort `nums` and `ranges` based on their values and start/end points, respectively. Then, use a greedy approach to select numbers that fall within the most ranges.
- Detailed breakdown of the approach:
  1. Sort `nums` in ascending order.
  2. Sort `ranges` based on their end points in ascending order.
  3. Initialize an empty set to store the selected numbers.
  4. Iterate over `ranges`. For each range, find the numbers in `nums` that fall within the range and have not been selected yet.
  5. Select the numbers that fall within the most ranges and add them to the set.
  6. Calculate the score by summing the selected numbers.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

int maxScore(std::vector<int>& nums, std::vector<std::vector<int>>& ranges) {
    std::sort(nums.begin(), nums.end());
    std::sort(ranges.begin(), ranges.end(), [](const auto& a, const auto& b) {
        return a[1] < b[1];
    });
    
    int maxScore = 0;
    std::set<int> selected;
    
    for (const auto& range : ranges) {
        int count = 0;
        int sum = 0;
        
        for (int num : nums) {
            if (num >= range[0] && num <= range[1] && selected.find(num) == selected.end()) {
                count++;
                sum += num;
            }
        }
        
        if (count > 0) {
            maxScore += sum;
            for (int num : nums) {
                if (num >= range[0] && num <= range[1] && selected.find(num) == selected.end()) {
                    selected.insert(num);
                }
            }
        }
    }
    
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + m \log m + n \cdot m)$, where $n$ is the number of elements in `nums` and $m$ is the number of ranges. This is because we sort `nums` and `ranges`, and then iterate over `ranges` and `nums`.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in `nums`, because we use a set to store the selected numbers.
> - **Optimality proof:** This solution is optimal because it uses a greedy approach to select the numbers that fall within the most ranges, which maximizes the score.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, greedy approach, and set operations.
- Problem-solving patterns identified: Using a greedy approach to solve optimization problems.
- Optimization techniques learned: Sorting and using a set to store selected numbers.
- Similar problems to practice: Other optimization problems that involve sorting and greedy approaches.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for duplicate numbers in `nums` or overlapping ranges in `ranges`.
- Edge cases to watch for: Handling cases where no numbers in `nums` fall within any range in `ranges`.
- Performance pitfalls: Using an inefficient algorithm that has a high time complexity.
- Testing considerations: Testing the solution with different inputs and edge cases to ensure its correctness and efficiency.