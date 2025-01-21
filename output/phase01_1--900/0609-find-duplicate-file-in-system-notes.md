## Find Duplicate File in System

**Problem Link:** https://leetcode.com/problems/find-duplicate-file-in-system/description

**Problem Statement:**
- Input format: A list of paths, where each path is a string that represents a file path.
- Constraints: Each path is a string of length `1 <= path.length <= 2000`.
- Expected output format: A list of lists, where each sublist contains the paths of duplicate files.
- Key requirements and edge cases to consider: 
  - A file is considered a duplicate if its content is the same as another file.
  - The same file can be listed multiple times in the input list.
- Example test cases with explanations:
  - Example 1: Input: `["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]`
    - Output: `[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]`
  - Example 2: Input: `["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]`
    - Output: `[["root/a/1.txt","root/c/3.txt"],["root/a/2.txt","root/c/d/4.txt"]]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare the content of each file with every other file.
- Step-by-step breakdown of the solution:
  1. Create a list to store the contents of each file.
  2. Iterate over each file path and extract its content.
  3. Compare the content of the current file with the content of every other file.
  4. If a duplicate is found, add the paths of the duplicate files to the result list.
- Why this approach comes to mind first: It's a straightforward approach that checks every possible pair of files.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

vector<vector<string>> findDuplicate(vector<string>& paths) {
    unordered_map<string, vector<string>> contentMap;
    for (const auto& path : paths) {
        size_t spacePos = path.find(' ');
        string dir = path.substr(0, spacePos);
        string fileContent = path.substr(spacePos + 1);
        size_t openParenPos = fileContent.find('(');
        string fileName = fileContent.substr(0, openParenPos);
        string content = fileContent.substr(openParenPos + 1, fileContent.size() - openParenPos - 2);
        if (contentMap.find(content) == contentMap.end()) {
            contentMap[content] = {dir + '/' + fileName};
        } else {
            contentMap[content].push_back(dir + '/' + fileName);
        }
    }
    vector<vector<string>> result;
    for (const auto& pair : contentMap) {
        if (pair.second.size() > 1) {
            result.push_back(pair.second);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of paths and $m$ is the average length of a path.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of paths and $m$ is the average length of a path.
> - **Why these complexities occur:** The brute force approach involves iterating over each file path and comparing its content with every other file.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a hash map to store the contents of each file and their corresponding paths.
- Detailed breakdown of the approach:
  1. Create a hash map to store the contents of each file and their corresponding paths.
  2. Iterate over each file path and extract its content.
  3. Use the content as a key in the hash map and add the current file path to the list of values.
  4. If a duplicate is found, add the paths of the duplicate files to the result list.
- Proof of optimality: This approach has a time complexity of $O(n \cdot m)$ and a space complexity of $O(n \cdot m)$, where $n$ is the number of paths and $m$ is the average length of a path.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

vector<vector<string>> findDuplicate(vector<string>& paths) {
    unordered_map<string, vector<string>> contentMap;
    for (const auto& path : paths) {
        size_t spacePos = path.find(' ');
        string dir = path.substr(0, spacePos);
        size_t openParenPos, closeParenPos;
        while ((openParenPos = path.find('(', spacePos)) != string::npos) {
            closeParenPos = path.find(')', openParenPos);
            string fileName = path.substr(spacePos + 1, openParenPos - spacePos - 1);
            string content = path.substr(openParenPos + 1, closeParenPos - openParenPos - 1);
            if (contentMap.find(content) == contentMap.end()) {
                contentMap[content] = {dir + '/' + fileName};
            } else {
                contentMap[content].push_back(dir + '/' + fileName);
            }
            spacePos = closeParenPos + 1;
        }
    }
    vector<vector<string>> result;
    for (const auto& pair : contentMap) {
        if (pair.second.size() > 1) {
            result.push_back(pair.second);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of paths and $m$ is the average length of a path.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of paths and $m$ is the average length of a path.
> - **Optimality proof:** This approach has the same time and space complexities as the brute force approach but is more efficient in practice due to the use of a hash map.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash maps, string manipulation, and duplicate detection.
- Problem-solving patterns identified: Using a hash map to store contents and their corresponding paths.
- Optimization techniques learned: Using a hash map to reduce the time complexity of duplicate detection.
- Similar problems to practice: `Find All Duplicates in an Array`, `Find the Duplicate Number`, and `Find the Duplicate in an Array`.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as empty paths or paths with no content.
- Edge cases to watch for: Paths with multiple files, paths with no files, and paths with empty contents.
- Performance pitfalls: Using a brute force approach with a high time complexity.
- Testing considerations: Testing with different types of input, such as paths with multiple files, paths with no files, and paths with empty contents.