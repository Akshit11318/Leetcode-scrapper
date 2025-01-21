## Vowels of All Substrings
**Problem Link:** https://leetcode.com/problems/vowels-of-all-substrings/description

**Problem Statement:**
- Input: A string `word` containing only lowercase English letters.
- Constraints: The length of `word` is between 1 and 2 * 10^5.
- Expected output: An array of integers where the i-th integer is the number of vowels in all substrings starting with the i-th character.
- Key requirements: Count the vowels in all substrings starting with each character.
- Example test cases:
  - Input: "aba"
    - Output: [4, 3, 6]
    - Explanation: For "a", substrings are "a", "ab", "aba" with 1 + 1 + 2 = 4 vowels. For "b", substrings are "b", "ba" with 0 + 1 = 1 vowel. For "a", substrings are "a", "aba" with 1 + 2 = 3 vowels.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To solve this problem, we need to generate all possible substrings for each character and count the vowels in them.
- Step-by-step breakdown of the solution:
  1. Iterate over each character in the input string.
  2. For each character, generate all possible substrings starting with it.
  3. Count the vowels in each substring.
  4. Sum up the vowel counts for all substrings starting with the current character.

```cpp
vector<int> countVowels(string word) {
    vector<int> result;
    for (int i = 0; i < word.size(); i++) {
        int vowelCount = 0;
        for (int j = i; j < word.size(); j++) {
            string substring = word.substr(i, j - i + 1);
            for (char c : substring) {
                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                    vowelCount++;
                }
            }
        }
        result.push_back(vowelCount);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the length of the input string. This is because for each character, we generate all substrings and then for each substring, we count the vowels.
> - **Space Complexity:** $O(n)$ for storing the result and temporary substrings.
> - **Why these complexities occur:** The brute force approach involves generating all possible substrings for each character and then counting vowels in each, leading to a cubic time complexity due to nested loops.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: We can simplify the counting by observing the pattern of how vowels contribute to the total count for each starting character.
- Detailed breakdown of the approach:
  1. Initialize an array `result` of the same length as the input string.
  2. For each character in the input string, iterate over all substrings starting with it but instead of counting vowels in each substring, directly add the contribution of the current character to the result.
  3. If the current character is a vowel, its contribution to the total count for the starting character of the substring is equal to the number of substrings it is part of, which can be calculated as $(n - i)$ where $n$ is the length of the input string and $i$ is the index of the current character.

```cpp
vector<int> countVowels(string word) {
    int n = word.size();
    vector<int> result(n);
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            if (word[j] == 'a' || word[j] == 'e' || word[j] == 'i' || word[j] == 'o' || word[j] == 'u') {
                result[i] += n - j;
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of the input string. This is because for each character, we potentially iterate over the rest of the string once.
> - **Space Complexity:** $O(n)$ for storing the result.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to count the vowels in all substrings starting with each character, leveraging the fact that the contribution of a vowel to the count can be directly calculated based on its position.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and substring manipulation.
- Problem-solving patterns identified: Breaking down complex problems into simpler, more manageable parts.
- Optimization techniques learned: Reducing the number of operations by leveraging patterns and properties of the input data.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect loop bounds, missing or incorrect conditional statements.
- Edge cases to watch for: Empty input string, input string with only one character.
- Performance pitfalls: Using inefficient algorithms or data structures that lead to high time or space complexity.
- Testing considerations: Thoroughly testing the solution with various input cases, including edge cases.