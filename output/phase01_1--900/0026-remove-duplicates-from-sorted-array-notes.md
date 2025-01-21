## Remove Duplicates from Sorted Array

**Problem Link:** https://leetcode.com/problems/remove-duplicates-from-sorted-array/description

**Problem Statement:**
- Input: A sorted array `nums` containing duplicates.
- Constraints: The input array is sorted in ascending order, and each element is an integer.
- Expected Output: The length of the array if all duplicates were removed.
- Key Requirements: Modify the input array in-place to remove duplicates and return the length of the modified array.
- Edge Cases: Handle arrays with no duplicates, all duplicates, and a mix of unique and duplicate elements.
- Example Test Cases:
  - Input: `nums = [1,1,2]`, Output: `2`, Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
  - Input: `nums = [0,0,1,1,1,2,2,3,3,4]`, Output: `5`, Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating through the array and checking for duplicates. A straightforward way to do this is to create a new array that only includes unique elements from the original array.
- Step-by-step breakdown:
  1. Create a new array to store unique elements.
  2. Iterate through the original array, adding each element to the new array only if it's not already present.
  3. Return the length of the new array.
- Why this approach comes to mind first: It's a simple, intuitive solution that directly addresses the problem statement.

```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        vector<int> uniqueNums;
        for (int num : nums) {
            if (uniqueNums.empty() || num != uniqueNums.back()) {
                uniqueNums.push_back(num);
            }
        }
        nums = uniqueNums;
        return nums.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array, because we're doing a single pass through the array.
> - **Space Complexity:** $O(n)$, because in the worst case (all elements are unique), the size of the new array will be equal to the size of the input array.
> - **Why these complexities occur:** The time complexity is linear due to the single pass through the array, and the space complexity is also linear because we're potentially creating a new array of the same size as the input.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Since the input array is already sorted, we can take advantage of this property to remove duplicates in-place without needing an additional array.
- Detailed breakdown:
  1. Initialize two pointers, one at the beginning of the array (`i`) and another at the second element (`j = 1`).
  2. Compare the elements at `i` and `j`. If they are different, move the element at `j` next to the element at `i` (i.e., `nums[i+1] = nums[j]`) and increment both `i` and `j`. If they are the same, just increment `j`.
  3. Repeat step 2 until `j` reaches the end of the array.
  4. The length of the modified array (without duplicates) is `i + 1`.
- Proof of optimality: This approach is optimal because it only requires a single pass through the array and uses a constant amount of additional space.

```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        int i = 0;
        for (int j = 1; j < nums.size(); j++) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }
        return i + 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array, because we're doing a single pass through the array.
> - **Space Complexity:** $O(1)$, because we're modifying the input array in-place and using a constant amount of additional space.
> - **Optimality proof:** This solution is optimal because it achieves the best possible time complexity ($O(n)$) for this problem while minimizing space usage ($O(1)$).

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: In-place modification, two-pointer technique, and leveraging the properties of sorted arrays.
- Problem-solving patterns identified: Looking for ways to reduce space complexity by modifying the input in-place and utilizing the given structure of the data (in this case, the sorted order).
- Optimization techniques learned: Recognizing opportunities to reduce the need for additional space by leveraging the input's structure.

**Mistakes to Avoid:**
- Assuming the need for additional space without considering in-place modification techniques.
- Overlooking the properties of the input data (e.g., the array being sorted) that can significantly simplify the solution.
- Not testing edge cases thoroughly, such as an empty array or an array with all elements being the same.