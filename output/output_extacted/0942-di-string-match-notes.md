## Di String Match
**Problem Link:** [https://leetcode.com/problems/di-string-match/description](https://leetcode.com/problems/di-string-match/description)

**Problem Statement:**
- Input: A string `s` consisting of only the characters `'D'` and `'I'`.
- Constraints: The length of `s` will be in the range `[1, 1000]`.
- Expected Output: A list of distinct integers that satisfies the conditions:
  - For all `i` where `s[i] == 'D'`, the number at the `i`-th position is less than the number at the `i-1`-th position.
  - For all `i` where `s[i] == 'I'`, the number at the `i`-th position is greater than the number at the `i-1`-th position.
- Key Requirements: The list should contain distinct integers from `0` to `s.length`.
- Example Test Cases:
  - Input: `"IDID"`
    - Output: `[0,4,1,3,2]`
  - Input: `"III"`
    - Output: `[0,1,2,3]`
  - Input: `"DDI"`
    - Output: `[3,2,0,1]`

---

### Brute Force Approach

**Explanation:**
- Initial Thought Process: Generate all permutations of numbers from `0` to `s.length`, then check each permutation to see if it satisfies the conditions given by the string `s`.
- Step-by-Step Breakdown:
  1. Generate all permutations of numbers from `0` to `s.length`.
  2. For each permutation, iterate through `s` and check if the condition is met for each character.
  3. If a permutation satisfies all conditions, return it as the solution.
- Why This Approach Comes to Mind First: It's a straightforward approach that checks all possible solutions.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void generatePermutations(vector<int>& nums, int start, int end, string& s) {
    if (start == end) {
        // Check if the current permutation satisfies the conditions
        bool satisfiesConditions = true;
        for (int i = 1; i < s.length(); ++i) {
            if (s[i] == 'D' && nums[i] >= nums[i-1]) {
                satisfiesConditions = false;
                break;
            }
            if (s[i] == 'I' && nums[i] <= nums[i-1]) {
                satisfiesConditions = false;
                break;
            }
        }
        if (satisfiesConditions) {
            // Print or store the satisfying permutation
            for (int num : nums) {
                cout << num << " ";
            }
            cout << endl;
        }
    } else {
        for (int i = start; i <= end; ++i) {
            swap(nums[start], nums[i]);
            generatePermutations(nums, start + 1, end, s);
            swap(nums[start], nums[i]); // backtrack
        }
    }
}

void bruteForceApproach(string& s) {
    vector<int> nums(s.length());
    for (int i = 0; i < s.length(); ++i) {
        nums[i] = i;
    }
    generatePermutations(nums, 0, s.length() - 1, s);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n)$, where $n$ is the length of the string `s`. This is because there are $n!$ permutations, and for each permutation, we check the conditions in $O(n)$ time.
> - **Space Complexity:** $O(n)$, for storing the permutation and the recursive call stack.
> - **Why These Complexities Occur:** The brute force approach generates all permutations and checks each one, leading to a high time complexity due to the factorial growth of permutations.

---

### Optimal Approach (Required)

**Explanation:**
- Key Insight: Since the numbers must be distinct and range from `0` to `s.length`, we can construct the solution by iterating through `s` and deciding whether to increase or decrease the current number based on the character ('I' or 'D').
- Detailed Breakdown:
  1. Initialize two pointers, `low` and `high`, to `0` and `s.length`, respectively.
  2. Initialize an empty vector `result` to store the solution.
  3. Iterate through `s`. For each character:
    - If the character is 'I', append the current `low` value to `result` and increment `low`.
    - If the character is 'D', append the current `high` value to `result` and decrement `high`.
  4. Return `result` as the solution.
- Proof of Optimality: This approach ensures that the numbers are distinct and satisfy the conditions given by `s`, and it does so in linear time, which is optimal for this problem.

```cpp
vector<int> optimalApproach(string& s) {
    vector<int> result;
    int low = 0, high = s.length();
    for (char c : s) {
        if (c == 'I') {
            result.push_back(low);
            low++;
        } else {
            result.push_back(high);
            high--;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we make a single pass through `s`.
> - **Space Complexity:** $O(n)$, for storing the result.
> - **Optimality Proof:** The optimal approach constructs the solution directly, avoiding unnecessary comparisons and ensuring that the solution is found in linear time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: permutation generation, condition checking, and iterative construction.
- Problem-solving patterns identified: breaking down the problem into smaller sub-problems and solving them iteratively.
- Optimization techniques learned: avoiding unnecessary computations by constructing the solution directly.
- Similar problems to practice: other string and permutation problems that require iterative or recursive solutions.

**Mistakes to Avoid:**
- Common implementation errors: off-by-one errors, incorrect condition checking, and failure to handle edge cases.
- Edge cases to watch for: empty strings, strings with only 'I' or only 'D', and strings with repeated characters.
- Performance pitfalls: using brute force approaches for large inputs, failing to optimize the solution for the given constraints.
- Testing considerations: testing with various inputs, including edge cases, to ensure the solution works correctly.