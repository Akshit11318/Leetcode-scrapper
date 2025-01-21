## Lexicographical Numbers

**Problem Link:** https://leetcode.com/problems/lexicographical-numbers/description

**Problem Statement:**
- Input format: An integer `n` representing the upper limit of the range of numbers.
- Constraints: `1 <= n <= 500`
- Expected output format: A list of integers from `1` to `n` in lexicographical order.
- Key requirements and edge cases to consider:
  - Handling numbers with varying lengths (e.g., `1`, `10`, `100`).
  - Ensuring lexicographical order, which means comparing numbers as strings.
- Example test cases with explanations:
  - For `n = 13`, the output should be `[1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]`.
  - For `n = 2`, the output should be `[1, 2]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Convert each number to a string and sort them lexicographically.
- Step-by-step breakdown of the solution:
  1. Generate a list of numbers from `1` to `n`.
  2. Convert each number to a string.
  3. Sort the list of strings.
  4. Convert the sorted strings back to integers.
- Why this approach comes to mind first: It directly addresses the requirement for lexicographical order by treating numbers as strings.

```cpp
vector<int> lexicalOrder(int n) {
    vector<int> result;
    for (int i = 1; i <= n; i++) {
        result.push_back(i);
    }
    // Convert to string, sort, and convert back to int
    sort(result.begin(), result.end(), [](int a, int b) {
        return to_string(a) < to_string(b);
    });
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation.
> - **Space Complexity:** $O(n)$ for storing the list of numbers.
> - **Why these complexities occur:** Sorting $n$ elements typically requires $O(n \log n)$ time, and storing $n$ numbers requires $O(n)$ space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using a queue to simulate the lexicographical order generation process.
- Detailed breakdown of the approach:
  1. Start with the number `1` in the queue.
  2. For each number in the queue, generate its next possible numbers by appending `0`, `1`, `2`, ..., `9` if the resulting number does not exceed `n`.
  3. Continue this process until the queue is empty, ensuring that numbers are generated and added to the result in lexicographical order.
- Proof of optimality: This approach avoids unnecessary comparisons and directly generates numbers in lexicographical order, minimizing the number of operations.

```cpp
vector<int> lexicalOrder(int n) {
    vector<int> result;
    int curr = 1;
    for (int i = 1; i <= n; i++) {
        result.push_back(curr);
        if (curr * 10 <= n) {
            curr *= 10;
        } else {
            if (curr >= n) {
                curr /= 10;
            }
            curr++;
            while (curr % 10 == 0) {
                curr /= 10;
            }
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, as each number from `1` to `n` is processed once.
> - **Space Complexity:** $O(n)$ for storing the result.
> - **Optimality proof:** This approach ensures that each number is generated exactly once and in lexicographical order, making it optimal for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Lexicographical sorting and queue-based generation.
- Problem-solving patterns identified: Direct generation of results in the required order can be more efficient than sorting.
- Optimization techniques learned: Avoiding unnecessary comparisons and using queues for efficient generation.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect handling of edge cases (e.g., numbers with varying lengths).
- Edge cases to watch for: Handling numbers that exceed `n` when appending digits.
- Performance pitfalls: Using inefficient sorting algorithms or unnecessary operations.
- Testing considerations: Thoroughly testing with different values of `n` and edge cases.