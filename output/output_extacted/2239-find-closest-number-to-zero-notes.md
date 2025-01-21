## Find Closest Number to Zero

**Problem Link:** https://leetcode.com/problems/find-closest-number-to-zero/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Output: The number in `nums` that is closest to zero. If there are multiple answers, return the one with the largest absolute value.
- Key requirements and edge cases:
  - The input array is not empty.
  - The array can contain positive, negative, and zero integers.
- Example test cases:
  - Input: `nums = [10, -10, 5, 0]`, Output: `0`
  - Input: `nums = [0, 0, 0]`, Output: `0`
  - Input: `nums = [5, 10, 20]`, Output: `5`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to compare each number in the array with zero and find the one with the smallest absolute difference.
- Step-by-step breakdown:
  1. Initialize a variable `closest` to store the number closest to zero and `minDiff` to store the minimum difference.
  2. Iterate through the array and for each number, calculate its absolute difference with zero.
  3. If the current difference is less than `minDiff`, update `minDiff` and `closest`.
  4. If the current difference equals `minDiff` but the current number has a larger absolute value, update `closest`.
- Why this approach comes to mind first: It directly addresses the problem by comparing each number to zero.

```cpp
int findClosestNumber(vector<int>& nums) {
    int closest = nums[0];
    int minDiff = abs(nums[0]);
    for (int i = 1; i < nums.size(); i++) {
        int diff = abs(nums[i]);
        if (diff < minDiff) {
            minDiff = diff;
            closest = nums[i];
        } else if (diff == minDiff && abs(nums[i]) > abs(closest)) {
            closest = nums[i];
        }
    }
    return closest;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store `closest` and `minDiff`.
> - **Why these complexities occur:** The time complexity is linear due to the iteration through the array, and the space complexity is constant because we use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal solution is essentially the same as the brute force approach because we must examine each number in the array at least once to determine which one is closest to zero.
- Detailed breakdown:
  1. Initialize variables to track the closest number and its distance to zero.
  2. Iterate through the array, updating the closest number based on the minimum distance to zero and, in case of a tie, the maximum absolute value.
- Proof of optimality: This approach is optimal because it only requires a single pass through the data and uses a minimal amount of extra memory, making it both time and space efficient.

```cpp
int findClosestNumber(vector<int>& nums) {
    int closest = nums[0];
    for (int num : nums) {
        if (abs(num) < abs(closest)) {
            closest = num;
        } else if (abs(num) == abs(closest) && num > closest) {
            closest = num;
        }
    }
    return closest;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store `closest`.
> - **Optimality proof:** This is optimal because we must examine each element at least once, and we do so in linear time with constant extra space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concept: The need to examine each element in the array at least once to find the closest number to zero.
- Problem-solving pattern: Iterating through an array to find a specific element based on certain conditions.
- Optimization technique: Using a single pass through the data and minimal extra memory.

**Mistakes to Avoid:**
- Not considering the case where multiple numbers have the same minimum distance to zero but different absolute values.
- Not initializing the `closest` variable correctly before the iteration.
- Assuming a more complex algorithm is needed when a simple iteration suffices.