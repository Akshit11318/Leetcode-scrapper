## Move Zeroes

**Problem Link:** https://leetcode.com/problems/move-zeroes/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: `0 <= nums.length <= 10^4`, `-2^31 <= nums[i] <= 2^31 - 1`.
- Expected output format: The input array `nums` modified in-place such that all non-zero elements are moved to the front of the array in the order they appear, and all zeroes are moved to the end.
- Key requirements and edge cases to consider: The input array can contain duplicate elements, and the order of non-zero elements must be preserved.
- Example test cases with explanations:
  - Example 1: `nums = [0,1,0,3,12]`. After moving zeroes to the end, the array becomes `[1,3,12,0,0]`.
  - Example 2: `nums = [4,2,4,0,0,3,0,5,1,0]`. After moving zeroes to the end, the array becomes `[4,2,4,3,5,1,0,0,0,0]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One of the simplest approaches to solve this problem is to iterate through the array and remove every zero, appending it to the end of the array after all non-zero elements have been processed. However, this would involve shifting elements in the array for each zero found, which is inefficient.
- Step-by-step breakdown of the solution: 
  1. Create a copy of the original array to preserve its contents.
  2. Initialize two pointers, one at the beginning of the array and one at the beginning of the copy.
  3. Iterate through the array, copying non-zero elements to the copy.
  4. Fill the rest of the copy with zeroes.
  5. Copy the modified copy back to the original array.
- Why this approach comes to mind first: It's a straightforward approach that directly addresses the requirement of moving zeroes to the end while preserving the order of non-zero elements.

```cpp
void moveZeroes(vector<int>& nums) {
    vector<int> copy = nums;
    int j = 0; // Pointer for non-zero elements
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] != 0) {
            copy[j++] = nums[i];
        }
    }
    // Fill the rest with zeroes
    for (; j < nums.size(); j++) {
        copy[j] = 0;
    }
    // Copy back to original array
    nums = copy;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of elements in the array, because we are doing a constant amount of work for each element.
> - **Space Complexity:** $O(n)$ because we are creating a copy of the input array.
> - **Why these complexities occur:** The time complexity is linear because we are iterating through the array once. The space complexity is also linear because we are creating a copy of the entire array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of creating a copy of the array, we can use two pointers to track the position of the next non-zero element and the current element being processed. This way, we can move non-zero elements to the front of the array in-place.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `j` for the next non-zero position and `i` for the current element.
  2. Iterate through the array with `i`. When a non-zero element is found, swap it with the element at the `j` position and increment `j`.
- Proof of optimality: This approach is optimal because it only requires a single pass through the array and uses a constant amount of extra space (for the pointers), resulting in a time complexity of $O(n)$ and a space complexity of $O(1)$.
- Why further optimization is impossible: Given that we must examine each element at least once to determine if it is zero or not, the time complexity cannot be improved beyond $O(n)$.

```cpp
void moveZeroes(vector<int>& nums) {
    int j = 0; // Pointer for the next non-zero position
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] != 0) {
            swap(nums[j], nums[i]);
            j++;
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of elements in the array, because we are doing a constant amount of work for each element.
> - **Space Complexity:** $O(1)$ because we are only using a constant amount of space to store the pointers.
> - **Optimality proof:** This is the most efficient solution because it minimizes both time and space complexity by only requiring a single pass through the array and using a constant amount of extra space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, in-place modification, and optimization of space complexity.
- Problem-solving patterns identified: The importance of considering both time and space complexity when evaluating the efficiency of a solution.
- Optimization techniques learned: Reducing space complexity by avoiding unnecessary data structures and using pointers instead.
- Similar problems to practice: Other array manipulation problems that require in-place modification or efficient use of space.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases (e.g., an array with all zeroes or all non-zeroes), or incorrectly implementing the swap operation.
- Edge cases to watch for: Empty arrays, arrays with a single element, and arrays with duplicate elements.
- Performance pitfalls: Using inefficient algorithms or data structures that lead to high time or space complexity.
- Testing considerations: Thoroughly testing the solution with a variety of input cases, including edge cases, to ensure correctness and efficiency.