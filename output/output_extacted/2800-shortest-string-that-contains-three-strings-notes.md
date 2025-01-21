## Shortest String That Contains Three Strings
**Problem Link:** https://leetcode.com/problems/shortest-string-that-contains-three-strings/description

**Problem Statement:**
- Input: Three strings `a`, `b`, and `c`.
- Output: The shortest string that contains all three strings as substrings. If no such string exists, return an empty string.
- Key requirements: The output string must contain all three input strings as substrings.
- Edge cases: Handle cases where the input strings are empty or where no string can contain all three as substrings.

### Brute Force Approach
**Explanation:**
- The initial thought process involves trying all possible combinations and permutations of the input strings to find the shortest one that contains all three.
- Step-by-step breakdown:
  1. Generate all permutations of the three strings.
  2. For each permutation, concatenate the strings to form a single string.
  3. Check if the concatenated string contains all three input strings as substrings.
  4. Keep track of the shortest string that satisfies the condition.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// Function to check if a string contains another as a substring
bool contains(const string& str, const string& substr) {
    return str.find(substr) != string::npos;
}

string shortestConcatenationBruteForce(const string& a, const string& b, const string& c) {
    vector<string> perms = {a + b + c, a + c + b, b + a + c, b + c + a, c + a + b, c + b + a};
    string shortest;
    
    for (const auto& perm : perms) {
        if (contains(perm, a) && contains(perm, b) && contains(perm, c)) {
            if (shortest.empty() || perm.length() < shortest.length()) {
                shortest = perm;
            }
        }
    }
    
    return shortest;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot m)$, where $n$ is the number of strings (3 in this case) and $m$ is the maximum length of a string. The factorial comes from generating all permutations, and $m$ comes from checking if a string is a substring of another.
> - **Space Complexity:** $O(m)$, for storing the permutations and the result.
> - **Why these complexities occur:** The brute force approach generates all permutations of the input strings and checks each one, leading to exponential time complexity due to permutation generation.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of trying all permutations, we can use a more systematic approach to find the shortest string. This involves considering the overlap between strings to minimize the total length.
- Detailed breakdown:
  1. Initialize the result with the first string.
  2. For each of the remaining strings, find the maximum overlap with the current result and append the non-overlapping part to the result.
  3. Repeat step 2 for all remaining strings.

```cpp
string shortestConcatenationOptimal(const string& a, const string& b, const string& c) {
    string result = a;
    vector<string> remaining = {b, c};
    
    while (!remaining.empty()) {
        string maxOverlapStr;
        int maxOverlap = 0;
        
        for (const auto& str : remaining) {
            for (int i = 1; i <= min(result.length(), str.length()); ++i) {
                if (result.substr(result.length() - i) == str.substr(0, i)) {
                    if (i > maxOverlap) {
                        maxOverlap = i;
                        maxOverlapStr = str;
                    }
                }
            }
        }
        
        if (maxOverlapStr.empty()) {
            // If no overlap is found, simply append the next string
            result += remaining[0];
            remaining.erase(remaining.begin());
        } else {
            result += maxOverlapStr.substr(maxOverlap);
            auto it = find(remaining.begin(), remaining.end(), maxOverlapStr);
            if (it != remaining.end()) {
                remaining.erase(it);
            }
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^2)$, where $m$ is the maximum length of a string. This is because for each string, we potentially check for overlaps with the current result string.
> - **Space Complexity:** $O(m)$, for storing the result and the remaining strings.
> - **Optimality proof:** This approach is optimal because it systematically considers the maximum overlap between strings, ensuring the shortest possible result. It avoids the exponential complexity of generating all permutations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: permutation generation, substring checking, and overlap optimization.
- Problem-solving patterns identified: systematic approach to finding the shortest string by considering overlaps.
- Optimization techniques learned: avoiding brute force by leveraging string overlaps.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases (e.g., empty strings), incorrect overlap calculation.
- Edge cases to watch for: empty input strings, no possible string containing all three as substrings.
- Performance pitfalls: using brute force for large inputs.
- Testing considerations: thorough testing with various input combinations, including edge cases.