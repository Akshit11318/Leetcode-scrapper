## Rearrange Array to Maximize Prefix Score
**Problem Link:** https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Output: The maximum possible prefix score that can be achieved by rearranging the elements in `nums`.
- Key Requirements:
  - The prefix score of an array is the number of positive prefixes.
  - A prefix is considered positive if the sum of its elements is positive.
- Edge Cases:
  - Empty array: The prefix score is 0.
  - Array with a single element: The prefix score is 1 if the element is positive, 0 otherwise.

**Example Test Cases:**
- Input: `nums = [2,3,1,-6,2,-3,3,2]`
  - Output: 6
  - Explanation: The optimal arrangement is `[2,3,1,2,3,2,-6,-3]`, which has 6 positive prefixes.
- Input: `nums = [1,2,3,4,5]`
  - Output: 5
  - Explanation: The optimal arrangement is the original array, which has 5 positive prefixes.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible permutations of the input array and calculate the prefix score for each permutation.
- Step-by-step breakdown:
  1. Generate all permutations of the input array.
  2. For each permutation, calculate the prefix score by iterating over the array and checking if the sum of the prefix is positive.
  3. Keep track of the maximum prefix score found so far.
- Why this approach comes to mind first: It is a straightforward approach that guarantees finding the optimal solution, but it is inefficient due to the large number of permutations.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int maxScore(std::vector<int>& nums) {
    int n = nums.size();
    int maxScore = 0;
    
    // Generate all permutations
    std::sort(nums.begin(), nums.end());
    do {
        int score = 0;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            if (sum > 0) {
                score++;
            }
        }
        maxScore = std::max(maxScore, score);
    } while (std::next_permutation(nums.begin(), nums.end()));
    
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n)$, where $n$ is the size of the input array. This is because there are $n!$ permutations, and for each permutation, we iterate over the array to calculate the prefix score.
> - **Space Complexity:** $O(1)$, excluding the space required for the input array. This is because we only use a constant amount of space to store the maximum score and other variables.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the large number of permutations, and the space complexity is low because we only use a constant amount of space.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: We can sort the array in descending order and then iterate over the array to calculate the prefix score. This approach works because we want to maximize the number of positive prefixes, and sorting the array in descending order ensures that we have the largest possible sum at each prefix.
- Detailed breakdown:
  1. Sort the input array in descending order.
  2. Initialize the prefix score and the sum of the prefix.
  3. Iterate over the sorted array, adding each element to the sum and incrementing the prefix score if the sum is positive.
- Why this approach is optimal: It is optimal because it guarantees finding the maximum possible prefix score by maximizing the sum at each prefix.

```cpp
int maxScore(std::vector<int>& nums) {
    int n = nums.size();
    int score = 0;
    int sum = 0;
    
    // Sort the array in descending order
    std::sort(nums.rbegin(), nums.rend());
    
    // Calculate the prefix score
    for (int i = 0; i < n; i++) {
        sum += nums[i];
        if (sum > 0) {
            score++;
        }
    }
    
    return score;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the size of the input array. This is because we sort the array using a comparison-based sorting algorithm, which has a time complexity of $O(n \log n)$.
> - **Space Complexity:** $O(1)$, excluding the space required for the input array. This is because we only use a constant amount of space to store the prefix score and the sum of the prefix.
> - **Optimality proof:** This approach is optimal because it guarantees finding the maximum possible prefix score by maximizing the sum at each prefix. The sorting step ensures that we have the largest possible sum at each prefix, and the iteration over the sorted array ensures that we count the maximum number of positive prefixes.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, prefix sum calculation, and optimization techniques.
- Problem-solving patterns identified: Maximizing a score by optimizing the sum at each prefix.
- Optimization techniques learned: Sorting the array in descending order to maximize the sum at each prefix.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input array.
- Edge cases to watch for: Empty array, array with a single element, and arrays with negative numbers.
- Performance pitfalls: Using an inefficient sorting algorithm or iterating over the array multiple times.
- Testing considerations: Test the function with different input arrays, including edge cases and large inputs.