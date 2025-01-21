## Split Message Based on Limit
**Problem Link:** https://leetcode.com/problems/split-message-based-on-limit/description

**Problem Statement:**
- Input format and constraints: The function takes a `message` string and a `limit` integer as input. The `message` string can be of any length, and the `limit` integer represents the maximum allowed length for each message part.
- Expected output format: The function should return a vector of strings, where each string represents a part of the original message, split according to the given limit.
- Key requirements and edge cases to consider: The function should handle cases where the message length is less than or equal to the limit, as well as cases where the message length exceeds the limit. It should also handle empty input strings and invalid limit values.
- Example test cases with explanations:
  - If the input message is "This is a test message" and the limit is 10, the output should be ["This is a", "test", "message"].
  - If the input message is "Short message" and the limit is 20, the output should be ["Short message"].

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over the input message character by character and checking if adding the current character to the current message part would exceed the limit. If it would exceed the limit, we add the current message part to the result vector and start a new message part with the current character.
- Step-by-step breakdown of the solution:
  1. Initialize an empty vector to store the message parts.
  2. Initialize an empty string to store the current message part.
  3. Iterate over each character in the input message.
  4. For each character, check if adding it to the current message part would exceed the limit.
  5. If it would exceed the limit, add the current message part to the result vector and start a new message part with the current character.
  6. If it would not exceed the limit, add the character to the current message part.
  7. After iterating over all characters, add the last message part to the result vector.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, as it involves simple string manipulation and iteration.

```cpp
vector<string> splitMessage(string message, int limit) {
    vector<string> result;
    string currentPart = "";
    
    for (char c : message) {
        if (currentPart.length() + 1 > limit) {
            result.push_back(currentPart);
            currentPart = "";
        }
        currentPart += c;
    }
    
    if (!currentPart.empty()) {
        result.push_back(currentPart);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input message. This is because we iterate over each character in the message once.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input message. This is because we store each message part in the result vector, which can contain up to $n$ characters in total.
> - **Why these complexities occur:** The time complexity occurs because we iterate over each character in the message, and the space complexity occurs because we store each message part in the result vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a similar approach to the brute force solution, but with some optimizations to reduce the number of iterations and string concatenations.
- Detailed breakdown of the approach:
  1. Initialize an empty vector to store the message parts.
  2. Initialize an empty string to store the current message part.
  3. Iterate over each character in the input message.
  4. For each character, check if adding it to the current message part would exceed the limit.
  5. If it would exceed the limit, add the current message part to the result vector and start a new message part with the current character.
  6. If it would not exceed the limit, add the character to the current message part.
  7. After iterating over all characters, add the last message part to the result vector.
- Proof of optimality: This approach is optimal because it involves a single pass over the input message and uses a minimal amount of extra memory to store the message parts.
- Why further optimization is impossible: Further optimization is impossible because we must iterate over each character in the message at least once to determine the message parts.

```cpp
vector<string> splitMessage(string message, int limit) {
    vector<string> result;
    string currentPart = "";
    
    for (char c : message) {
        if (currentPart.length() + 1 > limit) {
            result.push_back(currentPart);
            currentPart = "";
        }
        currentPart += c;
    }
    
    if (!currentPart.empty()) {
        result.push_back(currentPart);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input message. This is because we iterate over each character in the message once.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input message. This is because we store each message part in the result vector, which can contain up to $n$ characters in total.
> - **Optimality proof:** The time complexity is optimal because we must iterate over each character in the message at least once to determine the message parts. The space complexity is also optimal because we must store each message part in the result vector.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: string manipulation, iteration, and dynamic memory allocation.
- Problem-solving patterns identified: the problem involves a single pass over the input data and uses a minimal amount of extra memory.
- Optimization techniques learned: reducing the number of iterations and string concatenations.
- Similar problems to practice: other string manipulation problems, such as substring searching or string reversal.

**Mistakes to Avoid:**
- Common implementation errors: off-by-one errors, incorrect string concatenation, or failure to handle edge cases.
- Edge cases to watch for: empty input strings, invalid limit values, or input messages that exceed the limit.
- Performance pitfalls: using excessive memory or iterating over the input data multiple times.
- Testing considerations: testing with different input sizes, edge cases, and limit values to ensure the solution is correct and efficient.