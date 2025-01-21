## Find All Good Strings

**Problem Link:** https://leetcode.com/problems/find-all-good-strings/description

**Problem Statement:**
- Input format and constraints: Given the length of a string `n`, and two strings `s1` and `s2`, find all good strings of length `n` that can be formed using the characters of `s1` and `s2`. A string is good if it does not contain `s1` as a substring and its reverse is not a substring of `s2`.
- Expected output format: A list of all good strings.
- Key requirements and edge cases to consider: Handle cases where `n` is large, and `s1` and `s2` are of varying lengths. Also, consider cases where `s1` and `s2` are the same.
- Example test cases with explanations:
  - For `n = 3`, `s1 = "abc"`, and `s2 = "cba"`, the good strings would be those that do not contain `abc` and whose reverse does not contain `cba`.
  - For `n = 5`, `s1 = "aaaa"`, and `s2 = "aaaa"`, the good strings would be those that do not contain `aaaa` and whose reverse does not contain `aaaa`, which in this case would be very limited due to the repetitive nature of `s1` and `s2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible strings of length `n` and check each one to see if it contains `s1` as a substring and if its reverse contains `s2` as a substring.
- Step-by-step breakdown of the solution:
  1. Generate all possible strings of length `n`.
  2. For each string, check if it contains `s1` as a substring.
  3. If it does not contain `s1`, reverse the string and check if it contains `s2` as a substring.
  4. If neither condition is met, add the string to the list of good strings.
- Why this approach comes to mind first: It's straightforward and ensures that all possible strings are considered.

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> generateAllGoodStrings(int n, string s1, string s2) {
    vector<string> goodStrings;
    // Generate all possible strings of length n
    string chars = "abcdefghijklmnopqrstuvwxyz";
    vector<string> allStrings;
    generateAllStrings(allStrings, "", n, chars);
    
    for (const auto& str : allStrings) {
        // Check if str contains s1
        if (str.find(s1) == string::npos) {
            // Reverse str and check if it contains s2
            string reversedStr = str;
            reverse(reversedStr.begin(), reversedStr.end());
            if (reversedStr.find(s2) == string::npos) {
                goodStrings.push_back(str);
            }
        }
    }
    return goodStrings;
}

void generateAllStrings(vector<string>& allStrings, string current, int n, const string& chars) {
    if (current.size() == n) {
        allStrings.push_back(current);
        return;
    }
    for (char c : chars) {
        generateAllStrings(allStrings, current + c, n, chars);
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(26^n \cdot n)$, where $n$ is the length of the string. The $26^n$ comes from generating all possible strings (assuming lowercase English letters), and the $n$ comes from the string operations (finding substrings and reversing).
> - **Space Complexity:** $O(26^n \cdot n)$, as we need to store all generated strings.
> - **Why these complexities occur:** The brute force approach generates an exponential number of strings and then checks each one, leading to high time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible strings and then filtering, use a more targeted approach that builds strings character by character while ensuring they do not contain `s1` and their reverse does not contain `s2`.
- Detailed breakdown of the approach:
  1. Initialize an empty string `str`.
  2. Use a recursive function to build `str` character by character.
  3. At each step, ensure that adding the next character does not result in a string containing `s1` or its reverse containing `s2`.
  4. If a valid string of length `n` is formed, add it to the list of good strings.
- Proof of optimality: This approach avoids generating unnecessary strings, thus reducing the time complexity significantly compared to the brute force method.

```cpp
vector<string> generateAllGoodStringsOptimal(int n, string s1, string s2) {
    vector<string> goodStrings;
    string chars = "abcdefghijklmnopqrstuvwxyz";
    generateGoodString(goodStrings, "", n, s1, s2, chars);
    return goodStrings;
}

void generateGoodString(vector<string>& goodStrings, string current, int n, const string& s1, const string& s2, const string& chars) {
    if (current.size() == n) {
        goodStrings.push_back(current);
        return;
    }
    for (char c : chars) {
        string next = current + c;
        if (next.find(s1) == string::npos) {
            string reversedNext = next;
            reverse(reversedNext.begin(), reversedNext.end());
            if (reversedNext.find(s2) == string::npos) {
                generateGoodString(goodStrings, next, n, s1, s2, chars);
            }
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(26^n)$ in the worst case, but significantly improved in practice due to early pruning of branches that would lead to strings containing `s1` or having reverses containing `s2`.
> - **Space Complexity:** $O(n)$ for the recursion stack and $O(26^n)$ for storing the good strings, similar to the brute force approach but with the potential for much less actual memory usage due to pruning.
> - **Optimality proof:** This approach is optimal because it generates only strings that have the potential to be good, pruning branches as soon as they violate the conditions, thus minimizing unnecessary computation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Recursive string generation, substring checking, and string reversal.
- Problem-solving patterns identified: Using recursion to build solutions incrementally and pruning branches to optimize.
- Optimization techniques learned: Early checking for conditions that would disqualify a string from being good, thus avoiding unnecessary computation.
- Similar problems to practice: Other string manipulation and generation problems, especially those involving recursive approaches and optimization through pruning.

**Mistakes to Avoid:**
- Common implementation errors: Not properly checking for substring presence or incorrect string reversal.
- Edge cases to watch for: Handling cases where `n` is 0, or `s1` and `s2` are empty, and ensuring the approach works for all possible input combinations.
- Performance pitfalls: Failing to prune branches early, leading to exponential time complexity.
- Testing considerations: Thoroughly testing with various lengths of `n`, `s1`, and `s2`, including edge cases.