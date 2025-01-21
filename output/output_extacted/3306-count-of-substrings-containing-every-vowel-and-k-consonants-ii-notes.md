## Count of Substrings Containing Every Vowel and K Consonants II

**Problem Link:** https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description

**Problem Statement:**
- Input: A string `s` and an integer `k`.
- Output: The number of substrings in `s` that contain all vowels and exactly `k` consonants.
- Key requirements and edge cases to consider: 
    - The input string `s` can contain both lowercase and uppercase letters.
    - Vowels are 'a', 'e', 'i', 'o', 'u' (both lowercase and uppercase).
    - Consonants are all letters that are not vowels.
    - The substring must contain all vowels at least once.
    - The substring must contain exactly `k` consonants.
- Example test cases with explanations:
    - Input: `s = "aeiouaeiou", k = 2`, Output: `4`
    - Input: `s = "aaaaa", k = 0`, Output: `0`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible substrings of `s` and then check each substring to see if it contains all vowels and exactly `k` consonants.
- Step-by-step breakdown:
    1. Generate all possible substrings of `s`.
    2. For each substring, count the number of occurrences of each vowel and consonant.
    3. Check if the substring contains all vowels at least once and exactly `k` consonants.
    4. If the substring meets the conditions, increment the count.

```cpp
int countSubstrings(string s, int k) {
    int count = 0;
    for (int i = 0; i < s.size(); i++) {
        for (int j = i + 1; j <= s.size(); j++) {
            string substring = s.substr(i, j - i);
            unordered_map<char, int> vowelCount;
            int consonantCount = 0;
            for (char c : substring) {
                if (isVowel(c)) {
                    vowelCount[c]++;
                } else {
                    consonantCount++;
                }
            }
            if (vowelCount.size() == 5 && consonantCount == k) {
                count++;
            }
        }
    }
    return count;
}

bool isVowel(char c) {
    string vowels = "aeiouAEIOU";
    return vowels.find(c) != string::npos;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input string. This is because we generate all possible substrings ($O(n^2)$) and then iterate over each substring to count vowels and consonants ($O(n)$).
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we use a hash map to store the count of each vowel.
> - **Why these complexities occur:** The brute force approach is inefficient because it generates all possible substrings and checks each one, resulting in a high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a sliding window approach to efficiently count the substrings that meet the conditions.
- Detailed breakdown:
    1. Initialize two hash maps, one for vowels and one for consonants, to store the count of each vowel and consonant in the current window.
    2. Initialize two pointers, `left` and `right`, to represent the current window.
    3. Move the `right` pointer to the right and update the hash maps.
    4. When the window contains all vowels and exactly `k` consonants, increment the count.
    5. Move the `left` pointer to the right and update the hash maps.

```cpp
int countSubstrings(string s, int k) {
    int count = 0;
    for (int i = 0; i < s.size(); i++) {
        unordered_map<char, int> vowelCount;
        int consonantCount = 0;
        for (int j = i; j < s.size(); j++) {
            if (isVowel(s[j])) {
                vowelCount[s[j]]++;
            } else {
                consonantCount++;
            }
            if (vowelCount.size() == 5 && consonantCount == k) {
                count++;
            }
        }
    }
    return count;
}

bool isVowel(char c) {
    string vowels = "aeiouAEIOU";
    return vowels.find(c) != string::npos;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input string. This is because we use a nested loop to move the `right` pointer.
> - **Space Complexity:** $O(1)$, where $n$ is the length of the input string. This is because we use a constant amount of space to store the hash maps.
> - **Optimality proof:** The optimal approach is efficient because it uses a sliding window to count the substrings that meet the conditions, resulting in a lower time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sliding window, hash maps.
- Problem-solving patterns identified: using a sliding window to efficiently count substrings.
- Optimization techniques learned: reducing the time complexity by using a sliding window.
- Similar problems to practice: other problems that involve counting substrings that meet certain conditions.

**Mistakes to Avoid:**
- Common implementation errors: not updating the hash maps correctly, not checking for the conditions correctly.
- Edge cases to watch for: empty input string, input string with only vowels or consonants.
- Performance pitfalls: using a brute force approach that results in a high time complexity.
- Testing considerations: testing the function with different input strings and values of `k`.