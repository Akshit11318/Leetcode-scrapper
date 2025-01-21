## Defuse the Bomb

**Problem Link:** https://leetcode.com/problems/defuse-the-bomb/description

**Problem Statement:**
- Input format and constraints: Given an array of integers `code` and an integer `k`, defuse the bomb by finding the difference between each element and the element `k` positions ahead.
- Expected output format: Return the resulting array after defusing the bomb.
- Key requirements and edge cases to consider: When `k` positions ahead is out of bounds, wrap around to the start of the array.
- Example test cases with explanations:
  - Example 1: `code = [5,7,1,8], k = 3`, Output: `[12,10,16,13]`
  - Example 2: `code = [1,2,3,4], k = 0`, Output: `[0,0,0,0]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over the `code` array and for each element, calculate the difference between it and the element `k` positions ahead, wrapping around to the start of the array if necessary.
- Step-by-step breakdown of the solution:
  1. Initialize an empty array `result` to store the differences.
  2. Iterate over the `code` array with index `i`.
  3. For each element, calculate the index of the element `k` positions ahead, considering wrap-around.
  4. Calculate the difference between the current element and the element `k` positions ahead.
  5. Append the difference to the `result` array.
- Why this approach comes to mind first: It directly follows from understanding the problem statement and is a straightforward implementation.

```cpp
vector<int> decrypt(vector<int>& code, int k) {
    int n = code.size();
    vector<int> result(n);
    if (k == 0) return vector<int>(n, 0); // If k is 0, all differences are 0
    
    for (int i = 0; i < n; i++) {
        int sum = 0;
        for (int j = 1; j <= abs(k); j++) {
            int nextIndex = (i + (k > 0 ? j : -j)) % n;
            if (k > 0) sum += code[nextIndex];
            else sum -= code[nextIndex];
        }
        result[i] = sum;
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the size of the `code` array and $k$ is the given integer. This is because for each element in the array, we potentially iterate $k$ times.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the `code` array. This is for storing the result array.
> - **Why these complexities occur:** The time complexity is due to the nested loop structure, and the space complexity is due to the need to store the result array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Recognize that the brute force approach can be optimized by observing the pattern of differences and utilizing the fact that when `k` positions ahead is out of bounds, we wrap around to the start of the array. For `k > 0`, we can calculate the sum of the next `k` elements directly and efficiently.
- Detailed breakdown of the approach:
  1. Handle the case where `k == 0` by returning an array of zeros.
  2. For `k > 0`, initialize the sum of the next `k` elements.
  3. Iterate over the `code` array, updating the sum by subtracting the element that is no longer included and adding the new element that is `k` positions ahead, considering wrap-around.
- Proof of optimality: This approach has a significant reduction in time complexity compared to the brute force method because it avoids the nested loop structure.
- Why further optimization is impossible: The problem requires calculating a difference for each element in the array, and the optimal approach does so in a single pass, making it linear in terms of the array size.

```cpp
vector<int> decrypt(vector<int>& code, int k) {
    int n = code.size();
    if (k == 0) return vector<int>(n, 0);
    
    vector<int> result(n);
    if (k > 0) {
        int sum = 0;
        for (int i = 0; i < k; i++) sum += code[i];
        for (int i = 0; i < n; i++) {
            result[i] = sum;
            sum = sum - code[(i % n)] + code[((i + k) % n)];
        }
    } else {
        k = abs(k);
        int sum = 0;
        for (int i = n - k; i < n; i++) sum += code[i];
        for (int i = 0; i < n; i++) {
            result[i] = sum;
            sum = sum - code[((i + n - k) % n)] + code[(i % n)];
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the `code` array. This is because we make a single pass through the array.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the `code` array. This is for storing the result array.
> - **Optimality proof:** This approach is optimal because it achieves the calculation in a single pass, reducing the time complexity significantly compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Efficient calculation of cumulative sums and handling of wrap-around conditions.
- Problem-solving patterns identified: Recognizing the potential for optimizing nested loop structures by observing patterns in the data.
- Optimization techniques learned: Utilizing the properties of the problem to reduce computational complexity.
- Similar problems to practice: Problems involving arrays and requiring efficient calculation of sums or differences, such as sliding window problems.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases properly, such as when `k` is zero or negative.
- Edge cases to watch for: Wrap-around conditions and handling of negative `k`.
- Performance pitfalls: Implementing a brute force approach without considering optimizations.
- Testing considerations: Thoroughly testing with various inputs, including edge cases like `k = 0`, `k > n`, and negative `k`.