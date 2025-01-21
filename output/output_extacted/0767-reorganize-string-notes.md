## Reorganize String
**Problem Link:** https://leetcode.com/problems/reorganize-string/description

**Problem Statement:**
- Input: A string `s` containing lowercase English letters.
- Constraints: $1 \leq s.length \leq 10^5$.
- Expected Output: A string where no two adjacent characters are the same. If it is impossible to reorganize the string, return an empty string.
- Key Requirements: The output string should have the same characters as the input string, and no two adjacent characters should be the same.
- Edge Cases: If a character appears more than $(length(s) + 1) / 2$ times, it is impossible to reorganize the string.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible permutations of the input string and check if any of them satisfy the condition that no two adjacent characters are the same.
- Step-by-step breakdown:
  1. Generate all permutations of the input string.
  2. For each permutation, check if any two adjacent characters are the same.
  3. If a permutation is found that satisfies the condition, return it.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible solutions.

```cpp
#include <algorithm>
#include <string>

string reorganizeString(string s) {
    do {
        bool valid = true;
        for (int i = 0; i < s.size() - 1; i++) {
            if (s[i] == s[i + 1]) {
                valid = false;
                break;
            }
        }
        if (valid) return s;
    } while (std::next_permutation(s.begin(), s.end()));
    return "";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n)$ where $n$ is the length of the input string. This is because we are generating all permutations of the input string, which takes $O(n!)$ time, and for each permutation, we are checking if any two adjacent characters are the same, which takes $O(n)$ time.
> - **Space Complexity:** $O(n)$ where $n$ is the length of the input string. This is because we are storing the input string and its permutations.
> - **Why these complexities occur:** The time complexity is high because we are generating all permutations of the input string, and the space complexity is moderate because we are storing the input string and its permutations.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Use a priority queue to store the characters and their frequencies. The character with the highest frequency should be popped first and appended to the result string.
- Detailed breakdown:
  1. Count the frequency of each character in the input string.
  2. Create a priority queue to store the characters and their frequencies.
  3. While the priority queue is not empty, pop the character with the highest frequency and append it to the result string.
  4. If the last character in the result string is the same as the popped character, append the popped character to a temporary string and append the last character of the temporary string to the result string.
- Proof of optimality: This approach is optimal because it ensures that the character with the highest frequency is always appended to the result string first, which minimizes the chances of two adjacent characters being the same.

```cpp
#include <queue>
#include <unordered_map>
#include <string>

struct Node {
    char c;
    int freq;
    bool operator<(const Node& other) const {
        return freq < other.freq;
    }
};

string reorganizeString(string s) {
    unordered_map<char, int> freq;
    for (char c : s) {
        freq[c]++;
    }
    
    priority_queue<Node> pq;
    for (auto& pair : freq) {
        pq.push({pair.first, pair.second});
    }
    
    string res;
    while (!pq.empty()) {
        Node node1 = pq.top();
        pq.pop();
        if (!res.empty() && res.back() == node1.c) {
            if (pq.empty()) return "";
            Node node2 = pq.top();
            pq.pop();
            res += node2.c;
            if (--node2.freq > 0) {
                pq.push(node2);
            }
            pq.push(node1);
        } else {
            res += node1.c;
            if (--node1.freq > 0) {
                pq.push(node1);
            }
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ where $n$ is the length of the input string. This is because we are using a priority queue to store the characters and their frequencies, and each insertion and deletion operation takes $O(\log n)$ time.
> - **Space Complexity:** $O(n)$ where $n$ is the length of the input string. This is because we are storing the input string and its characters and frequencies.
> - **Optimality proof:** This approach is optimal because it ensures that the character with the highest frequency is always appended to the result string first, which minimizes the chances of two adjacent characters being the same.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queues, frequency counting, and string manipulation.
- Problem-solving patterns identified: Using priority queues to solve problems that require maximizing or minimizing some quantity.
- Optimization techniques learned: Using priority queues to optimize the solution by minimizing the chances of two adjacent characters being the same.
- Similar problems to practice: Other problems that involve string manipulation and frequency counting, such as finding the most frequent character in a string.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as when the input string is empty or has only one character.
- Edge cases to watch for: When the input string has a character that appears more than $(length(s) + 1) / 2$ times.
- Performance pitfalls: Using a brute force approach that generates all permutations of the input string.
- Testing considerations: Testing the solution with different input strings, including edge cases, to ensure that it works correctly.