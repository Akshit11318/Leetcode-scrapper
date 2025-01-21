## Find Maximum Number of String Pairs
**Problem Link:** https://leetcode.com/problems/find-maximum-number-of-string-pairs/description

**Problem Statement:**
- Input format and constraints: The input is a list of strings where each string has a length of at least 1. The constraint is to find the maximum number of pairs of strings that can be formed such that each pair consists of two strings that are not identical and the concatenation of the two strings is a palindrome.
- Expected output format: The output is the maximum number of pairs of strings that can be formed.
- Key requirements and edge cases to consider: The key requirement is to check for palindrome strings and the edge case is when there are no pairs of strings that can be formed.
- Example test cases with explanations:
  - Example 1: Input: ["abcd","dcba","lls","s","sssll"] Output: 2 Explanation: We can form two pairs: ["abcd", "dcba"] and ["s", "s"].
  - Example 2: Input: ["bat","tab","cat"] Output: 1 Explanation: We can form one pair: ["bat", "tab"].

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial thought process is to generate all possible pairs of strings and check if the concatenation of each pair is a palindrome.
- Step-by-step breakdown of the solution:
  1. Generate all possible pairs of strings.
  2. For each pair, concatenate the two strings.
  3. Check if the concatenated string is a palindrome.
  4. If it is a palindrome, increment the count of pairs.
- Why this approach comes to mind first: This approach comes to mind first because it is a straightforward solution that checks all possible pairs of strings.

```cpp
#include <iostream>
#include <vector>
#include <string>

bool isPalindrome(const std::string& s) {
    int left = 0;
    int right = s.length() - 1;
    while (left < right) {
        if (s[left] != s[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

int maxPairs(std::vector<std::string>& strings) {
    int count = 0;
    for (int i = 0; i < strings.size(); i++) {
        for (int j = i + 1; j < strings.size(); j++) {
            std::string concat = strings[i] + strings[j];
            if (isPalindrome(concat) && strings[i] != strings[j]) {
                count++;
            }
        }
    }
    return count;
}

int main() {
    std::vector<std::string> strings = {"abcd", "dcba", "lls", "s", "sssll"};
    std::cout << maxPairs(strings) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$ where $n$ is the number of strings and $m$ is the maximum length of a string. This is because we are generating all possible pairs of strings and checking if each pair is a palindrome.
> - **Space Complexity:** $O(1)$ because we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** These complexities occur because we are using nested loops to generate all possible pairs of strings and checking if each pair is a palindrome.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a hashmap to store the frequency of each string and its reverse. Then, we can iterate over the hashmap and count the number of pairs that can be formed.
- Detailed breakdown of the approach:
  1. Create a hashmap to store the frequency of each string and its reverse.
  2. Iterate over the hashmap and count the number of pairs that can be formed.
- Proof of optimality: This approach is optimal because we are only iterating over the hashmap once and counting the number of pairs that can be formed.
- Why further optimization is impossible: Further optimization is impossible because we need to iterate over the hashmap at least once to count the number of pairs that can be formed.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

int maxPairs(std::vector<std::string>& strings) {
    std::unordered_map<std::string, int> freq;
    for (const auto& str : strings) {
        std::string rev = str;
        std::reverse(rev.begin(), rev.end());
        if (freq.find(rev) != freq.end()) {
            freq[rev]--;
            if (freq[rev] == 0) {
                freq.erase(rev);
            }
        } else {
            freq[str]++;
        }
    }
    int count = 0;
    for (const auto& pair : freq) {
        count += pair.second / 2;
    }
    return count;
}

int main() {
    std::vector<std::string> strings = {"abcd", "dcba", "lls", "s", "sssll"};
    std::cout << maxPairs(strings) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of strings and $m$ is the maximum length of a string. This is because we are iterating over the hashmap and counting the number of pairs that can be formed.
> - **Space Complexity:** $O(n)$ because we are using a hashmap to store the frequency of each string and its reverse.
> - **Optimality proof:** This approach is optimal because we are only iterating over the hashmap once and counting the number of pairs that can be formed.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The key algorithmic concept demonstrated is the use of a hashmap to store the frequency of each string and its reverse.
- Problem-solving patterns identified: The problem-solving pattern identified is to use a hashmap to count the number of pairs that can be formed.
- Optimization techniques learned: The optimization technique learned is to use a hashmap to reduce the time complexity of the solution.
- Similar problems to practice: Similar problems to practice are problems that involve counting the number of pairs that can be formed from a given set of strings.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to not check if the strings are identical before counting the number of pairs that can be formed.
- Edge cases to watch for: An edge case to watch for is when there are no pairs of strings that can be formed.
- Performance pitfalls: A performance pitfall is to use a nested loop to count the number of pairs that can be formed, which has a high time complexity.
- Testing considerations: A testing consideration is to test the solution with different inputs and edge cases to ensure that it is correct and efficient.