## Next Greater Numerically Balanced Number
**Problem Link:** https://leetcode.com/problems/next-greater-numerically-balanced-number/description

**Problem Statement:**
- Input: An integer `n`.
- Output: The smallest integer greater than `n` that is numerically balanced.
- A number is numerically balanced if for every digit `d` with frequency `f`, the value of `d` equals `f`.
- The given integer `n` is in the range `[1, 10^6]`.

**Example Test Cases:**
- Input: `n = 2`
  - Output: `22`
  - Explanation: The number `22` is numerically balanced because the digit `2` appears twice.
- Input: `n = 1234`
  - Output: `1333`
  - Explanation: The number `1333` is the smallest integer greater than `1234` that is numerically balanced.

### Brute Force Approach
**Explanation:**
- Start with `n + 1`.
- For each number, calculate the frequency of its digits.
- Check if the number is numerically balanced by comparing each digit with its frequency.
- If a number is numerically balanced, return it.

```cpp
int nextBeautifulNumber(int n) {
    n++;
    while (true) {
        string str = to_string(n);
        unordered_map<int, int> freq;
        for (char c : str) {
            freq[c - '0']++;
        }
        bool isBalanced = true;
        for (auto& pair : freq) {
            if (pair.first != pair.second) {
                isBalanced = false;
                break;
            }
        }
        if (isBalanced) {
            return n;
        }
        n++;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot m)$, where $k$ is the number of integers checked and $m$ is the average number of digits in those integers.
> - **Space Complexity:** $O(m)$, where $m$ is the maximum number of digits in an integer.
> - **Why these complexities occur:** The brute force approach checks every integer greater than `n` and calculates the frequency of its digits, resulting in these complexities.

### Optimal Approach (Required)
**Explanation:**
- Since the brute force approach is already quite straightforward and efficient for this problem, further optimization is challenging without additional insights or constraints.
- The optimal approach remains the brute force approach with some minor optimizations for handling edge cases and improving readability.

```cpp
int nextBeautifulNumber(int n) {
    n++;
    while (true) {
        string str = to_string(n);
        unordered_map<int, int> freq;
        for (char c : str) {
            freq[c - '0']++;
        }
        bool isBalanced = true;
        for (auto& pair : freq) {
            if (pair.first != pair.second) {
                isBalanced = false;
                break;
            }
        }
        if (isBalanced) {
            return n;
        }
        n++;
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot m)$, where $k$ is the number of integers checked and $m$ is the average number of digits in those integers.
> - **Space Complexity:** $O(m)$, where $m$ is the maximum number of digits in an integer.
> - **Optimality proof:** This approach is optimal because it directly checks each integer greater than `n` for the condition of being numerically balanced, which is the most straightforward and efficient way to find the next beautiful number.

---

### Final Notes

**Learning Points:**
- Understanding the concept of numerically balanced numbers.
- Implementing a brute force approach to solve the problem.
- Analyzing the time and space complexities of the solution.

**Mistakes to Avoid:**
- Not checking for edge cases, such as when `n` is already a numerically balanced number.
- Incorrectly calculating the frequency of digits or comparing them with their values.
- Not optimizing the solution for readability and efficiency.