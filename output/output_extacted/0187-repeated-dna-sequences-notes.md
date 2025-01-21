## Repeated DNA Sequences

**Problem Link:** https://leetcode.com/problems/repeated-dna-sequences/description

**Problem Statement:**
- Input format: A string `s` consisting of only the characters `'A'`, `'C'`, `'G'`, and `'T'`.
- Constraints: `0 <= s.length <= 10^5`.
- Expected output format: A list of all unique `10`-letter sequences (substrings) that occur more than once in `s`.
- Key requirements and edge cases to consider:
  - Handling empty strings.
  - Dealing with strings of length less than `10`.
  - Identifying repeated sequences efficiently.
- Example test cases with explanations:
  - Input: `"AAAAACCCCCAAAAACCCCCC"`.
    Output: `["AAAAACCCCC", "CCCCCAAAAA"]`.
  - Input: `"ATCGATCGATCG"`.
    Output: `["ATCGATCGATCG"]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the string and extract every `10`-letter sequence. Store these sequences in a data structure and count their occurrences.
- Step-by-step breakdown of the solution:
  1. Initialize an empty map (or dictionary) to store sequences as keys and their counts as values.
  2. Iterate through the input string `s` with a sliding window of size `10`.
  3. For each window, extract the `10`-letter sequence and check if it's already in the map. If it is, increment its count; otherwise, add it to the map with a count of `1`.
  4. After iterating through the entire string, filter the map for sequences with counts greater than `1`.
- Why this approach comes to mind first: It directly addresses the problem statement by checking every possible sequence.

```cpp
#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>

vector<string> findRepeatedDnaSequences(string s) {
    unordered_map<string, int> seqCount;
    vector<string> repeatedSeqs;
    
    // Edge case handling: strings shorter than 10 characters
    if (s.length() < 10) {
        return repeatedSeqs;
    }
    
    for (int i = 0; i <= s.length() - 10; ++i) {
        string seq = s.substr(i, 10);
        if (seqCount.find(seq) != seqCount.end()) {
            seqCount[seq]++;
        } else {
            seqCount[seq] = 1;
        }
    }
    
    for (auto& pair : seqCount) {
        if (pair.second > 1) {
            repeatedSeqs.push_back(pair.first);
        }
    }
    
    return repeatedSeqs;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of the string and $m$ is the length of the sequence (in this case, `10`). The reason is that we're potentially iterating through the entire string and for each position, we might be doing some constant amount of work to extract the sequence and update its count.
> - **Space Complexity:** $O(n)$, because in the worst case, we might end up storing every sequence in the map. This happens when all sequences are unique.
> - **Why these complexities occur:** The time complexity is linear with respect to the string length because we're using a sliding window approach that checks every sequence once. The space complexity is also linear because we're storing each unique sequence in the map.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilize a `HashSet` (or `unordered_set` in C++) to keep track of sequences we've seen and another set for sequences we've seen more than once. This allows for constant time complexity when checking if a sequence has been seen before.
- Detailed breakdown of the approach:
  1. Initialize two sets: one for all unique sequences seen (`seen`) and another for sequences seen more than once (`repeated`).
  2. Iterate through the string with a sliding window of size `10`.
  3. For each window, check if the sequence is in the `seen` set. If it is and it's not in the `repeated` set, add it to the `repeated` set. If it's not in the `seen` set, add it to the `seen` set.
- Proof of optimality: This approach ensures that we only store sequences that are necessary (either because they've been seen once or more than once), and we only iterate through the string once, resulting in linear time complexity.

```cpp
#include <iostream>
#include <unordered_set>
#include <vector>
#include <string>

vector<string> findRepeatedDnaSequences(string s) {
    unordered_set<string> seen, repeated;
    vector<string> repeatedSeqs;
    
    if (s.length() < 10) {
        return repeatedSeqs;
    }
    
    for (int i = 0; i <= s.length() - 10; ++i) {
        string seq = s.substr(i, 10);
        if (seen.find(seq) != seen.end()) {
            if (repeated.find(seq) == repeated.end()) {
                repeatedSeqs.push_back(seq);
            }
        } else {
            seen.insert(seq);
        }
    }
    
    return repeatedSeqs;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of the string and $m` is the length of the sequence (`10` in this case). However, the constant factor is improved because we're doing constant time lookups in the sets.
> - **Space Complexity:** $O(n)$, because we're storing unique sequences in the `seen` and `repeated` sets.
> - **Optimality proof:** This is optimal because we're only iterating through the string once and using constant time operations for set lookups and insertions, resulting in the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique, use of hash sets for efficient lookups and storage.
- Problem-solving patterns identified: Breaking down the problem into manageable parts (e.g., handling edge cases, iterating through the string).
- Optimization techniques learned: Using sets for efficient storage and lookup of unique elements.
- Similar problems to practice: Other string manipulation and pattern recognition problems.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases properly (e.g., strings shorter than `10` characters).
- Edge cases to watch for: Empty strings, strings with only unique sequences, strings with sequences that are exactly `10` characters long.
- Performance pitfalls: Using data structures with inefficient lookup or insertion times (e.g., lists instead of sets).
- Testing considerations: Ensure to test with various input sizes and types (e.g., strings with many repeated sequences, strings with no repeated sequences).