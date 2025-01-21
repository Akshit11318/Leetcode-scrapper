## Remove Element
**Problem Link:** [https://leetcode.com/problems/remove-element/description](https://leetcode.com/problems/remove-element/description)

**Problem Statement:**
- Input format: An integer array `nums` and an integer `val`.
- Constraints: $0 \leq \text{nums.length} \leq 100$ and $0 \leq \text{val} \leq 100$.
- Expected output format: The length of the array after removing all occurrences of `val`.
- Key requirements: Modify the input array in-place.
- Example test cases:
  - Input: `nums = [3,2,2,3], val = 3`, Output: `2`, Explanation: `nums` is now `[2,2,_,_]`.
  - Input: `nums = [0,1,2,2,3,0,4,2], val = 2`, Output: `5`, Explanation: `nums` is now `[0,1,4,0,3,_,_,_]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the array and create a new array with all elements that are not equal to `val`.
- Step-by-step breakdown of the solution:
  1. Create a new array to store the result.
  2. Iterate through the input array.
  3. If the current element is not equal to `val`, add it to the new array.
- Why this approach comes to mind first: It is a straightforward and intuitive solution.

```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        vector<int> result;
        for (int num : nums) {
            if (num != val) {
                result.push_back(num);
            }
        }
        nums = result;
        return nums.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array, because we are iterating through the array once.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to create a new array of the same size as the input array.
> - **Why these complexities occur:** These complexities occur because we are creating a new array and iterating through the input array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of creating a new array, we can modify the input array in-place by using two pointers.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `i` and `j`, to the beginning of the array.
  2. Iterate through the array with `j`.
  3. If the current element is not equal to `val`, swap it with the element at index `i` and increment `i`.
- Proof of optimality: This solution has a time complexity of $O(n)$ and a space complexity of $O(1)$, which is optimal.

```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i = 0;
        for (int j = 0; j < nums.size(); j++) {
            if (nums[j] != val) {
                nums[i] = nums[j];
                i++;
            }
        }
        return i;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array, because we are iterating through the array once.
> - **Space Complexity:** $O(1)$, because we are modifying the input array in-place.
> - **Optimality proof:** This solution is optimal because it has the best possible time and space complexities.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two pointers technique, in-place modification.
- Problem-solving patterns identified: Modifying the input array instead of creating a new one.
- Optimization techniques learned: Using two pointers to reduce space complexity.
- Similar problems to practice: [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/), [Move Zeroes](https://leetcode.com/problems/move-zeroes/).

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input array.
- Edge cases to watch for: Input array with all elements equal to `val`.
- Performance pitfalls: Creating a new array instead of modifying the input array in-place.
- Testing considerations: Test the solution with different input arrays and values of `val`.