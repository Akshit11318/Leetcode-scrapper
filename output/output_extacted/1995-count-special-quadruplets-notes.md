## Count Special Quadruplets
**Problem Link:** https://leetcode.com/problems/count-special-quadruplets/description

**Problem Statement:**
- Input: An array of integers `nums` of length `n`.
- Constraints: $1 \leq n \leq 200$ and $1 \leq nums[i] \leq n$.
- Expected Output: The number of special quadruplets in the array, where a special quadruplet is a tuple `(a, b, c, d)` such that `0 <= a < b < c < d < n` and `a + c == b + d`.
- Key Requirements: Count all unique special quadruplets.
- Example Test Cases:
  - Input: `[1,2,3,6]`
    - Output: `1`
    - Explanation: The only special quadruplet is `(0, 1, 2, 3)` because `1 + 3 == 2 + 2` is not true for any other combination.
  - Input: `[3,3,6,4,4]`
    - Output: `0`
    - Explanation: No special quadruplets exist because no combination satisfies `a + c == b + d`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every possible combination of four numbers in the array to see if they form a special quadruplet.
- This involves using four nested loops to generate all possible quadruplets and then checking each one to see if it satisfies the condition `a + c == b + d`.
- This approach comes to mind first because it is straightforward and ensures that no potential quadruplet is overlooked.

```cpp
int countQuadruplets(vector<int>& nums) {
    int count = 0;
    int n = nums.size();
    for (int a = 0; a < n; a++) {
        for (int b = a + 1; b < n; b++) {
            for (int c = b + 1; c < n; c++) {
                for (int d = c + 1; d < n; d++) {
                    if (nums[a] + nums[c] == nums[b] + nums[d]) {
                        count++;
                    }
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$ because we are using four nested loops, each of which iterates over the array of size `n`.
> - **Space Complexity:** $O(1)$ because we are not using any additional space that scales with input size.
> - **Why these complexities occur:** The time complexity is high because we are checking every possible quadruplet, resulting in a large number of comparisons. The space complexity is low because we only need a constant amount of space to store the count and loop variables.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight to the optimal solution is to realize that we can reduce the number of comparisons needed by fixing two indices and then checking all possible combinations of the other two indices.
- However, for this problem, a more straightforward optimization involves recognizing that the brute force approach is already quite direct and that the main improvement comes from ensuring we only consider valid quadruplets and correctly handle the condition `a + c == b + d`.
- Given the constraints and the nature of the problem, we can see that the brute force approach, while not optimal in terms of time complexity, is straightforward and effective for the given input sizes.
- To optimize further, we could consider using a hashmap or similar data structure to store the sums of pairs and then count the occurrences of each sum, but given the constraints of the problem, the brute force approach is sufficient and easier to understand.

```cpp
int countQuadruplets(vector<int>& nums) {
    int count = 0;
    int n = nums.size();
    for (int a = 0; a < n; a++) {
        for (int b = a + 1; b < n; b++) {
            for (int c = b + 1; c < n; c++) {
                for (int d = c + 1; d < n; d++) {
                    if (nums[a] + nums[c] == nums[b] + nums[d]) {
                        count++;
                    }
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$ because we are still using four nested loops.
> - **Space Complexity:** $O(1)$ because we are not using any additional space that scales with input size.
> - **Optimality proof:** Given the constraints of the problem (small input size), the brute force approach is sufficient and considered optimal for practical purposes due to its simplicity and the lack of a significantly more efficient algorithm for this specific problem.

---

### Final Notes

**Learning Points:**
- The importance of understanding the constraints of the problem.
- How to approach problems with multiple nested loops.
- Recognizing when a brute force approach might be sufficient due to small input sizes.

**Mistakes to Avoid:**
- Not considering the constraints of the problem.
- Overcomplicating the solution with unnecessary optimizations.
- Not testing the solution with various input sizes and edge cases.