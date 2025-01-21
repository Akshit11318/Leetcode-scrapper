## Find the Longest Substring Containing Vowels in Even Counts

**Problem Link:** https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description

**Problem Statement:**
- Input format and constraints: The input is a string `s` consisting of lowercase English letters.
- Expected output format: The output is the length of the longest substring of `s` where every vowel appears an even number of times.
- Key requirements and edge cases to consider: Vowels are defined as 'a', 'e', 'i', 'o', and 'u'. The substring must be non-empty and contain at least one vowel.
- Example test cases with explanations: 
    - For `s = "eleetminicoworoep"`, the longest substring with vowels in even counts is `"leet"`, `"minico"`, `"roo"`, and `"wo"`. The length of the longest substring is 4.
    - For `s = "leetcodeisawesome"`, the longest substring with vowels in even counts is `"leetcode"`, `"is"`, `"awe"`. The length of the longest substring is 6.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can start by checking all possible substrings of `s`.
- Step-by-step breakdown of the solution:
    1. Generate all substrings of `s`.
    2. For each substring, count the occurrences of each vowel.
    3. Check if all vowels appear an even number of times in the substring.
    4. If they do, update the maximum length of the substring.
- Why this approach comes to mind first: It is the most straightforward way to ensure we check every possibility.

```cpp
int findTheLongestSubstring(string s) {
    int n = s.size();
    int maxLen = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n; j++) {
            string substr = s.substr(i, j - i);
            unordered_map<char, int> vowelCount;
            for (char c : substr) {
                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                    vowelCount[c]++;
                }
            }
            bool allEven = true;
            for (auto &pair : vowelCount) {
                if (pair.second % 2 != 0) {
                    allEven = false;
                    break;
                }
            }
            if (allEven) {
                maxLen = max(maxLen, (int)substr.size());
            }
        }
    }
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string `s`. This is because for each of the $O(n^2)$ substrings, we are potentially iterating over the substring again to count vowels.
> - **Space Complexity:** $O(n)$, for storing the substring and the vowel count map.
> - **Why these complexities occur:** The brute force approach involves generating all substrings and then checking each one, leading to high time complexity. The space complexity is due to storing the current substring and the vowel count map.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a bitmask to keep track of the parity of the count of each vowel. Since there are 5 vowels, we need 5 bits to represent the parity of their counts.
- Detailed breakdown of the approach:
    1. Initialize a map to store the bitmask and its corresponding index in the string.
    2. Initialize the bitmask to 0 (all vowels have even counts).
    3. Iterate over the string, updating the bitmask for each vowel encountered.
    4. If the updated bitmask is already in the map, it means we have found a substring where all vowels appear an even number of times. Update the maximum length if necessary.
    5. If the bitmask is not in the map, add it to the map with its current index.
- Proof of optimality: This approach ensures we only need to make a single pass through the string, reducing the time complexity significantly.

```cpp
int findTheLongestSubstring(string s) {
    int n = s.size();
    int maxLen = 0;
    unordered_map<int, int> bitmaskIndex;
    int bitmask = 0;
    bitmaskIndex[0] = -1; // For the case where the substring starts from the beginning
    for (int i = 0; i < n; i++) {
        if (s[i] == 'a') bitmask ^= 1;
        else if (s[i] == 'e') bitmask ^= 2;
        else if (s[i] == 'i') bitmask ^= 4;
        else if (s[i] == 'o') bitmask ^= 8;
        else if (s[i] == 'u') bitmask ^= 16;
        if (bitmaskIndex.find(bitmask) != bitmaskIndex.end()) {
            maxLen = max(maxLen, i - bitmaskIndex[bitmask]);
        } else {
            bitmaskIndex[bitmask] = i;
        }
    }
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we make a single pass through the string.
> - **Space Complexity:** $O(1)$, because the number of possible bitmasks is constant (32 possibilities for 5 bits), and the space used does not grow with the input size.
> - **Optimality proof:** This approach is optimal because it reduces the problem to a single pass through the string, avoiding the need to generate all substrings or count vowels multiple times.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation, bitmasking, and the use of a hashmap to store intermediate results.
- Problem-solving patterns identified: Reducing the problem to a simpler form (using bitmask to represent vowel counts) and using a single pass through the data.
- Optimization techniques learned: Avoiding unnecessary iterations and using bit manipulation for efficient counting.
- Similar problems to practice: Other problems involving substring matching, bit manipulation, or hashmap usage.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating the bitmask or forgetting to handle edge cases (like the substring starting from the beginning).
- Edge cases to watch for: Handling the case where the substring starts from the beginning of the string or when the string is empty.
- Performance pitfalls: Using brute force approaches or inefficient data structures that lead to high time or space complexity.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases like empty strings or strings without vowels.