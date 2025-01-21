## Confusing Number II

**Problem Link:** https://leetcode.com/problems/confusing-number-ii/description

**Problem Statement:**
- Input format and constraints: The problem takes an integer `N` as input, where `1 <= N <= 10^9`. 
- Expected output format: The task is to find the number of confusing numbers in the range `[1, N]`.
- Key requirements and edge cases to consider: A confusing number is a number that when rotated by 180 degrees, becomes a different number. For example, the number "6" becomes "9" when rotated by 180 degrees, making it a confusing number. The numbers "0", "1", and "8" are not confusing as they remain the same after rotation.
- Example test cases with explanations:
  - For `N = 20`, the confusing numbers are `6`, `9`, `11`, `16`, `18`, and `19`, so the output should be `6`.
  - For `N = 100`, the output should be the count of confusing numbers up to `100`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate through all numbers from `1` to `N`, convert each number to a string, and then check if the number is confusing by comparing it with its rotation.
- Step-by-step breakdown of the solution:
  1. Convert each number to a string to easily access and rotate its digits.
  2. Rotate the number by 180 degrees. This can be done by replacing each digit with its corresponding rotated digit (`0` stays `0`, `1` stays `1`, `6` becomes `9`, `8` stays `8`, `9` becomes `6`, and all other digits are not confusing).
  3. Compare the original number with its rotated version. If they are different, the number is confusing.
- Why this approach comes to mind first: It's a straightforward way to solve the problem by checking each number individually.

```cpp
int confusingNumberII(int N) {
    int count = 0;
    for (int i = 1; i <= N; ++i) {
        string str = to_string(i);
        string rotated = "";
        for (char c : str) {
            if (c == '6') rotated += '9';
            else if (c == '9') rotated += '6';
            else if (c != '0' && c != '1' && c != '8') {
                rotated = "-1"; // Mark as not confusing if any digit doesn't rotate
                break;
            } else rotated += c;
        }
        if (rotated != "-1" && str != rotated) count++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot logN)$, where $logN$ is due to converting each number to a string and then iterating over its digits.
> - **Space Complexity:** $O(logN)$ for storing the string representation of each number.
> - **Why these complexities occur:** The brute force approach iterates over all numbers up to `N`, and for each number, it converts it to a string and checks each digit, leading to the mentioned complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking each number individually, we can use a recursive approach to generate all possible confusing numbers up to `N`. We can start with an empty string and append digits one by one, making sure that the generated number does not exceed `N` and is indeed confusing.
- Detailed breakdown of the approach:
  1. Define a recursive function that generates all confusing numbers by appending digits (`0`, `1`, `6`, `8`, `9`) to the current number.
  2. In each recursive call, check if the current number exceeds `N`. If it does, stop exploring this branch.
  3. If the current number is within the range `[1, N]` and is confusing (i.e., different from its rotation), increment the count.
- Proof of optimality: This approach is optimal because it directly generates all confusing numbers without unnecessary checks, avoiding the overhead of converting each number to a string and checking its rotation.

```cpp
int confusingNumberII(int N) {
    int count = 0;
    vector<char> digits = {'0', '1', '6', '8', '9'};
    function<void(string, bool)> dfs = [&](string current, bool limited) {
        if (current.size() > 0) {
            int num = stoi(current);
            if (num > N) return;
            string rotated = "";
            for (char c : current) {
                if (c == '6') rotated += '9';
                else if (c == '9') rotated += '6';
                else rotated += c;
            }
            if (current != rotated) count++;
        }
        for (char digit : digits) {
            if (limited && digit == '0' && current.size() == 0) continue;
            if (limited && (digit < current[0])) continue;
            dfs(current + digit, limited && (digit == current[0]));
        }
    };
    dfs("", true);
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(5^M)$, where $M$ is the number of digits in `N`, because in the worst case, we might explore all possible combinations of digits up to the length of `N`.
> - **Space Complexity:** $O(M)$ for the recursion stack.
> - **Optimality proof:** This approach is optimal because it directly generates all confusing numbers without unnecessary checks, making it more efficient than the brute force approach for large `N`.