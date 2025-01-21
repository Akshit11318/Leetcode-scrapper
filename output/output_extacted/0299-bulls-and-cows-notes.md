## Bulls and Cows
**Problem Link:** https://leetcode.com/problems/bulls-and-cows/description

**Problem Statement:**
- Input format and constraints: The function `getHint` takes two strings, `secret` and `guess`, as input. Both strings are of length 4, consisting only of digits from 0 to 9.
- Expected output format: The function should return a string in the format "XA_YB", where X is the number of `bulls` (correct digits in the correct positions) and Y is the number of `cows` (correct digits in the wrong positions).
- Key requirements and edge cases to consider: 
    - Handle cases where the input strings may contain duplicate digits.
    - Ensure the output string is in the correct format.
- Example test cases with explanations:
    - Input: `secret = "1807"`, `guess = "7810"`
      Output: `"1A3B"`
      Explanation: 
        - The number of `bulls` is 1 (the digit '8' is in the correct position).
        - The number of `cows` is 3 (the digits '7', '1', and '0' are in the wrong positions).

---

### Brute Force Approach
**Explanation:**
- Initial thought process: We can compare each digit in the `guess` string with each digit in the `secret` string to count the number of `bulls` and `cows`.
- Step-by-step breakdown of the solution:
    1. Initialize two counters, `bulls` and `cows`, to zero.
    2. Iterate through each digit in the `guess` string and compare it with the corresponding digit in the `secret` string.
        - If the digits match, increment the `bulls` counter.
        - Otherwise, compare the digit with all other digits in the `secret` string.
            - If a match is found, increment the `cows` counter.
    3. Return the result in the format "XA_YB".

```cpp
string getHint(string secret, string guess) {
    int bulls = 0;
    int cows = 0;
    for (int i = 0; i < guess.length(); i++) {
        if (guess[i] == secret[i]) {
            bulls++;
        } else {
            for (int j = 0; j < secret.length(); j++) {
                if (guess[i] == secret[j]) {
                    cows++;
                    break;
                }
            }
        }
    }
    return to_string(bulls) + "A" + to_string(cows) + "B";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input strings. This is because we have a nested loop structure.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the counters and the result string.
> - **Why these complexities occur:** The nested loop structure causes the time complexity to be quadratic, while the space complexity is constant because we only use a fixed amount of space.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a single pass through the input strings to count the number of `bulls` and `cows`.
- Detailed breakdown of the approach:
    1. Initialize two counters, `bulls` and `cows`, to zero.
    2. Create a frequency array to store the frequency of each digit in the `secret` string.
    3. Iterate through each digit in the `guess` string.
        - If the digit matches the corresponding digit in the `secret` string, increment the `bulls` counter and decrement the frequency of the digit in the frequency array.
        - Otherwise, check if the digit is present in the frequency array. If it is, increment the `cows` counter and decrement the frequency of the digit in the frequency array.
    4. Return the result in the format "XA_YB".

```cpp
string getHint(string secret, string guess) {
    int bulls = 0;
    int cows = 0;
    int freq[10] = {0};
    for (int i = 0; i < secret.length(); i++) {
        freq[secret[i] - '0']++;
    }
    for (int i = 0; i < guess.length(); i++) {
        if (guess[i] == secret[i]) {
            bulls++;
            freq[guess[i] - '0']--;
        }
    }
    for (int i = 0; i < guess.length(); i++) {
        if (guess[i] != secret[i] && freq[guess[i] - '0'] > 0) {
            cows++;
            freq[guess[i] - '0']--;
        }
    }
    return to_string(bulls) + "A" + to_string(cows) + "B";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input strings. This is because we make a single pass through the input strings.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the frequency array and the result string.
> - **Optimality proof:** This is the optimal solution because we only make a single pass through the input strings, resulting in the minimum possible time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: 
    - Using frequency arrays to count the frequency of each digit.
    - Making a single pass through the input strings to optimize time complexity.
- Problem-solving patterns identified: 
    - Using a brute force approach to understand the problem, and then optimizing it.
- Optimization techniques learned: 
    - Reducing the number of passes through the input strings.
    - Using frequency arrays to reduce the time complexity.

**Mistakes to Avoid:**
- Common implementation errors: 
    - Not initializing the frequency array correctly.
    - Not decrementing the frequency of the digit in the frequency array when a match is found.
- Edge cases to watch for: 
    - Handling cases where the input strings may contain duplicate digits.
    - Ensuring the output string is in the correct format.
- Performance pitfalls: 
    - Using a nested loop structure, which can result in a high time complexity.
- Testing considerations: 
    - Testing the function with different input strings to ensure it produces the correct output.