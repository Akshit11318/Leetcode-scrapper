## Find Resultant Array After Removing Anagrams
**Problem Link:** https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description

**Problem Statement:**
- Input format: An array of strings `words`.
- Constraints: All strings in `words` will be unique.
- Expected output format: An array of strings after removing all anagrams from the input array.
- Key requirements: Identify and remove anagrams from the given array of strings.
- Example test cases:
  - Input: `words = ["abba","baba","bbaa","cd","cd"]`
    Output: `["abba","cd","cd"]`
  - Input: `words = ["a","a","b","ab","ba","aa"]`
    Output: `["a","a","a","ab","ba"]`

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to compare each string with every other string to check for anagrams.
- We will use a nested loop to compare each pair of strings.
- To check if two strings are anagrams, we will sort the characters in each string and compare the sorted strings.

```cpp
vector<string> removeAnagrams(vector<string>& words) {
    vector<string> result;
    for (string word : words) {
        bool isAnagram = false;
        for (string w : result) {
            string sortedWord = word;
            string sortedW = w;
            sort(sortedWord.begin(), sortedWord.end());
            sort(sortedW.begin(), sortedW.end());
            if (sortedWord == sortedW) {
                isAnagram = true;
                break;
            }
        }
        if (!isAnagram) {
            result.push_back(word);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m \log m)$, where $n$ is the number of strings and $m$ is the maximum length of a string. The nested loop gives us $O(n^2)$, and sorting each string gives us $O(m \log m)$.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of strings and $m$ is the maximum length of a string. We store the result in a new vector.
> - **Why these complexities occur:** The brute force approach involves comparing each pair of strings, which leads to the quadratic time complexity. Sorting each string to check for anagrams adds to the time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a `unordered_map` to store the sorted characters of each string as the key and the original string as the value.
- We iterate through the input array, sort the characters of each string, and check if the sorted string is already in the map.
- If it is not, we add it to the map and the result array.

```cpp
vector<string> removeAnagrams(vector<string>& words) {
    unordered_map<string, bool> seen;
    vector<string> result;
    for (string word : words) {
        string sortedWord = word;
        sort(sortedWord.begin(), sortedWord.end());
        if (seen.find(sortedWord) == seen.end()) {
            seen[sortedWord] = true;
            result.push_back(word);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \log m)$, where $n$ is the number of strings and $m$ is the maximum length of a string. We iterate through each string once and sort each string.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of strings and $m$ is the maximum length of a string. We store the result in a new vector and the map.
> - **Optimality proof:** This approach is optimal because we only iterate through each string once and use a map to keep track of seen anagrams, reducing the time complexity from quadratic to linear.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, using a map to keep track of seen elements.
- Problem-solving patterns identified: reducing time complexity by using a map to store intermediate results.
- Optimization techniques learned: using a map to avoid duplicate work.
- Similar problems to practice: other problems involving anagrams, such as finding all anagrams of a given string.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to sort the characters of each string, not using a map to keep track of seen anagrams.
- Edge cases to watch for: empty input array, strings with duplicate characters.
- Performance pitfalls: using a brute force approach with quadratic time complexity.
- Testing considerations: test with different input arrays, including edge cases.