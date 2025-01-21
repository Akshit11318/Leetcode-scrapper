## Minimum Array End

**Problem Link:** [https://leetcode.com/problems/minimum-array-end/description](https://leetcode.com/problems/minimum-array-end/description)

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 10^5`.
- Expected output format: The minimum possible value of `nums[0]`.
- Key requirements: Find the minimum possible value of `nums[0]` after performing operations where you can either increment `nums[i]` by 1, or decrement `nums[i+1]` by 1, for `i` in range `[0, nums.length - 1]`.
- Example test cases:
  - Input: `nums = [2,3,1,2]`, Output: `2`
  - Input: `nums = [1,2,3,2]`, Output: `1`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to consider all possible operations and find the minimum value of `nums[0]`.
- However, this approach quickly becomes infeasible due to the large number of possible operations.
- We can start by trying to decrement `nums[i+1]` as much as possible and then increment `nums[i]` to minimize `nums[0]`.

```cpp
int minElements(vector<int>& nums) {
    int n = nums.size();
    int res = nums[0];
    for (int i = 1; i < n; i++) {
        res = min(res, nums[i] + i);
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `nums`, because we are scanning the array once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space.
> - **Why these complexities occur:** The time complexity is linear because we are iterating over the array, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to realize that we can always decrement `nums[i+1]` by 1 to minimize `nums[i]`.
- We can start from the end of the array and work our way backwards, keeping track of the minimum value of `nums[i] + i`.
- This approach is optimal because we are considering all possible operations and finding the minimum value of `nums[0]`.

```cpp
int minElements(vector<int>& nums) {
    int n = nums.size();
    int res = nums[n - 1];
    for (int i = n - 2; i >= 0; i--) {
        res = min(res, nums[i] + n - 1 - i);
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `nums`, because we are scanning the array once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space.
> - **Optimality proof:** This approach is optimal because we are considering all possible operations and finding the minimum value of `nums[0]`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: `minElements` problem, scanning the array, and keeping track of the minimum value.
- Problem-solving patterns identified: considering all possible operations and finding the minimum value.
- Optimization techniques learned: using a constant amount of space and scanning the array once.
- Similar problems to practice: `minElements` problem, `maxElements` problem.

**Mistakes to Avoid:**
- Common implementation errors: not considering all possible operations, not keeping track of the minimum value.
- Edge cases to watch for: empty array, array with one element.
- Performance pitfalls: using more than a constant amount of space, scanning the array more than once.
- Testing considerations: testing with different input sizes, testing with different input values.