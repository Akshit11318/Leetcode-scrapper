## Guess the Word
**Problem Link:** [https://leetcode.com/problems/guess-the-word/description](https://leetcode.com/problems/guess-the-word/description)

**Problem Statement:**
- Input format and constraints: Master has a secret word, and you are trying to guess it. The secret word is a 6-letter word, and you can make up to 10 guesses. After each guess, the master will give you a hint, which is a string of 6 characters, where:
  - `0` means the corresponding character in your guess is not in the secret word.
  - `1` means the corresponding character in your guess is in the secret word, but not at the correct position.
  - `2` means the corresponding character in your guess is in the secret word and at the correct position.
- Expected output format: You should return a string, which is the secret word.
- Key requirements and edge cases to consider: You can only make up to 10 guesses. If you use up all your guesses, you should return the last guess.
- Example test cases with explanations:
  - If the secret word is "acckzz", and you guess "cccoyy", the master will give you a hint "0110zz".

### Brute Force Approach

**Explanation:**
- Initial thought process: We can try all possible combinations of 6-letter words and make a guess.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of 6-letter words.
  2. Make a guess and get the hint from the master.
  3. Use the hint to narrow down the possible combinations.
  4. Repeat steps 2 and 3 until we find the secret word or use up all our guesses.
- Why this approach comes to mind first: It's a straightforward approach, but it's not efficient.

```cpp
class Solution {
public:
    void findSecretWord(vector<string>& wordlist, Master& master) {
        for (int i = 0; i < 10; i++) {
            string guess = wordlist[0];
            int match = master.guess(guess);
            if (match == 6) {
                return;
            }
            vector<string> possibleWords;
            for (string word : wordlist) {
                if (matchWord(guess, word) == match) {
                    possibleWords.push_back(word);
                }
            }
            wordlist = possibleWords;
        }
    }

    int matchWord(string word1, string word2) {
        int match = 0;
        for (int i = 0; i < 6; i++) {
            if (word1[i] == word2[i]) {
                match++;
            }
        }
        return match;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(10 \times 2^{6 \times 26})$, where 10 is the maximum number of guesses, and $2^{6 \times 26}$ is the total number of possible combinations.
> - **Space Complexity:** $O(2^{6 \times 26})$, where we store all possible combinations.
> - **Why these complexities occur:** We are trying all possible combinations, which results in exponential time and space complexity.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a more efficient algorithm to narrow down the possible combinations.
- Detailed breakdown of the approach:
  1. Choose a word from the wordlist as the first guess.
  2. Get the hint from the master.
  3. Use the hint to narrow down the possible combinations.
  4. Choose the next guess from the remaining possible combinations.
  5. Repeat steps 2-4 until we find the secret word or use up all our guesses.
- Proof of optimality: This approach is optimal because we are using the most efficient way to narrow down the possible combinations.

```cpp
class Solution {
public:
    void findSecretWord(vector<string>& wordlist, Master& master) {
        for (int i = 0; i < 10; i++) {
            string guess = wordlist[0];
            int match = master.guess(guess);
            if (match == 6) {
                return;
            }
            vector<string> possibleWords;
            for (string word : wordlist) {
                if (matchWord(guess, word) == match) {
                    possibleWords.push_back(word);
                }
            }
            wordlist = possibleWords;
            if (wordlist.size() > 1) {
                string nextGuess = wordlist[0];
                int maxCount = 0;
                for (string word : wordlist) {
                    int count = 0;
                    for (string w : wordlist) {
                        if (matchWord(word, w) == 0) {
                            count++;
                        }
                    }
                    if (count > maxCount) {
                        maxCount = count;
                        nextGuess = word;
                    }
                }
                wordlist[0] = nextGuess;
            }
        }
    }

    int matchWord(string word1, string word2) {
        int match = 0;
        for (int i = 0; i < 6; i++) {
            if (word1[i] == word2[i]) {
                match++;
            }
        }
        return match;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(10 \times n^2)$, where $n$ is the number of words in the wordlist.
> - **Space Complexity:** $O(n)$, where we store the possible combinations.
> - **Optimality proof:** This approach is optimal because we are using the most efficient way to narrow down the possible combinations.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a more efficient algorithm to narrow down the possible combinations.
- Problem-solving patterns identified: Choosing the next guess from the remaining possible combinations.
- Optimization techniques learned: Using the hint to narrow down the possible combinations.
- Similar problems to practice: Guess Number Higher or Lower, Guess Number Higher or Lower II.

**Mistakes to Avoid:**
- Common implementation errors: Not using the hint to narrow down the possible combinations.
- Edge cases to watch for: Using up all the guesses.
- Performance pitfalls: Not choosing the next guess from the remaining possible combinations.
- Testing considerations: Testing the solution with different inputs and edge cases.