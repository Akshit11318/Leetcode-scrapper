## Valid Number
**Problem Link:** https://leetcode.com/problems/valid-number/description

**Problem Statement:**
- Input format and constraints: The input is a string `s` that may contain digits, decimal points, exponents, and signs.
- Expected output format: A boolean indicating whether the input string is a valid number or not.
- Key requirements and edge cases to consider: 
    - The input string may contain whitespace characters.
    - The input string may be empty.
    - The input string may contain invalid characters (e.g., letters).
- Example test cases with explanations:
    - "0" is a valid number.
    - "0.1" is a valid number.
    - "abc" is not a valid number.
    - "1 a" is not a valid number.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking each character in the input string to determine if it is a valid number.
- Step-by-step breakdown of the solution: 
    1. Check if the input string is empty.
    2. Check if the input string contains any invalid characters (e.g., letters).
    3. Check if the input string contains a decimal point and if it is in a valid position.
    4. Check if the input string contains an exponent and if it is in a valid position.
    5. Check if the input string contains a sign and if it is in a valid position.
- Why this approach comes to mind first: This approach is straightforward and involves checking each character in the input string.

```cpp
bool isNumber(string s) {
    // Remove leading and trailing whitespace characters
    s.erase(0, s.find_first_not_of(" "));
    s.erase(s.find_last_not_of(" ") + 1);

    // Check if the input string is empty
    if (s.empty()) return false;

    bool seen_e = false, seen_dot = false, seen_digit = false;
    for (int i = 0; i < s.size(); i++) {
        if (isdigit(s[i])) seen_digit = true;
        else if (s[i] == 'e' || s[i] == 'E') {
            if (seen_e || !seen_digit) return false;
            seen_e = true;
            seen_digit = false;
        } else if (s[i] == '.') {
            if (seen_dot || seen_e) return false;
            seen_dot = true;
        } else if (s[i] == '+' || s[i] == '-') {
            if (i != 0 && s[i - 1] != 'e' && s[i - 1] != 'E') return false;
        } else return false;
    }

    return seen_digit;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we are checking each character in the string.
> - **Space Complexity:** $O(1)$, because we are not using any additional data structures that scale with the input size.
> - **Why these complexities occur:** The time complexity occurs because we are checking each character in the input string. The space complexity occurs because we are not using any additional data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a finite state machine to check if the input string is a valid number.
- Detailed breakdown of the approach: 
    1. Initialize a set of states (e.g., start, integer, fraction, exponent).
    2. Initialize a set of transitions between states based on the input characters.
    3. Iterate through the input string and update the current state based on the transitions.
    4. If the final state is a valid state (e.g., integer, fraction), then the input string is a valid number.
- Proof of optimality: The optimal solution has a time complexity of $O(n)$ and a space complexity of $O(1)$, which is the best possible complexity for this problem.
- Why further optimization is impossible: Further optimization is impossible because we must check each character in the input string to determine if it is a valid number.

```cpp
bool isNumber(string s) {
    // Remove leading and trailing whitespace characters
    s.erase(0, s.find_first_not_of(" "));
    s.erase(s.find_last_not_of(" ") + 1);

    // Initialize states and transitions
    enum State { START, INTEGER, FRACTION, EXPONENT, END };
    enum CharType { DIGIT, DOT, E, SIGN, OTHER };
    vector<vector<State>> transitions = {
        {START, INTEGER, START, START, START},  // START
        {INTEGER, INTEGER, FRACTION, EXPONENT, END},  // INTEGER
        {FRACTION, FRACTION, END, EXPONENT, END},  // FRACTION
        {EXPONENT, INTEGER, END, END, END},  // EXPONENT
        {END, END, END, END, END}  // END
    };

    // Initialize current state
    State currentState = START;

    // Iterate through input string
    for (char c : s) {
        CharType charType;
        if (isdigit(c)) charType = DIGIT;
        else if (c == '.') charType = DOT;
        else if (c == 'e' || c == 'E') charType = E;
        else if (c == '+' || c == '-') charType = SIGN;
        else charType = OTHER;

        // Update current state
        currentState = transitions[currentState][charType];

        // If current state is END, return false
        if (currentState == END) return false;
    }

    // If final state is INTEGER or FRACTION, return true
    return currentState == INTEGER || currentState == FRACTION;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we are checking each character in the string.
> - **Space Complexity:** $O(1)$, because we are not using any additional data structures that scale with the input size.
> - **Optimality proof:** The optimal solution has a time complexity of $O(n)$ and a space complexity of $O(1)$, which is the best possible complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Finite state machines, transitions between states.
- Problem-solving patterns identified: Checking each character in the input string, using a finite state machine to determine if the input string is a valid number.
- Optimization techniques learned: Using a finite state machine to reduce the time complexity.
- Similar problems to practice: Validating IP addresses, validating email addresses.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for invalid characters, not checking for valid positions of decimal points and exponents.
- Edge cases to watch for: Empty input strings, input strings with whitespace characters, input strings with invalid characters.
- Performance pitfalls: Not using a finite state machine, not checking each character in the input string.
- Testing considerations: Testing with different input strings, testing with different edge cases.