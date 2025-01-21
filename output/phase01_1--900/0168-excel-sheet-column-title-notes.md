## Excel Sheet Column Title
**Problem Link:** https://leetcode.com/problems/excel-sheet-column-title/description

**Problem Statement:**
- Input format and constraints: The input is an integer `n` representing the column number in Excel, where `1 <= n <= 2^31 - 1`.
- Expected output format: The output should be a string representing the Excel column title corresponding to the input number.
- Key requirements and edge cases to consider: The Excel column title is based on a base-26 system, where each digit can be represented by a letter from 'A' to 'Z'. For example, 'A' corresponds to 1, 'B' corresponds to 2, and so on.
- Example test cases with explanations:
  - Input: `n = 1`, Output: `"A"`
  - Input: `n = 28`, Output: `"AB"`
  - Input: `n = 701`, Output: `"ZY"`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: One way to solve this problem is to use a brute force approach by iterating through all possible combinations of letters and checking if the current combination corresponds to the input number.
- Step-by-step breakdown of the solution:
  1. Initialize an empty string to store the result.
  2. Iterate through all possible combinations of letters.
  3. For each combination, calculate its corresponding number in the base-26 system.
  4. If the calculated number matches the input number, return the current combination as the result.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is inefficient and has a high time complexity.

```cpp
string convertToTitle(int n) {
    string result = "";
    while (n > 0) {
        n--;
        int remainder = n % 26;
        char c = 'A' + remainder;
        result = c + result;
        n /= 26;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$, where $n$ is the input number. This is because the while loop runs until $n$ becomes 0, and in each iteration, $n$ is divided by 26.
> - **Space Complexity:** $O(log(n))$, where $n$ is the input number. This is because the result string can have at most $log(n)$ characters.
> - **Why these complexities occur:** The time complexity is $O(log(n))$ because the while loop runs for $log(n)$ iterations, and in each iteration, a constant amount of work is done. The space complexity is $O(log(n))$ because the result string can have at most $log(n)$ characters.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is to use a mathematical approach to calculate the Excel column title corresponding to the input number. This can be done by repeatedly dividing the input number by 26 and appending the remainder to the result string.
- Detailed breakdown of the approach:
  1. Initialize an empty string to store the result.
  2. While the input number is greater than 0, repeat the following steps:
    - Calculate the remainder of the input number divided by 26.
    - Append the corresponding letter to the result string.
    - Update the input number by dividing it by 26.
  3. Return the result string.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(log(n))$ and a space complexity of $O(log(n))$, which is the best possible complexity for this problem.

```cpp
string convertToTitle(int n) {
    string result = "";
    while (n > 0) {
        n--;
        int remainder = n % 26;
        char c = 'A' + remainder;
        result = c + result;
        n /= 26;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(log(n))$, where $n$ is the input number. This is because the while loop runs for $log(n)$ iterations, and in each iteration, a constant amount of work is done.
> - **Space Complexity:** $O(log(n))$, where $n$ is the input number. This is because the result string can have at most $log(n)$ characters.
> - **Optimality proof:** This approach is optimal because it has the best possible time and space complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of mathematical calculations to solve a problem, as well as the use of a while loop to repeatedly perform a task.
- Problem-solving patterns identified: The problem requires the use of a mathematical approach to calculate the Excel column title corresponding to the input number.
- Optimization techniques learned: The problem demonstrates the use of a mathematical approach to optimize the solution, rather than using a brute force approach.
- Similar problems to practice: Other problems that involve calculating a result based on a mathematical formula, such as calculating the nth Fibonacci number or the nth term of a geometric sequence.

**Mistakes to Avoid:**
- Common implementation errors: One common implementation error is to forget to update the input number after calculating the remainder.
- Edge cases to watch for: One edge case to watch for is when the input number is 0, in which case the result should be an empty string.
- Performance pitfalls: One performance pitfall is to use a brute force approach, which can result in a high time complexity.
- Testing considerations: When testing the solution, it is important to test a variety of input values, including edge cases such as 0 and 1.