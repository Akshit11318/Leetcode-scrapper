## 1-Bit and 2-Bit Characters

**Problem Link:** https://leetcode.com/problems/1-bit-and-2-bit-characters/description

**Problem Statement:**
- Input: A binary array `bits`.
- Constraints: `1 <= bits.length <= 1000`, `bits[i]` is either `0` or `1`.
- Expected output: `true` if the last character must be a 1-bit character, `false` otherwise.
- Key requirements: Determine whether the last character must be a 1-bit character based on the given binary array.
- Example test cases:
  - Input: `[1, 0, 1]`, Output: `true`
  - Input: `[1, 1, 1]`, Output: `false`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try to decode the bits from left to right, keeping track of whether we are currently processing a 1-bit or 2-bit character.
- Step-by-step breakdown of the solution:
  1. Initialize an index `i` to 0.
  2. Loop through the bits array until we reach the end.
  3. If the current bit is 0, it must be a 1-bit character, so increment `i` by 1.
  4. If the current bit is 1, it must be the start of a 2-bit character, so increment `i` by 2.
  5. If `i` is equal to the length of the bits array after the loop, the last character must be a 1-bit character.
- Why this approach comes to mind first: It directly follows the problem statement and tries to simulate the decoding process.

```cpp
bool isOneBitCharacter(vector<int>& bits) {
    int i = 0;
    while (i < bits.size()) {
        if (bits[i] == 0) {
            i++;
        } else {
            i += 2;
        }
    }
    return i == bits.size() + 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the bits array, because we are scanning through the array once.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the index `i`.
> - **Why these complexities occur:** The time complexity is linear because we are scanning through the array once, and the space complexity is constant because we only use a fixed amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can still simulate the decoding process, but we should return `true` as soon as we reach the second last bit and it is 0, because the last bit must be a 1-bit character in this case.
- Detailed breakdown of the approach:
  1. Initialize an index `i` to 0.
  2. Loop through the bits array until we reach the second last bit.
  3. If the current bit is 0, it must be a 1-bit character, so increment `i` by 1.
  4. If the current bit is 1, it must be the start of a 2-bit character, so increment `i` by 2.
  5. If we reach the second last bit and it is 0, return `true`, because the last bit must be a 1-bit character.
  6. If we finish the loop without returning, return whether `i` is equal to the length of the bits array.
- Proof of optimality: This solution still has a linear time complexity, but it avoids unnecessary iterations by returning early when possible.

```cpp
bool isOneBitCharacter(vector<int>& bits) {
    int i = 0;
    while (i < bits.size() - 1) {
        if (bits[i] == 0) {
            i++;
        } else {
            i += 2;
        }
    }
    return i == bits.size() - 1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the bits array, because we are scanning through the array once.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the index `i`.
> - **Optimality proof:** The time complexity is still linear, but we avoid unnecessary iterations by returning early when possible. The space complexity remains constant.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Simulating a decoding process, using a loop to iterate through an array.
- Problem-solving patterns identified: Looking for early returns to avoid unnecessary iterations.
- Optimization techniques learned: Returning early when possible to reduce the number of iterations.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the second last bit and returning early.
- Edge cases to watch for: The case where the input array is empty or contains only one bit.
- Performance pitfalls: Not using a loop to iterate through the array, which can lead to exponential time complexity.
- Testing considerations: Test the function with different input arrays, including edge cases.