## Maximum Font to Fit a Sentence in a Screen

**Problem Link:** https://leetcode.com/problems/maximum-font-to-fit-a-sentence-in-a-screen/description

**Problem Statement:**
- Input format and constraints: Given a `width`, `height`, `fontSize`, and a `sentence`, find the maximum font size that can fit the sentence within the given `width` and `height`.
- Expected output format: The maximum font size as an integer.
- Key requirements and edge cases to consider: The font size should be an integer, and the sentence should fit entirely within the given dimensions.
- Example test cases with explanations:
  - Input: `width = 10, height = 10, fontSize = 10, sentence = "abcdefghijklmnopqrstuvwxyz"`
  - Expected Output: `9`
  - Explanation: The maximum font size that can fit the sentence is `9` because at font size `10`, the sentence would exceed the given `width` or `height`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible font sizes starting from `1` and check if the sentence can fit within the given `width` and `height` at each size.
- Step-by-step breakdown of the solution:
  1. Iterate through all possible font sizes from `1` to `fontSize`.
  2. For each font size, calculate the total width and height required to display the sentence.
  3. Check if the calculated width and height are within the given `width` and `height`.
  4. If they are, update the maximum font size.
- Why this approach comes to mind first: It's a straightforward approach to check every possible font size until we find the maximum one that fits.

```cpp
int maxFontSize(int width, int height, int fontSize, string sentence) {
    int maxWidth = 0;
    int maxHeight = 0;
    for (int i = 1; i <= fontSize; i++) {
        // Assuming the width of a character is proportional to the font size
        int charWidth = i;
        // Calculate the total width required for the sentence at the current font size
        int totalWidth = sentence.length() * charWidth;
        // Check if the sentence can fit within the given width at the current font size
        if (totalWidth <= width) {
            maxWidth = i;
        }
        // Assuming the height of a character is proportional to the font size
        int charHeight = i;
        // Calculate the total height required for the sentence at the current font size
        int totalHeight = charHeight;
        // Check if the sentence can fit within the given height at the current font size
        if (totalHeight <= height) {
            maxHeight = i;
        }
    }
    return min(maxWidth, maxHeight);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the `fontSize`. This is because we are iterating through all possible font sizes.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the maximum font size.
> - **Why these complexities occur:** The time complexity is linear because we are checking each font size once, and the space complexity is constant because we only need to keep track of the maximum font size found so far.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking every font size, we can use a binary search approach to find the maximum font size that fits the sentence.
- Detailed breakdown of the approach:
  1. Initialize the minimum and maximum font sizes to `1` and `fontSize`, respectively.
  2. Perform a binary search between the minimum and maximum font sizes.
  3. For each mid font size, calculate the total width and height required to display the sentence.
  4. If the sentence can fit within the given `width` and `height` at the mid font size, update the minimum font size to be the mid font size plus one.
  5. Otherwise, update the maximum font size to be the mid font size minus one.
  6. Repeat steps 2-5 until the minimum font size is greater than the maximum font size.
- Proof of optimality: This approach is optimal because it uses a binary search to find the maximum font size, reducing the number of iterations required.

```cpp
int maxFontSize(int width, int height, int fontSize, string sentence) {
    int left = 1;
    int right = fontSize;
    int result = 0;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        // Calculate the total width required for the sentence at the current font size
        int totalWidth = sentence.length() * mid;
        // Calculate the total height required for the sentence at the current font size
        int totalHeight = mid;
        // Check if the sentence can fit within the given width and height at the current font size
        if (totalWidth <= width && totalHeight <= height) {
            result = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the `fontSize`. This is because we are using a binary search approach.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the maximum font size.
> - **Optimality proof:** The time complexity is logarithmic because we are reducing the search space by half at each iteration, and the space complexity is constant because we only need to keep track of the maximum font size found so far.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search and iteration.
- Problem-solving patterns identified: Using a binary search approach to find the maximum font size that fits the sentence.
- Optimization techniques learned: Reducing the number of iterations required to find the maximum font size.
- Similar problems to practice: Finding the maximum value that satisfies a given condition.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty sentence or a font size of zero.
- Edge cases to watch for: Handling cases where the sentence is too long or the font size is too large.
- Performance pitfalls: Using an inefficient algorithm, such as checking every font size individually.
- Testing considerations: Testing the function with different input values, including edge cases.