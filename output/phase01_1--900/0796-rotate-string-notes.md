## Rotate String

**Problem Link:** https://leetcode.com/problems/rotate-string/description

**Problem Statement:**
- Input format and constraints: The problem takes two strings, `s` and `goal`, as input and checks if `s` can be rotated to match `goal`.
- Expected output format: The function should return `true` if `s` can be rotated to match `goal`, and `false` otherwise.
- Key requirements and edge cases to consider: Both strings must have the same length. If they do not, the function should return `false`.
- Example test cases with explanations: 
    - `s = "abcde", goal = "cdeab"` should return `true` because `s` can be rotated to match `goal`.
    - `s = "abcde", goal = "abced"` should return `false` because `s` cannot be rotated to match `goal`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One way to solve this problem is to generate all possible rotations of `s` and check if any of them match `goal`.
- Step-by-step breakdown of the solution: 
    1. Check if `s` and `goal` have the same length. If they do not, return `false`.
    2. Generate all possible rotations of `s`.
    3. Check if any of the rotations match `goal`.
- Why this approach comes to mind first: It is a straightforward and intuitive solution.

```cpp
class Solution {
public:
    bool rotateString(string s, string goal) {
        if (s.length() != goal.length()) {
            return false;
        }
        
        for (int i = 0; i < s.length(); i++) {
            string rotated = s.substr(i, s.length() - i) + s.substr(0, i);
            if (rotated == goal) {
                return true;
            }
        }
        
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of `s`, because we are generating $n$ rotations of `s` and checking each one in $O(n)$ time.
> - **Space Complexity:** $O(n)$, because we are storing each rotation of `s`.
> - **Why these complexities occur:** The time complexity is $O(n^2)$ because we are using a nested loop to generate all rotations of `s`. The space complexity is $O(n)$ because we are storing each rotation of `s`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all rotations of `s`, we can concatenate `s` with itself and check if `goal` is a substring of the concatenated string.
- Detailed breakdown of the approach: 
    1. Check if `s` and `goal` have the same length. If they do not, return `false`.
    2. Concatenate `s` with itself.
    3. Check if `goal` is a substring of the concatenated string.
- Proof of optimality: This solution is optimal because it has a time complexity of $O(n)$, which is the best possible time complexity for this problem.
- Why further optimization is impossible: We must check every character in `s` at least once to determine if `goal` is a rotation of `s`, so a time complexity of $O(n)$ is the best possible.

```cpp
class Solution {
public:
    bool rotateString(string s, string goal) {
        if (s.length() != goal.length()) {
            return false;
        }
        
        string concatenated = s + s;
        return concatenated.find(goal) != string::npos;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of `s`, because we are concatenating `s` with itself and checking if `goal` is a substring of the concatenated string.
> - **Space Complexity:** $O(n)$, because we are storing the concatenated string.
> - **Optimality proof:** This solution is optimal because it has a time complexity of $O(n)$, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: string manipulation, substring checking.
- Problem-solving patterns identified: using concatenation to simplify string rotation.
- Optimization techniques learned: reducing the number of operations by using a more efficient algorithm.
- Similar problems to practice: other string manipulation problems, such as checking if a string is a palindrome or finding the longest common substring between two strings.

**Mistakes to Avoid:**
- Common implementation errors: not checking if `s` and `goal` have the same length before attempting to rotate `s`.
- Edge cases to watch for: when `s` and `goal` have different lengths.
- Performance pitfalls: using an inefficient algorithm that has a high time complexity.
- Testing considerations: testing the function with different input strings, including edge cases such as empty strings and strings with different lengths.