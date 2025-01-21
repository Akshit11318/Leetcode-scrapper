## Adding Spaces to a String
**Problem Link:** https://leetcode.com/problems/adding-spaces-to-a-string/description

**Problem Statement:**
- Input format and constraints: The problem takes in a string `s` and an integer array `spaces` where `spaces[i]` is the position of the space in the string. The goal is to insert spaces into the string `s` according to the positions provided in the `spaces` array.
- Expected output format: The function should return a string with spaces inserted according to the positions in the `spaces` array.
- Key requirements and edge cases to consider: The input string `s` and the array `spaces` are non-empty. The positions in `spaces` are 1-indexed and sorted in ascending order.
- Example test cases with explanations: For example, given the string `s = "LeetcodeHelpsMe"` and `spaces = [8,13,15]`, the output should be `"Leetcode Helps Me"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate over the `spaces` array and insert a space into the string `s` at each position specified in the array.
- Step-by-step breakdown of the solution:
  1. Sort the `spaces` array in ascending order to ensure the positions are processed in the correct order.
  2. Initialize an empty result string.
  3. Iterate over the `spaces` array, and for each position, append the substring from the current position to the next position in the `spaces` array (or the end of the string if it's the last position) to the result string, preceded by a space if it's not the first substring.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it may not be the most efficient due to the string concatenation operations.

```cpp
string addSpaces(string s, vector<int>& spaces) {
    string result = "";
    int prev = 0;
    for (int i = 0; i < spaces.size(); i++) {
        result += s.substr(prev, spaces[i] - prev) + " ";
        prev = spaces[i];
    }
    result += s.substr(prev);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of the string `s` and $m$ is the number of positions in the `spaces` array. This is because we are iterating over the `spaces` array and performing string concatenation operations.
> - **Space Complexity:** $O(n + m)$, where $n$ is the length of the string `s` and $m` is the number of positions in the `spaces` array. This is because we are creating a new string with the spaces inserted.
> - **Why these complexities occur:** The time complexity occurs because we are iterating over the `spaces` array and performing string concatenation operations, which can be expensive. The space complexity occurs because we are creating a new string with the spaces inserted.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of using string concatenation, we can use a `StringBuilder` or a `string` with `reserve` to avoid reallocations and improve performance.
- Detailed breakdown of the approach:
  1. Initialize a `string` with the same length as the original string plus the number of positions in the `spaces` array.
  2. Iterate over the `spaces` array, and for each position, append the substring from the current position to the next position in the `spaces` array (or the end of the string if it's the last position) to the result string, preceded by a space if it's not the first substring.
- Proof of optimality: This approach is optimal because it avoids the overhead of string concatenation and uses a single pass over the `spaces` array.
- Why further optimization is impossible: This approach has a time complexity of $O(n + m)$, which is the best possible time complexity for this problem because we must iterate over the `spaces` array and the string `s`.

```cpp
string addSpaces(string s, vector<int>& spaces) {
    string result;
    result.reserve(s.length() + spaces.size());
    int prev = 0;
    for (int i = 0; i < spaces.size(); i++) {
        result += s.substr(prev, spaces[i] - prev);
        result += ' ';
        prev = spaces[i];
    }
    result += s.substr(prev);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of the string `s` and $m$ is the number of positions in the `spaces` array.
> - **Space Complexity:** $O(n + m)$, where $n$ is the length of the string `s` and $m$ is the number of positions in the `spaces` array.
> - **Optimality proof:** This approach is optimal because it uses a single pass over the `spaces` array and the string `s`, and it avoids the overhead of string concatenation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: String manipulation, iteration over arrays, and optimization techniques.
- Problem-solving patterns identified: Using a `StringBuilder` or a `string` with `reserve` to avoid reallocations and improve performance.
- Optimization techniques learned: Avoiding string concatenation and using a single pass over the input data.
- Similar problems to practice: Problems involving string manipulation and optimization.

**Mistakes to Avoid:**
- Common implementation errors: Using string concatenation in a loop, which can lead to poor performance.
- Edge cases to watch for: Handling empty strings and arrays, and ensuring that the positions in the `spaces` array are valid.
- Performance pitfalls: Using string concatenation in a loop, which can lead to poor performance.
- Testing considerations: Testing the function with different input strings and arrays, and ensuring that the function handles edge cases correctly.