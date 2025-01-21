## Minimum Average of Smallest and Largest Elements

**Problem Link:** https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/description

**Problem Statement:**
- Input: A list of integers `nums` and an integer `k`.
- Constraints: `2 <= nums.length <= 1000`, `1 <= nums[i] <= 10^4`, and `1 <= k <= nums.length`.
- Expected Output: The minimum possible average of the smallest and largest elements after `k` operations.
- Key Requirements and Edge Cases:
  - The array can be modified in-place.
  - We can increase or decrease any element in the array by 1 in a single operation.
  - Example test cases:
    - `nums = [4, 1, 2, 3], k = 2`, the output should be `3.0`.
    - `nums = [7, 8, 8], k = 1`, the output should be `7.0`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of increasing or decreasing elements to find the minimum average.
- We can generate all permutations of the array after `k` operations and calculate the average for each permutation.
- This approach comes to mind first because it's a straightforward way to consider all possibilities.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

double minAverage(vector<int>& nums, int k) {
    double minAvg = 1e9;
    sort(nums.begin(), nums.end());
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            vector<int> temp = nums;
            int operations = k;
            // Try to increase the smallest element and decrease the largest element
            while (operations > 0 && temp[i] < temp[j]) {
                temp[i]++;
                temp[j]--;
                operations--;
            }
            double avg = (double)(temp[i] + temp[j]) / 2.0;
            minAvg = min(minAvg, avg);
        }
    }
    return minAvg;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k)$, where $n$ is the number of elements in the array. The reason for this complexity is that we're iterating over all pairs of elements and performing `k` operations for each pair.
> - **Space Complexity:** $O(n)$, as we're creating a temporary copy of the array.
> - **Why these complexities occur:** The brute force approach involves trying all possible combinations of elements, which results in a high time complexity. The space complexity is relatively low because we're only creating a single temporary copy of the array.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is that we should always try to make the smallest element as large as possible and the largest element as small as possible.
- We can achieve this by sorting the array and then increasing the smallest element and decreasing the largest element until we've used up all `k` operations.
- This approach is optimal because it minimizes the difference between the smallest and largest elements, which in turn minimizes their average.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

double minAverage(vector<int>& nums, int k) {
    sort(nums.begin(), nums.end());
    int n = nums.size();
    int minVal = nums[0];
    int maxVal = nums[n - 1];
    // Increase the smallest element and decrease the largest element
    while (k > 0 && minVal < maxVal) {
        if (maxVal - minVal > 1) {
            minVal++;
            maxVal--;
            k -= 2;
        } else {
            minVal++;
            k--;
        }
    }
    return (double)(minVal + maxVal) / 2.0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + k)$, where $n$ is the number of elements in the array. The reason for this complexity is that we're sorting the array and then performing at most `k` operations.
> - **Space Complexity:** $O(n)$, as we're sorting the array in-place.
> - **Optimality proof:** This approach is optimal because it minimizes the difference between the smallest and largest elements, which in turn minimizes their average. We're using all `k` operations to reduce the difference between the smallest and largest elements, which is the most efficient way to minimize their average.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, greedy algorithms, and optimization techniques.
- Problem-solving patterns identified: minimizing the difference between two values to minimize their average.
- Optimization techniques learned: using all available operations to reduce the difference between the smallest and largest elements.
- Similar problems to practice: other optimization problems involving arrays and sorting.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, such as when `k` is 0 or when the array has only one element.
- Edge cases to watch for: when the smallest and largest elements are equal, or when `k` is greater than the difference between the largest and smallest elements.
- Performance pitfalls: using a brute force approach, which can result in a high time complexity.
- Testing considerations: testing the function with different inputs, including edge cases, to ensure it's working correctly.