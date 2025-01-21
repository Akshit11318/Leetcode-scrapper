## Design a File Sharing System
**Problem Link:** https://leetcode.com/problems/design-a-file-sharing-system/description

**Problem Statement:**
- Design a file sharing system with methods `share`, `unshare`, and `get`.
- The `share` method takes a file ID and a user ID as input and shares the file with the given user.
- The `unshare` method takes a file ID and a user ID as input and unshares the file from the given user.
- The `get` method takes a file ID and a user ID as input and returns the file content if the user has access to the file.
- Key requirements and edge cases to consider:
  - A user can only access a file if it has been shared with them.
  - A user can only unshare a file if they have shared it with someone else.
  - The file content should be stored and retrieved efficiently.

**Example Test Cases:**
- `share(1, 2)`: Share file 1 with user 2.
- `unshare(1, 2)`: Unshare file 1 from user 2.
- `get(1, 2)`: Get the content of file 1 for user 2.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to use a simple data structure to store the file content and the users who have access to each file.
- We can use a `map` to store the file content and another `map` to store the users who have access to each file.
- The `share` method will add the user to the list of users who have access to the file.
- The `unshare` method will remove the user from the list of users who have access to the file.
- The `get` method will check if the user has access to the file and return the file content if they do.

```cpp
class FileSharing {
public:
    map<int, string> files;
    map<int, set<int>> shared;

    FileSharing() {}

    void share(int file_id, int user_id) {
        shared[file_id].insert(user_id);
    }

    void unshare(int file_id, int user_id) {
        shared[file_id].erase(user_id);
    }

    string get(int file_id, int user_id) {
        if (shared[file_id].find(user_id) != shared[file_id].end()) {
            return files[file_id];
        }
        return "";
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for `share` and `unshare` methods, $O(1)$ for `get` method.
> - **Space Complexity:** $O(n + m)$ where $n$ is the number of files and $m$ is the number of users.
> - **Why these complexities occur:** The `map` and `set` data structures allow for efficient insertion, deletion, and search operations.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal approach is to use the same data structure as the brute force approach, but with some optimizations.
- We can use a `unordered_map` instead of a `map` to store the file content and the users who have access to each file.
- This will improve the performance of the `get` method.

```cpp
class FileSharing {
public:
    unordered_map<int, string> files;
    unordered_map<int, unordered_set<int>> shared;

    FileSharing() {}

    void share(int file_id, int user_id) {
        shared[file_id].insert(user_id);
    }

    void unshare(int file_id, int user_id) {
        shared[file_id].erase(user_id);
    }

    string get(int file_id, int user_id) {
        if (shared[file_id].find(user_id) != shared[file_id].end()) {
            return files[file_id];
        }
        return "";
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for `share` and `unshare` methods, $O(1)$ for `get` method.
> - **Space Complexity:** $O(n + m)$ where $n$ is the number of files and $m$ is the number of users.
> - **Optimality proof:** The use of `unordered_map` and `unordered_set` data structures allows for efficient insertion, deletion, and search operations, making this approach optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: data structures (maps, sets), optimization techniques (using unordered data structures).
- Problem-solving patterns identified: using data structures to store and retrieve data efficiently.
- Optimization techniques learned: using unordered data structures to improve performance.

**Mistakes to Avoid:**
- Common implementation errors: using the wrong data structure, not handling edge cases.
- Edge cases to watch for: users who do not have access to a file, files that are not shared with any users.
- Performance pitfalls: using data structures with poor performance characteristics.
- Testing considerations: testing the `share`, `unshare`, and `get` methods with different inputs and edge cases.