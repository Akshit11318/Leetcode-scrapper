## Reconstruct Original Digits from English
**Problem Link:** https://leetcode.com/problems/reconstruct-original-digits-from-english/description

**Problem Statement:**
- Input format: A string `s` containing the English representation of digits from 0 to 9.
- Constraints: `s` consists of lowercase English letters only.
- Expected output format: The original digits in the order they were represented by the English words.
- Key requirements and edge cases to consider:
  - Each digit from 0 to 9 will be represented by its English word at most once.
  - The length of `s` is at most 1000.
- Example test cases with explanations:
  - Input: `s = "owoztneoer"`
    Output: `0`
    Explanation: The unique number words in the string are "zero".
  - Input: `s = "fviefuro"`
    Output: `45`
    Explanation: The unique number words in the string are "four", "five".

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a dictionary or a list of English words for each digit from 0 to 9, then try to find each word in the input string `s`.
- Step-by-step breakdown of the solution:
  1. Define a list of English words for digits.
  2. Iterate through each word and check if it exists in the string `s`.
  3. If a word is found, remove it from `s` and append the corresponding digit to the result.
- Why this approach comes to mind first: It directly addresses the problem by matching the English words with the digits they represent.

```cpp
#include <iostream>
#include <string>
#include <vector>

std::string originalDigits(std::string s) {
    std::string word[] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    int count[26] = {0};
    for (char c : s) count[c - 'a']++;
    
    std::string res;
    // Use unique letters to identify numbers
    if (count[25] > 0) { // 'z' is in "zero"
        int zeros = count[25];
        res += std::string(zeros, '0');
        // Remove 'z', 'e', 'r', 'o' for each "zero"
        count[25] = count[4] = count[17] = count[14] -= zeros;
    }
    if (count[20] > 0) { // 'w' is in "two"
        int twos = count[20];
        res += std::string(twos, '2');
        // Remove 't', 'w', 'o' for each "two"
        count[20] = count[19] = count[14] -= twos;
    }
    if (count[8] > 0) { // 'u' is in "four"
        int fours = count[8];
        res += std::string(fours, '4');
        // remove 'f', 'o', 'u', 'r' for each "four"
        count[8] = count[5] = count[14] = count[17] -= fours;
    }
    if (count[5] > 0) { // 'f' is in "five"
        int fives = count[5];
        res += std::string(fives, '5');
        // remove 'f', 'i', 'v', 'e' for each "five"
        count[5] = count[8] = count[21] = count[4] -= fives;
    }
    if (count[19] > 0) { // 't' is in "three" and "two" is removed
        int threes = count[19];
        res += std::string(threes, '3');
        // remove 't', 'h', 'r', 'e', 'e' for each "three"
        count[19] = count[7] = count[17] = count[4] -= threes;
    }
    if (count[18] > 0) { // 's' is in "six"
        int sixes = count[18];
        res += std::string(sixes, '6');
        // remove 's', 'i', 'x' for each "six"
        count[18] = count[8] = count[23] -= sixes;
    }
    if (count[2] > 0) { // 'g' is in "eight"
        int eights = count[2];
        res += std::string(eights, '8');
        // remove 'e', 'i', 'g', 'h', 't' for each "eight"
        count[2] = count[4] = count[7] = count[19] = count[20] -= eights;
    }
    if (count[4] > 0) { // 'i' is in "nine"
        int nines = count[4];
        res += std::string(nines, '9');
        // remove 'n', 'i', 'n', 'e' for each "nine"
        count[4] = count[13] = count[14] -= nines;
    }
    if (count[0] > 0) { // 'o' is in "one"
        int ones = count[0];
        res += std::string(ones, '1');
        // remove 'o', 'n', 'e' for each "one"
        count[0] = count[13] = count[4] -= ones;
    }
    
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`, because we're iterating through `s` once to count the letters and then process each unique digit word.
> - **Space Complexity:** $O(1)$, because we use a fixed amount of space to store the counts of letters and the result string.
> - **Why these complexities occur:** The time complexity is linear due to the iteration through `s`, and the space complexity is constant because we're using fixed-size arrays and a string of maximum length equal to `s`.

---

### Optimal Approach (Required)

The provided brute force approach is actually quite efficient and can be considered optimal for this problem because it directly addresses the requirements by identifying unique letters that correspond to specific digits. The key insight here is to use the unique letters in the English words for digits to determine their presence in the string `s`. This approach ensures that we can reconstruct the original digits from the English words with a linear time complexity.

**Explanation:**
- The optimal approach works by first counting the occurrences of each letter in `s`.
- Then, it iterates through the unique digit words in a specific order, checking for the presence of their unique letters.
- If a unique letter is found, it means the corresponding digit word is present in `s`, so we append the digit to the result and remove the letters of the digit word from the count.
- This process continues until all unique digit words have been checked.

The provided code in the brute force section is already implementing this optimal approach, making further optimization unnecessary.

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`.
> - **Space Complexity:** $O(1)$, because we're using a fixed amount of space.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the input string to count the letters and then a fixed number of operations to check for each unique digit word, resulting in a linear time complexity. The space complexity is constant, making it efficient for large inputs.