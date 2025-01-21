## Find the K-th Character in String Game II
**Problem Link:** https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/description

**Problem Statement:**
- Input format and constraints: Given a string `s`, an integer `k`, and a list of integers `indices`, where `s` is the initial string, `k` is the position of the character to find, and `indices` is a list of indices in the string `s` that will be used to generate new strings by concatenating `s` with a substring of `s` starting at each index in `indices`.
- Expected output format: The `k-th` character in the resulting string after performing the string game.
- Key requirements and edge cases to consider: Handling cases where `k` exceeds the length of the initial string, ensuring correct indexing, and managing the growth of the string.
- Example test cases with explanations: For instance, given `s = "abc"`, `k = 4`, and `indices = [0, 1, 2]`, the string game would generate new strings by appending substrings of `s` starting at each index in `indices` to `s`, and we need to find the character at position `k` in the resulting string.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves simulating the string game by iteratively appending substrings of `s` starting at each index in `indices` to `s`, and then finding the `k-th` character in the resulting string.
- Step-by-step breakdown of the solution:
  1. Initialize the resulting string with `s`.
  2. For each index in `indices`, append the substring of `s` starting at the current index to the resulting string.
  3. Repeat step 2 until the length of the resulting string is greater than or equal to `k`.
  4. Return the character at position `k-1` in the resulting string.

```cpp
string kthCharacter(string s, int k, vector<int>& indices) {
    string result = s;
    while (result.size() < k) {
        for (int index : indices) {
            result += s.substr(index);
            if (result.size() >= k) break;
        }
    }
    return string(1, result[k-1]);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the length of `s`, $m$ is the number of indices, and $k$ is the target position. This is because in the worst case, we append substrings of `s` to the result for each index in `indices` until the result's length exceeds `k`.
> - **Space Complexity:** $O(n \cdot m \cdot k)$, as we store the resulting string which can grow up to a size of $n \cdot m \cdot k$ in the worst case.
> - **Why these complexities occur:** The time and space complexities are high due to the repeated appending of substrings to the result, which can lead to an exponential growth in the size of the resulting string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of actually appending the substrings to the result, we can keep track of the length of the resulting string and the character at position `k` without modifying the original string `s`. This is because the string game has a repetitive pattern.
- Detailed breakdown of the approach:
  1. Initialize the length of the resulting string with the length of `s`.
  2. For each index in `indices`, calculate the new length of the resulting string if we were to append the substring of `s` starting at the current index.
  3. If the new length exceeds `k`, we can determine the `k-th` character by considering the repetitive pattern of the string game.
- Proof of optimality: This approach is optimal because it avoids the unnecessary work of actually appending substrings to the result, reducing both time and space complexity significantly.

```cpp
string kthCharacter(string s, int k, vector<int>& indices) {
    int n = s.size();
    for (int index : indices) {
        if (k <= n) break;
        k -= n;
        n += s.size() - index;
    }
    return string(1, s[(k-1) % s.size()]);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m)$, where $m$ is the number of indices, because we only iterate through the indices once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the length of the resulting string and the character at position `k`.
> - **Optimality proof:** This approach is optimal because it reduces the problem to a simple iteration through the indices and a constant-time calculation to find the `k-th` character, achieving the best possible time and space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of recognizing patterns in string manipulation problems and the use of modular arithmetic to find characters in repetitive sequences.
- Problem-solving patterns identified: Looking for ways to avoid unnecessary work by using mathematical insights to reduce the problem size.
- Optimization techniques learned: Using mathematical properties of the problem to avoid explicit string manipulation.
- Similar problems to practice: Other string manipulation problems involving patterns or repetitive sequences.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect indexing, failure to handle edge cases, and inefficient use of string operations.
- Edge cases to watch for: Handling cases where `k` exceeds the length of the initial string, ensuring correct indexing, and managing the growth of the string.
- Performance pitfalls: Avoiding the brute force approach that leads to high time and space complexity.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases, to ensure correctness and efficiency.