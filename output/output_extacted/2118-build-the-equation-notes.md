## Build the Equation
**Problem Link:** https://leetcode.com/problems/build-the-equation/description

**Problem Statement:**
- Given a string `equation` representing a simple equation, return a string representing the equation with the variable `x` isolated on the left side of the equation.
- The input equation will only contain integers, `x`, and the four basic arithmetic operators (`+`, `-`, `*`, `/`).
- The equation will always have an `=` sign separating the left and right sides of the equation.
- The equation will always have exactly one `x` term.
- The equation will always have a solution.

**Example Test Cases:**

* Input: `"2x+3=7"`
* Output: `"x=(7-3)/2"`
* Explanation: To isolate `x`, subtract 3 from both sides and then divide both sides by 2.

* Input: `"x+5=9"`
* Output: `"x=9-5"`
* Explanation: To isolate `x`, subtract 5 from both sides.

* Input: `"5=x"`
* Output: `"x=5"`
* Explanation: The equation is already solved for `x`, so no additional steps are needed.

### Brute Force Approach

**Explanation:**
The brute force approach involves parsing the equation from left to right, identifying the terms containing `x` and the constants, and then applying the necessary operations to isolate `x`.

1. Split the equation into left and right sides based on the `=` sign.
2. Parse each side of the equation to identify the terms containing `x` and the constants.
3. Apply the necessary operations to isolate `x` on the left side of the equation.

```cpp
#include <iostream>
#include <string>
#include <vector>

std::string buildEquation(std::string equation) {
    // Split the equation into left and right sides
    size_t equalsIndex = equation.find('=');
    std::string leftSide = equation.substr(0, equalsIndex);
    std::string rightSide = equation.substr(equalsIndex + 1);

    // Initialize variables to store the coefficients and constants
    int xCoefficient = 0;
    int constant = 0;

    // Parse the left side of the equation
    size_t startIndex = 0;
    while (startIndex < leftSide.size()) {
        size_t endIndex = leftSide.find('+', startIndex);
        if (endIndex == std::string::npos) {
            endIndex = leftSide.find('-', startIndex);
            if (endIndex == std::string::npos) {
                endIndex = leftSide.size();
            }
        }

        std::string term = leftSide.substr(startIndex, endIndex - startIndex);

        // Check if the term contains 'x'
        if (term.find('x') != std::string::npos) {
            // Extract the coefficient of 'x'
            if (term.size() == 1) {
                xCoefficient += 1;
            } else {
                xCoefficient += std::stoi(term.substr(0, term.size() - 1));
            }
        } else {
            // Extract the constant
            constant -= std::stoi(term);
        }

        startIndex = endIndex;
    }

    // Parse the right side of the equation
    startIndex = 0;
    while (startIndex < rightSide.size()) {
        size_t endIndex = rightSide.find('+', startIndex);
        if (endIndex == std::string::npos) {
            endIndex = rightSide.find('-', startIndex);
            if (endIndex == std::string::npos) {
                endIndex = rightSide.size();
            }
        }

        std::string term = rightSide.substr(startIndex, endIndex - startIndex);

        // Check if the term contains 'x'
        if (term.find('x') != std::string::npos) {
            // Extract the coefficient of 'x'
            if (term.size() == 1) {
                xCoefficient -= 1;
            } else {
                xCoefficient -= std::stoi(term.substr(0, term.size() - 1));
            }
        } else {
            // Extract the constant
            constant += std::stoi(term);
        }

        startIndex = endIndex;
    }

    // Construct the final equation
    std::string finalEquation = "x=";

    // Check if the coefficient of 'x' is 1
    if (xCoefficient == 1) {
        finalEquation += std::to_string(constant);
    } else if (xCoefficient == -1) {
        finalEquation += "-" + std::to_string(-constant);
    } else {
        finalEquation += "(" + std::to_string(constant) + ")/" + std::to_string(xCoefficient);
    }

    return finalEquation;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input equation. This is because we are scanning the equation from left to right to parse the terms.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input equation. This is because we are storing the parsed terms in variables.
> - **Why these complexities occur:** The time complexity occurs because we are scanning the equation from left to right, and the space complexity occurs because we are storing the parsed terms in variables.

### Optimal Approach (Required)

**Explanation:**
The optimal approach involves using a similar strategy as the brute force approach but with some optimizations.

1. Split the equation into left and right sides based on the `=` sign.
2. Parse each side of the equation to identify the terms containing `x` and the constants.
3. Apply the necessary operations to isolate `x` on the left side of the equation.

```cpp
#include <iostream>
#include <string>
#include <vector>

