## Check If It Is Possible to Split Array
**Problem Link:** https://leetcode.com/problems/check-if-it-is-possible-to-split-array/description

**Problem Statement:**
- Input: An integer array `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^5`, `1 <= k <= 10^5`.
- Expected Output: `true` if it is possible to split the array into `k` non-empty subarrays such that the sum of each subarray is equal to the target sum, `false` otherwise.
- Key Requirements and Edge Cases:
  - The sum of each subarray must be equal to the target sum.
  - The array must be split into exactly `k` non-empty subarrays.
  - Example test cases: `[1, 2, 3, 4, 5]` with `k = 2` and target sum `9` should return `true` because `[1, 2, 3]` and `[4, 5]` sum up to `9` and `9`, respectively.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible ways to split the array into `k` subarrays and checking if the sum of each subarray equals the target sum.
- Step-by-step breakdown:
  1. Generate all possible combinations of splitting the array into `k` subarrays.
  2. For each combination, calculate the sum of each subarray.
  3. Check if all sums are equal to the target sum.
- This approach comes to mind first because it directly addresses the problem statement, but it's inefficient due to the high number of combinations.

```cpp
#include <vector>
#include <numeric>

bool canSplitArray(std::vector<int>& nums, int k) {
    int targetSum = std::accumulate(nums.begin(), nums.end(), 0) / k;
    int n = nums.size();
    
    // Generate all possible combinations of splitting the array into k subarrays
    std::vector<std::vector<int>> combinations;
    std::vector<int> currentCombination;
    generateCombinations(nums, k, 0, currentCombination, combinations);
    
    for (const auto& combination : combinations) {
        bool isValid = true;
        for (int i = 0; i < combination.size(); ++i) {
            int subarraySum = 0;
            for (int j = combination[i]; j < (i == combination.size() - 1 ? n : combination[i + 1]); ++j) {
                subarraySum += nums[j];
            }
            if (subarraySum != targetSum) {
                isValid = false;
                break;
            }
        }
        if (isValid) {
            return true;
        }
    }
    return false;
}

void generateCombinations(const std::vector<int>& nums, int k, int startIndex, std::vector<int>& currentCombination, std::vector<std::vector<int>>& combinations) {
    if (currentCombination.size() == k - 1) {
        combinations.push_back(currentCombination);
        return;
    }
    
    for (int i = startIndex; i < nums.size(); ++i) {
        currentCombination.push_back(i);
        generateCombinations(nums, k, i + 1, currentCombination, combinations);
        currentCombination.pop_back();
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot k \cdot n)$, where $n$ is the size of the input array. This is because we generate all possible combinations of splitting the array and for each combination, we calculate the sum of each subarray.
> - **Space Complexity:** $O(2^n \cdot k)$, where $k$ is the number of subarrays. This is because we store all possible combinations of splitting the array.
> - **Why these complexities occur:** These complexities occur because we use a recursive approach to generate all possible combinations of splitting the array, which results in an exponential number of combinations.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a prefix sum array to efficiently calculate the sum of each subarray.
- Detailed breakdown of the approach:
  1. Calculate the prefix sum array of the input array.
  2. Calculate the target sum by dividing the total sum of the array by `k`.
  3. Initialize a variable to store the number of subarrays with sum equal to the target sum.
  4. Iterate through the prefix sum array and for each element, check if the sum of the subarray ending at the current index is equal to the target sum.
  5. If the sum is equal to the target sum, increment the number of subarrays.
- Proof of optimality: This approach is optimal because it only requires a single pass through the input array and uses a prefix sum array to efficiently calculate the sum of each subarray.

```cpp
#include <vector>
#include <numeric>

bool canSplitArray(std::vector<int>& nums, int k) {
    int totalSum = std::accumulate(nums.begin(), nums.end(), 0);
    if (totalSum % k != 0) {
        return false;
    }
    
    int targetSum = totalSum / k;
    int currentSum = 0;
    int subarrayCount = 0;
    
    for (int num : nums) {
        currentSum += num;
        if (currentSum == targetSum) {
            subarrayCount++;
            currentSum = 0;
        } else if (currentSum > targetSum) {
            return false;
        }
    }
    
    return subarrayCount == k;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we only require a single pass through the input array.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the prefix sum and the number of subarrays.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the input array and uses a prefix sum array to efficiently calculate the sum of each subarray.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: prefix sum array, efficient calculation of subarray sums.
- Problem-solving patterns identified: using prefix sum arrays to efficiently calculate subarray sums.
- Optimization techniques learned: using a single pass through the input array to reduce time complexity.
- Similar problems to practice: problems involving subarray sums and prefix sum arrays.

**Mistakes to Avoid:**
- Common implementation errors: not checking if the total sum of the array is divisible by `k`.
- Edge cases to watch for: empty input array, `k` equal to 0 or 1.
- Performance pitfalls: using a recursive approach to generate all possible combinations of splitting the array.
- Testing considerations: test the function with different input arrays and values of `k`.