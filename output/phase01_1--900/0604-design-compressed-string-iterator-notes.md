## Design Compressed String Iterator
**Problem Link:** https://leetcode.com/problems/design-compressed-string-iterator/description

**Problem Statement:**
- Input format: A string `compressed` representing a compressed string where each character is followed by its count (e.g., "3[a]2[bc]" means "aaabcbc").
- Constraints: The compressed string is guaranteed to be valid.
- Expected output format: Implement a class `StringIterator` that supports two operations:
  - `next()`: Returns the next character in the compressed string. If there are no more characters, returns a space.
  - `hasNext()`: Returns `true` if there are more characters in the compressed string; otherwise, returns `false`.
- Key requirements and edge cases:
  - Handle compressed strings with varying lengths and characters.
  - Ensure `next()` and `hasNext()` work correctly for all valid compressed strings.
- Example test cases:
  - `compressed = "3[a]2[bc]"`: The iterator should return 'a', 'a', 'a', 'b', 'c', 'b', 'c', and then a space.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Expand the compressed string into a regular string and then iterate over it.
- Step-by-step breakdown:
  1. Parse the compressed string to expand it into a full string.
  2. Implement `next()` to return the next character in the expanded string.
  3. Implement `hasNext()` to check if there are more characters in the expanded string.
- Why this approach comes to mind first: It's straightforward and directly addresses the problem statement.

```cpp
class StringIterator {
private:
    string expanded;
    int index;

public:
    StringIterator(string compressed) {
        int i = 0;
        while (i < compressed.size()) {
            int count = 0;
            while (i < compressed.size() && isdigit(compressed[i])) {
                count = count * 10 + (compressed[i] - '0');
                i++;
            }
            i++; // Skip '['
            string str = "";
            while (i < compressed.size() && compressed[i] != ']') {
                str += compressed[i];
                i++;
            }
            i++; // Skip ']'
            for (int j = 0; j < count; j++) {
                expanded += str;
            }
        }
        index = 0;
    }

    char next() {
        if (hasNext()) {
            return expanded[index++];
        }
        return ' ';
    }

    bool hasNext() {
        return index < expanded.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the compressed string, because we iterate over the compressed string once to expand it, and then each `next()` operation takes constant time. However, expanding the string can lead to a large expanded string, making this approach inefficient for very large inputs.
> - **Space Complexity:** $O(n)$ for storing the expanded string, which can be much larger than the original compressed string.
> - **Why these complexities occur:** The brute force approach involves expanding the compressed string, which can result in a large string, leading to high memory usage and a one-time high computational cost for expansion.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of expanding the entire compressed string, we can parse it on the fly as we iterate.
- Detailed breakdown:
  1. Initialize an index to track the current position in the compressed string.
  2. Implement `next()` to parse the compressed string from the current index, extracting the count and character(s), and then return the next character.
  3. Implement `hasNext()` by checking if there are more characters to parse in the compressed string.
- Proof of optimality: This approach avoids expanding the entire string, reducing memory usage significantly, especially for large inputs.

```cpp
class StringIterator {
private:
    string compressed;
    int index;
    char currChar;
    int count;

public:
    StringIterator(string compressed) : compressed(compressed), index(0), count(0) {
        // Initialize next character
        if (hasNext()) {
            next();
        }
    }

    char next() {
        if (!hasNext()) {
            return ' ';
        }
        count--;
        char ret = currChar;
        if (count == 0) {
            // Parse next sequence
            index++; // Skip the number
            index++; // Skip '['
            string str = "";
            while (index < compressed.size() && compressed[index] != ']') {
                str += compressed[index];
                index++;
            }
            index++; // Skip ']'
            int newCount = 0;
            while (index > 0 && isdigit(compressed[index-1])) {
                newCount = newCount * 10 + (compressed[index-1] - '0');
                index--;
            }
            count = newCount;
            currChar = str[0];
            if (str.size() > 1) {
                currChar = str;
            } else {
                currChar = str[0];
            }
        }
        return ret;
    }

    bool hasNext() {
        while (index < compressed.size() && (compressed[index] == ']' || isdigit(compressed[index]))) {
            index++;
        }
        return index < compressed.size();
    }
};
```

However, the optimal approach provided above still has some redundancy in parsing the string and handling multi-character sequences. A more streamlined version would focus on parsing the compressed string efficiently, handling counts and characters in a single pass without unnecessary backtracking or redundant checks.

A more optimized version of the `StringIterator` class, focusing on a streamlined and efficient parsing of the compressed string, would look like this:

```cpp
class StringIterator {
private:
    string compressed;
    int index;
    string currStr;
    int currCount;

public:
    StringIterator(string compressed) : compressed(compressed), index(0), currCount(0) {
        // Initialize next sequence
        parseNext();
    }

    char next() {
        if (!hasNext()) {
            return ' ';
        }
        char ret = currStr[0];
        currCount--;
        if (currCount == 0) {
            parseNext();
        }
        return ret;
    }

    bool hasNext() {
        return currCount > 0 || index < compressed.size();
    }

private:
    void parseNext() {
        if (index >= compressed.size()) {
            return;
        }
        int count = 0;
        while (index < compressed.size() && isdigit(compressed[index])) {
            count = count * 10 + (compressed[index] - '0');
            index++;
        }
        index++; // Skip '['
        currStr = "";
        while (index < compressed.size() && compressed[index] != ']') {
            currStr += compressed[index];
            index++;
        }
        index++; // Skip ']'
        currCount = count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the compressed string, as we parse the string once, and each operation takes constant time.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input string, as we only use a constant amount of space to store the current sequence and index.
> - **Optimality proof:** This approach is optimal because it minimizes both time and space complexity by parsing the string on the fly and avoiding unnecessary expansions or redundant operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Parsing, iteration, and string manipulation.
- Problem-solving patterns: Breaking down complex strings into manageable parts and handling them iteratively.
- Optimization techniques: Avoiding unnecessary operations and minimizing memory usage.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect parsing of counts and strings, and failing to handle edge cases properly.
- Edge cases to watch for: Empty strings, strings with no compressed sequences, and sequences with counts of zero.
- Performance pitfalls: Expanding the entire compressed string unnecessarily, leading to high memory usage and computational costs.
- Testing considerations: Ensure thorough testing of all methods (`next()`, `hasNext()`) with various compressed strings, including edge cases.