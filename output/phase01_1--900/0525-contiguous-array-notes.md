## Contiguous Array
**Problem Link:** https://leetcode.com/problems/contiguous-array/description

**Problem Statement:**
- Given an array of integers `nums` containing `0`s and `1`s, find the maximum length of a contiguous subarray that has an equal number of `0`s and `1`s.
- Input format: An array of integers `nums`.
- Expected output format: The maximum length of a contiguous subarray with an equal number of `0`s and `1`s.
- Key requirements and edge cases to consider:
  - Handle empty arrays.
  - Consider arrays with no contiguous subarrays having an equal number of `0`s and `1`s.
- Example test cases:
  - `nums = [0,1]`: The maximum length is `2`.
  - `nums = [0,1,0]`: The maximum length is `2`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible subarray to see if it has an equal number of `0`s and `1`s.
- Step-by-step breakdown:
  1. Generate all possible subarrays.
  2. For each subarray, count the number of `0`s and `1`s.
  3. If the counts are equal, update the maximum length found so far.
- Why this approach comes to mind first: It's a straightforward, intuitive method that ensures we don't miss any potential subarrays.

```cpp
class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int maxLen = 0;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i; j < nums.size(); j++) {
                int zeros = 0, ones = 0;
                for (int k = i; k <= j; k++) {
                    if (nums[k] == 0) zeros++;
                    else ones++;
                }
                if (zeros == ones) maxLen = max(maxLen, j - i + 1);
            }
        }
        return maxLen;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of elements in `nums`. This is because we have three nested loops: one for generating subarrays and two for counting `0`s and `1`s within each subarray.
> - **Space Complexity:** $O(1)$, not including the space needed for the input array. This is because we only use a constant amount of space to store our variables.
> - **Why these complexities occur:** The brute force approach is inherently inefficient due to its exhaustive nature, leading to high time complexity. However, it uses minimal extra space, keeping space complexity low.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of counting `0`s and `1`s separately for each subarray, we can use a single pass through the array and keep track of the difference between the counts of `0`s and `1`s encountered so far.
- Detailed breakdown:
  1. Initialize a hashmap to store the difference between `0`s and `1`s encountered so far and its corresponding index.
  2. Initialize variables to keep track of the maximum length and the current difference.
  3. Iterate through the array, updating the current difference based on whether we encounter a `0` or a `1`.
  4. If the current difference is `0`, it means we have an equal number of `0`s and `1`s from the start of the array to the current position. Update the maximum length if necessary.
  5. If the current difference is already in the hashmap, it means we've found a subarray with an equal number of `0`s and `1`s starting from the index after the one stored in the hashmap for this difference. Update the maximum length if necessary.
- Proof of optimality: This approach is optimal because it only requires a single pass through the array, resulting in linear time complexity, and it uses extra space to store the hashmap, which is necessary for efficient lookups.

```cpp
class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        unordered_map<int, int> diffIndexMap;
        int maxLen = 0, diff = 0;
        diffIndexMap[0] = -1; // Base case for when the difference is 0
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) diff--;
            else diff++;
            if (diffIndexMap.find(diff) != diffIndexMap.end()) {
                maxLen = max(maxLen, i - diffIndexMap[diff]);
            } else {
                diffIndexMap[diff] = i;
            }
        }
        return maxLen;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in `nums`. This is because we make a single pass through the array.
> - **Space Complexity:** $O(n)$, for storing the hashmap in the worst case when all differences are unique.
> - **Optimality proof:** This approach is optimal because it achieves linear time complexity, which is the best we can do for this problem since we must at least read the input once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a hashmap for efficient lookups, reducing time complexity by avoiding redundant calculations.
- Problem-solving patterns identified: Looking for ways to reduce the problem to a single pass through the data, using extra space to improve time complexity.
- Optimization techniques learned: Avoiding nested loops, using hashmaps for fast lookups.
- Similar problems to practice: Other problems involving finding maximum lengths or counts within arrays or strings.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases (like an empty array), not initializing variables correctly.
- Edge cases to watch for: Empty arrays, arrays with no contiguous subarrays having an equal number of `0`s and `1`s.
- Performance pitfalls: Using brute force approaches for large inputs, not considering the use of extra space to improve time complexity.
- Testing considerations: Test with arrays of varying sizes, including edge cases like empty arrays or arrays with a single element.