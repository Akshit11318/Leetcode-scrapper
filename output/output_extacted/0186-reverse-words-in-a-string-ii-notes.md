## Reverse Words in a String II
**Problem Link:** https://leetcode.com/problems/reverse-words-in-a-string-ii/description

**Problem Statement:**
- Input: A character array `s` of size `n`.
- Constraints: `1 <= n <= 10^4`, `s` consists of only lowercase English letters and spaces.
- Expected Output: Reverse each word in `s` in-place.
- Key Requirements: 
    - Reverse the order of characters within each word.
    - Keep the order of the words themselves the same.
- Example Test Cases:
    - Input: `s = ["t","h","e"," ","w","o","r","l","d"]`
      Output: `["w","o","r","l","d"," ","t","h","e"]`
    - Input: `s = ["a"]`
      Output: `["a"]`

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to iterate over the array, identify each word, reverse it, and then place the reversed words back into the array while maintaining their original order.
- Step-by-step breakdown:
    1. Initialize two pointers to track the start and end of each word.
    2. When a space is encountered, reverse the word between the two pointers.
    3. After reversing all words, the array will contain the words in their original order but with each word's characters reversed.

```cpp
void reverseWords(vector<char>& s) {
    int start = 0;
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == ' ') {
            reverse(s.begin() + start, s.begin() + i);
            start = i + 1;
        }
    }
    // Reverse the last word
    reverse(s.begin() + start, s.end());
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the size of the input array `s`. This is because we potentially visit each character once to reverse the words.
> - **Space Complexity:** $O(1)$ as we are modifying the input array in-place and not using any additional space that scales with input size.
> - **Why these complexities occur:** The time complexity is linear because we make a single pass through the array, reversing words as we go. The space complexity is constant because we only use a fixed amount of space to store our pointers and other variables, regardless of the input size.

---

### Optimal Approach (Required)
**Explanation:**
- The optimal approach involves reversing the entire string first and then reversing each word individually. This approach ensures that the words are in their original order but with each word's characters reversed.
- Step-by-step breakdown:
    1. Reverse the entire input string `s`.
    2. Initialize two pointers to track the start and end of each word in the reversed string.
    3. When a space is encountered, reverse the word between the two pointers.
    4. After reversing all words, the array will contain the words in their original order but with each word's characters reversed.

```cpp
void reverseWords(vector<char>& s) {
    // Reverse the entire string
    reverse(s.begin(), s.end());
    
    int start = 0;
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == ' ') {
            reverse(s.begin() + start, s.begin() + i);
            start = i + 1;
        }
    }
    // Reverse the last word
    reverse(s.begin() + start, s.end());
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the size of the input array `s`. This is because we reverse the entire string and then reverse each word individually, both of which are linear operations.
> - **Space Complexity:** $O(1)$ as we are modifying the input array in-place and not using any additional space that scales with input size.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations needed to reverse each word in the string while maintaining their original order, achieving this in a single pass through the string after the initial reversal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Reversing strings and arrays, using pointers to track start and end indices of words.
- Problem-solving patterns identified: Breaking down complex string manipulation problems into simpler reversal operations.
- Optimization techniques learned: Minimizing the number of passes through the input data to achieve the desired transformation.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the last word correctly after reversing the entire string.
- Edge cases to watch for: Empty strings, strings with a single word, strings with multiple consecutive spaces.
- Performance pitfalls: Using inefficient algorithms that result in higher than necessary time complexities.
- Testing considerations: Ensure to test with various inputs, including edge cases and large inputs to verify correctness and performance.