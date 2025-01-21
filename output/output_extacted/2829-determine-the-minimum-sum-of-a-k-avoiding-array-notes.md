## Determine the Minimum Sum of a K-Avoiding Array

**Problem Link:** https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/description

**Problem Statement:**
- Input format: An integer array `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= k <= 10^9`, `1 <= nums[i] <= 10^9`.
- Expected output format: The minimum sum of a k-avoiding array.
- Key requirements: A k-avoiding array is an array where no two elements are congruent modulo k.
- Edge cases: Handle cases where the input array is empty or k is 1.

**Example Test Cases:**
- Input: `nums = [1,2,3,4,5], k = 5`, Output: `15`
- Input: `nums = [1,2,3,4,5], k = 3`, Output: `12`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible k-avoiding arrays and calculate their sums.
- Step-by-step breakdown:
  1. Generate all permutations of the input array.
  2. For each permutation, check if it is a k-avoiding array.
  3. If it is, calculate its sum.
  4. Keep track of the minimum sum found.

```cpp
#include <vector>
#include <algorithm>
#include <numeric>

int minimumSum(std::vector<int>& nums, int k) {
    // Generate all permutations of the input array
    std::sort(nums.begin(), nums.end());
    int minSum = INT_MAX;
    do {
        // Check if the current permutation is a k-avoiding array
        bool isKAvoiding = true;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] % k == nums[j] % k) {
                    isKAvoiding = false;
                    break;
                }
            }
            if (!isKAvoiding) break;
        }
        // If it is, calculate its sum
        if (isKAvoiding) {
            int sum = std::accumulate(nums.begin(), nums.end(), 0);
            // Keep track of the minimum sum found
            minSum = std::min(minSum, sum);
        }
    } while (std::next_permutation(nums.begin(), nums.end()));
    return minSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n^2)$, where $n$ is the length of the input array. This is because we generate all permutations of the input array and for each permutation, we check if it is a k-avoiding array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum sum and the current permutation.
> - **Why these complexities occur:** The high time complexity occurs because we generate all permutations of the input array, which has a factorial number of permutations. The space complexity is low because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a greedy approach to construct a k-avoiding array with the minimum sum.
- Step-by-step breakdown:
  1. Sort the input array in ascending order.
  2. Initialize an empty result array.
  3. Iterate over the sorted input array and add each element to the result array if it is not congruent modulo k to any element already in the result array.
  4. If an element is congruent modulo k to an element already in the result array, add the next smallest element that is not congruent modulo k to the result array.

```cpp
#include <vector>
#include <algorithm>
#include <numeric>

int minimumSum(std::vector<int>& nums, int k) {
    // Sort the input array in ascending order
    std::sort(nums.begin(), nums.end());
    std::vector<int> result;
    for (int num : nums) {
        // Check if the current number is congruent modulo k to any number in the result array
        bool isCongruent = false;
        for (int res : result) {
            if (num % k == res % k) {
                isCongruent = true;
                break;
            }
        }
        // If it is not congruent, add it to the result array
        if (!isCongruent) {
            result.push_back(num);
        }
    }
    // Calculate the sum of the result array
    return std::accumulate(result.begin(), result.end(), 0);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + n \cdot m)$, where $n$ is the length of the input array and $m$ is the size of the result array. This is because we sort the input array and then iterate over it to construct the result array.
> - **Space Complexity:** $O(n)$, as we store the result array.
> - **Optimality proof:** This approach is optimal because it constructs a k-avoiding array with the minimum sum by greedily selecting the smallest elements that are not congruent modulo k.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: greedy algorithms, sorting, and modular arithmetic.
- Problem-solving patterns identified: using a greedy approach to construct an optimal solution.
- Optimization techniques learned: using a sorting step to simplify the problem and reduce the search space.

**Mistakes to Avoid:**
- Common implementation errors: not checking for congruence modulo k correctly, not handling edge cases such as an empty input array.
- Edge cases to watch for: handling cases where the input array is empty or k is 1.
- Performance pitfalls: using a brute force approach that generates all permutations of the input array.
- Testing considerations: testing the implementation with a variety of input arrays and values of k to ensure correctness.