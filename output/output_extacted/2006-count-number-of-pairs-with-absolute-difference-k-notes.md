## Count Number of Pairs with Absolute Difference K
**Problem Link:** https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description

**Problem Statement:**
- Input format and constraints: The problem takes an array of integers `nums` and an integer `k` as input, with the constraint that `1 <= nums.length <= 200` and `1 <= nums[i] <= 200`.
- Expected output format: The function should return the number of pairs of indices `(i, j)` such that `1 <= i < j <= nums.length` and `abs(nums[i] - nums[j]) == k`.
- Key requirements and edge cases to consider: The function should handle arrays with duplicate elements and should be able to count pairs with absolute difference `k` efficiently.
- Example test cases with explanations:
  - Example 1: Input: `nums = [1,2,3,4,5], k = 1`, Output: `4`. Explanation: The pairs with an absolute difference of 1 are: `(1,2)`, `(2,3)`, `(3,4)`, and `(4,5)`.
  - Example 2: Input: `nums = [1,5,3,19,18,25], k = 3`, Output: `2`. Explanation: The pairs with an absolute difference of 3 are: `(1,4)` and `(5,6)`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to iterate over all possible pairs of indices in the array and check if the absolute difference between the elements at those indices is equal to `k`.
- Step-by-step breakdown of the solution:
  1. Initialize a variable to store the count of pairs with an absolute difference of `k`.
  2. Iterate over all possible pairs of indices in the array.
  3. For each pair, calculate the absolute difference between the elements at those indices.
  4. If the absolute difference is equal to `k`, increment the count.
- Why this approach comes to mind first: This approach is intuitive because it directly checks all possible pairs, ensuring that no valid pair is missed.

```cpp
int countKDifference(vector<int>& nums, int k) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (abs(nums[i] - nums[j]) == k) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input array `nums`. This is because we are iterating over all pairs of indices in the array.
> - **Space Complexity:** $O(1)$, as we are only using a constant amount of space to store the count and indices.
> - **Why these complexities occur:** The time complexity is quadratic because we have nested loops that each iterate over the array, and the space complexity is constant because we do not use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since the range of values in `nums` is small (from 1 to 200), we can use a frequency array to count the occurrences of each number. Then, for each number, we check if the number plus `k` or minus `k` exists in the frequency array.
- Detailed breakdown of the approach:
  1. Create a frequency array to store the count of each number in `nums`.
  2. Iterate over `nums` to populate the frequency array.
  3. Initialize a variable to store the count of pairs with an absolute difference of `k`.
  4. Iterate over the frequency array. For each number, check if the number plus `k` or minus `k` exists in the frequency array. If it does, increment the count by the product of their frequencies.
- Proof of optimality: This approach is optimal because it reduces the time complexity from quadratic to linear by avoiding the need to check all pairs of numbers in `nums`.

```cpp
int countKDifference(vector<int>& nums, int k) {
    int freq[201] = {0}; // Assuming nums[i] is in the range [1, 200]
    int count = 0;
    
    for (int num : nums) {
        freq[num]++;
    }
    
    for (int i = 1; i <= 200; i++) {
        if (i + k <= 200) {
            count += freq[i] * freq[i + k];
        }
        if (i - k >= 1 && i - k != i + k) { // Avoid counting pairs twice
            count += freq[i] * freq[i - k];
        }
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of `nums` and $m$ is the range of values in `nums` (200 in this case). This is because we first iterate over `nums` to populate the frequency array and then iterate over the frequency array to count pairs.
> - **Space Complexity:** $O(m)$, for the frequency array.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity to linear with respect to the input size and the range of values, making it much more efficient than the brute force approach for large inputs.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Frequency arrays, optimization of brute force approaches.
- Problem-solving patterns identified: Using auxiliary arrays to store frequencies or other relevant information to reduce time complexity.
- Optimization techniques learned: Reducing quadratic time complexity to linear by avoiding unnecessary comparisons.
- Similar problems to practice: Other problems involving frequency counts or optimization of brute force approaches.

**Mistakes to Avoid:**
- Common implementation errors: Off-by-one errors in array indexing, incorrect handling of edge cases.
- Edge cases to watch for: Empty input arrays, arrays with a single element, arrays with all elements being the same.
- Performance pitfalls: Using brute force approaches for large inputs, not optimizing algorithms when possible.
- Testing considerations: Thoroughly testing with a variety of inputs, including edge cases and large inputs, to ensure correctness and efficiency.