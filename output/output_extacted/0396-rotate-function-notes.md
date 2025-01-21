## Rotate Function

**Problem Link:** https://leetcode.com/problems/rotate-function/description

**Problem Statement:**
- Input: An array `A` of integers representing a function `F(0) = 0`, `F(1) = A[0]`, `F(2) = A[0] + A[1]`, ..., `F(n) = A[0] + A[1] + ... + A[n-1]`.
- Constraints: `1 <= A.length <= 10^5`, `0 <= A[i] <= 10^5`.
- Expected Output: The maximum value of the function `F(k)` for any rotation `k`.
- Key Requirements: The function `F(k)` is defined as the sum of the products of each element in the array `A` and its `1`-based index after rotating `k` steps.
- Example Test Cases:
  - Input: `A = [4, 3, 2, 6]`
  - Output: `26`
  - Explanation: After rotating `3` steps, `A` becomes `[6, 4, 3, 2]`. The function `F(3)` is `6*1 + 4*2 + 3*3 + 2*4 = 26`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward approach is to calculate the function `F(k)` for each possible rotation `k` and keep track of the maximum value.
- Step-by-step breakdown:
  1. Iterate over each possible rotation `k`.
  2. For each rotation `k`, calculate the function `F(k)` by summing the products of each element in the rotated array `A` and its `1`-based index.
  3. Update the maximum value of `F(k)` if the current value is greater.
- Why this approach comes to mind first: It is the most intuitive way to solve the problem, as it directly implements the definition of the function `F(k)`.

```cpp
int maxRotateFunction(vector<int>& A) {
    int n = A.size();
    int maxVal = INT_MIN;
    for (int k = 0; k < n; k++) {
        int sum = 0;
        for (int i = 0; i < n; i++) {
            int idx = (i + k) % n;
            sum += idx * A[idx];
        }
        maxVal = max(maxVal, sum);
    }
    return maxVal;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the array `A`. This is because we have two nested loops: one for each rotation `k` and one for calculating the function `F(k)` for each rotation.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum value of `F(k)`.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the nested loops, but it has a low space complexity since we only need to store a single variable to keep track of the maximum value.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The function `F(k)` can be calculated in $O(1)$ time using the following formula: `F(k) = F(k-1) + sum - n * A[n-k]`, where `sum` is the sum of all elements in the array `A`.
- Detailed breakdown:
  1. Calculate the initial value of `F(0)`.
  2. Calculate the sum of all elements in the array `A`.
  3. Iterate over each possible rotation `k`, updating the value of `F(k)` using the formula.
  4. Update the maximum value of `F(k)` if the current value is greater.
- Proof of optimality: This approach has a time complexity of $O(n)$, which is optimal since we need to iterate over the array at least once to calculate the function `F(k)`.

```cpp
int maxRotateFunction(vector<int>& A) {
    int n = A.size();
    int maxVal = 0;
    int sum = 0;
    int f = 0;
    for (int i = 0; i < n; i++) {
        sum += A[i];
        f += i * A[i];
    }
    maxVal = f;
    for (int k = 1; k < n; k++) {
        f = f + sum - n * A[n-k];
        maxVal = max(maxVal, f);
    }
    return maxVal;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the array `A`. This is because we only need to iterate over the array once to calculate the initial value of `F(0)` and the sum of all elements.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum value of `F(k)` and the sum of all elements.
> - **Optimality proof:** This approach is optimal since we only need to iterate over the array once to calculate the function `F(k)` for each rotation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Dynamic programming, formula derivation.
- Problem-solving patterns: Using formulas to reduce time complexity.
- Optimization techniques: Reducing the number of iterations.
- Similar problems to practice: Other problems involving dynamic programming and formula derivation.

**Mistakes to Avoid:**
- Not considering the formula derivation approach.
- Not optimizing the time complexity.
- Not handling edge cases correctly.
- Not testing the solution thoroughly.