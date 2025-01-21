## Sum of All Odd Length Subarrays

**Problem Link:** https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description

**Problem Statement:**
- Input: An integer array `arr` of size `n`.
- Constraints: `1 <= n <= 100`, `1 <= arr[i] <= 1000`.
- Expected output: The sum of all elements in all odd-length subarrays.
- Key requirements: Calculate the sum of all elements in subarrays with odd lengths.
- Edge cases: Handle arrays with a single element, and arrays with all elements being the same.

**Example Test Cases:**
- Input: `arr = [1, 2, 3, 4, 5, 6]`
- Output: `58`
- Explanation: The odd-length subarrays are `[1]`, `[2]`, `[3]`, `[4]`, `[5]`, `[6]`, `[1, 2, 3]`, `[2, 3, 4]`, `[3, 4, 5]`, `[4, 5, 6]`, `[1, 2, 3, 4, 5]`, `[2, 3, 4, 5, 6]`, `[1, 2, 3, 4, 5, 6]`. The sum of all elements in these subarrays is `1 + 2 + 3 + 4 + 5 + 6 + 1 + 2 + 3 + 2 + 3 + 4 + 3 + 4 + 5 + 4 + 5 + 6 + 1 + 2 + 3 + 4 + 5 + 2 + 3 + 4 + 5 + 6 + 1 + 2 + 3 + 4 + 5 + 6 = 58`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible subarrays and check if their length is odd.
- Step-by-step breakdown:
  1. Generate all possible subarrays.
  2. Check if the length of each subarray is odd.
  3. If the length is odd, calculate the sum of its elements.
  4. Add the sum to the total sum.
- This approach comes to mind first because it directly addresses the problem statement.

```cpp
int sumOddLengthSubarrays(vector<int>& arr) {
    int n = arr.size();
    int sum = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int len = j - i + 1;
            if (len % 2 != 0) {
                for (int k = i; k <= j; k++) {
                    sum += arr[k];
                }
            }
        }
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the size of the input array. This is because we have three nested loops: one to generate subarrays, one to check the length, and one to calculate the sum.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the sum and the current subarray.
> - **Why these complexities occur:** The time complexity is cubic because we generate all possible subarrays and check each one's length. The space complexity is constant because we don't use any additional data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use the concept of contribution of each element to the total sum.
- Each element will be part of multiple odd-length subarrays.
- We can calculate the contribution of each element by considering the number of odd-length subarrays it will be part of.
- Step-by-step breakdown:
  1. Calculate the contribution of each element.
  2. Sum up the contributions of all elements.

```cpp
int sumOddLengthSubarrays(vector<int>& arr) {
    int n = arr.size();
    int sum = 0;
    for (int i = 0; i < n; i++) {
        int contribution = 0;
        for (int j = i; j < n; j++) {
            int len = j - i + 1;
            if (len % 2 != 0) {
                contribution += arr[i];
            }
        }
        sum += contribution;
    }
    return sum;
}
```

However, this can be further optimized by directly calculating the contribution of each element without generating all subarrays.

```cpp
int sumOddLengthSubarrays(vector<int>& arr) {
    int n = arr.size();
    int sum = 0;
    for (int i = 0; i < n; i++) {
        int contribution = 0;
        for (int j = 0; j <= i; j++) {
            for (int k = i; k < n; k++) {
                int len = k - j + 1;
                if (len % 2 != 0) {
                    contribution += 1;
                }
            }
        }
        sum += contribution * arr[i];
    }
    return sum;
}
```

But we can simplify it even more by noticing the pattern in the contribution of each element.

For an element at index `i`, it will be part of `(i + 1) * (n - i)` subarrays in total. Half of these will be odd-length subarrays (when `i` is even) or half will be even-length subarrays (when `i` is odd), due to the symmetry of subarray lengths around the middle element.

However, we can calculate the exact contribution of each element to the sum of odd-length subarrays directly using a formula derived from the pattern of subarray lengths.

```cpp
int sumOddLengthSubarrays(vector<int>& arr) {
    int n = arr.size();
    int sum = 0;
    for (int i = 0; i < n; i++) {
        for (int len = 1; len <= n; len += 2) {
            if (i - len / 2 >= 0 && i + len / 2 < n) {
                sum += arr[i];
            }
        }
    }
    return sum;
}
```

Or, using a mathematical approach to calculate the number of times each element appears in an odd-length subarray.

```cpp
int sumOddLengthSubarrays(vector<int>& arr) {
    int n = arr.size();
    int sum = 0;
    for (int i = 0; i < n; i++) {
        int count = (i + 1) * (n - i);
        if (count % 2 == 0) {
            count /= 2;
        } else {
            count = (count + 1) / 2;
        }
        sum += count * arr[i];
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ for the first optimized version, and $O(n)$ for the final version after simplification.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the sum and the current element's contribution.
> - **Optimality proof:** The final version is optimal because it directly calculates the contribution of each element to the sum of odd-length subarrays in linear time, without generating all subarrays. This is the best possible time complexity for this problem, as we must at least read the input array once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: generating subarrays, calculating contributions of elements, and optimizing using mathematical insights.
- Problem-solving patterns identified: breaking down the problem into smaller parts, using symmetry and patterns to simplify calculations.
- Optimization techniques learned: reducing the number of iterations, using mathematical formulas to calculate contributions directly.
- Similar problems to practice: other problems involving subarrays and sums, such as finding the maximum sum of a subarray or the sum of all subarrays.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, not validating input, not optimizing the solution.
- Edge cases to watch for: arrays with a single element, arrays with all elements being the same, empty arrays.
- Performance pitfalls: using brute force approaches, not optimizing the solution, using unnecessary data structures.
- Testing considerations: testing with small and large inputs, testing with edge cases, testing with different types of inputs (e.g., positive and negative numbers).