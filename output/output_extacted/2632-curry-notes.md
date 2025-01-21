## Curry
**Problem Link:** https://leetcode.com/problems/curry/description

**Problem Statement:**
- Input format and constraints: The problem asks us to implement a function that takes in a function and returns a curried version of that function. The input function can take any number of arguments.
- Expected output format: The output should be a curried version of the input function.
- Key requirements and edge cases to consider: The curried function should be able to handle any number of arguments and should be able to be called with any number of arguments at a time.
- Example test cases with explanations:
  - `curry(add)(1)(2)(3)` should return `6`, where `add` is a function that takes in any number of arguments and returns their sum.
  - `curry(multiply)(2)(3)(4)` should return `24`, where `multiply` is a function that takes in any number of arguments and returns their product.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach would be to create a new function that takes in the input function and returns a new function that takes in the first argument. This new function would then return another function that takes in the second argument, and so on.
- Step-by-step breakdown of the solution: We would create a recursive function that takes in the input function and the current arguments. If the number of arguments is equal to the number of arguments the input function takes, we would call the input function with the arguments. Otherwise, we would return a new function that takes in the next argument.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it can be inefficient and hard to implement.

```cpp
class Solution {
public:
    template <typename... Args>
    auto curry(std::function<int(Args...)> func) {
        return [func](auto... args) {
            if constexpr (sizeof...(args) == sizeof...(Args)) {
                return func(args...);
            } else {
                return curry([func, args...](auto... rest) {
                    return func(args..., rest...);
                });
            }
        };
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of arguments the input function takes.
> - **Space Complexity:** $O(n)$, where $n$ is the number of arguments the input function takes.
> - **Why these complexities occur:** The time and space complexities occur because we are recursively creating new functions that take in the next argument.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `std::function` to store the input function and the current arguments. We can then use a lambda function to create a new function that takes in the next argument.
- Detailed breakdown of the approach: We would create a `std::function` that takes in the input function and the current arguments. We would then use a lambda function to create a new function that takes in the next argument. If the number of arguments is equal to the number of arguments the input function takes, we would call the input function with the arguments.
- Proof of optimality: This approach is optimal because it uses a `std::function` to store the input function and the current arguments, which is more efficient than recursively creating new functions.
- Why further optimization is impossible: Further optimization is impossible because we need to store the input function and the current arguments, and using a `std::function` is the most efficient way to do so.

```cpp
class Solution {
public:
    template <typename... Args>
    auto curry(std::function<int(Args...)> func) {
        return [func](auto... args) mutable {
            if constexpr (sizeof...(args) == sizeof...(Args)) {
                return func(args...);
            } else {
                return curry([func, args...](auto... rest) {
                    return func(args..., rest...);
                });
            }
        };
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of arguments the input function takes.
> - **Space Complexity:** $O(n)$, where $n$ is the number of arguments the input function takes.
> - **Optimality proof:** This approach is optimal because it uses a `std::function` to store the input function and the current arguments, which is more efficient than recursively creating new functions.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the concept of currying, which is a technique of transforming a function that takes multiple arguments into a sequence of functions, each taking a single argument.
- Problem-solving patterns identified: The problem identifies the pattern of using a `std::function` to store the input function and the current arguments, which is a common technique in functional programming.
- Optimization techniques learned: The problem demonstrates the technique of using a lambda function to create a new function that takes in the next argument, which is a common technique in functional programming.
- Similar problems to practice: Similar problems to practice include implementing a `map` function, an `filter` function, and a `reduce` function.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to forget to use the `mutable` keyword when creating a lambda function that captures variables by value.
- Edge cases to watch for: An edge case to watch for is when the input function takes no arguments, in which case the curried function should return the result of calling the input function.
- Performance pitfalls: A performance pitfall is to use a recursive function to create a new function that takes in the next argument, which can be inefficient and cause a stack overflow.
- Testing considerations: A testing consideration is to test the curried function with different numbers of arguments, including zero arguments and one argument.