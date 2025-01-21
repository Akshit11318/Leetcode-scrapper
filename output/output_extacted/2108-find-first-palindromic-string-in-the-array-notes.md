## Find First Palindromic String in the Array

**Problem Link:** https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description

**Problem Statement:**
- Input: An array of strings `words`.
- Constraints: `1 <= words.length <= 100`, `1 <= words[i].length <= 100`, `words[i]` consists of lowercase English letters.
- Expected Output: The first palindromic string in the array, or an empty string if no such string exists.
- Key Requirements: A string is considered palindromic if it reads the same backward as forward.
- Edge Cases: The input array may contain no palindromic strings.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking each string in the array to see if it's a palindrome.
- We'll iterate over each string in the array and then check if it's the same when reversed.
- This approach comes to mind first because it directly addresses the problem statement without requiring additional insights.

```cpp
string firstPalindrome(vector<string>& words) {
    for (auto word : words) {
        string reversed = word;
        reverse(reversed.begin(), reversed.end());
        if (word == reversed) return word;
    }
    return "";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of words and $m$ is the maximum length of a word. This is because for each word, we potentially reverse the entire string.
> - **Space Complexity:** $O(m)$, as we create a reversed copy of each word. The space used does not grow with the number of words, only with the length of the longest word.
> - **Why these complexities occur:** The time complexity is dominated by the string reversal operation inside the loop over all words. The space complexity is due to creating a reversed copy of each word.

---

### Optimal Approach (Required)

**Explanation:**
- Instead of reversing the entire string and comparing, we can use two pointers starting from the beginning and end of the string and move towards the center.
- This approach avoids the unnecessary overhead of creating a reversed string and directly compares characters from the start and end.
- It's optimal because it minimizes the number of operations needed to check if a string is a palindrome.

```cpp
string firstPalindrome(vector<string>& words) {
    for (auto word : words) {
        int left = 0, right = word.size() - 1;
        bool isPalindrome = true;
        while (left < right) {
            if (word[left] != word[right]) {
                isPalindrome = false;
                break;
            }
            left++;
            right--;
        }
        if (isPalindrome) return word;
    }
    return "";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of words and $m$ is the maximum length of a word. This is because for each word, we potentially compare all characters.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the pointers and the boolean flag, regardless of the input size.
> - **Optimality proof:** This approach is optimal because it checks each character in each string exactly once, which is necessary to determine if a string is a palindrome. The space complexity is also optimal as it uses a constant amount of space.

---

### Final Notes

**Learning Points:**
- The importance of directly addressing the problem statement with a straightforward approach.
- The value of optimizing the initial approach by reducing unnecessary operations (e.g., string reversal).
- Understanding the trade-offs between different solutions, particularly in terms of time and space complexity.

**Mistakes to Avoid:**
- Assuming that creating a reversed copy of a string is the most efficient way to check for palindromes.
- Not considering the impact of string operations on time and space complexity.
- Failing to optimize the solution by reducing unnecessary operations.