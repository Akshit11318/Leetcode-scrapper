## Join Two Arrays by ID

**Problem Link:** https://leetcode.com/problems/join-two-arrays-by-id/description

**Problem Statement:**
- Input: Two arrays, `A` and `B`, where each element is an array containing an `id` and a `value`.
- Constraints: The `id` in each array is unique.
- Expected Output: A new array where each element is an array containing the `id`, `value` from `A`, and `value` from `B`, if an `id` is present in both `A` and `B`.
- Key Requirements: The solution should handle cases where an `id` is present in one array but not the other.
- Edge Cases: Empty arrays, arrays with no matching `id`s.

Example Test Cases:
- `A = [[1, 2], [2, 3], [3, 4]]`, `B = [[1, 1], [2, 2], [4, 5]]`
- Expected Output: `[[1, 2, 1], [2, 3, 2]]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process is to iterate through each array and compare `id`s to find matches.
- Step-by-step breakdown:
  1. Iterate through `A`.
  2. For each element in `A`, iterate through `B` to find a matching `id`.
  3. If a match is found, add a new array with the `id` and `value`s from both `A` and `B`.
- Why this approach comes to mind first: It's straightforward and doesn't require any additional data structures.

```cpp
#include <iostream>
#include <vector>

std::vector<std::vector<int>> joinArrays(std::vector<std::vector<int>>& A, std::vector<std::vector<int>>& B) {
    std::vector<std::vector<int>> result;
    for (const auto& a : A) {
        for (const auto& b : B) {
            if (a[0] == b[0]) {
                result.push_back({a[0], a[1], b[1]});
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the sizes of `A` and `B`, respectively. This is because for each element in `A`, we potentially iterate through all elements in `B`.
> - **Space Complexity:** $O(n \cdot m)$ in the worst case, if every `id` in `A` has a match in `B`, resulting in a new array for each pair.
> - **Why these complexities occur:** The nested loop structure leads to the time complexity, and the potential for creating a new array for each match leads to the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Using a `std::unordered_map` to store `id`-`value` pairs from one array allows for constant time lookups when iterating through the other array.
- Detailed breakdown:
  1. Store `id`-`value` pairs from `A` in an `unordered_map`.
  2. Iterate through `B`, and for each `id`, check if it exists in the map.
  3. If it does, add a new array with the `id` and `value`s from both `A` and `B`.
- Why this is optimal: It reduces the time complexity significantly by avoiding nested loops.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

std::vector<std::vector<int>> joinArrays(std::vector<std::vector<int>>& A, std::vector<std::vector<int>>& B) {
    std::unordered_map<int, int> idValueMap;
    for (const auto& a : A) {
        idValueMap[a[0]] = a[1];
    }
    
    std::vector<std::vector<int>> result;
    for (const auto& b : B) {
        if (idValueMap.find(b[0]) != idValueMap.end()) {
            result.push_back({b[0], idValueMap[b[0]], b[1]});
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the sizes of `A` and `B`, respectively. This is because we make a single pass through each array.
> - **Space Complexity:** $O(n)$ for storing the `id`-`value` pairs from `A` in the map, plus $O(k)$ for the result, where $k$ is the number of matches found.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to find matches between the two arrays, leveraging the constant time complexity of `unordered_map` lookups.

---

### Final Notes

**Learning Points:**
- The importance of choosing the right data structure for the problem, in this case, `std::unordered_map` for efficient lookups.
- How to analyze time and space complexity to evaluate the efficiency of an algorithm.
- The trade-off between brute force and optimal solutions in terms of complexity and readability.

**Mistakes to Avoid:**
- Not considering the impact of nested loops on time complexity.
- Not leveraging data structures that can reduce complexity, such as `unordered_map`.
- Not validating inputs and handling edge cases properly.