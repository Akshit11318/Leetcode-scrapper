## Reverse Substrings Between Each Pair of Parentheses

**Problem Link:** https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description

**Problem Statement:**
- Input format: a string `s` containing parentheses and letters.
- Constraints: `1 <= s.length <= 2 * 10^4`, `s[i]` is either a lowercase letter or a parenthesis.
- Expected output format: the modified string where every substring enclosed in parentheses is reversed.
- Key requirements and edge cases to consider: handle nested parentheses, empty substrings, and single-character substrings.
- Example test cases with explanations:
  - Input: `(abcd)`, Output: `dcba`
  - Input: `(u(love)i)`, Output: `iloveu`
  - Input: `(ed(et(oc))el)`, Output: `leetcode`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: iterate through the string and whenever we encounter an opening parenthesis, start storing the characters until we find the corresponding closing parenthesis.
- Step-by-step breakdown of the solution:
  1. Iterate through the string.
  2. When an opening parenthesis is encountered, store the characters until the corresponding closing parenthesis is found.
  3. Reverse the stored substring.
  4. Replace the original substring (including parentheses) with the reversed substring.
- Why this approach comes to mind first: it directly addresses the requirement of reversing substrings between parentheses.

```cpp
#include <iostream>
#include <string>
using namespace std;

string reverseParentheses(string s) {
    while (s.find('(') != string::npos) {
        int start = s.rfind('(');
        int end = s.find(')', start);
        string substr = s.substr(start + 1, end - start - 1);
        string reversed = "";
        for (int i = substr.length() - 1; i >= 0; i--) {
            reversed += substr[i];
        }
        s.replace(start, end - start + 1, reversed);
    }
    return s;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string. The `find` and `rfind` operations are $O(n)$, and in the worst case, we might have to perform these operations for each character in the string.
> - **Space Complexity:** $O(n)$, for storing the reversed substrings.
> - **Why these complexities occur:** The brute force approach involves repeated string operations, which are inherently expensive in terms of time and space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: use a stack to keep track of the characters and parentheses. When we encounter a closing parenthesis, pop characters from the stack until we find the corresponding opening parenthesis, reverse the popped characters, and then push them back onto the stack.
- Detailed breakdown of the approach:
  1. Initialize an empty stack.
  2. Iterate through the string. For each character:
     - If it's an opening parenthesis, push it onto the stack.
     - If it's a closing parenthesis, pop characters from the stack until we find the corresponding opening parenthesis, reverse the popped characters, and then push them back onto the stack.
     - If it's a letter, push it onto the stack.
  3. After iterating through the entire string, the stack will contain the modified string with all substrings between parentheses reversed.
- Proof of optimality: this approach ensures that we only reverse each substring once and avoid unnecessary string operations, leading to a significant improvement in efficiency.

```cpp
#include <iostream>
#include <string>
#include <stack>
using namespace std;

string reverseParentheses(string s) {
    stack<char> st;
    for (char c : s) {
        if (c == '(') {
            st.push(c);
        } else if (c == ')') {
            string temp = "";
            while (st.top() != '(') {
                temp += st.top();
                st.pop();
            }
            st.pop(); // Remove the '('
            for (char ch : temp) {
                st.push(ch);
            }
        } else {
            st.push(c);
        }
    }
    string result = "";
    while (!st.empty()) {
        result = st.top() + result;
        st.pop();
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. We perform a constant amount of work for each character in the string.
> - **Space Complexity:** $O(n)$, for the stack used to store the characters.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the string and uses a stack to efficiently manage the characters and parentheses.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: using a stack to manage nested structures (parentheses), and reversing substrings efficiently.
- Problem-solving patterns identified: identifying the need for a stack when dealing with nested structures, and optimizing string operations by minimizing the number of reversals.
- Optimization techniques learned: using a stack to avoid repeated string operations and reducing the time complexity from $O(n^2)$ to $O(n)$.
- Similar problems to practice: other string manipulation problems involving parentheses or nested structures.

**Mistakes to Avoid:**
- Common implementation errors: not properly handling the case when there are multiple nested parentheses, or not correctly reversing the substrings.
- Edge cases to watch for: empty strings, single-character strings, and strings with unbalanced parentheses.
- Performance pitfalls: using inefficient string operations or not optimizing the reversal of substrings.
- Testing considerations: thoroughly testing the solution with a variety of inputs, including edge cases and large strings.