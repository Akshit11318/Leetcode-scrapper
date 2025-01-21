## Shuffle the Array
**Problem Link:** https://leetcode.com/problems/shuffle-the-array/description

**Problem Statement:**
- Input: An array `nums` of size `2n` and an integer `n`.
- Constraints: `1 <= n <= 10^4`, `nums.length == 2n`.
- Expected output: An array of size `2n` where the elements at the first `n` indices are shuffled with the elements at the last `n` indices.
- Key requirements and edge cases to consider: Ensure that the resulting array has the same elements as the original array but with the first `n` elements shuffled with the last `n` elements.
- Example test cases with explanations:
  - Example 1: Input: `nums = [1,2,3,4,4,3,2,1], n = 4`, Output: `[1,4,2,3,3,2,4,1]`
  - Example 2: Input: `nums = [1,1,2,2], n = 2`, Output: `[1,2,1,2]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To shuffle the array, we can use two pointers, one at the start and one at the middle of the array, and then interleave the elements.
- Step-by-step breakdown of the solution:
  1. Create a new array to store the shuffled elements.
  2. Initialize two pointers, one at the start and one at the middle of the array.
  3. Interleave the elements from the start and middle pointers into the new array.
- Why this approach comes to mind first: It's a straightforward approach that directly addresses the problem statement.

```cpp
vector<int> shuffle(vector<int>& nums, int n) {
    vector<int> result;
    for (int i = 0; i < n; i++) {
        result.push_back(nums[i]);
        result.push_back(nums[i + n]);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements to shuffle. This is because we are iterating over the array once.
> - **Space Complexity:** $O(n)$, as we are creating a new array to store the shuffled elements.
> - **Why these complexities occur:** The time complexity is linear because we are performing a constant amount of work for each element in the array. The space complexity is also linear because we need to store the shuffled elements in a new array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal because we need to visit each element in the array at least once to shuffle it.
- Detailed breakdown of the approach: The same approach as the brute force solution.
- Proof of optimality: Since we need to visit each element in the array at least once, the time complexity cannot be better than $O(n)$.
- Why further optimization is impossible: We cannot avoid visiting each element in the array, so the time complexity is already optimal.

```cpp
vector<int> shuffle(vector<int>& nums, int n) {
    vector<int> result;
    for (int i = 0; i < n; i++) {
        result.push_back(nums[i]);
        result.push_back(nums[i + n]);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements to shuffle.
> - **Space Complexity:** $O(n)$, as we are creating a new array to store the shuffled elements.
> - **Optimality proof:** The time complexity is optimal because we need to visit each element in the array at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Interleaving elements from two arrays.
- Problem-solving patterns identified: Creating a new array to store the result.
- Optimization techniques learned: Avoiding unnecessary operations by directly interleaving elements.
- Similar problems to practice: Other array manipulation problems, such as reversing an array or finding the first duplicate.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the bounds of the array.
- Edge cases to watch for: Handling arrays with duplicate elements.
- Performance pitfalls: Using unnecessary operations or data structures.
- Testing considerations: Testing with arrays of different sizes and contents.