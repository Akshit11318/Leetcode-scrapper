## Sort Colors
**Problem Link:** https://leetcode.com/problems/sort-colors/description

**Problem Statement:**
- Input: An array `nums` containing `n` integers where each integer is either 0, 1, or 2.
- Constraints: You must sort the array in-place using a constant amount of space.
- Expected Output: The input array `nums` sorted in-place.
- Key Requirements:
  - The input array contains only 0s, 1s, and 2s.
  - The array must be sorted in-place.
  - The use of constant extra space is required.
- Edge Cases:
  - An empty array is already sorted.
  - An array with a single element is already sorted.
  - An array with two elements requires a simple comparison and swap if necessary.
- Example Test Cases:
  - Input: `nums = [2,0,2,1,1,0]`
    - Output: `[0,0,1,1,2,2]`
  - Input: `nums = [2,0,1]`
    - Output: `[0,1,2]`

---

### Brute Force Approach
**Explanation:**
- The initial thought process might involve using a sorting algorithm like bubble sort or insertion sort. However, these algorithms do not take advantage of the fact that the input array contains only three distinct numbers (0, 1, and 2).
- A brute force approach could involve counting the occurrences of 0, 1, and 2, then reconstructing the array with the counts.

```cpp
void sortColors(vector<int>& nums) {
    int count0 = 0, count1 = 0, count2 = 0;
    for (int num : nums) {
        if (num == 0) count0++;
        else if (num == 1) count1++;
        else count2++;
    }
    nums.clear();
    while (count0--) nums.push_back(0);
    while (count1--) nums.push_back(1);
    while (count2--) nums.push_back(2);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we make two passes over the array: one to count the occurrences of each number and another to reconstruct the array.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to clear and rebuild the entire array, which requires additional space proportional to the size of the input array.
> - **Why these complexities occur:** The brute force approach requires two passes over the array, leading to linear time complexity. The space complexity is also linear because we are not truly sorting in-place; instead, we are rebuilding the array, which requires additional space.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal approach is known as the Dutch National Flag algorithm, which is a three-way partitioning algorithm. It works by maintaining four pointers: `low`, `mid`, `high`, and the current pointer `i`.
- `low` is used to track the position where the next 0 should be placed, `high` is used to track the position where the next 2 should be placed, and `mid` (or `i`) is used to scan the array.
- When `i` encounters a 0, it swaps the element at `i` with the element at `low` and increments both `low` and `i`.
- When `i` encounters a 1, it simply increments `i`.
- When `i` encounters a 2, it swaps the element at `i` with the element at `high` and decrements `high` without incrementing `i`, because after the swap, the element at `i` needs to be checked again.

```cpp
void sortColors(vector<int>& nums) {
    int low = 0, high = nums.size() - 1, i = 0;
    while (i <= high) {
        if (nums[i] == 0) {
            swap(nums[low], nums[i]);
            low++;
            i++;
        } else if (nums[i] == 1) {
            i++;
        } else {
            swap(nums[i], nums[high]);
            high--;
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, because we make a single pass over the array.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the pointers.
> - **Optimality proof:** This algorithm is optimal because it achieves the goal of sorting the array in-place with a constant amount of extra space in linear time, which is the best we can do given the constraints of the problem.

---

### Final Notes

**Learning Points:**
- The **Dutch National Flag** algorithm is useful for sorting arrays with a limited number of distinct elements.
- **In-place sorting** requires careful management of pointers and swaps to avoid using extra space.
- **Three-way partitioning** can be an efficient technique for certain types of sorting problems.

**Mistakes to Avoid:**
- Not recognizing the opportunity to use a specialized sorting algorithm like the Dutch National Flag.
- Failing to manage pointers correctly, leading to incorrect swaps or index out-of-bounds errors.
- Not testing the algorithm thoroughly with different inputs, including edge cases.