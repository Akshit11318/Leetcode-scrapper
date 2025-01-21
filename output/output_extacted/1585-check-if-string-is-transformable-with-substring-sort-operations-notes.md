## Check if String is Transformable with Substring Sort Operations
**Problem Link:** https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/description

**Problem Statement:**
- Input format: `s` and `t` as strings, `k` as an integer.
- Constraints: $1 \leq s.length \leq 10^5$, $s.length == t.length$, $1 \leq k \leq 10^5$, $s$ and $t$ consist only of lowercase letters.
- Expected output format: `true` if `s` can be transformed into `t` using the given operations, `false` otherwise.
- Key requirements and edge cases to consider: The transformation involves sorting substrings of length `k`. We need to check if `s` can be transformed into `t` by repeatedly sorting substrings of length `k`.
- Example test cases with explanations: 
  - Input: `s = "abc", t = "bac", k = 2` Output: `false` Explanation: You cannot transform "abc" into "bac" by sorting a substring of length 2.
  - Input: `s = "abc", t = "bca", k = 2` Output: `true` Explanation: You can transform "abc" into "bca" by sorting a substring of length 2.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward way to solve this problem is to simulate the transformation process by repeatedly sorting substrings of length `k`.
- Step-by-step breakdown of the solution:
  1. Start with the input string `s`.
  2. For each possible substring of length `k` in `s`, sort the substring.
  3. Check if the resulting string is equal to `t`.
- Why this approach comes to mind first: This approach directly implements the transformation process described in the problem statement.

```cpp
class Solution {
public:
    bool isTransformable(string s, string t, int k) {
        // Input validation
        if (s.length() != t.length()) {
            return false;
        }
        
        // Initialize a copy of the input string
        string current = s;
        
        // Simulate the transformation process
        while (true) {
            bool transformed = false;
            for (int i = 0; i <= current.length() - k; i++) {
                string substr = current.substr(i, k);
                sort(substr.begin(), substr.end());
                if (substr != current.substr(i, k)) {
                    // Sort the substring
                    current.replace(i, k, substr);
                    transformed = true;
                }
            }
            // If no transformation occurred in the last iteration, break the loop
            if (!transformed) {
                break;
            }
        }
        
        // Check if the final transformed string is equal to t
        return current == t;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k \cdot log(k))$, where $n$ is the length of the input string. This is because in the worst case, we might need to sort all substrings of length `k`.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we need to store the transformed string.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, which has a time complexity of $O(k \cdot log(k))$. The space complexity is due to the storage of the transformed string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a more efficient data structure to keep track of the positions of characters in the string. Specifically, we can use a `map` to store the positions of each character.
- Detailed breakdown of the approach:
  1. Initialize a `map` to store the positions of each character in the string `s`.
  2. For each character in the string `t`, check if the positions of the characters in `s` are valid. Specifically, we need to check if the position of the current character in `s` is less than or equal to the position of the previous character in `s`.
- Proof of optimality: This approach is optimal because it only requires a single pass through the string `t`, and it uses a `map` to keep track of the positions of characters in `s`. This results in a significant improvement in time complexity compared to the brute force approach.

```cpp
class Solution {
public:
    bool isTransformable(string s, string t, int k) {
        // Input validation
        if (s.length() != t.length()) {
            return false;
        }
        
        // Initialize a map to store the positions of each character
        map<char, vector<int>> pos;
        for (int i = 0; i < s.length(); i++) {
            pos[s[i]].push_back(i);
        }
        
        // Check if the positions of characters in s are valid
        for (int i = 0; i < t.length(); i++) {
            char c = t[i];
            if (pos[c].empty()) {
                return false;
            }
            int p = pos[c].back();
            pos[c].pop_back();
            for (char j = 'a'; j < c; j++) {
                if (!pos[j].empty() && pos[j].back() < p) {
                    return false;
                }
            }
        }
        
        return true;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we only need to make a single pass through the string `t`.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we need to store the positions of characters in the string `s`.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the string `t`, and it uses a `map` to keep track of the positions of characters in `s`. This results in a significant improvement in time complexity compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The use of a `map` to keep track of the positions of characters in the string `s`.
- Problem-solving patterns identified: The use of a more efficient data structure to improve the time complexity of the solution.
- Optimization techniques learned: The use of a `map` to reduce the time complexity of the solution.
- Similar problems to practice: Other problems that involve using a `map` to keep track of the positions of characters in a string.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the positions of characters in `s` are valid.
- Edge cases to watch for: The case where the input strings `s` and `t` are empty.
- Performance pitfalls: Not using a `map` to keep track of the positions of characters in `s`, resulting in a higher time complexity.
- Testing considerations: Testing the solution with different input strings `s` and `t`, and with different values of `k`.