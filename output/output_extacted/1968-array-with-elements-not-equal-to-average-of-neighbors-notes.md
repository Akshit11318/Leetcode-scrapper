## Array with Elements Not Equal to Average of Neighbors

**Problem Link:** https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/description

**Problem Statement:**
- Input: An integer array `nums` of length `n`.
- Constraints: `1 <= n <= 10^5`, `1 <= nums[i] <= 10^5`.
- Expected Output: An array with elements not equal to the average of its neighbors.
- Key Requirements: 
    - For each element in the array, its value should not be equal to the average of its neighbors.
    - The average is calculated by summing the neighboring elements and dividing by the number of neighbors.
- Edge Cases: 
    - The array has only one element.
    - The array has two elements.

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking each element in the array to see if it's equal to the average of its neighbors.
- Step-by-step breakdown:
    1. Iterate over the array, considering each element as a potential candidate.
    2. For each element, calculate the average of its neighbors.
    3. Check if the current element is equal to the calculated average.
    4. If it is, replace the element with a new value that is not equal to the average of its neighbors.
- This approach comes to mind first because it directly addresses the problem statement.

```cpp
vector<int> rearrangeArray(vector<int>& nums) {
    vector<int> result = nums;
    for (int i = 0; i < result.size(); i++) {
        double average = 0.0;
        int count = 0;
        if (i > 0) {
            average += result[i - 1];
            count++;
        }
        if (i < result.size() - 1) {
            average += result[i + 1];
            count++;
        }
        if (count > 0) {
            average /= count;
            if (result[i] == average) {
                // Find a new value that is not equal to the average
                for (int j = 0; j < result.size(); j++) {
                    if (j != i && result[j] != average) {
                        swap(result[i], result[j]);
                        break;
                    }
                }
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because in the worst case, we're iterating over the array for each element to find a new value that is not equal to the average of its neighbors.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we're creating a copy of the input array.
> - **Why these complexities occur:** The brute force approach involves nested iterations over the array, leading to a quadratic time complexity. The space complexity is linear because we're creating a copy of the input array.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to realize that we don't need to calculate the average for each element and then find a new value.
- Instead, we can simply rearrange the elements in such a way that no element is equal to the average of its neighbors.
- One way to achieve this is by swapping adjacent elements.
- Proof of optimality: This approach is optimal because it ensures that no element is equal to the average of its neighbors, and it does so in linear time.

```cpp
vector<int> rearrangeArray(vector<int>& nums) {
    for (int i = 0; i < nums.size() - 1; i += 2) {
        swap(nums[i], nums[i + 1]);
    }
    return nums;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we're iterating over the array once, swapping adjacent elements.
> - **Space Complexity:** $O(1)$, where $n$ is the number of elements in the array. This is because we're not using any extra space that scales with the input size.
> - **Optimality proof:** This approach is optimal because it achieves the desired result in linear time and constant space, which is the best possible complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Swapping elements to achieve a desired property.
- Problem-solving patterns identified: Rearranging elements to satisfy a condition.
- Optimization techniques learned: Reducing time complexity by avoiding unnecessary calculations.
- Similar problems to practice: Other rearrangement problems, such as rearranging an array to satisfy a certain condition.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as arrays with one or two elements.
- Edge cases to watch for: Arrays with an odd number of elements, where the middle element may not have two neighbors.
- Performance pitfalls: Using a brute force approach that leads to quadratic time complexity.
- Testing considerations: Testing the solution with arrays of different sizes and compositions to ensure it works correctly in all cases.