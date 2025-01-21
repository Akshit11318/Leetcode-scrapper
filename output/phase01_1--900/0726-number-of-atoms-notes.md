## Number of Atoms
**Problem Link:** https://leetcode.com/problems/number-of-atoms/description

**Problem Statement:**
- Input format: A string `formula` representing a chemical formula.
- Constraints: The input string `formula` will always be a valid chemical formula.
- Expected output format: A string representing the count of each atom in the chemical formula.
- Key requirements and edge cases to consider:
  - Handle parentheses to represent groups of atoms.
  - Handle numbers to represent the count of atoms or groups.
  - Handle uppercase and lowercase letters to distinguish between different atoms.
- Example test cases with explanations:
  - Input: `"H2O"` - Output: `"H2O"`
  - Input: `"Mg(OH)2"` - Output: `"H2MgO2"`
  - Input: `"K4(ON(F))2"` - Output: `"F2K4N2O4"`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Parse the string character by character, handling each type of character (uppercase letter, lowercase letter, digit, or parenthesis) separately.
- Step-by-step breakdown of the solution:
  1. Initialize a stack to store the intermediate results.
  2. Iterate over the string, and for each character:
    - If the character is an uppercase letter, push it onto the stack with a count of 1.
    - If the character is a lowercase letter, update the last element in the stack with the new character.
    - If the character is a digit, update the count of the last element in the stack.
    - If the character is an opening parenthesis, push a new element onto the stack with a count of 1.
    - If the character is a closing parenthesis, pop elements from the stack until the matching opening parenthesis is found, and update the counts accordingly.
- Why this approach comes to mind first: It's a straightforward way to handle the different types of characters in the string.

```cpp
#include <iostream>
#include <stack>
#include <string>
#include <map>

using namespace std;

string countOfAtoms(string formula) {
    stack<map<string, int>> st;
    st.push({});
    for (int i = 0; i < formula.size(); i++) {
        if (isupper(formula[i])) {
            string atom = "";
            atom += formula[i];
            if (i + 1 < formula.size() && islower(formula[i + 1])) {
                atom += formula[i + 1];
                i++;
            }
            if (i + 1 < formula.size() && isdigit(formula[i + 1])) {
                int j = i + 1;
                while (j < formula.size() && isdigit(formula[j])) j++;
                int count = stoi(formula.substr(i + 1, j - i - 1));
                i = j - 1;
                st.top()[atom] += count;
            } else {
                st.top()[atom]++;
            }
        } else if (isdigit(formula[i])) {
            int j = i;
            while (j < formula.size() && isdigit(formula[j])) j++;
            int count = stoi(formula.substr(i, j - i));
            i = j - 1;
            st.top()[atom] *= count;
        } else if (formula[i] == '(') {
            st.push({});
        } else if (formula[i] == ')') {
            map<string, int> curr = st.top();
            st.pop();
            for (auto& [atom, count] : curr) {
                st.top()[atom] += count;
            }
        }
    }
    map<string, int> result = st.top();
    string ans = "";
    for (auto& [atom, count] : result) {
        ans += atom;
        if (count > 1) ans += to_string(count);
    }
    return ans;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we iterate over the string once.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to push $n/2$ elements onto the stack.
> - **Why these complexities occur:** The time complexity is linear because we only iterate over the string once, and the space complexity is linear because in the worst case, we might need to store $n/2$ elements on the stack.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Use a stack to store the intermediate results, and handle the characters in the string based on their types.
- Detailed breakdown of the approach:
  1. Initialize a stack to store the intermediate results.
  2. Iterate over the string, and for each character:
    - If the character is an uppercase letter, push it onto the stack with a count of 1.
    - If the character is a lowercase letter, update the last element in the stack with the new character.
    - If the character is a digit, update the count of the last element in the stack.
    - If the character is an opening parenthesis, push a new element onto the stack with a count of 1.
    - If the character is a closing parenthesis, pop elements from the stack until the matching opening parenthesis is found, and update the counts accordingly.
- Proof of optimality: This approach is optimal because it only iterates over the string once and uses a stack to store the intermediate results, resulting in a time complexity of $O(n)$.

```cpp
#include <iostream>
#include <stack>
#include <string>
#include <map>

using namespace std;

string countOfAtoms(string formula) {
    stack<map<string, int>> st;
    st.push({});
    int i = 0;
    while (i < formula.size()) {
        if (isupper(formula[i])) {
            string atom = "";
            atom += formula[i];
            if (i + 1 < formula.size() && islower(formula[i + 1])) {
                atom += formula[i + 1];
                i++;
            }
            i++;
            int count = 0;
            while (i < formula.size() && isdigit(formula[i])) {
                count = count * 10 + formula[i] - '0';
                i++;
            }
            if (count == 0) count = 1;
            st.top()[atom] += count;
        } else if (formula[i] == '(') {
            st.push({});
            i++;
        } else if (formula[i] == ')') {
            i++;
            int count = 0;
            while (i < formula.size() && isdigit(formula[i])) {
                count = count * 10 + formula[i] - '0';
                i++;
            }
            if (count == 0) count = 1;
            map<string, int> curr = st.top();
            st.pop();
            for (auto& [atom, c] : curr) {
                st.top()[atom] += c * count;
            }
        }
    }
    map<string, int> result = st.top();
    string ans = "";
    for (auto& [atom, count] : result) {
        ans += atom;
        if (count > 1) ans += to_string(count);
    }
    return ans;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we iterate over the string once.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to push $n/2$ elements onto the stack.
> - **Optimality proof:** This approach is optimal because it only iterates over the string once and uses a stack to store the intermediate results, resulting in a time complexity of $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a stack to store intermediate results, handling characters in a string based on their types.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems, using a stack to store the intermediate results.
- Optimization techniques learned: Using a stack to store the intermediate results, iterating over the string only once.
- Similar problems to practice: Parsing strings, using stacks to store intermediate results.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the characters in the string correctly, not using a stack to store the intermediate results.
- Edge cases to watch for: Handling the case where the input string is empty, handling the case where the input string contains only one type of character.
- Performance pitfalls: Not using a stack to store the intermediate results, iterating over the string multiple times.
- Testing considerations: Testing the function with different input strings, testing the function with edge cases.