## Simplify Path
**Problem Link:** https://leetcode.com/problems/simplify-path/description

**Problem Statement:**
- Input format: A string `path` representing a file system path.
- Constraints: The path is a string of length `1` to `3000` characters, containing only letters, digits, and `/`.
- Expected output format: A simplified version of the input path.
- Key requirements and edge cases to consider:
  - The path can contain `..` and `.` directories, which need to be handled accordingly.
  - The path can be absolute or relative.
- Example test cases with explanations:
  - Input: `"/home/"`, Output: `"/home"`
  - Input: `"/../"`, Output: `"/"`
  - Input: `"/home//foo/"`, Output: `"/home/foo"`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Split the path into components using `/` as the separator, and then process each component one by one.
- Step-by-step breakdown of the solution:
  1. Split the path into components.
  2. Initialize an empty stack to store the valid components.
  3. Iterate over each component:
     - If the component is `..`, pop the last component from the stack if it's not empty.
     - If the component is `.` or an empty string, skip it.
     - Otherwise, push the component into the stack.
  4. Join the components in the stack with `/` to form the simplified path.

```cpp
vector<string> split(const string& str, char delimiter) {
    vector<string> tokens;
    string token;
    istringstream tokenStream(str);
    while (getline(tokenStream, token, delimiter)) {
        tokens.push_back(token);
    }
    return tokens;
}

string simplifyPath(string path) {
    vector<string> components = split(path, '/');
    stack<string> stack;
    for (const string& component : components) {
        if (component == "..") {
            if (!stack.empty()) {
                stack.pop();
            }
        } else if (component != "." && !component.empty()) {
            stack.push(component);
        }
    }
    string simplifiedPath;
    while (!stack.empty()) {
        simplifiedPath = "/" + stack.top() + simplifiedPath;
        stack.pop();
    }
    return simplifiedPath.empty() ? "/" : simplifiedPath;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of components in the path, since we process each component once.
> - **Space Complexity:** $O(n)$, since in the worst case, we might need to store all components in the stack.
> - **Why these complexities occur:** The brute force approach involves iterating over each component in the path and performing a constant amount of work for each component, resulting in linear time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same as the brute force approach, but with a more efficient implementation using a vector instead of a stack.
- Detailed breakdown of the approach:
  1. Split the path into components.
  2. Initialize an empty vector to store the valid components.
  3. Iterate over each component:
     - If the component is `..`, remove the last component from the vector if it's not empty.
     - If the component is `.` or an empty string, skip it.
     - Otherwise, add the component to the vector.
  4. Join the components in the vector with `/` to form the simplified path.
- Proof of optimality: This approach has the same time and space complexities as the brute force approach but is more efficient in practice due to the use of a vector.

```cpp
string simplifyPath(string path) {
    vector<string> components;
    string component;
    for (char c : path) {
        if (c == '/') {
            if (!component.empty()) {
                if (component == "..") {
                    if (!components.empty()) {
                        components.pop_back();
                    }
                } else if (component != ".") {
                    components.push_back(component);
                }
                component.clear();
            }
        } else {
            component += c;
        }
    }
    if (!component.empty()) {
        if (component == "..") {
            if (!components.empty()) {
                components.pop_back();
            }
        } else if (component != ".") {
            components.push_back(component);
        }
    }
    string simplifiedPath;
    for (const string& component : components) {
        simplifiedPath += "/" + component;
    }
    return simplifiedPath.empty() ? "/" : simplifiedPath;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input path, since we process each character in the path once.
> - **Space Complexity:** $O(n)$, since in the worst case, we might need to store all components in the vector.
> - **Optimality proof:** This approach is optimal because it only processes each character in the input path once and uses a minimal amount of extra space to store the simplified path.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: String manipulation, path simplification, and stack/vector usage.
- Problem-solving patterns identified: Handling edge cases, such as `..` and `.` directories, and optimizing the solution using a vector.
- Optimization techniques learned: Using a vector instead of a stack to improve efficiency.
- Similar problems to practice: Path-related problems, such as finding the shortest path in a graph or simplifying a relative path.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, such as `..` and `.` directories, and not checking for empty strings or vectors.
- Edge cases to watch for: Absolute and relative paths, paths with `..` and `.` directories, and paths with trailing or leading slashes.
- Performance pitfalls: Using inefficient data structures, such as stacks or linked lists, and not optimizing the solution for large input paths.
- Testing considerations: Testing the solution with various input paths, including edge cases, to ensure correctness and efficiency.