## Sum of Beauty of All Substrings

**Problem Link:** https://leetcode.com/problems/sum-of-beauty-of-all-substrings/description

**Problem Statement:**
- Input: A string `s` containing lowercase English letters.
- Output: The sum of the beauty of all substrings in `s`.
- Key requirements: 
  - The beauty of a substring is the difference between the frequency of the most frequent character and the frequency of the least frequent character in the substring.
  - Consider all possible substrings of `s`.
- Edge cases: 
  - If `s` is empty, return 0.
  - If `s` contains only one unique character, the beauty of all substrings will be 0.

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating over all possible substrings of `s`.
- For each substring, calculate the frequency of each character.
- Then, find the maximum and minimum frequencies to determine the beauty of the substring.
- Sum up the beauty of all substrings.

```cpp
int beautySum(string s) {
    int n = s.size(), res = 0;
    for (int i = 0; i < n; i++) {
        unordered_map<char, int> count;
        int maxCount = 0;
        for (int j = i; j < n; j++) {
            count[s[j]]++;
            maxCount = max(maxCount, count[s[j]]);
            int minCount = INT_MAX;
            for (auto& it : count) {
                minCount = min(minCount, it.second);
            }
            res += maxCount - minCount;
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `s`. This is because for each substring, we are iterating over its characters to find the maximum and minimum frequencies.
> - **Space Complexity:** $O(n)$, as in the worst case, we might need to store all characters in the `count` map.
> - **Why these complexities occur:** The high time complexity is due to the nested loops and the iteration over the map for each substring.

### Optimal Approach (Required)

**Explanation:**
- To optimize the solution, we can use a sliding window approach and maintain the frequency of characters within the current window.
- We also keep track of the frequency of each character in the window using a map.
- When expanding the window to the right, we update the frequency of the new character and when shrinking the window from the left, we decrease the frequency of the character going out of the window.

However, a better approach exists before reaching the optimal solution.

### Better Approach

**Explanation:**
- Instead of iterating over all substrings and then finding the frequency of each character in the substring, we can fix the length of the substring and slide a window of that length over `s`.
- For each window position, calculate the frequency of characters in the window.
- This approach still has a high time complexity but is an intermediate step towards the optimal solution.

```cpp
int beautySum(string s) {
    int n = s.size(), res = 0;
    for (int len = 1; len <= n; len++) {
        for (int i = 0; i <= n - len; i++) {
            unordered_map<char, int> count;
            for (int j = i; j < i + len; j++) {
                count[s[j]]++;
            }
            int maxCount = 0, minCount = INT_MAX;
            for (auto& it : count) {
                maxCount = max(maxCount, it.second);
                minCount = min(minCount, it.second);
            }
            res += maxCount - minCount;
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `s`. This is still high because for each window, we are iterating over its characters to update the frequency map.
> - **Space Complexity:** $O(n)$, for storing the frequency map.
> - **Improvement over brute force:** This approach is more systematic but still has the same time complexity as the brute force. However, it sets the stage for further optimization.

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using a frequency array instead of a map for each character in the substring.
- This is because we only deal with lowercase English letters, so we can use an array of size 26 to store the frequency of each character.
- We slide a window over `s` and for each window position, we update the frequency array.
- Then, we find the maximum and minimum frequencies from the array to calculate the beauty of the substring.

```cpp
int beautySum(string s) {
    int n = s.size(), res = 0;
    for (int len = 3; len <= n; len++) {
        for (int i = 0; i <= n - len; i++) {
            int freq[26] = {0};
            for (int j = i; j < i + len; j++) {
                freq[s[j] - 'a']++;
            }
            int maxCount = 0, minCount = INT_MAX;
            for (int j = 0; j < 26; j++) {
                if (freq[j] > 0) {
                    maxCount = max(maxCount, freq[j]);
                    minCount = min(minCount, freq[j]);
                }
            }
            res += maxCount - minCount;
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the length of `s` and $m$ is the size of the character set (26 for lowercase English letters). This is because we iterate over all substrings and for each substring, we update the frequency array.
> - **Space Complexity:** $O(1)$, as the space used does not grow with the size of the input, excluding the space needed for the input itself.
> - **Optimality proof:** This solution is optimal because it minimizes the number of operations needed to calculate the beauty of all substrings. It avoids unnecessary iterations and uses an efficient data structure (array) to store character frequencies.

---

### Final Notes

**Learning Points:**
- The importance of understanding the constraints of the problem to choose the right data structure (e.g., using an array for character frequencies instead of a map).
- How to apply the sliding window technique to problems involving substrings.
- The value of breaking down a problem into smaller, more manageable parts to find an optimal solution.

**Mistakes to Avoid:**
- Using a map for character frequencies when dealing with a fixed character set.
- Not considering the sliding window approach for substring-related problems.
- Failing to optimize the solution by reducing unnecessary iterations or using inefficient data structures.