std::string buildEquation(std::string equation) {
    // Split the equation into left and right sides
    size_t equalsIndex = equation.find('=');
    std::string leftSide = equation.substr(0, equalsIndex);
    std::string rightSide = equation.substr(equalsIndex + 1);

    // Initialize variables to store the coefficients and constants
    int xCoefficient = 0;
    int constant = 0;

    // Parse the left side of the equation
    size_t startIndex = 0;
    while (startIndex < leftSide.size()) {
        size_t endIndex = leftSide.find('+', startIndex);
        if (endIndex == std::string::npos) {
            endIndex = leftSide.find('-', startIndex);
            if (endIndex == std::string::npos) {
                endIndex = leftSide.size();
            }
        }

        std::string term = leftSide.substr(startIndex, endIndex - startIndex);

        // Check if the term contains 'x'
        if (term.find('x') != std::string::npos) {
            // Extract the coefficient of 'x'
            if (term.size() == 1) {
                xCoefficient += 1;
            } else if (term[0] == '-') {
                xCoefficient -= 1;
            } else {
                xCoefficient += std::stoi(term.substr(0, term.size() - 1));
            }
        } else {
            // Extract the constant
            if (term[0] == '-') {
                constant -= std::stoi(term.substr(1));
            } else {
                constant += std::stoi(term);
            }
        }

        startIndex = endIndex;
    }

    // Parse the right side of the equation
    startIndex = 0;
    while (startIndex < rightSide.size()) {
        size_t endIndex = rightSide.find('+', startIndex);
        if (endIndex == std::string::npos) {
            endIndex = rightSide.find('-', startIndex);
            if (endIndex == std::string::npos) {
                endIndex = rightSide.size();
            }
        }

        std::string term = rightSide.substr(startIndex, endIndex - startIndex);

        // Check if the term contains 'x'
        if (term.find('x') != std::string::npos) {
            // Extract the coefficient of 'x'
            if (term.size() == 1) {
                xCoefficient -= 1;
            } else if (term[0] == '-') {
                xCoefficient += 1;
            } else {
                xCoefficient -= std::stoi(term.substr(0, term.size() - 1));
            }
        } else {
            // Extract the constant
            if (term[0] == '-') {
                constant += std::stoi(term.substr(1));
            } else {
                constant -= std::stoi(term);
            }
        }

        startIndex = endIndex;
    }

    // Construct the final equation
    std::string finalEquation = "x=";

    // Check if the coefficient of 'x' is 1
    if (xCoefficient == 1) {
        finalEquation += std::to_string(constant);
    } else if (xCoefficient == -1) {
        finalEquation += "-" + std::to_string(-constant);
    } else {
        finalEquation += "(" + std::to_string(constant) + ")/" + std::to_string(xCoefficient);
    }

    return finalEquation;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input equation. This is because we are scanning the equation from left to right to parse the terms.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input equation. This is because we are storing the parsed terms in variables.
> - **Optimality proof:** The optimal approach has the same time and space complexity as the brute force approach but with some optimizations. It correctly handles the cases where the coefficient of 'x' is 1 or -1 and constructs the final equation accordingly.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: parsing equations, identifying terms, and applying operations to isolate variables.
- Problem-solving patterns identified: splitting equations into left and right sides, parsing terms, and applying operations to isolate variables.
- Optimization techniques learned: handling special cases where the coefficient of 'x' is 1 or -1.

**Mistakes to Avoid:**
- Not handling special cases where the coefficient of 'x' is 1 or -1.
- Not correctly parsing the terms in the equation.
- Not applying the correct operations to isolate 'x'.

**Similar Problems to Practice:**
- Solving linear equations with multiple variables.
- Solving quadratic equations.
- Solving systems of linear equations.