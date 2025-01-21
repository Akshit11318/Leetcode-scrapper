## Length of the Longest Valid Substring
**Problem Link:** https://leetcode.com/problems/length-of-the-longest-valid-substring/description

**Problem Statement:**
- Input: A string `s` containing just the characters `'('` and `')'`.
- Constraints: `1 <= s.length <= 10^5`.
- Expected Output: The length of the longest valid substring.
- Key Requirements: A valid substring is one that has a correct balance of opening and closing parentheses.
- Example Test Cases:
  - Input: `"(()"` - Output: `2` - Explanation: The longest valid substring is `"()"`.
  - Input: `")()())"` - Output: `4` - Explanation: The longest valid substring is `"()()"`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to check every possible substring to see if it's valid.
- This involves iterating over the string and for each starting position, checking all possible ending positions.
- For each substring, we then check if it's valid by ensuring that the number of opening parentheses is equal to the number of closing parentheses at any point.

```cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        int n = s.size();
        int maxLength = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j <= n; j++) {
                string substring = s.substr(i, j - i);
                if (isValid(substring)) {
                    maxLength = max(maxLength, (int)substring.size());
                }
            }
        }
        
        return maxLength;
    }
    
    bool isValid(string s) {
        int balance = 0;
        for (char c : s) {
            if (c == '(') balance++;
            else balance--;
            if (balance < 0) return false;
        }
        return balance == 0;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ - This comes from the nested loops over the string and the validation check for each substring.
> - **Space Complexity:** $O(n)$ - This is for storing the substrings.
> - **Why these complexities occur:** The brute force approach involves checking every possible substring, leading to exponential time complexity due to the nested loops and substring operations.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal approach uses a stack to keep track of the indices of unmatched opening parentheses.
- We initialize the stack with -1 to handle the case where the longest valid substring starts at the beginning of the string.
- We then iterate over the string. When we encounter an opening parenthesis, we push its index onto the stack. When we encounter a closing parenthesis, we pop the top of the stack.
- If the stack is empty after popping (meaning there was no matching opening parenthesis), we push the current index back onto the stack.
- The maximum length of valid substring is then calculated by subtracting the top of the stack from the current index and comparing it with the maximum length found so far.

```cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        int n = s.size();
        int maxLength = 0;
        stack<int> st;
        st.push(-1);
        
        for (int i = 0; i < n; i++) {
            if (s[i] == '(') {
                st.push(i);
            } else {
                st.pop();
                if (st.empty()) {
                    st.push(i);
                } else {
                    maxLength = max(maxLength, i - st.top());
                }
            }
        }
        
        return maxLength;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ - This comes from the single pass through the string.
> - **Space Complexity:** $O(n)$ - This is for the stack in the worst case where all characters are opening parentheses.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the string and uses a stack to efficiently keep track of the indices of unmatched opening parentheses, ensuring that we consider all possible valid substrings.

---

### Final Notes
**Learning Points:**
- The importance of using stacks for parsing and matching problems.
- How to optimize brute force approaches by reducing the number of operations and using data structures efficiently.
- The concept of "balance" in string matching problems and how to maintain it.

**Mistakes to Avoid:**
- Not considering edge cases such as an empty string or a string with only one type of parenthesis.
- Not optimizing the solution for large inputs, leading to performance issues.
- Failing to validate the input and handle errors properly.

By following the optimal approach and understanding the complexities involved, we can efficiently solve the problem of finding the length of the longest valid substring in a given string of parentheses.