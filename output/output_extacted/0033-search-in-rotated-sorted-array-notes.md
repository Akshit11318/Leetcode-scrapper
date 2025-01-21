## Search in Rotated Sorted Array
**Problem Link:** https://leetcode.com/problems/search-in-rotated-sorted-array/description

**Problem Statement:**
- Input: A rotated sorted array `nums` and a target value `target`.
- Constraints: The array `nums` is sorted in ascending order but rotated at some pivot index unknown to you beforehand. All elements in `nums` are unique.
- Expected Output: The index of the `target` if it is in the array; otherwise, return `-1`.
- Key Requirements and Edge Cases: The array may contain duplicates, and the target may or may not be in the array. The rotation is arbitrary, meaning the pivot point is unknown.
- Example Test Cases:
  - `nums = [4,5,6,7,0,1,2], target = 0` should return `4`.
  - `nums = [4,5,6,7,0,1,2], target = 3` should return `-1`.
  - `nums = [1], target = 0` should return `-1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Simply iterate through the array and check each element to see if it matches the target.
- Step-by-step breakdown of the solution:
  1. Start from the first element of the array.
  2. Compare the current element with the target.
  3. If they match, return the current index.
  4. If they don't match, move to the next element and repeat step 2 until the end of the array is reached.
  5. If the loop completes without finding the target, return `-1`.
- Why this approach comes to mind first: It's the simplest and most straightforward way to solve the problem, requiring minimal additional logic or data structures.

```cpp
int search(vector<int>& nums, int target) {
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] == target) return i;
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because in the worst case, we might have to check every element.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the index and the target value.
> - **Why these complexities occur:** The time complexity is linear because we potentially check every element once, and the space complexity is constant because we don't use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The array is sorted but rotated. We can use a modified binary search algorithm to find the target efficiently.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `left` and `right`, to the start and end of the array, respectively.
  2. While `left` is less than or equal to `right`, calculate the middle index `mid`.
  3. If the target is found at the middle index, return `mid`.
  4. Determine which half of the array is sorted by comparing the values at `left` and `right` with the value at `mid`.
  5. Based on the sorted half, decide which half to continue searching in by adjusting the `left` or `right` pointer.
  6. Repeat steps 2-5 until the target is found or the search space is empty.
- Proof of optimality: This approach is optimal because it reduces the search space by half at each step, similar to a standard binary search, achieving a time complexity of $O(log n)$ in the best case.

```cpp
int search(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) return mid;
        
        // Check if the left half is sorted
        if (nums[left] <= nums[mid]) {
            // If target is in the sorted left half, update right pointer
            if (nums[left] <= target && target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } 
        // If the left half is not sorted, the right half must be sorted
        else {
            // If target is in the sorted right half, update left pointer
            if (nums[mid] < target && target <= nums[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log n)$, where $n$ is the number of elements in the array, because we divide the search space roughly in half at each step.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the pointers and the target value.
> - **Optimality proof:** This approach is optimal because it achieves the best possible time complexity for searching in a sorted but rotated array, leveraging the structure of the input to minimize the number of comparisons needed.

---

### Final Notes

**Learning Points:**
- The importance of understanding the structure of the input data.
- How to apply and modify standard algorithms (like binary search) to fit specific problem constraints.
- The value of analyzing the problem to identify key insights that lead to efficient solutions.

**Mistakes to Avoid:**
- Not considering the rotation of the array and how it affects the search strategy.
- Failing to handle edge cases, such as an empty array or a target that is not present.
- Not optimizing the search algorithm for the specific constraints of the problem, leading to inefficient solutions.