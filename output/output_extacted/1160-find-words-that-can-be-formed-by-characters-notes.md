## Find Words That Can Be Formed by Characters
**Problem Link:** https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description

**Problem Statement:**
- Input format and constraints: Given an array of strings `words` and a string `chars`, return all the strings in the `words` array that can be formed from the characters of `chars`.
- Expected output format: A list of strings.
- Key requirements and edge cases to consider: 
  - Each character in `chars` can only be used as many times as it appears in `chars`.
  - Each string in `words` can only be used once.
- Example test cases with explanations: 
  - Example 1: Input: `words = ["cat","bt","hat","tree"]`, `chars = "atach"`. Output: `["cat","hat"]`. Explanation: Only "cat" and "hat" can be formed from the characters of `chars`.
  - Example 2: Input: `words = ["hello","world","leetcode"]`, `chars = "welldonehoneyr"`. Output: `["hello","world","leetcode"]`. Explanation: All three words can be formed from the characters of `chars`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: For each word in the `words` array, count the frequency of each character and compare it with the frequency of characters in `chars`. If a word can be formed, add it to the result list.
- Step-by-step breakdown of the solution:
  1. Iterate through each word in the `words` array.
  2. For each word, count the frequency of each character.
  3. Compare the frequency count of the word with the frequency count of `chars`.
  4. If the word can be formed, add it to the result list.
- Why this approach comes to mind first: It's a straightforward approach that checks each word individually against the available characters.

```cpp
vector<string> findWords(vector<string>& words, string chars) {
    vector<string> result;
    for (string word : words) {
        unordered_map<char, int> wordCount, charsCount;
        for (char c : word) wordCount[c]++;
        for (char c : chars) charsCount[c]++;
        
        bool canBeFormed = true;
        for (auto& pair : wordCount) {
            if (charsCount.find(pair.first) == charsCount.end() || pair.second > charsCount[pair.first]) {
                canBeFormed = false;
                break;
            }
        }
        
        if (canBeFormed) result.push_back(word);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the number of words, $m$ is the maximum length of a word, and $k$ is the length of `chars`. The reason is that for each word, we're iterating through its characters and the characters of `chars`.
> - **Space Complexity:** $O(n \cdot m + k)$, where $n$ is the number of words and $m$ is the maximum length of a word. This is because we're storing the frequency counts of characters for each word and for `chars`.
> - **Why these complexities occur:** The brute force approach involves iterating through each character of each word and `chars`, leading to the time complexity. The space complexity comes from storing the frequency counts.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of counting the frequency of characters for each word individually, we can count the frequency of characters in `chars` once and then compare it with the frequency count of each word.
- Detailed breakdown of the approach:
  1. Count the frequency of characters in `chars`.
  2. Iterate through each word in the `words` array.
  3. For each word, count the frequency of its characters.
  4. Compare the frequency count of the word with the pre-counted frequency of `chars`.
  5. If the word can be formed, add it to the result list.
- Proof of optimality: This approach is optimal because it minimizes the number of times we need to count the frequency of characters in `chars`, reducing the overall time complexity.

```cpp
vector<string> findWords(vector<string>& words, string chars) {
    vector<string> result;
    unordered_map<char, int> charsCount;
    for (char c : chars) charsCount[c]++;
    
    for (string word : words) {
        unordered_map<char, int> wordCount;
        for (char c : word) wordCount[c]++;
        
        bool canBeFormed = true;
        for (auto& pair : wordCount) {
            if (charsCount.find(pair.first) == charsCount.end() || pair.second > charsCount[pair.first]) {
                canBeFormed = false;
                break;
            }
        }
        
        if (canBeFormed) result.push_back(word);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m + k)$, where $n$ is the number of words, $m$ is the maximum length of a word, and $k$ is the length of `chars`. The reason is that we're iterating through `chars` once and then through each word.
> - **Space Complexity:** $O(n \cdot m + k)$, where $n$ is the number of words and $m$ is the maximum length of a word. This is because we're storing the frequency counts of characters for each word and for `chars`.
> - **Optimality proof:** This approach is optimal because it minimizes the number of times we need to count the frequency of characters in `chars`, reducing the overall time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Frequency counting, string manipulation.
- Problem-solving patterns identified: Pre-processing the input to reduce the time complexity.
- Optimization techniques learned: Minimizing the number of times we need to perform a certain operation (in this case, counting the frequency of characters in `chars`).
- Similar problems to practice: Other string manipulation and frequency counting problems.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the existence of a character in the frequency count map before accessing it.
- Edge cases to watch for: Empty strings, strings with only one character.
- Performance pitfalls: Not pre-processing the input to reduce the time complexity.
- Testing considerations: Test with different lengths of `chars` and words, test with words that can and cannot be formed from `chars`.