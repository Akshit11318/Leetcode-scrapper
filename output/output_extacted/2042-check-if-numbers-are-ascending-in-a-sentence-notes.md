## Check if Numbers Are Ascending in a Sentence

**Problem Link:** https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/description

**Problem Statement:**
- Input format: a string `s` containing a sentence with numbers.
- Constraints: `1 <= s.length <= 10^5`, `s` consists of lowercase letters and integers from `0` to `9`.
- Expected output format: a boolean indicating whether numbers in the sentence are in ascending order.
- Key requirements and edge cases to consider:
  - Numbers can be single-digit or multi-digit.
  - Non-numeric characters should be ignored.
  - If there are no numbers, the function should return `True`.
- Example test cases with explanations:
  - `s = "1 box has 3 pencils"` should return `True` because numbers are in ascending order.
  - `s = "1 box has 1 pencils"` should return `False` because numbers are not in ascending order.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Extract all numbers from the sentence, store them in a list, and then check if the list is sorted in ascending order.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list `numbers` to store the extracted numbers.
  2. Iterate through each character in the sentence.
  3. If the character is a digit, extract the number by continuously checking the next characters until a non-digit character is found.
  4. Add the extracted number to the `numbers` list.
  5. After iterating through the entire sentence, check if the `numbers` list is sorted in ascending order.
- Why this approach comes to mind first: It's a straightforward and intuitive method to solve the problem by explicitly extracting and comparing numbers.

```cpp
bool areNumbersAscending(string s) {
    vector<int> numbers;
    string currentNumber = "";
    
    for (char c : s) {
        if (isdigit(c)) {
            currentNumber += c;
        } else if (!currentNumber.empty()) {
            numbers.push_back(stoi(currentNumber));
            currentNumber.clear();
        }
    }
    
    if (!currentNumber.empty()) {
        numbers.push_back(stoi(currentNumber));
    }
    
    for (int i = 1; i < numbers.size(); i++) {
        if (numbers[i] <= numbers[i - 1]) {
            return false;
        }
    }
    
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the sentence, because we iterate through the sentence once to extract numbers and then potentially once more to check if the numbers are in ascending order.
> - **Space Complexity:** $O(m)$, where $m$ is the number of numbers in the sentence, because we store the extracted numbers in a list.
> - **Why these complexities occur:** The time complexity is linear due to the iteration through the sentence and potential comparison of numbers. The space complexity is directly related to the number of numbers found in the sentence.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of storing all numbers and then checking if they are in ascending order, we can keep track of the last seen number and immediately return `false` if a number is not greater than the last seen number.
- Detailed breakdown of the approach:
  1. Initialize a variable `lastNumber` to negative infinity to ensure the first number is always greater.
  2. Iterate through each character in the sentence, extracting numbers as before.
  3. For each extracted number, check if it is greater than the `lastNumber`. If not, return `false`.
  4. Update `lastNumber` with the current number.
- Proof of optimality: This approach has the same time complexity as the brute force but reduces the space complexity to constant because we only need to keep track of the last seen number.

```cpp
bool areNumbersAscending(string s) {
    int lastNumber = INT_MIN;
    string currentNumber = "";
    
    for (char c : s) {
        if (isdigit(c)) {
            currentNumber += c;
        } else if (!currentNumber.empty()) {
            int current = stoi(currentNumber);
            if (current <= lastNumber) {
                return false;
            }
            lastNumber = current;
            currentNumber.clear();
        }
    }
    
    if (!currentNumber.empty()) {
        int current = stoi(currentNumber);
        if (current <= lastNumber) {
            return false;
        }
    }
    
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the sentence, because we still iterate through the sentence once.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the last seen number and the current number being extracted.
> - **Optimality proof:** This is optimal because we cannot reduce the time complexity below linear without skipping the extraction of numbers, which is necessary to solve the problem. The space complexity is constant, which is the best we can achieve for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional checks, and the importance of optimizing space complexity.
- Problem-solving patterns identified: The need to consider edge cases, such as an empty sentence or a sentence with no numbers.
- Optimization techniques learned: Reducing space complexity by minimizing the storage of intermediate results.
- Similar problems to practice: Other string manipulation and comparison problems.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as an empty string or a string with leading or trailing spaces.
- Edge cases to watch for: Sentences with very large numbers, sentences with numbers at the beginning or end, and sentences with non-numeric characters.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to high time or space complexity.
- Testing considerations: Thoroughly testing the function with a variety of inputs, including edge cases and boundary conditions.