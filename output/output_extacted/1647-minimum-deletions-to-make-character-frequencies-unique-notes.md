## Minimum Deletions to Make Character Frequencies Unique
**Problem Link:** https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/description

**Problem Statement:**
- Input format and constraints: Given a string `s`, find the minimum number of deletions to make character frequencies unique.
- Expected output format: The minimum number of deletions required.
- Key requirements and edge cases to consider:
  - The input string `s` can contain any lowercase English letters.
  - The frequency of each character in `s` should be unique after deletions.
- Example test cases with explanations:
  - For `s = "aab"`, the minimum number of deletions is `1` to make `a` appear once and `b` appear once.
  - For `s = "abc"`, the minimum number of deletions is `0` since all characters already have unique frequencies.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate all possible subsets of the string and calculate the frequency of each character in each subset.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsets of the string.
  2. For each subset, calculate the frequency of each character.
  3. Check if the frequencies are unique.
  4. If unique, calculate the number of deletions made to reach this subset.
  5. Keep track of the minimum number of deletions that result in unique frequencies.
- Why this approach comes to mind first: It's a straightforward approach that checks all possibilities but is inefficient due to its exponential time complexity.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>

int minDeletionsBruteForce(std::string s) {
    int n = s.length();
    int minDeletions = INT_MAX;

    // Generate all possible subsets
    for (int mask = 0; mask < (1 << n); ++mask) {
        std::unordered_map<char, int> freq;
        int deletions = 0;

        // Calculate frequency of each character in the subset
        for (int i = 0; i < n; ++i) {
            if ((mask & (1 << i)) == 0) {
                // Character is deleted
                deletions++;
            } else {
                // Character is included
                freq[s[i]]++;
            }
        }

        // Check if frequencies are unique
        std::unordered_map<int, int> freqFreq;
        bool unique = true;
        for (auto& pair : freq) {
            if (freqFreq.find(pair.second) != freqFreq.end()) {
                unique = false;
                break;
            }
            freqFreq[pair.second] = 1;
        }

        if (unique && deletions < minDeletions) {
            minDeletions = deletions;
        }
    }

    return minDeletions;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string. This is because we generate all possible subsets of the string and for each subset, we calculate the frequency of each character.
> - **Space Complexity:** $O(n)$, for storing the frequency of each character in the subset.
> - **Why these complexities occur:** The brute force approach is inefficient because it generates all possible subsets of the string, leading to an exponential time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all subsets, we can sort the frequencies of characters and then try to make each frequency unique by reducing it if necessary.
- Detailed breakdown of the approach:
  1. Calculate the frequency of each character in the string.
  2. Sort the frequencies in descending order.
  3. Iterate through the sorted frequencies and for each frequency, check if it's greater than the previous unique frequency.
  4. If it is, reduce the frequency until it's less than the previous unique frequency and count the reductions as deletions.
- Proof of optimality: This approach is optimal because it directly addresses the requirement of making each character's frequency unique with the minimum number of deletions. It does so by prioritizing the reduction of higher frequencies first, which minimizes the overall number of deletions needed.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
#include <algorithm>

int minDeletionsOptimal(std::string s) {
    std::unordered_map<char, int> freq;
    for (char c : s) {
        freq[c]++;
    }

    std::vector<int> freqs;
    for (auto& pair : freq) {
        freqs.push_back(pair.second);
    }

    std::sort(freqs.rbegin(), freqs.rend());

    int deletions = 0;
    int lastFreq = INT_MAX;

    for (int i = 0; i < freqs.size(); ++i) {
        while (freqs[i] >= lastFreq && freqs[i] > 0) {
            freqs[i]--;
            deletions++;
        }
        lastFreq = freqs[i];
    }

    return deletions;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of unique characters in the string. This is because we sort the frequencies of characters.
> - **Space Complexity:** $O(n)$, for storing the frequency of each character.
> - **Optimality proof:** This approach is optimal because it directly addresses the requirement with the minimum number of operations necessary, avoiding unnecessary deletions by prioritizing the reduction of higher frequencies first.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Frequency calculation, sorting, and iterative reduction.
- Problem-solving patterns identified: Directly addressing the problem's constraints and requirements.
- Optimization techniques learned: Prioritizing reductions based on higher frequencies first.
- Similar problems to practice: Problems involving frequency calculations and optimizations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect frequency calculations or sorting.
- Edge cases to watch for: Handling strings with no characters or strings with all unique characters.
- Performance pitfalls: Using inefficient sorting algorithms or not optimizing the reduction process.
- Testing considerations: Thoroughly testing with various input strings, including edge cases.