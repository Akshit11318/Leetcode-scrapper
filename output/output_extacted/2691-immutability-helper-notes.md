## Immutability Helper
**Problem Link:** https://leetcode.com/problems/immutability-helper/description

**Problem Statement:**
- Input format: The function `updateNestedObject` takes in an object `obj`, a `path` to a nested property, and a `value` to update that property with.
- Expected output format: The function returns a new object with the updated value at the specified path, without modifying the original object.
- Key requirements and edge cases to consider:
  - The path can be a string or an array of strings.
  - The path can point to a non-existent property, in which case the function should create the necessary intermediate objects.
  - The function should handle edge cases such as an empty path, a path with duplicate keys, or a null/undefined value.
- Example test cases with explanations:
  - Updating a simple property: `updateNestedObject({ a: 1 }, 'a', 2)` returns `{ a: 2 }`.
  - Updating a nested property: `updateNestedObject({ a: { b: 1 } }, 'a.b', 2)` returns `{ a: { b: 2 } }`.
  - Creating a new property: `updateNestedObject({ a: 1 }, 'b.c', 2)` returns `{ a: 1, b: { c: 2 } }`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves recursively traversing the object to find the property at the specified path and updating its value. If the path points to a non-existent property, the function creates the necessary intermediate objects.
- Step-by-step breakdown of the solution:
  1. Split the path into an array of keys if it's a string.
  2. Initialize a variable to store the current object being traversed.
  3. Iterate through the keys in the path, creating new objects as necessary.
  4. Once the end of the path is reached, update the value of the property.
- Why this approach comes to mind first: The brute force approach is straightforward and easy to implement, but it may not be efficient for large objects or complex paths.

```cpp
function updateNestedObject(obj, path, value) {
  // Split the path into an array of keys
  const keys = Array.isArray(path) ? path : path.split('.');

  // Initialize a variable to store the current object being traversed
  let currentObj = { ...obj };

  // Iterate through the keys in the path
  for (let i = 0; i < keys.length - 1; i++) {
    const key = keys[i];
    // Create a new object if the key doesn't exist
    if (!currentObj[key]) {
      currentObj[key] = {};
    }
    // Update the current object
    currentObj = currentObj[key];
  }

  // Update the value of the property at the end of the path
  currentObj[keys[keys.length - 1]] = value;

  // Return the updated object
  return obj;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the path, because we're iterating through the keys in the path.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the path, because we're creating new objects as necessary.
> - **Why these complexities occur:** The brute force approach has a linear time and space complexity because we're iterating through the keys in the path and creating new objects as necessary.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal approach involves using a recursive function to traverse the object and update the value at the specified path. This approach is more efficient than the brute force approach because it avoids creating unnecessary intermediate objects.
- Detailed breakdown of the approach:
  1. Define a recursive function that takes in the current object, the remaining path, and the value to update.
  2. If the path is empty, return the value.
  3. Otherwise, create a new object with the same properties as the current object, and recursively call the function on the next key in the path.
- Proof of optimality: The optimal approach has a time complexity of $O(n)$ and a space complexity of $O(n)$, where $n$ is the length of the path, making it more efficient than the brute force approach.

```cpp
function updateNestedObject(obj, path, value) {
  // Define a recursive function to traverse the object
  function recursiveUpdate(currentObj, remainingPath, value) {
    // If the path is empty, return the value
    if (remainingPath.length === 0) {
      return value;
    }

    // Create a new object with the same properties as the current object
    const newCurrentObj = { ...currentObj };

    // Recursively call the function on the next key in the path
    newCurrentObj[remainingPath[0]] = recursiveUpdate(
      currentObj[remainingPath[0]],
      remainingPath.slice(1),
      value
    );

    // Return the updated object
    return newCurrentObj;
  }

  // Split the path into an array of keys
  const keys = Array.isArray(path) ? path : path.split('.');

  // Call the recursive function
  return recursiveUpdate(obj, keys, value);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the path, because we're recursively traversing the object.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the path, because we're creating new objects as necessary.
> - **Optimality proof:** The optimal approach has a linear time and space complexity because we're recursively traversing the object and creating new objects as necessary, making it more efficient than the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: recursive functions, object traversal, and property updating.
- Problem-solving patterns identified: using recursive functions to solve problems with nested structures.
- Optimization techniques learned: avoiding unnecessary intermediate objects to improve efficiency.
- Similar problems to practice: updating nested arrays, traversing graphs, and solving recursive problems.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, such as empty paths or null/undefined values.
- Edge cases to watch for: paths with duplicate keys, or properties with the same name as the path.
- Performance pitfalls: creating unnecessary intermediate objects, or using inefficient data structures.
- Testing considerations: testing the function with different input scenarios, including edge cases and boundary values.