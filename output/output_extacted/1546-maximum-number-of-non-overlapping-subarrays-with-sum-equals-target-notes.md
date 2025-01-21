## Maximum Number of Non-Overlapping Subarrays with Sum Equals Target

**Problem Link:** https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/description

**Problem Statement:**
- Input: An integer array `nums` and an integer `target`.
- Expected output: The maximum number of non-overlapping subarrays that sum to `target`.
- Key requirements: 
  - A subarray is non-overlapping if it does not share any elements with another subarray.
  - The sum of each subarray must equal `target`.
- Edge cases: 
  - Empty array.
  - No subarray sums to `target`.
  - All subarrays overlap.

**Example Test Cases:**
- `nums = [1,1,1,1,1], target = 5` returns `1` because the only non-overlapping subarray is the entire array.
- `nums = [1,3,2,1,3,2,1,2,1,1], target = 5` returns `3` because there are three non-overlapping subarrays that sum to `5`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible subarray to see if its sum equals `target`.
- We then try to find non-overlapping subarrays among these.
- This approach comes to mind first because it involves a straightforward application of the problem's requirements.

```cpp
int maxNonOverlapping(vector<int>& nums, int target) {
    int count = 0;
    int lastEnd = -1; // Last end index of a subarray that sums to target
    for (int i = 0; i < nums.size(); i++) {
        int sum = 0;
        for (int j = i; j < nums.size(); j++) {
            sum += nums[j];
            if (sum == target && j > lastEnd) {
                count++;
                lastEnd = j;
                break;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in `nums`, because we have a nested loop structure checking every possible subarray.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store our variables.
> - **Why these complexities occur:** The time complexity is quadratic due to the nested loops, while the space complexity is constant because we do not use any data structures that scale with input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a prefix sum array and a hashmap to store the cumulative sum and its index.
- We then iterate through the array, updating the cumulative sum and checking if the difference between the current cumulative sum and `target` exists in the hashmap.
- If it does, we update our count of non-overlapping subarrays and remove the previous subarray from consideration.
- This approach is optimal because it allows us to find all non-overlapping subarrays that sum to `target` in a single pass through the array.

```cpp
int maxNonOverlapping(vector<int>& nums, int target) {
    unordered_map<int, int> prefixSumIndex;
    prefixSumIndex[0] = -1; // Base case for prefix sum 0
    int cumulativeSum = 0;
    int lastEnd = -1; // Last end index of a subarray that sums to target
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        cumulativeSum += nums[i];
        if (prefixSumIndex.find(cumulativeSum - target) != prefixSumIndex.end() && prefixSumIndex[cumulativeSum - target] > lastEnd) {
            count++;
            lastEnd = i;
        }
        if (prefixSumIndex.find(cumulativeSum) == prefixSumIndex.end()) {
            prefixSumIndex[cumulativeSum] = i;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in `nums`, because we make a single pass through the array.
> - **Space Complexity:** $O(n)$, because in the worst case, we might store every prefix sum in the hashmap.
> - **Optimality proof:** This is the best possible time complexity because we must at least read the input once. The space complexity is also optimal because we need to store the prefix sums to efficiently find non-overlapping subarrays.

---

### Final Notes

**Learning Points:**
- The importance of using prefix sums and hashmaps to solve problems involving cumulative sums and subarrays.
- How to optimize a brute force solution by reducing unnecessary computations and using more efficient data structures.
- The trade-off between time and space complexity in algorithm design.

**Mistakes to Avoid:**
- Failing to consider edge cases, such as an empty input array or no subarrays that sum to the target.
- Not validating inputs, such as checking for null or invalid input arrays.
- Not optimizing the solution for performance, leading to slow or inefficient code.