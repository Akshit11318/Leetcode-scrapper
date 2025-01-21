## Convert Callback-Based Function to Promise-Based Function

**Problem Link:** https://leetcode.com/problems/convert-callback-based-function-to-promise-based-function/description

**Problem Statement:**
- Input format and constraints: The problem involves converting a callback-based function to a promise-based function. The input function takes a callback as an argument and calls it with a result.
- Expected output format: The expected output is a promise-based function that resolves with the result.
- Key requirements and edge cases to consider: The function should handle errors and resolve or reject the promise accordingly.
- Example test cases with explanations: For example, if the input function is `checkPassword`, the promise-based function should resolve with `true` if the password is correct and reject with an error if it's incorrect.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves creating a new promise and resolving or rejecting it based on the result of the callback-based function.
- Step-by-step breakdown of the solution:
  1. Create a new promise using the `Promise` constructor.
  2. Call the callback-based function with a custom callback that resolves or rejects the promise.
  3. Handle errors and resolve or reject the promise accordingly.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be the most efficient or elegant solution.

```cpp
class Solution {
public:
    auto checkPassword(const string& password) {
        return [password]() -> promise<bool> {
            promise<bool> p;
            checkPassword(password, [&](bool result) {
                p.set_value(result);
            });
            return p.get_future();
        }();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we're simply creating a new promise and resolving or rejecting it based on the result of the callback-based function.
> - **Space Complexity:** $O(1)$, because we're not using any additional space that scales with the input.
> - **Why these complexities occur:** These complexities occur because we're not performing any operations that depend on the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using the `std::promise` and `std::future` classes to create a promise-based function.
- Detailed breakdown of the approach:
  1. Create a `std::promise` object to represent the promise.
  2. Create a `std::future` object to represent the future result of the promise.
  3. Call the callback-based function with a custom callback that sets the value of the promise.
  4. Return the future object.
- Proof of optimality: This solution is optimal because it uses the most efficient and elegant way to create a promise-based function in C++.
- Why further optimization is impossible: Further optimization is impossible because we're already using the most efficient and elegant solution.

```cpp
class Solution {
public:
    auto checkPassword(const string& password) {
        promise<bool> p;
        auto f = p.get_future();
        checkPassword(password, [&](bool result) {
            p.set_value(result);
        });
        return f;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, because we're simply creating a new promise and resolving or rejecting it based on the result of the callback-based function.
> - **Space Complexity:** $O(1)$, because we're not using any additional space that scales with the input.
> - **Optimality proof:** This solution is optimal because it uses the most efficient and elegant way to create a promise-based function in C++.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of promises and futures in C++.
- Problem-solving patterns identified: The problem requires identifying the key insight that leads to the optimal solution.
- Optimization techniques learned: The problem requires optimizing the solution by using the most efficient and elegant way to create a promise-based function.
- Similar problems to practice: Similar problems include converting other callback-based functions to promise-based functions.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is not handling errors correctly.
- Edge cases to watch for: An edge case to watch for is when the callback-based function calls the callback with an error.
- Performance pitfalls: A performance pitfall is using an inefficient solution that scales poorly with the input size.
- Testing considerations: Testing considerations include testing the function with different inputs and edge cases.