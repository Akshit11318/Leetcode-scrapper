## Next Palindrome Using Same Digits

**Problem Link:** https://leetcode.com/problems/next-palindrome-using-same-digits/description

**Problem Statement:**
- Input: A positive integer `n`.
- Constraints: `1 <= n <= 10^8`.
- Expected output: The next smallest palindrome number greater than `n` using the same digits. If no such palindrome exists, return the next smallest palindrome with the same number of digits.
- Key requirements and edge cases to consider:
  - Handling numbers with leading zeros.
  - Finding the next smallest palindrome with the same number of digits if no palindrome can be formed using the same digits.
- Example test cases with explanations:
  - Input: `n = 1234`, Output: `1331`.
  - Input: `n = 1221`, Output: `1221` because it is already a palindrome.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible palindromes with the same number of digits and check if any of them use the same digits and are greater than the input number.
- Step-by-step breakdown of the solution:
  1. Generate all possible numbers with the same number of digits as the input number.
  2. Check if each generated number is a palindrome and uses the same digits as the input number.
  3. If such a number is found and is greater than the input number, return it.
- Why this approach comes to mind first: It is a straightforward and intuitive approach, but it is inefficient due to the large number of possible numbers to check.

```cpp
#include <iostream>
#include <string>
#include <algorithm>

bool isPalindrome(int n) {
    std::string str = std::to_string(n);
    std::string rev = str;
    std::reverse(rev.begin(), rev.end());
    return str == rev;
}

bool sameDigits(int a, int b) {
    std::string strA = std::to_string(a);
    std::string strB = std::to_string(b);
    std::sort(strA.begin(), strA.end());
    std::sort(strB.begin(), strB.end());
    return strA == strB;
}

int nextPalindrome(int n) {
    while (true) {
        n++;
        if (isPalindrome(n) && sameDigits(n, n)) {
            return n;
        }
    }
}

int main() {
    int n;
    std::cin >> n;
    std::cout << nextPalindrome(n) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(10^k \cdot k)$, where $k$ is the number of digits in the input number, because we generate all possible numbers with $k$ digits and check if each is a palindrome.
> - **Space Complexity:** $O(k)$, because we need to store the input number and the generated numbers.
> - **Why these complexities occur:** The brute force approach requires generating a large number of possible numbers and checking each one, resulting in high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible numbers, we can incrementally build the next palindrome by mirroring the first half of the number.
- Detailed breakdown of the approach:
  1. If the input number is already a palindrome, increment the middle digit (or the second middle digit if the number of digits is even).
  2. If the input number is not a palindrome, increment the first half of the number and mirror it to form a palindrome.
- Proof of optimality: This approach ensures that we find the next smallest palindrome with the same number of digits, if possible, and it does so in the most efficient way by only considering the necessary increments.

```cpp
#include <iostream>
#include <string>
#include <algorithm>

int nextPalindrome(int n) {
    std::string str = std::to_string(n);
    int len = str.length();
    int mid = len / 2;

    if (len % 2 == 0) { // even number of digits
        std::string firstHalf = str.substr(0, mid);
        std::string secondHalf = str.substr(mid, mid);
        std::reverse(firstHalf.begin(), firstHalf.end());

        if (firstHalf <= secondHalf) {
            std::string incrementedFirstHalf = std::to_string(std::stoi(firstHalf) + 1);
            std::reverse(incrementedFirstHalf.begin(), incrementedFirstHalf.end());
            return std::stoi(incrementedFirstHalf + incrementedFirstHalf);
        } else {
            return std::stoi(str.substr(0, mid) + str.substr(0, mid));
        }
    } else { // odd number of digits
        std::string firstHalf = str.substr(0, mid);
        std::string secondHalf = str.substr(mid + 1, mid);
        std::reverse(firstHalf.begin(), firstHalf.end());

        if (str[mid] == '9') {
            if (firstHalf <= secondHalf) {
                std::string incrementedFirstHalf = std::to_string(std::stoi(firstHalf) + 1);
                std::reverse(incrementedFirstHalf.begin(), incrementedFirstHalf.end());
                return std::stoi(incrementedFirstHalf + "0" + incrementedFirstHalf);
            } else {
                return std::stoi(str.substr(0, mid) + str.substr(0, mid));
            }
        } else {
            return std::stoi(str.substr(0, mid) + (char)(str[mid] + 1) + str.substr(0, mid));
        }
    }
}

int main() {
    int n;
    std::cin >> n;
    std::cout << nextPalindrome(n) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k)$, where $k$ is the number of digits in the input number, because we only need to process the input number once.
> - **Space Complexity:** $O(k)$, because we need to store the input number and the generated palindrome.
> - **Optimality proof:** This approach is optimal because it finds the next smallest palindrome with the same number of digits, if possible, and it does so in the most efficient way by only considering the necessary increments.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Incremental building of palindromes, mirroring of numbers.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems (even and odd number of digits), using symmetry to reduce the search space.
- Optimization techniques learned: Avoiding unnecessary computations by only considering the necessary increments.
- Similar problems to practice: Finding the next smallest palindrome with a different number of digits, finding the largest palindrome with the same digits.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect handling of edge cases (e.g., numbers with leading zeros), incorrect implementation of the mirroring step.
- Edge cases to watch for: Numbers with leading zeros, numbers with an odd number of digits.
- Performance pitfalls: Using inefficient algorithms (e.g., generating all possible numbers) instead of incremental building.
- Testing considerations: Testing with different inputs (e.g., numbers with an even and odd number of digits), testing with edge cases.