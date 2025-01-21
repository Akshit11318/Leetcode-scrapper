## Maximum Average Subarray II
**Problem Link:** https://leetcode.com/problems/maximum-average-subarray-ii/description

**Problem Statement:**
- Given an array of integers `nums` and an integer `k`, find the maximum average subarray of length `k`.
- Input format: `nums` is an array of integers, `k` is an integer.
- Expected output format: The maximum average subarray value.
- Key requirements and edge cases to consider: `1 <= k <= nums.size()`, `-10^4 <= nums[i] <= 10^4`, `nums` is not empty.
- Example test cases with explanations:
  - Example 1: `nums = [1,12,-5,-6,50,3]`, `k = 4`, Output: `12.75`
  - Example 2: `nums = [5]`, `k = 1`, Output: `5.0`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible subarray of length `k` to find the maximum average.
- Step-by-step breakdown:
  1. Iterate over the array with two nested loops to generate all possible subarrays of length `k`.
  2. For each subarray, calculate the sum of its elements.
  3. Calculate the average of the subarray by dividing the sum by `k`.
  4. Keep track of the maximum average found.
- Why this approach comes to mind first: It's straightforward and guarantees finding the maximum average subarray by checking all possibilities.

```cpp
#include <iostream>
#include <vector>
#include <climits>

double findMaxAverage(std::vector<int>& nums, int k) {
    double maxAverage = -1e9; // Initialize maxAverage to a very low value
    for (int i = 0; i <= nums.size() - k; i++) {
        int sum = 0;
        for (int j = i; j < i + k; j++) {
            sum += nums[j];
        }
        double average = static_cast<double>(sum) / k;
        maxAverage = std::max(maxAverage, average);
    }
    return maxAverage;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the size of `nums`, because for each starting position `i`, we calculate the sum of `k` elements.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum average and the sum of the current subarray.
> - **Why these complexities occur:** The nested loops cause the time complexity to be $O(n \cdot k)$, and since we only use a fixed amount of space, the space complexity is $O(1)$.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to the optimal solution: We can use a single pass through the array to calculate the sum of all subarrays of length `k` by maintaining a running sum.
- Detailed breakdown:
  1. Initialize the sum of the first subarray of length `k`.
  2. Iterate over the rest of the array, updating the sum by subtracting the element that falls out of the window and adding the new element that enters the window.
  3. At each step, calculate the average of the current subarray and update the maximum average if necessary.
- Proof of optimality: This approach only requires a single pass through the array, making it more efficient than the brute force approach.

```cpp
double findMaxAverage(std::vector<int>& nums, int k) {
    double maxAverage = -1e9;
    int windowSum = 0;
    for (int i = 0; i < nums.size(); i++) {
        windowSum += nums[i];
        if (i >= k) {
            windowSum -= nums[i - k];
        }
        if (i >= k - 1) {
            double average = static_cast<double>(windowSum) / k;
            maxAverage = std::max(maxAverage, average);
        }
    }
    return maxAverage;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of `nums`, because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum average and the sum of the current window.
> - **Optimality proof:** This is the optimal solution because we only need to make a single pass through the array to find the maximum average subarray of length `k`, and we cannot do better than linear time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a sliding window to efficiently calculate the sum of subarrays.
- Problem-solving patterns identified: Maintaining a running sum to avoid redundant calculations.
- Optimization techniques learned: Reducing the number of iterations by using a single pass through the array.
- Similar problems to practice: Maximum Subarray, Minimum Window Substring.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the window sum correctly when the window moves.
- Edge cases to watch for: Handling the case when `k` is equal to the size of `nums`.
- Performance pitfalls: Using nested loops to calculate the sum of subarrays, leading to quadratic time complexity.
- Testing considerations: Testing the function with different values of `k` and edge cases like an empty array or `k` being larger than the array size.