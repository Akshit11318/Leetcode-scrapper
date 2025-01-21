## Total Hamming Distance
**Problem Link:** https://leetcode.com/problems/total-hamming-distance/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 10^4`, `0 <= nums[i] <= 10^9`.
- Expected output format: The total Hamming distance between all pairs of elements.
- Key requirements and edge cases to consider: Handle large input arrays and integer values.
- Example test cases with explanations:
  - Example 1: `nums = [4, 14, 2]`, Output: `6`.
  - Example 2: `nums = [4, 14, 4]`, Output: `4`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the Hamming distance between each pair of numbers in the array and sum them up.
- Step-by-step breakdown of the solution:
  1. Iterate through the array for each pair of numbers.
  2. For each pair, calculate the Hamming distance by performing a bitwise XOR operation and counting the number of bits set.
  3. Sum up the Hamming distances for all pairs.
- Why this approach comes to mind first: Directly calculating the Hamming distance between all pairs seems like the most straightforward way to solve the problem.

```cpp
int totalHammingDistance(vector<int>& nums) {
    int n = nums.size();
    int totalDistance = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int xorResult = nums[i] ^ nums[j];
            int hammingDistance = 0;
            while (xorResult) {
                hammingDistance += xorResult & 1;
                xorResult >>= 1;
            }
            totalDistance += hammingDistance;
        }
    }
    return totalDistance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot \log{M})$, where $n$ is the number of elements and $M$ is the maximum value in the array. This is because we are iterating over all pairs of numbers and for each pair, we are performing a bitwise operation that takes $O(\log{M})$ time.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array, as we only use a constant amount of space.
> - **Why these complexities occur:** The nested loops cause the $O(n^2)$ term, and the bitwise operations inside the loop contribute the $O(\log{M})$ factor.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of calculating the Hamming distance between each pair of numbers, we can calculate the contribution of each bit position across all numbers. For each bit position, the number of pairs that contribute to the Hamming distance is the product of the number of elements with the bit set and the number of elements with the bit unset.
- Detailed breakdown of the approach:
  1. Iterate through each bit position.
  2. For each bit position, count the number of elements with the bit set and the number of elements with the bit unset.
  3. Calculate the contribution of this bit position to the total Hamming distance.
  4. Sum up the contributions from all bit positions.
- Proof of optimality: This approach avoids calculating the Hamming distance for each pair of numbers, reducing the time complexity significantly.

```cpp
int totalHammingDistance(vector<int>& nums) {
    int n = nums.size();
    int totalDistance = 0;
    for (int i = 0; i < 30; i++) { // Assuming 30-bit integers
        int ones = 0, zeros = 0;
        for (int num : nums) {
            if (num & (1 << i)) ones++;
            else zeros++;
        }
        totalDistance += ones * zeros;
    }
    return totalDistance;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot \log{M})$, where $n$ is the number of elements and $M$ is the maximum value in the array. This is because we are iterating over all elements for each bit position.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Optimality proof:** This approach has the best possible time complexity because we must at least read the input once, and the bit manipulation operations are necessary to calculate the Hamming distance.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation, counting, and optimization techniques.
- Problem-solving patterns identified: Looking for ways to avoid redundant calculations and using bit-level operations to simplify problems.
- Optimization techniques learned: Avoiding unnecessary calculations by considering the properties of the problem.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, such as when the input array is empty.
- Edge cases to watch for: Large input arrays, integer overflow, and bit manipulation errors.
- Performance pitfalls: Using inefficient algorithms or data structures, such as calculating the Hamming distance for each pair of numbers.
- Testing considerations: Thoroughly testing the solution with various input sizes and values to ensure correctness and performance.