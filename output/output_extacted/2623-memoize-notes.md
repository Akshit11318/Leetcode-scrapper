## Memoize
**Problem Link:** https://leetcode.com/problems/memoize/description

**Problem Statement:**
- Input format and constraints: The problem asks to implement a `memoize` function that takes another function `f` as input and returns a memoized version of `f`. The memoized version should cache the results of `f` for different inputs to avoid redundant computations.
- Expected output format: The memoized function should return the same output as the original function `f` for a given input.
- Key requirements and edge cases to consider: The memoized function should handle cases where `f` is called multiple times with the same input, and it should also handle cases where `f` is called with different inputs.
- Example test cases with explanations: For example, if `f` is a function that calculates the factorial of a number, the memoized version of `f` should return the cached result if `f` has already been called with the same input.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: One possible approach is to use a simple caching mechanism to store the results of `f` for different inputs.
- Step-by-step breakdown of the solution:
  1. Create a cache data structure to store the results of `f` for different inputs.
  2. When the memoized function is called with an input, check if the result is already cached.
  3. If the result is cached, return the cached result.
  4. If the result is not cached, call the original function `f` with the input and cache the result.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, as it simply involves adding a caching layer on top of the original function `f`.

```cpp
#include <unordered_map>
#include <functional>

template <typename Func>
auto memoize(Func f) {
    std::unordered_map<std::string, int> cache;
    return [f, cache](int x) mutable {
        if (cache.find(std::to_string(x)) != cache.end()) {
            return cache[std::to_string(x)];
        } else {
            int result = f(x);
            cache[std::to_string(x)] = result;
            return result;
        }
    };
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for cached results, $O(f(x))$ for non-cached results, where $f(x)$ is the time complexity of the original function `f`.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique inputs to the memoized function.
> - **Why these complexities occur:** The time complexity is $O(1)$ for cached results because we can simply look up the result in the cache. For non-cached results, the time complexity is $O(f(x))$ because we need to call the original function `f`. The space complexity is $O(n)$ because we need to store the results of `f` for each unique input in the cache.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a more efficient caching mechanism, such as an `unordered_map`, to store the results of `f` for different inputs.
- Detailed breakdown of the approach:
  1. Create an `unordered_map` to store the results of `f` for different inputs.
  2. When the memoized function is called with an input, check if the result is already cached in the `unordered_map`.
  3. If the result is cached, return the cached result.
  4. If the result is not cached, call the original function `f` with the input and cache the result in the `unordered_map`.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(1)$ for cached results and $O(f(x))$ for non-cached results, and a space complexity of $O(n)$, where $n$ is the number of unique inputs to the memoized function.

```cpp
#include <unordered_map>
#include <functional>

template <typename Func>
auto memoize(Func f) {
    std::unordered_map<int, int> cache;
    return [f, cache](int x) mutable {
        if (cache.find(x) != cache.end()) {
            return cache[x];
        } else {
            int result = f(x);
            cache[x] = result;
            return result;
        }
    };
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for cached results, $O(f(x))$ for non-cached results, where $f(x)$ is the time complexity of the original function `f`.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique inputs to the memoized function.
> - **Optimality proof:** This approach is optimal because it has the best possible time and space complexities for a memoization problem.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Memoization, caching, and optimization.
- Problem-solving patterns identified: Using caching to avoid redundant computations.
- Optimization techniques learned: Using an `unordered_map` to store cached results.
- Similar problems to practice: Other memoization problems, such as memoizing a recursive function.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to cache the result of the original function `f`.
- Edge cases to watch for: Handling cases where the input to the memoized function is not a valid input to the original function `f`.
- Performance pitfalls: Using a caching mechanism with poor performance, such as a `map` instead of an `unordered_map`.
- Testing considerations: Testing the memoized function with different inputs to ensure that it is working correctly.