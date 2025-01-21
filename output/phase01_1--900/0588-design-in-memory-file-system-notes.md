## Design In-Memory File System

**Problem Link:** [https://leetcode.com/problems/design-in-memory-file-system/description](https://leetcode.com/problems/design-in-memory-file-system/description)

**Problem Statement:**
- Input format: The input consists of a series of `create`, `mkdir`, `addContentToFile`, `readContentFromFile` operations.
- Constraints: The file system has a root directory, and each file/directory name is a string without `.` or `..`.
- Expected output format: The result of each operation.
- Key requirements: Implement an in-memory file system that supports `create`, `mkdir`, `addContentToFile`, `readContentFromFile` operations.
- Example test cases:
  - `create("/a", 1)`: Create a file named `a` in the root directory with content `1`.
  - `mkdir("/a/b")`: Create a directory named `b` in the directory `a`.
  - `addContentToFile("/a/b/c", 2)`: Add content `2` to the file `c` in the directory `b`.
  - `readContentFromFile("/a/b/c")`: Read the content of the file `c` in the directory `b`.

### Brute Force Approach

**Explanation:**
- Initial thought process: Use a nested map to represent the file system, where each directory is a map of its children (files and subdirectories).
- Step-by-step breakdown:
  1. Create a `FileSystem` class with a nested map `fs` to represent the file system.
  2. Implement the `create` operation by checking if the parent directory exists and creating the file with the given content.
  3. Implement the `mkdir` operation by checking if the parent directory exists and creating the subdirectory.
  4. Implement the `addContentToFile` operation by checking if the file exists and appending the content.
  5. Implement the `readContentFromFile` operation by checking if the file exists and returning its content.

```cpp
class FileSystem {
public:
    unordered_map<string, pair<int, unordered_map<string, FileSystem*>>> fs;

    FileSystem() {
        fs[""] = {0, {}};
    }

    bool create(string path, int value) {
        int start = 0;
        while (true) {
            int end = path.find('/', start);
            if (end == string::npos) {
                end = path.length();
            }
            string dir = path.substr(start, end - start);
            if (end == path.length()) {
                if (fs.find(path) != fs.end()) {
                    return false;
                }
                fs[path] = {value, {}};
                return true;
            }
            if (fs.find(path.substr(0, end)) == fs.end()) {
                return false;
            }
            start = end + 1;
        }
    }

    bool mkdir(string path) {
        int start = 0;
        while (true) {
            int end = path.find('/', start);
            if (end == string::npos) {
                end = path.length();
            }
            string dir = path.substr(start, end - start);
            if (end == path.length()) {
                if (fs.find(path) != fs.end()) {
                    return false;
                }
                fs[path] = {0, {}};
                return true;
            }
            if (fs.find(path.substr(0, end)) == fs.end()) {
                return false;
            }
            start = end + 1;
        }
    }

    void addContentToFile(string filePath, int content) {
        fs[filePath].first += content;
    }

    int readContentFromFile(string filePath) {
        return fs[filePath].first;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of operations.
> - **Space Complexity:** $O(n)$, where $n$ is the number of files and directories.
> - **Why these complexities occur:** The time complexity is linear because each operation involves traversing the file system tree. The space complexity is also linear because we need to store all files and directories in the file system.

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use a Trie-like data structure to represent the file system, where each node represents a directory or file.
- Detailed breakdown:
  1. Create a `TrieNode` class to represent each node in the Trie.
  2. Implement the `create` operation by traversing the Trie and creating the file with the given content.
  3. Implement the `mkdir` operation by traversing the Trie and creating the subdirectory.
  4. Implement the `addContentToFile` operation by traversing the Trie and appending the content to the file.
  5. Implement the `readContentFromFile` operation by traversing the Trie and returning the content of the file.

```cpp
class TrieNode {
public:
    unordered_map<string, TrieNode*> children;
    bool isFile;
    string content;

    TrieNode() : isFile(false), content("") {}
};

class FileSystem {
public:
    TrieNode* root;

    FileSystem() {
        root = new TrieNode();
    }

    bool create(string path, int value) {
        TrieNode* node = root;
        vector<string> components = splitPath(path);
        for (int i = 0; i < components.size() - 1; i++) {
            string component = components[i];
            if (node->children.find(component) == node->children.end()) {
                node->children[component] = new TrieNode();
            }
            node = node->children[component];
        }
        string fileName = components.back();
        if (node->children.find(fileName) != node->children.end()) {
            return false;
        }
        node->children[fileName] = new TrieNode();
        node->children[fileName]->isFile = true;
        node->children[fileName]->content = to_string(value);
        return true;
    }

    bool mkdir(string path) {
        TrieNode* node = root;
        vector<string> components = splitPath(path);
        for (int i = 0; i < components.size(); i++) {
            string component = components[i];
            if (node->children.find(component) == node->children.end()) {
                node->children[component] = new TrieNode();
            }
            node = node->children[component];
        }
        return true;
    }

    void addContentToFile(string filePath, int value) {
        TrieNode* node = root;
        vector<string> components = splitPath(filePath);
        for (int i = 0; i < components.size(); i++) {
            string component = components[i];
            if (node->children.find(component) == node->children.end()) {
                return;
            }
            node = node->children[component];
        }
        node->content += to_string(value);
    }

    int readContentFromFile(string filePath) {
        TrieNode* node = root;
        vector<string> components = splitPath(filePath);
        for (int i = 0; i < components.size(); i++) {
            string component = components[i];
            if (node->children.find(component) == node->children.end()) {
                return -1;
            }
            node = node->children[component];
        }
        return stoi(node->content);
    }

    vector<string> splitPath(string path) {
        vector<string> components;
        string component;
        for (char c : path) {
            if (c == '/') {
                if (!component.empty()) {
                    components.push_back(component);
                    component.clear();
                }
            } else {
                component += c;
            }
        }
        if (!component.empty()) {
            components.push_back(component);
        }
        return components;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of operations.
> - **Space Complexity:** $O(n)$, where $n$ is the number of files and directories.
> - **Optimality proof:** The time and space complexities are optimal because we need to traverse the file system tree for each operation and store all files and directories.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Trie data structure, file system operations.
- Problem-solving patterns identified: Using a Trie-like data structure to represent a hierarchical structure.
- Optimization techniques learned: Using a Trie to reduce the time complexity of file system operations.
- Similar problems to practice: Implementing a file system with additional operations (e.g., delete, rename).

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases (e.g., empty paths, non-existent directories).
- Edge cases to watch for: Creating a file in a non-existent directory, reading from a non-existent file.
- Performance pitfalls: Using a naive approach with high time complexity (e.g., using a linear search to find a file).
- Testing considerations: Testing the file system with various operations and edge cases.