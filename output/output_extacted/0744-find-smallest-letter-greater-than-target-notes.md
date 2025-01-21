## Find Smallest Letter Greater Than Target
**Problem Link:** https://leetcode.com/problems/find-smallest-letter-greater-than-target/description

**Problem Statement:**
- Input: A sorted array of lowercase English letters `letters` and a target letter `target`.
- Constraints: The array `letters` contains at least 2 distinct letters, all letters are lowercase, and `target` is a lowercase letter.
- Expected Output: Find the smallest letter in `letters` that is lexicographically greater than `target`.
- Key Requirements and Edge Cases:
  - If no such letter exists, return the first letter in `letters`.
  - The array `letters` may contain duplicate letters.
- Example Test Cases:
  - Input: `letters = ["c", "f", "j"]`, `target = "a"`
    Output: `"c"`
  - Input: `letters = ["c", "f", "j"]`, `target = "d"`
    Output: `"f"`
  - Input: `letters = ["c", "f", "j"]`, `target = "j"`
    Output: `"c"`

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to iterate through the array `letters` and find the first letter that is lexicographically greater than `target`.
- This approach comes to mind first because it directly addresses the problem statement.

```cpp
char nextGreatestLetter(vector<char>& letters, char target) {
    for (char letter : letters) {
        if (letter > target) {
            return letter;
        }
    }
    return letters[0]; // If no greater letter is found, return the first letter
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in `letters`, because we potentially iterate through all elements in the array once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the current letter being compared.
> - **Why these complexities occur:** The time complexity is linear because we iterate through the array, and the space complexity is constant because we do not allocate any additional space that scales with input size.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a binary search approach to find the smallest letter greater than `target`.
- This is because `letters` is sorted, allowing us to leverage the properties of binary search for efficiency.
- We initialize two pointers, `left` and `right`, to the start and end of the array, respectively.
- We then perform a binary search, adjusting the pointers based on whether the middle element is greater than `target`.

```cpp
char nextGreatestLetter(vector<char>& letters, char target) {
    int left = 0, right = letters.size();
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (letters[mid] <= target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return letters[left % letters.size()]; // Return the smallest letter greater than target, or the first letter if no greater letter exists
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the number of elements in `letters`, because we use a binary search approach that halves the search space with each iteration.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the pointers and the target.
> - **Optimality proof:** This is optimal because we take advantage of the sorted nature of the input array, allowing us to find the smallest letter greater than `target` in logarithmic time.

---

### Final Notes

**Learning Points:**
- The importance of recognizing sorted input and leveraging binary search for efficiency.
- Understanding how to adjust binary search to find the first occurrence of an element greater than a target.
- Recognizing the need to handle edge cases, such as when no greater letter exists.

**Mistakes to Avoid:**
- Not taking advantage of the sorted input, leading to a brute force approach.
- Failing to handle edge cases properly, such as returning the first letter when no greater letter exists.
- Incorrectly implementing binary search, leading to incorrect results or inefficiencies.