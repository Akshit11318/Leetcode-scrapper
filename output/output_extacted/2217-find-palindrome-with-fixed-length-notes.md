## Find Palindrome With Fixed Length

**Problem Link:** https://leetcode.com/problems/find-palindrome-with-fixed-length/description

**Problem Statement:**
- Given an integer `n`, return the smallest palindrome with a fixed length of `n`.
- Input: `n` is an integer.
- Expected output: The smallest palindrome with a fixed length of `n`.
- Key requirements and edge cases to consider:
  - `n` is an integer in the range `[1, 9]`.
  - The output should be a palindrome, meaning it reads the same backward as forward.
- Example test cases with explanations:
  - Input: `n = 1`
    - Output: `1`
    - Explanation: The smallest palindrome with a length of `1` is `1`.
  - Input: `n = 2`
    - Output: `11`
    - Explanation: The smallest palindrome with a length of `2` is `11`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the smallest palindrome with a fixed length `n`, we can start by checking all numbers from `1` to `9` (for `n = 1`) or `10` to `99` (for `n = 2`), and so on, until we find a palindrome.
- Step-by-step breakdown of the solution:
  1. Start from the smallest possible number with `n` digits.
  2. Check if the current number is a palindrome by comparing it with its reverse.
  3. If it is a palindrome, return it. Otherwise, increment the number and repeat the process.
- Why this approach comes to mind first: It's a straightforward approach that checks every possible number until it finds a palindrome.

```cpp
class Solution {
public:
    string findPalindrome(int n) {
        int start = pow(10, n - 1); // Start from the smallest n-digit number
        while (true) {
            string str = to_string(start);
            string rev = str;
            reverse(rev.begin(), rev.end());
            if (str == rev) {
                return str;
            }
            start++;
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(10^n)$, where $n$ is the input number. This is because in the worst case, we might have to check all numbers up to $10^n$.
> - **Space Complexity:** $O(n)$, where $n$ is the input number. This is because we need to store the current number as a string.
> - **Why these complexities occur:** The time complexity is high because we're checking every possible number, and the space complexity is due to the conversion of the number to a string for palindrome checking.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: For a number to be a palindrome, its first half must be the reverse of its second half. For the smallest palindrome, we can simply mirror the first half to create the second half.
- Detailed breakdown of the approach:
  1. For `n = 1`, the smallest palindrome is `1`.
  2. For even `n`, the smallest palindrome can be formed by taking the smallest `n/2` digit number and mirroring it.
  3. For odd `n`, the smallest palindrome can be formed by taking the smallest `(n-1)/2` digit number, appending `0`, and then mirroring the first part.
- Proof of optimality: This approach directly constructs the smallest possible palindrome without needing to check every number, making it more efficient.

```cpp
class Solution {
public:
    string findPalindrome(int n) {
        if (n == 1) return "1";
        string firstHalf = to_string(1);
        while (firstHalf.length() < n / 2) {
            firstHalf += "0";
        }
        if (n % 2 == 0) {
            return firstHalf + string(firstHalf.rbegin(), firstHalf.rend());
        } else {
            return firstHalf + "0" + string(firstHalf.rbegin(), firstHalf.rend());
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the input number. This is because we're constructing the palindrome by mirroring the first half.
> - **Space Complexity:** $O(n)$, where $n` is the input number. This is because we need to store the first half of the palindrome and its reverse.
> - **Optimality proof:** This approach is optimal because it directly constructs the smallest palindrome without checking every possible number, resulting in a significant reduction in time complexity compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Palindrome construction, mirroring, and efficient string manipulation.
- Problem-solving patterns identified: Direct construction of the solution instead of brute force checking.
- Optimization techniques learned: Reducing time complexity by avoiding unnecessary checks and using properties of palindromes.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling the case for `n = 1`, not properly mirroring the first half for even and odd `n`.
- Edge cases to watch for: `n = 1` and ensuring the palindrome has exactly `n` digits.
- Performance pitfalls: Using the brute force approach for large `n`, which can lead to very high time complexity.
- Testing considerations: Thoroughly testing with different values of `n`, including edge cases like `n = 1` and larger values to ensure the solution scales well.