## Maximum Number of Balloons
**Problem Link:** https://leetcode.com/problems/maximum-number-of-balloons/description

**Problem Statement:**
- Input format: A string `text` containing only lowercase letters.
- Constraints: $1 \leq \text{length of } text \leq 10^4$.
- Expected output format: The maximum number of times the string "balloon" can be formed from the letters in `text`.
- Key requirements: Count the occurrences of each character in `text` and determine the maximum number of times "balloon" can be formed.
- Edge cases: Handle cases where `text` is empty or does not contain enough characters to form "balloon".
- Example test cases:
  - Input: `text = "loonbalxballpoon"`; Output: `2`
  - Input: `text = "nlaebolko"`; Output: `1`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Count the occurrences of each character in `text` and then calculate how many times "balloon" can be formed.
- Step-by-step breakdown:
  1. Initialize a frequency map to store the count of each character in `text`.
  2. Iterate over `text` to populate the frequency map.
  3. Calculate the maximum number of times "balloon" can be formed based on the frequency map.
- Why this approach comes to mind first: It directly addresses the problem by counting the necessary characters and then determining the maximum formations.

```cpp
#include <iostream>
#include <unordered_map>
using namespace std;

int maxNumberOfBalloons(string text) {
    unordered_map<char, int> freqMap;
    for (char c : text) {
        freqMap[c]++;
    }

    int bCount = freqMap['b'];
    int aCount = freqMap['a'];
    int lCount = freqMap['l'] / 2;
    int oCount = freqMap['o'] / 2;
    int nCount = freqMap['n'];

    return min({bCount, aCount, lCount, oCount, nCount});
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `text`, because we iterate over `text` once to populate the frequency map.
> - **Space Complexity:** $O(1)$, because the size of the frequency map is constant (it only stores counts for the characters in "balloon").
> - **Why these complexities occur:** The time complexity is linear due to the single pass over `text`, and the space complexity is constant because the frequency map has a fixed size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: The same as the brute force approach, but we recognize that the solution can be optimized by directly counting the characters needed for "balloon" without storing all character frequencies.
- Detailed breakdown:
  1. Initialize counters for 'b', 'a', 'l', 'o', and 'n'.
  2. Iterate over `text` and increment the corresponding counter for each character.
  3. Calculate the maximum number of times "balloon" can be formed based on the counters.
- Proof of optimality: This approach is optimal because it directly counts the necessary characters in a single pass, minimizing both time and space complexity.

```cpp
int maxNumberOfBalloons(string text) {
    int b = 0, a = 0, l = 0, o = 0, n = 0;
    for (char c : text) {
        if (c == 'b') b++;
        else if (c == 'a') a++;
        else if (c == 'l') l++;
        else if (c == 'o') o++;
        else if (c == 'n') n++;
    }

    return min({b, a, l / 2, o / 2, n});
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `text`, because we make a single pass over `text`.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the counters.
> - **Optimality proof:** This solution is optimal because it achieves the minimum time complexity ($O(n)$) necessary to examine each character in `text` at least once and uses the minimum space complexity ($O(1)$) by only storing the necessary counters.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Frequency counting, minimum value calculation.
- Problem-solving patterns: Directly addressing the problem by counting necessary elements.
- Optimization techniques: Minimizing space usage by only storing necessary information.
- Similar problems to practice: Other string manipulation and frequency counting problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases (e.g., empty string).
- Edge cases to watch for: Handling cases where `text` does not contain enough characters to form "balloon".
- Performance pitfalls: Using more complex data structures than necessary, leading to increased space or time complexity.
- Testing considerations: Ensure to test with various inputs, including edge cases like an empty string or a string without any of the characters in "balloon".