## Form Smallest Number From Two Digit Arrays

**Problem Link:** https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/description

**Problem Statement:**
- Input format: Two integer arrays `num1` and `num2` of length 2, where each integer is between 10 and 99.
- Constraints: `10 <= num1[i], num2[i] <= 99` for all `i`.
- Expected output format: The smallest possible integer that can be formed by concatenating a number from `num1` with a number from `num2`.
- Key requirements and edge cases to consider: All possible combinations of numbers from the two arrays should be considered, and the smallest resulting integer should be returned.
- Example test cases with explanations:
  - If `num1 = [25, 50]` and `num2 = [10, 60]`, the smallest possible integer is `2510`.
  - If `num1 = [10, 25]` and `num2 = [50, 60]`, the smallest possible integer is `1050`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can simply concatenate each number from `num1` with each number from `num2` and keep track of the smallest resulting integer.
- Step-by-step breakdown of the solution:
  1. Initialize the smallest integer to a large value (e.g., `INT_MAX`).
  2. Iterate over each number `a` in `num1`.
  3. For each `a`, iterate over each number `b` in `num2`.
  4. Concatenate `a` and `b` to form a new integer `ab`.
  5. If `ab` is smaller than the current smallest integer, update the smallest integer.
- Why this approach comes to mind first: It is straightforward and easy to implement, as it simply checks all possible combinations of numbers.

```cpp
class Solution {
public:
    int minNumber(vector<int>& num1, vector<int>& num2) {
        int smallest = INT_MAX;
        for (int a : num1) {
            for (int b : num2) {
                int ab = a * 100 + b;
                if (ab < smallest) smallest = ab;
                int ba = b * 100 + a;
                if (ba < smallest) smallest = ba;
            }
        }
        return smallest;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the lengths of `num1` and `num2`, respectively. In this case, $n = m = 2$, so the time complexity is $O(1)$.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the smallest integer.
> - **Why these complexities occur:** The time complexity occurs because we are iterating over each number in `num1` and `num2` once, and the space complexity occurs because we are only using a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all possible combinations of numbers, we can simply concatenate the smallest number from `num1` with the smallest number from `num2`.
- Detailed breakdown of the approach:
  1. Find the smallest number in `num1`.
  2. Find the smallest number in `num2`.
  3. Concatenate the two smallest numbers to form the smallest possible integer.
- Proof of optimality: This approach is optimal because it always returns the smallest possible integer that can be formed by concatenating a number from `num1` with a number from `num2`.
- Why further optimization is impossible: This approach is already optimal because it only checks the smallest numbers in `num1` and `num2`, which is the minimum amount of work required to find the smallest possible integer.

```cpp
class Solution {
public:
    int minNumber(vector<int>& num1, vector<int>& num2) {
        int a = *min_element(num1.begin(), num1.end());
        int b = *min_element(num2.begin(), num2.end());
        return min(a * 100 + b, b * 100 + a);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the lengths of `num1` and `num2`, respectively. In this case, $n = m = 2$, so the time complexity is $O(1)$.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the smallest numbers.
> - **Optimality proof:** This approach is optimal because it always returns the smallest possible integer that can be formed by concatenating a number from `num1` with a number from `num2`.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Finding the minimum value in an array, concatenating numbers to form a new integer.
- Problem-solving patterns identified: Checking all possible combinations of numbers, using the smallest numbers to form the smallest possible integer.
- Optimization techniques learned: Reducing the number of iterations required to find the smallest possible integer.
- Similar problems to practice: Finding the maximum possible integer that can be formed by concatenating numbers from two arrays.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to check all possible combinations of numbers, using the wrong operator to concatenate numbers.
- Edge cases to watch for: When the smallest number in `num1` is larger than the smallest number in `num2`, or vice versa.
- Performance pitfalls: Using a brute force approach that checks all possible combinations of numbers, resulting in a time complexity of $O(n \cdot m)$.
- Testing considerations: Testing the function with different inputs, such as arrays with different lengths or containing different numbers.