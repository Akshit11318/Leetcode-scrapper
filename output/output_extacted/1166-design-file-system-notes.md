## Design File System
**Problem Link:** https://leetcode.com/problems/design-file-system/description

**Problem Statement:**
- Input format and constraints: The file system supports the following operations:
  - `createPath(path, value)`: Creates a new path and assigns a value to it if the path does not exist. If the path already exists, no operation is performed.
  - `get(path)`: Returns the value associated with a path if the path exists. If the path does not exist, it returns -1.
- Expected output format: The output of the `get` operation should be an integer representing the value associated with the path.
- Key requirements and edge cases to consider:
  - The file system supports a maximum of 10^5 operations.
  - Each path is a string consisting of English letters, digits, and forward slashes (`/`), and its length does not exceed 100 characters.
  - The value associated with each path is an integer in the range [1, 10^9].
- Example test cases with explanations:
  - `createPath("/a", 1)`: Creates a new path "/a" and assigns a value of 1 to it.
  - `get("/a")`: Returns the value associated with the path "/a", which is 1.
  - `createPath("/a/b", 2)`: Creates a new path "/a/b" and assigns a value of 2 to it.
  - `get("/a/b")`: Returns the value associated with the path "/a/b", which is 2.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can use a simple data structure to store the paths and their associated values.
- Step-by-step breakdown of the solution:
  1. Create a data structure (e.g., a map) to store the paths and their associated values.
  2. In the `createPath` operation, check if the path already exists in the data structure. If it does, do nothing. If it does not, create a new entry in the data structure with the given path and value.
  3. In the `get` operation, check if the path exists in the data structure. If it does, return the associated value. If it does not, return -1.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, as it directly addresses the problem statement.

```cpp
class TrieNode {
public:
    unordered_map<string, int> values;
    unordered_map<string, TrieNode*> children;
};

class FileSystem {
private:
    TrieNode* root;
public:
    FileSystem() {
        root = new TrieNode();
    }

    bool createPath(string path, int value) {
        vector<string> components;
        string component = "";
        for (char c : path) {
            if (c == '/') {
                if (!component.empty()) {
                    components.push_back(component);
                    component = "";
                }
            } else {
                component += c;
            }
        }
        if (!component.empty()) {
            components.push_back(component);
        }

        TrieNode* current = root;
        for (int i = 0; i < components.size(); i++) {
            if (current->children.find(components[i]) == current->children.end()) {
                if (i == components.size() - 1) {
                    current->values[components[i]] = value;
                    return true;
                } else {
                    return false;
                }
            }
            current = current->children[components[i]];
        }
        return false;
    }

    int get(string path) {
        vector<string> components;
        string component = "";
        for (char c : path) {
            if (c == '/') {
                if (!component.empty()) {
                    components.push_back(component);
                    component = "";
                }
            } else {
                component += c;
            }
        }
        if (!component.empty()) {
            components.push_back(component);
        }

        TrieNode* current = root;
        for (int i = 0; i < components.size(); i++) {
            if (current->children.find(components[i]) == current->children.end()) {
                if (i == components.size() - 1) {
                    if (current->values.find(components[i]) != current->values.end()) {
                        return current->values[components[i]];
                    } else {
                        return -1;
                    }
                } else {
                    return -1;
                }
            }
            current = current->children[components[i]];
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of components in the path. This is because we need to iterate through each component in the path to create or retrieve the value.
> - **Space Complexity:** $O(n)$, where $n$ is the total number of components in all paths. This is because we need to store each component in the Trie data structure.
> - **Why these complexities occur:** These complexities occur because we need to iterate through each component in the path to create or retrieve the value, and we need to store each component in the Trie data structure.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a Trie data structure to store the paths and their associated values. This allows us to efficiently create and retrieve values for paths.
- Detailed breakdown of the approach:
  1. Create a TrieNode class to represent each node in the Trie.
  2. Create a FileSystem class to manage the Trie and provide the `createPath` and `get` operations.
  3. In the `createPath` operation, iterate through each component in the path and create a new node in the Trie if the component does not exist.
  4. In the `get` operation, iterate through each component in the path and return the associated value if the path exists.
- Why further optimization is impossible: This approach is already optimal because we need to iterate through each component in the path to create or retrieve the value, and we need to store each component in the Trie data structure.

```cpp
class TrieNode {
public:
    unordered_map<string, int> values;
    unordered_map<string, TrieNode*> children;
};

class FileSystem {
private:
    TrieNode* root;
public:
    FileSystem() {
        root = new TrieNode();
    }

    bool createPath(string path, int value) {
        vector<string> components;
        string component = "";
        for (char c : path) {
            if (c == '/') {
                if (!component.empty()) {
                    components.push_back(component);
                    component = "";
                }
            } else {
                component += c;
            }
        }
        if (!component.empty()) {
            components.push_back(component);
        }

        TrieNode* current = root;
        for (int i = 0; i < components.size(); i++) {
            if (current->children.find(components[i]) == current->children.end()) {
                if (i == components.size() - 1) {
                    current->values[components[i]] = value;
                    return true;
                } else {
                    TrieNode* newNode = new TrieNode();
                    current->children[components[i]] = newNode;
                    current = newNode;
                }
            } else {
                current = current->children[components[i]];
            }
        }
        return false;
    }

    int get(string path) {
        vector<string> components;
        string component = "";
        for (char c : path) {
            if (c == '/') {
                if (!component.empty()) {
                    components.push_back(component);
                    component = "";
                }
            } else {
                component += c;
            }
        }
        if (!component.empty()) {
            components.push_back(component);
        }

        TrieNode* current = root;
        for (int i = 0; i < components.size(); i++) {
            if (current->children.find(components[i]) == current->children.end()) {
                if (i == components.size() - 1) {
                    if (current->values.find(components[i]) != current->values.end()) {
                        return current->values[components[i]];
                    } else {
                        return -1;
                    }
                } else {
                    return -1;
                }
            }
            current = current->children[components[i]];
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of components in the path. This is because we need to iterate through each component in the path to create or retrieve the value.
> - **Space Complexity:** $O(n)$, where $n$ is the total number of components in all paths. This is because we need to store each component in the Trie data structure.
> - **Optimality proof:** This approach is optimal because we need to iterate through each component in the path to create or retrieve the value, and we need to store each component in the Trie data structure.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Trie data structure, path creation and retrieval.
- Problem-solving patterns identified: Using a Trie data structure to efficiently store and retrieve paths and their associated values.
- Optimization techniques learned: Using a Trie data structure to reduce the time complexity of path creation and retrieval operations.
- Similar problems to practice: Other problems that involve using a Trie data structure, such as autocomplete and prefix matching.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as empty paths or paths with multiple consecutive slashes.
- Edge cases to watch for: Paths with multiple consecutive slashes, paths that are not properly normalized.
- Performance pitfalls: Using a data structure that has a high time complexity for path creation and retrieval operations, such as a linear search.
- Testing considerations: Testing the `createPath` and `get` operations with different types of paths, including empty paths and paths with multiple consecutive slashes.