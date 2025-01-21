## Find Permutation
**Problem Link:** [https://leetcode.com/problems/find-permutation/description](https://leetcode.com/problems/find-permutation/description)

**Problem Statement:**
- Input format: A string `s` containing `n` elements and an array `nums` of size `n`.
- Constraints: `1 <= n <= 10^6`, `s` consists of `'D'` and `'I'`, and `nums` is a permutation of numbers from `1` to `n`.
- Expected output format: An array of integers representing a valid permutation of `nums` that satisfies the conditions given in `s`.
- Key requirements and edge cases to consider: The output permutation must satisfy the conditions specified by `s`, where `'D'` indicates a decrease and `'I'` indicates an increase in the permutation.
- Example test cases with explanations: 
  - Input: `s = "IDDDI"`, `nums = [1, 2, 3, 4, 5]`. Output: `[1, 4, 3, 2, 5]`.
  - Input: `s = "DDI"`, `nums = [3, 5, 2]`. Output: `[3, 2, 5]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all permutations of `nums` and check each one against the conditions specified in `s`.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of `nums`.
  2. For each permutation, iterate through `s` and check if the corresponding elements in the permutation satisfy the conditions.
  3. If a permutation satisfies all conditions, return it as the result.
- Why this approach comes to mind first: It's a straightforward way to ensure that we consider all possible permutations.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void generatePermutations(vector<int>& nums, int start, vector<vector<int>>& permutations) {
    if (start == nums.size() - 1) {
        permutations.push_back(nums);
    } else {
        for (int i = start; i < nums.size(); i++) {
            swap(nums[start], nums[i]);
            generatePermutations(nums, start + 1, permutations);
            swap(nums[start], nums[i]);
        }
    }
}

vector<int> findPermutation(string s, vector<int>& nums) {
    vector<vector<int>> permutations;
    generatePermutations(nums, 0, permutations);
    for (const auto& permutation : permutations) {
        bool isValid = true;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == 'I' && permutation[i] >= permutation[i + 1]) {
                isValid = false;
                break;
            } else if (s[i] == 'D' && permutation[i] <= permutation[i + 1]) {
                isValid = false;
                break;
            }
        }
        if (isValid) {
            return permutation;
        }
    }
    return {}; // No valid permutation found
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n)$, where $n$ is the number of elements in `nums`. This is because we generate all permutations of `nums` (which takes $O(n!)$ time) and then check each permutation against the conditions in `s` (which takes $O(n)$ time).
> - **Space Complexity:** $O(n! \cdot n)$, where $n$ is the number of elements in `nums`. This is because we store all permutations of `nums` in memory.
> - **Why these complexities occur:** The brute force approach involves generating all permutations of `nums`, which leads to exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can build the permutation incrementally by maintaining two pointers, one for the next smallest number and one for the next largest number.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `small` and `large`, to the smallest and largest numbers in `nums`, respectively.
  2. Iterate through `s` and build the permutation incrementally. If the current character is `'I'`, append the next smallest number to the permutation and move the `small` pointer. If the current character is `'D'`, append the next largest number to the permutation and move the `large` pointer.
  3. After iterating through `s`, append any remaining numbers to the permutation in ascending order.
- Proof of optimality: This approach ensures that we build a valid permutation in $O(n)$ time, which is optimal because we must at least read the input.

```cpp
vector<int> findPermutation(string s, vector<int>& nums) {
    vector<int> permutation;
    int small = 1, large = nums.size();
    for (char c : s) {
        if (c == 'I') {
            permutation.push_back(small++);
        } else {
            permutation.push_back(large--);
        }
    }
    while (small <= large) {
        permutation.push_back(small++);
    }
    return permutation;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in `nums`. This is because we iterate through `s` and build the permutation incrementally.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in `nums`. This is because we store the permutation in memory.
> - **Optimality proof:** This approach is optimal because we must at least read the input, and we build the permutation in a single pass.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Incremental construction of a permutation, use of two pointers to maintain the next smallest and largest numbers.
- Problem-solving patterns identified: Building a solution incrementally, using pointers to maintain state.
- Optimization techniques learned: Avoiding unnecessary work by building the solution incrementally, using pointers to reduce memory allocation.
- Similar problems to practice: Other permutation-related problems, such as generating all permutations of a given set.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating the `small` and `large` pointers, failing to append remaining numbers to the permutation.
- Edge cases to watch for: Empty input, invalid input characters.
- Performance pitfalls: Using inefficient algorithms, such as generating all permutations and checking each one.
- Testing considerations: Test with different input sizes, edge cases, and invalid inputs.