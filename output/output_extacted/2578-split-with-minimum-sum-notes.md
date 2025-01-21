## Split with Minimum Sum
**Problem Link:** https://leetcode.com/problems/split-with-minimum-sum/description

**Problem Statement:**
- Input format: A string `num` containing only digits.
- Constraints: `1 <= num.length <= 10^5`.
- Expected output format: The minimum sum that can be obtained by splitting `num` into two non-empty parts.
- Key requirements and edge cases to consider: The split should result in two non-empty strings, each of which can be parsed into a non-negative integer.

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible splits of the input string `num`.
- Step-by-step breakdown of the solution:
  1. Iterate over all possible split positions in the string `num`.
  2. For each split position, split `num` into two non-empty substrings.
  3. Parse each substring into a non-negative integer.
  4. Calculate the sum of these two integers.
  5. Keep track of the minimum sum found.
- Why this approach comes to mind first: It is a straightforward way to consider all possible splits and calculate their sums.

```cpp
class Solution {
public:
    int minimumSum(string num) {
        int n = num.size();
        int minSum = INT_MAX;
        for (int i = 1; i < n; i++) {
            // Split num into two substrings
            string left = num.substr(0, i);
            string right = num.substr(i);
            
            // Parse substrings into integers
            int leftInt = stoi(left);
            int rightInt = stoi(right);
            
            // Calculate the sum
            int sum = leftInt + rightInt;
            
            // Update the minimum sum
            minSum = min(minSum, sum);
        }
        return minSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of `num` and $m$ is the average time complexity of parsing a substring into an integer, which can be considered constant for practical purposes. Thus, it simplifies to $O(n)$.
> - **Space Complexity:** $O(n)$, as we are creating substrings of `num`.
> - **Why these complexities occur:** The time complexity is due to the iteration over all possible split positions and the parsing of substrings into integers. The space complexity is due to the creation of substrings.

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of trying all possible splits, we can directly find the minimum sum by considering the digits of `num`.
- Detailed breakdown of the approach:
  1. Sort the digits of `num` in ascending order.
  2. Form the first number by concatenating the smallest digit with the next smallest digit.
  3. Form the second number by concatenating the remaining digits.
  4. Calculate the sum of these two numbers.
- Proof of optimality: This approach is optimal because it ensures that the sum of the two numbers formed is minimized. By placing the smallest digits in the tens place of the numbers, we minimize the overall sum.

```cpp
class Solution {
public:
    int minimumSum(int num) {
        string strNum = to_string(num);
        vector<int> digits;
        for (char c : strNum) {
            digits.push_back(c - '0');
        }
        sort(digits.begin(), digits.end());
        
        int firstNum = digits[0] * 10 + digits[2];
        int secondNum = digits[1] * 10 + digits[3];
        
        return firstNum + secondNum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of digits in `num`. This is due to the sorting of digits.
> - **Space Complexity:** $O(n)$, for storing the digits of `num`.
> - **Optimality proof:** This solution is optimal because it minimizes the sum by strategically placing the smallest digits in the tens places of the two numbers formed.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting and strategic placement of digits to minimize a sum.
- Problem-solving patterns identified: Looking for ways to minimize a sum by optimizing the placement of elements.
- Optimization techniques learned: Sorting and clever construction of numbers from digits.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases properly, such as when `num` has fewer than four digits.
- Edge cases to watch for: Ensuring that the split results in two non-empty strings that can be parsed into non-negative integers.
- Performance pitfalls: Using inefficient algorithms for finding the minimum sum, such as trying all possible splits without optimization.
- Testing considerations: Testing with various inputs, including edge cases like small numbers or numbers with repeating digits.