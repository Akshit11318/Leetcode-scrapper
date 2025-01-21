## Find the Substring with Maximum Cost
**Problem Link:** https://leetcode.com/problems/find-the-substring-with-maximum-cost/description

**Problem Statement:**
- Input format and constraints: The problem takes a string `s` and two arrays `start` and `end` of the same length, where `start[i]` and `end[i]` represent the start and end indices of a substring, and a value `k`. The goal is to find the maximum cost of a substring that can be achieved by considering the values at the start and end indices of each substring.
- Expected output format: The maximum cost of a substring.
- Key requirements and edge cases to consider: 
    - The input string `s` consists only of lowercase English letters.
    - The start and end indices are 0-based.
    - The value `k` is used to calculate the cost.
- Example test cases with explanations:
    - Example 1: Given `s = "adaa"`, `start = [0, 0, 1]`, `end = [0, 2, 2]`, and `k = 2`, the maximum cost of a substring is calculated by considering the values at the start and end indices of each substring and the given value `k`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over all possible substrings of the input string `s` and calculating the cost for each substring by considering the values at the start and end indices of each substring.
- Step-by-step breakdown of the solution:
    1. Generate all possible substrings of the input string `s`.
    2. For each substring, calculate the cost by considering the values at the start and end indices of each substring.
    3. Keep track of the maximum cost found so far.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, as it involves checking all possible substrings and calculating their costs.

```cpp
#include <iostream>
#include <string>

int maximumCostSubstring(const std::string& s, const int* start, const int* end, int k, int n) {
    int maxCost = 0;
    for (int i = 0; i < n; i++) {
        int cost = (s[start[i]] - 'a' + 1) * k + (s[end[i]] - 'a' + 1);
        maxCost = std::max(maxCost, cost);
    }
    return maxCost;
}

int main() {
    std::string s = "adaa";
    int start[] = {0, 0, 1};
    int end[] = {0, 2, 2};
    int k = 2;
    int n = sizeof(start) / sizeof(start[0]);
    std::cout << "Maximum cost of a substring: " << maximumCostSubstring(s, start, end, k, n) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of substrings, because we are iterating over each substring once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the maximum cost and other variables.
> - **Why these complexities occur:** These complexities occur because we are simply iterating over each substring and calculating its cost, which takes constant time.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves directly calculating the maximum cost by considering the values at the start and end indices of each substring, without generating all possible substrings.
- Detailed breakdown of the approach:
    1. Iterate over the start and end indices of each substring.
    2. For each substring, calculate the cost by considering the values at the start and end indices.
    3. Keep track of the maximum cost found so far.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n)$, which is the minimum time complexity required to solve this problem, as we need to consider each substring at least once.
- Why further optimization is impossible: Further optimization is impossible because we need to consider each substring at least once to calculate its cost, and this approach already does that in linear time.

```cpp
#include <iostream>
#include <string>

int maximumCostSubstring(const std::string& s, const int* start, const int* end, int k, int n) {
    int maxCost = 0;
    for (int i = 0; i < n; i++) {
        int cost = (s[start[i]] - 'a' + 1) * k + (s[end[i]] - 'a' + 1);
        maxCost = std::max(maxCost, cost);
    }
    return maxCost;
}

int main() {
    std::string s = "adaa";
    int start[] = {0, 0, 1};
    int end[] = {0, 2, 2};
    int k = 2;
    int n = sizeof(start) / sizeof(start[0]);
    std::cout << "Maximum cost of a substring: " << maximumCostSubstring(s, start, end, k, n) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of substrings, because we are iterating over each substring once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the maximum cost and other variables.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n)$, which is the minimum time complexity required to solve this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, calculation of maximum cost.
- Problem-solving patterns identified: Direct calculation of maximum cost.
- Optimization techniques learned: Avoiding unnecessary calculations.
- Similar problems to practice: Other string-related problems, such as finding the longest substring with a certain property.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing variables, not checking for edge cases.
- Edge cases to watch for: Empty input string, invalid start and end indices.
- Performance pitfalls: Using inefficient algorithms, such as generating all possible substrings.
- Testing considerations: Test with different input strings, start and end indices, and values of `k`.