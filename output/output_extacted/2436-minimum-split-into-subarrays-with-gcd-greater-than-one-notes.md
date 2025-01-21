## Minimum Split into Subarrays with GCD Greater Than One
**Problem Link:** https://leetcode.com/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 1000`, `1 <= nums[i] <= 1000`.
- Expected Output: The minimum number of subarrays that can be split from `nums` such that each subarray has a GCD greater than 1.
- Key Requirements: Each subarray must have a GCD greater than 1.
- Edge Cases: If the input array is empty, the function should return 0.

### Brute Force Approach
**Explanation:**
- The initial thought process is to generate all possible subarrays from the given array and calculate the GCD of each subarray.
- Then, we count the minimum number of subarrays that satisfy the condition (GCD > 1).
- This approach comes to mind first because it is straightforward and does not require any advanced mathematical insights.

```cpp
class Solution {
public:
    int minimumSplit(vector<int>& nums) {
        int n = nums.size();
        int res = 0;
        int i = 0;
        while (i < n) {
            int j = i;
            bool found = false;
            while (j < n) {
                int gcd = getGCD(nums, i, j);
                if (gcd > 1) {
                    res++;
                    i = j + 1;
                    found = true;
                    break;
                }
                j++;
            }
            if (!found) {
                i++;
                res++;
            }
        }
        return res;
    }
    
    int getGCD(vector<int>& nums, int start, int end) {
        int gcd = nums[start];
        for (int i = start + 1; i <= end; i++) {
            gcd = __gcd(gcd, nums[i]);
        }
        return gcd;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input array. This is because we are generating all possible subarrays and calculating their GCDs.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the nested loops used to generate all possible subarrays and calculate their GCDs.

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is to use a two-pointer technique to efficiently find the minimum number of subarrays with GCD greater than 1.
- We maintain two pointers, `i` and `j`, both starting from the beginning of the array.
- We move `j` to the right until we find a subarray with GCD greater than 1, and then we move `i` to `j + 1`.
- This process continues until we have processed the entire array.

```cpp
class Solution {
public:
    int minimumSplit(vector<int>& nums) {
        int n = nums.size();
        int res = 0;
        int i = 0;
        while (i < n) {
            int gcd = 0;
            for (int j = i; j < n; j++) {
                gcd = __gcd(gcd, nums[j]);
                if (gcd > 1) {
                    res++;
                    i = j + 1;
                    break;
                }
            }
            if (gcd == 1) {
                res++;
                i++;
            }
        }
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array. This is because we are using a two-pointer technique to efficiently find the minimum number of subarrays with GCD greater than 1.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with the input size.
> - **Optimality proof:** The optimal approach has a time complexity of $O(n^2)$, which is the best possible complexity for this problem because we need to consider all possible subarrays.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: two-pointer technique, GCD calculation.
- Problem-solving patterns identified: using a two-pointer technique to efficiently find the minimum number of subarrays with a certain property.
- Optimization techniques learned: reducing the time complexity from $O(n^3)$ to $O(n^2)$ by using a two-pointer technique.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, such as an empty input array.
- Edge cases to watch for: an input array with a single element, an input array with all elements having a GCD of 1.
- Performance pitfalls: using a brute force approach with high time complexity.
- Testing considerations: testing the function with different input arrays, including edge cases.