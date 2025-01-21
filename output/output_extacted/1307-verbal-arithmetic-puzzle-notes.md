## Verbal Arithmetic Puzzle
**Problem Link:** https://leetcode.com/problems/verbal-arithmetic-puzzle/description

**Problem Statement:**
- Input format: You are given a string `equation` representing a verbal arithmetic puzzle, where each word is a variable.
- Constraints: Each variable is a lowercase letter, and the length of each variable is at most 10.
- Expected output format: Return `true` if there exists an assignment of integers to variables that makes the equation true, and `false` otherwise.
- Key requirements and edge cases to consider: 
    - The equation must be true when the variables are replaced with their assigned integers.
    - Each variable should be assigned a unique integer between 0 and 9.
    - The first character of each variable cannot be 0.
- Example test cases with explanations: 
    - "a + b = c" can be true if a = 1, b = 2, and c = 3.
    - "a + a = b" cannot be true because a and b must be distinct.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible assignments of integers to variables and check if the equation holds true.
- Step-by-step breakdown of the solution: 
    1. Generate all permutations of integers from 0 to 9 for the variables.
    2. For each permutation, replace the variables in the equation with their assigned integers.
    3. Evaluate the equation and check if it is true.
    4. If a true equation is found, return `true`.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to try all possible combinations.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

bool isSolvable(string equation) {
    vector<char> vars;
    for (char c : equation) {
        if (isalpha(c) && find(vars.begin(), vars.end(), c) == vars.end()) {
            vars.push_back(c);
        }
    }

    vector<int> perm(10);
    for (int i = 0; i < 10; i++) {
        perm[i] = i;
    }

    do {
        unordered_map<char, int> assignment;
        for (int i = 0; i < vars.size(); i++) {
            assignment[vars[i]] = perm[i];
        }

        string left = "", right = "";
        int op = 0;
        for (char c : equation) {
            if (c == '+' || c == '=') {
                op++;
            } else if (isalpha(c)) {
                if (op == 0) {
                    left += to_string(assignment[c]);
                } else if (op == 1) {
                    left += to_string(assignment[c]);
                } else {
                    right += to_string(assignment[c]);
                }
            } else {
                left += c;
            }
        }

        int leftVal = stoi(left);
        int rightVal = stoi(right);

        if (leftVal == rightVal) {
            return true;
        }
    } while (next_permutation(perm.begin(), perm.end()));

    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(10!)$ because we are trying all permutations of integers from 0 to 9 for the variables.
> - **Space Complexity:** $O(n)$ where $n$ is the number of variables, because we need to store the permutation and the assignment of integers to variables.
> - **Why these complexities occur:** The time complexity is high because we are trying all possible combinations of integers for the variables, and the space complexity is relatively low because we only need to store a few variables.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a backtracking algorithm to try all possible assignments of integers to variables.
- Detailed breakdown of the approach: 
    1. Create a set of available integers from 0 to 9.
    2. For each variable, try each available integer and recursively check if the equation holds true.
    3. If a true equation is found, return `true`.
    4. If no true equation is found after trying all possible assignments, return `false`.
- Proof of optimality: This approach is optimal because it tries all possible assignments of integers to variables in a systematic way, avoiding unnecessary computations.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
#include <unordered_set>

using namespace std;

bool isSolvable(string equation, unordered_map<char, int>& assignment, unordered_set<int>& used) {
    if (equation.empty()) {
        return true;
    }

    char var = equation[0];
    equation = equation.substr(1);

    if (assignment.find(var) != assignment.end()) {
        return isSolvable(equation, assignment, used);
    }

    for (int i = 0; i <= 9; i++) {
        if (used.find(i) == used.end()) {
            if (var == equation[0] && i == 0) {
                continue;
            }

            assignment[var] = i;
            used.insert(i);

            if (isSolvable(equation, assignment, used)) {
                return true;
            }

            assignment.erase(var);
            used.erase(i);
        }
    }

    return false;
}

bool isSolvable(string equation) {
    unordered_map<char, int> assignment;
    unordered_set<int> used;

    return isSolvable(equation, assignment, used);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(10!)$ because we are trying all possible assignments of integers to variables.
> - **Space Complexity:** $O(n)$ where $n$ is the number of variables, because we need to store the assignment and the set of used integers.
> - **Optimality proof:** This approach is optimal because it tries all possible assignments of integers to variables in a systematic way, avoiding unnecessary computations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Backtracking, recursion, and permutation generation.
- Problem-solving patterns identified: Trying all possible assignments of integers to variables and checking if the equation holds true.
- Optimization techniques learned: Using a backtracking algorithm to avoid unnecessary computations.
- Similar problems to practice: Other problems involving backtracking and recursion, such as the N-Queens problem.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a variable is already assigned an integer before trying a new assignment.
- Edge cases to watch for: The first character of each variable cannot be 0.
- Performance pitfalls: Trying all permutations of integers from 0 to 9 for the variables without using a backtracking algorithm.
- Testing considerations: Test the function with different equations and check if it returns the correct result.