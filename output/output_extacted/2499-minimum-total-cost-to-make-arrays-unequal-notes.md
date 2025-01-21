## Minimum Total Cost to Make Arrays Unequal

**Problem Link:** https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/description

**Problem Statement:**
- Given two arrays `nums1` and `nums2` of the same length `n`, the task is to make the arrays unequal by changing the elements of `nums1`. The cost of changing an element from `a` to `b` is `abs(a-b)`.
- The goal is to find the minimum total cost required to make `nums1` and `nums2` unequal.
- The input arrays contain integers, and the length `n` is a positive integer.
- The expected output is the minimum total cost.

**Example Test Cases:**
- `nums1 = [1, 2, 3], nums2 = [1, 2, 4]`
- `nums1 = [1, 2, 3], nums2 = [1, 2, 3]`

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of changing elements in `nums1` and calculate the total cost for each combination.
- The brute force approach involves iterating over all possible values for each element in `nums1` and checking if the modified array is unequal to `nums2`.
- This approach comes to mind first because it guarantees finding the minimum total cost by exploring all possibilities.

```cpp
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int minCost(vector<int>& nums1, vector<int>& nums2) {
    int n = nums1.size();
    int minCost = INT_MAX;
    
    for (int mask = 0; mask < (1 << n); mask++) {
        int cost = 0;
        bool unequal = false;
        
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                // Try all possible values for nums1[i]
                for (int val = -100; val <= 100; val++) {
                    int newCost = abs(nums1[i] - val);
                    if (val != nums2[i]) {
                        unequal = true;
                    }
                    cost += newCost;
                }
            }
        }
        
        if (unequal) {
            minCost = min(minCost, cost);
        }
    }
    
    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot 201 \cdot n)$, where $n$ is the length of the input arrays. The reason is that we iterate over all possible subsets of indices (using the bitmask `mask`) and for each subset, we try all possible values for the corresponding elements in `nums1`.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum cost and other variables.
> - **Why these complexities occur:** The time complexity is high because we explore all possible combinations of changing elements in `nums1`, and for each combination, we try all possible values for the modified elements.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to realize that we only need to change the elements of `nums1` that are equal to the corresponding elements in `nums2`.
- We can use a greedy approach to find the minimum total cost by changing the equal elements one by one.
- The proof of optimality is that any other approach would require changing more elements or changing elements by a larger amount, resulting in a higher total cost.

```cpp
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int minCost(vector<int>& nums1, vector<int>& nums2) {
    int n = nums1.size();
    int minCost = 0;
    
    for (int i = 0; i < n; i++) {
        if (nums1[i] == nums2[i]) {
            // Try to change nums1[i] to a value that is closest to nums2[i]
            int minDiff = INT_MAX;
            for (int val = -100; val <= 100; val++) {
                if (val != nums2[i]) {
                    minDiff = min(minDiff, abs(nums1[i] - val));
                }
            }
            minCost += minDiff;
        }
    }
    
    return minCost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 201)$, where $n$ is the length of the input arrays. The reason is that we iterate over the elements of `nums1` and for each element, we try all possible values to find the minimum difference.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum cost and other variables.
> - **Optimality proof:** This approach is optimal because we only change the elements that are equal to the corresponding elements in `nums2`, and we change them to the closest possible value. Any other approach would require changing more elements or changing elements by a larger amount, resulting in a higher total cost.

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of a greedy approach to find the minimum total cost.
- The problem-solving pattern identified is to try to change the elements of `nums1` that are equal to the corresponding elements in `nums2` to the closest possible value.
- The optimization technique learned is to use a greedy approach to find the minimum total cost.

**Mistakes to Avoid:**
- A common implementation error is to try to change all elements of `nums1` instead of only the elements that are equal to the corresponding elements in `nums2`.
- An edge case to watch for is when the input arrays are empty.
- A performance pitfall is to use a brute force approach that tries all possible combinations of changing elements in `nums1`.