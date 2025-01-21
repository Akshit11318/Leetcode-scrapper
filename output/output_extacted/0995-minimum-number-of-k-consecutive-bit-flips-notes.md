## Minimum Number of K-Consecutive Bit Flips
**Problem Link:** https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/description

**Problem Statement:**
- Input format: A binary string `nums` and an integer `k`.
- Constraints: `1 <= k <= nums.length <= 10^4`, `nums` consists only of `0`s and `1`s.
- Expected output format: The minimum number of `k`-consecutive bit flips required to make all bits in `nums` equal.
- Key requirements and edge cases to consider:
  - Handling cases where `k` is larger than the remaining length of `nums`.
  - Determining the impact of flipping bits on the overall count of flips.
- Example test cases with explanations:
  - `nums = "00110", k = 2` should return `2` because we can flip the first two bits to get `11`, and then flip the next two bits to get `00`, resulting in `1100`, which is all equal.
  - `nums = "01010", k = 2` should return `0` because the string is already composed of alternating bits and no flips are needed.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Consider every possible sequence of flips and check if it leads to a solution where all bits are equal.
- Step-by-step breakdown of the solution:
  1. Iterate through all possible lengths of flips (from `1` to `k`).
  2. For each length, iterate through all possible start positions in `nums`.
  3. Flip the bits in the current window and check if all bits in `nums` are now equal.
  4. If they are, count this as a valid flip sequence.
- Why this approach comes to mind first: It's a straightforward enumeration of all possibilities, which is often the first step in solving combinatorial problems.

```cpp
int minKBitFlips(string nums, int k) {
    int n = nums.length();
    int res = 0;
    for (int i = 0; i < n; i++) {
        if (nums[i] == '0') {
            // Try flipping
            if (i + k <= n) {
                res++;
                // Flip bits
                for (int j = i; j < i + k; j++) {
                    nums[j] = (nums[j] == '0') ? '1' : '0';
                }
            }
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$ because for each of the `n` positions, we potentially flip `k` bits.
> - **Space Complexity:** $O(1)$ because we modify the input string in-place and use a constant amount of space to store the result.
> - **Why these complexities occur:** The brute force approach involves iterating through the string and for each position, potentially flipping `k` bits, leading to a time complexity of $O(n \cdot k)$. The space complexity is $O(1)$ because we only use a constant amount of space to store our result and we modify the input string in-place.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of trying all possible flips, maintain a queue of flips that have been applied but not yet "expired". This allows us to efficiently keep track of the parity of bits without actually flipping them.
- Detailed breakdown of the approach:
  1. Initialize a queue to store the indices of flips that have been applied.
  2. Iterate through `nums`. For each bit:
     - If the bit is `0` and there are no pending flips, apply a flip and increment the result.
     - If the bit is `1` and there are no pending flips, do nothing because the bit is already in the desired state.
     - If there are pending flips, check if the current bit's state matches the expected state given the pending flips. If not, apply a new flip.
  3. When a flip expires (i.e., we've moved `k` positions past its start), remove it from the queue.
- Proof of optimality: This approach ensures that we only apply flips when necessary and keep track of the effects of previous flips efficiently, minimizing the number of flips required.

```cpp
int minKBitFlips(string nums, int k) {
    int n = nums.length();
    int res = 0;
    queue<int> flips;
    for (int i = 0; i < n; i++) {
        if (!flips.empty() && flips.front() + k == i) flips.pop();
        if ((nums[i] - '0') == (flips.size() % 2)) {
            if (i + k > n) return -1; // Impossible to make all bits equal
            res++;
            flips.push(i);
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we iterate through `nums` once and perform constant time operations for each bit.
> - **Space Complexity:** $O(n)$ because in the worst case, we might have to store every index in the queue.
> - **Optimality proof:** This approach is optimal because it only applies flips when necessary (i.e., when the current bit does not match the expected state given previous flips) and keeps track of the effects of previous flips efficiently using a queue, ensuring that we minimize the number of flips required to make all bits equal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Queue data structure, efficient tracking of bit flips.
- Problem-solving patterns identified: Using a queue to keep track of "pending" operations (in this case, bit flips) and updating the result based on the state of these operations.
- Optimization techniques learned: Minimizing the number of operations (flips) by only applying them when necessary and using a data structure (queue) to efficiently manage the state of these operations.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to remove expired flips from the queue, incorrectly updating the result based on the state of pending flips.
- Edge cases to watch for: Handling cases where `k` is larger than the remaining length of `nums`, ensuring that the approach correctly handles the parity of bits given the pending flips.
- Performance pitfalls: Using an inefficient data structure or algorithm that results in unnecessary flips or excessive computation.
- Testing considerations: Thoroughly testing the approach with various inputs, including edge cases, to ensure correctness and efficiency.