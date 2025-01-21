## Find Score of an Array After Marking All Elements
**Problem Link:** https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/description

**Problem Statement:**
- Input: An array of integers `arr` and a target integer `k`.
- Constraints: The array will have at least 1 element and at most 10^5 elements, with each element being a non-negative integer.
- Expected Output: The maximum score that can be achieved after marking all elements in the array.
- Key Requirements: The score is calculated by multiplying the number of elements in the array that are not divisible by `k` by the number of elements in the array that are divisible by `k`.
- Example Test Cases:
  - For `arr = [2, 5, 9, 3]` and `k = 3`, the output should be `2`, because the numbers not divisible by `k` are `2`, `5`, and `9`, and the numbers divisible by `k` are `3`.
  - For `arr = [1, 2, 3, 4, 5]` and `k = 2`, the output should be `6`, because the numbers not divisible by `k` are `1`, `3`, and `5`, and the numbers divisible by `k` are `2` and `4`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To calculate the score, we need to count the numbers in the array that are divisible by `k` and the numbers that are not divisible by `k`.
- Step-by-step breakdown of the solution:
  1. Initialize two counters, `divisibleCount` and `notDivisibleCount`, to 0.
  2. Iterate through each number in the array.
  3. For each number, check if it is divisible by `k` by using the modulo operator (`%`).
  4. If the number is divisible by `k`, increment `divisibleCount`. Otherwise, increment `notDivisibleCount`.
  5. After iterating through all numbers, calculate the score by multiplying `notDivisibleCount` by `divisibleCount`.
- Why this approach comes to mind first: It is a straightforward approach that directly implements the problem statement.

```cpp
int findScore(int arr[], int n, int k) {
    int divisibleCount = 0;
    int notDivisibleCount = 0;
    
    for (int i = 0; i < n; i++) {
        if (arr[i] % k == 0) {
            divisibleCount++;
        } else {
            notDivisibleCount++;
        }
    }
    
    return notDivisibleCount * divisibleCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we are iterating through the array once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the counters.
> - **Why these complexities occur:** The time complexity is linear because we are performing a constant amount of work for each element in the array, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem statement does not require any additional insights beyond the brute force approach, as the brute force approach already has a time complexity of $O(n)$, which is optimal for this problem.
- Detailed breakdown of the approach: The optimal approach is the same as the brute force approach, as it already achieves the optimal time complexity.
- Proof of optimality: The optimal time complexity for this problem is $O(n)$, because we must at least read the input array once to calculate the score.
- Why further optimization is impossible: Further optimization is impossible because we must at least read the input array once, which takes $O(n)$ time.

```cpp
int findScore(int arr[], int n, int k) {
    int divisibleCount = 0;
    int notDivisibleCount = 0;
    
    for (int i = 0; i < n; i++) {
        if (arr[i] % k == 0) {
            divisibleCount++;
        } else {
            notDivisibleCount++;
        }
    }
    
    return notDivisibleCount * divisibleCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the counters.
> - **Optimality proof:** The time complexity is optimal because we must at least read the input array once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and basic arithmetic operations.
- Problem-solving patterns identified: Direct implementation of the problem statement.
- Optimization techniques learned: None, as the brute force approach is already optimal.
- Similar problems to practice: Other problems that involve basic arithmetic operations and iteration.

**Mistakes to Avoid:**
- Common implementation errors: Off-by-one errors, incorrect use of the modulo operator, and incorrect initialization of counters.
- Edge cases to watch for: Empty input arrays, arrays with a single element, and arrays with all elements divisible by `k`.
- Performance pitfalls: Using inefficient algorithms or data structures that scale poorly with the input size.
- Testing considerations: Test the function with a variety of input arrays and values of `k` to ensure correctness.