## Construct String with Minimum Cost

**Problem Link:** https://leetcode.com/problems/construct-string-with-minimum-cost/description

**Problem Statement:**
- Given a string `s` and an integer `cost`, construct a new string with minimum cost by appending the characters of `s` to the new string.
- The cost of appending a character is determined by the number of occurrences of that character in the new string.
- The cost of appending a character is `0` if it does not exist in the new string, `1` if it exists once, and `2` if it exists more than once.
- Return the minimum cost of constructing the new string.

**Input format and constraints:**
- `s`: a string consisting of lowercase letters
- `cost`: an integer representing the cost of constructing the new string
- `1 <= s.length() <= 10^5`
- `1 <= cost <= 10^6`

**Expected output format:**
- An integer representing the minimum cost of constructing the new string

**Key requirements and edge cases to consider:**
- Handle cases where the input string is empty
- Handle cases where the cost is negative
- Handle cases where the input string contains duplicate characters

**Example test cases with explanations:**
- Example 1: `s = "abaac", cost = 0`, expected output: `3`
- Example 2: `s = "abc", cost = 0`, expected output: `0`
- Example 3: `s = "aabaa", cost = 0`, expected output: `7`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through the input string and calculate the cost of appending each character to the new string.
- We can use a frequency map to keep track of the occurrences of each character in the new string.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

int minCost(string s) {
    unordered_map<char, int> freq;
    int cost = 0;
    for (char c : s) {
        if (freq.find(c) == freq.end()) {
            freq[c] = 1;
            cost += 0;
        } else if (freq[c] == 1) {
            freq[c]++;
            cost += 1;
        } else {
            freq[c]++;
            cost += 2;
        }
    }
    return cost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we iterate through the string once.
> - **Space Complexity:** $O(n)$, because we use a frequency map to store the occurrences of each character.
> - **Why these complexities occur:** The time complexity occurs because we iterate through the string once, and the space complexity occurs because we use a frequency map to store the occurrences of each character.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a frequency map to keep track of the occurrences of each character in the new string.
- We can iterate through the input string and calculate the cost of appending each character to the new string.
- This approach is optimal because it has a time complexity of $O(n)$ and a space complexity of $O(n)$.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

int minCost(string s) {
    unordered_map<char, int> freq;
    int cost = 0;
    for (char c : s) {
        freq[c]++;
        cost += (freq[c] - 1);
    }
    return cost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we iterate through the string once.
> - **Space Complexity:** $O(n)$, because we use a frequency map to store the occurrences of each character.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(n)$ and a space complexity of $O(n)$, which is the best possible complexity for this problem.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of a frequency map to keep track of the occurrences of each character in the new string.
- The problem-solving pattern identified is to iterate through the input string and calculate the cost of appending each character to the new string.
- The optimization technique learned is to use a frequency map to reduce the time complexity of the algorithm.

**Mistakes to Avoid:**
- A common implementation error is to forget to initialize the frequency map.
- An edge case to watch for is when the input string is empty.
- A performance pitfall is to use a data structure with a high time complexity, such as a linked list, to store the occurrences of each character.
- A testing consideration is to test the algorithm with different input strings and costs to ensure that it produces the correct output.