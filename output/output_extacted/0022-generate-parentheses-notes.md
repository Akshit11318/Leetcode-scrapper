## Generate Parentheses

**Problem Link:** https://leetcode.com/problems/generate-parentheses/description

**Problem Statement:**
- Input format and constraints: The problem takes an integer `n` as input, representing the number of pairs of parentheses to generate. The input is guaranteed to be a non-negative integer.
- Expected output format: The function should return a vector of strings, where each string is a valid combination of `n` pairs of parentheses.
- Key requirements and edge cases to consider: The function should generate all possible combinations of `n` pairs of parentheses, ensuring that each combination is valid (i.e., every opening parenthesis has a corresponding closing parenthesis).
- Example test cases with explanations:
  - For `n = 3`, the output should include strings like `"((()))"`, `"(()())"`, and `"()(())"`, among others.
  - For `n = 1`, the output should be `["()"]`.
  - For `n = 0`, the output should be `[""]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach to solving this problem might involve generating all possible combinations of `n` pairs of parentheses and then filtering out the invalid combinations.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of `n` pairs of parentheses.
  2. Check each combination to ensure it is valid (i.e., every opening parenthesis has a corresponding closing parenthesis).
  3. If a combination is valid, add it to the result list.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it can be inefficient for large values of `n`.

```cpp
#include <vector>
#include <string>

void generate(vector<string>& result, string current, int open, int close, int n) {
    if (current.size() == 2 * n) {
        result.push_back(current);
        return;
    }
    
    if (open < n) {
        generate(result, current + "(", open + 1, close, n);
    }
    
    if (close < open) {
        generate(result, current + ")", open, close + 1, n);
    }
}

vector<string> generateParenthesis(int n) {
    vector<string> result;
    generate(result, "", 0, 0, n);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^n / n^{3/2})$, where $n$ is the input integer. This is because there are $2n$ characters in each valid combination, and the number of valid combinations is given by the $n$-th Catalan number, which has an asymptotic formula of $4^n / n^{3/2}$.
> - **Space Complexity:** $O(4^n / n^{3/2})$, where $n$ is the input integer. This is because we need to store all the valid combinations in the result list.
> - **Why these complexities occur:** These complexities occur because we are generating all possible combinations of `n` pairs of parentheses and checking each combination for validity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible combinations and filtering out the invalid ones, we can use a recursive approach to generate only the valid combinations.
- Detailed breakdown of the approach:
  1. Start with an empty string and a count of opening and closing parentheses.
  2. If the count of opening parentheses is less than `n`, recursively add an opening parenthesis and increment the count.
  3. If the count of closing parentheses is less than the count of opening parentheses, recursively add a closing parenthesis and increment the count.
  4. If the length of the string is equal to `2 * n`, add the string to the result list.
- Proof of optimality: This approach is optimal because it generates only the valid combinations of `n` pairs of parentheses, avoiding the overhead of generating and filtering out invalid combinations.
- Why further optimization is impossible: This approach has a time complexity of $O(4^n / n^{3/2})$, which is the minimum time complexity required to generate all valid combinations of `n` pairs of parentheses.

```cpp
#include <vector>
#include <string>

void generate(vector<string>& result, string current, int open, int close, int n) {
    if (current.size() == 2 * n) {
        result.push_back(current);
        return;
    }
    
    if (open < n) {
        generate(result, current + "(", open + 1, close, n);
    }
    
    if (close < open) {
        generate(result, current + ")", open, close + 1, n);
    }
}

vector<string> generateParenthesis(int n) {
    vector<string> result;
    generate(result, "", 0, 0, n);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^n / n^{3/2})$, where $n$ is the input integer. This is because we are generating all valid combinations of `n` pairs of parentheses, and the number of valid combinations is given by the $n$-th Catalan number, which has an asymptotic formula of $4^n / n^{3/2}$.
> - **Space Complexity:** $O(4^n / n^{3/2})$, where $n$ is the input integer. This is because we need to store all the valid combinations in the result list.
> - **Optimality proof:** This approach is optimal because it generates only the valid combinations of `n` pairs of parentheses, avoiding the overhead of generating and filtering out invalid combinations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive approach, backtracking, and Catalan numbers.
- Problem-solving patterns identified: Generating all possible combinations and filtering out invalid ones, and using recursive approach to generate only valid combinations.
- Optimization techniques learned: Avoiding unnecessary computations by generating only valid combinations.
- Similar problems to practice: Generating all possible combinations of a given string, generating all possible permutations of a given array.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, not using recursive approach correctly.
- Edge cases to watch for: Handling `n = 0` and `n = 1` correctly.
- Performance pitfalls: Generating all possible combinations and filtering out invalid ones, which can be inefficient for large values of `n`.
- Testing considerations: Testing the function with different values of `n`, including edge cases like `n = 0` and `n = 1`.