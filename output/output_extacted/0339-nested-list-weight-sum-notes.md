## Nested List Weight Sum

**Problem Link:** https://leetcode.com/problems/nested-list-weight-sum/description

**Problem Statement:**
- Input format and constraints: The input is a nested list `nestedList` of integers and lists, where each integer is a weight and each list is a nested list. The weights are non-negative integers.
- Expected output format: The output is the sum of each integer multiplied by its depth.
- Key requirements and edge cases to consider: The input list can contain both integers and lists, and the lists can be nested to any depth.
- Example test cases with explanations:
  - Example 1: Input: `[1,[4,[6]],[8,1]]`, Output: `1*1 + 4*2 + 6*3 + 8*2 + 1*3 = 27`
  - Example 2: Input: `[1,[4,[6]],[8,1]]`, Output: `1*1 + 4*2 + 6*3 + 8*2 + 1*3 = 27`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to recursively traverse the nested list and calculate the sum of each integer multiplied by its depth.
- Step-by-step breakdown of the solution:
  1. Define a recursive function that takes a nested list and a depth as input.
  2. Initialize a variable to store the sum of the weights.
  3. Iterate over each element in the nested list.
  4. If the element is an integer, add its weight multiplied by the depth to the sum.
  5. If the element is a list, recursively call the function with the list and the next depth.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, as it directly follows the problem statement.

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
> - **Time Complexity:** $O(n)$, where $n$ is the total number of integers and lists in the nested list, since we visit each element once.
> - **Space Complexity:** $O(d)$, where $d$ is the maximum depth of the nested list, since we use recursive calls to traverse the list.
> - **Why these complexities occur:** The time complexity is linear because we only visit each element once, and the space complexity is dependent on the maximum depth because of the recursive calls.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach, as we must visit each element in the nested list to calculate the sum of its weights.
- Detailed breakdown of the approach:
  1. Define a recursive function that takes a nested list and a depth as input.
  2. Initialize a variable to store the sum of the weights.
  3. Iterate over each element in the nested list.
  4. If the element is an integer, add its weight multiplied by the depth to the sum.
  5. If the element is a list, recursively call the function with the list and the next depth.
- Proof of optimality: This approach is optimal because we must visit each element in the nested list to calculate the sum of its weights, and the recursive approach is the most straightforward way to do this.

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
> - **Time Complexity:** $O(n)$, where $n$ is the total number of integers and lists in the nested list, since we visit each element once.
> - **Space Complexity:** $O(d)$, where $d$ is the maximum depth of the nested list, since we use recursive calls to traverse the list.
> - **Optimality proof:** This approach is optimal because we must visit each element in the nested list to calculate the sum of its weights, and the recursive approach is the most straightforward way to do this.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive traversal of a nested list, calculation of the sum of weights.
- Problem-solving patterns identified: Using recursive calls to traverse a nested list, calculating the sum of weights by multiplying each weight by its depth.
- Optimization techniques learned: Using a recursive approach to simplify the code and reduce the time complexity.
- Similar problems to practice: Other problems involving recursive traversal of nested lists, such as calculating the sum of weights in a nested list with a different structure.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the base case of the recursion, not updating the sum correctly.
- Edge cases to watch for: Handling empty lists, lists with only integers, lists with only lists.
- Performance pitfalls: Using an inefficient data structure, such as a linked list, to store the nested list.
- Testing considerations: Testing the function with different types of input, such as lists with only integers, lists with only lists, and lists with a mix of integers and lists.