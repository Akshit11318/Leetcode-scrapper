## Apply Operations to Maximize Score
**Problem Link:** https://leetcode.com/problems/apply-operations-to-maximize-score/description

**Problem Statement:**
- Input: An integer array `nums` of size `n`, and an integer `k`.
- Constraints: `1 <= n <= 10^5`, `1 <= k <= 10^5`, and `0 <= nums[i] <= 10^5`.
- Expected Output: The maximum possible score after applying the operations `k` times.
- Key Requirements: The operations involve either incrementing an element by 1 or appending a new element to the array with a value of 1.
- Edge Cases: When `k` is 0, no operations can be applied, and the score remains the sum of the squares of the elements in `nums`. When `k` equals or exceeds the sum of the elements in `nums`, the score can be maximized by appending new elements.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible combinations of operations (incrementing an element or appending a new element) `k` times and calculate the score after each set of operations.
- Step-by-step breakdown:
  1. Initialize a variable to store the maximum score found so far.
  2. Generate all possible sequences of `k` operations (increment or append).
  3. For each sequence, apply the operations to a copy of the input array `nums`.
  4. Calculate the score for the modified array by summing the squares of its elements.
  5. Update the maximum score if the current score is higher.
- Why this approach comes to mind first: It directly addresses the problem by considering all possible ways to apply the operations, ensuring no potential solution is overlooked.

```cpp
#include <vector>
#include <algorithm>

int maximumScore(std::vector<int>& nums, int k) {
    int maxScore = 0;
    // Generate all permutations of operations (increment or append)
    // This is a simplified representation; actual implementation would involve recursion or a similar method to generate all sequences
    for (int i = 0; i < (1 << k); ++i) { // Example loop, actual implementation would be more complex
        std::vector<int> temp = nums;
        for (int j = 0; j < k; ++j) {
            if ((i & (1 << j))) { // If the jth bit is set, increment an element
                // Logic to choose which element to increment or append
                // This is simplified; actual logic would depend on the specific sequence generation method
                temp[temp.size() - 1]++;
            } else { // Append a new element
                temp.push_back(1);
            }
        }
        int score = 0;
        for (int num : temp) {
            score += num * num;
        }
        maxScore = std::max(maxScore, score);
    }
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^k \cdot n)$, where $n$ is the number of elements in `nums`. This is because we generate $2^k$ sequences of operations and for each sequence, we potentially modify and calculate the score for the array.
> - **Space Complexity:** $O(n + k)$, as we need to store the modified array and the sequence of operations.
> - **Why these complexities occur:** The brute force approach involves generating an exponential number of sequences and then applying these sequences to the input array, leading to high time complexity. The space complexity is due to storing the modified array and the sequences of operations.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: The score is maximized when the sum of the squares of the elements is as large as possible. Given the operations (increment or append), we should prioritize appending new elements (each with a value of 1) when `k` is large because this allows us to distribute `k` across more elements, reducing the average value per element but increasing the overall sum of squares due to the square of the number of elements increasing faster than the linear decrease in value per element.
- Detailed breakdown: 
  1. If `k` is less than or equal to the sum of the elements in `nums`, we should increment the smallest elements first because this maximizes the increase in the sum of squares per operation.
  2. If `k` exceeds the sum of the elements in `nums`, we append new elements with a value of 1 until `k` is exhausted or we reach a point where appending does not increase the score further.
- Proof of optimality: This approach is optimal because it ensures that the operations are applied in a way that maximizes the sum of squares. By prioritizing the smallest elements for increment operations and appending new elements when `k` is large, we ensure that the distribution of values maximizes the score.

```cpp
#include <vector>
#include <algorithm>

int maximumScore(std::vector<int>& nums, int k) {
    std::sort(nums.begin(), nums.end());
    long long score = 0;
    for (int num : nums) {
        score += (long long)num * num;
    }
    
    for (int i = 0; i < k; ++i) {
        if (!nums.empty() && nums[0] <= k - i) {
            nums[0]++;
            score += 2 * nums[0] - 1;
        } else {
            nums.insert(nums.begin(), 1);
            score += 1;
            k -= nums[0];
        }
    }
    return score;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + k)$, where $n$ is the number of elements in `nums`. The sorting operation dominates the time complexity.
> - **Space Complexity:** $O(n)$, for storing the input array and potentially inserting new elements.
> - **Optimality proof:** This approach is optimal because it prioritizes operations that maximize the increase in the sum of squares. By first sorting the array and then applying the operations, we ensure that the smallest elements are incremented first, and new elements are appended when this is more beneficial, thus maximizing the score.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, greedy algorithm principles.
- Problem-solving patterns identified: Prioritizing operations based on their impact on the objective function (maximizing the sum of squares).
- Optimization techniques learned: Applying operations in a way that maximizes the objective function, considering the trade-offs between different operations.

**Mistakes to Avoid:**
- Common implementation errors: Not considering the edge cases where `k` is 0 or exceeds the sum of the elements in `nums`.
- Edge cases to watch for: Handling the scenarios where `k` equals or exceeds the sum of the elements in `nums`, and where `k` is 0.
- Performance pitfalls: Using a brute force approach for large inputs, which can lead to exponential time complexity.
- Testing considerations: Testing with various inputs, including edge cases, to ensure the solution works correctly under different scenarios.