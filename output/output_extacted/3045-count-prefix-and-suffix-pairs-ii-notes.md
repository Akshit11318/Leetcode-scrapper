## Count Prefix and Suffix Pairs II

**Problem Link:** https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/description

**Problem Statement:**
- Input: Two arrays of strings, `words1` and `words2`.
- Constraints: Both arrays contain only lowercase English letters and have a length of at least 1 and at most $10^5$. Each string has a length of at least 1 and at most 1000.
- Expected Output: An array of integers representing the count of prefix and suffix pairs for each word in `words1`.
- Key Requirements: For each word in `words1`, find how many words in `words2` are both a prefix and a suffix of the word.
- Edge Cases: Handling empty strings or arrays, and words with varying lengths.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each word in `words1`, check every word in `words2` to see if it is both a prefix and a suffix of the word.
- Step-by-step breakdown:
  1. Iterate through each word in `words1`.
  2. For each word in `words1`, iterate through each word in `words2`.
  3. Check if the word from `words2` is a prefix of the current word from `words1`.
  4. Check if the word from `words2` is also a suffix of the current word from `words1`.
  5. If both conditions are met, increment the count for the current word from `words1`.
- Why this approach comes to mind first: It directly addresses the problem statement by checking every possible combination, which is a straightforward but inefficient way to solve the problem.

```cpp
vector<int> countPrefixAndSuffixPairs(vector<string>& words1, vector<string>& words2) {
    vector<int> counts;
    for (const auto& word1 : words1) {
        int count = 0;
        for (const auto& word2 : words2) {
            if (word1.size() >= word2.size()) {
                bool isPrefix = true;
                bool isSuffix = true;
                for (int i = 0; i < word2.size(); i++) {
                    if (word1[i] != word2[i]) isPrefix = false;
                    if (word1[word1.size() - word2.size() + i] != word2[i]) isSuffix = false;
                }
                if (isPrefix && isSuffix) count++;
            }
        }
        counts.push_back(count);
    }
    return counts;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$ where $n$ is the number of words in `words1`, $m$ is the number of words in `words2`, and $k$ is the maximum length of a word. This is because for each word in `words1`, we potentially check every word in `words2` and for each of those, we check up to the length of the word.
> - **Space Complexity:** $O(n)$ for storing the counts of prefix and suffix pairs for each word in `words1`.
> - **Why these complexities occur:** The brute force approach involves nested loops over the input arrays and an additional loop over the characters of the words, leading to high time complexity. The space complexity is relatively low as we only need to store the counts for each word in `words1`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a `std::unordered_map` to store the words from `words2` and their counts. Then, for each word in `words1`, we can check all its prefixes and suffixes of the same length to see if they are in the map, thus reducing the number of comparisons needed.
- Detailed breakdown:
  1. Create an `std::unordered_map` to store the words from `words2` and their counts.
  2. Iterate through each word in `words1`.
  3. For each word in `words1`, generate all possible prefixes and suffixes of the same length.
  4. Check if each prefix/suffix pair is in the map and if so, increment the count.
- Proof of optimality: This approach reduces the time complexity significantly by avoiding the need to compare each word in `words1` with every word in `words2`. Instead, it leverages the efficient lookup of `std::unordered_map`.

```cpp
vector<int> countPrefixAndSuffixPairs(vector<string>& words1, vector<string>& words2) {
    unordered_map<string, int> wordCounts;
    for (const auto& word : words2) wordCounts[word]++;
    
    vector<int> counts;
    for (const auto& word1 : words1) {
        int count = 0;
        for (int len = 1; len <= word1.size(); len++) {
            string prefix = word1.substr(0, len);
            string suffix = word1.substr(word1.size() - len);
            if (prefix == suffix && wordCounts.find(prefix) != wordCounts.end()) {
                count += wordCounts[prefix];
            }
        }
        counts.push_back(count);
    }
    return counts;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m + n \cdot k^2)$ where $n$ is the number of words in `words1`, $m$ is the number of words in `words2`, and $k$ is the maximum length of a word. The first term accounts for populating the map, and the second term accounts for generating prefixes/suffixes and looking them up in the map.
> - **Space Complexity:** $O(m)$ for storing the words from `words2` in the map, plus $O(n)$ for storing the counts for each word in `words1`.
> - **Optimality proof:** This approach is optimal because it minimizes the number of comparisons needed by leveraging the efficient lookup of `std::unordered_map` for prefix/suffix pairs, thus reducing the time complexity significantly compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- The importance of leveraging data structures like `std::unordered_map` for efficient lookup.
- How to approach problems that involve comparing elements across two arrays.
- The trade-off between time and space complexity in algorithm design.

**Mistakes to Avoid:**
- Not considering the use of efficient data structures for lookup.
- Failing to optimize nested loops by reducing the number of comparisons.
- Not accounting for edge cases such as empty strings or arrays.