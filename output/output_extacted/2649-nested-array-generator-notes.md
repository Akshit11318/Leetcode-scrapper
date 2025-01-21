## Nested List Weight Sum
**Problem Link:** https://leetcode.com/problems/nested-list-weight-sum/description

**Problem Statement:**
- Input format: A nested list of integers and lists, and an integer `depth`.
- Constraints: The nested list is non-empty and does not contain empty lists.
- Expected output format: The sum of all integers multiplied by their depth.
- Key requirements and edge cases to consider: Handling nested lists of varying depths and ensuring correct multiplication by depth.
- Example test cases with explanations:
  - `[1,[4,[6]]]` with depth 1 should return `27` because `1 * 1 + 4 * 2 + 6 * 3`.
  - `[1,[4,[6]]]` with depth 2 should return `18` because `1 * 2 + 4 * 3 + 6 * 4`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Recursively traverse the nested list, keeping track of the current depth.
- Step-by-step breakdown of the solution:
  1. Define a recursive function that takes the nested list and the current depth.
  2. For each element in the list, if it's an integer, multiply it by the current depth and add to the sum.
  3. If the element is a list, recursively call the function with the sublist and the next depth level.
- Why this approach comes to mind first: It directly addresses the requirement to sum integers based on their depth in the nested list.

```cpp
class Solution {
public:
    int depthSum(vector<NestedInteger>& nestedList) {
        return helper(nestedList, 1);
    }
    
    int helper(vector<NestedInteger>& nestedList, int depth) {
        int sum = 0;
        for (auto& ni : nestedList) {
            if (ni.isInteger()) {
                sum += ni.getInteger() * depth;
            } else {
                sum += helper(ni.getList(), depth + 1);
            }
        }
        return sum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$ where $N$ is the total number of integers in the nested list, since we visit each integer once.
> - **Space Complexity:** $O(D)$ where $D$ is the maximum depth of the nested list, due to the recursive call stack.
> - **Why these complexities occur:** The time complexity is linear because we process each integer once, and the space complexity is dependent on the maximum recursion depth.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using a single pass through the nested list, maintaining a stack to track the depth of each integer.
- Detailed breakdown of the approach:
  1. Initialize a stack with the initial list and its depth.
  2. While the stack is not empty, pop the top element (a list and its depth).
  3. For each element in the popped list, if it's an integer, add its value times the current depth to the sum.
  4. If it's a list, push it back onto the stack with the next depth level.
- Proof of optimality: This approach visits each integer exactly once, ensuring the time complexity is optimal.

```cpp
class Solution {
public:
    int depthSum(vector<NestedInteger>& nestedList) {
        int sum = 0;
        stack<pair<vector<NestedInteger>, int>> s;
        s.push({nestedList, 1});
        
        while (!s.empty()) {
            auto [list, depth] = s.top();
            s.pop();
            
            for (auto& ni : list) {
                if (ni.isInteger()) {
                    sum += ni.getInteger() * depth;
                } else {
                    s.push({ni.getList(), depth + 1});
                }
            }
        }
        
        return sum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N)$, where $N$ is the total number of integers in the nested list.
> - **Space Complexity:** $O(D)$, where $D$ is the maximum depth of the nested list.
> - **Optimality proof:** This approach ensures each integer is processed exactly once, achieving optimal time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive traversal, stack usage for depth tracking.
- Problem-solving patterns identified: Handling nested structures, using depth to calculate weighted sums.
- Optimization techniques learned: Avoiding unnecessary recursive calls, utilizing a stack for efficient depth management.
- Similar problems to practice: Other problems involving nested lists or trees and depth-based calculations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect depth tracking, missing recursive base cases.
- Edge cases to watch for: Empty lists, lists with varying depths, single-element lists.
- Performance pitfalls: Inefficient recursion, not utilizing stack for depth management.
- Testing considerations: Ensure coverage of different depths, single and multiple integers at each depth.