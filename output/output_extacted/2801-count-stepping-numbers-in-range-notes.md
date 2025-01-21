## Count Stepping Numbers in Range
**Problem Link:** https://leetcode.com/problems/count-stepping-numbers-in-range/description

**Problem Statement:**
- Input format: Two integers `low` and `high`, where `1 <= low <= high <= 10^9`.
- Expected output format: The count of `stepping numbers` in the range `[low, high]`.
- Key requirements and edge cases to consider:
  - A `stepping number` is a number that has adjacent digits differing by 1.
  - The input range is inclusive.
- Example test cases with explanations:
  - For `low = 0` and `high = 21`, the stepping numbers in the range are `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21]`, so the output should be `13`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each number in the range and check if it's a stepping number.
- Step-by-step breakdown of the solution:
  1. Iterate over the range `[low, high]`.
  2. For each number, convert it to a string to easily access adjacent digits.
  3. Check if the number is a stepping number by comparing adjacent digits.
  4. If the number is a stepping number, increment the count.
- Why this approach comes to mind first: It directly checks each number in the range, making it straightforward but potentially inefficient.

```cpp
int countSteppingNumbers(int low, int high) {
    int count = 0;
    for (int num = low; num <= high; num++) {
        string strNum = to_string(num);
        bool isStepping = true;
        for (int i = 0; i < strNum.size() - 1; i++) {
            if (abs(strNum[i] - strNum[i + 1]) != 1) {
                isStepping = false;
                break;
            }
        }
        if (isStepping) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of integers in the range `[low, high]` and $m$ is the average number of digits in these integers. This is because for each number, we potentially check each digit.
> - **Space Complexity:** $O(m)$, for storing the string representation of the current number.
> - **Why these complexities occur:** The brute force approach checks every number and potentially every digit in each number, leading to these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking each number in the range, we can generate stepping numbers starting from each digit `0-9` and count how many fall within the given range.
- Detailed breakdown of the approach:
  1. For each starting digit `0-9`, generate stepping numbers.
  2. Use a queue or recursion to explore all possible stepping numbers from each starting digit.
  3. For each generated stepping number, check if it falls within the range `[low, high]`.
  4. If it does, increment the count of stepping numbers.
- Proof of optimality: This approach avoids unnecessary checks by only generating numbers that could potentially be stepping numbers within the range.

```cpp
int countSteppingNumbers(int low, int high) {
    int count = 0;
    for (int i = 0; i <= 9; i++) {
        dfs(i, low, high, count);
    }
    return count;
}

void dfs(int num, int low, int high, int& count) {
    if (num >= low && num <= high) {
        count++;
    }
    if (num > high) {
        return;
    }
    int lastDigit = num % 10;
    if (lastDigit > 0) {
        dfs(num * 10 + lastDigit - 1, low, high, count);
    }
    if (lastDigit < 9) {
        dfs(num * 10 + lastDigit + 1, low, high, count);
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(b^d)$, where $b$ is the base (10 for decimal) and $d$ is the maximum number of digits in the numbers within the range. This is because in the worst case, we explore a tree of height $d$ and branching factor $b$.
> - **Space Complexity:** $O(d)$, due to the recursion stack.
> - **Optimality proof:** This approach is optimal because it only generates and checks numbers that are potential stepping numbers within the range, avoiding unnecessary computations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Depth-first search (DFS) and generation of numbers with specific properties.
- Problem-solving patterns identified: Avoiding brute force by generating solutions rather than checking all possibilities.
- Optimization techniques learned: Using DFS to explore a constrained solution space efficiently.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as numbers with leading zeros or the transition from single-digit to multi-digit numbers.
- Edge cases to watch for: Numbers at the boundaries of the range and how they are included or excluded.
- Performance pitfalls: Using inefficient algorithms that check every number in the range without considering the properties of stepping numbers.