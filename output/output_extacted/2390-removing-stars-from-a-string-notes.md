## Removing Stars From a String
**Problem Link:** https://leetcode.com/problems/removing-stars-from-a-string/description

**Problem Statement:**
- Input: a string `s` containing characters and stars (`*`).
- Constraints: `1 <= s.length <= 10^5`.
- Expected Output: the string after removing all characters that are immediately followed by a star (`*`).
- Key Requirements:
  - Iterate through the string and remove characters followed by a star.
  - Handle edge cases such as consecutive stars, leading or trailing stars, and stars at the end of the string.
- Example Test Cases:
  - Input: `s = "leet**cod*e"`
    - Expected Output: `"leetcode"`
  - Input: `s = "erase*****"`
    - Expected Output: `""`

---

### Brute Force Approach

**Explanation:**
- Initial Thought Process: Iterate through the string and whenever we encounter a star, remove the character preceding it.
- Step-by-Step Breakdown:
  1. Initialize an empty result string.
  2. Iterate through the input string.
  3. If the current character is not a star, append it to the result string.
  4. If the current character is a star and the result string is not empty, remove the last character from the result string.
- Why This Approach Comes to Mind First: It directly follows the problem's requirements without considering any optimizations.

```cpp
#include <string>
using namespace std;

string removeStars(string s) {
    string result = "";
    for (char c : s) {
        if (c != '*') {
            result += c;
        } else if (!result.empty()) {
            result.pop_back();
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we're doing a constant amount of work for each character in the string.
> - **Space Complexity:** $O(n)$, because in the worst case (no stars), we might end up storing all characters in the result string.
> - **Why These Complexities Occur:** The time complexity is linear due to the single pass through the input string. The space complexity is also linear because we're using an additional string to store the result.

---

### Optimal Approach (Required)

**Explanation:**
- Key Insight: The same approach as the brute force is already optimal because it only requires a single pass through the string and uses a stack-like behavior (via the `result` string) to efficiently remove characters when encountering a star.
- Detailed Breakdown: The same steps as the brute force approach apply here because the initial solution was already optimal for this problem.
- Proof of Optimality: Any solution must at least read the input string once, resulting in a time complexity of at least $O(n)$. The given approach achieves this lower bound, making it optimal.

```cpp
#include <string>
using namespace std;

string removeStars(string s) {
    string result = "";
    for (char c : s) {
        if (c != '*') {
            result += c;
        } else if (!result.empty()) {
            result.pop_back();
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we make one pass through the input.
> - **Space Complexity:** $O(n)$, because we store the result in a separate string, which in the worst case could be the size of the input string.
> - **Optimality Proof:** The solution is optimal because it achieves the minimum time complexity required to solve the problem (reading the input once) and uses a minimal amount of extra space to store the result.

---

### Final Notes

**Learning Points:**
- Key Algorithmic Concepts Demonstrated: Single pass through the string, using a string as a stack for efficient character removal.
- Problem-Solving Patterns Identified: Handling edge cases (like stars at the end or consecutive stars) by checking the state of the result string before attempting to remove characters.
- Optimization Techniques Learned: Recognizing when the initial solution is already optimal and understanding the importance of single-pass algorithms for linear time complexity.

**Mistakes to Avoid:**
- Common Implementation Errors: Forgetting to check if the result string is empty before attempting to remove a character, which would lead to runtime errors.
- Edge Cases to Watch For: Stars at the beginning, middle, or end of the string, and consecutive stars.
- Performance Pitfalls: Using inefficient data structures or algorithms that result in higher than necessary time or space complexity.
- Testing Considerations: Thoroughly testing the function with various inputs, including edge cases, to ensure it behaves as expected.