## Memoize II

**Problem Link:** https://leetcode.com/problems/memoize-ii/description

**Problem Statement:**
- Input format and constraints: The problem requires creating a memoization function that can be used to memoize other functions. The input function `f` can be any function, and the memoized function should return the same result as `f` for the same input arguments.
- Expected output format: The memoized function should return the result of `f` for the given input arguments.
- Key requirements and edge cases to consider: The memoized function should store the results of `f` for each set of input arguments to avoid redundant computations.
- Example test cases with explanations:
  - Example 1: Memoizing a function that adds two numbers.
  - Example 2: Memoizing a function that calculates the factorial of a number.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial approach is to create a memoization function that uses a dictionary to store the results of `f` for each set of input arguments.
- Step-by-step breakdown of the solution:
  1. Create a dictionary to store the results of `f`.
  2. Define a memoized function that checks if the result for the given input arguments is already stored in the dictionary.
  3. If the result is stored, return it. Otherwise, compute the result using `f`, store it in the dictionary, and return it.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, making it a natural first choice.

```cpp
class Solution {
public:
    template <typename F>
    auto memoize(F f) {
        std::unordered_map<std::string, int> memo;
        return [f, memo](int x) mutable {
            std::string key = std::to_string(x);
            if (memo.find(key) != memo.end()) {
                return memo[key];
            }
            int result = f(x);
            memo[key] = result;
            return result;
        };
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for memoized results, $O(f(x))$ for unmemoized results, where $f(x)$ is the time complexity of the input function `f`.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique input arguments.
> - **Why these complexities occur:** The time complexity is $O(1)$ for memoized results because the result is already stored in the dictionary. The space complexity is $O(n)$ because we need to store the results for each unique input argument.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is to use a similar approach as the brute force solution but with some optimizations.
- Detailed breakdown of the approach:
  1. Use a `std::function` to store the input function `f`.
  2. Use a `std::unordered_map` to store the memoized results.
  3. Use a lambda function to define the memoized function.
- Proof of optimality: This solution is optimal because it has a time complexity of $O(1)$ for memoized results and $O(f(x))$ for unmemoized results, and a space complexity of $O(n)$.
- Why further optimization is impossible: Further optimization is impossible because we need to store the results for each unique input argument, and we need to compute the result using `f` for unmemoized results.

```cpp
class Solution {
public:
    template <typename F>
    auto memoize(F f) {
        std::unordered_map<std::string, int> memo;
        return [f, memo](auto... args) mutable {
            std::string key = std::to_string(std::tuple{args...});
            if (memo.find(key) != memo.end()) {
                return memo[key];
            }
            int result = f(args...);
            memo[key] = result;
            return result;
        };
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for memoized results, $O(f(x))$ for unmemoized results, where $f(x)$ is the time complexity of the input function `f`.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique input arguments.
> - **Optimality proof:** This solution is optimal because it has a time complexity of $O(1)$ for memoized results and $O(f(x))$ for unmemoized results, and a space complexity of $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Memoization, lambda functions, `std::unordered_map`.
- Problem-solving patterns identified: Using a dictionary to store memoized results, using a lambda function to define the memoized function.
- Optimization techniques learned: Using `std::unordered_map` instead of `std::map`, using a lambda function instead of a regular function.
- Similar problems to practice: Memoizing a recursive function, memoizing a function with multiple arguments.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check if the result is already stored in the dictionary, forgetting to store the result in the dictionary.
- Edge cases to watch for: Handling multiple arguments, handling recursive functions.
- Performance pitfalls: Using a `std::map` instead of a `std::unordered_map`, using a regular function instead of a lambda function.
- Testing considerations: Testing with different input functions, testing with different input arguments.