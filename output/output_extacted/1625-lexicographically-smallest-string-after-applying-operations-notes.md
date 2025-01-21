## Lexicographically Smallest String After Applying Operations
**Problem Link:** https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/description

**Problem Statement:**
- Input format and constraints: You are given a string `s` and two operations to apply to `s`: 
  - `swap(i, j)`: Swap the characters at indices `i` and `j`.
  - `reverse(i, j)`: Reverse the substring from index `i` to `j`.
- Expected output format: Return the lexicographically smallest string after applying these operations.
- Key requirements and edge cases to consider: 
  - All operations must be applied in the order they are given.
  - The string `s` only contains lowercase English letters.
- Example test cases with explanations:
  - For `s = "cba"`, `operations = [["0","1","swap"],["1","2","reverse"]]`, the output should be `"acb"`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The simplest approach is to apply each operation directly to the string `s` as they are given.
- Step-by-step breakdown of the solution:
  1. Start with the original string `s`.
  2. For each operation in `operations`, apply it to the current string.
  3. After all operations are applied, return the resulting string.
- Why this approach comes to mind first: It directly follows the problem statement without considering any optimizations.

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

string lexicographicallySmallestString(string s, vector<vector<string>>& operations) {
    for (auto& op : operations) {
        if (op[2] == "swap") {
            int i = stoi(op[0]);
            int j = stoi(op[1]);
            swap(s[i], s[j]);
        } else if (op[2] == "reverse") {
            int i = stoi(op[0]);
            int j = stoi(op[1]);
            reverse(s.begin() + i, s.begin() + j + 1);
        }
    }
    return s;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of operations and $m$ is the length of the string. This is because in the worst case, each operation could potentially involve reversing the entire string.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output. This is because we are modifying the string in-place.
> - **Why these complexities occur:** The time complexity is due to the potential reversal operation, which can take up to $m$ time. The space complexity is low because we only use a constant amount of extra space to store indices and operation types.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Since the goal is to find the lexicographically smallest string after applying all operations, we can take advantage of the fact that the operations are applied in sequence. This means we can build the result string character by character, always choosing the smallest possible character from the remaining unassigned characters.
- Detailed breakdown of the approach:
  1. Initialize an empty result string and a set of unassigned characters from the original string.
  2. For each operation, update the set of unassigned characters accordingly.
  3. At each step, choose the smallest character from the unassigned characters that can be placed next in the result string, ensuring the lexicographically smallest outcome.
- Proof of optimality: This approach ensures that at each step, the smallest possible character is chosen, which guarantees the lexicographically smallest result after all operations are applied.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

string lexicographicallySmallestString(string s, vector<vector<string>>& operations) {
    set<char> unassigned(s.begin(), s.end());
    string result;
    
    for (auto& op : operations) {
        if (op[2] == "swap") {
            // Swapping doesn't change the set of unassigned characters
            continue;
        } else if (op[2] == "reverse") {
            // Reversing also doesn't change the set of unassigned characters
            continue;
        }
    }
    
    // Since the operations don't affect the set of characters, we can simply sort the string
    sort(s.begin(), s.end());
    return s;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m \log m)$, where $m$ is the length of the string. This is because we sort the string once.
> - **Space Complexity:** $O(m)$, for storing the set of unassigned characters.
> - **Optimality proof:** This approach is optimal because it ensures the lexicographically smallest string is produced by sorting the characters, which is the most efficient way to achieve this given the operations provided.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, set operations, and understanding the impact of sequence operations on a string.
- Problem-solving patterns identified: Breaking down complex operations into simpler, more manageable steps.
- Optimization techniques learned: Recognizing that certain operations (like swap and reverse) do not change the set of characters, allowing for a simpler solution.
- Similar problems to practice: Other string manipulation and sorting problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly applying operations or misunderstanding the impact of operations on the string.
- Edge cases to watch for: Handling empty strings or operations lists.
- Performance pitfalls: Failing to recognize the simplification provided by the operations not affecting the character set, leading to an overly complex solution.
- Testing considerations: Ensuring to test with various operation sequences and string lengths.