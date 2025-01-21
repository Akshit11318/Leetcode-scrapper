## Rotate Array

**Problem Link:** https://leetcode.com/problems/rotate-array/description

**Problem Statement:**
- Input: An array `nums` of integers and an integer `k`.
- Constraints: $1 \leq nums.length \leq 2 \times 10^4$, $-2^{31} \leq nums[i] \leq 2^{31} - 1$, $0 \leq k \leq 10^5$.
- Expected output: Rotate the array to the right by `k` steps.
- Key requirements: Modify the array in-place, handle cases where `k` is greater than the length of the array.
- Example test cases:
  - Input: `nums = [1,2,3,4,5,6,7]`, `k = 3`.
    - Output: `[5,6,7,1,2,3,4]`.
  - Input: `nums = [-1,-100,3,99]`, `k = 2`.
    - Output: `[3,99,-1,-100]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One straightforward way to rotate the array is to shift each element one position to the right `k` times.
- Step-by-step breakdown of the solution:
  1. Loop through the array `k` times.
  2. In each iteration, save the last element of the array.
  3. Shift all elements one position to the right.
  4. Place the saved last element at the beginning of the array.
- Why this approach comes to mind first: It directly implements the concept of rotating the array by moving elements.

```cpp
void rotate(vector<int>& nums, int k) {
    k %= nums.size(); // To handle cases where k is greater than nums.size()
    for (int i = 0; i < k; i++) {
        int temp = nums[nums.size() - 1];
        for (int j = nums.size() - 1; j > 0; j--) {
            nums[j] = nums[j - 1];
        }
        nums[0] = temp;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the number of elements in the array. This is because in the worst case, we are shifting all elements $k$ times.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array. We only use a constant amount of space to store the temporary variable.
> - **Why these complexities occur:** The time complexity is high because we are performing a significant number of operations (shifting elements) for each rotation step. The space complexity is low because we only use a small, constant amount of extra space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of rotating the array `k` times, we can achieve the same result by reversing the entire array and then reversing the first `k` elements and the rest of the array separately.
- Detailed breakdown of the approach:
  1. Reverse the entire array.
  2. Reverse the first `k` elements of the reversed array.
  3. Reverse the rest of the array (from index `k` to the end).
- Proof of optimality: This approach reduces the number of operations significantly, especially when `k` is large, because reversing the array can be done more efficiently than shifting elements one by one.

```cpp
void rotate(vector<int>& nums, int k) {
    k %= nums.size(); // To handle cases where k is greater than nums.size()
    reverse(nums.begin(), nums.end()); // Reverse the entire array
    reverse(nums.begin(), nums.begin() + k); // Reverse the first k elements
    reverse(nums.begin() + k, nums.end()); // Reverse the rest of the array
}

void reverse(vector<int>::iterator start, vector<int>::iterator end) {
    while (start < end - 1) {
        swap(*start, *(end - 1));
        start++;
        end--;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because reversing the array (or parts of it) takes linear time.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array. We only use a constant amount of space for the function call stack and temporary swaps.
> - **Optimality proof:** This is optimal because we perform a constant amount of work for each element in the array, and we do this only once, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Array rotation, reversal, and the importance of reducing the number of operations to achieve optimality.
- Problem-solving patterns identified: Looking for alternative representations of the problem (e.g., reversing instead of shifting) can lead to more efficient solutions.
- Optimization techniques learned: Reducing the number of operations by finding a more efficient algorithm (reversal instead of multiple shifts).

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where `k` is greater than the array length, not using the most efficient algorithm for array reversal.
- Edge cases to watch for: Empty array, `k` equals the array length, `k` is greater than the array length.
- Performance pitfalls: Using a brute force approach that shifts elements one by one, which can be very slow for large arrays or large `k`.