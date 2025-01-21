## Minimum Operations to Make Median of Array Equal to K
**Problem Link:** https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/description

**Problem Statement:**
- Input format and constraints: Given an array `nums` of size `n`, and an integer `k`. The goal is to make the median of the array equal to `k` by performing the minimum number of operations. An operation is defined as either increasing or decreasing an element in the array by 1.
- Expected output format: The minimum number of operations required to make the median of the array equal to `k`.
- Key requirements and edge cases to consider: The median of the array can be either an integer in the array or the average of two integers in the array (for arrays of even length). The operations can only increase or decrease an element by 1, and the goal is to minimize the total number of operations.

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of operations on the array to find the minimum number of operations required to make the median equal to `k`.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of operations (increasing or decreasing an element by 1) on the array.
  2. For each combination, calculate the new median of the array.
  3. If the new median is equal to `k`, calculate the total number of operations performed.
  4. Keep track of the minimum number of operations required to make the median equal to `k`.
- Why this approach comes to mind first: The brute force approach is often the most straightforward and easiest to understand, as it involves trying all possible solutions and selecting the best one.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int minOperations(vector<int>& nums, int k) {
    int n = nums.size();
    int minOps = INT_MAX;
    
    // Generate all possible combinations of operations
    for (int mask = 0; mask < (1 << (2 * n)); mask++) {
        vector<int> arr = nums;
        int ops = 0;
        
        // Apply operations to the array
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << (2 * i))) != 0) {
                arr[i]++;
                ops++;
            }
            if ((mask & (1 << (2 * i + 1))) != 0) {
                arr[i]--;
                ops++;
            }
        }
        
        // Calculate the new median
        sort(arr.begin(), arr.end());
        double median;
        if (n % 2 == 0) {
            median = (arr[n / 2 - 1] + arr[n / 2]) / 2.0;
        } else {
            median = arr[n / 2];
        }
        
        // Update the minimum number of operations
        if (median == k) {
            minOps = min(minOps, ops);
        }
    }
    
    return minOps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{2n} \cdot n \log n)$, where $n$ is the size of the array. This is because we generate all possible combinations of operations, and for each combination, we sort the array to calculate the median.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the array. This is because we need to store the array and the current combination of operations.
> - **Why these complexities occur:** The brute force approach involves trying all possible combinations of operations, which results in an exponential time complexity. The sorting operation to calculate the median also contributes to the time complexity.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of trying all possible combinations of operations, we can focus on the elements that are closest to the target median `k`. We can calculate the minimum number of operations required to move these elements to `k`.
- Detailed breakdown of the approach:
  1. Sort the array in ascending order.
  2. Calculate the median of the array.
  3. If the median is less than `k`, we need to increase the elements that are closest to `k`.
  4. If the median is greater than `k`, we need to decrease the elements that are closest to `k`.
  5. Calculate the minimum number of operations required to move these elements to `k`.
- Proof of optimality: This approach is optimal because we are focusing on the elements that are closest to the target median `k`, which minimizes the number of operations required.

```cpp
int minOperations(vector<int>& nums, int k) {
    int n = nums.size();
    sort(nums.begin(), nums.end());
    
    int ops = 0;
    if (n % 2 == 0) {
        // For even-length arrays, we need to move the two middle elements to k
        int mid1 = nums[n / 2 - 1];
        int mid2 = nums[n / 2];
        ops += abs(mid1 - k) + abs(mid2 - k);
    } else {
        // For odd-length arrays, we need to move the middle element to k
        int mid = nums[n / 2];
        ops += abs(mid - k);
    }
    
    return ops;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the size of the array. This is because we need to sort the array to calculate the median.
> - **Space Complexity:** $O(1)$, where $n$ is the size of the array. This is because we only need to store the array and the current median.
> - **Optimality proof:** This approach is optimal because we are focusing on the elements that are closest to the target median `k`, which minimizes the number of operations required.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, median calculation, and optimization techniques.
- Problem-solving patterns identified: Focusing on the elements that are closest to the target median `k` to minimize the number of operations required.
- Optimization techniques learned: Instead of trying all possible combinations of operations, we can focus on the elements that are closest to the target median `k`.
- Similar problems to practice: Other optimization problems that involve minimizing the number of operations required to achieve a certain goal.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the array correctly, or not calculating the median correctly.
- Edge cases to watch for: Arrays of length 0 or 1, or arrays with duplicate elements.
- Performance pitfalls: Trying all possible combinations of operations, which can result in an exponential time complexity.
- Testing considerations: Test the function with different input arrays and target medians `k` to ensure that it is working correctly.