## Earliest Second to Mark Indices I
**Problem Link:** https://leetcode.com/problems/earliest-second-to-mark-indices-i/description

**Problem Statement:**
- Input format: You are given a string `s` consisting of lowercase English letters and an integer array `indices` of the same length as `s`.
- Constraints: `1 <= s.length <= 10^5` and `s.length == indices.length`.
- Expected output format: Return the string `s` with each character moved to its corresponding index in `indices`.
- Key requirements and edge cases to consider: Handle overlapping indices correctly, and ensure characters are moved to their correct positions based on the indices provided.

**Example Test Cases:**
- Example 1: Input: `s = "abc", indices = [0,1,2]`, Output: `"abc"`.
- Example 2: Input: `s = "cba", indices = [0,1,2]`, Output: `"cba"`.
- Example 3: Input: `s = "aaa", indices = [2,1,0]`, Output: `"aaa"`.

### Brute Force Approach
**Explanation:**
- Initial thought process: Create a new string and fill it with characters based on the indices provided.
- Step-by-step breakdown of the solution:
  1. Initialize an empty result string with the same length as `s`.
  2. Iterate over `s` and `indices` simultaneously.
  3. For each character and its corresponding index, place the character at the specified index in the result string.
- Why this approach comes to mind first: It's a straightforward, intuitive approach that directly addresses the problem statement.

```cpp
#include <iostream>
#include <string>

using namespace std;

string restoreString(string s, vector<int>& indices) {
    string result(s.length(), ' ');
    for (int i = 0; i < s.length(); i++) {
        result[indices[i]] = s[i];
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of string `s`, because we iterate over `s` and `indices` once.
> - **Space Complexity:** $O(n)$, for the result string.
> - **Why these complexities occur:** The iteration over the input strings and the creation of a new string of the same length dictate these complexities.

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The given brute force approach is already optimal for this problem because it requires a single pass through the input data and uses a minimal amount of extra space to store the result.
- Detailed breakdown of the approach: Same as the brute force approach.
- Proof of optimality: Since we must visit each character and its index at least once to construct the result string, and we do so in a single pass, the time complexity of $O(n)$ is optimal.
- Why further optimization is impossible: Any algorithm must at least read the input, which takes $O(n)$ time, making further optimization in terms of time complexity impossible.

```cpp
// Same as the brute force code, as it is already optimal
string restoreString(string s, vector<int>& indices) {
    string result(s.length(), ' ');
    for (int i = 0; i < s.length(); i++) {
        result[indices[i]] = s[i];
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of string `s`.
> - **Space Complexity:** $O(n)$, for the result string.
> - **Optimality proof:** The algorithm's time complexity matches the lower bound required to read the input, and it uses minimal extra space, making it optimal.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: String manipulation, indexing, and the importance of understanding the problem constraints.
- Problem-solving patterns identified: Recognizing when a brute force approach is actually optimal due to the nature of the problem.
- Optimization techniques learned: Sometimes, the simplest approach is the most efficient, especially when it involves a single pass through the data.
- Similar problems to practice: Other string manipulation problems, such as substring searches or string reversals.

**Mistakes to Avoid:**
- Common implementation errors: Off-by-one errors when indexing, not checking for edge cases like empty strings.
- Edge cases to watch for: Handling strings of length 1, ensuring indices are valid.
- Performance pitfalls: Using inefficient algorithms for string manipulation, such as excessive string concatenation.
- Testing considerations: Thoroughly test with different lengths of strings and various index patterns to ensure correctness.