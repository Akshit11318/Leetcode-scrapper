## Fraction to Recurring Decimal
**Problem Link:** https://leetcode.com/problems/fraction-to-recurring-decimal/description

**Problem Statement:**
- Input: `numerator` and `denominator` as integers
- Constraints: `denominator` is not zero
- Expected Output: String representation of the decimal expansion of the fraction
- Key Requirements:
  - Handle recurring decimals
  - Handle non-recurring decimals
  - Handle zero numerator
- Edge Cases:
  - Division by zero (already constrained against)
  - Numerator or denominator is zero
- Example Test Cases:
  - `numerator = 1, denominator = 2` -> Output: `"0.5"`
  - `numerator = 2, denominator = 3` -> Output: `"0.(6)"`
  - `numerator = 4, denominator = 11` -> Output: `"0.(36)"`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves performing long division and tracking remainders to identify recurring decimals.
- Step-by-step breakdown:
  1. Perform integer division to get the whole number part.
  2. Use the remainder as the new numerator for the fractional part.
  3. Continue dividing until the remainder is zero or a recurring pattern is detected.
- This approach comes to mind first because it directly mirrors the manual process of performing long division.

```cpp
string fractionToDecimal(int numerator, int denominator) {
    if (numerator == 0) return "0";
    string result = "";
    if ((numerator < 0) ^ (denominator < 0)) result += "-";
    long long num = abs((long long)numerator);
    long long den = abs((long long)denominator);
    result += to_string(num / den);
    long long remainder = num % den;
    if (remainder == 0) return result;
    result += ".";
    unordered_map<long long, int> map;
    while (remainder != 0 && map.find(remainder) == map.end()) {
        map[remainder] = result.size();
        remainder *= 10;
        result += to_string(remainder / den);
        remainder %= den;
    }
    if (remainder != 0) {
        int index = map[remainder];
        result.insert(index, "(");
        result += ")";
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$ where $n$ is the numerator, because in the worst case, we might have to append a digit to the result for each power of 10 up to $n$.
> - **Space Complexity:** $O(log(n))$ due to the storage of remainders in the map and the growth of the result string.
> - **Why these complexities occur:** The time complexity is due to the division and the potential for appending digits to the result string, while the space complexity comes from storing remainders and the result string.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is essentially the same as the brute force, with optimizations in handling the integer part and the fractional part separately.
- Key insight: Using a map to store remainders and their corresponding indices in the result string allows for efficient detection of recurring decimals.
- Detailed breakdown:
  1. Handle the integer part by performing integer division.
  2. For the fractional part, use a map to track remainders and their indices.
  3. When a recurring remainder is found, insert parentheses around the recurring part.
- Proof of optimality: This approach is optimal because it minimizes the number of divisions required and efficiently detects recurring decimals.

```cpp
string fractionToDecimal(int numerator, int denominator) {
    if (numerator == 0) return "0";
    string result = "";
    if ((numerator < 0) ^ (denominator < 0)) result += "-";
    long long num = abs((long long)numerator);
    long long den = abs((long long)denominator);
    result += to_string(num / den);
    long long remainder = num % den;
    if (remainder == 0) return result;
    result += ".";
    unordered_map<long long, int> map;
    while (remainder != 0 && map.find(remainder) == map.end()) {
        map[remainder] = result.size();
        remainder *= 10;
        result += to_string(remainder / den);
        remainder %= den;
    }
    if (remainder != 0) {
        int index = map[remainder];
        result.insert(index, "(");
        result += ")";
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$ where $n$ is the numerator, because in the worst case, we might have to append a digit to the result for each power of 10 up to $n$.
> - **Space Complexity:** $O(log(n))$ due to the storage of remainders in the map and the growth of the result string.
> - **Optimality proof:** This approach is optimal because it performs the minimum number of divisions necessary to compute the decimal representation and efficiently detects recurring patterns.

---

### Final Notes

**Learning Points:**
- **Long Division**: Understanding how long division works is crucial for solving this problem.
- **Hashing Remainders**: Using a map to store remainders and their indices is key to efficiently detecting recurring decimals.
- **String Manipulation**: Knowing how to manipulate strings in C++ (e.g., inserting characters, appending) is important for constructing the result.

**Mistakes to Avoid:**
- **Integer Overflow**: Be careful with integer overflows, especially when multiplying the remainder by 10.
- **Map Usage**: Ensure proper usage of the map, including checking for existing keys before inserting.
- **Edge Cases**: Always consider edge cases, such as a numerator or denominator of zero, and handle them appropriately.