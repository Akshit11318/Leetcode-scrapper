## Sort the People
**Problem Link:** https://leetcode.com/problems/sort-the-people/description

**Problem Statement:**
- Input format: `names` and `heights` arrays of the same length, where `names[i]` corresponds to `heights[i]`.
- Constraints: `1 <= names.length <= 10^5`, `1 <= names[i].length <= 20`, `0 <= heights[i] <= 10^6`.
- Expected output format: A list of names sorted in descending order of their corresponding heights.
- Key requirements and edge cases to consider: Handling duplicate heights, ensuring names are correctly sorted in descending order of heights.
- Example test cases with explanations:
  - Example 1: Input: `names = ["Mary","John","Emma"], heights = [180,165,170]`, Output: `["Mary","Emma","John"]`.
  - Example 2: Input: `names = ["Alice","Bob","Alice"], heights = [155,185,155]`, Output: `["Bob","Alice","Alice"]`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Combine `names` and `heights` into pairs and sort these pairs based on heights in descending order.
- Step-by-step breakdown of the solution:
  1. Create pairs of `(name, height)` from the input arrays.
  2. Sort these pairs in descending order based on `height`.
  3. Extract `name` from each pair in the sorted order.
- Why this approach comes to mind first: It's straightforward and directly addresses the requirement of sorting names based on their heights.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

struct Person {
    std::string name;
    int height;
};

bool compare(const Person& a, const Person& b) {
    return a.height > b.height;
}

std::vector<std::string> sortPeople(std::vector<std::string>& names, std::vector<int>& heights) {
    int n = names.size();
    std::vector<Person> people(n);
    
    // Create pairs of (name, height)
    for (int i = 0; i < n; ++i) {
        people[i].name = names[i];
        people[i].height = heights[i];
    }
    
    // Sort pairs in descending order of height
    std::sort(people.begin(), people.end(), compare);
    
    // Extract names in sorted order
    std::vector<std::string> sortedNames(n);
    for (int i = 0; i < n; ++i) {
        sortedNames[i] = people[i].name;
    }
    
    return sortedNames;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting $n$ pairs.
> - **Space Complexity:** $O(n)$ for storing $n$ pairs.
> - **Why these complexities occur:** Sorting is the dominant operation, and we need to store all pairs to sort them.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Utilize a data structure that inherently supports sorting or use an algorithm that can sort based on a key (in this case, `height`).
- Detailed breakdown of the approach:
  1. Create a vector of pairs `(height, name)` to facilitate sorting by `height`.
  2. Use `std::sort` with a custom comparator to sort the pairs in descending order of `height`.
  3. Extract `name` from each pair in the sorted order.
- Proof of optimality: This approach is optimal because it leverages the standard library's sorting algorithm, which is highly optimized, and it directly addresses the problem's requirements without unnecessary complexity.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

std::vector<std::string> sortPeople(std::vector<std::string>& names, std::vector<int>& heights) {
    int n = names.size();
    std::vector<std::pair<int, std::string>> people(n);
    
    // Create pairs of (height, name) for sorting
    for (int i = 0; i < n; ++i) {
        people[i] = {heights[i], names[i]};
    }
    
    // Sort pairs in descending order of height
    std::sort(people.begin(), people.end(), [](const auto& a, const auto& b) {
        return a.first > b.first;
    });
    
    // Extract names in sorted order
    std::vector<std::string> sortedNames(n);
    for (int i = 0; i < n; ++i) {
        sortedNames[i] = people[i].second;
    }
    
    return sortedNames;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to sorting $n$ pairs.
> - **Space Complexity:** $O(n)$ for storing $n$ pairs.
> - **Optimality proof:** This is the most straightforward and efficient way to solve the problem, leveraging standard library functions for sorting.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, use of pairs for combining data, and leveraging standard library functions.
- Problem-solving patterns identified: Directly addressing the problem statement, using appropriate data structures for efficiency.
- Optimization techniques learned: Using built-in sorting algorithms, minimizing unnecessary operations.
- Similar problems to practice: Other sorting and data manipulation problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect comparator functions, not handling edge cases like duplicate heights.
- Edge cases to watch for: Duplicate heights, names of varying lengths.
- Performance pitfalls: Using inefficient sorting algorithms or data structures.
- Testing considerations: Ensure all possible combinations of inputs are tested, including edge cases.