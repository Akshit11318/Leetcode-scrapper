## Truncate Sentence
**Problem Link:** https://leetcode.com/problems/truncate-sentence/description

**Problem Statement:**
- Input format and constraints: The problem takes a string `s` and an integer `k` as input, where `s` is the sentence to be truncated and `k` is the maximum number of words allowed in the truncated sentence.
- Expected output format: The function should return a string representing the truncated sentence.
- Key requirements and edge cases to consider:
  - The sentence can contain any number of words, and the words can be separated by one or more spaces.
  - If the sentence contains fewer than `k` words, the function should return the original sentence.
  - If the sentence contains more than `k` words, the function should truncate the sentence to the first `k` words.
- Example test cases with explanations:
  - `s = "Hello world", k = 1` -> "Hello"
  - `s = "Hello world", k = 2` -> "Hello world"
  - `s = "Hello world", k = 3` -> "Hello world"

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward approach is to split the sentence into words and then take the first `k` words.
- Step-by-step breakdown of the solution:
  1. Split the sentence into words using spaces as the delimiter.
  2. Check if the number of words is less than or equal to `k`. If so, return the original sentence.
  3. Otherwise, truncate the sentence to the first `k` words and return the result.
- Why this approach comes to mind first: This approach is the most intuitive way to solve the problem, as it directly addresses the requirement of truncating the sentence to the first `k` words.

```cpp
string truncateSentence(string s, int k) {
    istringstream iss(s);
    vector<string> words;
    string word;

    // Split the sentence into words
    while (iss >> word) {
        words.push_back(word);
    }

    // Check if the number of words is less than or equal to k
    if (words.size() <= k) {
        return s;
    }

    // Truncate the sentence to the first k words
    string truncatedSentence;
    for (int i = 0; i < k; i++) {
        truncatedSentence += words[i];
        if (i < k - 1) {
            truncatedSentence += " ";
        }
    }

    return truncatedSentence;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of words in the sentence, because we need to split the sentence into words and then iterate over the words to truncate the sentence.
> - **Space Complexity:** $O(n)$, because we need to store the words in a vector.
> - **Why these complexities occur:** The time complexity occurs because we need to iterate over the words in the sentence, and the space complexity occurs because we need to store the words in a vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `stringstream` to split the sentence into words and then take the first `k` words.
- Detailed breakdown of the approach:
  1. Use a `stringstream` to split the sentence into words.
  2. Take the first `k` words from the `stringstream`.
  3. Join the words back into a sentence using spaces as the delimiter.
- Proof of optimality: This approach is optimal because it only requires a single pass over the input sentence, and it uses a `stringstream` to split the sentence into words, which is an efficient operation.

```cpp
string truncateSentence(string s, int k) {
    istringstream iss(s);
    vector<string> words;
    string word;

    // Split the sentence into words
    for (int i = 0; i < k && iss >> word; i++) {
        words.push_back(word);
    }

    // Join the words back into a sentence
    string truncatedSentence;
    for (const auto& w : words) {
        truncatedSentence += w + " ";
    }

    // Remove the trailing space
    if (!truncatedSentence.empty()) {
        truncatedSentence.pop_back();
    }

    return truncatedSentence;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of words in the sentence, because we need to split the sentence into words and then iterate over the words to truncate the sentence.
> - **Space Complexity:** $O(k)$, because we only need to store the first `k` words in a vector.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the input sentence, and it uses a `stringstream` to split the sentence into words, which is an efficient operation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `stringstream` to split a sentence into words, and taking the first `k` words from a `stringstream`.
- Problem-solving patterns identified: Splitting a sentence into words and then taking the first `k` words.
- Optimization techniques learned: Using a `stringstream` to split a sentence into words, which is an efficient operation.
- Similar problems to practice: Truncating a sentence to a certain number of characters, or truncating a sentence to a certain number of words while preserving the original sentence structure.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the number of words is less than or equal to `k` before truncating the sentence.
- Edge cases to watch for: Handling empty sentences or sentences with only one word.
- Performance pitfalls: Using an inefficient algorithm to split the sentence into words, such as using a loop to iterate over the characters in the sentence.
- Testing considerations: Testing the function with different inputs, such as sentences with different numbers of words, and checking that the output is correct in each case.