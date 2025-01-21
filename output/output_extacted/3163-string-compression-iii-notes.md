## String Compression III
**Problem Link:** [https://leetcode.com/problems/string-compression-iii/description](https://leetcode.com/problems/string-compression-iii/description)

**Problem Statement:**
- Input: `s` - a string, and `k` - an integer.
- Constraints: `1 <= s.length <= 200`, `1 <= k <= 100`.
- Expected Output: The length of the compressed string after applying the operations `append`, `appendcount`, and `frequence` to `s`, with the goal of minimizing the length of the compressed string.
- Key Requirements: 
  - Understand the operations `append`, `appendcount`, and `frequence` and how they affect the string.
  - Determine the optimal sequence of operations to minimize the compressed string length.
- Example Test Cases:
  - `s = "abc", k = 2` should return `4` because we can use `append` to add 'a', 'b', and 'c', and then use `appendcount` to add the count of each character, resulting in a string of length `4`.
  - `s = "aabba", k = 2` should return `5` because we can use `append` to add 'a', 'a', 'b', 'b', and 'a', and then use `appendcount` to add the count of each character, resulting in a string of length `5`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to try all possible combinations of operations (`append`, `appendcount`, and `frequence`) and keep track of the minimum length achieved.
- This approach involves generating all permutations of operations and evaluating each permutation's impact on the string length.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int bruteForce(string s, int k) {
    int n = s.length();
    int minLen = n; // Initialize minimum length as the original string length
    // Generate all permutations of operations
    for (int mask = 0; mask < (1 << n); mask++) {
        string compressed = "";
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) { // If bit is set, use appendcount
                int count = 1;
                while (i + 1 < n && s[i] == s[i + 1]) {
                    i++;
                    count++;
                }
                compressed += s[i];
                compressed += to_string(count);
            } else { // Otherwise, use append
                compressed += s[i];
            }
        }
        minLen = min(minLen, (int)compressed.length());
    }
    return minLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string. This is because we generate all permutations of operations (which is $2^n$) and for each permutation, we potentially iterate through the string.
> - **Space Complexity:** $O(n)$, as we need to store the compressed string for each permutation.
> - **Why these complexities occur:** The brute force approach involves trying all possible combinations of operations, leading to exponential time complexity. The space complexity is linear due to the need to store the compressed string.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to realize that the optimal solution involves using `appendcount` whenever possible to reduce the length of the compressed string.
- We can achieve this by maintaining a count of consecutive characters and using `appendcount` when the count is greater than 1.

```cpp
int optimalSolution(string s, int k) {
    int n = s.length();
    int minLen = 0;
    int count = 1;
    for (int i = 1; i <= n; i++) {
        if (i == n || s[i] != s[i - 1]) {
            minLen += 1 + (count > 1 ? to_string(count).length() : 0);
            count = 1;
        } else {
            count++;
        }
    }
    return minLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string. This is because we make a single pass through the string.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count and minimum length.
> - **Optimality proof:** This solution is optimal because it uses `appendcount` whenever possible to reduce the length of the compressed string, and it does so in a way that minimizes the number of operations required.

---

### Final Notes

**Learning Points:**
- The importance of understanding the operations and their impact on the string length.
- The need to consider all possible combinations of operations in the brute force approach.
- The key insight that leads to the optimal solution: using `appendcount` whenever possible to reduce the length of the compressed string.

**Mistakes to Avoid:**
- Not considering all possible combinations of operations in the brute force approach.
- Not using `appendcount` whenever possible in the optimal solution.
- Not maintaining a count of consecutive characters in the optimal solution.