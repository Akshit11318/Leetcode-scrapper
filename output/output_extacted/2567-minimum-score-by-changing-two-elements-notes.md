## Minimum Score by Changing Two Elements
**Problem Link:** https://leetcode.com/problems/minimum-score-by-changing-two-elements/description

**Problem Statement:**
- Input format: You are given an integer array `nums` of length `n`.
- Constraints: `3 <= n <= 10^5`, `1 <= nums[i] <= 10^5`.
- Expected output format: The minimum possible score after changing at most two elements.
- Key requirements and edge cases to consider: The score is calculated as the sum of all elements, except for the maximum and minimum values which are not included in the sum. You can change at most two elements in the array to achieve the minimum score.
- Example test cases with explanations:
    - For `nums = [1, 3, 5]`, the minimum score is `3` after changing the first element to `5` and the last element to `1`.
    - For `nums = [1, 2, 3, 4, 5]`, the minimum score is `6` without changing any elements.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible combinations of changing at most two elements and calculate the score for each combination.
- Step-by-step breakdown of the solution:
    1. Generate all possible combinations of changing at most two elements.
    2. For each combination, calculate the score by excluding the maximum and minimum values.
    3. Keep track of the minimum score found so far.
- Why this approach comes to mind first: It's a straightforward approach that considers all possible scenarios.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int minScore(std::vector<int>& nums) {
    int n = nums.size();
    int min_score = INT_MAX;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            std::vector<int> temp = nums;
            if (i != j) {
                temp[i] = 1;
                temp[j] = 1;
            } else {
                temp[i] = 1;
            }
            std::sort(temp.begin(), temp.end());
            int score = 0;
            for (int k = 1; k < n - 1; k++) {
                score += temp[k];
            }
            min_score = std::min(min_score, score);
        }
    }
    return min_score;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3 \log n)$, where $n$ is the length of the input array. This is because we have two nested loops to generate all possible combinations, and we sort the array for each combination.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we create a temporary array for each combination.
> - **Why these complexities occur:** The time complexity is high due to the nested loops and sorting operation, while the space complexity is moderate due to the temporary array creation.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The score is calculated by excluding the maximum and minimum values. Therefore, we can minimize the score by changing the maximum and/or minimum values to the smallest possible values.
- Detailed breakdown of the approach:
    1. Find the maximum and minimum values in the array.
    2. Calculate the score without changing any elements.
    3. Calculate the score by changing the maximum value to the smallest possible value.
    4. Calculate the score by changing the minimum value to the smallest possible value.
    5. Calculate the score by changing both the maximum and minimum values to the smallest possible values.
    6. Return the minimum score found among the above calculations.
- Proof of optimality: This approach is optimal because it considers all possible scenarios of changing at most two elements and calculates the score accordingly.

```cpp
int minScore(std::vector<int>& nums) {
    int n = nums.size();
    std::sort(nums.begin(), nums.end());
    int score = 0;
    for (int i = 1; i < n - 1; i++) {
        score += nums[i];
    }
    int min_score = score;
    // Change the maximum value
    int score_max = 0;
    for (int i = 1; i < n; i++) {
        score_max += nums[i];
    }
    min_score = std::min(min_score, score_max);
    // Change the minimum value
    int score_min = 0;
    for (int i = 0; i < n - 1; i++) {
        score_min += nums[i];
    }
    min_score = std::min(min_score, score_min);
    // Change both the maximum and minimum values
    int score_both = 0;
    for (int i = 1; i < n - 1; i++) {
        score_both += nums[i];
    }
    min_score = std::min(min_score, score_both);
    return min_score;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the length of the input array. This is because we sort the array once.
> - **Space Complexity:** $O(1)$, where $n$ is the length of the input array. This is because we only use a constant amount of space to store the scores.
> - **Optimality proof:** This approach is optimal because it considers all possible scenarios of changing at most two elements and calculates the score accordingly, resulting in the minimum possible score.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, iteration, and comparison.
- Problem-solving patterns identified: Identifying the key insight that leads to the optimal solution, and using a systematic approach to calculate the score.
- Optimization techniques learned: Using a single pass to calculate the score, and minimizing the number of comparisons.
- Similar problems to practice: Problems that involve finding the minimum or maximum value in an array, or problems that require a systematic approach to calculate a score.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty array or an array with a single element.
- Edge cases to watch for: Arrays with duplicate maximum or minimum values.
- Performance pitfalls: Using a brute force approach or an approach with a high time complexity.
- Testing considerations: Testing the function with different input arrays, including edge cases and large arrays.