## Sentence Screen Fitting

**Problem Link:** https://leetcode.com/problems/sentence-screen-fitting/description

**Problem Statement:**
- Input format: Two parameters, `rows` and `cols`, representing the number of rows and columns on the screen, and a string `sentence` containing one or more sentences.
- Constraints: `1 <= rows <= 100`, `1 <= cols <= 2000`, `1 <= sentence.length <= 5000`.
- Expected output format: The number of times the sentence can fit on the screen.
- Key requirements and edge cases to consider: Handling sentences of varying lengths, wrapping sentences across rows, and counting the total number of times a sentence can be displayed on the screen.
- Example test cases with explanations: For example, given `rows = 2`, `cols = 8`, and `sentence = "hello world"`, the sentence can fit on the screen twice.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To simulate the process of writing the sentence on the screen row by row, handling the wrap-around to the next line when a sentence exceeds the column limit.
- Step-by-step breakdown of the solution:
  1. Initialize variables to track the current row and column positions.
  2. Split the sentence into words and iterate over them.
  3. For each word, check if adding it to the current row would exceed the column limit. If so, move to the next row.
  4. Keep track of how many times the sentence can be fully displayed on the screen.
- Why this approach comes to mind first: It directly simulates the process of fitting sentences onto a screen, making it intuitive but potentially inefficient due to its step-by-step nature.

```cpp
int wordsTyping(vector<string>& sentence, int rows, int cols) {
    int count = 0; // Count of full sentences displayed
    int row = 0;   // Current row
    int col = 0;   // Current column
    
    while (row < rows) {
        for (auto word : sentence) {
            if (col + word.size() + 1 <= cols) {
                col += word.size() + 1; // +1 for the space
            } else {
                row++;
                col = word.size();
                if (row >= rows) break;
            }
        }
        if (row >= rows) break;
        count++; // Increment count after a full sentence is displayed
        row++;
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot r)$, where $n$ is the number of words in a sentence, $m$ is the number of sentences, and $r$ is the number of rows. This is because in the worst case, we iterate over all words in all sentences for each row.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input, as we use a constant amount of space to store our variables.
> - **Why these complexities occur:** The time complexity is high because we simulate the writing process for each character in each word across all rows, leading to a multiplicative relationship between the number of words, sentences, and rows. The space complexity is low because we only use a fixed amount of space to store our counters and variables.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of simulating the writing process row by row, we can calculate how many times a sentence can fit into a row and then multiply this by the number of rows.
- Detailed breakdown of the approach:
  1. Calculate the total number of characters in a sentence, including spaces between words.
  2. Determine how many sentences can fit in one row by dividing the row length by the sentence length.
  3. Multiply the number of sentences that can fit in one row by the total number of rows to get the total count of sentences displayed.
- Proof of optimality: This approach is optimal because it directly calculates the maximum number of sentences that can fit on the screen without needing to simulate the writing process, reducing the time complexity significantly.
- Why further optimization is impossible: This approach already achieves the best possible time complexity by avoiding unnecessary iterations and directly calculating the result.

```cpp
int wordsTyping(vector<string>& sentence, int rows, int cols) {
    int sentenceLength = 0;
    for (auto word : sentence) {
        sentenceLength += word.size() + 1; // +1 for the space
    }
    sentenceLength -= 1; // Subtract 1 because there's no space after the last word
    
    int countPerRow = cols / sentenceLength;
    if (countPerRow == 0) return 0; // If a sentence cannot fit in a row
    
    return countPerRow * rows;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of words in a sentence. This is because we only need to iterate over the words once to calculate the sentence length.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store our variables.
> - **Optimality proof:** This solution is optimal because it achieves a linear time complexity with respect to the number of words in a sentence, which is the minimum required to process the input.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Simulation vs. direct calculation, optimization through avoiding unnecessary iterations.
- Problem-solving patterns identified: Identifying the key insight that leads to an optimal solution, such as calculating sentence fits per row.
- Optimization techniques learned: Avoiding simulation when direct calculation is possible, reducing time complexity by minimizing iterations.
- Similar problems to practice: Other problems involving fitting items into a limited space, such as packing problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as when a sentence cannot fit in a row.
- Edge cases to watch for: Handling sentences of varying lengths, ensuring correct calculation of sentence fits per row.
- Performance pitfalls: Using simulation when direct calculation is possible, leading to higher time complexities.
- Testing considerations: Thoroughly testing with different input sizes and edge cases to ensure correctness and performance.