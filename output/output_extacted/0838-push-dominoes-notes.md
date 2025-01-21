## Push Dominoes
**Problem Link:** https://leetcode.com/problems/push-dominoes/description

**Problem Statement:**
- Input format: A string `dominoes` representing the initial state of dominoes, where '.' represents a standing domino, 'L' represents a domino that has fallen to the left, and 'R' represents a domino that has fallen to the right.
- Constraints: `1 <= dominoes.length <= 500`
- Expected output format: A string representing the final state of the dominoes after they have all fallen.
- Key requirements and edge cases to consider:
  - A domino will fall to the left if it is adjacent to a domino that has fallen to the left.
  - A domino will fall to the right if it is adjacent to a domino that has fallen to the right.
  - If a domino is equidistant from a domino that has fallen to the left and a domino that has fallen to the right, it will remain standing.
- Example test cases with explanations:
  - Input: `".L.R...LR..L.."`
  - Output: `"LL.RR.LLRRLL.."`
  - Explanation: The dominoes will fall as follows:
    1. The domino at index 1 falls to the left, causing the domino at index 0 to fall to the left.
    2. The domino at index 3 falls to the right, causing the domino at index 4 to fall to the right.
    3. The dominoes at indices 5-7 remain standing because they are equidistant from the dominoes that have fallen to the left and right.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Simulate the falling of dominoes one by one, starting from the leftmost domino.
- Step-by-step breakdown of the solution:
  1. Initialize an array to store the final state of the dominoes.
  2. Iterate over the dominoes from left to right.
  3. For each domino, check if it has fallen to the left or right.
  4. If a domino has fallen, update the state of the adjacent dominoes accordingly.
  5. Repeat steps 2-4 until no more dominoes can fall.
- Why this approach comes to mind first: It is a straightforward and intuitive way to simulate the falling of dominoes.

```cpp
string pushDominoes(string dominoes) {
    int n = dominoes.length();
    string result = dominoes;
    while (true) {
        bool changed = false;
        string temp = result;
        for (int i = 0; i < n; i++) {
            if (result[i] == '.') {
                if (i > 0 && result[i-1] == 'L') {
                    temp[i] = 'L';
                    changed = true;
                }
                if (i < n-1 && result[i+1] == 'R') {
                    temp[i] = 'R';
                    changed = true;
                }
            }
        }
        result = temp;
        if (!changed) break;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of the input string and $m$ is the number of iterations until no more dominoes can fall.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string.
> - **Why these complexities occur:** The time complexity occurs because we are simulating the falling of dominoes one by one, and in the worst case, we may need to iterate over the dominoes $m$ times. The space complexity occurs because we need to store the final state of the dominoes.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use two pointers to track the positions of the dominoes that have fallen to the left and right.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `left` and `right`, to the start of the string.
  2. Iterate over the string, and for each character, check if it is 'L' or 'R'.
  3. If the character is 'L', update the `left` pointer to the current position.
  4. If the character is 'R', update the `right` pointer to the current position.
  5. If the `left` and `right` pointers are equidistant from the current position, update the character at the current position to '.'.
  6. Otherwise, update the character at the current position to 'L' if the `left` pointer is closer, or 'R' if the `right` pointer is closer.
- Proof of optimality: This approach is optimal because it only requires a single pass over the string, and it uses a constant amount of extra space to store the `left` and `right` pointers.

```cpp
string pushDominoes(string dominoes) {
    int n = dominoes.length();
    string result = dominoes;
    int left = -1;
    for (int right = 0; right < n; right++) {
        if (dominoes[right] == 'L') {
            left = right;
        } else if (dominoes[right] == 'R') {
            if (left == -1) {
                // If there is no 'L' on the left, all '.' will fall to the right
                for (int i = right - 1; i >= 0; i--) {
                    if (dominoes[i] == '.') {
                        result[i] = 'R';
                    } else {
                        break;
                    }
                }
            } else {
                // If there is an 'L' on the left, the '.' between 'L' and 'R' will be 'L' or 'R' based on the distance
                int mid = (left + right) / 2;
                for (int i = left + 1; i <= mid; i++) {
                    result[i] = 'L';
                }
                for (int i = mid + 1; i < right; i++) {
                    result[i] = 'R';
                }
            }
            left = -1;
        }
    }
    if (left != -1) {
        // If there is no 'R' on the right, all '.' will fall to the left
        for (int i = n - 1; i >= left; i--) {
            if (dominoes[i] == '.') {
                result[i] = 'L';
            } else {
                break;
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the string, and it uses a constant amount of extra space to store the `left` and `right` pointers.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two pointers, simulation.
- Problem-solving patterns identified: Divide and conquer, greedy algorithm.
- Optimization techniques learned: Using two pointers to reduce the time complexity.
- Similar problems to practice: Other problems that involve simulation or two pointers.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly.
- Edge cases to watch for: When the input string is empty or contains only one character.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Test the function with different input strings to ensure it works correctly.