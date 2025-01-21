## Minimize the Maximum of Two Arrays

**Problem Link:** https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/description

**Problem Statement:**
- Input format and constraints: Given two arrays `nums1` and `nums2` of length `m` and `n` respectively, find the minimum maximum value of the two arrays.
- Expected output format: The minimum maximum value that can be achieved.
- Key requirements and edge cases to consider: The arrays can be empty, and the maximum value of the two arrays can be the same.
- Example test cases with explanations:
  - Example 1: `nums1 = [2,2,1,1,1,2,2]`, `nums2 = [10,10,10]`, the minimum maximum value is 3.
  - Example 2: `nums1 = [7,7,7,7,7,7,7]`, `nums2 = [1,1,1,1,1,1,1]`, the minimum maximum value is 7.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsets of both arrays, calculate the maximum value for each subset, and find the minimum of these maximum values.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of `nums1`.
  2. For each subset of `nums1`, calculate the maximum value.
  3. Generate all possible subsets of `nums2`.
  4. For each subset of `nums2`, calculate the maximum value.
  5. Find the minimum of the maximum values calculated in steps 2 and 4.
- Why this approach comes to mind first: It's a straightforward approach that considers all possible scenarios.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int minimizeTheMaximumOfTwoArrays(std::vector<int>& nums1, std::vector<int>& nums2) {
    int m = nums1.size();
    int n = nums2.size();
    
    int maxVal = std::max(*std::max_element(nums1.begin(), nums1.end()), *std::max_element(nums2.begin(), nums2.end()));
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int minMax = std::max(nums1[i], nums2[j]);
            maxVal = std::min(maxVal, minMax);
        }
    }
    
    return maxVal;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \cdot n)$, where $m$ and $n$ are the sizes of `nums1` and `nums2` respectively. This is because we are iterating over each element of both arrays.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with input size.
> - **Why these complexities occur:** The time complexity is due to the nested loops, and the space complexity is because we are only using a constant amount of space to store the maximum value.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible subsets, we can use binary search to find the minimum maximum value.
- Detailed breakdown of the approach:
  1. Initialize the search range to the minimum and maximum values of the two arrays.
  2. Perform a binary search within this range.
  3. For each mid value in the search range, check if it's possible to achieve this value as the maximum of both arrays.
  4. If it's possible, update the upper bound of the search range. Otherwise, update the lower bound.
- Proof of optimality: This approach is optimal because it reduces the search space from $O(m \cdot n)$ to $O(\log(maxVal))$, where $maxVal$ is the maximum value of the two arrays.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

bool canAchieve(std::vector<int>& nums1, std::vector<int>& nums2, int target) {
    int m = nums1.size();
    int n = nums2.size();
    int count = 0;
    
    for (int i = 0; i < m; i++) {
        if (nums1[i] <= target) {
            count++;
        }
    }
    
    for (int i = 0; i < n; i++) {
        if (nums2[i] <= target) {
            count++;
        }
    }
    
    return count >= (m + n + 1) / 2;
}

int minimizeTheMaximumOfTwoArrays(std::vector<int>& nums1, std::vector<int>& nums2) {
    int m = nums1.size();
    int n = nums2.size();
    
    int minVal = std::min(*std::min_element(nums1.begin(), nums1.end()), *std::min_element(nums2.begin(), nums2.end()));
    int maxVal = std::max(*std::max_element(nums1.begin(), nums1.end()), *std::max_element(nums2.begin(), nums2.end()));
    
    while (minVal < maxVal) {
        int mid = minVal + (maxVal - minVal) / 2;
        
        if (canAchieve(nums1, nums2, mid)) {
            maxVal = mid;
        } else {
            minVal = mid + 1;
        }
    }
    
    return minVal;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O((m + n) \cdot \log(maxVal))$, where $m$ and $n$ are the sizes of `nums1` and `nums2` respectively, and $maxVal$ is the maximum value of the two arrays. This is because we are performing a binary search and for each mid value, we are checking if it's possible to achieve this value as the maximum of both arrays.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with input size.
> - **Optimality proof:** This approach is optimal because it reduces the search space from $O(m \cdot n)$ to $O(\log(maxVal))$, where $maxVal$ is the maximum value of the two arrays.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, greedy algorithm.
- Problem-solving patterns identified: Reducing the search space, using binary search to find the optimal solution.
- Optimization techniques learned: Using binary search to reduce the search space.
- Similar problems to practice: Problems that involve finding the minimum or maximum value of a function, or problems that involve binary search.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not checking for overflow.
- Edge cases to watch for: Empty arrays, arrays with a single element.
- Performance pitfalls: Using a brute force approach, not optimizing the search space.
- Testing considerations: Testing with different input sizes, testing with edge cases.