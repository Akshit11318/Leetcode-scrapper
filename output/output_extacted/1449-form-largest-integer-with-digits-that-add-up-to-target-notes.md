## Form Largest Integer with Digits That Add Up to Target
**Problem Link:** https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/description

**Problem Statement:**
- Input format and constraints: Given an array of digits and a target integer, form the largest possible integer using these digits such that the sum of the digits in the formed integer is equal to the target.
- Expected output format: A string representing the largest integer that can be formed.
- Key requirements and edge cases to consider: The input array may contain duplicates, and the target may not be achievable with the given digits.
- Example test cases with explanations: 
    - Input: `digits = [3,6,2,6,1,4,3,5,4], target = 12`
      Output: `"6214"`
    - Input: `digits = [1,1,1,1,1,1], target = 6`
      Output: `"111111"`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate all permutations of the input array and check each permutation to see if its sum equals the target. If it does, compare it with the current maximum integer.
- Step-by-step breakdown of the solution:
    1. Generate all permutations of the input array.
    2. For each permutation, calculate the sum of its elements.
    3. If the sum equals the target, form the integer by concatenating the digits and update the maximum integer if necessary.
- Why this approach comes to mind first: It's straightforward and ensures all possibilities are considered, but it's inefficient due to the large number of permutations for big inputs.

```cpp
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

void backtrack(vector<int>& digits, int start, vector<int>& path, int target, string& max_str) {
    if (target == 0) {
        string curr_str;
        for (int num : path) curr_str += to_string(num);
        if (curr_str.length() > max_str.length() || (curr_str.length() == max_str.length() && curr_str > max_str)) {
            max_str = curr_str;
        }
    } else {
        for (int i = start; i < digits.size(); ++i) {
            if (digits[i] > target) continue;
            path.push_back(digits[i]);
            backtrack(digits, i + 1, path, target - digits[i], max_str);
            path.pop_back();
        }
    }
}

string largestNumber(vector<int>& digits, int target) {
    sort(digits.rbegin(), digits.rend());
    string max_str = "";
    vector<int> path;
    backtrack(digits, 0, path, target, max_str);
    return max_str;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of digits, because in the worst case, we generate all subsets of the input array.
> - **Space Complexity:** $O(n)$, for storing the recursion stack and the current path.
> - **Why these complexities occur:** The brute force approach generates all possible subsets of the input array, leading to exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use dynamic programming to store the maximum integer that can be formed for each possible sum from 1 to the target, and for each digit from the input array. This avoids recalculating the same subproblems multiple times.
- Detailed breakdown of the approach:
    1. Initialize a dynamic programming table `dp` where `dp[i][j]` represents the maximum integer that can be formed using the first `i` digits to achieve a sum of `j`.
    2. Fill the `dp` table by iterating over the digits and the possible sums, updating `dp[i][j]` based on whether including the current digit improves the maximum integer.
    3. The final answer is stored in `dp[n][target]`, where `n` is the number of digits.

```cpp
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

string largestNumber(vector<int>& digits, int target) {
    int n = digits.size();
    vector<vector<string>> dp(n + 1, vector<string>(target + 1, ""));
    
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= target; ++j) {
            if (digits[i - 1] <= j) {
                string incl = dp[i - 1][j - digits[i - 1]];
                if (incl.length() > 0) incl += to_string(digits[i - 1]);
                else incl = to_string(digits[i - 1]);
                if (incl.length() > dp[i - 1][j].length() || (incl.length() == dp[i - 1][j].length() && incl > dp[i - 1][j])) {
                    dp[i][j] = incl;
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            } else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }
    
    return dp[n][target];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot target)$, where $n$ is the number of digits, because we fill the `dp` table once.
> - **Space Complexity:** $O(n \cdot target)$, for storing the `dp` table.
> - **Optimality proof:** This approach is optimal because it uses dynamic programming to avoid recalculating the same subproblems, reducing the time complexity significantly compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, recursion, and backtracking.
- Problem-solving patterns identified: Breaking down the problem into smaller subproblems and using memoization to avoid redundant calculations.
- Optimization techniques learned: Using dynamic programming to reduce time complexity.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases properly, such as when the target cannot be achieved with the given digits.
- Edge cases to watch for: Duplicates in the input array, target being too large or too small.
- Performance pitfalls: Using the brute force approach for large inputs, which can lead to exponential time complexity.
- Testing considerations: Testing with different input sizes, target values, and edge cases to ensure the solution works correctly and efficiently.