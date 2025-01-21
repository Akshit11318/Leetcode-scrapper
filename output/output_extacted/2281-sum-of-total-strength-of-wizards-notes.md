## Sum of Total Strength of Wizards
**Problem Link:** https://leetcode.com/problems/sum-of-total-strength-of-wizards/description

**Problem Statement:**
- Input format and constraints: Given an array `strength` of length `n`, where `strength[i]` represents the strength of the `i-th` wizard.
- Expected output format: The total strength of all wizards.
- Key requirements and edge cases to consider: The strength of a wizard is calculated as the sum of the strengths of all wizards in the range `[i - k, i + k]`, where `k` is the number of wizards to the left and right of the current wizard. If `k` is greater than the distance to the boundary, only include the wizards within the boundary.
- Example test cases with explanations: For example, given `strength = [1, 3, 1, 2]`, the total strength of all wizards is `1 + 3 + 1 + 2 = 7`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the total strength for each wizard by summing the strengths of all wizards in the range `[i - k, i + k]`.
- Step-by-step breakdown of the solution:
  1. Iterate over each wizard in the array.
  2. For each wizard, iterate over the range `[i - k, i + k]` and sum the strengths of all wizards in this range.
  3. Add the sum of strengths in the range to the total strength.
- Why this approach comes to mind first: This approach is straightforward and directly calculates the total strength for each wizard.

```cpp
int totalStrength(vector<int>& strength) {
    int n = strength.size();
    long long total = 0;
    for (int i = 0; i < n; i++) {
        for (int k = 0; k <= n; k++) {
            long long sum = 0;
            for (int j = max(0, i - k); j <= min(n - 1, i + k); j++) {
                sum += strength[j];
            }
            total += sum * strength[i];
        }
    }
    return total % (int)(1e9 + 7);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of wizards. This is because we have three nested loops: one to iterate over each wizard, one to iterate over the range `[i - k, i + k]`, and one to sum the strengths in this range.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the total strength and the sum of strengths in the range.
> - **Why these complexities occur:** The time complexity occurs because we have three nested loops, and the space complexity occurs because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a prefix sum array to calculate the sum of strengths in the range `[i - k, i + k]` in constant time.
- Detailed breakdown of the approach:
  1. Create a prefix sum array `prefix` where `prefix[i]` is the sum of strengths from index `0` to `i`.
  2. Iterate over each wizard in the array.
  3. For each wizard, iterate over the range `[0, n]` and calculate the sum of strengths in the range `[i - k, i + k]` using the prefix sum array.
  4. Add the sum of strengths in the range to the total strength.
- Proof of optimality: This approach is optimal because we only iterate over the array once and use a prefix sum array to calculate the sum of strengths in the range in constant time.

```cpp
int totalStrength(vector<int>& strength) {
    int n = strength.size();
    long long total = 0;
    for (int i = 0; i < n; i++) {
        for (int k = 0; k <= n; k++) {
            long long sum = 0;
            int left = max(0, i - k);
            int right = min(n - 1, i + k);
            for (int j = left; j <= right; j++) {
                sum += strength[j];
            }
            total = (total + sum * strength[i]) % (int)(1e9 + 7);
        }
    }
    return total;
}
```

However, this can still be optimized by using a prefix sum array.

```cpp
int totalStrength(vector<int>& strength) {
    int n = strength.size();
    long long total = 0;
    vector<long long> prefix(n + 1);
    for (int i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + strength[i];
    }
    for (int i = 0; i < n; i++) {
        for (int k = 0; k <= n; k++) {
            int left = max(0, i - k);
            int right = min(n - 1, i + k);
            long long sum = prefix[right + 1] - prefix[left];
            total = (total + sum * strength[i]) % (int)(1e9 + 7);
        }
    }
    return total;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of wizards. This is because we have two nested loops: one to iterate over each wizard and one to iterate over the range `[0, n]`.
> - **Space Complexity:** $O(n)$, as we use a prefix sum array to store the sum of strengths from index `0` to `i`.
> - **Optimality proof:** This approach is optimal because we only iterate over the array twice and use a prefix sum array to calculate the sum of strengths in the range in constant time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prefix sum array, iteration over a range, and calculation of sum of strengths in a range.
- Problem-solving patterns identified: Using a prefix sum array to calculate the sum of strengths in a range in constant time.
- Optimization techniques learned: Using a prefix sum array to reduce the time complexity from $O(n^3)$ to $O(n^2)$.

**Mistakes to Avoid:**
- Common implementation errors: Not using a prefix sum array to calculate the sum of strengths in the range.
- Edge cases to watch for: The range `[i - k, i + k]` may exceed the boundary of the array.
- Performance pitfalls: Not using a prefix sum array to reduce the time complexity.
- Testing considerations: Test the code with different inputs and edge cases to ensure it works correctly.