## Number of Subsequences with Odd Sum
**Problem Link:** https://leetcode.com/problems/number-of-subsequences-with-odd-sum/description

**Problem Statement:**
- Input: An array of integers `arr`.
- Constraints: `1 <= arr.length <= 10^5`, `1 <= arr[i] <= 10^9`.
- Expected output: The number of subsequences with an odd sum.
- Key requirements and edge cases to consider: Handling arrays with large numbers, considering empty arrays, and arrays with a single element.
- Example test cases with explanations:
  - Example 1: Input: `[1,2,3,4,5]`, Output: `16`. Explanation: The subsequences with odd sums are `[1]`, `[1,2,3]`, `[1,2,4,5]`, `[1,3]`, `[1,3,4,5]`, `[1,4,5]`, `[2,3,4,5]`, `[3]`, `[3,4,5]`, `[4,5]`, `[5]`, `[1,2,3,4]`, `[1,2,4]`, `[1,3,4]`, `[2,3,4]`, and `[3,4]`.
  - Example 2: Input: `[2,2,2]`, Output: `0`. Explanation: There are no subsequences with an odd sum because all numbers are even.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences of the input array and calculate the sum of each subsequence.
- Step-by-step breakdown of the solution:
  1. Initialize a counter for subsequences with odd sums.
  2. Generate all possible subsequences using bit manipulation (each bit represents whether an element is included in the subsequence or not).
  3. For each subsequence, calculate the sum of its elements.
  4. If the sum is odd, increment the counter.
- Why this approach comes to mind first: It's a straightforward way to consider all possible subsequences.

```cpp
int numOfSubsequencesWithOddSum(vector<int>& arr) {
    int n = arr.size();
    int count = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        int sum = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i))) {
                sum += arr[i];
            }
        }
        if (sum % 2 != 0) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of elements in the array. This is because we generate $2^n$ subsequences and for each subsequence, we calculate the sum which takes $O(n)$ time.
> - **Space Complexity:** $O(1)$, not counting the space needed for the input array. This is because we only use a constant amount of space to store the count and the mask.
> - **Why these complexities occur:** The time complexity is exponential because we consider all possible subsequences, and the space complexity is constant because we only use a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Notice that for any given element in the array, half of the subsequences that include it will have an odd sum if the element itself is odd, and half will have an even sum if the element is even. This is because adding an odd number flips the parity of the sum, and adding an even number keeps the parity the same.
- Detailed breakdown of the approach:
  1. Initialize a variable to keep track of the total number of subsequences with an odd sum.
  2. For each element in the array, consider its contribution to the total count based on its parity.
  3. If the element is odd, it will contribute to half of the subsequences (that include it) having an odd sum.
  4. If the element is even, it will not change the parity of the sum of any subsequence that includes it.
- Proof of optimality: This approach is optimal because it avoids generating all subsequences explicitly, instead, it calculates the count based on the properties of odd and even numbers.

```cpp
int numOfSubsequencesWithOddSum(vector<int>& arr) {
    long long oddCount = 0, evenCount = 1; // Initialize with 1 for the empty subsequence
    for (int num : arr) {
        if (num % 2 == 0) { // If the number is even
            oddCount = oddCount * 2; // Even doesn't change parity, so double the odd count
            evenCount = evenCount * 2; // Double the even count as well
        } else { // If the number is odd
            long long newOddCount = oddCount + evenCount; // Odd flips parity, so add even to odd
            evenCount = oddCount; // Even becomes the previous odd count
            oddCount = newOddCount; // Update odd count
        }
    }
    return oddCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, not counting the space needed for the input array. This is because we only use a constant amount of space to store the counts.
> - **Optimality proof:** This approach is optimal because it processes the array in linear time and uses constant space, which is the best we can achieve given that we must at least read the input.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation, parity analysis, and dynamic programming.
- Problem-solving patterns identified: Breaking down complex problems into simpler sub-problems and using mathematical insights to optimize the solution.
- Optimization techniques learned: Avoiding unnecessary computations by leveraging properties of the data.
- Similar problems to practice: Problems involving subsequences, parity, and combinatorics.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as empty arrays or arrays with a single element.
- Edge cases to watch for: Arrays with large numbers, and ensuring that the solution does not overflow for large inputs.
- Performance pitfalls: Using inefficient algorithms that have high time or space complexity.
- Testing considerations: Thoroughly testing the solution with a variety of inputs, including edge cases and large inputs.