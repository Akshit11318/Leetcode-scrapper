## Remove Duplicates from Sorted Array II

**Problem Link:** [https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description)

**Problem Statement:**
- Given a sorted array `nums` containing duplicates, modify the array in-place such that each element appears at most twice and return the new length of the array.
- Input format and constraints: `nums` is a non-empty array of integers, and the length of `nums` will not exceed $10^4$.
- Expected output format: The new length of the array after removing duplicates.
- Key requirements and edge cases to consider: The input array is sorted, and each element should appear at most twice in the resulting array.
- Example test cases with explanations:
  - For `nums = [1,1,1,2,2,3]`, the output should be `5` with the array modified to `[1,1,2,2,3]`.
  - For `nums = [0,0,1,1,1,1,2,3,3]`, the output should be `7` with the array modified to `[0,0,1,1,2,3,3]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a new array and iterate through the original array, adding each element to the new array only if it appears at most twice.
- Step-by-step breakdown of the solution:
  1. Initialize an empty array `result` to store the elements with duplicates removed.
  2. Initialize a counter `count` to keep track of the occurrences of each element.
  3. Iterate through the input array `nums`.
  4. For each element, check if it is the same as the previous element. If it is, increment the counter.
  5. If the counter is less than or equal to 2, add the element to the `result` array.
  6. If the element is different from the previous one, reset the counter.
- Why this approach comes to mind first: It directly addresses the requirement of limiting each element's occurrences to at most two by manually counting and filtering.

```cpp
#include <vector>

int removeDuplicates(std::vector<int>& nums) {
    if (nums.size() <= 2) {
        return nums.size();
    }
    
    std::vector<int> result;
    int count = 1;
    result.push_back(nums[0]);
    
    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] == nums[i - 1]) {
            count++;
        } else {
            count = 1;
        }
        
        if (count <= 2) {
            result.push_back(nums[i]);
        }
    }
    
    nums = result;
    return nums.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array, because we iterate through the array once.
> - **Space Complexity:** $O(n)$, as in the worst case, we might end up storing all elements in the `result` array.
> - **Why these complexities occur:** The iteration through the array causes the linear time complexity, and creating a new array for storing the result leads to the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of creating a new array, we can modify the input array in-place by using two pointers, one for reading and one for writing.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `read` and `write`, both starting at the beginning of the array.
  2. Initialize a counter `count` to track the occurrences of each element.
  3. Iterate through the array with the `read` pointer.
  4. If the current element is the same as the previous one, increment the counter.
  5. If the counter is less than or equal to 2, move the element to the `write` pointer's position and increment the `write` pointer.
  6. If the element is different from the previous one, reset the counter and move the element to the `write` pointer's position, then increment the `write` pointer.
- Proof of optimality: This approach minimizes both time and space complexity by only iterating through the array once and not using any additional space that scales with input size.

```cpp
#include <vector>

int removeDuplicates(std::vector<int>& nums) {
    if (nums.size() <= 2) {
        return nums.size();
    }
    
    int write = 2;
    for (int read = 2; read < nums.size(); read++) {
        if (nums[read] != nums[write - 2]) {
            nums[write] = nums[read];
            write++;
        }
    }
    
    return write;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array, because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the pointers and counter, regardless of the input size.
> - **Optimality proof:** This is the best possible time complexity for this problem since we must at least read the input once. The space complexity is optimal as well because we are modifying the input array in-place without using any data structures that scale with the input size.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: In-place modification, two-pointer technique, and counter-based tracking.
- Problem-solving patterns identified: The importance of considering in-place solutions for array modification problems.
- Optimization techniques learned: Minimizing space usage by avoiding unnecessary data structures and leveraging the input array itself for modifications.
- Similar problems to practice: Other array modification problems, such as removing duplicates or shifting elements.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as arrays with fewer than three elements.
- Edge cases to watch for: Empty arrays, arrays with a single element, and arrays where all elements are the same.
- Performance pitfalls: Using inefficient data structures or algorithms that result in higher than necessary time or space complexity.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases, to ensure correctness and robustness.