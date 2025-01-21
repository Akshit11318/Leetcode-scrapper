## Replace Question Marks in String to Minimize its Value

**Problem Link:** https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/description

**Problem Statement:**
- Input: A string `s` containing digits and question marks.
- Output: Replace all question marks with digits to minimize the value of the resulting string.
- Key Requirements: 
  - The string can contain only digits and question marks.
  - The input string will not be empty.
  - The goal is to minimize the resulting string value.

**Example Test Cases:**
- Input: "0??"
  - Output: "009"
- Input: "9??1"
  - Output: "901"

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of digits for the question marks and compare the resulting strings.
- This approach involves generating all permutations of digits (0-9) for the question marks in the string.

```cpp
class Solution {
public:
    string smallestNumber(string s) {
        vector<string> res;
        dfs(s, "", res);
        sort(res.begin(), res.end());
        return res[0];
    }
    
    void dfs(string s, string path, vector<string>& res) {
        if (s.empty()) {
            res.push_back(path);
            return;
        }
        if (s[0] != '?') {
            dfs(s.substr(1), path + s[0], res);
        } else {
            for (int i = 0; i <= 9; i++) {
                dfs(s.substr(1), path + to_string(i), res);
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(10^n)$, where n is the number of question marks in the string. This is because for each question mark, we have 10 choices (0-9).
> - **Space Complexity:** $O(10^n)$, as in the worst case, we might store all permutations in the `res` vector.
> - **Why these complexities occur:** The exponential time and space complexities are due to the brute force nature of trying all possible digit combinations for each question mark.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to replace question marks with the smallest possible digit (0) unless doing so would lead to a larger number when a smaller digit could be used later.
- We prioritize replacing question marks with '0' when it does not lead to a larger number.
- If we encounter a situation where a larger digit must be used to minimize the number (e.g., after a non-zero digit), we use the smallest possible digit that does not increase the number's value unnecessarily.

```cpp
class Solution {
public:
    string smallestNumber(string s) {
        string res = "";
        for (char c : s) {
            if (c != '?') {
                res += c;
            } else {
                if (res.empty() || res.back() == '0') {
                    res += '0';
                } else {
                    res += '1';
                }
            }
        }
        return res;
    }
};
```

However, this approach needs adjustment because simply appending '0' or '1' based on the previous character does not always yield the minimum number, especially considering the impact of leading zeros and the potential for larger numbers when question marks are replaced with '1' after a non-zero digit.

A more accurate optimal approach involves understanding that to minimize the string value:
- Leading zeros should be avoided.
- After a non-zero digit, '0' should be used to minimize the value.

```cpp
class Solution {
public:
    string smallestNumber(string s) {
        string res = "";
        bool nonZeroEncountered = false;
        for (char c : s) {
            if (c != '?') {
                res += c;
                if (c != '0') nonZeroEncountered = true;
            } else {
                if (res.empty()) {
                    res += '1'; // To avoid leading zeros
                } else if (nonZeroEncountered) {
                    res += '0'; // After a non-zero digit, append '0'
                } else {
                    res += '0'; // Before any non-zero digit, append '0'
                }
            }
        }
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where n is the length of the string, because we make a single pass through the string.
> - **Space Complexity:** $O(n)$, as we build the resulting string of the same length as the input string.
> - **Optimality proof:** This approach is optimal because it ensures that the smallest possible digits are used to replace question marks, avoiding leading zeros and minimizing the value of the resulting string.

---

### Final Notes

**Learning Points:**
- The importance of understanding the problem constraints and the implications of different approaches.
- The concept of minimizing string value by strategically replacing question marks with digits.
- The optimization technique of avoiding unnecessary complexity by directly constructing the optimal solution.

**Mistakes to Avoid:**
- Overcomplicating the solution with unnecessary iterations or permutations.
- Not considering the impact of leading zeros and the strategic placement of digits to minimize the string value.
- Failing to validate the input and handle edge cases properly.