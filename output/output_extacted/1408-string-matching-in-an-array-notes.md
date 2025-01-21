## String Matching in an Array

**Problem Link:** https://leetcode.com/problems/string-matching-in-an-array/description

**Problem Statement:**
- Input: An array of strings `words`.
- Constraints: `1 <= words.length <= 100`, `1 <= words[i].length <= 10`, `words[i]` consists of lowercase English letters.
- Expected Output: A list of all substrings of `words` that appear in at least two different words.
- Key Requirements and Edge Cases: 
  - Consider all possible substrings of each word.
  - A substring is considered if it appears in at least two different words.
  - Example test cases: 
    - Input: `words = ["mass","as","hero","superhero"]`
    - Output: `["as","hero"]`
    - Explanation: "as" appears in "mass" and "hero", and "hero" appears in "hero" and "superhero".

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each word in the array, generate all possible substrings and check if any of these substrings appear in other words.
- Step-by-step breakdown of the solution:
  1. Iterate over each word in the array.
  2. For each word, generate all possible substrings.
  3. For each substring, check if it appears in any other word.
  4. If a substring is found in at least two different words, add it to the result list.

```cpp
vector<string> stringMatching(vector<string>& words) {
    vector<string> result;
    for (int i = 0; i < words.size(); i++) {
        for (int j = 0; j < words[i].length(); j++) {
            for (int k = j + 1; k <= words[i].length(); k++) {
                string substr = words[i].substr(j, k - j);
                int count = 0;
                for (int l = 0; l < words.size(); l++) {
                    if (words[l].find(substr) != string::npos) {
                        count++;
                    }
                }
                if (count > 1 && find(result.begin(), result.end(), substr) == result.end()) {
                    result.push_back(substr);
                }
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m^3)$, where $n$ is the number of words and $m$ is the maximum length of a word. This is because for each word, we generate all substrings (which takes $O(m^2)$ time) and then check each substring against all other words (which takes $O(n \cdot m)$ time).
> - **Space Complexity:** $O(n \cdot m^2)$, where $n$ is the number of words and $m$ is the maximum length of a word. This is because we store all substrings of all words.
> - **Why these complexities occur:** The high time complexity occurs because we are generating all substrings for each word and then checking each substring against all other words. The space complexity is high because we are storing all substrings.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all substrings for each word and then checking against all other words, we can iterate through each word and its substrings only once, keeping track of how many times each substring appears across all words.
- Detailed breakdown of the approach:
  1. Create a hashmap to store the frequency of each substring.
  2. Iterate over each word in the array.
  3. For each word, generate all possible substrings and update their frequencies in the hashmap.
  4. After processing all words, iterate through the hashmap and add any substrings with a frequency greater than 1 to the result list.

```cpp
vector<string> stringMatching(vector<string>& words) {
    unordered_map<string, int> freq;
    for (const auto& word : words) {
        for (int i = 0; i < word.length(); i++) {
            for (int j = i + 1; j <= word.length(); j++) {
                string substr = word.substr(i, j - i);
                freq[substr]++;
            }
        }
    }
    vector<string> result;
    for (const auto& pair : freq) {
        if (pair.second > 1) {
            result.push_back(pair.first);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m^3)$, where $n$ is the number of words and $m$ is the maximum length of a word. This is because we still generate all substrings for each word but now we only iterate through the hashmap once at the end to find substrings with frequency greater than 1.
> - **Space Complexity:** $O(n \cdot m^2)$, where $n$ is the number of words and $m$ is the maximum length of a word. This is because we store the frequency of each substring in the hashmap.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to find all substrings that appear in at least two different words. We only iterate through each word and its substrings once and use a hashmap for efficient lookup and frequency counting.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: substring generation, hashmap usage for frequency counting.
- Problem-solving patterns identified: iterating through all possible substrings of a string, using a hashmap to count frequencies.
- Optimization techniques learned: reducing redundant operations by using a hashmap to store and look up substring frequencies.
- Similar problems to practice: problems involving substring matching or frequency counting.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases (e.g., empty strings), incorrect hashmap operations.
- Edge cases to watch for: empty input array, words with no common substrings.
- Performance pitfalls: using inefficient data structures or algorithms, not minimizing the number of operations.
- Testing considerations: test with various input sizes, edge cases, and expected outputs to ensure correctness and efficiency.