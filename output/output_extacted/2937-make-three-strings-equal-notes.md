## Make Three Strings Equal
**Problem Link:** https://leetcode.com/problems/make-three-strings-equal/description

**Problem Statement:**
- Input format and constraints: Three binary strings `s1`, `s2`, and `s3` are given, each of length `n`.
- Expected output format: Return `true` if it is possible to make the strings equal by performing a sequence of operations on the strings. Otherwise, return `false`.
- Key requirements and edge cases to consider: 
    - A valid operation is to delete a substring of length `1` from the beginning of a string and append it to the end of the same string. 
    - The strings are equal if they become the same after some sequence of operations.
- Example test cases with explanations: 
    - Example 1: `s1 = "abc", s2 = "bca", s3 = "cab"`, return `true`. 
    - Example 2: `s1 = "abc", s2 = "bca", s3 = "bac"`, return `false`.

### Brute Force Approach

**Explanation:**
- Initial thought process: To check if the strings can be made equal, we can try all possible operations and check if the strings become equal after any sequence of operations.
- Step-by-step breakdown of the solution: 
    1. Generate all permutations of the strings by performing the allowed operations.
    2. Check if any permutation of the three strings are equal.
- Why this approach comes to mind first: This approach is straightforward and tries to explore all possibilities.

```cpp
#include <iostream>
#include <string>
#include <set>

bool makeEqual(std::string s1, std::string s2, std::string s3) {
    std::set<std::string> s1_set, s2_set, s3_set;
    std::set<std::string> temp_set;

    temp_set.insert(s1);
    for (int i = 0; i < s1.size(); i++) {
        std::string temp = s1.substr(i + 1) + s1.substr(0, i + 1);
        temp_set.insert(temp);
    }
    s1_set = temp_set;

    temp_set.clear();
    temp_set.insert(s2);
    for (int i = 0; i < s2.size(); i++) {
        std::string temp = s2.substr(i + 1) + s2.substr(0, i + 1);
        temp_set.insert(temp);
    }
    s2_set = temp_set;

    temp_set.clear();
    temp_set.insert(s3);
    for (int i = 0; i < s3.size(); i++) {
        std::string temp = s3.substr(i + 1) + s3.substr(0, i + 1);
        temp_set.insert(temp);
    }
    s3_set = temp_set;

    for (const auto& str : s1_set) {
        if (s2_set.find(str) != s2_set.end() && s3_set.find(str) != s3_set.end()) {
            return true;
        }
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times 2^n)$ where $n$ is the length of the strings. This is because for each string, we generate all possible permutations.
> - **Space Complexity:** $O(2^n)$ for storing the permutations of each string.
> - **Why these complexities occur:** These complexities occur because we are generating all possible permutations of the strings, which results in exponential time and space complexity.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: If the three strings can be made equal, they must have the same characters.
- Detailed breakdown of the approach: 
    1. Check if the strings have the same characters.
    2. If they do, check if any rotation of the strings is equal.
- Proof of optimality: This approach is optimal because it only checks for the necessary conditions for the strings to be made equal, without generating all possible permutations.
- Why further optimization is impossible: This approach already checks for the minimum necessary conditions, so further optimization is not possible.

```cpp
#include <iostream>
#include <string>
#include <unordered_set>

bool makeEqual(std::string s1, std::string s2, std::string s3) {
    std::unordered_set<char> s1_set, s2_set, s3_set;

    for (char c : s1) s1_set.insert(c);
    for (char c : s2) s2_set.insert(c);
    for (char c : s3) s3_set.insert(c);

    if (s1_set != s2_set || s1_set != s3_set) return false;

    int n = s1.size();
    for (int i = 0; i < n; i++) {
        std::string temp1 = s1.substr(i) + s1.substr(0, i);
        std::string temp2 = s2.substr(i) + s2.substr(0, i);
        std::string temp3 = s3.substr(i) + s3.substr(0, i);

        if (temp1 == temp2 && temp2 == temp3) return true;
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the strings. This is because we only check for the necessary conditions.
> - **Space Complexity:** $O(1)$ for storing the sets of characters.
> - **Optimality proof:** This approach is optimal because it only checks for the necessary conditions for the strings to be made equal, without generating all possible permutations.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Checking for necessary conditions, using sets to store unique characters.
- Problem-solving patterns identified: Checking for necessary conditions before exploring all possibilities.
- Optimization techniques learned: Avoiding generating all possible permutations, using sets to store unique characters.
- Similar problems to practice: Problems that require checking for necessary conditions before exploring all possibilities.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for necessary conditions before exploring all possibilities.
- Edge cases to watch for: Strings with different characters, strings with the same characters but different rotations.
- Performance pitfalls: Generating all possible permutations, using inefficient data structures.
- Testing considerations: Testing with different inputs, including edge cases.