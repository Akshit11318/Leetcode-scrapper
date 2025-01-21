## Split Array Largest Sum
**Problem Link:** [https://leetcode.com/problems/split-array-largest-sum/description](https://leetcode.com/problems/split-array-largest-sum/description)

**Problem Statement:**
- Input format and constraints: Given an array of integers `nums` and an integer `m`, split the array into `m` non-empty subarrays such that the largest sum of subarrays is minimized.
- Expected output format: The minimum largest sum.
- Key requirements and edge cases to consider: 
    - `1 <= nums.length <= 1000`
    - `0 <= nums[i] <= 10^6`
    - `1 <= m <= min(50, nums.length)`
- Example test cases with explanations: 
    - `nums = [7,2,5,10,8], m = 2`, the minimum largest sum is `18` because we can split the array into `[7,2,5]` and `[10,8]`.
    - `nums = [1,2,3,4,5], m = 2`, the minimum largest sum is `9` because we can split the array into `[1,2,3]` and `[4,5]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible ways to split the array into `m` subarrays and calculate the largest sum for each split.
- Step-by-step breakdown of the solution:
    1. Generate all possible splits of the array into `m` subarrays.
    2. For each split, calculate the sum of each subarray.
    3. Find the maximum sum among all subarrays in the current split.
    4. Update the minimum largest sum if the current maximum sum is smaller.
- Why this approach comes to mind first: It's a straightforward way to solve the problem by trying all possibilities.

```cpp
#include <vector>
#include <algorithm>

int bruteForceSplitArray(std::vector<int>& nums, int m) {
    int n = nums.size();
    int minLargestSum = INT_MAX;

    // Generate all possible splits
    std::vector<int> splits;
    std::function<void(int, int)> generateSplits = [&](int start, int count) {
        if (count == m - 1) {
            splits.push_back(n);
            return;
        }
        for (int i = start; i < n; ++i) {
            splits.push_back(i + 1);
            generateSplits(i + 1, count + 1);
            splits.pop_back();
        }
    };
    generateSplits(0, 0);

    // Calculate the largest sum for each split
    for (int i = 0; i < splits.size(); i += m - 1) {
        std::vector<int> subarraySums;
        int sum = 0;
        for (int j = 0; j < m; ++j) {
            int end = (j == m - 1) ? n : splits[i + j];
            for (int k = (j == 0) ? 0 : splits[i + j - 1]; k < end; ++k) {
                sum += nums[k];
            }
            subarraySums.push_back(sum);
            sum = 0;
        }
        int maxSum = *std::max_element(subarraySums.begin(), subarraySums.end());
        minLargestSum = std::min(minLargestSum, maxSum);
    }

    return minLargestSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot m \cdot n)$, where $n$ is the number of elements in the array. This is because we generate all possible splits and for each split, we calculate the sum of each subarray.
> - **Space Complexity:** $O(n)$, for storing the splits and subarray sums.
> - **Why these complexities occur:** The exponential time complexity is due to generating all possible splits, and the linear space complexity is for storing the splits and subarray sums.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use binary search to find the minimum largest sum. The idea is to try all possible values of the largest sum and check if it's possible to split the array into `m` subarrays such that the sum of each subarray is less than or equal to the current largest sum.
- Detailed breakdown of the approach:
    1. Calculate the total sum of the array and the maximum element in the array.
    2. Initialize the search range to `[maxElement, totalSum]`.
    3. Perform binary search on the search range.
    4. For each mid value, check if it's possible to split the array into `m` subarrays such that the sum of each subarray is less than or equal to `mid`.
    5. If it's possible, update the right boundary of the search range to `mid - 1`. Otherwise, update the left boundary to `mid + 1`.
- Proof of optimality: The binary search approach ensures that we find the minimum largest sum in $O(n \log S)$ time, where $S$ is the sum of all elements in the array.

```cpp
int splitArray(std::vector<int>& nums, int m) {
    int n = nums.size();
    int totalSum = 0;
    int maxElement = 0;
    for (int num : nums) {
        totalSum += num;
        maxElement = std::max(maxElement, num);
    }

    int left = maxElement;
    int right = totalSum;
    while (left < right) {
        int mid = left + (right - left) / 2;
        int count = 1;
        int sum = 0;
        for (int num : nums) {
            sum += num;
            if (sum > mid) {
                count++;
                sum = num;
            }
        }
        if (count <= m) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return left;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log S)$, where $n$ is the number of elements in the array and $S$ is the sum of all elements in the array.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space.
> - **Optimality proof:** The binary search approach ensures that we find the minimum largest sum in $O(n \log S)$ time, which is optimal because we need to check all possible values of the largest sum.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, dynamic programming.
- Problem-solving patterns identified: Using binary search to find the minimum or maximum value of a function.
- Optimization techniques learned: Using binary search to reduce the search space.
- Similar problems to practice: [https://leetcode.com/problems/koko-eating-bananas/](https://leetcode.com/problems/koko-eating-bananas/), [https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/).

**Mistakes to Avoid:**
- Common implementation errors: Not checking the base cases, not handling edge cases.
- Edge cases to watch for: When the array is empty, when `m` is 1 or `n`.
- Performance pitfalls: Using brute force approach, not using binary search.
- Testing considerations: Test the function with different inputs, including edge cases.