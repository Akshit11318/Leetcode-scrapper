## Construct String with Repeat Limit
**Problem Link:** https://leetcode.com/problems/construct-string-with-repeat-limit/description

**Problem Statement:**
- Input: `repeatedLimit` (integer) and `repeatedString` (string)
- Output: Construct the lexicographically largest string by repeating `repeatedString` with a limit of `repeatedLimit` on any character's repetition.
- Key requirements and edge cases to consider: 
    - Handling cases where `repeatedString` is empty or `repeatedLimit` is 0.
    - Ensuring the constructed string does not exceed the repetition limit for any character.
    - Determining the lexicographically largest possible string under these constraints.
- Example test cases with explanations:
    - Given `repeatedLimit = 1` and `repeatedString = "deven"`, the lexicographically largest string is `"deven"` since we cannot repeat any character more than once.
    - Given `repeatedLimit = 2` and `repeatedString = "deven"`, the lexicographically largest string would consider repetition limits and string lexicographical order.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating over all possible combinations of characters from `repeatedString`, keeping track of the count of each character to ensure it does not exceed `repeatedLimit`.
- Step-by-step breakdown:
    1. Generate all permutations of characters from `repeatedString` up to a certain length (determined by `repeatedLimit` and the length of `repeatedString`).
    2. For each permutation, check if any character's count exceeds `repeatedLimit`.
    3. If not, compare this permutation lexicographically with the current maximum string found.
- Why this approach comes to mind first: It's a straightforward, exhaustive search approach that checks all possibilities.

```cpp
#include <iostream>
#include <string>
#include <map>

using namespace std;

string constructString(int repeatedLimit, string repeatedString) {
    string maxString = "";
    for (int len = 1; len <= repeatedString.length() * repeatedLimit; len++) {
        // Generate all permutations of the given length
        // This is a simplified representation; actual implementation would involve recursion or iteration
        for (auto perm : generatePermutations(repeatedString, len)) {
            map<char, int> charCount;
            bool exceedsLimit = false;
            for (char c : perm) {
                charCount[c]++;
                if (charCount[c] > repeatedLimit) {
                    exceedsLimit = true;
                    break;
                }
            }
            if (!exceedsLimit && perm > maxString) {
                maxString = perm;
            }
        }
    }
    return maxString;
}

// Simplified representation of generating permutations
// Actual implementation would be more complex
string generatePermutations(string str, int len) {
    // This function would generate all permutations of 'str' up to 'len' characters
    // and return them in a data structure for iteration.
}

int main() {
    int repeatedLimit = 2;
    string repeatedString = "deven";
    cout << constructString(repeatedLimit, repeatedString) << endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot m)$ where $n$ is the length of `repeatedString` and $m$ is the maximum length of the string we're constructing, which is bounded by `repeatedLimit * n`. This is because we're generating all permutations and checking each one.
> - **Space Complexity:** $O(n \cdot m)$ for storing the permutations and the character count map.
> - **Why these complexities occur:** The brute force approach involves generating and checking all possible strings, leading to high time and space complexities due to the combinatorial explosion of permutations.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves constructing the string character by character, ensuring that we always choose the lexicographically largest character from `repeatedString` that does not exceed the repetition limit.
- Detailed breakdown:
    1. Initialize an empty result string and a count map to track the repetition of each character.
    2. Iterate until we cannot add any more characters without exceeding the repetition limit or until we have added as many characters as possible.
    3. In each iteration, find the lexicographically largest character in `repeatedString` that has not exceeded its repetition limit.
    4. Add this character to the result string and increment its count in the map.
- Proof of optimality: This approach is optimal because it always chooses the lexicographically largest possible character at each step, ensuring the resulting string is the lexicographically largest possible under the given constraints.

```cpp
#include <iostream>
#include <string>
#include <map>

using namespace std;

string constructString(int repeatedLimit, string repeatedString) {
    string result = "";
    map<char, int> charCount;
    
    while (true) {
        char maxChar = '\0';
        for (char c : repeatedString) {
            if ((charCount[c] < repeatedLimit) && (c > maxChar)) {
                maxChar = c;
            }
        }
        if (maxChar == '\0') break; // No more characters can be added
        result += maxChar;
        charCount[maxChar]++;
    }
    return result;
}

int main() {
    int repeatedLimit = 2;
    string repeatedString = "deven";
    cout << constructString(repeatedLimit, repeatedString) << endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the length of `repeatedString` and $m$ is the maximum length of the string we're constructing, which is bounded by `repeatedLimit * n`. This is because we're potentially iterating over `repeatedString` for each character we add to the result.
> - **Space Complexity:** $O(n)$ for the character count map.
> - **Optimality proof:** This approach ensures the lexicographically largest string is constructed by always choosing the largest possible character that does not exceed the repetition limit, making it optimal.

---

### Final Notes

**Learning Points:**
- The importance of character counting and tracking in string manipulation problems.
- The concept of lexicographical ordering and how to achieve it in string construction.
- Optimization techniques to reduce complexity from brute force approaches.

**Mistakes to Avoid:**
- Not considering the repetition limit for each character.
- Failing to initialize and update the character count map correctly.
- Not checking for the termination condition (when no more characters can be added) in the optimal approach.