## Non-Decreasing Array
**Problem Link:** [https://leetcode.com/problems/non-decreasing-array/description](https://leetcode.com/problems/non-decreasing-array/description)

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 2000`, `-1000 <= nums[i] <= 1000`.
- Expected output format: A boolean indicating whether the array can be made non-decreasing by changing at most one element.
- Key requirements and edge cases to consider: The array can be modified by changing at most one element to make it non-decreasing.
- Example test cases with explanations:
  - Input: `nums = [4,2,3]`, Output: `true` (Explanation: You can change the 4 to a 1 to make the array non-decreasing).
  - Input: `nums = [4,2,1]`, Output: `false` (Explanation: You cannot make the array non-decreasing by changing at most one element).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible modifications to the array and check if any of them result in a non-decreasing array.
- Step-by-step breakdown of the solution:
  1. Iterate over each element in the array.
  2. For each element, try modifying it to every possible value between the minimum and maximum values in the array.
  3. Check if the modified array is non-decreasing.
  4. If a non-decreasing array is found, return `true`.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to try all possible modifications and check if any of them result in a non-decreasing array.

```cpp
bool checkPossibility(vector<int>& nums) {
    int n = nums.size();
    for (int i = 0; i < n; i++) {
        for (int j = -1000; j <= 1000; j++) {
            vector<int> temp = nums;
            temp[i] = j;
            bool isNonDecreasing = true;
            for (int k = 0; k < n - 1; k++) {
                if (temp[k] > temp[k + 1]) {
                    isNonDecreasing = false;
                    break;
                }
            }
            if (isNonDecreasing) {
                return true;
            }
        }
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 2001 \cdot n)$, where $n$ is the length of the input array. This is because we are iterating over each element in the array, trying each possible modification, and checking if the modified array is non-decreasing.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we are creating a copy of the input array for each modification.
> - **Why these complexities occur:** These complexities occur because we are trying all possible modifications and checking if any of them result in a non-decreasing array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can iterate over the array and check if any element is greater than the next element. If we find such a pair, we can try modifying the current element or the next element to make the array non-decreasing.
- Detailed breakdown of the approach:
  1. Initialize a variable `count` to 0 to keep track of the number of modifications needed.
  2. Iterate over the array and check if any element is greater than the next element.
  3. If we find such a pair, increment `count` and try modifying the current element or the next element to make the array non-decreasing.
  4. If `count` is greater than 1, return `false` because we need more than one modification to make the array non-decreasing.
- Proof of optimality: This approach is optimal because we are only iterating over the array once and trying at most two modifications for each pair of elements that need to be modified.

```cpp
bool checkPossibility(vector<int>& nums) {
    int count = 0;
    for (int i = 0; i < nums.size() - 1; i++) {
        if (nums[i] > nums[i + 1]) {
            count++;
            if (count > 1) {
                return false;
            }
            if (i > 0 && nums[i - 1] > nums[i + 1] && i < nums.size() - 2 && nums[i] > nums[i + 2]) {
                return false;
            }
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we are only iterating over the array once.
> - **Space Complexity:** $O(1)$, where $n$ is the length of the input array. This is because we are not using any extra space that scales with the input size.
> - **Optimality proof:** This approach is optimal because we are only iterating over the array once and trying at most two modifications for each pair of elements that need to be modified.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, modification, and checking for non-decreasing arrays.
- Problem-solving patterns identified: Trying all possible modifications and checking if any of them result in a non-decreasing array.
- Optimization techniques learned: Iterating over the array only once and trying at most two modifications for each pair of elements that need to be modified.
- Similar problems to practice: Problems that involve modifying arrays to satisfy certain conditions.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as arrays with only one element.
- Edge cases to watch for: Arrays with only one element, arrays with all elements equal, and arrays with all elements in decreasing order.
- Performance pitfalls: Trying all possible modifications and checking if any of them result in a non-decreasing array, which can result in high time complexity.
- Testing considerations: Testing the function with different input arrays, including edge cases, to ensure that it works correctly.