## Count Number of Special Subsequences

**Problem Link:** https://leetcode.com/problems/count-number-of-special-subsequences/description

**Problem Statement:**
- Input format: You are given a binary array `nums`.
- Constraints: `1 <= nums.length <= 10^5`.
- Expected output format: The number of special subsequences in the array.
- Key requirements: A special subsequence is a subsequence that contains at least one `0` and at least one `1`.
- Example test cases:
  - Input: `nums = [1,1,1,0,0]`
    - Output: `8`
    - Explanation: There are 8 special subsequences: `[0,1]`, `[0,1,1]`, `[0,1,1,1]`, `[0,1,1,1,1]`, `[0,0,1]`, `[0,0,1,1]`, `[0,0,1,1,1]`, and `[0,0,0,1]`.
  - Input: `nums = [0,1,0,1,0,1]`
    - Output: `16`
    - Explanation: There are 16 special subsequences.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find all possible subsequences and check each one for at least one `0` and one `1`.
- Step-by-step breakdown:
  1. Generate all possible subsequences of the input array.
  2. For each subsequence, check if it contains at least one `0` and one `1`.
  3. If it does, increment the count of special subsequences.

```cpp
int countSpecialSubsequences(vector<int>& nums) {
    int n = nums.size();
    int count = 0;
    // Generate all possible subsequences
    for (int mask = 1; mask < (1 << n); mask++) {
        bool hasZero = false;
        bool hasOne = false;
        // Check each element in the subsequence
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                if (nums[i] == 0) hasZero = true;
                if (nums[i] == 1) hasOne = true;
            }
        }
        // If the subsequence contains at least one 0 and one 1, increment count
        if (hasZero && hasOne) count++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input array. The reason for this complexity is that we generate all possible subsequences (of which there are $2^n$) and for each subsequence, we potentially check all elements (up to $n$ checks).
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output. This is because we only use a constant amount of space to store our variables.
> - **Why these complexities occur:** The brute force approach involves generating all possible subsequences and checking each one, which leads to exponential time complexity due to the number of subsequences and linear time complexity for checking each subsequence.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of generating all subsequences, we can use dynamic programming to keep track of the number of subsequences ending at each position that contain at least one `0` and at least one `1`.
- Detailed breakdown:
  1. Initialize variables to keep track of the number of subsequences ending at each position that contain at least one `0`, at least one `1`, and both.
  2. Iterate through the array, updating these counts based on the current element.
  3. The total count of special subsequences is the sum of the counts of subsequences ending at each position that contain both `0` and `1`.

```cpp
int countSpecialSubsequences(vector<int>& nums) {
    long long count0 = 0, count1 = 0, count01 = 0;
    for (int num : nums) {
        if (num == 0) {
            count0 = count0 * 2 + 1;
            count01 = count01 * 2;
        } else {
            count1 = count1 * 2 + 1;
            count01 = count01 * 2 + count0;
        }
    }
    return count01;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output. This is because we only use a constant amount of space to store our variables.
> - **Optimality proof:** This approach is optimal because it avoids the unnecessary generation of all subsequences and instead uses dynamic programming to efficiently calculate the count of special subsequences. It achieves a linear time complexity, which is the best possible for this problem since we must at least read the input once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Dynamic programming, bit manipulation (in the brute force approach).
- Problem-solving patterns: Breaking down a problem into smaller sub-problems and solving them efficiently.
- Optimization techniques: Avoiding unnecessary work by using dynamic programming to store and reuse the results of sub-problems.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables correctly, not handling edge cases.
- Edge cases to watch for: Empty input array, arrays with only `0`s or only `1`s.
- Performance pitfalls: Using the brute force approach for large inputs.
- Testing considerations: Testing with arrays of varying lengths and compositions to ensure correctness and performance.