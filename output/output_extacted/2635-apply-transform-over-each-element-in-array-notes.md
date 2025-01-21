## Apply Transform Over Each Element in Array
**Problem Link:** https://leetcode.com/problems/apply-transform-over-each-element-in-array/description

**Problem Statement:**
- Input format: An array of integers `arr` and a function `transformFunc`.
- Constraints: The input array can be empty or contain any number of integers.
- Expected output format: The transformed array after applying `transformFunc` to each element.
- Key requirements and edge cases to consider: Handling empty arrays, arrays with a single element, and ensuring the `transformFunc` is applied correctly to each element.

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate through each element in the array and apply the given `transformFunc` to it, storing the results in a new array.
- Step-by-step breakdown of the solution:
  1. Initialize an empty array to store the transformed elements.
  2. Iterate through each element in the input array.
  3. For each element, apply the `transformFunc` and append the result to the new array.
  4. Return the new array containing all transformed elements.
- Why this approach comes to mind first: It's straightforward and directly addresses the problem statement by applying the transformation function to each element.

```cpp
#include <vector>

std::vector<int> applyTransform(std::vector<int>& arr, std::function<int(int)> transformFunc) {
    std::vector<int> transformedArr;
    for (int num : arr) {
        transformedArr.push_back(transformFunc(num));
    }
    return transformedArr;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we are iterating through the array once.
> - **Space Complexity:** $O(n)$, because in the worst case, we are storing all elements in a new array.
> - **Why these complexities occur:** The iteration through the array and the creation of a new array with the same number of elements dictate these complexities.

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already quite efficient, with a linear time complexity. However, we can slightly optimize the memory allocation by reserving space in the new array before filling it, thus avoiding potential reallocations during `push_back` operations.
- Detailed breakdown of the approach: Same as the brute force, but with an additional step to reserve space in the new array.
- Proof of optimality: This approach remains $O(n)$ in time but ensures more efficient memory management.
- Why further optimization is impossible: Given the requirement to transform each element, a linear time complexity is inherent.

```cpp
#include <vector>

std::vector<int> applyTransformOptimal(std::vector<int>& arr, std::function<int(int)> transformFunc) {
    std::vector<int> transformedArr;
    transformedArr.reserve(arr.size()); // Reserve space for efficiency
    for (int num : arr) {
        transformedArr.push_back(transformFunc(num));
    }
    return transformedArr;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array.
> - **Space Complexity:** $O(n)$, because we are storing all transformed elements in a new array.
> - **Optimality proof:** The time complexity is optimal because we must visit each element at least once. The space complexity is also optimal under the assumption that we need to return a new array with the transformed elements.

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Linear iteration, function application to each element in an array.
- Problem-solving patterns identified: Applying transformations to each element in a collection.
- Optimization techniques learned: Reserving space in vectors to avoid reallocations.
- Similar problems to practice: Other array or vector transformation problems.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases like empty arrays.
- Edge cases to watch for: Arrays with a single element, very large arrays.
- Performance pitfalls: Not reserving space in the new array, leading to potential performance issues due to reallocations.
- Testing considerations: Ensure to test with arrays of varying sizes, including edge cases like empty arrays and arrays with negative numbers or zero.