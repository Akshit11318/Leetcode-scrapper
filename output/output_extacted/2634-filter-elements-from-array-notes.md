## Filter Elements from Array
**Problem Link:** https://leetcode.com/problems/filter-elements-from-array/description

**Problem Statement:**
- Input format and constraints: Given an array `nums` and a predicate function `predicate`.
- Expected output format: Return a new array containing all elements of `nums` for which `predicate` returns `true`.
- Key requirements and edge cases to consider: The function should work for arrays of any size and with any predicate function.
- Example test cases with explanations:
  - Example 1: `nums = [1, 2, 3, 4]`, `predicate = x => x % 2 === 0`. Output: `[2, 4]`.
  - Example 2: `nums = [1, 2, 3, 4]`, `predicate = x => x > 3`. Output: `[4]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To filter elements from an array based on a given condition, we can iterate through each element and check if it satisfies the condition.
- Step-by-step breakdown of the solution:
  1. Create a new array to store the filtered elements.
  2. Iterate through each element in the input array.
  3. For each element, apply the predicate function to check if it satisfies the condition.
  4. If the element satisfies the condition, add it to the new array.
- Why this approach comes to mind first: It's straightforward and easy to understand, making it a natural first approach.

```cpp
#include <vector>
#include <functional>

std::vector<int> filterElementsFromArray(std::vector<int>& nums, std::function<bool(int)> predicate) {
    std::vector<int> result;
    for (int num : nums) {
        if (predicate(num)) {
            result.push_back(num);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array, because we iterate through each element once.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to store all elements in the new array.
> - **Why these complexities occur:** These complexities are due to the iteration through the array and the potential need to store all elements in the new array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal because we must check each element at least once to determine if it satisfies the predicate.
- Detailed breakdown of the approach: The same steps as the brute force approach apply, as it's already optimal.
- Proof of optimality: Since we must examine each element to apply the predicate, we cannot do better than $O(n)$ time complexity.
- Why further optimization is impossible: Any algorithm must at least read the input, which requires $O(n)$ time for an array of $n$ elements.

```cpp
#include <vector>
#include <functional>

std::vector<int> filterElementsFromArray(std::vector<int>& nums, std::function<bool(int)> predicate) {
    std::vector<int> result;
    result.reserve(nums.size()); // Pre-allocate space for potential best-case scenario
    for (int num : nums) {
        if (predicate(num)) {
            result.push_back(num);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to store all elements in the new array.
> - **Optimality proof:** This is optimal because we must check each element at least once, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Linear scanning and filtering based on a predicate.
- Problem-solving patterns identified: The need to examine each element in the input to apply a condition.
- Optimization techniques learned: Pre-allocating space in the result vector to reduce reallocations.
- Similar problems to practice: Other filtering or mapping problems that require iterating through an array.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases like an empty input array or a predicate that always returns false.
- Edge cases to watch for: Handling arrays with a large number of elements and ensuring the predicate function is correctly applied.
- Performance pitfalls: Failing to pre-allocate space for the result vector, leading to potential reallocations during push_back operations.
- Testing considerations: Thoroughly testing the function with various input sizes, predicate functions, and edge cases.