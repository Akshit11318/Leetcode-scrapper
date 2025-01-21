## Maximum Average Subarray I
**Problem Link:** https://leetcode.com/problems/maximum-average-subarray-i/description

**Problem Statement:**
- Given an array `nums` and an integer `k`, find the maximum average of a subarray of length `k`.
- Input format and constraints: `1 <= k <= nums.size()` and `nums.size()` is between 1 and 10^4.
- Expected output format: A double representing the maximum average.
- Key requirements and edge cases to consider: Empty arrays, arrays with a single element, and arrays where `k` is equal to the array length.
- Example test cases with explanations:
  - `nums = [1, 12, -5, -6, 50, 3], k = 4` should return `12.75`.
  - `nums = [5], k = 1` should return `5.0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the sum of every possible subarray of length `k` and divide by `k` to find the average.
- Step-by-step breakdown of the solution:
  1. Iterate over the array with a sliding window of size `k`.
  2. For each window, calculate the sum of the elements.
  3. Calculate the average by dividing the sum by `k`.
  4. Keep track of the maximum average found.
- Why this approach comes to mind first: It directly addresses the problem by considering all possible subarrays.

```cpp
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double maxAverage = -INFINITY;
        for (int i = 0; i <= nums.size() - k; i++) {
            double sum = 0.0;
            for (int j = i; j < i + k; j++) {
                sum += nums[j];
            }
            double average = sum / k;
            maxAverage = max(maxAverage, average);
        }
        return maxAverage;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the size of the array, because for each starting position, we sum `k` elements.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the sum, average, and maximum average.
> - **Why these complexities occur:** The nested loop structure causes the time complexity to be proportional to the product of the array size and the window size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of recalculating the sum of the subarray for each position, we can maintain a running sum and update it by subtracting the element going out of the window and adding the element entering the window.
- Detailed breakdown of the approach:
  1. Initialize the sum of the first window.
  2. Initialize the maximum average with the average of the first window.
  3. Slide the window one element at a time, updating the sum by subtracting the outgoing element and adding the incoming element.
  4. Update the maximum average if the current window's average is higher.
- Proof of optimality: This approach considers all subarrays of length `k` in a single pass through the array, making it the most efficient way to find the maximum average.

```cpp
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double sum = 0.0;
        for (int i = 0; i < k; i++) {
            sum += nums[i];
        }
        double maxAverage = sum / k;
        for (int i = k; i < nums.size(); i++) {
            sum = sum - nums[i - k] + nums[i];
            maxAverage = max(maxAverage, sum / k);
        }
        return maxAverage;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the array, because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the sum and the maximum average.
> - **Optimality proof:** This approach has the best possible time complexity because it only requires a single pass through the array, making it impossible to improve upon.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique and maintaining a running sum.
- Problem-solving patterns identified: Looking for ways to avoid redundant calculations and optimizing loops.
- Optimization techniques learned: Using a single pass through the data and minimizing the number of operations within the loop.
- Similar problems to practice: Other sliding window problems, such as finding the maximum sum of a subarray or the longest substring without repeating characters.

**Mistakes to Avoid:**
- Common implementation errors: Failing to update the sum correctly when sliding the window or not handling edge cases properly.
- Edge cases to watch for: Empty arrays, arrays with a single element, and arrays where `k` is equal to the array length.
- Performance pitfalls: Using nested loops when a single pass is possible, leading to unnecessary time complexity.
- Testing considerations: Ensure that the solution works correctly for arrays of different sizes, including edge cases, and that it handles different values of `k`.