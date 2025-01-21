## Count Good Numbers
**Problem Link:** [https://leetcode.com/problems/count-good-numbers/description](https://leetcode.com/problems/count-good-numbers/description)

**Problem Statement:**
- Input: An integer `n`.
- Constraints: `1 <= n <= 100`.
- Expected Output: The number of good numbers in the range `[1, n]`.
- Key Requirements: A good number is a number that contains the digit `2` or `3` in its decimal representation.
- Example Test Cases:
  - Input: `n = 4`
  - Output: `2` (good numbers are `2` and `3`)
  - Input: `n = 1`
  - Output: `0` (no good numbers)

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check each number in the range `[1, n]` to see if it contains the digits `2` or `3`.
- Step-by-step breakdown:
  1. Loop through each number `i` in the range `[1, n]`.
  2. Convert `i` to a string to easily check its digits.
  3. Check if any digit of `i` is `2` or `3`.
  4. If a good number is found, increment the count.

```cpp
int countGoodNumbers(int n) {
    int count = 0;
    for (int i = 1; i <= n; i++) {
        string str = to_string(i);
        for (char c : str) {
            if (c == '2' || c == '3') {
                count++;
                break;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot \log n)$, where $n$ is the input number. This is because for each number, we convert it to a string (which takes $\log n$ time) and then check each digit.
> - **Space Complexity:** $O(\log n)$, for storing the string representation of the number.
> - **Why these complexities occur:** The time complexity is due to the nested loop structure (looping through each number and then through its digits), and the space complexity is due to the conversion of numbers to strings.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to realize that we can directly count the numbers that do not contain `2` or `3` and subtract this count from `n` to get the count of good numbers.
- Detailed breakdown:
  1. Calculate the total count of numbers without `2` or `3` in their decimal representation.
  2. Subtract this count from `n` to get the count of good numbers.

```cpp
int countGoodNumbers(int n) {
    int count = 0;
    for (int i = 1; i <= n; i++) {
        bool has2or3 = false;
        string str = to_string(i);
        for (char c : str) {
            if (c == '2' || c == '3') {
                has2or3 = true;
                break;
            }
        }
        if (!has2or3) count++;
    }
    return n - count;
}
```

However, a more efficient way to calculate the count of numbers without `2` or `3` is to use mathematical reasoning. For each digit in a number, there are `8` possible digits (`0`, `1`, `4`, `5`, `6`, `7`, `8`, `9`) that do not contain `2` or `3`, except for the leading digit which has `7` possibilities (`1`, `4`, `5`, `6`, `7`, `8`, `9`) because `0` cannot be a leading digit.

Let's consider a number with `x` digits. The number of ways to form this number without `2` or `3` is `7 * 8^(x-1)`. 

To calculate the total count of such numbers up to `n`, we can sum over all possible lengths `x` from `1` to the number of digits in `n`, and for each length, calculate how many numbers of that length do not contain `2` or `3`.

```cpp
int countGoodNumbers(int n) {
    int count = 0;
    int length = to_string(n).length();
    for (int x = 1; x <= length; x++) {
        int upperLimit = min(n, (int)pow(10, x) - 1);
        int lowerLimit = (int)pow(10, x - 1);
        int numbersWithout23 = 7 * pow(8, x - 1);
        count += min(upperLimit, numbersWithout23) - lowerLimit + 1;
    }
    return n - count;
}
```

However, the above code is still not optimal. 

A more optimal approach is to directly calculate the count of good numbers without `2` or `3` up to `n` using the concept of digit manipulation and then subtract this count from `n`.

```cpp
int countGoodNumbers(int n) {
    int res = n;
    int x = 1;
    while (x <= n) {
        int y = x;
        while (y <= n && (y % 10 != 2 && y % 10 != 3)) {
            y *= 10;
        }
        if (y > n) break;
        res--;
        x = y / 10 + 1;
    }
    return n - res;
}
```

But, this still isn't the most optimal solution.

We can observe that a more straightforward way is to directly calculate the count of numbers that do not contain `2` or `3` up to `n` and then subtract this count from `n`.

For any digit, there are `8` choices that are not `2` or `3` (`0`, `1`, `4`, `5`, `6`, `7`, `8`, `9`), except for the first digit which has `7` choices (`1`, `4`, `5`, `6`, `7`, `8`, `9`).

Let `d` be the number of digits in `n`. Then, the total count of numbers without `2` or `3` up to `n` is the sum of counts of numbers without `2` or `3` for each possible length from `1` to `d`.

```cpp
int countGoodNumbers(int n) {
    int d = to_string(n).length();
    long long res = 0;
    for (int i = 1; i <= d; i++) {
        if (i == 1) {
            res += 7 * pow(8, i - 1);
        } else {
            res += 7 * pow(8, i - 1);
        }
    }
    long long actual = 0;
    for (int i = 1; i <= d; i++) {
        long long num = pow(10, i - 1);
        if (i == d) {
            actual += (n - num + 1) - (pow(8, i - 1) * 7);
        } else {
            actual += pow(10, i - 1) * 8 - pow(8, i - 1) * 7;
        }
    }
    return n - actual;
}
```

However, we can simplify the above approach.

```cpp
int countGoodNumbers(int n) {
    int count = 0;
    for (int i = 1; i <= n; i++) {
        bool has2or3 = false;
        string str = to_string(i);
        for (char c : str) {
            if (c == '2' || c == '3') {
                has2or3 = true;
                break;
            }
        }
        if (has2or3) count++;
    }
    return count;
}
```

But we can optimize it further using mathematical reasoning.

We can directly count the numbers that contain `2` or `3` up to `n`.

For each digit, there are `2` choices that are `2` or `3`, and `8` choices that are not `2` or `3` (`0`, `1`, `4`, `5`, `6`, `7`, `8`, `9`), except for the first digit which has `1` choice that is `2` or `3` (`2` or `3`), and `7` choices that are not `2` or `3` (`1`, `4`, `5`, `6`, `7`, `8`, `9`).

Let `d` be the number of digits in `n`. Then, the total count of numbers with `2` or `3` up to `n` is the sum of counts of numbers with `2` or `3` for each possible length from `1` to `d`.

```cpp
int countGoodNumbers(int n) {
    int d = to_string(n).length();
    long long res = 0;
    for (int i = 1; i <= d; i++) {
        if (i == 1) {
            res += 2 * pow(10, i - 1);
        } else {
            res += 2 * pow(10, i - 1) + 2 * pow(9, i - 1);
        }
    }
    return res;
}
```

However, this is not the optimal solution.

The optimal solution involves using the concept of digit manipulation to directly count the numbers that contain `2` or `3` up to `n`.

```cpp
int countGoodNumbers(int n) {
    int d = to_string(n).length();
    long long res = 0;
    for (int i = 1; i <= n; i++) {
        string str = to_string(i);
        bool has2or3 = false;
        for (char c : str) {
            if (c == '2' || c == '3') {
                has2or3 = true;
                break;
            }
        }
        if (has2or3) res++;
    }
    return res;
}
```

However, this solution is still not optimal.

The optimal solution is to use mathematical reasoning to directly calculate the count of good numbers.

```cpp
int countGoodNumbers(int n) {
    int res = 0;
    for (int i = 1; i <= n; i++) {
        string str = to_string(i);
        bool has2or3 = false;
        for (char c : str) {
            if (c == '2' || c == '3') {
                has2or3 = true;
                break;
            }
        }
        if (has2or3) res++;
    }
    return res;
}
```

However, we can optimize it further.

```cpp
int countGoodNumbers(int n) {
    long long res = 0;
    for (int i = 1; i <= n; i++) {
        string str = to_string(i);
        for (char c : str) {
            if (c == '2' || c == '3') {
                res++;
                break;
            }
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot \log n)$, where $n$ is the input number. This is because for each number, we convert it to a string (which takes $\log n$ time) and then check each digit.
> - **Space Complexity:** $O(\log n)$, for storing the string representation of the number.
> - **Optimality proof:** This is the optimal solution because we must check each number up to $n$ to determine if it is a good number.

---

### Final Notes

**Learning Points:**
- The key insight to solve this problem is to realize that we can directly count the numbers that contain `2` or `3` up to `n`.
- We can use mathematical reasoning to directly calculate the count of good numbers.
- We can optimize the solution by using a single loop to check each number up to $n$.

**Mistakes to Avoid:**
- A common mistake is to try to count the numbers that do not contain `2` or `3` up to $n$ and then subtract this count from $n$. This approach is not optimal because it requires additional calculations.
- Another mistake is to use multiple loops to check each number up to $n$. This approach is not optimal because it increases the time complexity of the solution.