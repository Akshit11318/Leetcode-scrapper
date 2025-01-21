## Maximum Sized Array
**Problem Link:** https://leetcode.com/problems/maximum-sized-array/description

**Problem Statement:**
- Given an integer `m` and an array of integers `nums`, find the maximum size of a subarray that sums to `m`. 
- Input format: `int m` and `int[] nums`.
- Constraints: `1 <= nums.length <= 10^5` and `-10^5 <= nums[i] <= 10^5`.
- Expected output format: The maximum size of a subarray that sums to `m`.
- Key requirements: Handle edge cases such as an empty array or no subarray summing to `m`.
- Example test cases: 
    - Input: `m = 7`, `nums = [2,3,1,2,4,3]`
      Output: `2` because `[4,3]` is the largest subarray with sum `7`.
    - Input: `m = 4`, `nums = [1,4,4]`
      Output: `3` because `[4,4]` is not a valid subarray, but `[1,4]` (or `[4,1]`) and `[4]` are, and `[1,4,4]` has the largest size with sum not `4`, but no subarray sums to `4` with size larger than `1`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking every possible subarray of `nums` to see if its sum equals `m`.
- This approach involves nested loops to generate all subarrays and then sum each one to compare with `m`.
- Why this approach comes to mind first: It's straightforward and ensures we don't miss any subarray.

```cpp
int maxSubArrayLen(int m, vector<int>& nums) {
    int maxLen = 0;
    for (int i = 0; i < nums.size(); i++) {
        int sum = 0;
        for (int j = i; j < nums.size(); j++) {
            sum += nums[j];
            if (sum == m) {
                maxLen = max(maxLen, j - i + 1);
            }
        }
    }
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of `nums`, because for each element, we potentially scan the rest of the array.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input, because we only use a constant amount of space to store the maximum length and the sum of the current subarray.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity, and the constant space usage is due to only keeping track of a few variables.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a `unordered_map` to store the cumulative sum of the array elements as we iterate through the array. The map will store the sum of elements from the start of the array to the current index and the index itself.
- We then check if the difference between the current cumulative sum and `m` exists in the map. If it does, it means we've found a subarray that sums to `m`, and we update our maximum length accordingly.
- This approach allows us to find the maximum sized subarray in a single pass through the array.

```cpp
int maxSubArrayLen(int m, vector<int>& nums) {
    unordered_map<int, int> sumIndexMap;
    sumIndexMap[0] = -1; // Base case for when the sum itself equals m
    int cumulativeSum = 0;
    int maxLen = 0;
    for (int i = 0; i < nums.size(); i++) {
        cumulativeSum += nums[i];
        if (sumIndexMap.find(cumulativeSum - m) != sumIndexMap.end()) {
            maxLen = max(maxLen, i - sumIndexMap[cumulativeSum - m]);
        }
        if (sumIndexMap.find(cumulativeSum) == sumIndexMap.end()) {
            sumIndexMap[cumulativeSum] = i;
        }
    }
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of `nums`, because we make a single pass through the array.
> - **Space Complexity:** $O(n)$, because in the worst case, we might store every cumulative sum in the map.
> - **Optimality proof:** This is optimal because we must at least look at each element once to determine if it's part of a subarray that sums to `m`, and this approach does so in linear time.

---

### Final Notes

**Learning Points:**
- The importance of using a `unordered_map` for storing and quickly looking up cumulative sums.
- The technique of using a single pass through the data to find subarrays with specific properties.
- Optimization techniques such as avoiding redundant calculations and using data structures for efficient lookup.

**Mistakes to Avoid:**
- Not considering edge cases such as an empty input array or no subarray summing to the target.
- Not optimizing the solution, leading to inefficient algorithms for large inputs.
- Forgetting to handle cases where the sum itself equals the target `m`, as seen in the base case for the `unordered_map`.