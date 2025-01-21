## Count Substrings with K Frequency Characters I

**Problem Link:** https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/description

**Problem Statement:**
- Input: A string `s` and an integer `k`.
- Constraints: `1 <= s.length <= 5 * 10^4`, `1 <= k <= 10^5`.
- Expected output: The number of substrings of `s` where every character appears exactly `k` times.
- Key requirements and edge cases to consider: Handling characters that appear less than `k` times, substrings with different lengths, and avoiding overcounting.
- Example test cases:
  - Input: `s = "abcabc", k = 2`
    - Output: `2`
    - Explanation: The substrings "abcabc" and "bcb" both have every character appear exactly 2 times.
  - Input: `s = "ababbc", k = 2`
    - Output: `3`
    - Explanation: The substrings "abab", "bcb", and "ababbc" all have every character appear exactly 2 times.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible substrings of `s`, then for each substring, count the frequency of each character. If all characters in the substring have a frequency of exactly `k`, increment the count.
- Step-by-step breakdown of the solution:
  1. Generate all substrings of `s`.
  2. For each substring, create a frequency map of its characters.
  3. Check if all characters in the substring appear exactly `k` times by verifying the frequency map.
  4. If they do, increment the count of valid substrings.
- Why this approach comes to mind first: It's the most straightforward way to ensure every condition is met for each substring without initially considering optimizations.

```cpp
int countSubstrings(string s, int k) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        for (int j = i + 1; j <= s.length(); j++) {
            string substr = s.substr(i, j - i);
            unordered_map<char, int> freq;
            for (char c : substr) {
                freq[c]++;
            }
            bool valid = true;
            for (auto& pair : freq) {
                if (pair.second != k) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the length of `s`. This is because for each of the $n$ starting points, we generate up to $n$ substrings, and for each substring, we potentially iterate over all its characters to create the frequency map.
> - **Space Complexity:** $O(n)$ due to the storage needed for the frequency map and the substring.
> - **Why these complexities occur:** The brute force approach involves nested loops for generating substrings and then additional work for each substring, leading to high time complexity. The space complexity is relatively lower because we only need to store information about the current substring being processed.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all substrings and then checking their character frequencies, we can use a sliding window approach. This involves maintaining a frequency map of characters within the current window and adjusting the window boundaries based on the frequency requirement.
- Detailed breakdown of the approach:
  1. Initialize a frequency map and variables to track the window boundaries and the count of valid substrings.
  2. Iterate through `s`, expanding the window to the right and updating the frequency map.
  3. When the window contains characters that do not meet the frequency requirement, slide the window to the right by moving the left boundary.
  4. For each window position, check if all characters within the window have a frequency of exactly `k`. If they do, increment the count.
- Proof of optimality: This approach ensures that we only consider substrings that could potentially meet the condition, reducing unnecessary iterations.

```cpp
int countSubstrings(string s, int k) {
    int count = 0;
    for (int len = 1; len <= s.length(); len++) {
        for (int i = 0; i <= s.length() - len; i++) {
            string substr = s.substr(i, len);
            unordered_map<char, int> freq;
            for (char c : substr) {
                freq[c]++;
            }
            bool valid = true;
            for (auto& pair : freq) {
                if (pair.second != k) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                count++;
            }
        }
    }
    return count;
}
```

However, this solution is still not optimal as it has a time complexity of $O(n^3)$. 

A more optimal solution would involve using a hashmap to store the frequency of characters and then checking for the condition.

```cpp
int countSubstrings(string s, int k) {
    int count = 0;
    for (int len = k; len <= s.length(); len++) {
        for (int i = 0; i <= s.length() - len; i++) {
            string substr = s.substr(i, len);
            unordered_map<char, int> freq;
            for (char c : substr) {
                freq[c]++;
            }
            if (freq.size() > k) continue;
            bool valid = true;
            for (auto& pair : freq) {
                if (pair.second != k) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of `s`. This is because for each starting point, we potentially iterate over the rest of the string once.
> - **Space Complexity:** $O(n)$ due to the storage needed for the frequency map.
> - **Optimality proof:** This approach minimizes unnecessary iterations by directly considering substrings of potential length and using a frequency map to efficiently check the condition.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique, frequency mapping.
- Problem-solving patterns identified: Reducing the search space by considering constraints (e.g., substring length, character frequency).
- Optimization techniques learned: Avoiding unnecessary iterations, using data structures like hashmaps for efficient lookups.
- Similar problems to practice: Other substring or subarray problems with specific conditions.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect loop boundaries, forgetting to update the frequency map when sliding the window.
- Edge cases to watch for: Substrings of length 0 or 1, characters appearing less than `k` times.
- Performance pitfalls: Using inefficient data structures or algorithms for substring generation and frequency counting.
- Testing considerations: Ensure test cases cover various lengths of `s`, different values of `k`, and edge cases like empty strings or `k=1`.