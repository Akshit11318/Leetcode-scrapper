## Flattening a Deeply Nested Array
**Problem Link:** https://leetcode.com/problems/flatten-deeply-nested-array/description

**Problem Statement:**
- Input format and constraints: The input is a deeply nested array of integers and arrays. The goal is to flatten this array into a one-dimensional array of integers.
- Expected output format: The output should be a one-dimensional array containing all the integers from the input array.
- Key requirements and edge cases to consider: The input array can contain integers and arrays at any depth. The solution should handle arrays of varying sizes and structures.
- Example test cases with explanations:
  - Input: `[1, [2, 3, [4, 5]], 6]`
  - Output: `[1, 2, 3, 4, 5, 6]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to recursively traverse the array. When an integer is encountered, it is added to the result. When an array is encountered, the function calls itself with the sub-array.
- Step-by-step breakdown of the solution:
  1. Define a recursive function that takes an array as input.
  2. Iterate through each element in the array.
  3. If the element is an integer, add it to the result array.
  4. If the element is an array, call the recursive function with the sub-array and append the result to the main result array.
- Why this approach comes to mind first: It's a straightforward way to handle nested structures by breaking them down into simpler cases.

```cpp
#include <iostream>
#include <vector>

std::vector<int> flatten(const std::vector<std::variant<int, std::vector<std::variant<int, std::vector<>>>>>& nestedArray) {
    std::vector<int> result;
    for (const auto& element : nestedArray) {
        if (std::holds_alternative<int>(element)) {
            result.push_back(std::get<int>(element));
        } else {
            std::vector<std::variant<int, std::vector<std::variant<int, std::vector<>>>> subArray = std::get<std::vector<std::variant<int, std::vector<std::variant<int, std::vector<>>>>>>(element);
            std::vector<int> subResult = flatten(subArray);
            result.insert(result.end(), subResult.begin(), subResult.end());
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the total number of elements (integers and arrays) in the nested array, since each element is processed once.
> - **Space Complexity:** $O(n)$, due to the recursive call stack and the space required for the result array.
> - **Why these complexities occur:** The time complexity is linear because each element is visited once. The space complexity is also linear due to the recursive call stack and the storage needed for the flattened array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The recursive approach is already quite efficient for this problem. However, to slightly improve and ensure we're at the optimal solution, we recognize that the problem doesn't require any additional information beyond what's provided by the recursive traversal. Thus, the optimal solution remains a refined version of the brute force approach, focusing on clarity and efficiency in implementation.
- Detailed breakdown of the approach: The approach remains similar to the brute force, with a focus on ensuring each element is processed exactly once and that the recursion is well-managed to avoid unnecessary overhead.
- Proof of optimality: The solution is optimal because it visits each element exactly once, which is necessary to flatten the array, and it uses a minimal amount of extra space to store the recursive call stack and the result.

```cpp
#include <iostream>
#include <vector>

std::vector<int> flatten(const std::vector<std::variant<int, std::vector<std::variant<int, std::vector<>>>>>& nestedArray) {
    std::vector<int> result;
    for (const auto& element : nestedArray) {
        if (std::holds_alternative<int>(element)) {
            result.push_back(std::get<int>(element));
        } else {
            std::vector<std::variant<int, std::vector<std::variant<int, std::vector<>>>> subArray = std::get<std::vector<std::variant<int, std::vector<std::variant<int, std::vector<>>>>>>(element);
            std::vector<int> subResult = flatten(subArray);
            result.insert(result.end(), subResult.begin(), subResult.end());
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the total number of elements in the nested array.
> - **Space Complexity:** $O(n)$, for the recursive call stack and the result array.
> - **Optimality proof:** This solution is optimal because it processes each element exactly once and uses minimal extra space, achieving the best possible time and space complexity for the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive traversal and handling of nested data structures.
- Problem-solving patterns identified: Breaking down complex structures into simpler cases through recursion.
- Optimization techniques learned: Ensuring each element is processed exactly once and minimizing extra space usage.
- Similar problems to practice: Other problems involving recursive traversal of nested structures.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect handling of recursive function calls or failure to check the type of each element.
- Edge cases to watch for: Empty arrays, deeply nested arrays, and arrays containing only integers.
- Performance pitfalls: Excessive recursion without proper termination conditions or inefficient handling of large inputs.
- Testing considerations: Thoroughly testing with various input structures, including edge cases.