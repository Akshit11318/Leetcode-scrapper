## Find the K-th Character in String Game I
**Problem Link:** https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/description

**Problem Statement:**
- Given a string `s` and an integer `k`, find the `k-th` character in the string `s` after a certain number of operations.
- The string `s` is transformed into a new string by replacing each character with two characters: the character itself and a character that is `1` greater than the current character in the ASCII table.
- This process is repeated `n` times, where `n` is the number of operations.
- The input string `s` only contains lowercase English letters.
- The integer `k` is in the range `[1, 2^(n+1) - 1]`.
- The expected output is a single character, which is the `k-th` character in the final string after `n` operations.

**Example Test Cases:**
- Input: `s = "a", k = 2, n = 1`
  - Output: `"b"`
- Input: `s = "a", k = 3, n = 2`
  - Output: `"d"`

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to simulate the transformation process `n` times and then find the `k-th` character in the final string.
- This approach involves creating a new string at each step by replacing each character with two characters: the character itself and the character that is `1` greater than the current character in the ASCII table.

```cpp
class Solution {
public:
    string kthCharacter(string s, int k, int n) {
        string current = s;
        for (int i = 0; i < n; i++) {
            string next;
            for (char c : current) {
                next += c;
                next += (char)(c + 1);
            }
            current = next;
        }
        return string(1, current[k - 1]);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n} \cdot |s|)$, where $|s|$ is the length of the string `s`. This is because we are simulating the transformation process `n` times, and at each step, we are creating a new string that is approximately twice the length of the previous string.
> - **Space Complexity:** $O(2^{n} \cdot |s|)$, where $|s|$ is the length of the string `s`. This is because we need to store the intermediate strings at each step.
> - **Why these complexities occur:** These complexities occur because we are using a brute force approach to simulate the transformation process. We are creating a new string at each step, which requires both time and space proportional to the length of the string.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is to notice that the `k-th` character in the final string can be determined without simulating the entire transformation process.
- We can use a recursive approach to find the `k-th` character. At each step, we can determine whether the `k-th` character is in the first half or the second half of the string.
- If `k` is in the first half, we can recursively find the `k-th` character in the first half. If `k` is in the second half, we can recursively find the `(k - 2^i)`-th character in the first half, where `i` is the current step.

```cpp
class Solution {
public:
    string kthCharacter(string s, int k, int n) {
        return helper(s, k, n);
    }
    
    char helper(string s, int k, int n) {
        if (n == 0) {
            return s[k - 1];
        }
        int len = (1 << n) * s.size();
        if (k <= len / 2) {
            return helper(s, k, n - 1);
        } else {
            return (char)(helper(s, k - len / 2, n - 1) + 1);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where `n` is the number of operations. This is because we are using a recursive approach to find the `k-th` character, and the maximum depth of the recursion tree is `n`.
> - **Space Complexity:** $O(n)$, where `n` is the number of operations. This is because we need to store the recursive call stack.
> - **Optimality proof:** This is the optimal solution because we are using a recursive approach to find the `k-th` character, which avoids simulating the entire transformation process.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: recursive approach, divide-and-conquer strategy.
- Problem-solving patterns identified: using recursion to avoid simulating the entire process.
- Optimization techniques learned: using a recursive approach to reduce the time and space complexity.

**Mistakes to Avoid:**
- Common implementation errors: not handling the base case correctly in the recursive approach.
- Edge cases to watch for: handling the case where `k` is in the first half or the second half of the string.
- Performance pitfalls: using a brute force approach to simulate the entire transformation process.
- Testing considerations: testing the solution with different inputs, including edge cases.