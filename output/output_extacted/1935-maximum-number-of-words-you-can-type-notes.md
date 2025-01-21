## Maximum Number of Words You Can Type
**Problem Link:** https://leetcode.com/problems/maximum-number-of-words-you-can-type/description

**Problem Statement:**
- Input format and constraints: Given a string `text` and an array of strings `brokenLetters`, return the maximum number of words you can type.
- Expected output format: An integer representing the maximum number of words that can be typed.
- Key requirements and edge cases to consider: The function should only consider words that do not contain any of the broken letters.
- Example test cases with explanations:
  - `text = "hello world", brokenLetters = ["e", "o"]`, the function should return 1 because only "hello" can be typed.
  - `text = "leet code", brokenLetters = ["e", "t"]`, the function should return 1 because only "code" can be typed.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can iterate through each word in the `text` and check if it contains any of the `brokenLetters`.
- Step-by-step breakdown of the solution:
  1. Split the `text` into words.
  2. Iterate through each word.
  3. For each word, check if it contains any of the `brokenLetters`.
  4. If a word does not contain any `brokenLetters`, increment the count of words that can be typed.
- Why this approach comes to mind first: It is a straightforward approach that checks each word individually.

```cpp
int canBeTypedWords(string text, string brokenLetters) {
    // Split the text into words
    istringstream iss(text);
    string word;
    int count = 0;

    // Iterate through each word
    while (iss >> word) {
        bool containsBrokenLetter = false;

        // Check if the word contains any broken letters
        for (char c : word) {
            if (brokenLetters.find(c) != string::npos) {
                containsBrokenLetter = true;
                break;
            }
        }

        // If the word does not contain any broken letters, increment the count
        if (!containsBrokenLetter) {
            count++;
        }
    }

    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the number of words in the `text`, $m$ is the average length of a word, and $k$ is the length of `brokenLetters`. This is because for each word, we are checking each character against the `brokenLetters`.
> - **Space Complexity:** $O(1)$, excluding the space required for the input and output. This is because we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The time complexity occurs because of the nested loops, and the space complexity occurs because we are not using any additional space that scales with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking each word individually, we can create a set of `brokenLetters` to reduce the time complexity of checking if a word contains any `brokenLetters`.
- Detailed breakdown of the approach:
  1. Create a set of `brokenLetters`.
  2. Split the `text` into words.
  3. Iterate through each word.
  4. For each word, check if it contains any of the `brokenLetters` using the set.
  5. If a word does not contain any `brokenLetters`, increment the count of words that can be typed.
- Proof of optimality: This approach is optimal because we are reducing the time complexity of checking if a word contains any `brokenLetters` from $O(k)$ to $O(1)$, where $k$ is the length of `brokenLetters`.

```cpp
int canBeTypedWords(string text, string brokenLetters) {
    // Create a set of broken letters
    unordered_set<char> brokenLettersSet(brokenLetters.begin(), brokenLetters.end());

    // Split the text into words
    istringstream iss(text);
    string word;
    int count = 0;

    // Iterate through each word
    while (iss >> word) {
        bool containsBrokenLetter = false;

        // Check if the word contains any broken letters
        for (char c : word) {
            if (brokenLettersSet.find(c) != brokenLettersSet.end()) {
                containsBrokenLetter = true;
                break;
            }
        }

        // If the word does not contain any broken letters, increment the count
        if (!containsBrokenLetter) {
            count++;
        }
    }

    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of words in the `text` and $m$ is the average length of a word. This is because for each word, we are checking each character against the `brokenLettersSet`.
> - **Space Complexity:** $O(k)$, where $k$ is the length of `brokenLetters`. This is because we are creating a set of `brokenLetters`.
> - **Optimality proof:** This approach is optimal because we are reducing the time complexity of checking if a word contains any `brokenLetters` from $O(k)$ to $O(1)$, where $k$ is the length of `brokenLetters`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a set to reduce the time complexity of checking if a word contains any `brokenLetters`.
- Problem-solving patterns identified: Creating a set of `brokenLetters` to reduce the time complexity of checking if a word contains any `brokenLetters`.
- Optimization techniques learned: Using a set to reduce the time complexity of checking if a word contains any `brokenLetters`.
- Similar problems to practice: Problems that involve checking if a word contains any certain characters.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a word contains any `brokenLetters` before incrementing the count.
- Edge cases to watch for: Words that contain multiple `brokenLetters`, words that do not contain any `brokenLetters`.
- Performance pitfalls: Not using a set to reduce the time complexity of checking if a word contains any `brokenLetters`.
- Testing considerations: Testing the function with different inputs, including words that contain multiple `brokenLetters`, words that do not contain any `brokenLetters`, and empty strings.