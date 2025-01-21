## Minimum Length of String After Deleting Similar Ends
**Problem Link:** https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/description

**Problem Statement:**
- Input format: A string `s` containing only lowercase letters.
- Constraints: `1 <= s.length <= 10^5`.
- Expected output format: The minimum length of `s` after deleting similar ends.
- Key requirements and edge cases to consider: 
  - The string can be empty after deletion.
  - Only the ends of the string can be deleted.
- Example test cases with explanations:
  - `s = "cabaabac"` should return `2` because we can delete `c` and `a` from the ends, resulting in `baab`.
  - `s = "aabccabba"` should return `1` because we can delete `a` and `b` from the ends, resulting in `c`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of deleting characters from the ends.
- Step-by-step breakdown of the solution:
  1. Initialize two pointers, one at the start and one at the end of the string.
  2. Compare the characters at the pointers.
  3. If they are the same, move the pointers towards the center of the string.
  4. If they are different, break the loop.
  5. After the loop, the remaining characters in the string represent the minimum length after deleting similar ends.

```cpp
class Solution {
public:
    int minimumLength(string s) {
        int left = 0, right = s.size() - 1;
        while (left < right) {
            if (s[left] == s[right]) {
                char c = s[left];
                while (left <= right && s[left] == c) left++;
                while (left <= right && s[right] == c) right--;
            } else {
                break;
            }
        }
        return right - left + 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because in the worst case, we might have to traverse the entire string.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the pointers and the character.
> - **Why these complexities occur:** The time complexity is linear because we are potentially scanning the entire string once, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

The provided brute force approach is actually the optimal solution for this problem. The key insight is to use two pointers, one at the start and one at the end, and move them towards the center of the string based on the comparison of the characters at the pointers. This approach ensures that we delete the maximum number of similar characters from the ends, resulting in the minimum length of the string.

```cpp
class Solution {
public:
    int minimumLength(string s) {
        int left = 0, right = s.size() - 1;
        while (left < right) {
            if (s[left] == s[right]) {
                char c = s[left];
                while (left <= right && s[left] == c) left++;
                while (left <= right && s[right] == c) right--;
            } else {
                break;
            }
        }
        return right - left + 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the pointers and the character.
> - **Optimality proof:** This approach is optimal because it ensures that we delete the maximum number of similar characters from the ends, resulting in the minimum length of the string. Any other approach would either not delete the maximum number of similar characters or would have a higher time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, string manipulation.
- Problem-solving patterns identified: Using two pointers to track the ends of a string, comparing characters and moving pointers accordingly.
- Optimization techniques learned: Minimizing the number of iterations by breaking the loop when the characters at the pointers are different.
- Similar problems to practice: Other string manipulation problems, such as palindrome checking or substring searching.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the base case where the string is empty, not handling the case where the characters at the pointers are different.
- Edge cases to watch for: Empty string, single-character string, string with all identical characters.
- Performance pitfalls: Using a brute force approach with a high time complexity, not optimizing the solution for the given constraints.
- Testing considerations: Testing the solution with different input strings, including edge cases and large inputs.