## Minimize Deviation in Array
**Problem Link:** https://leetcode.com/problems/minimize-deviation-in-array/description

**Problem Statement:**
- Input format: You are given an array of integers `nums` and an integer `k`.
- Constraints: The length of `nums` is at least 1 and at most $10^5$. Each element in `nums` is between 1 and $10^9$ (inclusive). `k` is a positive integer.
- Expected output format: The minimum possible difference between the maximum and minimum elements in the array after at most `k` operations.
- Key requirements and edge cases to consider: We can perform two types of operations: 
  1. If `nums[i]` is even, we can divide `nums[i]` by 2.
  2. We can multiply `nums[i]` by 2.
  Each operation can be performed at most `k` times.

### Brute Force Approach
**Explanation:**
- The initial thought process involves trying all possible combinations of operations on each element in the array and checking which combination results in the minimum difference between the maximum and minimum elements.
- Step-by-step breakdown: 
  1. Generate all possible combinations of operations for each element.
  2. For each combination, apply the operations to the elements and calculate the difference between the maximum and minimum elements.
  3. Keep track of the minimum difference found.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

int minimizeDeviation(std::vector<int>& nums, int k) {
    int minDiff = INT_MAX;
    for (int mask = 0; mask < (1 << nums.size()); mask++) {
        std::vector<int> temp = nums;
        for (int i = 0; i < nums.size(); i++) {
            if ((mask & (1 << i))) {
                // Apply operation to temp[i]
                while (temp[i] % 2 == 0 && k > 0) {
                    temp[i] /= 2;
                    k--;
                }
            }
        }
        int maxVal = *std::max_element(temp.begin(), temp.end());
        int minVal = *std::min_element(temp.begin(), temp.end());
        minDiff = std::min(minDiff, maxVal - minVal);
    }
    return minDiff;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot k)$, where $n$ is the number of elements in `nums`. This is because we generate $2^n$ combinations and for each combination, we apply at most $k$ operations to each element.
> - **Space Complexity:** $O(n)$, as we need to store the temporary array `temp`.
> - **Why these complexities occur:** The brute force approach involves generating all possible combinations of operations, which results in exponential time complexity. The space complexity is linear because we only need to store a temporary array of the same size as the input array.

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a priority queue to keep track of the maximum element in the array. We also keep track of the minimum element in the array.
- We iterate through the array and for each element, we check if it is even. If it is even, we divide it by 2 and add it back to the priority queue.
- We keep track of the minimum difference between the maximum and minimum elements.

```cpp
#include <queue>
#include <vector>
#include <algorithm>

int minimizeDeviation(std::vector<int>& nums, int k) {
    std::priority_queue<int> maxHeap;
    int minVal = INT_MAX;
    for (int num : nums) {
        maxHeap.push(num);
        minVal = std::min(minVal, num);
    }
    int minDiff = INT_MAX;
    while (k > 0) {
        int maxVal = maxHeap.top();
        maxHeap.pop();
        if (maxVal % 2 == 1) {
            break;
        }
        maxVal /= 2;
        maxHeap.push(maxVal);
        minVal = std::min(minVal, maxVal);
        minDiff = std::min(minDiff, maxHeap.top() - minVal);
        k--;
    }
    return minDiff;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the number of elements in `nums`. This is because we iterate through the array and for each element, we perform at most $k$ operations.
> - **Space Complexity:** $O(n)$, as we need to store the priority queue.
> - **Optimality proof:** This approach is optimal because we only consider the maximum element in the array and try to minimize it. We also keep track of the minimum element in the array to ensure that the difference between the maximum and minimum elements is minimized.

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queue, iteration, and minimization.
- Problem-solving patterns identified: Using a priority queue to keep track of the maximum element and iterating through the array to find the minimum difference.
- Optimization techniques learned: Minimizing the maximum element and keeping track of the minimum element.
- Similar problems to practice: Minimizing the maximum element in an array, finding the minimum difference between two elements in an array.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if an element is even before dividing it by 2.
- Edge cases to watch for: When the input array is empty or contains only one element.
- Performance pitfalls: Using a brute force approach that generates all possible combinations of operations.
- Testing considerations: Testing the function with different input arrays and values of `k`.