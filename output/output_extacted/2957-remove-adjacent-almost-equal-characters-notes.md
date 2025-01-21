## Remove Adjacent Almost Equal Characters
**Problem Link:** [https://leetcode.com/problems/remove-adjacent-almost-equal-characters/description](https://leetcode.com/problems/remove-adjacent-almost-equal-characters/description)

**Problem Statement:**
- Input format: a string `S` containing lowercase English letters.
- Constraints: `1 <= S.length <= 1000`.
- Expected output format: a string with all adjacent almost equal characters removed.
- Key requirements and edge cases to consider: characters are considered almost equal if their ASCII values differ by at most 1.
- Example test cases:
  - Input: "abcba"
    Output: ""
  - Input: "abba"
    Output: ""

---

### Brute Force Approach

**Explanation:**
- Initial thought process: iterate over the string and compare each character with its adjacent ones.
- Step-by-step breakdown of the solution:
  1. Initialize an empty result string.
  2. Iterate over the input string.
  3. For each character, check if it is almost equal to the last character in the result string.
  4. If they are almost equal, remove the last character from the result string.
  5. If they are not almost equal, append the current character to the result string.
- Why this approach comes to mind first: it is a straightforward, intuitive solution.

```cpp
using namespace std;

string removeAlmostEqualCharacters(string S) {
    string result = "";
    for (char c : S) {
        if (!result.empty() && abs(c - result.back()) <= 1) {
            result.pop_back();
        } else {
            result += c;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string $S$. This is because we iterate over the string once.
> - **Space Complexity:** $O(n)$, as we store the result string which can be of the same length as the input string.
> - **Why these complexities occur:** the iteration over the string and the storage of the result string cause these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: the same as the brute force approach, as it already has a linear time complexity.
- Detailed breakdown of the approach: same as the brute force approach.
- Proof of optimality: since we must examine each character in the string at least once, a linear time complexity is the best we can achieve.
- Why further optimization is impossible: we cannot avoid examining each character, and the operations performed for each character take constant time.

```cpp
using namespace std;

string removeAlmostEqualCharacters(string S) {
    string result = "";
    for (char c : S) {
        if (!result.empty() && abs(c - result.back()) <= 1) {
            result.pop_back();
        } else {
            result += c;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string $S$.
> - **Space Complexity:** $O(n)$, as we store the result string which can be of the same length as the input string.
> - **Optimality proof:** the linear time complexity is optimal because we must examine each character at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: iteration, conditional statements, and string manipulation.
- Problem-solving patterns identified: the importance of considering edge cases and the use of a result string to build the output.
- Optimization techniques learned: none, as the brute force approach is already optimal.
- Similar problems to practice: other string manipulation problems, such as removing duplicates or finding substrings.

**Mistakes to Avoid:**
- Common implementation errors: not checking for an empty result string before accessing its last character.
- Edge cases to watch for: an empty input string or a string with only one character.
- Performance pitfalls: using inefficient string manipulation operations, such as concatenating strings in a loop.
- Testing considerations: test the function with different input strings, including edge cases and large inputs.