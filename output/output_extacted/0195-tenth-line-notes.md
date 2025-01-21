## Tenth Line
**Problem Link:** https://leetcode.com/problems/tenth-line/description

**Problem Statement:**
- Input format: The input is a file with multiple lines of text.
- Constraints: The file can have any number of lines, and each line can have any number of characters.
- Expected output format: The tenth line of the file.
- Key requirements and edge cases to consider:
  - If the file has fewer than ten lines, return an empty string.
  - If the file has exactly ten lines, return the tenth line.
  - If the file has more than ten lines, return the tenth line.
- Example test cases with explanations:
  - If the file has the following lines:
    ```
    line1
    line2
    line3
    line4
    line5
    line6
    line7
    line8
    line9
    line10
    ```
    The output should be `line10`.
  - If the file has the following lines:
    ```
    line1
    line2
    line3
    line4
    line5
    line6
    line7
    line8
    line9
    ```
    The output should be an empty string.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Read the entire file into memory and store all lines in a data structure.
- Step-by-step breakdown of the solution:
  1. Open the file and read all lines into a vector of strings.
  2. Check if the vector has at least ten elements.
  3. If it does, return the tenth element. Otherwise, return an empty string.
- Why this approach comes to mind first: It's the simplest way to solve the problem, as it doesn't require any complex logic or data structures.

```cpp
#include <fstream>
#include <vector>
#include <string>

std::string tenthLine(const std::string& filePath) {
    std::ifstream file(filePath);
    if (!file.is_open()) {
        return "";
    }

    std::vector<std::string> lines;
    std::string line;
    while (std::getline(file, line)) {
        lines.push_back(line);
    }

    if (lines.size() < 10) {
        return "";
    }

    return lines[9];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of lines in the file. This is because we're reading all lines into memory.
> - **Space Complexity:** $O(n)$, where $n$ is the number of lines in the file. This is because we're storing all lines in a vector.
> - **Why these complexities occur:** These complexities occur because we're reading the entire file into memory and storing all lines in a data structure.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We only need to keep track of the current line number and the last line we've read.
- Detailed breakdown of the approach:
  1. Open the file and read it line by line.
  2. Keep track of the current line number.
  3. If the current line number is 10, return the current line.
  4. If we've reached the end of the file and haven't returned a line, return an empty string.
- Proof of optimality: This approach is optimal because it only reads the file once and doesn't store any unnecessary data.
- Why further optimization is impossible: This approach is already optimal because it only reads the necessary data and doesn't perform any unnecessary operations.

```cpp
#include <fstream>
#include <string>

std::string tenthLine(const std::string& filePath) {
    std::ifstream file(filePath);
    if (!file.is_open()) {
        return "";
    }

    std::string line;
    int lineNumber = 0;
    while (std::getline(file, line)) {
        lineNumber++;
        if (lineNumber == 10) {
            return line;
        }
    }

    return "";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of lines in the file. This is because we're reading the file line by line.
> - **Space Complexity:** $O(1)$, because we're only storing a constant amount of data.
> - **Optimality proof:** This approach is optimal because it only reads the necessary data and doesn't perform any unnecessary operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Reading files, keeping track of line numbers, and optimizing memory usage.
- Problem-solving patterns identified: Reading files line by line to avoid storing unnecessary data.
- Optimization techniques learned: Avoiding unnecessary memory allocations and only reading necessary data.
- Similar problems to practice: Reading specific lines from a file, counting the number of lines in a file, and searching for specific text in a file.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the file is open before reading it, not checking for errors when reading the file, and not handling edge cases.
- Edge cases to watch for: Files with fewer than ten lines, files with exactly ten lines, and files with more than ten lines.
- Performance pitfalls: Reading the entire file into memory, storing unnecessary data, and performing unnecessary operations.
- Testing considerations: Testing with files of different sizes, testing with files with different line counts, and testing with files containing different types of data.