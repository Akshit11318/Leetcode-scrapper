## Replace Elements with Greatest Element on Right Side
**Problem Link:** https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description

**Problem Statement:**
- Input format and constraints: Given an array `arr`, replace each element with the greatest element on its right side.
- Expected output format: Return the modified array.
- Key requirements and edge cases to consider: The array may contain duplicate elements, and the greatest element on the right side of an element may be the element itself if it is the largest.
- Example test cases with explanations:
  - Input: `arr = [17,18,5,4,6,1]`
    - Output: `[18,6,6,6,1,-1]`
    - Explanation: For each element, find the greatest element on its right side. If no element exists on the right side, replace it with `-1`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: For each element in the array, iterate through all elements on its right side to find the greatest one.
- Step-by-step breakdown of the solution:
  1. Iterate through the array from left to right.
  2. For each element, iterate through the elements on its right side to find the maximum value.
  3. Replace the current element with the maximum value found on its right side. If no elements exist on the right side, replace it with `-1`.
- Why this approach comes to mind first: It directly addresses the problem statement by considering each element and its right side separately.

```cpp
vector<int> replaceElements(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n; i++) {
        int maxRight = -1; // Initialize maxRight as -1 in case no element is found on the right
        for (int j = i + 1; j < n; j++) {
            if (arr[j] > maxRight) {
                maxRight = arr[j];
            }
        }
        arr[i] = maxRight; // Replace current element with the max on its right
    }
    return arr;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because for each element, we potentially iterate through the rest of the array.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output arrays, as we only use a constant amount of space to store the maximum value on the right side of the current element.
> - **Why these complexities occur:** The nested loop structure leads to the quadratic time complexity. The space complexity is constant because we only use a fixed amount of extra memory to store the maximum value on the right side.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of iterating through the elements on the right side for each element, we can make a single pass from right to left, keeping track of the maximum element seen so far.
- Detailed breakdown of the approach:
  1. Initialize a variable `maxSoFar` to `-1`, which will store the maximum element seen on the right side as we iterate from right to left.
  2. Iterate through the array from right to left.
  3. For each element, replace it with the current `maxSoFar` value.
  4. Update `maxSoFar` if the current element is greater than `maxSoFar`.
- Proof of optimality: This approach ensures that we only need to make one pass through the array, resulting in a linear time complexity, which is the best possible for this problem since we must at least read the input once.

```cpp
vector<int> replaceElements(vector<int>& arr) {
    int n = arr.size();
    int maxSoFar = -1; // Initialize maxSoFar as -1
    for (int i = n - 1; i >= 0; i--) {
        int temp = arr[i]; // Store current element in temp
        arr[i] = maxSoFar; // Replace current element with maxSoFar
        if (temp > maxSoFar) {
            maxSoFar = temp; // Update maxSoFar if current element is greater
        }
    }
    return arr;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output arrays, as we only use a constant amount of space to store the maximum value seen so far.
> - **Optimality proof:** The linear time complexity is optimal because we must at least examine each element once to determine the greatest element on its right side.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration from right to left to avoid redundant computations, and using a single pass to achieve optimal time complexity.
- Problem-solving patterns identified: Looking for opportunities to reduce the number of iterations or computations by reordering operations or using temporary storage efficiently.
- Optimization techniques learned: Reducing the number of comparisons and iterations by making a single pass and maintaining a running maximum.
- Similar problems to practice: Problems involving array manipulations, such as finding the next greater element, or problems that can be solved by making a single pass through the input.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly initializing variables, or forgetting to update variables when necessary.
- Edge cases to watch for: Handling arrays with zero or one element, or arrays containing duplicate maximum values.
- Performance pitfalls: Using nested loops when a single pass is possible, or using excessive memory when constant space is sufficient.
- Testing considerations: Thoroughly testing the function with various input sizes, including edge cases, to ensure correctness and performance.