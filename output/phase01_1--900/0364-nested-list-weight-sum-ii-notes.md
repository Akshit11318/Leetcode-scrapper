## Nested List Weight Sum II

**Problem Link:** https://leetcode.com/problems/nested-list-weight-sum-ii/description

**Problem Statement:**
- Input format: A nested list of integers and lists, where each integer is weighted by its depth.
- Constraints: The maximum depth of the nested list is 50, and the maximum sum of the numbers in the nested list is $10^4$.
- Expected output format: The weighted sum of all integers in the nested list.
- Key requirements and edge cases to consider: Handling nested lists of varying depths and summing the weighted integers.
- Example test cases with explanations:
  - Example 1: `[[1,1],2,[3]]` returns 10, because the depth of the first integer is 2, the second integer is 1, and the third integer is 2.
  - Example 2: `[1,[4,[6]]]` returns 17, because the depth of the first integer is 1, the second integer is 2, and the third integer is 3.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Recursively traverse the nested list, calculating the weighted sum at each level.
- Step-by-step breakdown of the solution:
  1. Define a recursive function to traverse the nested list.
  2. For each element in the list, check if it's an integer or a nested list.
  3. If it's an integer, add its weighted value to the sum.
  4. If it's a nested list, recursively call the function with the nested list and the current depth.
- Why this approach comes to mind first: It's a straightforward, intuitive solution that handles the recursive nature of the problem.

```cpp
class Solution {
public:
    int depthSumInverse(vector<NestedInteger>& nestedList) {
        int maxDepth = getMaxDepth(nestedList, 1);
        return depthSumInverse(nestedList, 1, maxDepth);
    }
    
    int getMaxDepth(vector<NestedInteger>& nestedList, int depth) {
        int max = depth;
        for (auto& ni : nestedList) {
            if (ni.isInteger()) continue;
            max = std::max(max, getMaxDepth(ni.getList(), depth + 1));
        }
        return max;
    }
    
    int depthSumInverse(vector<NestedInteger>& nestedList, int depth, int maxDepth) {
        int sum = 0;
        for (auto& ni : nestedList) {
            if (ni.isInteger()) {
                sum += ni.getInteger() * (maxDepth - depth + 1);
            } else {
                sum += depthSumInverse(ni.getList(), depth + 1, maxDepth);
            }
        }
        return sum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot d)$, where $n$ is the total number of integers and $d$ is the maximum depth of the nested list.
> - **Space Complexity:** $O(d)$, due to the recursive call stack.
> - **Why these complexities occur:** The recursive function traverses each element in the nested list, and the maximum depth determines the height of the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Calculate the maximum depth of the nested list first, then traverse the list again to calculate the weighted sum.
- Detailed breakdown of the approach:
  1. Define a function to calculate the maximum depth of the nested list.
  2. Define another function to calculate the weighted sum, using the maximum depth.
- Proof of optimality: This solution has the same time complexity as the brute force approach but avoids redundant calculations.

```cpp
class Solution {
public:
    int depthSumInverse(vector<NestedInteger>& nestedList) {
        int maxDepth = getMaxDepth(nestedList, 1);
        return depthSumInverse(nestedList, 1, maxDepth);
    }
    
    int getMaxDepth(vector<NestedInteger>& nestedList, int depth) {
        int max = depth;
        for (auto& ni : nestedList) {
            if (ni.isInteger()) continue;
            max = std::max(max, getMaxDepth(ni.getList(), depth + 1));
        }
        return max;
    }
    
    int depthSumInverse(vector<NestedInteger>& nestedList, int depth, int maxDepth) {
        int sum = 0;
        for (auto& ni : nestedList) {
            if (ni.isInteger()) {
                sum += ni.getInteger() * (maxDepth - depth + 1);
            } else {
                sum += depthSumInverse(ni.getList(), depth + 1, maxDepth);
            }
        }
        return sum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot d)$, where $n$ is the total number of integers and $d$ is the maximum depth of the nested list.
> - **Space Complexity:** $O(d)$, due to the recursive call stack.
> - **Optimality proof:** This solution has the same time complexity as the brute force approach but avoids redundant calculations, making it optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive traversal of nested lists, calculation of weighted sums.
- Problem-solving patterns identified: Calculating the maximum depth of a nested list before traversing it.
- Optimization techniques learned: Avoiding redundant calculations by calculating the maximum depth first.
- Similar problems to practice: Other problems involving recursive traversal of nested lists.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the base case of the recursion, or incorrectly calculating the weighted sum.
- Edge cases to watch for: Handling empty nested lists, or lists with a single integer.
- Performance pitfalls: Using inefficient data structures or algorithms, such as using a linear search instead of a recursive function.
- Testing considerations: Testing the function with different types of input, such as nested lists of varying depths and sizes.