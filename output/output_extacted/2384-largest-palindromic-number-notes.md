## Largest Palindromic Number
**Problem Link:** [https://leetcode.com/problems/largest-palindromic-number/description](https://leetcode.com/problems/largest-palindromic-number/description)

**Problem Statement:**
- Input format: A string `num` representing a non-negative integer.
- Constraints: $1 \leq \text{length of } num \leq 10^5$
- Expected output format: The largest palindromic number that can be obtained by rearranging the digits of `num`.
- Key requirements: The output must be a palindrome and must be the largest possible.
- Example test cases:
  - Input: `"321"` Output: `"323"`
  - Input: `"444947137"` Output: `"7449447"`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible permutations of the digits in `num`, then check each permutation to see if it's a palindrome. If it is, compare it to the current maximum palindrome found.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the digits in `num`.
  2. For each permutation, check if it's a palindrome.
  3. If a permutation is a palindrome, convert it to an integer and compare it with the current maximum palindrome.
  4. Update the maximum palindrome if the current one is larger.
- Why this approach comes to mind first: It's a straightforward, exhaustive search approach that guarantees finding the largest palindromic number but is inefficient due to the high number of permutations.

```cpp
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

// Function to check if a string is a palindrome
bool isPalindrome(const string& str) {
    int left = 0, right = str.length() - 1;
    while (left < right) {
        if (str[left] != str[right]) return false;
        left++, right--;
    }
    return true;
}

string largestPalindromicNumber(string num) {
    // Generate all permutations
    sort(num.begin(), num.end());
    string maxPalindrome = "";
    do {
        // Check if permutation is a palindrome
        if (isPalindrome(num)) {
            // Update maxPalindrome if necessary
            if (num > maxPalindrome) maxPalindrome = num;
        }
    } while (next_permutation(num.begin(), num.end()));
    return maxPalindrome;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$ due to generating all permutations of `n` digits, where $n$ is the length of `num`.
> - **Space Complexity:** $O(n)$ for storing the permutations and the current maximum palindrome.
> - **Why these complexities occur:** The brute force approach involves generating all permutations, which leads to a factorial time complexity. The space complexity is linear due to the need to store the current permutation and the maximum palindrome found so far.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of generating all permutations, we can count the frequency of each digit in `num` and then construct the largest palindrome by placing the largest digits in the first half of the palindrome and mirroring them in the second half. If there's a digit with an odd count, it can be placed in the middle of the palindrome.
- Detailed breakdown of the approach:
  1. Count the frequency of each digit in `num`.
  2. Sort the digits in descending order based on their frequency and value.
  3. Construct the first half of the palindrome by placing the largest digits first.
  4. Mirror the first half to construct the second half, except for the middle digit if the length of the palindrome is odd.
- Proof of optimality: This approach guarantees finding the largest palindromic number because it prioritizes the largest digits and constructs the palindrome in a way that maximizes its value.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string largestPalindromicNumber(string num) {
    vector<int> count(10, 0); // Count frequency of each digit
    for (char c : num) count[c - '0']++;
    
    string firstHalf = ""; // First half of the palindrome
    string mid = ""; // Middle digit if the length is odd
    
    for (int i = 9; i >= 0; --i) {
        // Add the largest possible digits to the first half
        for (int j = 0; j < count[i] / 2; ++j) {
            firstHalf += to_string(i);
        }
        // If a digit has an odd count, it can be the middle digit
        if (count[i] % 2 == 1 && mid.empty()) {
            mid = to_string(i);
        }
    }
    
    // Construct the palindrome
    string palindrome = firstHalf + mid + string(firstHalf.rbegin(), firstHalf.rend());
    return palindrome;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + 10 \log 10)$, where $n$ is the length of `num`. The dominant operation is counting the frequency of digits and constructing the palindrome.
> - **Space Complexity:** $O(n)$ for storing the frequency count and the palindrome.
> - **Optimality proof:** This approach is optimal because it directly constructs the largest possible palindrome without unnecessary iterations or comparisons, ensuring a linear time complexity.

---

### Final Notes

**Learning Points:**
- **Digit frequency counting:** Useful for problems involving constructing numbers or strings with specific properties.
- **Palindrome construction:** Understanding how to construct palindromes from given digits or characters.
- **Optimization techniques:** Avoiding brute force by directly constructing the optimal solution based on the problem's constraints.

**Mistakes to Avoid:**
- **Not considering all digits:** Failing to account for all digits when constructing the palindrome.
- **Incorrect handling of odd counts:** Not properly placing digits with odd counts in the middle of the palindrome.
- **Inefficient algorithms:** Using brute force or inefficient algorithms that lead to high time complexities.