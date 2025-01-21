## Nth Magical Number

**Problem Link:** https://leetcode.com/problems/nth-magical-number/description

**Problem Statement:**
- Input format: Given two integers `n` and `a` and `b`, where `n` is the position of the magical number, and `a` and `b` are the base numbers.
- Expected output format: The `n`-th magical number, which is the `n`-th number in the sequence formed by numbers that are multiples of `a` or `b`.
- Key requirements and edge cases to consider: The sequence should be in ascending order, and the numbers should be positive integers.
- Example test cases with explanations:
  - `n = 3, a = 2, b = 3`, the sequence is `[2, 3, 4, 6, 6, 8, 9, 10, 12, ...]`, so the 3rd magical number is `4`.
  - `n = 4, a = 2, b = 4`, the sequence is `[2, 4, 4, 6, 8, 8, 10, ...]`, so the 4th magical number is `6`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a sequence of magical numbers by generating multiples of `a` and `b` and then sorting them in ascending order.
- Step-by-step breakdown of the solution:
  1. Initialize an empty vector to store the magical numbers.
  2. Initialize two variables, `i` and `j`, to 1, which will be used to generate multiples of `a` and `b`.
  3. Use a loop to generate multiples of `a` and `b` and add them to the vector.
  4. Sort the vector in ascending order.
  5. Return the `n`-th number in the vector.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that directly addresses the problem statement.

```cpp
class Solution {
public:
    int nthMagicalNumber(int n, int a, int b) {
        vector<int> magicalNumbers;
        int i = 1, j = 1;
        while (magicalNumbers.size() < n) {
            int numA = a * i;
            int numB = b * j;
            if (numA <= numB) {
                magicalNumbers.push_back(numA);
                i++;
            }
            if (numB <= numA) {
                if (magicalNumbers.empty() || magicalNumbers.back() != numB) {
                    magicalNumbers.push_back(numB);
                }
                j++;
            }
        }
        return magicalNumbers.back();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the input number, because we are generating $n$ magical numbers.
> - **Space Complexity:** $O(n)$, because we are storing $n$ magical numbers in the vector.
> - **Why these complexities occur:** The brute force approach has a linear time complexity because we are generating magical numbers one by one, and the space complexity is also linear because we are storing all the generated numbers in the vector.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use binary search to find the `n`-th magical number. The idea is to find the range of possible values for the `n`-th magical number and then use binary search to narrow down the range until we find the exact value.
- Detailed breakdown of the approach:
  1. Calculate the least common multiple (LCM) of `a` and `b`.
  2. Initialize the low and high bounds for the binary search. The low bound is the minimum of `a` and `b`, and the high bound is the maximum of `a` and `b` multiplied by `n`.
  3. Use binary search to find the `n`-th magical number.
- Proof of optimality: The binary search approach has a logarithmic time complexity, which is more efficient than the brute force approach for large inputs.
- Why further optimization is impossible: The binary search approach is already optimal because it has a logarithmic time complexity, which is the best possible time complexity for this problem.

```cpp
class Solution {
public:
    int nthMagicalNumber(int n, int a, int b) {
        int lcm = a * b / gcd(a, b);
        int low = min(a, b);
        int high = (int)1e15;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (mid / a + mid / b - mid / lcm < n) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }
    
    int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$, where $n$ is the input number, because we are using binary search to find the `n`-th magical number.
> - **Space Complexity:** $O(1)$, because we are only using a constant amount of space to store the variables.
> - **Optimality proof:** The binary search approach has a logarithmic time complexity, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, LCM calculation, and GCD calculation.
- Problem-solving patterns identified: Using binary search to find the range of possible values and then narrowing down the range until the exact value is found.
- Optimization techniques learned: Using binary search to reduce the time complexity from linear to logarithmic.
- Similar problems to practice: Finding the `n`-th number in a sequence, calculating the LCM and GCD of two numbers, and using binary search to solve problems.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as when `a` and `b` are equal or when `n` is 1.
- Edge cases to watch for: When `a` and `b` are equal, the sequence only contains multiples of `a`. When `n` is 1, the `n`-th magical number is simply `a`.
- Performance pitfalls: Using a brute force approach for large inputs, which can result in a time limit exceeded error.
- Testing considerations: Testing the solution with different inputs, including edge cases, to ensure that it works correctly and efficiently.