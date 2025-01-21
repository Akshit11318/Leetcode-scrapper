## Maximum Number of Operations to Reduce Integer to 0
**Problem Link:** https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/description

**Problem Statement:**
- Input: `num`, `target`
- Constraints: `1 <= num, target <= 10^9`
- Output: Maximum number of operations to reduce `num` to `target`
- Key requirements: Each operation can either decrement `num` by 1 or divide it by 2 if it's even
- Edge cases: When `num` is less than `target`, return 0

**Example Test Cases:**
- `num = 3`, `target = 2` -> 1
- `num = 5`, `target = 3` -> 2

---

### Brute Force Approach
**Explanation:**
- Start with the given number `num` and iteratively apply the two possible operations: decrement by 1 or divide by 2 if even.
- For each operation, check if the resulting number is equal to `target`. If it is, return the number of operations performed.
- If not, continue applying operations until `num` becomes less than `target` or we reach a predetermined maximum number of operations to avoid infinite loops.

```cpp
class Solution {
public:
    int maxOperations(int num, int target) {
        int maxOps = 0;
        dfs(num, target, 0, maxOps);
        return maxOps;
    }
    
    void dfs(int num, int target, int ops, int& maxOps) {
        if (num == target) {
            maxOps = max(maxOps, ops);
            return;
        }
        if (num < target || ops > 1000) return; // arbitrary max ops to prevent infinite loop
        
        // Decrement by 1
        dfs(num - 1, target, ops + 1, maxOps);
        
        // Divide by 2 if even
        if (num % 2 == 0) {
            dfs(num / 2, target, ops + 1, maxOps);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$ where $n$ is the number of bits in `num`, due to the recursive nature of the DFS.
> - **Space Complexity:** $O(n)$ for the recursion stack.
> - **Why these complexities occur:** The brute force approach explores all possible paths of operations, leading to exponential time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Since we're looking to maximize the number of operations, we should always choose the operation that reduces `num` the most, which is dividing by 2 when `num` is even.
- We can use a greedy approach, starting from `num` and iteratively applying the operations until we reach `target`.
- If at any point `num` becomes less than `target`, we know that the optimal path involves only decrements from this point onwards.

```cpp
class Solution {
public:
    int maxOperations(int num, int target) {
        int ops = 0;
        while (num > target) {
            if (num % 2 == 0) {
                num /= 2;
            } else {
                num -= 1;
            }
            ops++;
        }
        return ops;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$ where $n$ is `num`, because in the worst case, we divide `num` by 2 until it reaches `target`.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store `ops` and `num`.
> - **Optimality proof:** This approach is optimal because it always chooses the operation that reduces `num` the most, ensuring the maximum number of operations.

---

### Final Notes
**Learning Points:**
- Greedy algorithms can be very effective for optimization problems where the locally optimal choice leads to a globally optimal solution.
- Understanding the problem constraints and identifying the most reducing operation can significantly simplify the solution.

**Mistakes to Avoid:**
- Not considering the greedy approach for optimization problems.
- Failing to recognize the importance of choosing the most reducing operation in each step.
- Not optimizing the solution for the given constraints, leading to inefficient algorithms.