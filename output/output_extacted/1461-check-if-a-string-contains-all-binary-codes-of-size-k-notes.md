## Check if a String Contains All Binary Codes of Size K

**Problem Link:** https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description

**Problem Statement:**
- Input: A string `s` and an integer `k`.
- Constraints: `1 <= k <= 20`, `1 <= s.length <= 5 * 10^5`.
- Expected output: Return `true` if `s` contains all binary codes of size `k`, otherwise return `false`.
- Key requirements and edge cases to consider:
  - The string `s` only contains `0`s and `1`s.
  - A binary code of size `k` is a substring of `s` with length `k`.
- Example test cases with explanations:
  - For `s = "00110"` and `k = 2`, the binary codes of size `k` are `"00"`, `"01"`, `"10"`, and `"11"`. Since `s` contains all these codes, the output is `true`.
  - For `s = "0110"` and `k = 1`, the binary codes of size `k` are `"0"` and `"1"`. Since `s` contains both codes, the output is `true`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible binary codes of size `k` and check if each code exists in the string `s`.
- Step-by-step breakdown of the solution:
  1. Generate all possible binary codes of size `k`.
  2. Iterate through the string `s` and check if each code exists in `s`.
  3. If any code does not exist, return `false`.
- Why this approach comes to mind first: It is a straightforward and intuitive approach that involves generating all possible codes and checking their existence in the string.

```cpp
#include <iostream>
#include <string>
#include <set>

bool hasAllCodes(std::string s, int k) {
    int n = s.length();
    std::set<std::string> codes;

    // Generate all possible binary codes of size k
    for (int i = 0; i <= n - k; i++) {
        std::string code = s.substr(i, k);
        codes.insert(code);
    }

    // Check if all possible codes exist
    for (int i = 0; i < (1 << k); i++) {
        std::string code;
        for (int j = 0; j < k; j++) {
            code += ((i >> (k - 1 - j)) & 1) ? '1' : '0';
        }
        if (codes.find(code) == codes.end()) {
            return false;
        }
    }

    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^k \cdot k + n - k + 1)$, where $n$ is the length of the string `s`. The first term comes from generating all possible codes, and the second term comes from iterating through the string.
> - **Space Complexity:** $O(2^k \cdot k)$, where $k$ is the size of the binary codes. This is because we store all possible codes in a set.
> - **Why these complexities occur:** The time complexity occurs because we generate all possible codes and check their existence in the string. The space complexity occurs because we store all possible codes in a set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible codes, we can use a sliding window approach to check if all codes exist in the string.
- Detailed breakdown of the approach:
  1. Initialize a set to store unique codes.
  2. Iterate through the string using a sliding window of size `k`.
  3. For each window, extract the code and add it to the set.
  4. If the size of the set is equal to $2^k$, return `true`.
- Proof of optimality: This approach is optimal because it only requires a single pass through the string and uses a set to store unique codes.

```cpp
#include <iostream>
#include <string>
#include <set>

bool hasAllCodes(std::string s, int k) {
    int n = s.length();
    std::set<std::string> codes;

    for (int i = 0; i <= n - k; i++) {
        std::string code = s.substr(i, k);
        codes.insert(code);
    }

    return codes.size() == (1 << k);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n - k + 1)$, where $n$ is the length of the string `s`. This is because we iterate through the string using a sliding window.
> - **Space Complexity:** $O(2^k \cdot k)$, where $k$ is the size of the binary codes. This is because we store unique codes in a set.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the string and uses a set to store unique codes.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, set data structure.
- Problem-solving patterns identified: Using a set to store unique codes, iterating through a string using a sliding window.
- Optimization techniques learned: Avoiding unnecessary code generation, using a set to store unique codes.
- Similar problems to practice: Problems involving strings, sets, and sliding windows.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, not initializing variables.
- Edge cases to watch for: Empty strings, strings with only one character, strings with repeating characters.
- Performance pitfalls: Using inefficient algorithms, not optimizing code.
- Testing considerations: Testing with different inputs, testing with edge cases.
