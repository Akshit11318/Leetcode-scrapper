## Permutations
**Problem Link:** [https://leetcode.com/problems/permutations/description](https://leetcode.com/problems/permutations/description)

**Problem Statement:**
- Input format and constraints: The problem takes an array of distinct integers as input and returns all possible permutations of these integers.
- Expected output format: The output should be a list of lists, where each sublist is a permutation of the input integers.
- Key requirements and edge cases to consider: The input array can contain negative numbers and zero. The length of the input array can vary from 1 to 6.
- Example test cases with explanations:
  - Input: `[1, 2, 3]`
  - Output: `[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To generate all permutations of the input array, we can use a recursive approach where we select each element in the array as the first element of the permutation and then recursively generate all permutations of the remaining elements.
- Step-by-step breakdown of the solution:
  1. Start with an empty permutation.
  2. For each element in the input array, add it to the permutation and recursively generate all permutations of the remaining elements.
  3. Backtrack by removing the last added element from the permutation.
- Why this approach comes to mind first: This approach is intuitive because it follows the natural process of selecting each element as the first element of the permutation and then generating all possible permutations of the remaining elements.

```cpp
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        backtrack(result, nums, 0);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result, vector<int>& nums, int start) {
        if (start == nums.size()) {
            result.push_back(nums);
        }
        for (int i = start; i < nums.size(); i++) {
            swap(nums[start], nums[i]);
            backtrack(result, nums, start + 1);
            swap(nums[start], nums[i]);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the number of elements in the input array. This is because there are $n!$ possible permutations of $n$ distinct elements.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the input array. This is because the maximum depth of the recursion tree is $n$.
> - **Why these complexities occur:** The time complexity occurs because we are generating all possible permutations of the input array, which is $n!$. The space complexity occurs because we need to store the recursion stack, which can go up to a depth of $n$.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach because generating all permutations of an array is an inherently expensive operation that requires $O(n!)$ time.
- Detailed breakdown of the approach:
  1. Use a recursive function to generate all permutations of the input array.
  2. In each recursive call, select each element in the array as the first element of the permutation and recursively generate all permutations of the remaining elements.
  3. Backtrack by removing the last added element from the permutation.
- Proof of optimality: This approach is optimal because it generates all possible permutations of the input array, which is the required output. Any other approach would either not generate all permutations or would do so in a less efficient manner.
- Why further optimization is impossible: Further optimization is impossible because generating all permutations of an array is an inherently expensive operation that requires $O(n!)$ time. Any optimization would need to reduce the number of permutations generated, which is not possible if we need to generate all permutations.

```cpp
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        backtrack(result, nums, 0);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result, vector<int>& nums, int start) {
        if (start == nums.size()) {
            result.push_back(nums);
        }
        for (int i = start; i < nums.size(); i++) {
            swap(nums[start], nums[i]);
            backtrack(result, nums, start + 1);
            swap(nums[start], nums[i]);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the number of elements in the input array. This is because there are $n!$ possible permutations of $n$ distinct elements.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the input array. This is because the maximum depth of the recursion tree is $n$.
> - **Optimality proof:** This approach is optimal because it generates all possible permutations of the input array, which is the required output. Any other approach would either not generate all permutations or would do so in a less efficient manner.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursion, backtracking.
- Problem-solving patterns identified: Generating all permutations of an array.
- Optimization techniques learned: None, because generating all permutations is an inherently expensive operation.
- Similar problems to practice: Generating all combinations of an array, generating all subsets of an array.

**Mistakes to Avoid:**
- Common implementation errors: Not backtracking correctly, not swapping elements correctly.
- Edge cases to watch for: Empty input array, input array with duplicate elements.
- Performance pitfalls: Not using recursion correctly, not using backtracking correctly.
- Testing considerations: Test with different input arrays, test with different sizes of input arrays.