## Check if Object is Instance of Class

**Problem Link:** https://leetcode.com/problems/check-if-object-instance-of-class/description

**Problem Statement:**
- Input format and constraints: The problem takes in two parameters, `obj` and `cls`, where `obj` is an object and `cls` is a class.
- Expected output format: The function should return `true` if `obj` is an instance of `cls`, and `false` otherwise.
- Key requirements and edge cases to consider: The function should handle cases where `obj` is `null` or `cls` is not a class.
- Example test cases with explanations:
  - `checkIfInstanceOf(5, Integer)`: Returns `true` because `5` is an instance of `Integer`.
  - `checkIfInstanceOf("hello", String)`: Returns `true` because `"hello"` is an instance of `String`.
  - `checkIfInstanceOf(null, Object)`: Returns `false` because `null` is not an instance of any class.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can use a simple `if` statement to check if `obj` is an instance of `cls`.
- Step-by-step breakdown of the solution: 
  1. Check if `cls` is a class.
  2. If `cls` is a class, use the `dynamic_cast` operator to check if `obj` is an instance of `cls`.
- Why this approach comes to mind first: This approach is straightforward and easy to understand.

```cpp
class Solution {
public:
    bool checkIfInstanceOf(int obj, int cls) {
        // Check if cls is a class
        // Note: In C++, we can't directly check if a variable is a class.
        // However, since the problem statement doesn't specify how cls is defined,
        // we assume it's a class for the sake of this example.
        
        // Use dynamic_cast to check if obj is an instance of cls
        return dynamic_cast<void*>(obj) != nullptr;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we are performing a constant number of operations.
> - **Space Complexity:** $O(1)$ because we are not using any additional space that scales with input size.
> - **Why these complexities occur:** The time and space complexities are constant because we are not iterating over any data structures or using any recursive functions.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use the `isinstance` equivalent in C++ to check if an object is an instance of a class.
- Detailed breakdown of the approach: 
  1. Use the `typeid` operator to get the type of `obj`.
  2. Use the `dynamic_cast` operator to check if `obj` is an instance of `cls`.
- Proof of optimality: This approach is optimal because it directly checks if `obj` is an instance of `cls` without any additional overhead.
- Why further optimization is impossible: This approach is already optimal because it uses the most efficient way to check if an object is an instance of a class in C++.

```cpp
class Solution {
public:
    bool checkIfInstanceOf(int obj, int cls) {
        // Use typeid to get the type of obj
        auto objType = typeid(obj);
        
        // Use dynamic_cast to check if obj is an instance of cls
        return dynamic_cast<void*>(obj) != nullptr;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ because we are performing a constant number of operations.
> - **Space Complexity:** $O(1)$ because we are not using any additional space that scales with input size.
> - **Optimality proof:** This approach is optimal because it directly checks if `obj` is an instance of `cls` without any additional overhead.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Type checking, dynamic casting.
- Problem-solving patterns identified: Using `typeid` and `dynamic_cast` to check if an object is an instance of a class.
- Optimization techniques learned: Directly checking if an object is an instance of a class without any additional overhead.
- Similar problems to practice: Type checking, object-oriented programming.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if `cls` is a class before using `dynamic_cast`.
- Edge cases to watch for: `obj` being `null`, `cls` not being a class.
- Performance pitfalls: Using recursive functions or iterating over large data structures.
- Testing considerations: Test with different types of objects and classes, including edge cases.