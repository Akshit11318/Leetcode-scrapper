## Maximum Number of Occurrences of a Substring

**Problem Link:** https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/description

**Problem Statement:**
- Input format and constraints: Given a string `s`, an integer `k`, and a set of characters `letters`, find the maximum number of occurrences of a substring with `k` characters from `letters`.
- Expected output format: The maximum number of occurrences of a substring with `k` characters from `letters`.
- Key requirements and edge cases to consider: The substring must contain only characters from `letters`, and the substring must have exactly `k` characters.
- Example test cases with explanations: 
    - `s = "abc", k = 2, letters = ["a", "b", "c"]`, the maximum number of occurrences is `2` because the substrings `"ab"` and `"bc"` both have `2` characters from `letters`.
    - `s = "abc", k = 3, letters = ["a", "b", "c"]`, the maximum number of occurrences is `1` because the substring `"abc"` has `3` characters from `letters`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible substrings of `s` with `k` characters and count the occurrences of each substring that only contains characters from `letters`.
- Step-by-step breakdown of the solution: 
    1. Generate all possible substrings of `s` with `k` characters.
    2. For each substring, check if it only contains characters from `letters`.
    3. Count the occurrences of each valid substring in `s`.
- Why this approach comes to mind first: It is a straightforward approach that checks all possible substrings.

```cpp
int maxNumberOfOccurrences(string s, int k, vector<string>& letters) {
    int max_count = 0;
    for (int i = 0; i <= s.size() - k; i++) {
        string substring = s.substr(i, k);
        bool is_valid = true;
        for (char c : substring) {
            bool found = false;
            for (string letter : letters) {
                if (c == letter[0]) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                is_valid = false;
                break;
            }
        }
        if (is_valid) {
            int count = 0;
            for (int j = 0; j <= s.size() - k; j++) {
                if (s.substr(j, k) == substring) {
                    count++;
                }
            }
            max_count = max(max_count, count);
        }
    }
    return max_count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k \cdot m)$, where $n$ is the length of `s`, $k$ is the length of the substring, and $m$ is the number of letters in `letters`. This is because we generate all possible substrings of `s` with `k` characters, and for each substring, we check if it only contains characters from `letters` and count its occurrences in `s`.
> - **Space Complexity:** $O(k)$, where $k$ is the length of the substring. This is because we need to store the current substring.
> - **Why these complexities occur:** The time complexity is high because we generate all possible substrings and count their occurrences, and the space complexity is low because we only need to store the current substring.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a sliding window approach to generate all possible substrings of `s` with `k` characters and count the occurrences of each substring that only contains characters from `letters`.
- Detailed breakdown of the approach: 
    1. Initialize a set `letter_set` to store the characters in `letters`.
    2. Initialize a hashmap `count_map` to store the count of each valid substring.
    3. Initialize a variable `max_count` to store the maximum count of occurrences.
    4. Iterate over `s` with a sliding window of size `k`.
    5. For each substring, check if it only contains characters from `letters` by checking if all characters are in `letter_set`.
    6. If the substring is valid, increment its count in `count_map` and update `max_count`.
- Proof of optimality: This approach is optimal because it only generates each substring once and uses a hashmap to store the count of each substring, which reduces the time complexity.

```cpp
int maxNumberOfOccurrences(string s, int k, vector<string>& letters) {
    unordered_set<char> letter_set;
    for (string letter : letters) {
        letter_set.insert(letter[0]);
    }
    unordered_map<string, int> count_map;
    int max_count = 0;
    for (int i = 0; i <= s.size() - k; i++) {
        string substring = s.substr(i, k);
        bool is_valid = true;
        for (char c : substring) {
            if (letter_set.find(c) == letter_set.end()) {
                is_valid = false;
                break;
            }
        }
        if (is_valid) {
            count_map[substring]++;
            max_count = max(max_count, count_map[substring]);
        }
    }
    return max_count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the length of `s` and $k` is the length of the substring. This is because we iterate over `s` with a sliding window of size `k` and check if each substring is valid.
> - **Space Complexity:** $O(n \cdot k)$, where $n` is the length of `s` and `k` is the length of the substring. This is because we need to store the count of each valid substring in a hashmap.
> - **Optimality proof:** This approach is optimal because it only generates each substring once and uses a hashmap to store the count of each substring, which reduces the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, hashmap usage.
- Problem-solving patterns identified: Using a set to store characters and a hashmap to store counts.
- Optimization techniques learned: Using a sliding window to reduce the number of substrings generated, using a hashmap to store counts.
- Similar problems to practice: Problems involving substring generation and counting.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a character is in the set of letters before incrementing the count.
- Edge cases to watch for: Substrings that are not valid because they contain characters not in the set of letters.
- Performance pitfalls: Generating all possible substrings and counting their occurrences without using a hashmap.
- Testing considerations: Testing with different inputs and edge cases to ensure the solution works correctly.