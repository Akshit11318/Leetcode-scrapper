## Minimum Addition to Make Integer Beautiful
**Problem Link:** https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/description

**Problem Statement:**
- Input: An integer `n`.
- Constraints: `1 <= n <= 10^6`.
- Expected Output: The minimum number of operations required to make `n` a **beautiful number**.
- Key Requirements: A **beautiful number** is a number whose digits sum up to a number less than or equal to `k`, where `k` is given and `1 <= k <= 9`.
- Example Test Cases:
  - For `n = 16` and `k = 6`, the output should be `1` because `16` becomes `7` (which is beautiful) after subtracting `9`.
  - For `n = 2` and `k = 2`, the output should be `0` because `2` is already beautiful.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible number less than or equal to `n` to see if subtracting it from `n` results in a beautiful number.
- We start from `n` and decrement by `1` until we find a beautiful number or reach `0`.
- This approach is straightforward but inefficient for large `n`.

```cpp
class Solution {
public:
    int minAdditionToMakeBeautiful(int n, int k) {
        int operations = 0;
        while (n > 0) {
            int sum = 0;
            int temp = n;
            while (temp > 0) {
                sum += temp % 10;
                temp /= 10;
            }
            if (sum <= k) break;
            n--;
            operations++;
        }
        return operations;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot log(n))$ because in the worst case, we might need to check every number up to `n`, and for each number, we calculate the sum of its digits, which takes $O(log(n))$ time.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store our variables.
> - **Why these complexities occur:** The time complexity is dominated by the loop that checks every number up to `n` and the nested loop that calculates the sum of digits for each number.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to realize that we should aim to reduce the sum of the digits of `n` as much as possible with each subtraction, which means we should subtract the largest possible digit (`9`) from `n` in each step.
- We calculate the sum of the digits of `n` and subtract `9` from `n` as many times as necessary until the sum of the digits of `n` is less than or equal to `k`.
- This approach is optimal because it minimizes the number of subtractions needed.

```cpp
class Solution {
public:
    int minAdditionToMakeBeautiful(int n, int k) {
        int operations = 0;
        while (true) {
            int sum = 0;
            int temp = n;
            while (temp > 0) {
                sum += temp % 10;
                temp /= 10;
            }
            if (sum <= k) break;
            n -= 9;
            operations++;
        }
        return operations;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$ because we subtract `9` from `n` in each iteration, and we perform a constant amount of work in each iteration.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store our variables.
> - **Optimality proof:** This approach is optimal because it minimizes the number of subtractions needed by always subtracting the largest possible digit (`9`) from `n`.

---

### Final Notes

**Learning Points:**
- The importance of understanding the problem constraints and using them to guide the solution.
- The value of looking for patterns or properties of the input that can be exploited to improve efficiency.
- The use of greedy algorithms to find optimal solutions in certain types of problems.

**Mistakes to Avoid:**
- Not considering the constraints of the problem and trying to solve a more general version of the problem.
- Not looking for opportunities to reduce the problem size or simplify the problem.
- Not testing the solution thoroughly to ensure it works correctly for all possible inputs.