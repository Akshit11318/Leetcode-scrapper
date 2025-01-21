## Shifting Letters

**Problem Link:** https://leetcode.com/problems/shifting-letters/description

**Problem Statement:**
- Input format: a string `s` and an integer array `shifts`.
- Constraints: `1 <= s.length <= 10^5` and `shifts.length == s.length`.
- Expected output format: a string with each letter in `s` shifted by the corresponding value in `shifts`.
- Key requirements: 
  - Shift each letter in `s` by the corresponding value in `shifts`.
  - If the shift value is positive, shift the letter to the right in the alphabet.
  - If the shift value is negative, shift the letter to the left in the alphabet.
- Edge cases:
  - Handle wrap-around when shifting beyond 'z' or before 'a'.
  - Ensure the output is in lowercase.

**Example Test Cases:**
- Input: `s = "abc", shifts = [3,5,9]`.
- Output: `"rpl"`.
- Explanation: 
  - 'a' is shifted by 3 to 'd', then by 5 to 'i', then by 9 to 'r'.
  - 'b' is shifted by 5 to 'g', then by 9 to 'p'.
  - 'c' is shifted by 9 to 'l'.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through the string and apply each shift to the corresponding character.
- We need to handle the wrap-around when shifting beyond 'z' or before 'a'.

```cpp
string shiftingLetters(string s, vector<int>& shifts) {
    string result = s;
    for (int i = 0; i < s.length(); i++) {
        int shift = 0;
        for (int j = i; j < shifts.size(); j++) {
            shift += shifts[j];
            result[i] = 'a' + (result[i] - 'a' + shift) % 26;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string `s`. This is because we have a nested loop structure.
> - **Space Complexity:** $O(1)$, excluding the space required for the output string. This is because we only use a constant amount of space to store the shift value and the result.
> - **Why these complexities occur:** The nested loop structure causes the time complexity to be quadratic. The space complexity is constant because we only use a fixed amount of space to store the shift value and the result.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a prefix sum array to store the cumulative sum of the shifts.
- This allows us to calculate the total shift for each character in constant time.

```cpp
string shiftingLetters(string s, vector<int>& shifts) {
    int n = s.length();
    vector<int> prefixSum(n + 1, 0);
    for (int i = n - 1; i >= 0; i--) {
        prefixSum[i] = prefixSum[i + 1] + shifts[i];
    }
    string result = s;
    for (int i = 0; i < n; i++) {
        result[i] = 'a' + (result[i] - 'a' + prefixSum[i]) % 26;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we have two separate loops that each run in linear time.
> - **Space Complexity:** $O(n)$, excluding the space required for the output string. This is because we use a prefix sum array of size $n + 1$.
> - **Optimality proof:** This is the optimal solution because we only need to iterate through the string and the shifts array once to calculate the prefix sum, and then once more to apply the shifts to the characters. This is the minimum number of iterations required to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: prefix sum arrays, modular arithmetic.
- Problem-solving patterns identified: using prefix sums to reduce the time complexity of a problem.
- Optimization techniques learned: using a prefix sum array to avoid nested loops.
- Similar problems to practice: problems that involve cumulative sums or prefix sums.

**Mistakes to Avoid:**
- Common implementation errors: not handling wrap-around when shifting beyond 'z' or before 'a'.
- Edge cases to watch for: empty input strings, strings with only one character.
- Performance pitfalls: using a nested loop structure when a prefix sum array can be used instead.
- Testing considerations: testing the function with different input strings and shift arrays, including edge cases.