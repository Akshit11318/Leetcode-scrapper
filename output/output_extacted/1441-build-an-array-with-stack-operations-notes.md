## Build an Array with Stack Operations
**Problem Link:** https://leetcode.com/problems/build-an-array-with-stack-operations/description

**Problem Statement:**
- Input: `target` array and `n` integer
- Constraints: `1 <= target.length <= 100`, `1 <= n <= 100`
- Expected output: a list of `push` and `pop` operations to build the `target` array
- Key requirements: 
  - Start with an empty stack.
  - For each number in the `target` array, if it is not in the stack, `push` it.
  - If it is in the stack, `pop` it from the stack.
- Edge cases: 
  - If the `target` array is empty, return an empty list.
  - If `n` is less than the maximum value in the `target` array, it is impossible to build the `target` array.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to iterate through the `target` array and for each number, check if it is in the stack.
- If it is not in the stack, `push` it. If it is in the stack, `pop` it from the stack.
- This approach comes to mind first because it directly follows the problem statement.

```cpp
class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string> result;
        int j = 1;
        for (int i = 0; i < target.size(); i++) {
            while (j < target[i]) {
                result.push_back("Push");
                result.push_back("Pop");
                j++;
            }
            result.push_back("Push");
            j++;
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the size of the `target` array and $m$ is the maximum value in the `target` array.
> - **Space Complexity:** $O(n \cdot m)$ for storing the result.
> - **Why these complexities occur:** The while loop inside the for loop causes the time complexity to be $O(n \cdot m)$, and the space complexity is $O(n \cdot m)$ because in the worst case, we might need to store $n \cdot m$ operations.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is to realize that we only need to `push` each number in the `target` array once.
- We can use a single loop to iterate through the `target` array and for each number, `push` it and then `push` and `pop` all the numbers between the current number and the next number in the `target` array.
- This approach is optimal because it has a linear time complexity.

```cpp
class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string> result;
        int j = 1;
        for (int i = 0; i < target.size(); i++) {
            while (j < target[i]) {
                result.push_back("Push");
                result.push_back("Pop");
                j++;
            }
            result.push_back("Push");
            j++;
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the size of the `target` array and $m$ is the maximum value in the `target` array.
> - **Space Complexity:** $O(n \cdot m)$ for storing the result.
> - **Optimality proof:** This is the best possible time complexity because we need to at least read the input array and write the output array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: iteration, conditional statements, and stack operations.
- Problem-solving patterns identified: using a while loop inside a for loop to handle the `push` and `pop` operations.
- Optimization techniques learned: reducing the number of operations by only `push`ing each number in the `target` array once.
- Similar problems to practice: other problems involving stack operations and iteration.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to increment the index `j` after `push`ing and `pop`ing a number.
- Edge cases to watch for: an empty `target` array or `n` being less than the maximum value in the `target` array.
- Performance pitfalls: using unnecessary nested loops or recursive function calls.
- Testing considerations: testing the function with different input arrays and values of `n`.