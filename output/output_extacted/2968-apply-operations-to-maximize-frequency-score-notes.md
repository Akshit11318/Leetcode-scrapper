## Apply Operations to Maximize Frequency Score

**Problem Link:** https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/description

**Problem Statement:**
- Input: An integer array `nums`.
- Constraints: `1 <= nums.length <= 2 * 10^4`, `1 <= nums[i] <= 10^5`.
- Expected output: The maximum frequency score that can be achieved by applying operations to `nums`.
- Key requirements: The frequency score is the sum of the frequency of the most frequent element after applying operations. An operation consists of either incrementing or decrementing an element in `nums` by 1.

**Example Test Cases:**
- Example 1: Input: `nums = [1,2,4]`, Output: `3`. Explanation: After applying the operation, the array becomes `[1,2,2]`, and the frequency score is `3`.
- Example 2: Input: `nums = [1,2,3]`, Output: `2`. Explanation: After applying the operation, the array becomes `[1,2,2]`, and the frequency score is `2`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible operations on the array `nums` and calculate the frequency score for each resulting array.
- The brute force approach involves iterating over all possible combinations of incrementing and decrementing each element in `nums`.
- This approach is not efficient due to the large number of possible combinations.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

int maxFrequencyScore(std::vector<int>& nums) {
    int maxScore = 0;
    // Generate all possible combinations of operations
    for (int mask = 0; mask < (1 << nums.size()); mask++) {
        std::vector<int> temp = nums;
        for (int i = 0; i < nums.size(); i++) {
            if ((mask & (1 << i)) != 0) {
                temp[i]++;
            } else {
                temp[i]--;
            }
        }
        // Calculate the frequency score for the current combination
        std::unordered_map<int, int> freq;
        for (int num : temp) {
            freq[num]++;
        }
        int maxFreq = 0;
        for (auto& pair : freq) {
            maxFreq = std::max(maxFreq, pair.second);
        }
        maxScore = std::max(maxScore, maxFreq);
    }
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of `nums`. This is because we generate all possible combinations of operations and calculate the frequency score for each combination.
> - **Space Complexity:** $O(n)$, where $n$ is the length of `nums`. This is because we need to store the temporary array and the frequency map.
> - **Why these complexities occur:** The brute force approach involves generating all possible combinations of operations, which results in an exponential time complexity. The space complexity is linear because we need to store the temporary array and the frequency map.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to sort the array `nums` and then apply operations to make the elements as close to the median as possible.
- The optimal approach involves sorting the array `nums` and then applying operations to make the elements as close to the median as possible.
- This approach is optimal because it minimizes the number of operations needed to achieve the maximum frequency score.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

int maxFrequencyScore(std::vector<int>& nums) {
    std::sort(nums.begin(), nums.end());
    int maxScore = 0;
    for (int i = 0; i < nums.size(); i++) {
        int freq = 0;
        for (int j = i; j < nums.size(); j++) {
            if (nums[j] - nums[i] <= j - i) {
                freq++;
            }
        }
        maxScore = std::max(maxScore, freq);
    }
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of `nums`. This is because we sort the array and then iterate over the array to calculate the frequency score.
> - **Space Complexity:** $O(1)$, where $n$ is the length of `nums`. This is because we only need to store the maximum frequency score.
> - **Optimality proof:** The optimal approach is optimal because it minimizes the number of operations needed to achieve the maximum frequency score. By sorting the array and applying operations to make the elements as close to the median as possible, we ensure that the maximum frequency score is achieved.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, frequency calculation, and optimization.
- Problem-solving patterns identified: using sorting to simplify the problem and applying operations to achieve the maximum frequency score.
- Optimization techniques learned: minimizing the number of operations needed to achieve the maximum frequency score.

**Mistakes to Avoid:**
- Common implementation errors: not considering the edge cases, not optimizing the solution.
- Edge cases to watch for: empty array, array with a single element, array with duplicate elements.
- Performance pitfalls: using inefficient algorithms, not considering the time and space complexities.
- Testing considerations: testing the solution with different inputs, including edge cases and large inputs.