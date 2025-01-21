## Smallest Missing Integer Greater Than Sequential Prefix Sum

**Problem Link:** https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Expected output: The smallest integer `k` greater than the sequential prefix sum of `nums` that is not in the array.
- Key requirements and edge cases to consider: The array can contain negative numbers, and the prefix sum can be negative. The smallest missing integer should be greater than the prefix sum.
- Example test cases:
  - Input: `nums = [3, 4]`
    - Output: `2`
    - Explanation: The prefix sum is `3`, so the smallest missing integer greater than the prefix sum is `2`.
  - Input: `nums = [1, 2, 0]`
    - Output: `3`
    - Explanation: The prefix sum is `3`, so the smallest missing integer greater than the prefix sum is `3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the prefix sum of the array and then iterate through all integers starting from the prefix sum plus one until we find a missing integer.
- Step-by-step breakdown of the solution:
  1. Calculate the prefix sum of the array.
  2. Initialize a variable `k` to the prefix sum plus one.
  3. Iterate through all integers starting from `k` until we find a missing integer.
- Why this approach comes to mind first: It is a straightforward approach that checks every possible integer until it finds a missing one.

```cpp
int findSmallestInteger(vector<int>& nums) {
    int prefixSum = 0;
    for (int num : nums) {
        prefixSum += num;
    }
    int k = prefixSum + 1;
    while (true) {
        bool found = false;
        for (int num : nums) {
            if (num == k) {
                found = true;
                break;
            }
        }
        if (!found) {
            return k;
        }
        k++;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the size of the input array and $k$ is the smallest missing integer greater than the prefix sum. This is because in the worst case, we need to iterate through all integers starting from the prefix sum plus one until we find a missing integer.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the prefix sum and the variable `k`.
> - **Why these complexities occur:** The time complexity occurs because we need to iterate through all integers starting from the prefix sum plus one until we find a missing integer. The space complexity is constant because we only use a fixed amount of space to store the prefix sum and the variable `k`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `set` to store the elements of the array and then iterate through all integers starting from the prefix sum plus one until we find a missing integer.
- Detailed breakdown of the approach:
  1. Calculate the prefix sum of the array.
  2. Create a `set` to store the elements of the array.
  3. Initialize a variable `k` to the prefix sum plus one.
  4. Iterate through all integers starting from `k` until we find a missing integer.
- Proof of optimality: This approach is optimal because it uses a `set` to store the elements of the array, which allows us to check if an integer is in the array in constant time. This reduces the time complexity from $O(n \cdot k)$ to $O(n + k)$.

```cpp
int findSmallestInteger(vector<int>& nums) {
    int prefixSum = 0;
    for (int num : nums) {
        prefixSum += num;
    }
    set<int> numSet(nums.begin(), nums.end());
    int k = prefixSum + 1;
    while (true) {
        if (numSet.find(k) == numSet.end()) {
            return k;
        }
        k++;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + k)$, where $n$ is the size of the input array and $k$ is the smallest missing integer greater than the prefix sum. This is because we need to iterate through all integers starting from the prefix sum plus one until we find a missing integer.
> - **Space Complexity:** $O(n)$, as we use a `set` to store the elements of the array.
> - **Optimality proof:** This approach is optimal because it uses a `set` to store the elements of the array, which allows us to check if an integer is in the array in constant time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `set` to store elements of an array and iterating through all integers starting from a given value until we find a missing integer.
- Problem-solving patterns identified: Using a `set` to reduce the time complexity of checking if an integer is in an array.
- Optimization techniques learned: Using a `set` to store elements of an array and iterating through all integers starting from a given value until we find a missing integer.
- Similar problems to practice: Finding the smallest missing integer in an array, finding the largest integer in an array that is less than a given value.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if an integer is in the array before incrementing the variable `k`.
- Edge cases to watch for: The array can contain negative numbers, and the prefix sum can be negative.
- Performance pitfalls: Not using a `set` to store the elements of the array, which can lead to a high time complexity.
- Testing considerations: Testing the function with different input arrays, including arrays with negative numbers and arrays with a large range of values.