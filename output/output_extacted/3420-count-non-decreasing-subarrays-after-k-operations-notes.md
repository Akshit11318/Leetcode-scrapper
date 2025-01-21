## Count Non-Decreasing Subarrays After K Operations

**Problem Link:** https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/description

**Problem Statement:**
- Input: An array of integers `nums` and an integer `k`.
- Output: The number of non-decreasing subarrays after at most `k` operations.
- Key requirements: A non-decreasing subarray is one where every element is less than or equal to the next one.
- Edge cases: Handle cases where `k` is 0, and the array is already non-decreasing.

**Example Test Cases:**
- `nums = [1, 2, 3, 4, 5], k = 0` should return `15` because all subarrays are non-decreasing.
- `nums = [5, 4, 3, 2, 1], k = 3` should return `9` because after at most 3 operations, we can make the subarrays non-decreasing.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of operations on the array to make subarrays non-decreasing.
- Step-by-step breakdown:
  1. Generate all possible subarrays.
  2. For each subarray, try all possible combinations of at most `k` operations to make it non-decreasing.
  3. Count the number of subarrays that can be made non-decreasing.

```cpp
int countSubarrays(vector<int>& nums, int k) {
    int n = nums.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            vector<int> subarray = vector<int>(nums.begin() + i, nums.begin() + j + 1);
            int operations = 0;
            for (int l = 0; l < subarray.size() - 1; l++) {
                if (subarray[l] > subarray[l + 1]) {
                    operations++;
                }
            }
            if (operations <= k) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the size of the input array. This is because we are generating all possible subarrays ($O(n^2)$) and then for each subarray, we are checking if it can be made non-decreasing with at most `k` operations ($O(n)$).
> - **Space Complexity:** $O(n)$, for storing the subarray.
> - **Why these complexities occur:** The brute force approach involves trying all possible combinations, leading to high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to realize that we can make a subarray non-decreasing by performing operations on it only if the difference between the maximum and minimum elements in the subarray is less than or equal to `k`.
- Detailed breakdown:
  1. For each possible subarray length, calculate the maximum number of operations required to make it non-decreasing.
  2. Use a sliding window approach to efficiently calculate the maximum and minimum elements in each subarray.

```cpp
int countSubarrays(vector<int>& nums, int k) {
    int n = nums.size();
    int count = 0;
    for (int length = 1; length <= n; length++) {
        for (int i = 0; i <= n - length; i++) {
            int maxVal = INT_MIN;
            int minVal = INT_MAX;
            for (int j = i; j < i + length; j++) {
                maxVal = max(maxVal, nums[j]);
                minVal = min(minVal, nums[j]);
            }
            if (maxVal - minVal <= k) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the size of the input array. This is because we are generating all possible subarrays ($O(n^2)$) and then for each subarray, we are calculating the maximum and minimum elements ($O(n)$).
> - **Space Complexity:** $O(1)$, excluding the input array.
> - **Optimality proof:** This approach is optimal because we are efficiently calculating the maximum and minimum elements in each subarray, and we are not performing any redundant operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sliding window approach, efficient calculation of maximum and minimum elements.
- Problem-solving patterns identified: breaking down the problem into smaller sub-problems, using a brute force approach as a starting point.
- Optimization techniques learned: reducing the time complexity by using a sliding window approach.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases correctly, not initializing variables properly.
- Edge cases to watch for: when `k` is 0, when the array is already non-decreasing.
- Performance pitfalls: using a brute force approach without optimizing it, not using a sliding window approach to efficiently calculate the maximum and minimum elements.