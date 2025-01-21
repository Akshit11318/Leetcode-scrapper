## Undefined to Null
**Problem Link:** https://leetcode.com/problems/undefined-to-null/description

**Problem Statement:**
- Input format and constraints: The problem involves replacing `undefined` with `null` in a given JSON object.
- Expected output format: The modified JSON object with all occurrences of `undefined` replaced with `null`.
- Key requirements and edge cases to consider: Handling nested objects, arrays, and primitive values.
- Example test cases with explanations:
    - Replacing `undefined` with `null` in a simple object.
    - Handling nested objects and arrays.
    - Preserving primitive values.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Recursively traverse the JSON object and replace `undefined` with `null`.
- Step-by-step breakdown of the solution:
    1. Check if the input is an object or an array.
    2. If it's an object, iterate over its properties and recursively replace `undefined` with `null`.
    3. If it's an array, iterate over its elements and recursively replace `undefined` with `null`.
- Why this approach comes to mind first: It's a straightforward and intuitive solution.

```cpp
#include <iostream>
#include <unordered_map>
#include <vector>

using json = std::unordered_map<std::string, std::any>;

void replaceUndefined(json& obj) {
    for (auto& [key, value] : obj) {
        if (value.type() == typeid(std::nullptr_t)) {
            value = nullptr;
        } else if (value.type() == typeid(json)) {
            replaceUndefined(std::any_cast<json&>(value));
        } else if (value.type() == typeid(std::vector<std::any>)) {
            auto& vec = std::any_cast<std::vector<std::any>&>(value);
            for (auto& elem : vec) {
                if (elem.type() == typeid(json)) {
                    replaceUndefined(std::any_cast<json&>(elem));
                }
            }
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of properties in the JSON object, since we recursively traverse the object.
> - **Space Complexity:** $O(n)$, since we use recursive calls to traverse the object.
> - **Why these complexities occur:** The recursive traversal of the object leads to these complexities.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Using a recursive approach with a stack to avoid excessive recursive calls.
- Detailed breakdown of the approach:
    1. Create a stack to store objects and arrays that need to be processed.
    2. Push the input object onto the stack.
    3. While the stack is not empty, pop an object or array and process it.
    4. If it's an object, iterate over its properties and push any objects or arrays onto the stack.
    5. If it's an array, iterate over its elements and push any objects or arrays onto the stack.
- Proof of optimality: This approach has the same time complexity as the brute force approach but avoids excessive recursive calls.

```cpp
#include <iostream>
#include <unordered_map>
#include <vector>
#include <stack>

using json = std::unordered_map<std::string, std::any>;

void replaceUndefined(json& obj) {
    std::stack<std::any> stack;
    stack.push(obj);

    while (!stack.empty()) {
        auto value = stack.top();
        stack.pop();

        if (value.type() == typeid(json)) {
            auto& obj = std::any_cast<json&>(value);
            for (auto& [key, val] : obj) {
                if (val.type() == typeid(json) || val.type() == typeid(std::vector<std::any>)) {
                    stack.push(val);
                } else if (val.type() == typeid(std::nullptr_t)) {
                    val = nullptr;
                }
            }
        } else if (value.type() == typeid(std::vector<std::any>)) {
            auto& vec = std::any_cast<std::vector<std::any>&>(value);
            for (auto& elem : vec) {
                if (elem.type() == typeid(json) || elem.type() == typeid(std::vector<std::any>)) {
                    stack.push(elem);
                } else if (elem.type() == typeid(std::nullptr_t)) {
                    elem = nullptr;
                }
            }
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of properties in the JSON object, since we use a stack to process objects and arrays.
> - **Space Complexity:** $O(n)$, since we use a stack to store objects and arrays.
> - **Optimality proof:** This approach has the same time complexity as the brute force approach but avoids excessive recursive calls, making it more efficient in practice.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive traversal, stack-based processing.
- Problem-solving patterns identified: Handling nested objects and arrays, preserving primitive values.
- Optimization techniques learned: Using a stack to avoid excessive recursive calls.
- Similar problems to practice: JSON parsing, object traversal.

**Mistakes to Avoid:**
- Common implementation errors: Not handling nested objects and arrays correctly, not preserving primitive values.
- Edge cases to watch for: Handling empty objects and arrays, handling objects with circular references.
- Performance pitfalls: Using excessive recursive calls, not optimizing the algorithm for large inputs.
- Testing considerations: Testing with different input sizes, testing with different types of input data.