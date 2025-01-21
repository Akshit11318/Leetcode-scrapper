## Rearranging Fruits
**Problem Link:** https://leetcode.com/problems/rearranging-fruits/description

**Problem Statement:**
- Input format and constraints: You are given a basket of `n` fruits, where each fruit is either an apple or a banana. The fruits are represented by a string `position`, where `'a'` denotes an apple and `'b'` denotes a banana.
- Expected output format: Determine if you can make the fruits in the basket _alternating_ between apples and bananas, and return the rearranged string if possible.
- Key requirements and edge cases to consider: The input string will only contain `'a'` and `'b'`. The length of the string will be in the range `[1, 100]`.
- Example test cases with explanations:
  - Input: `"aba"`
    - Output: `"aba"`
    - Explanation: The fruits are already alternating between apples and bananas.
  - Input: `"abba"`
    - Output: `""`
    - Explanation: The fruits cannot be rearranged to be alternating.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible permutations of the string and check if any of them are alternating.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the input string.
  2. For each permutation, check if the fruits are alternating.
  3. If a permutation is found that is alternating, return it.
- Why this approach comes to mind first: It's a straightforward approach that checks all possible solutions.

```cpp
#include <algorithm>
#include <string>

std::string rearrangingFruits(std::string position) {
    // Generate all permutations of the input string
    std::sort(position.begin(), position.end());
    do {
        // Check if the fruits are alternating
        bool alternating = true;
        for (int i = 1; i < position.size(); i++) {
            if (position[i] == position[i - 1]) {
                alternating = false;
                break;
            }
        }
        if (alternating) {
            return position;
        }
    } while (std::next_permutation(position.begin(), position.end()));
    return "";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the length of the input string. This is because we are generating all permutations of the string.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we need to store the input string and its permutations.
> - **Why these complexities occur:** The brute force approach has high time complexity because it generates all permutations of the input string, which is a time-consuming operation.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can count the number of apples and bananas in the input string and check if it's possible to make them alternating.
- Detailed breakdown of the approach:
  1. Count the number of apples and bananas in the input string.
  2. Check if the difference between the counts is more than 1. If it is, return an empty string.
  3. Otherwise, return a string that alternates between apples and bananas.
- Proof of optimality: This approach is optimal because it only requires a single pass through the input string to count the number of apples and bananas.

```cpp
std::string rearrangingFruits(std::string position) {
    int apples = 0, bananas = 0;
    for (char c : position) {
        if (c == 'a') {
            apples++;
        } else {
            bananas++;
        }
    }
    if (abs(apples - bananas) > 1) {
        return "";
    }
    std::string result;
    if (apples > bananas) {
        for (int i = 0; i < bananas; i++) {
            result += "ab";
        }
        result += "a";
    } else if (bananas > apples) {
        for (int i = 0; i < apples; i++) {
            result += "ba";
        }
        result += "b";
    } else {
        for (int i = 0; i < apples; i++) {
            result += "ab";
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we only need to make a single pass through the input string to count the number of apples and bananas.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we need to store the result string.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the input string to count the number of apples and bananas, and then constructs the result string in a single pass.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Counting, string manipulation, and optimization.
- Problem-solving patterns identified: Checking if a string can be rearranged to meet certain conditions.
- Optimization techniques learned: Reducing the time complexity of an algorithm by avoiding unnecessary operations.
- Similar problems to practice: Other string manipulation and counting problems.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, such as when the input string is empty or contains only one type of fruit.
- Edge cases to watch for: When the difference between the counts of apples and bananas is more than 1.
- Performance pitfalls: Using inefficient algorithms, such as generating all permutations of the input string.
- Testing considerations: Testing the function with different input strings, including edge cases.