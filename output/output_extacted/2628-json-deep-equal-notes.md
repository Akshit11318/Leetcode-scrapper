## JSON Deep Equal
**Problem Link:** https://leetcode.com/problems/json-deep-equal/description

**Problem Statement:**
- Input format and constraints: The function takes two JSON objects, `obj1` and `obj2`, as input and returns a boolean indicating whether they are deeply equal.
- Expected output format: The function returns `true` if `obj1` and `obj2` are deeply equal, and `false` otherwise.
- Key requirements and edge cases to consider: The function must handle nested objects and arrays, and it must check for equality of all properties and elements.
- Example test cases with explanations:
  - `JSONDeepEqual(1, 1)` returns `true`
  - `JSONDeepEqual(1, 2)` returns `false`
  - `JSONDeepEqual("a", "a")` returns `true`
  - `JSONDeepEqual("a", "b")` returns `false`
  - `JSONDeepEqual([1, 2], [1, 2])` returns `true`
  - `JSONDeepEqual([1, 2], [1, 3])` returns `false`
  - `JSONDeepEqual({"a": 1}, {"a": 1})` returns `true`
  - `JSONDeepEqual({"a": 1}, {"a": 2})` returns `false`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To check if two JSON objects are deeply equal, we need to recursively check all properties and elements of the objects and arrays.
- Step-by-step breakdown of the solution:
  1. If both objects are of the same type, we can compare them directly.
  2. If one object is an array and the other is not, we return `false`.
  3. If one object is an object and the other is not, we return `false`.
  4. If both objects are arrays, we recursively compare their elements.
  5. If both objects are objects, we recursively compare their properties.
- Why this approach comes to mind first: It's a straightforward approach that checks for equality of all properties and elements.

```cpp
bool JSONDeepEqual(const JsonValue& obj1, const JsonValue& obj2) {
    // If both objects are of the same type
    if (obj1.isInteger() && obj2.isInteger()) {
        return obj1.asInt() == obj2.asInt();
    } else if (obj1.isString() && obj2.isString()) {
        return obj1.asString() == obj2.asString();
    } else if (obj1.isBoolean() && obj2.isBoolean()) {
        return obj1.asBool() == obj2.asBool();
    } else if (obj1.isNull() && obj2.isNull()) {
        return true;
    }
    
    // If one object is an array and the other is not
    if (obj1.isArray() != obj2.isArray()) {
        return false;
    }
    
    // If both objects are arrays
    if (obj1.isArray() && obj2.isArray()) {
        if (obj1.size() != obj2.size()) {
            return false;
        }
        for (int i = 0; i < obj1.size(); i++) {
            if (!JSONDeepEqual(obj1[i], obj2[i])) {
                return false;
            }
        }
        return true;
    }
    
    // If both objects are objects
    if (obj1.isObject() && obj2.isObject()) {
        if (obj1.size() != obj2.size()) {
            return false;
        }
        for (const auto& key : obj1.keys()) {
            if (!obj2.has(key)) {
                return false;
            }
            if (!JSONDeepEqual(obj1[key], obj2[key])) {
                return false;
            }
        }
        return true;
    }
    
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the total number of properties and elements in the two JSON objects. This is because we recursively check all properties and elements.
> - **Space Complexity:** $O(n)$, where $n$ is the maximum depth of the recursion. This is because we use recursive function calls to check all properties and elements.
> - **Why these complexities occur:** The time complexity occurs because we recursively check all properties and elements, and the space complexity occurs because we use recursive function calls.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is similar to the brute force approach, but it uses a more efficient way to compare arrays and objects.
- Detailed breakdown of the approach:
  1. If both objects are of the same type, we can compare them directly.
  2. If one object is an array and the other is not, we return `false`.
  3. If one object is an object and the other is not, we return `false`.
  4. If both objects are arrays, we recursively compare their elements using a loop.
  5. If both objects are objects, we recursively compare their properties using a loop.
- Proof of optimality: The optimal solution has a time complexity of $O(n)$ and a space complexity of $O(n)$, which is the best possible complexity for this problem.

```cpp
bool JSONDeepEqual(const JsonValue& obj1, const JsonValue& obj2) {
    // If both objects are of the same type
    if (obj1.type() == obj2.type()) {
        if (obj1.isInteger()) {
            return obj1.asInt() == obj2.asInt();
        } else if (obj1.isString()) {
            return obj1.asString() == obj2.asString();
        } else if (obj1.isBoolean()) {
            return obj1.asBool() == obj2.asBool();
        } else if (obj1.isNull()) {
            return true;
        }
    }
    
    // If one object is an array and the other is not
    if (obj1.isArray() != obj2.isArray()) {
        return false;
    }
    
    // If both objects are arrays
    if (obj1.isArray() && obj2.isArray()) {
        if (obj1.size() != obj2.size()) {
            return false;
        }
        for (int i = 0; i < obj1.size(); i++) {
            if (!JSONDeepEqual(obj1[i], obj2[i])) {
                return false;
            }
        }
        return true;
    }
    
    // If both objects are objects
    if (obj1.isObject() && obj2.isObject()) {
        if (obj1.size() != obj2.size()) {
            return false;
        }
        for (const auto& key : obj1.keys()) {
            if (!obj2.has(key)) {
                return false;
            }
            if (!JSONDeepEqual(obj1[key], obj2[key])) {
                return false;
            }
        }
        return true;
    }
    
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the total number of properties and elements in the two JSON objects. This is because we recursively check all properties and elements.
> - **Space Complexity:** $O(n)$, where $n$ is the maximum depth of the recursion. This is because we use recursive function calls to check all properties and elements.
> - **Optimality proof:** The optimal solution has a time complexity of $O(n)$ and a space complexity of $O(n)$, which is the best possible complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursion, loop iteration, and type checking.
- Problem-solving patterns identified: Checking for equality of all properties and elements, and using recursive function calls to check nested objects and arrays.
- Optimization techniques learned: Using a more efficient way to compare arrays and objects, and avoiding unnecessary recursive function calls.
- Similar problems to practice: Deep copying of objects and arrays, and checking for equality of complex data structures.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for null or undefined values, and not handling edge cases such as empty arrays or objects.
- Edge cases to watch for: Checking for equality of nested objects and arrays, and handling cases where one object is an array and the other is not.
- Performance pitfalls: Using unnecessary recursive function calls, and not optimizing the comparison of arrays and objects.
- Testing considerations: Testing the function with different types of input, such as integers, strings, booleans, and null values, and testing edge cases such as empty arrays or objects.