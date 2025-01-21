## Delete Duplicate Folders in System
**Problem Link:** https://leetcode.com/problems/delete-duplicate-folders-in-system/description

**Problem Statement:**
- Input format: A list of paths of folders in the system.
- Constraints: Each path is a string consisting of English letters and '/'.
- Expected output format: A list of paths of folders to be deleted.
- Key requirements: Identify and delete duplicate folders based on their contents.
- Edge cases: Empty paths, single folder paths, paths with different names but same contents.

**Example Test Cases:**
- Input: `[["a"],["c"],["d"],["c"]]`
  Output: `["c"]`
- Input: `[["a"],["c"],["d"],["c"],["c"],["f"],["a"],["f"],["f"],["f"],["f"],["f"],["f"],["f"],["f"]]`
  Output: `["c","c","f","f","f","f","f","f","f","f"]`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves comparing each folder's contents with every other folder to identify duplicates.
- This approach requires generating all possible combinations of folders and then comparing their contents.
- It comes to mind first because it directly addresses the problem statement without considering efficiency.

```cpp
#include <vector>
#include <string>
#include <unordered_map>

std::vector<std::string> deleteDuplicateFolder(const std::vector<std::vector<std::string>>& paths) {
    std::unordered_map<std::string, int> folderContents;
    std::vector<std::string> duplicates;

    // Generate all possible folder contents
    for (const auto& path : paths) {
        std::string content;
        for (const auto& folder : path) {
            content += folder + "/";
        }

        // Count occurrences of each folder content
        if (folderContents.find(content) != folderContents.end()) {
            folderContents[content]++;
        } else {
            folderContents[content] = 1;
        }
    }

    // Identify and mark duplicate folders for deletion
    for (const auto& path : paths) {
        std::string content;
        for (const auto& folder : path) {
            content += folder + "/";
        }

        if (folderContents[content] > 1) {
            std::string pathStr;
            for (const auto& folder : path) {
                pathStr += "/" + folder;
            }
            duplicates.push_back(pathStr);
        }
    }

    return duplicates;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the number of paths and $m$ is the maximum number of folders in a path. This is because we are generating all possible folder contents and then comparing them.
> - **Space Complexity:** $O(n \cdot m)$, as we store all folder contents and their counts.
> - **Why these complexities occur:** The brute force approach involves nested loops to generate and compare folder contents, leading to high time complexity. The space complexity is due to storing all folder contents and their counts.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a `Trie` data structure to efficiently store and compare folder contents.
- We construct the Trie by iterating through each path and adding folders to the Trie.
- We keep track of the number of occurrences of each folder content by storing a count at each node in the Trie.
- We then traverse the Trie to identify and mark duplicate folders for deletion.

```cpp
#include <vector>
#include <string>
#include <unordered_map>

struct TrieNode {
    std::unordered_map<std::string, TrieNode*> children;
    int count = 0;
};

std::vector<std::string> deleteDuplicateFolder(const std::vector<std::vector<std::string>>& paths) {
    TrieNode* root = new TrieNode();
    std::vector<std::string> duplicates;

    // Construct the Trie and count occurrences of each folder content
    for (const auto& path : paths) {
        TrieNode* node = root;
        for (const auto& folder : path) {
            if (node->children.find(folder) == node->children.end()) {
                node->children[folder] = new TrieNode();
            }
            node = node->children[folder];
        }
        node->count++;
    }

    // Identify and mark duplicate folders for deletion
    std::function<void(TrieNode*, std::string)> traverse = [&](TrieNode* node, std::string path) {
        if (node->count > 1) {
            duplicates.push_back(path);
        }
        for (const auto& child : node->children) {
            traverse(child.second, path + "/" + child.first);
        }
    };
    traverse(root, "");

    return duplicates;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of paths and $m$ is the maximum number of folders in a path. This is because we are constructing the Trie and then traversing it.
> - **Space Complexity:** $O(n \cdot m)$, as we store the Trie and the counts of folder contents.
> - **Optimality proof:** The Trie data structure allows us to efficiently store and compare folder contents, reducing the time complexity from $O(n^2 \cdot m)$ to $O(n \cdot m)$. This is the best possible complexity for this problem.

---

### Final Notes

**Learning Points:**
- Using a Trie data structure to efficiently store and compare folder contents.
- Constructing a Trie by iterating through each path and adding folders to the Trie.
- Keeping track of the number of occurrences of each folder content by storing a count at each node in the Trie.
- Traversing the Trie to identify and mark duplicate folders for deletion.

**Mistakes to Avoid:**
- Not considering the efficiency of the algorithm and using a brute force approach.
- Not using a Trie data structure to store and compare folder contents.
- Not keeping track of the number of occurrences of each folder content.
- Not traversing the Trie to identify and mark duplicate folders for deletion.