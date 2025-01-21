## Partition Array into Disjoint Intervals
**Problem Link:** https://leetcode.com/problems/partition-array-into-disjoint-intervals/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: The length of `nums` is in the range $[1, 10^5]$.
- Expected Output: An integer representing the partition index.
- Key Requirements: Find the smallest index `k` such that all elements in the left partition are less than all elements in the right partition.
- Edge Cases: Consider arrays with single elements, duplicate elements, and elements in strictly increasing or decreasing order.

**Example Test Cases:**
- For the input `[5,0,3,8,6]`, the output should be `3` because the left partition `[5,0,3]` is less than the right partition `[8,6]`.
- For the input `[1,1,1,0,6,12]`, the output should be `4` because the left partition `[1,1,1,0]` is less than the right partition `[6,12]`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking every possible partition index `k` and verifying if all elements in the left partition are less than all elements in the right partition.
- This approach involves nested loops: one for iterating over possible partition indices and another for comparing elements across the partition.

```cpp
class Solution {
public:
    int partitionDisjoint(vector<int>& nums) {
        int n = nums.size();
        for (int k = 1; k < n; k++) {
            bool validPartition = true;
            for (int i = 0; i < k; i++) {
                for (int j = k; j < n; j++) {
                    if (nums[i] > nums[j]) {
                        validPartition = false;
                        break;
                    }
                }
                if (!validPartition) break;
            }
            if (validPartition) return k;
        }
        return n; // Default return if no valid partition is found
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ because for each potential partition index $k$, we are comparing every element in the left partition with every element in the right partition.
> - **Space Complexity:** $O(1)$ because we are using a constant amount of space to store the partition index and other variables.
> - **Why these complexities occur:** The brute force approach involves nested loops that grow with the size of the input array, leading to high time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to maintain two arrays: one for the maximum value seen so far from the left (`leftMax`) and one for the minimum value seen so far from the right (`rightMin`).
- We iterate through the array once to populate `leftMax` and `rightMin`.
- Then, we find the first index where the `leftMax` is less than the `rightMin`, which represents the smallest index `k` that satisfies the partition condition.

```cpp
class Solution {
public:
    int partitionDisjoint(vector<int>& nums) {
        int n = nums.size();
        vector<int> leftMax(n, 0);
        vector<int> rightMin(n, 0);
        
        leftMax[0] = nums[0];
        for (int i = 1; i < n; i++) {
            leftMax[i] = max(leftMax[i-1], nums[i]);
        }
        
        rightMin[n-1] = nums[n-1];
        for (int i = n-2; i >= 0; i--) {
            rightMin[i] = min(rightMin[i+1], nums[i]);
        }
        
        for (int k = 1; k < n; k++) {
            if (leftMax[k-1] <= rightMin[k]) {
                return k;
            }
        }
        return n; // Default return if no valid partition is found
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we are iterating through the array twice: once to populate `leftMax` and once to populate `rightMin`, and then a final pass to find the partition index.
> - **Space Complexity:** $O(n)$ because we are using two arrays of the same size as the input array to store `leftMax` and `rightMin`.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the data to populate the auxiliary arrays and then a simple comparison to find the partition index, minimizing both time and space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated include the use of auxiliary arrays to track maximum and minimum values and the application of a single pass through the data to achieve optimal time complexity.
- Problem-solving patterns identified include breaking down the problem into smaller, manageable parts (finding `leftMax` and `rightMin`) and then combining these parts to solve the original problem.
- Optimization techniques learned include minimizing the number of passes through the data and using auxiliary arrays to avoid redundant computations.

**Mistakes to Avoid:**
- Common implementation errors include incorrect initialization of `leftMax` and `rightMin` arrays and failure to handle edge cases properly.
- Edge cases to watch for include arrays with single elements, duplicate elements, and elements in strictly increasing or decreasing order.
- Performance pitfalls include using nested loops that grow with the size of the input array, leading to high time complexity.