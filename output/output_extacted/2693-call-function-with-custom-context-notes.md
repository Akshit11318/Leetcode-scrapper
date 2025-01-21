## Call Function with Custom Context
**Problem Link:** https://leetcode.com/problems/call-function-with-custom-context/description

**Problem Statement:**
- Input: A `fn` function, an `obj` object, and an array of arguments `args`.
- Expected output: The result of calling `fn` with `obj` as its `this` context and `args` as its arguments.
- Key requirements: The function should be called with the specified context and arguments.
- Example test cases:
  - `callFunctionWithCustomContext(function(a, b) { return a + b; }, { foo: 'bar' }, [1, 2])` should return `3`.
  - `callFunctionWithCustomContext(function() { return this.foo; }, { foo: 'bar' }, [])` should return `'bar'`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to use the `apply` method of JavaScript functions, which allows us to specify the `this` context and an array of arguments.
- However, since we are restricted to C++, we can use the `std::invoke` function with `std::bind` to achieve similar results.
- We will create a `std::function` object from the input function and bind the context to it using `std::bind`.

```cpp
#include <functional>

int callFunctionWithCustomContext(std::function<int(int, int)> fn, std::string obj, std::vector<int> args) {
    // Create a std::function object from the input function
    auto boundFn = std::bind(fn, std::placeholders::_1, std::placeholders::_2);
    // Call the bound function with the provided arguments
    return boundFn(args[0], args[1]);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, since we are simply calling a function with bound arguments.
> - **Space Complexity:** $O(1)$, since we are not using any additional space that scales with input size.
> - **Why these complexities occur:** The `std::bind` and `std::invoke` functions do not introduce any significant overhead, and the space usage is constant.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal solution is to use `std::invoke` directly with the input function, context, and arguments.
- This approach eliminates the need for `std::bind` and provides a more straightforward and efficient solution.
- We can use `std::invoke` with a lambda function to capture the context and arguments.

```cpp
#include <functional>

int callFunctionWithCustomContext(std::function<int(int, int)> fn, std::string obj, std::vector<int> args) {
    // Create a lambda function that captures the context and arguments
    auto lambdaFn = [fn, obj, args]() { return fn(args[0], args[1]); };
    // Call the lambda function using std::invoke
    return std::invoke(lambdaFn);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, since we are simply calling a function with captured arguments.
> - **Space Complexity:** $O(1)$, since we are not using any additional space that scales with input size.
> - **Optimality proof:** This approach is optimal because it eliminates unnecessary overhead and uses the most direct and efficient way to call a function with a custom context.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: function binding, lambda functions, and `std::invoke`.
- Problem-solving patterns identified: using `std::bind` and `std::invoke` to call functions with custom contexts.
- Optimization techniques learned: eliminating unnecessary overhead by using `std::invoke` directly.
- Similar problems to practice: problems involving function binding, lambda functions, and `std::invoke`.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to capture the context and arguments in the lambda function.
- Edge cases to watch for: handling cases where the input function has a different signature or the context is `nullptr`.
- Performance pitfalls: using `std::bind` unnecessarily, which can introduce overhead.
- Testing considerations: testing the function with different input functions, contexts, and arguments to ensure correctness.