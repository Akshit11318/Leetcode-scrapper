## Sort Vowels in a String
**Problem Link:** https://leetcode.com/problems/sort-vowels-in-a-string/description

**Problem Statement:**
- Input: A string `s`.
- Output: The string `s` with all vowels sorted in ascending order.
- Constraints: The input string only contains lowercase English letters.
- Key requirements: Sort only the vowels in the string, leaving the consonants in their original positions.
- Example test cases:
  - Input: `"bac"` - Output: `"abc"`
  - Input: `"code"` - Output: `"ceod"`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Extract all vowels from the string, sort them, and then replace the original vowels in the string with the sorted ones.
- Step-by-step breakdown:
  1. Initialize an empty string `vowels` to store the vowels from the input string.
  2. Iterate through the input string to extract all vowels and append them to `vowels`.
  3. Sort the `vowels` string in ascending order.
  4. Initialize an empty string `result` to build the final sorted string.
  5. Initialize a pointer `vowelIndex` to track the current position in the sorted `vowels` string.
  6. Iterate through the input string again. If a character is a vowel, append the next vowel from the sorted `vowels` string to `result` and increment `vowelIndex`. If a character is not a vowel, append it to `result` as is.

```cpp
#include <algorithm>
#include <string>

string sortVowels(string s) {
    string vowels = "";
    for (char c : s) {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            vowels += c;
        }
    }
    sort(vowels.begin(), vowels.end());
    string result = "";
    int vowelIndex = 0;
    for (char c : s) {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            result += vowels[vowelIndex++];
        } else {
            result += c;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of vowels in the string, due to the sorting operation.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string, for storing the vowels and the result.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and storing the vowels and the result requires additional space.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of sorting the vowels separately, we can use two pointers to swap the vowels in place, thus avoiding the need for extra space to store the sorted vowels.
- Detailed breakdown:
  1. Initialize two pointers, `left` and `right`, to the start and end of the string, respectively.
  2. Move the `left` pointer to the right until it points to a vowel.
  3. Move the `right` pointer to the left until it points to a vowel.
  4. If the vowel at the `left` pointer is greater than the vowel at the `right` pointer, swap them.
  5. Repeat steps 2-4 until the `left` pointer meets or crosses the `right` pointer.

```cpp
string sortVowels(string s) {
    int left = 0;
    int right = s.length() - 1;
    while (left < right) {
        while (left < right && !isVowel(s[left])) left++;
        while (left < right && !isVowel(s[right])) right--;
        if (s[left] > s[right]) {
            swap(s[left], s[right]);
        }
        left++;
        right--;
    }
    return s;
}

bool isVowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, as we potentially visit each character twice.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output, as we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the string and uses no additional space that scales with input size.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, in-place swapping.
- Problem-solving patterns identified: Avoiding unnecessary space usage, optimizing time complexity by reducing operations.
- Optimization techniques learned: Using two pointers to swap elements in place, minimizing the number of passes through the data.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as an empty string or a string with no vowels.
- Edge cases to watch for: Strings with repeated vowels, strings with vowels at the beginning or end.
- Performance pitfalls: Using inefficient sorting algorithms or data structures that lead to high time or space complexity.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases, to ensure correctness and efficiency.