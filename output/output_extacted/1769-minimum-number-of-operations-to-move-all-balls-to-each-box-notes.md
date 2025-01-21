## Minimum Number of Operations to Move All Balls to Each Box
**Problem Link:** https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description

**Problem Statement:**
- Input format and constraints: The input is a string `boxes` consisting of `0`s and `1`s, where `0` represents an empty box and `1` represents a box with a ball. The length of the string is denoted by `n`.
- Expected output format: The output should be an array of integers, where the `i-th` element represents the minimum number of operations required to move all balls to the `i-th` box.
- Key requirements and edge cases to consider: The input string will only contain `0`s and `1`s, and the length of the string will be between `1` and `1000`.
- Example test cases with explanations: 
    - Input: `boxes = "110"`
      Output: `[1,1,3]`
      Explanation: To move all balls to the first box, we need 1 operation (move the ball from the second box to the first box). To move all balls to the second box, we need 1 operation (move the ball from the first box to the second box). To move all balls to the third box, we need 3 operations (move both balls from the first and second boxes to the third box).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over each box and calculating the minimum number of operations required to move all balls to that box.
- Step-by-step breakdown of the solution:
    1. Initialize an array `operations` of size `n` to store the minimum number of operations required for each box.
    2. Iterate over each box `i` from `0` to `n-1`.
    3. For each box `i`, iterate over each ball `j` in the string `boxes`.
    4. Calculate the distance between the current box `i` and the ball `j` using the formula `abs(i - j)`.
    5. Add the distance to the total operations required for the current box `i`.
- Why this approach comes to mind first: The brute force approach is straightforward and involves iterating over each box and calculating the minimum number of operations required.

```cpp
vector<int> minOperations(string boxes) {
    int n = boxes.size();
    vector<int> operations(n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (boxes[j] == '1') {
                operations[i] += abs(i - j);
            }
        }
    }
    return operations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the input string. This is because we have two nested loops iterating over the string.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we need to store the minimum number of operations required for each box.
> - **Why these complexities occur:** The time complexity is $O(n^2)$ because we have two nested loops, and the space complexity is $O(n)$ because we need to store the minimum number of operations required for each box.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can calculate the minimum number of operations required for each box in a single pass by maintaining a running sum of the distances.
- Detailed breakdown of the approach:
    1. Initialize an array `operations` of size `n` to store the minimum number of operations required for each box.
    2. Initialize two variables `balls` and `distance` to `0`.
    3. Iterate over each box `i` from `0` to `n-1`.
    4. For each box `i`, if the current box contains a ball (`boxes[i] == '1'`), increment the `balls` count and add the current distance to the `operations[i]`.
    5. Update the `distance` by adding the difference between the current box and the previous box (`i - (balls - 1)`).
- Why further optimization is impossible: The optimal approach has a time complexity of $O(n)$, which is the best possible time complexity for this problem.

```cpp
vector<int> minOperations(string boxes) {
    int n = boxes.size();
    vector<int> operations(n);
    for (int i = 0; i < n; i++) {
        int balls = 0, distance = 0;
        for (int j = 0; j <= i; j++) {
            if (boxes[j] == '1') {
                balls++;
                distance += i - j;
            }
        }
        for (int j = i + 1; j < n; j++) {
            if (boxes[j] == '1') {
                distance += j - i;
            }
        }
        operations[i] = distance;
    }
    return operations;
}
```

However, we can optimize this further by using the fact that the distance between two points is symmetric. 

```cpp
vector<int> minOperations(string boxes) {
    int n = boxes.size();
    vector<int> operations(n);
    for (int i = 0; i < n; i++) {
        int distance = 0;
        for (int j = 0; j < n; j++) {
            if (boxes[j] == '1') {
                distance += abs(i - j);
            }
        }
        operations[i] = distance;
    }
    return operations;
}
```

And we can optimize it even further by using prefix sum.

```cpp
vector<int> minOperations(string boxes) {
    int n = boxes.size();
    vector<int> operations(n);
    vector<int> prefix(n + 1);
    for (int i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + (boxes[i] == '1' ? i : 0);
    }
    for (int i = 0; i < n; i++) {
        int left = prefix[i];
        int right = prefix[n] - prefix[i + 1] - (i + 1) * (n - i - 1 - (prefix[n] - prefix[i + 1]));
        operations[i] = left + right;
    }
    return operations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we have a single loop iterating over the string.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we need to store the minimum number of operations required for each box.
> - **Optimality proof:** The optimal approach has a time complexity of $O(n)$, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of prefix sum and symmetric distance calculation.
- Problem-solving patterns identified: The problem requires the use of dynamic programming and prefix sum to optimize the solution.
- Optimization techniques learned: The problem demonstrates the use of prefix sum and symmetric distance calculation to optimize the solution.
- Similar problems to practice: Problems that involve calculating minimum distances or using prefix sum, such as the "Minimum Average Difference" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty input string.
- Edge cases to watch for: The input string may be empty, or it may contain only `0`s or only `1`s.
- Performance pitfalls: Not using prefix sum or symmetric distance calculation, which can lead to a time complexity of $O(n^2)$.
- Testing considerations: Test the solution with different input strings, including edge cases, to ensure that it works correctly.