## Removing Minimum and Maximum from Array
**Problem Link:** https://leetcode.com/problems/removing-minimum-and-maximum-from-array/description

**Problem Statement:**
- Input format and constraints: Given a sorted array `nums` of size `n`, find the minimum number of operations required to remove the minimum and maximum elements from the array.
- Expected output format: The minimum number of operations.
- Key requirements and edge cases to consider: The array can be empty, and the minimum and maximum elements can be the same.
- Example test cases with explanations:
  - `nums = [2, 2]`, output: `2`
  - `nums = [2, 2, 2, 2]`, output: `2`
  - `nums = [1, 2, 3, 4]`, output: `2`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible combinations of removing elements from the array.
- Step-by-step breakdown of the solution:
  1. Iterate over the array to find the minimum and maximum elements.
  2. Remove the minimum and maximum elements from the array.
  3. Repeat steps 1-2 until the array is empty.
- Why this approach comes to mind first: It's a straightforward and intuitive approach.

```cpp
int minOperations(vector<int>& nums) {
    int operations = 0;
    while (!nums.empty()) {
        int min_val = *min_element(nums.begin(), nums.end());
        int max_val = *max_element(nums.begin(), nums.end());
        if (min_val == max_val) {
            nums.clear();
            operations++;
        } else {
            nums.erase(max_element(nums.begin(), nums.end()));
            nums.erase(min_element(nums.begin(), nums.end()));
            operations++;
        }
    }
    return operations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the array. This is because we're using the `min_element` and `max_element` functions in a loop, which have a time complexity of $O(n)$.
> - **Space Complexity:** $O(1)$, as we're not using any additional data structures that scale with the input size.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the repeated use of the `min_element` and `max_element` functions, which have to iterate over the entire array.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Since the array is sorted, the minimum and maximum elements are always at the beginning and end of the array, respectively.
- Detailed breakdown of the approach:
  1. Check if the array is empty. If it is, return 0.
  2. If the array has only one element, return 1.
  3. Otherwise, return the minimum between the number of elements at the beginning and end of the array.
- Proof of optimality: This approach is optimal because we're taking advantage of the fact that the array is sorted, which allows us to find the minimum and maximum elements in constant time.

```cpp
int minOperations(vector<int>& nums) {
    if (nums.empty()) return 0;
    if (nums.size() == 1) return 1;
    int min_count = 0;
    int max_count = 0;
    int min_val = nums[0];
    int max_val = nums[nums.size() - 1];
    for (int num : nums) {
        if (num == min_val) min_count++;
        if (num == max_val) max_count++;
    }
    if (min_val == max_val) return min_count;
    return min(min_count, max_count);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the array. This is because we're iterating over the array once to count the occurrences of the minimum and maximum elements.
> - **Space Complexity:** $O(1)$, as we're not using any additional data structures that scale with the input size.
> - **Optimality proof:** This approach is optimal because we're taking advantage of the fact that the array is sorted, which allows us to find the minimum and maximum elements in constant time. We're also only iterating over the array once, which minimizes the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Taking advantage of the fact that the array is sorted to find the minimum and maximum elements in constant time.
- Problem-solving patterns identified: Using the properties of the input data to optimize the solution.
- Optimization techniques learned: Iterating over the array only once to minimize the time complexity.
- Similar problems to practice: Other problems that involve taking advantage of the properties of the input data to optimize the solution.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty array or an array with only one element.
- Edge cases to watch for: Arrays with duplicate minimum and maximum elements.
- Performance pitfalls: Using the brute force approach, which has a high time complexity.
- Testing considerations: Testing the solution with different input sizes and edge cases to ensure it works correctly.