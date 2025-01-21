## Longest Palindrome by Concatenating Two-Letter Words

**Problem Link:** https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/description

**Problem Statement:**
- Input: An array of strings `words` where each string is a two-letter word.
- Constraints: Each word in `words` is a two-letter word, and the length of `words` is in the range `[1, 10^4]`.
- Expected Output: The length of the longest palindrome that can be formed by concatenating two-letter words from the `words` array.
- Key Requirements:
  - The palindrome must consist of two-letter words from the input array.
  - Each two-letter word can be used at most once.
- Edge Cases:
  - If no palindrome can be formed, return 0.
  - If only one two-letter word can form a palindrome, return 2.

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking all possible combinations of two-letter words to form a palindrome.
- This approach involves generating all permutations of the input words and checking each permutation to see if it forms a palindrome.
- Why this approach comes to mind first: It is the most straightforward way to ensure that all possibilities are considered.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int longestPalindrome(vector<string>& words) {
    int n = words.size();
    int maxLen = 0;
    
    // Generate all permutations of the input words
    vector<vector<string>> perms;
    vector<string> temp;
    permute(words, temp, perms);
    
    // Check each permutation to see if it forms a palindrome
    for (auto& perm : perms) {
        string str;
        for (auto& word : perm) {
            str += word;
        }
        if (isPalindrome(str)) {
            maxLen = max(maxLen, (int)str.length());
        }
    }
    
    return maxLen;
}

void permute(vector<string>& words, vector<string>& temp, vector<vector<string>>& perms) {
    if (temp.size() == words.size()) {
        perms.push_back(temp);
        return;
    }
    for (int i = 0; i < words.size(); i++) {
        if (find(temp.begin(), temp.end(), words[i]) != temp.end()) {
            continue;
        }
        temp.push_back(words[i]);
        permute(words, temp, perms);
        temp.pop_back();
    }
}

bool isPalindrome(string& str) {
    int left = 0, right = str.length() - 1;
    while (left < right) {
        if (str[left] != str[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n)$, where $n$ is the number of input words. This is because we generate all permutations of the input words and check each permutation to see if it forms a palindrome.
> - **Space Complexity:** $O(n! \cdot n)$, where $n$ is the number of input words. This is because we store all permutations of the input words.
> - **Why these complexities occur:** The brute force approach involves generating all permutations of the input words and checking each permutation to see if it forms a palindrome. This results in high time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a hashmap to store the frequency of each two-letter word and its reverse.
- We iterate through the input words and update the frequency of each word and its reverse in the hashmap.
- We then iterate through the hashmap and count the number of pairs of words that can form a palindrome.
- If a word is a palindrome itself (i.e., it reads the same forwards and backwards), we can add it to the palindrome once.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

int longestPalindrome(vector<string>& words) {
    unordered_map<string, int> freq;
    for (auto& word : words) {
        freq[word]++;
    }
    
    int maxLen = 0;
    bool hasMiddle = false;
    for (auto& pair : freq) {
        string word = pair.first;
        string reverse = word;
        reverse[0] = word[1];
        reverse[1] = word[0];
        
        if (word == reverse) {
            if (freq[word] % 2 == 1) {
                hasMiddle = true;
            }
            maxLen += (freq[word] / 2) * 4;
        } else if (freq.count(reverse) > 0) {
            maxLen += 2 * min(freq[word], freq[reverse]);
            freq[reverse] = 0;
        }
    }
    
    if (hasMiddle) {
        maxLen += 2;
    }
    
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of input words. This is because we iterate through the input words once to update the frequency of each word and its reverse in the hashmap, and then iterate through the hashmap once to count the number of pairs of words that can form a palindrome.
> - **Space Complexity:** $O(n)$, where $n$ is the number of input words. This is because we store the frequency of each word and its reverse in the hashmap.
> - **Optimality proof:** This approach is optimal because it counts the maximum number of pairs of words that can form a palindrome in a single pass through the input words and the hashmap. It also handles the case where a word is a palindrome itself correctly.

---

### Final Notes

**Learning Points:**
- The importance of using a hashmap to store the frequency of each two-letter word and its reverse.
- How to count the number of pairs of words that can form a palindrome.
- How to handle the case where a word is a palindrome itself.

**Mistakes to Avoid:**
- Not using a hashmap to store the frequency of each two-letter word and its reverse, resulting in high time complexity.
- Not counting the number of pairs of words that can form a palindrome correctly.
- Not handling the case where a word is a palindrome itself correctly.