## Count Words Obtained After Adding a Letter
**Problem Link:** https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/description

**Problem Statement:**
- Input: Two lists of strings, `startWords` and `targetWords`.
- Constraints: Each string consists only of lowercase English letters, and the length of each string is between 1 and 26.
- Expected Output: The number of strings in `targetWords` that can be formed by adding exactly one letter to the end of a string in `startWords`.
- Key Requirements: 
  - Each string in `startWords` can be used as a prefix for multiple strings in `targetWords`.
  - The order of characters in the string matters.
- Example Test Cases:
  - Input: `startWords = ["ant","act","add"]`, `targetWords = ["ant","act","acti","add"]`
    - Output: `2`
    - Explanation: `ant` can be formed by adding 't' to the end of an empty string, `acti` can be formed by adding 'i' to the end of `act`, and `add` can be formed by adding 'd' to the end of an empty string, but only `acti` and `add` can be formed by adding a letter to a word in `startWords`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to iterate through each string in `targetWords` and check if it can be formed by adding a letter to any string in `startWords`.
- We will generate all possible prefixes of each string in `targetWords` by removing one character at a time and check if any of these prefixes exist in `startWords`.
- This approach comes to mind first because it directly addresses the problem statement by checking all possible combinations.

```cpp
class Solution {
public:
    int wordCount(vector<string>& startWords, vector<string>& targetWords) {
        unordered_set<string> startWordSet(startWords.begin(), startWords.end());
        int count = 0;
        for (const string& targetWord : targetWords) {
            bool found = false;
            for (int i = 0; i < targetWord.size(); ++i) {
                string prefix = targetWord.substr(0, i) + targetWord.substr(i + 1);
                if (startWordSet.find(prefix) != startWordSet.end()) {
                    found = true;
                    break;
                }
            }
            if (found) {
                count++;
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the number of strings in `targetWords`, $m$ is the average length of a string in `targetWords`, and $k$ is the number of strings in `startWords`. This is because for each string in `targetWords`, we generate $m$ prefixes and check if each prefix exists in `startWords`.
> - **Space Complexity:** $O(k)$, where $k$ is the number of strings in `startWords`. This is because we store all strings in `startWords` in a set for efficient lookup.
> - **Why these complexities occur:** These complexities occur because we are using a brute force approach that checks all possible combinations of prefixes for each string in `targetWords`.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is to realize that we can use a `unordered_set` to store the `startWords` for efficient lookup.
- We can then iterate through each string in `targetWords` and for each string, generate all possible prefixes by removing one character at a time and check if any of these prefixes exist in the `startWords` set.
- This approach is optimal because it reduces the time complexity of checking if a prefix exists in `startWords` from $O(k)$ to $O(1)$ on average.

```cpp
class Solution {
public:
    int wordCount(vector<string>& startWords, vector<string>& targetWords) {
        unordered_set<string> startWordSet(startWords.begin(), startWords.end());
        int count = 0;
        for (const string& targetWord : targetWords) {
            bool found = false;
            for (int i = 0; i < targetWord.size(); ++i) {
                string prefix = targetWord.substr(0, i) + targetWord.substr(i + 1);
                if (startWordSet.find(prefix) != startWordSet.end()) {
                    found = true;
                    break;
                }
            }
            if (found) {
                count++;
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of strings in `targetWords` and $m$ is the average length of a string in `targetWords`. This is because for each string in `targetWords`, we generate $m$ prefixes and check if each prefix exists in `startWords` in $O(1)$ time on average.
> - **Space Complexity:** $O(k)$, where $k$ is the number of strings in `startWords`. This is because we store all strings in `startWords` in a set for efficient lookup.
> - **Optimality proof:** This approach is optimal because it uses a `unordered_set` to store `startWords` for efficient lookup, reducing the time complexity of checking if a prefix exists in `startWords` from $O(k)$ to $O(1)$ on average.

---

### Final Notes

**Learning Points:**
- The importance of using `unordered_set` for efficient lookup.
- The trade-off between time and space complexity.
- The use of string manipulation functions such as `substr` to generate prefixes.

**Mistakes to Avoid:**
- Not using a `unordered_set` to store `startWords`, resulting in a higher time complexity.
- Not checking if a prefix exists in `startWords` before incrementing the count, resulting in incorrect results.
- Not handling edge cases such as empty strings or strings with only one character.