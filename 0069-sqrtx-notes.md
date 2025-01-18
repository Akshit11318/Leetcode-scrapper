## Integer Square Root

**Problem Link:** [leetcode.com/problems/sqrtx/description](https://leetcode.com/problems/sqrtx/description)

**Problem Statement (in your own words):**

The problem asks to find the integer square root of a given non-negative integer. The integer square root is the largest integer whose square is less than or equal to the given number. The input is a non-negative integer, and the output should be the integer square root of that number.

---

### Brute Force Approach

**Explanation:**

The brute force solution involves checking every integer from 0 to the given number to see if its square is less than or equal to the given number.

1. Initialize a variable `i` to 0.
2. Loop through all integers from 0 to the given number.
3. For each integer `i`, check if `i * i` is less than or equal to the given number.
4. If `i * i` is greater than the given number, return `i - 1` as the integer square root.
5. If the loop completes without finding an integer whose square is greater than the given number, return the given number.

```cpp
class Solution {
public:
    int mySqrt(int x) {
        int i = 0;
        while (i * i <= x) {
            i++;
        }
        return i - 1;
    }
};
```

> Complexity Analysis:
> 
> **Time Complexity:** O(√x) because in the worst case, we need to check up to the square root of the given number. The formula is derived from the fact that the loop runs until `i * i` exceeds `x`, which happens when `i` is approximately equal to `√x`.
> 
> **Space Complexity:** O(1) because we only use a constant amount of space to store the variable `i`.

---

### Optimal Approach

**Explanation:**

The optimal approach involves using a binary search algorithm to find the integer square root.

1. Initialize two pointers, `low` and `high`, to 0 and the given number, respectively.
2. Perform a binary search between `low` and `high`.
3. For each midpoint `mid`, check if `mid * mid` is less than or equal to the given number.
4. If `mid * mid` is less than or equal to the given number, update `low` to `mid + 1`.
5. If `mid * mid` is greater than the given number, update `high` to `mid`.
6. Repeat steps 3-5 until `low` exceeds `high`.
7. Return `low - 1` as the integer square root.

```cpp
class Solution {
public:
    int mySqrt(int x) {
        if (x < 2) {
            return x;
        }
        int low = 2;
        int high = x / 2;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            long square = (long) mid * mid;
            if (square == x) {
                return mid;
            } else if (square < x) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return high;
    }
};
```

> Complexity Analysis:
> 
> - **Time Complexity:** O(log n) because we use a binary search algorithm, which reduces the search space by half at each step. The formula is derived from the fact that the number of iterations is proportional to the number of bits in the input number.
> - **Space Complexity:** O(1) because we only use a constant amount of space to store the pointers and the midpoint.

---

### Final Notes

**Learning Points:**

* The integer square root problem can be solved using a brute force approach or an optimal approach using binary search.
* The binary search approach is more efficient, especially for large input numbers.
* The time complexity of the binary search approach is O(log n), which is much faster than the O(√x) time complexity of the brute force approach.

**Mistakes to Avoid:**

* Not considering the case where the input number is 0 or 1, which can cause incorrect results.
* Not using a long data type to calculate the square of the midpoint, which can cause overflow for large input numbers.
* Not updating the `low` and `high` pointers correctly during the binary search, which can cause incorrect results or infinite loops.