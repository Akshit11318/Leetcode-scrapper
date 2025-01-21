## Bind Function to Context
**Problem Link:** https://leetcode.com/problems/bind-function-to-context/description

**Problem Statement:**
- Input format and constraints: The problem requires binding a given function to a specific context (object) and returning the bound function.
- Expected output format: The output should be a function that can be called with any number of arguments, and it should call the original function with the given context as `this`.
- Key requirements and edge cases to consider: The bound function should be able to handle any number of arguments, and it should preserve the original function's behavior.
- Example test cases with explanations:
  - Binding a simple function to an object.
  - Binding a function with multiple arguments.
  - Binding a function with default arguments.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a new function that calls the original function with the given context as `this`.
- Step-by-step breakdown of the solution:
  1. Create a new function that takes any number of arguments.
  2. Use the `apply` method to call the original function with the given context as `this`.
- Why this approach comes to mind first: It is a straightforward way to bind a function to a context.

```cpp
class Solution {
public:
    static Function bind(Function fn, Context context) {
        return [fn, context](auto... args) {
            return fn(context, args...);
        };
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we are simply creating a new function and returning it.
> - **Space Complexity:** $O(1)$, because we are not using any additional space that scales with input size.
> - **Why these complexities occur:** The time complexity is constant because we are not iterating over any input, and the space complexity is constant because we are not using any data structures that scale with input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a lambda function to create a closure that captures the original function and context.
- Detailed breakdown of the approach:
  1. Create a lambda function that captures the original function and context.
  2. Use the captured function and context to call the original function.
- Proof of optimality: This approach is optimal because it uses the least amount of code and does not introduce any unnecessary complexity.
- Why further optimization is impossible: We are already using the most efficient way to create a bound function in C++.

```cpp
class Solution {
public:
    static auto bind(auto fn, auto context) {
        return [fn, context](auto... args) {
            return fn(context, args...);
        };
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we are simply creating a new function and returning it.
> - **Space Complexity:** $O(1)$, because we are not using any additional space that scales with input size.
> - **Optimality proof:** This approach is optimal because it uses the least amount of code and does not introduce any unnecessary complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Lambda functions, closures, and function binding.
- Problem-solving patterns identified: Using lambda functions to create closures and bind functions to contexts.
- Optimization techniques learned: Using the most efficient way to create a bound function in C++.
- Similar problems to practice: Binding functions to contexts in other programming languages.

**Mistakes to Avoid:**
- Common implementation errors: Not capturing the original function and context correctly.
- Edge cases to watch for: Handling functions with multiple arguments and default arguments.
- Performance pitfalls: Using unnecessary complexity or data structures that scale with input size.
- Testing considerations: Testing the bound function with different inputs and edge cases.