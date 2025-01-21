## Beautiful Array
**Problem Link:** [https://leetcode.com/problems/beautiful-array/description](https://leetcode.com/problems/beautiful-array/description)

**Problem Statement:**
- Input format and constraints: The problem takes an integer `n` as input and asks to find a beautiful array of size `n`. A beautiful array is an array such that for any two different indices `i` and `j`, if `i` is even, then `nums[i] > nums[j]`, and if `i` is odd, then `nums[i] < nums[j]`.
- Expected output format: The function should return a beautiful array of size `n`.
- Key requirements and edge cases to consider: The array should be beautiful and of size `n`. If `n` is 1, the function should return `[1]`.
- Example test cases with explanations:
  - For `n = 4`, the function could return `[2, 1, 3, 4]` because for any two different indices `i` and `j`, if `i` is even, then `nums[i] > nums[j]`, and if `i` is odd, then `nums[i] < nums[j]`.
  - For `n = 3`, the function could return `[3, 1, 2]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking all possible permutations of numbers from 1 to `n` and verifying if each permutation satisfies the conditions of a beautiful array.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of numbers from 1 to `n`.
  2. For each permutation, check if it satisfies the conditions of a beautiful array.
  3. If a permutation satisfies the conditions, return it as a beautiful array.
- Why this approach comes to mind first: This approach comes to mind first because it is a straightforward way to solve the problem. However, it is not efficient because it involves generating all permutations of numbers from 1 to `n`, which has a time complexity of $O(n!)$. 

```cpp
class Solution {
public:
    vector<int> beautifulArray(int n) {
        vector<int> nums(n);
        for (int i = 0; i < n; i++) {
            nums[i] = i + 1;
        }
        vector<vector<int>> permutations;
        permute(nums, 0, n - 1, permutations);
        for (auto& perm : permutations) {
            if (isBeautiful(perm)) {
                return perm;
            }
        }
        return {};
    }

    void permute(vector<int>& nums, int left, int right, vector<vector<int>>& permutations) {
        if (left == right) {
            permutations.push_back(nums);
        } else {
            for (int i = left; i <= right; i++) {
                swap(nums[left], nums[i]);
                permute(nums, left + 1, right, permutations);
                swap(nums[left], nums[i]);
            }
        }
    }

    bool isBeautiful(vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < nums.size(); j++) {
                if (i != j) {
                    if (i % 2 == 0 && nums[i] <= nums[j]) {
                        return false;
                    }
                    if (i % 2 == 1 && nums[i] >= nums[j]) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$ because we are generating all permutations of numbers from 1 to `n`.
> - **Space Complexity:** $O(n!)$ because we are storing all permutations of numbers from 1 to `n`.
> - **Why these complexities occur:** These complexities occur because we are using a brute force approach to solve the problem.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a divide-and-conquer approach to construct a beautiful array. We can start with a base case of `[1]` and then recursively construct a beautiful array of size `n` by combining two beautiful arrays of smaller sizes.
- Detailed breakdown of the approach:
  1. Start with a base case of `[1]`.
  2. Recursively construct a beautiful array of size `n` by combining two beautiful arrays of smaller sizes.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(n)$ and a space complexity of $O(n)$, which is much more efficient than the brute force approach.
- Why further optimization is impossible: Further optimization is impossible because we need to construct a beautiful array of size `n`, which requires at least $O(n)$ time and space.

```cpp
class Solution {
public:
    vector<int> beautifulArray(int n) {
        vector<int> res = {1};
        while (res.size() < n) {
            vector<int> tmp;
            for (int x : res) {
                if (x * 2 - 1 <= n) {
                    tmp.push_back(x * 2 - 1);
                }
            }
            for (int x : res) {
                if (x * 2 <= n) {
                    tmp.push_back(x * 2);
                }
            }
            res = tmp;
        }
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we are constructing a beautiful array of size `n` using a divide-and-conquer approach.
> - **Space Complexity:** $O(n)$ because we are storing a beautiful array of size `n`.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n)$ and a space complexity of $O(n)$, which is much more efficient than the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Divide-and-conquer approach, recursive construction of a beautiful array.
- Problem-solving patterns identified: Using a base case and recursively constructing a solution.
- Optimization techniques learned: Using a divide-and-conquer approach to reduce time and space complexity.
- Similar problems to practice: Constructing a beautiful array with different conditions, such as a beautiful array with a different parity condition.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the base case correctly, not recursively constructing the solution correctly.
- Edge cases to watch for: Handling the case where `n` is 1, handling the case where `n` is even or odd.
- Performance pitfalls: Using a brute force approach, not using a divide-and-conquer approach to reduce time and space complexity.
- Testing considerations: Testing the function with different inputs, testing the function with edge cases.