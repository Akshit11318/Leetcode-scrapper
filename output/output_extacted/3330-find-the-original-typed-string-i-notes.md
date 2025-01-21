## Find the Original Typed String I
**Problem Link:** https://leetcode.com/problems/find-the-original-typed-string-i/description

**Problem Statement:**
- Input format: `s` - a string representing the typed string
- Constraints: `1 <= s.length <= 100`
- Expected output format: `string` - the original string before typing errors
- Key requirements and edge cases to consider:
  - The original string is typed with some characters being typed twice
  - The `#` character is used to indicate a backspace
  - If a backspace is encountered, the last character in the string is removed
- Example test cases with explanations:
  - Input: `"ab#c"`
    - Output: `"ac"`
    - Explanation: The original string is `"ac"` because the `#` character removes the `b` character
  - Input: `"ab##"`
    - Output: `""`
    - Explanation: The original string is empty because the `#` characters remove all characters

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Simulate the typing process and keep track of the characters that are typed and removed
- Step-by-step breakdown of the solution:
  1. Initialize an empty string to store the original string
  2. Iterate through each character in the input string
  3. If the character is not a `#`, add it to the original string
  4. If the character is a `#`, remove the last character from the original string if it is not empty
- Why this approach comes to mind first: It is a straightforward simulation of the typing process

```cpp
string findOriginalString(string s) {
  string original;
  for (char c : s) {
    if (c == '#') {
      if (!original.empty()) {
        original.pop_back();
      }
    } else {
      original.push_back(c);
    }
  }
  return original;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string `s`, because we iterate through each character in the string once
> - **Space Complexity:** $O(n)$, because we store the original string which can be up to the length of the input string
> - **Why these complexities occur:** The simulation of the typing process requires iterating through each character in the input string, and storing the original string requires additional space

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Use a stack to simulate the typing process
- Detailed breakdown of the approach:
  1. Initialize an empty stack to store the characters
  2. Iterate through each character in the input string
  3. If the character is not a `#`, push it onto the stack
  4. If the character is a `#`, pop the top character from the stack if it is not empty
  5. After iterating through all characters, the stack contains the original string
- Proof of optimality: The stack-based approach has the same time and space complexity as the brute force approach, but it is more efficient because it uses a stack to simulate the typing process, which reduces the overhead of string operations

```cpp
string findOriginalString(string s) {
  stack<char> st;
  for (char c : s) {
    if (c == '#') {
      if (!st.empty()) {
        st.pop();
      }
    } else {
      st.push(c);
    }
  }
  string original;
  while (!st.empty()) {
    original.push_back(st.top());
    st.pop();
  }
  reverse(original.begin(), original.end());
  return original;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string `s`, because we iterate through each character in the string once
> - **Space Complexity:** $O(n)$, because we store the characters in the stack which can be up to the length of the input string
> - **Optimality proof:** The stack-based approach has the same time and space complexity as the brute force approach, but it is more efficient because it uses a stack to simulate the typing process, which reduces the overhead of string operations

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Simulation of the typing process, use of a stack to simulate the typing process
- Problem-solving patterns identified: Using a stack to simulate a process
- Optimization techniques learned: Using a stack to reduce the overhead of string operations
- Similar problems to practice: Problems that involve simulating a process or using a stack to solve a problem

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the stack is empty before popping a character
- Edge cases to watch for: Handling the case where the input string is empty
- Performance pitfalls: Using a string to simulate the typing process instead of a stack
- Testing considerations: Testing the function with different input strings, including edge cases such as an empty string or a string with only `#` characters.