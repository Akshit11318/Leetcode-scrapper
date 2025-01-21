## Three Equal Parts

**Problem Link:** https://leetcode.com/problems/three-equal-parts/description

**Problem Statement:**
- Input format: A string `s` consisting of only `1`s and `0`s.
- Constraints: The length of `s` is a multiple of 3.
- Expected output format: An array of two integers `[i, j]` where `i` and `j` are the indices of the first and last characters of the middle part of `s` when divided into three equal parts. If it's not possible to divide `s` into three equal parts, return `[-1, -1]`.
- Key requirements and edge cases to consider:
  - The length of `s` must be a multiple of 3.
  - All three parts must be equal.
- Example test cases with explanations:
  - Input: `s = "10101"`, Output: `[-1, -1]` because it's not possible to divide `s` into three equal parts.
  - Input: `s = "000111000"`, Output: `[3, 12]` because the first and last indices of the middle part are 3 and 12 respectively.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of three equal parts and check if they are equal.
- Step-by-step breakdown of the solution:
  1. Calculate the length of each part by dividing the length of `s` by 3.
  2. Iterate over all possible start indices of the first part.
  3. For each start index, extract the three parts and check if they are equal.
- Why this approach comes to mind first: It's a straightforward approach that tries all possible combinations.

```cpp
vector<int> threeEqualParts(string s) {
    int n = s.length();
    int partLength = n / 3;
    for (int i = 0; i <= partLength; i++) {
        for (int j = i + partLength; j <= 2 * partLength; j++) {
            string part1 = s.substr(0, partLength);
            string part2 = s.substr(i, partLength);
            string part3 = s.substr(j, partLength);
            if (part1 == part2 && part2 == part3) {
                return {i, j + partLength - 1};
            }
        }
    }
    return {-1, -1};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of `s`. This is because we have two nested loops that iterate over the string.
> - **Space Complexity:** $O(n)$ because we are creating substrings of `s`.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of three equal parts, which results in a quadratic time complexity. The space complexity is linear because we are creating substrings of `s`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can calculate the total number of `1`s in `s` and check if it's a multiple of 3. If not, we can return `[-1, -1]` immediately.
- Detailed breakdown of the approach:
  1. Calculate the total number of `1`s in `s`.
  2. If the total number of `1`s is not a multiple of 3, return `[-1, -1]`.
  3. Initialize two pointers, one at the beginning of the first part and one at the end of the third part.
  4. Move the pointers towards each other until they meet.
  5. If the pointers meet at the same index, return the indices of the first and last characters of the middle part.
- Proof of optimality: This approach is optimal because it only needs to iterate over `s` once to calculate the total number of `1`s and then moves two pointers towards each other.

```cpp
vector<int> threeEqualParts(string s) {
    int n = s.length();
    int partLength = n / 3;
    int ones = 0;
    for (char c : s) {
        if (c == '1') ones++;
    }
    if (ones % 3 != 0) return {-1, -1};
    int first = -1, second = -1;
    int leftOnes = 0, rightOnes = ones;
    for (int i = 0; i < n; i++) {
        if (s[i] == '1') leftOnes++;
        rightOnes -= s[i] == '1' ? 1 : 0;
        if (leftOnes == ones / 3 && rightOnes == ones / 3) {
            first = i;
        }
        if (leftOnes == (ones / 3) * 2 && rightOnes == ones / 3) {
            second = i;
        }
    }
    if (first == -1 || second == -1) return {-1, -1};
    while (first < second) {
        if (s[first] != s[second]) return {-1, -1};
        first++;
        second++;
    }
    return {first - partLength, second};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of `s`. This is because we only need to iterate over `s` once to calculate the total number of `1`s and then move two pointers towards each other.
> - **Space Complexity:** $O(1)$ because we are only using a constant amount of space.
> - **Optimality proof:** This approach is optimal because it only needs to iterate over `s` once and then moves two pointers towards each other, resulting in a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, counting `1`s in a string.
- Problem-solving patterns identified: Checking if a string can be divided into three equal parts.
- Optimization techniques learned: Reducing the number of iterations by calculating the total number of `1`s first.
- Similar problems to practice: Finding the first and last indices of a substring in a string.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the total number of `1`s is a multiple of 3 before trying to divide the string into three equal parts.
- Edge cases to watch for: Empty string, string with no `1`s, string with only one `1`.
- Performance pitfalls: Using a brute force approach that tries all possible combinations of three equal parts.
- Testing considerations: Testing with different input sizes, testing with different numbers of `1`s in the string.