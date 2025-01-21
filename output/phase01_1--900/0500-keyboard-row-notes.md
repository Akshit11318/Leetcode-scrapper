## Keyboard Row
**Problem Link:** https://leetcode.com/problems/keyboard-row/description

**Problem Statement:**
- Given a list of words, return the list of words that can be typed on a single row of the keyboard.
- Input format: A list of strings `words`.
- Constraints: Each word contains only lowercase letters.
- Expected output format: A list of strings that can be typed on a single row of the keyboard.
- Key requirements and edge cases to consider:
  - Handling empty strings or null inputs.
  - Considering the keyboard layout: the first row is `qwertyuiop`, the second row is `asdfghjkl`, and the third row is `zxcvbnm`.
- Example test cases with explanations:
  - Input: `["Hello", "Alaska", "Dad", "Peace"]`
  - Output: `["Alaska", "Dad"]`
  - Explanation: Only `Alaska` and `Dad` can be typed on a single row of the keyboard.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check each word against each row of the keyboard to see if it can be typed on a single row.
- Step-by-step breakdown of the solution:
  1. Define the keyboard rows as strings.
  2. For each word, check if all its characters are in the same row of the keyboard.
  3. If a word can be typed on a single row, add it to the result list.
- Why this approach comes to mind first: It directly checks each word against the keyboard layout, which seems like the most straightforward way to solve the problem.

```cpp
class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        vector<string> rows = {"qwertyuiop", "asdfghjkl", "zxcvbnm"};
        vector<string> result;
        
        for (const string& word : words) {
            bool found = false;
            for (const string& row : rows) {
                bool allInRow = true;
                for (char c : word) {
                    if (row.find(tolower(c)) == string::npos) {
                        allInRow = false;
                        break;
                    }
                }
                if (allInRow) {
                    result.push_back(word);
                    found = true;
                    break;
                }
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the number of words, $m$ is the average length of a word, and $k$ is the number of rows on the keyboard. This is because for each word, we potentially check each character against each row.
> - **Space Complexity:** $O(n)$, where $n$ is the number of words. This is because in the worst case, all words could be added to the result list.
> - **Why these complexities occur:** The brute force approach involves nested loops for each word, character, and row, leading to the cubic time complexity. The space complexity is linear because we store the result in a list that could potentially hold all input words.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking each word against each row for each character, we can use a `set` or an equivalent data structure to store the characters in each row for efficient lookups.
- Detailed breakdown of the approach:
  1. Create sets for each row of the keyboard for fast lookups.
  2. For each word, determine which row it belongs to by checking its characters against the sets.
  3. If all characters of a word are in the same row's set, add the word to the result list.
- Proof of optimality: This approach reduces the time complexity by using sets for fast lookups, making it more efficient than the brute force approach.
- Why further optimization is impossible: Given the need to check each character of each word against the keyboard rows, this approach is optimal as it minimizes the number of operations required.

```cpp
class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        unordered_set<char> row1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'};
        unordered_set<char> row2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'};
        unordered_set<char> row3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'};
        vector<string> result;
        
        for (const string& word : words) {
            bool row1Match = true, row2Match = true, row3Match = true;
            for (char c : word) {
                char lowerC = tolower(c);
                if (row1.find(lowerC) == row1.end()) row1Match = false;
                if (row2.find(lowerC) == row2.end()) row2Match = false;
                if (row3.find(lowerC) == row3.end()) row3Match = false;
            }
            if (row1Match || row2Match || row3Match) {
                result.push_back(word);
            }
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of words and $m$ is the average length of a word. This is because for each word, we check each character against the sets.
> - **Space Complexity:** $O(1)$, since we use a constant amount of space to store the sets of characters for each row, regardless of the input size.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to check each word against the keyboard rows, using sets for fast lookups.

---

### Final Notes

**Learning Points:**
- **Efficient data structures:** Using sets for fast lookups can significantly improve the efficiency of algorithms.
- **Problem-solving patterns:** Identifying the need for fast lookups and applying the appropriate data structures is a key pattern in algorithm design.
- **Optimization techniques:** Recognizing the potential for optimization and applying techniques like using sets can lead to more efficient solutions.

**Mistakes to Avoid:**
- **Inefficient loops:** Avoid using nested loops when possible, especially when dealing with large datasets.
- **Slow lookup methods:** Be aware of the lookup times of different data structures and choose the most efficient one for the task at hand.
- **Lack of input validation:** Always consider the potential for invalid or edge-case inputs and handle them appropriately.