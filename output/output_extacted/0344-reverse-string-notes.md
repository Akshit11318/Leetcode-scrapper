## Reverse String

**Problem Link:** [https://leetcode.com/problems/reverse-string/description](https://leetcode.com/problems/reverse-string/description)

**Problem Statement:**
- Input format: A character array `s` of length `n`.
- Constraints: `1 <= s.length <= 10^5`.
- Expected output format: The input string `s` with its characters reversed.
- Key requirements and edge cases to consider: Handling strings with odd and even lengths, preserving the original string's case and special characters.
- Example test cases:
  - Input: `s = ["h","e","l","l","o"]`
    - Output: `["o","l","l","e","h"]`
  - Input: `s = ["H","a","n","n","a","h"]`
    - Output: `["h","a","n","n","a","H"]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a new array and fill it with characters from the input array in reverse order.
- Step-by-step breakdown of the solution:
  1. Initialize an empty array `result` of the same length as the input array `s`.
  2. Iterate over the input array `s` from the last character to the first.
  3. For each character, append it to the `result` array.
- Why this approach comes to mind first: It's a straightforward, intuitive way to reverse a string by creating a new array and filling it with characters in reverse order.

```cpp
void reverseString(vector<char>& s) {
    vector<char> result;
    for (int i = s.size() - 1; i >= 0; i--) {
        result.push_back(s[i]);
    }
    s = result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string `s`. This is because we're iterating over the input array once.
> - **Space Complexity:** $O(n)$, as we're creating a new array of the same length as the input array.
> - **Why these complexities occur:** The time complexity is linear because we're performing a constant amount of work for each character in the input array. The space complexity is also linear because we're creating a new array that's the same size as the input array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can reverse the string in-place by swapping characters from the beginning and end of the array, moving towards the center.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `left` and `right`, to the start and end of the input array `s`, respectively.
  2. While `left` is less than `right`, swap the characters at the `left` and `right` indices.
  3. Increment `left` and decrement `right` to move towards the center of the array.
- Proof of optimality: This approach is optimal because it only requires a single pass through the input array, resulting in a time complexity of $O(n)$, and it uses a constant amount of extra space, resulting in a space complexity of $O(1)$.

```cpp
void reverseString(vector<char>& s) {
    int left = 0;
    int right = s.size() - 1;
    while (left < right) {
        swap(s[left], s[right]);
        left++;
        right--;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string `s`. This is because we're performing a constant amount of work for each character in the input array.
> - **Space Complexity:** $O(1)$, as we're only using a constant amount of extra space to store the `left` and `right` pointers.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity and uses a constant amount of extra space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: In-place modification, two-pointer technique.
- Problem-solving patterns identified: Reversing a sequence by swapping elements from the beginning and end.
- Optimization techniques learned: Reducing space complexity by using a constant amount of extra space.
- Similar problems to practice: Reversing a linked list, rotating an array.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to increment or decrement the pointers, swapping the wrong elements.
- Edge cases to watch for: Handling strings with odd and even lengths, preserving the original string's case and special characters.
- Performance pitfalls: Using a non-constant amount of extra space, resulting in a higher space complexity.
- Testing considerations: Testing the function with strings of different lengths, including edge cases like empty strings and strings with a single character.