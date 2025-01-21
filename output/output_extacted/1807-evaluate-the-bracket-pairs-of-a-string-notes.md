## Evaluate the Bracket Pairs of a String

**Problem Link:** https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/description

**Problem Statement:**
- Input: A string `s` containing bracket pairs and a 2D array `knowledge` where each element is a string representing a key-value pair.
- Constraints: The string `s` only contains lowercase letters and bracket pairs, and the `knowledge` array does not contain any duplicate keys.
- Expected Output: Evaluate the bracket pairs in the string `s` based on the `knowledge` array.
- Key Requirements: Replace each bracket pair with its corresponding value from the `knowledge` array. If a bracket pair is not found in the `knowledge` array, replace it with `?`.
- Example Test Cases:
  - Input: `s = "(name)is(age)yearsold(is)awesome", knowledge = [["name","John"],["age","20"]]`
  - Output: `"Johnis20yearsold?isawesome"`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first step is to identify the bracket pairs in the string `s`. We can do this by iterating through the string and finding the indices of the opening and closing brackets.
- Step-by-step breakdown of the solution:
  1. Iterate through the string `s` to find the bracket pairs.
  2. For each bracket pair, extract the key inside the brackets.
  3. Iterate through the `knowledge` array to find the value corresponding to the key.
  4. Replace the bracket pair with its corresponding value or `?` if not found.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

string evaluate(string s, vector<vector<string>>& knowledge) {
    unordered_map<string, string> knowledgeMap;
    for (auto& pair : knowledge) {
        knowledgeMap[pair[0]] = pair[1];
    }

    string result = "";
    bool inBrackets = false;
    string key = "";

    for (char c : s) {
        if (c == '(') {
            inBrackets = true;
        } else if (c == ')') {
            inBrackets = false;
            if (knowledgeMap.find(key) != knowledgeMap.end()) {
                result += knowledgeMap[key];
            } else {
                result += '?';
            }
            key = "";
        } else if (inBrackets) {
            key += c;
        } else {
            result += c;
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of the string `s` and $m$ is the total length of all strings in the `knowledge` array. This is because we iterate through the string `s` once and through the `knowledge` array once to build the `knowledgeMap`.
> - **Space Complexity:** $O(m)$, where $m$ is the total length of all strings in the `knowledge` array. This is because we store the `knowledge` array in a `knowledgeMap`.
> - **Why these complexities occur:** The time complexity occurs because we iterate through the string `s` and the `knowledge` array once. The space complexity occurs because we store the `knowledge` array in a `knowledgeMap`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use an `unordered_map` to store the `knowledge` array, which allows us to look up values in constant time.
- Detailed breakdown of the approach:
  1. Build a `knowledgeMap` from the `knowledge` array.
  2. Iterate through the string `s` and extract the bracket pairs.
  3. For each bracket pair, look up its value in the `knowledgeMap` and replace it with the value or `?` if not found.

```cpp
string evaluate(string s, vector<vector<string>>& knowledge) {
    unordered_map<string, string> knowledgeMap;
    for (auto& pair : knowledge) {
        knowledgeMap[pair[0]] = pair[1];
    }

    string result = "";
    bool inBrackets = false;
    string key = "";

    for (char c : s) {
        if (c == '(') {
            inBrackets = true;
        } else if (c == ')') {
            inBrackets = false;
            if (knowledgeMap.find(key) != knowledgeMap.end()) {
                result += knowledgeMap[key];
            } else {
                result += '?';
            }
            key = "";
        } else if (inBrackets) {
            key += c;
        } else {
            result += c;
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of the string `s` and $m$ is the total length of all strings in the `knowledge` array.
> - **Space Complexity:** $O(m)$, where $m$ is the total length of all strings in the `knowledge` array.
> - **Optimality proof:** This is the optimal solution because we iterate through the string `s` and the `knowledge` array once, and we use a `knowledgeMap` to look up values in constant time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, string manipulation, and hash map usage.
- Problem-solving patterns identified: Using a `knowledgeMap` to look up values in constant time.
- Optimization techniques learned: Using an `unordered_map` to reduce lookup time.
- Similar problems to practice: String manipulation and hash map usage problems.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as empty strings or bracket pairs.
- Edge cases to watch for: Empty strings, bracket pairs without a corresponding value in the `knowledge` array.
- Performance pitfalls: Using a linear search instead of a hash map to look up values.
- Testing considerations: Test with different input sizes and edge cases to ensure the solution is correct and efficient.