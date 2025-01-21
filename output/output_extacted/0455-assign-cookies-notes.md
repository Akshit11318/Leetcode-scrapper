## Assign Cookies
**Problem Link:** [https://leetcode.com/problems/assign-cookies/description](https://leetcode.com/problems/assign-cookies/description)

**Problem Statement:**
- Input format: Two arrays, `g` and `s`, where `g[i]` is the greed factor of the `i-th` child, and `s[j]` is the size of the `j-th` cookie.
- Constraints: `1 <= g.length <= 3 * 10^4`, `1 <= s.length <= 3 * 10^4`, `1 <= g[i], s[j] <= 2^31 - 1`.
- Expected output format: The maximum number of children who can be satisfied.
- Key requirements and edge cases to consider: The size of the cookie should be greater than or equal to the greed factor of the child.
- Example test cases with explanations:
  - `g = [1,2,3]`, `s = [1,2]`, Output: `2` (Child 1 and child 2 will be satisfied)
  - `g = [1,2]`, `s = [1,2,3]`, Output: `2` (Child 1 and child 2 will be satisfied)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of children and cookies to find the maximum number of satisfied children.
- Step-by-step breakdown of the solution:
  1. Initialize a variable to store the maximum number of satisfied children.
  2. Iterate over all possible subsets of children.
  3. For each subset, try all possible assignments of cookies to children in the subset.
  4. Check if the current assignment satisfies all children in the subset.
  5. Update the maximum number of satisfied children if the current assignment satisfies more children.
- Why this approach comes to mind first: It's a straightforward way to solve the problem, but it's inefficient due to its high time complexity.

```cpp
#include <vector>
#include <algorithm>

int findContentChildren(std::vector<int>& g, std::vector<int>& s) {
    std::sort(g.begin(), g.end());
    std::sort(s.begin(), s.end());
    int child = 0;
    for (int cookie = 0; child < g.size() && cookie < s.size(); cookie++) {
        if (s[cookie] >= g[child]) {
            child++;
        }
    }
    return child;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + m \log m)$ where $n$ and $m$ are the number of children and cookies respectively, due to sorting.
> - **Space Complexity:** $O(1)$ as we are not using any extra space that scales with input size.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, and the space complexity is constant because we only use a fixed amount of space to store the indices.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Sort both arrays and then iterate over them, assigning the smallest cookie that satisfies the current child's greed factor.
- Detailed breakdown of the approach:
  1. Sort the arrays of children and cookies in ascending order.
  2. Initialize two pointers, one for the children and one for the cookies.
  3. Iterate over the cookies, and for each cookie, check if it can satisfy the current child's greed factor.
  4. If it can, move to the next child and continue the process.
- Proof of optimality: This approach ensures that we satisfy the maximum number of children because we always assign the smallest cookie that can satisfy the current child's greed factor.

```cpp
int findContentChildren(std::vector<int>& g, std::vector<int>& s) {
    std::sort(g.begin(), g.end());
    std::sort(s.begin(), s.end());
    int child = 0;
    for (int cookie = 0; child < g.size() && cookie < s.size(); cookie++) {
        if (s[cookie] >= g[child]) {
            child++;
        }
    }
    return child;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + m \log m)$ where $n$ and $m$ are the number of children and cookies respectively, due to sorting.
> - **Space Complexity:** $O(1)$ as we are not using any extra space that scales with input size.
> - **Optimality proof:** The time complexity is optimal because we must at least look at each child and cookie once, and the space complexity is optimal because we only use a constant amount of space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, two-pointer technique.
- Problem-solving patterns identified: Greedy algorithm.
- Optimization techniques learned: Using sorting to simplify the problem.
- Similar problems to practice: Other problems that involve assigning resources to tasks, such as the `Fractional Knapsack Problem`.

**Mistakes to Avoid:**
- Common implementation errors: Not checking the bounds of the arrays, not handling the case where there are no children or cookies.
- Edge cases to watch for: The case where there are no children or cookies, the case where the greed factors are all greater than the cookie sizes.
- Performance pitfalls: Using a brute force approach, not using sorting to simplify the problem.
- Testing considerations: Test the function with different inputs, including edge cases, to ensure it works correctly.