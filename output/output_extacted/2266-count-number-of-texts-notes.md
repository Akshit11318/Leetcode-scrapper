## Count Number of Texts

**Problem Link:** https://leetcode.com/problems/count-number-of-texts/description

**Problem Statement:**
- Input: A string `pressedNumbers` representing the sequence of numbers pressed on a phone keypad.
- Constraints: The input string consists only of digits from 2 to 9.
- Expected Output: The number of possible texts that can be generated from the input sequence.
- Key Requirements: Consider the number of possible letters each digit can represent and calculate the total number of possible texts.
- Edge Cases: Empty input string, single-digit input, and sequences with varying lengths.
- Example Test Cases:
  - Input: "222" - Output: 3 (Possible texts: "aa", "ka", "kk")
  - Input: "23" - Output: 4 (Possible texts: "ad", "ae", "af", "bd", "be", "bf", "cd")

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible texts by considering each digit's possible letters and calculate the total count.
- Step-by-step breakdown of the solution:
  1. Define the number of possible letters for each digit.
  2. Initialize a counter for the total number of possible texts.
  3. Iterate through the input sequence, considering each digit's possible letters and update the counter accordingly.

```cpp
#include <string>
#include <unordered_map>

int countTextsBruteForce(const std::string& pressedNumbers) {
    if (pressedNumbers.empty()) return 0;

    std::unordered_map<char, int> digitToLetters = {
        {'2', 3}, {'3', 3}, {'4', 3}, {'5', 3}, {'6', 3}, {'7', 4}, {'8', 3}, {'9', 4}
    };

    int count = 1;
    for (char c : pressedNumbers) {
        count *= digitToLetters[c];
    }

    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we iterate through the string once.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the `digitToLetters` map and the `count` variable.
> - **Why these complexities occur:** The time complexity is linear due to the iteration through the input string, while the space complexity is constant because we use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same approach used in the brute force solution is already optimal, as we only need to iterate through the input sequence once to calculate the total number of possible texts.
- Detailed breakdown of the approach: The optimal solution remains the same as the brute force approach.
- Proof of optimality: Since we only need to consider each digit's possible letters once, the optimal time complexity is $O(n)$, where $n$ is the length of the input string.

```cpp
#include <string>
#include <unordered_map>

int countTextsOptimal(const std::string& pressedNumbers) {
    if (pressedNumbers.empty()) return 0;

    std::unordered_map<char, int> digitToLetters = {
        {'2', 3}, {'3', 3}, {'4', 3}, {'5', 3}, {'6', 3}, {'7', 4}, {'8', 3}, {'9', 4}
    };

    int count = 1;
    for (char c : pressedNumbers) {
        count *= digitToLetters[c];
    }

    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string, because we iterate through the string once.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the `digitToLetters` map and the `count` variable.
> - **Optimality proof:** The time complexity is optimal because we only need to iterate through the input string once, and the space complexity is optimal because we use a fixed amount of space regardless of the input size.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, multiplication, and lookup in a map.
- Problem-solving patterns identified: Using a map to store the number of possible letters for each digit.
- Optimization techniques learned: None, as the optimal solution is already achieved in the brute force approach.
- Similar problems to practice: Other problems involving iteration and multiplication, such as calculating the number of possible combinations.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle the empty input string case, or using the wrong data type for the `count` variable.
- Edge cases to watch for: Single-digit input, and sequences with varying lengths.
- Performance pitfalls: Using an inefficient data structure, such as a vector, to store the possible letters for each digit.
- Testing considerations: Testing the function with different input sequences, including empty strings and single-digit inputs.