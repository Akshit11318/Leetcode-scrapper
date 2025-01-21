## Letter Case Permutation

**Problem Link:** https://leetcode.com/problems/letter-case-permutation/description

**Problem Statement:**
- Input: A string `s` containing lowercase letters and digits.
- Output: A list of all possible letter case permutations of `s`.
- Key requirements: The solution should handle strings of varying lengths and generate all possible permutations, considering each letter can be either lowercase or uppercase.
- Example test cases:
  - Input: `s = "a1b2"`
  - Output: `["a1b2","a1B2","A1b2","A1B2"]`
  - Input: `s = "3z4"`
  - Output: `["3z4","3Z4"]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all permutations by iterating through each character and deciding whether to convert it to uppercase or keep it as is (if it's a letter), then store the resulting strings.
- Step-by-step breakdown of the solution:
  1. Check if the character is a letter.
  2. If it's a letter, generate two permutations: one with the letter in lowercase and one with it in uppercase.
  3. If it's not a letter (i.e., it's a digit), keep it as is and move on to the next character.
- Why this approach comes to mind first: It's a straightforward way to ensure all possible permutations are considered.

```cpp
void backtrack(string s, int start, vector<string>& result) {
    if (start == s.size()) {
        result.push_back(s);
        return;
    }
    
    // If the current character is a letter, try both cases
    if (isalpha(s[start])) {
        s[start] = tolower(s[start]);
        backtrack(s, start + 1, result);
        
        s[start] = toupper(s[start]);
        backtrack(s, start + 1, result);
    } else {
        // If it's not a letter, just move on
        backtrack(s, start + 1, result);
    }
}

vector<string> letterCasePermutation(string s) {
    vector<string> result;
    backtrack(s, 0, result);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string. This is because in the worst case, each character could be a letter, leading to $2^n$ permutations, and for each permutation, we're doing $O(n)$ work to construct the string.
> - **Space Complexity:** $O(2^n \cdot n)$, for storing the result, and $O(n)$ for the recursion stack in the worst case.
> - **Why these complexities occur:** The exponential time and space complexity are due to the recursive nature of the solution and the fact that we're storing all permutations.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The same approach used in the brute force solution is actually optimal because we must generate all permutations to solve the problem. However, we can optimize the code slightly for readability and to avoid unnecessary operations.
- Detailed breakdown of the approach: The approach remains the same as the brute force, but we acknowledge it as optimal due to the problem's nature requiring all permutations.
- Proof of optimality: Since each letter can be either uppercase or lowercase, and there are no other constraints, generating all $2^n$ permutations (where $n$ is the number of letters) is unavoidable for an exact solution.

```cpp
void backtrack(string& s, int start, vector<string>& result) {
    if (start == s.size()) {
        result.push_back(s);
        return;
    }
    
    if (isalpha(s[start])) {
        char original = s[start];
        s[start] = tolower(s[start]);
        backtrack(s, start + 1, result);
        
        s[start] = toupper(original);
        backtrack(s, start + 1, result);
    } else {
        backtrack(s, start + 1, result);
    }
}

vector<string> letterCasePermutation(string s) {
    vector<string> result;
    backtrack(s, 0, result);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string and also accounts for the number of letters since non-letters don't branch the recursion.
> - **Space Complexity:** $O(2^n \cdot n)$ for the result and $O(n)$ for the recursion stack.
> - **Optimality proof:** This solution is optimal because it must generate all possible permutations to meet the problem's requirements, and it does so with minimal overhead.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursion, backtracking, and permutation generation.
- Problem-solving patterns identified: The need to consider all possible states (in this case, uppercase and lowercase for letters) when generating permutations.
- Optimization techniques learned: While the optimal solution has the same time complexity as the brute force, recognizing the necessity of generating all permutations is key to understanding why further optimization is not possible.

**Mistakes to Avoid:**
- Not considering all possible cases for letters (both uppercase and lowercase).
- Not handling non-letter characters correctly (they should not cause the function to branch into additional recursive calls).
- Failing to understand the exponential nature of permutation problems and the implications for time and space complexity.