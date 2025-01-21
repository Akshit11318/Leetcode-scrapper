## Restore IP Addresses

**Problem Link:** https://leetcode.com/problems/restore-ip-addresses/description

**Problem Statement:**
- Input: A string `s` containing only digits.
- Output: All possible valid IP addresses that can be formed by inserting dots into `s`.
- Key requirements: Each part of the IP address must be between 0 and 255 (inclusive) and must not have leading zeros (except for zero itself).
- Example test cases: 
  - Input: "25525511135"
  - Output: ["255.255.11.135","255.255.111.35"]
  - Input: "0000"
  - Output: ["0.0.0.0"]
  - Input: "101023"
  - Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of inserting dots into the string `s`.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of inserting 3 dots into `s`.
  2. For each combination, split `s` into 4 parts.
  3. Check if each part is a valid IP segment (between 0 and 255, and no leading zeros).
  4. If all parts are valid, add the IP address to the result list.
- Why this approach comes to mind first: It's the most straightforward way to solve the problem by trying all possibilities.

```cpp
class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> result;
        int n = s.length();
        for (int i = 1; i < n && i < 4; i++) {
            for (int j = i + 1; j < n && j < i + 3; j++) {
                for (int k = j + 1; k < n && k < j + 3; k++) {
                    string s1 = s.substr(0, i);
                    string s2 = s.substr(i, j - i);
                    string s3 = s.substr(j, k - j);
                    string s4 = s.substr(k);
                    if (isValid(s1) && isValid(s2) && isValid(s3) && isValid(s4)) {
                        result.push_back(s1 + "." + s2 + "." + s3 + "." + s4);
                    }
                }
            }
        }
        return result;
    }

    bool isValid(string s) {
        if (s.length() > 1 && s[0] == '0') return false;
        int num = stoi(s);
        return num >= 0 && num <= 255;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the length of the string `s`. This is because in the worst case, we are generating all possible combinations of inserting dots into `s`.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we need to store the result list.
> - **Why these complexities occur:** These complexities occur because we are trying all possible combinations of inserting dots into `s`, which results in exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use backtracking to generate all possible combinations of IP segments.
- Detailed breakdown of the approach:
  1. Define a helper function to check if a string is a valid IP segment.
  2. Define another helper function to backtrack and generate all possible combinations of IP segments.
  3. In the backtracking function, try all possible lengths for the current IP segment (1, 2, or 3).
  4. If the current IP segment is valid, recursively call the backtracking function for the next IP segment.
  5. If we have generated 4 IP segments, add the IP address to the result list.
- Proof of optimality: This approach is optimal because we are only trying valid combinations of IP segments, which reduces the search space significantly.

```cpp
class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> result;
        backtrack(result, s, 0, {});
        return result;
    }

    void backtrack(vector<string>& result, string s, int start, vector<string> path) {
        if (path.size() == 4) {
            if (start == s.length()) {
                string ip = path[0];
                for (int i = 1; i < 4; i++) {
                    ip += "." + path[i];
                }
                result.push_back(ip);
            }
            return;
        }
        for (int i = 1; i <= 3; i++) {
            if (start + i > s.length()) break;
            string segment = s.substr(start, i);
            if (isValid(segment)) {
                path.push_back(segment);
                backtrack(result, s, start + i, path);
                path.pop_back();
            }
        }
    }

    bool isValid(string s) {
        if (s.length() > 1 && s[0] == '0') return false;
        int num = stoi(s);
        return num >= 0 && num <= 255;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(3^n)$, where $n$ is the length of the string `s`. This is because in the worst case, we are trying all possible combinations of IP segments.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we need to store the result list and the recursion stack.
> - **Optimality proof:** This approach is optimal because we are only trying valid combinations of IP segments, which reduces the search space significantly.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Backtracking, string manipulation.
- Problem-solving patterns identified: Using backtracking to generate all possible combinations of IP segments.
- Optimization techniques learned: Reducing the search space by only trying valid combinations of IP segments.
- Similar problems to practice: Other problems that involve generating all possible combinations of something, such as permutations or subsets.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for valid IP segments, not handling edge cases.
- Edge cases to watch for: Empty string, string with less than 4 characters, string with more than 12 characters.
- Performance pitfalls: Trying all possible combinations of inserting dots into the string, which results in exponential time complexity.
- Testing considerations: Test the solution with different inputs, including edge cases and large inputs.