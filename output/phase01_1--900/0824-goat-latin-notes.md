## Goat Latin
**Problem Link:** https://leetcode.com/problems/goat-latin/description

**Problem Statement:**
- Input format: A string `s` containing a sequence of words.
- Constraints: $1 \leq \text{number of words} \leq 100$, $1 \leq \text{length of each word} \leq 30$.
- Expected output format: A modified string where each word is translated into `Goat Latin`.
- Key requirements and edge cases to consider: The rules for translating a word into `Goat Latin` are as follows:
  - If the word begins with a vowel (one of 'a', 'e', 'i', 'o', 'u'), you just add "ma" to the end of the word.
  - If the word begins with a consonant (i.e. not a vowel), you move all of the first consonant (or consonants, if the word begins with multiple consonants) to the end of the word and add "ma".
  - You then add one letter 'a' to the end of each word per its word position in the sentence, starting with 1.
- Example test cases with explanations:
  - Input: `"The quick brown fox jumped over the lazy dog"`
  - Expected Output: `"Imaa peaks oatenlmlab agooatb ma fooba mooba looba aalphz hoomelooma i"`


### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating through each word in the input string, applying the rules of `Goat Latin` to each word, and then combining the translated words back into a single string.
- Step-by-step breakdown of the solution:
  1. Split the input string into individual words.
  2. For each word, check if it starts with a vowel or a consonant.
  3. Apply the `Goat Latin` translation rules based on whether the word starts with a vowel or a consonant.
  4. Add the appropriate number of 'a's to the end of each word based on its position in the sentence.
  5. Combine the translated words back into a single string.

```cpp
class Solution {
public:
    string toGoatLatin(string s) {
        vector<string> words;
        string word;
        // Split the input string into words
        for (char c : s) {
            if (c == ' ') {
                words.push_back(word);
                word.clear();
            } else {
                word += c;
            }
        }
        words.push_back(word);
        
        for (int i = 0; i < words.size(); i++) {
            string translatedWord;
            // Check if the word starts with a vowel
            if (isVowel(words[i][0])) {
                translatedWord = words[i] + "ma";
            } else {
                // Move the first consonant(s) to the end and add "ma"
                int j = 0;
                while (j < words[i].size() && !isVowel(words[i][j])) {
                    j++;
                }
                translatedWord = words[i].substr(j) + words[i].substr(0, j) + "ma";
            }
            // Add the appropriate number of 'a's
            for (int k = 0; k <= i; k++) {
                translatedWord += 'a';
            }
            words[i] = translatedWord;
        }
        
        string result;
        for (string w : words) {
            result += w + " ";
        }
        // Remove the trailing space
        result.pop_back();
        return result;
    }
    
    bool isVowel(char c) {
        string vowels = "aeiouAEIOU";
        return vowels.find(c) != string::npos;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of words in the input string and $m$ is the maximum length of a word. This is because we iterate through each character in each word.
> - **Space Complexity:** $O(n \cdot m)$, as we need to store the translated words.
> - **Why these complexities occur:** The time complexity is due to the iteration through each character in each word, and the space complexity is due to the storage of the translated words.


### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is essentially the same as the brute force approach, as we must iterate through each word and apply the translation rules. However, we can make some minor optimizations to the code.
- Detailed breakdown of the approach:
  1. Split the input string into individual words using a `istringstream`.
  2. For each word, check if it starts with a vowel or a consonant.
  3. Apply the `Goat Latin` translation rules based on whether the word starts with a vowel or a consonant.
  4. Add the appropriate number of 'a's to the end of each word based on its position in the sentence.
  5. Combine the translated words back into a single string.

```cpp
class Solution {
public:
    string toGoatLatin(string s) {
        istringstream iss(s);
        string word, result;
        int count = 1;
        while (iss >> word) {
            if (isVowel(word[0])) {
                word += "ma";
            } else {
                word = word.substr(1) + word[0] + "ma";
            }
            word += string(count, 'a');
            result += word + " ";
            count++;
        }
        result.pop_back();
        return result;
    }
    
    bool isVowel(char c) {
        string vowels = "aeiouAEIOU";
        return vowels.find(tolower(c)) != string::npos;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of words in the input string and $m$ is the maximum length of a word.
> - **Space Complexity:** $O(n \cdot m)$, as we need to store the translated words.
> - **Optimality proof:** This is the optimal solution because we must iterate through each word and apply the translation rules. The use of an `istringstream` to split the input string into words is more efficient than manually splitting the string.


### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: String manipulation, iteration, and conditional statements.
- Problem-solving patterns identified: The use of a brute force approach to develop an initial solution, followed by optimization and refinement.
- Optimization techniques learned: The use of `istringstream` to split the input string into words, and the optimization of conditional statements.

**Mistakes to Avoid:**
- Common implementation errors: Failure to handle edge cases, such as empty input strings or words that start with multiple consonants.
- Edge cases to watch for: Words that start with vowels or consonants, and the correct application of the `Goat Latin` translation rules.
- Performance pitfalls: Inefficient string manipulation and iteration.
- Testing considerations: Thorough testing of the solution with various input strings and edge cases.