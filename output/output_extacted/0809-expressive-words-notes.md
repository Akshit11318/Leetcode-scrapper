## Expressive Words

**Problem Link:** https://leetcode.com/problems/expressive-words/description

**Problem Statement:**
- Input format and constraints: The input consists of a string `S` and a list of strings `words`. The task is to find the number of strings in `words` that can be made expressive by inserting exclamation marks.
- Expected output format: The function should return the count of expressive words.
- Key requirements and edge cases to consider: 
    - A character in `S` can be made expressive if it is followed by the same character at least twice.
    - A character in a word can be made expressive if it is followed by the same character at least twice in `S`.
- Example test cases with explanations:
    - `S = "heeellooo", words = ["hello", "hi", "hel"]`: The function should return 1 because "hello" can be made expressive by inserting exclamation marks.
    - `S = "abcd", words = ["ab", "cd", "ab"]`: The function should return 0 because none of the words can be made expressive.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking each word in the list to see if it can be made expressive by inserting exclamation marks.
- Step-by-step breakdown of the solution: 
    1. Iterate over each word in the list.
    2. For each word, iterate over each character and check if it can be made expressive in `S`.
    3. If a character can be made expressive, check the next character in `S` to see if it is the same.
    4. If the next character is the same, continue checking until a different character is found.
    5. If the count of the same character is greater than or equal to 3, the character can be made expressive.
- Why this approach comes to mind first: This approach is straightforward and involves checking each word and character individually.

```cpp
int expressiveWords(string S, vector<string>& words) {
    int count = 0;
    for (string word : words) {
        bool isExpressive = true;
        int i = 0, j = 0;
        while (i < word.size() && j < S.size()) {
            if (word[i] != S[j]) {
                isExpressive = false;
                break;
            }
            int wordCount = 0, sCount = 0;
            while (i + wordCount < word.size() && word[i] == word[i + wordCount]) {
                wordCount++;
            }
            while (j + sCount < S.size() && S[j] == S[j + sCount]) {
                sCount++;
            }
            if (wordCount != sCount && (wordCount > sCount || wordCount < sCount && sCount < 3)) {
                isExpressive = false;
                break;
            }
            i += wordCount;
            j += sCount;
        }
        if (i < word.size() || j < S.size()) {
            isExpressive = false;
        }
        if (isExpressive) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of words and $m$ is the average length of a word.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the count and indices.
> - **Why these complexities occur:** The time complexity occurs because we iterate over each word and character in the word. The space complexity occurs because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using two pointers to iterate over the word and `S` simultaneously.
- Detailed breakdown of the approach: 
    1. Initialize two pointers, `i` and `j`, to the start of the word and `S`.
    2. Iterate over the word and `S` using the two pointers.
    3. If the current character in the word is not equal to the current character in `S`, return false.
    4. If the current character in the word is equal to the current character in `S`, count the number of consecutive occurrences of the character in the word and `S`.
    5. If the counts are not equal and the count in `S` is less than 3, return false.
    6. If the counts are equal or the count in `S` is greater than or equal to 3, move the pointers to the next character.
- Proof of optimality: This approach is optimal because it only requires a single pass over the word and `S`, resulting in a time complexity of $O(n \cdot m)$.

```cpp
int expressiveWords(string S, vector<string>& words) {
    int count = 0;
    for (string word : words) {
        int i = 0, j = 0;
        while (i < word.size() && j < S.size()) {
            if (word[i] != S[j]) {
                break;
            }
            int wordCount = 0, sCount = 0;
            char c = word[i];
            while (i < word.size() && word[i] == c) {
                wordCount++;
                i++;
            }
            while (j < S.size() && S[j] == c) {
                sCount++;
                j++;
            }
            if (wordCount != sCount && (wordCount > sCount || wordCount < sCount && sCount < 3)) {
                break;
            }
        }
        if (i == word.size() && j == S.size()) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of words and $m$ is the average length of a word.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space to store the count and indices.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the word and `S`, resulting in a time complexity of $O(n \cdot m)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two pointers, counting consecutive occurrences of characters.
- Problem-solving patterns identified: Using two pointers to iterate over two strings simultaneously.
- Optimization techniques learned: Using a single pass over the strings to reduce time complexity.
- Similar problems to practice: Other problems involving string manipulation and counting consecutive occurrences of characters.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for equal counts of consecutive occurrences of characters.
- Edge cases to watch for: Handling cases where the word is longer than `S` or vice versa.
- Performance pitfalls: Using nested loops to iterate over the word and `S`, resulting in a higher time complexity.
- Testing considerations: Testing cases where the word is equal to `S`, where the word is longer than `S`, and where the word is shorter than `S`.