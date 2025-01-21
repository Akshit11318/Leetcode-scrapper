## Longest Absolute File Path

**Problem Link:** https://leetcode.com/problems/longest-absolute-file-path/description

**Problem Statement:**
- Input: A string `input` containing the file system hierarchy in a specific format.
- Constraints: The input string is well-formed, and the hierarchy is valid.
- Expected Output: The length of the longest absolute path in the file system.
- Key Requirements:
  - Each directory or file name does not contain a dot (`.`).
  - The directory or file name does not start with a slash (`/`).
  - The input only contains directories and files in the format described.
- Edge Cases: Empty input string, single directory or file, multiple levels of directories.
- Example Test Cases:
  - Input: `"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"`
    - Expected Output: `20` (Explanation: `dir/subdir2/file.ext`)
  - Input: `"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"`
    - Expected Output: `32` (Explanation: `dir/subdir2/subsubdir2/file2.ext`)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Parse the input string line by line, and for each line, determine its depth based on the number of tabs (`\t`) at the beginning.
- Step-by-step breakdown:
  1. Split the input string into lines.
  2. For each line, count the number of tabs at the beginning to determine its depth.
  3. Keep track of the current directory path and its length.
  4. If the line represents a file (contains a dot), calculate the length of the absolute path by adding the file name to the current directory path.
  5. Update the maximum length found so far.
- Why this approach comes to mind first: It directly follows from understanding the input format and the requirement to find the longest absolute path.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

int lengthLongestPath(std::string input) {
    std::istringstream iss(input);
    std::string line;
    int maxLength = 0;
    std::vector<std::string> path;
    
    while (std::getline(iss, line)) {
        int depth = 0;
        while (line[depth] == '\t') depth++;
        line = line.substr(depth); // Remove tabs
        
        // Adjust path based on depth
        while (path.size() > depth) path.pop_back();
        
        if (path.empty()) path.push_back(line);
        else {
            path.push_back(path.back() + "/" + line);
        }
        
        // Check if it's a file
        if (line.find('.') != std::string::npos) {
            maxLength = std::max(maxLength, static_cast<int>(path.back().length()));
        }
    }
    
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of lines in the input string and $m$ is the maximum length of a line. This is because we process each character in each line.
> - **Space Complexity:** $O(n \cdot m)$, for storing the current path and its components.
> - **Why these complexities occur:** The brute force approach involves parsing the input string line by line and character by character, leading to linear time complexity with respect to the input size. The space complexity is also linear because, in the worst case, we might need to store all lines in the path.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of reconstructing the full path for each file, we can keep track of the length of the path at each level and update it as we move through the directory hierarchy.
- Detailed breakdown:
  1. Split the input string into lines and process each line to determine its depth.
  2. Use a stack to keep track of the lengths of the directories at each level.
  3. When encountering a file, calculate its absolute path length by adding its name to the length of the path at its level.
  4. Update the maximum length found.
- Proof of optimality: This approach avoids unnecessary string concatenations and directly calculates the lengths of paths, making it more efficient than the brute force approach.

```cpp
int lengthLongestPath(std::string input) {
    std::istringstream iss(input);
    std::string line;
    int maxLength = 0;
    std::vector<int> stack = {0}; // Initialize with root directory
    
    while (std::getline(iss, line)) {
        int depth = 0;
        while (line[depth] == '\t') depth++;
        line = line.substr(depth); // Remove tabs
        
        // Adjust stack based on depth
        while (stack.size() > depth + 1) stack.pop_back();
        
        int pathLength = stack.back() + line.length() + 1; // +1 for the slash
        stack.push_back(pathLength);
        
        // Check if it's a file
        if (line.find('.') != std::string::npos) {
            maxLength = std::max(maxLength, pathLength - 1); // Subtract 1 because we added 1 for the slash
        }
    }
    
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of lines and $m$ is the average length of a line. This is because we still process each line and its characters.
> - **Space Complexity:** $O(n)$, for the stack that keeps track of the lengths of the paths at each level.
> - **Optimality proof:** This approach is optimal because it processes the input in a single pass and uses a minimal amount of extra space to keep track of the necessary information. It avoids unnecessary string concatenations, making it more efficient than the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Parsing, stack usage, and path manipulation.
- Problem-solving patterns: Breaking down the problem into manageable parts (lines and their depths), using data structures (stack) to efficiently track and update information.
- Optimization techniques: Avoiding unnecessary string concatenations, using integers to represent lengths instead of reconstructing full paths.

**Mistakes to Avoid:**
- Not correctly handling the depth of directories and files.
- Not updating the maximum length correctly.
- Using inefficient data structures or algorithms for tracking path lengths.
- Not considering edge cases, such as an empty input string or a single directory/file.