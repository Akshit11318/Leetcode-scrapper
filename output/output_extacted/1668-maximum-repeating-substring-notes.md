## Maximum Repeating Substring
**Problem Link:** https://leetcode.com/problems/maximum-repeating-substring/description

**Problem Statement:**
- Input format: Two strings `sequence` and `word`.
- Constraints: `1 <= sequence.length <= 100`, `1 <= word.length <= 100`, `sequence` and `word` consist of lowercase English letters.
- Expected output format: The maximum number of times a substring can be repeated in the given sequence.
- Key requirements and edge cases to consider: Handling cases where the word does not repeat in the sequence, and when the sequence is shorter than the word.
- Example test cases with explanations:
  - Example 1: sequence = "ababc", word = "ab" -> Output: 2 (because "abab" is a substring of "ababc").
  - Example 2: sequence = "ababc", word = "ba" -> Output: 1 (because "ba" is a substring of "ababc").
  - Example 3: sequence = "ababc", word = "ac" -> Output: 0 (because "acac" is not a substring of "ababc").

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible repeated substring of the given word to see if it's a substring of the sequence.
- Step-by-step breakdown of the solution:
  1. Initialize a variable to keep track of the maximum repetitions found so far.
  2. Loop through each possible repetition of the word, starting from 1 repetition up to a point where the repeated word is longer than the sequence.
  3. For each repetition, check if the repeated word is a substring of the sequence.
  4. If it is, update the maximum repetitions found.
- Why this approach comes to mind first: It directly addresses the problem by checking all possible scenarios of word repetition.

```cpp
int maxRepeating(string sequence, string word) {
    int maxRepetitions = 0;
    string repeatedWord = word;
    while (repeatedWord.length() <= sequence.length()) {
        if (sequence.find(repeatedWord) != string::npos) {
            maxRepetitions++;
            repeatedWord += word;
        } else {
            break;
        }
    }
    return maxRepetitions;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the length of the sequence and $m$ is the length of the word. This is because in the worst case, we might need to check every character in the sequence for every repetition of the word.
> - **Space Complexity:** $O(m)$ for storing the repeated word.
> - **Why these complexities occur:** The time complexity is due to the string search operation inside a loop that potentially runs up to the length of the sequence. The space complexity is due to the storage of the repeated word.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same as the brute force approach, but with a more efficient implementation by directly building the repeated word and checking if it's a substring of the sequence without unnecessary iterations.
- Detailed breakdown of the approach:
  1. Initialize a variable to store the maximum repetitions.
  2. Initialize a string to store the repeated word, starting with the word itself.
  3. Loop until the repeated word is longer than the sequence.
  4. Inside the loop, check if the sequence contains the repeated word.
  5. If it does, increment the repetition count and append the word to the repeated word.
  6. If not, break out of the loop since further repetitions will only make the repeated word longer and less likely to be a substring.
- Proof of optimality: This approach is optimal because it directly checks for the condition specified in the problem (whether a repeated word is a substring of the sequence) without any unnecessary steps.

```cpp
int maxRepeating(string sequence, string word) {
    int count = 0;
    string repeatedWord = word;
    while (sequence.find(repeatedWord) != string::npos) {
        count++;
        repeatedWord += word;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the length of the sequence and $m$ is the length of the word. This is because we're potentially searching for the repeated word in the sequence up to $n/m$ times.
> - **Space Complexity:** $O(m)$ for storing the repeated word.
> - **Optimality proof:** This is the most straightforward and efficient way to solve the problem, as it directly checks the condition without any unnecessary iterations or computations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: String manipulation, substring searching.
- Problem-solving patterns identified: Directly addressing the problem statement with minimal complexity.
- Optimization techniques learned: Avoiding unnecessary iterations and computations.
- Similar problems to practice: Other string manipulation and pattern searching problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as when the word is longer than the sequence.
- Edge cases to watch for: When the sequence or word is empty, or when the word does not repeat in the sequence.
- Performance pitfalls: Using inefficient string searching algorithms or unnecessarily repeating computations.
- Testing considerations: Thoroughly testing with various inputs, including edge cases.