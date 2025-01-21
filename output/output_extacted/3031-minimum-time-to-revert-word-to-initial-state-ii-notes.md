## Minimum Time to Revert Word to Initial State II

**Problem Link:** https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/description

**Problem Statement:**
- Input format and constraints: Given a string `word` consisting of lowercase English letters and an integer `k`, find the minimum time required to revert `word` to its initial state by repeatedly applying the following operation: 
  - Choose a letter `c` and change all occurrences of `c` to `a`.
- Expected output format: Return the minimum time required to revert `word` to its initial state.
- Key requirements and edge cases to consider: 
  - `1 <= k <= 10^5`
  - `1 <= word.length <= 10^5`
  - The string `word` consists of only lowercase English letters.
- Example test cases with explanations: 
  - Input: `word = "aaa", k = 3`
    - Output: `0`
    - Explanation: The word is already in its initial state.
  - Input: `word = "abc", k = 3`
    - Output: `2`
    - Explanation: Change 'b' to 'a' in one operation and change 'c' to 'a' in another operation.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible sequences of operations and calculate the time required for each sequence.
- Step-by-step breakdown of the solution:
  1. Generate all possible sequences of operations.
  2. For each sequence, apply the operations to the word and calculate the time required.
  3. Keep track of the minimum time required among all sequences.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible solutions.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int minTimeToRevertWord(std::string word, int k) {
    int n = word.length();
    int minTime = n;
    // Try all possible sequences of operations
    for (int mask = 0; mask < (1 << 26); mask++) {
        std::string tempWord = word;
        int time = 0;
        // Apply the operations to the word
        for (int i = 0; i < 26; i++) {
            if ((mask & (1 << i)) != 0) {
                for (int j = 0; j < n; j++) {
                    if (tempWord[j] == 'a' + i) {
                        tempWord[j] = 'a';
                    }
                }
                time++;
            }
        }
        // Update the minimum time required
        if (tempWord == std::string(n, 'a')) {
            minTime = std::min(minTime, time);
        }
    }
    return minTime;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{26} \cdot n)$, where $n$ is the length of the word.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the word.
> - **Why these complexities occur:** The brute force approach tries all possible sequences of operations, resulting in an exponential time complexity. The space complexity is linear due to the temporary word used to apply the operations.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The minimum time required to revert the word to its initial state is equal to the number of distinct letters in the word minus one.
- Detailed breakdown of the approach:
  1. Count the frequency of each letter in the word.
  2. Calculate the number of distinct letters in the word.
  3. Return the number of distinct letters minus one as the minimum time required.
- Proof of optimality: The optimal solution is based on the fact that each operation can change all occurrences of a letter to 'a'. Therefore, the minimum time required is equal to the number of distinct letters minus one.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int minTimeToRevertWord(std::string word, int k) {
    int n = word.length();
    std::vector<bool> seen(26, false);
    int distinctLetters = 0;
    // Count the frequency of each letter in the word
    for (int i = 0; i < n; i++) {
        if (!seen[word[i] - 'a']) {
            distinctLetters++;
            seen[word[i] - 'a'] = true;
        }
    }
    // Return the number of distinct letters minus one as the minimum time required
    return distinctLetters - 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the word.
> - **Space Complexity:** $O(1)$, since the space used does not grow with the size of the input.
> - **Optimality proof:** The optimal solution is based on the fact that each operation can change all occurrences of a letter to 'a'. Therefore, the minimum time required is equal to the number of distinct letters minus one.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Counting the frequency of each letter and calculating the number of distinct letters.
- Problem-solving patterns identified: Using a boolean array to keep track of seen letters.
- Optimization techniques learned: Avoiding unnecessary operations by using a simple and efficient approach.
- Similar problems to practice: Other problems involving string manipulation and counting distinct elements.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the boolean array correctly or not updating the count of distinct letters correctly.
- Edge cases to watch for: Handling empty strings or strings with only one distinct letter.
- Performance pitfalls: Using an inefficient approach that has a high time complexity.
- Testing considerations: Testing the function with different inputs, including edge cases and large strings.