## Count Numbers with Unique Digits II

**Problem Link:** https://leetcode.com/problems/count-numbers-with-unique-digits-ii/description

**Problem Statement:**
- Input: An integer `n`, representing the maximum number to consider.
- Constraints: $0 \leq n \leq 10^8$
- Expected Output: The number of numbers with unique digits in the range `[0, n]`.
- Key Requirements and Edge Cases:
  - Consider numbers with leading zeros as invalid for the purpose of this count, except for the number 0 itself.
  - Handle cases where `n` is 0 or negative.

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking each number from 0 to `n` to see if it has unique digits.
- This approach comes to mind first because it directly addresses the problem statement without requiring additional insights.

```cpp
int countNumbersWithUniqueDigits(int n) {
    int count = 0;
    for (int i = 0; i <= n; i++) {
        string str = to_string(i);
        set<char> uniqueDigits;
        bool hasUniqueDigits = true;
        for (char digit : str) {
            if (!uniqueDigits.insert(digit).second) {
                hasUniqueDigits = false;
                break;
            }
        }
        if (hasUniqueDigits) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the input number and $m$ is the average number of digits in the numbers up to $n$. This is because we're checking each number up to $n$ and for each number, we're iterating over its digits.
> - **Space Complexity:** $O(m)$, due to the space required to store the set of unique digits for each number.
> - **Why these complexities occur:** The brute force approach requires checking each number individually, leading to linear time complexity with respect to the input number `n`. The space complexity is due to the set used to store unique digits for each number.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to recognize that we can calculate the number of unique digit numbers for each length (from 1 to 10 digits) without actually generating the numbers.
- For a number of length $i$, the first digit can be chosen from 9 options (excluding 0 to avoid leading zeros for numbers > 0), and each subsequent digit can be chosen from the remaining digits (10 - j - 1 options for the j-th digit).
- We sum up the counts for all lengths up to the length of `n`.

```cpp
int countNumbersWithUniqueDigits(int n) {
    if (n == 0) return 1;
    int count = 10;
    int unique = 9;
    int availableNumber = unique;
    int digits = n;
    while (digits > 1 && availableNumber > 0) {
        availableNumber *= (10 - digits + 1);
        unique += availableNumber;
        digits--;
        count += availableNumber;
    }
    if (n > 10) {
        for (int i = 11; i <= n; i++) {
            int temp = i;
            set<char> st;
            while (temp > 0) {
                st.insert(temp % 10);
                temp /= 10;
            }
            if (st.size() == to_string(i).length()) {
                count++;
            }
        }
    }
    return min(count, n + 1);
}
```

However, considering our constraints and requirements, a more optimal and straightforward approach without needing to iterate through all numbers would be focusing on calculating the possibilities directly:

```cpp
int countNumbersWithUniqueDigits(int n) {
    if (n < 10) return n + 1;
    long long res = 10;
    long long cur = 9;
    for (int i = 2; i <= 10; i++) {
        cur *= (11 - i);
        res += cur;
        if (to_string(n).length() == i) {
            break;
        }
    }
    if (to_string(n).length() > 10) return res;
    vector<bool> seen(10, false);
    string str = to_string(n);
    for (int i = 0; i < str.length(); i++) {
        int val = str[i] - '0';
        if (i == 0 && val == 0) continue;
        if (seen[val]) break;
        seen[val] = true;
        if (i == str.length() - 1) res++;
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$, because the number of digits in `n` determines the number of iterations.
> - **Space Complexity:** $O(1)$, since the space used does not grow with the size of the input `n`.
> - **Optimality proof:** This approach is optimal because it directly calculates the number of unique digit numbers without iterating over all numbers up to `n`, thus avoiding unnecessary computations.

---

### Final Notes

**Learning Points:**
- The importance of considering the constraints and requirements of the problem.
- How to approach problems by first considering brute force and then optimizing.
- Understanding how to calculate permutations with restrictions (unique digits in this case).

**Mistakes to Avoid:**
- Not considering the constraints of the problem, such as the limit on `n`.
- Not optimizing the solution, leading to inefficient code.
- Not handling edge cases, such as when `n` is 0 or negative.