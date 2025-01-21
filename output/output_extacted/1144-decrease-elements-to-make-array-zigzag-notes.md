## Decrease Elements To Make Array Zigzag

**Problem Link:** https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/description

**Problem Statement:**
- Input: An integer array `nums`.
- Constraints: `1 <= nums.length <= 1000`, `1 <= nums[i] <= 1000`.
- Expected Output: The minimum number of moves to make the array zigzag.
- Key Requirements:
  - For an array to be zigzag, every pair of adjacent elements must have different parity (one odd, one even) or be unequal.
  - A move consists of decreasing an element by 1.
- Edge Cases:
  - Empty array
  - Array with a single element
- Example Test Cases:
  - `nums = [1,2,3]`: The array can be made zigzag by decreasing the second element to 1 (resulting in `[1,1,3]`) and then decreasing the third element to 2 (resulting in `[1,1,2]`), which requires 2 moves.
  - `nums = [9,6,1,6,2]`: The array can be made zigzag by decreasing the first element to 8, the third element to 0, and the fifth element to 1 (resulting in `[8,6,0,6,1]`), which requires 4 moves.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible combination of decreases for each element to see if the resulting array is zigzag.
- This approach is straightforward but inefficient due to its exponential time complexity.

```cpp
int movesToMakeZigzag(vector<int>& nums) {
    int n = nums.size();
    int minMoves = INT_MAX;

    // Generate all possible binary sequences of length n
    for (int mask = 0; mask < (1 << n); mask++) {
        vector<int> arr = nums;
        int moves = 0;

        // Apply the decrease operation based on the binary sequence
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i))) {
                while (i > 0 && arr[i] <= arr[i-1]) {
                    arr[i]--;
                    moves++;
                }
                while (i < n-1 && arr[i] <= arr[i+1]) {
                    arr[i]--;
                    moves++;
                }
            }
        }

        // Check if the resulting array is zigzag
        bool isZigzag = true;
        for (int i = 0; i < n-1; i++) {
            if (arr[i] == arr[i+1]) {
                isZigzag = false;
                break;
            }
        }

        if (isZigzag) {
            minMoves = min(minMoves, moves);
        }
    }

    return minMoves;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input array, due to generating all possible binary sequences and checking each one.
> - **Space Complexity:** $O(n)$, for storing the temporary array and the binary sequence.
> - **Why these complexities occur:** The brute force approach involves generating an exponential number of possibilities and checking each one, leading to high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves iterating through the array and considering two cases for each element: decreasing it to make the array zigzag if it's at an even index, or not decreasing it if it's at an odd index.
- We keep track of the minimum moves required for both cases.

```cpp
int movesToMakeZigzag(vector<int>& nums) {
    int n = nums.size();
    int res = INT_MAX;

    for (int parity = 0; parity < 2; parity++) {
        int moves = 0;
        for (int i = 0; i < n; i++) {
            if (i % 2 == parity) {
                int minNei = INT_MAX;
                if (i > 0) minNei = min(minNei, nums[i-1]);
                if (i < n-1) minNei = min(minNei, nums[i+1]);
                if (nums[i] <= minNei) {
                    moves += nums[i] - minNei + 1;
                }
            }
        }
        res = min(res, moves);
    }

    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array, as we're making a single pass through the array for each parity.
> - **Space Complexity:** $O(1)$, as we're using a constant amount of space to store the minimum moves and the current index.
> - **Optimality proof:** This approach is optimal because it considers all possible cases for making the array zigzag (even and odd indices) and chooses the one that requires the minimum number of moves.

---

### Final Notes

**Learning Points:**
- The importance of considering different parities when making an array zigzag.
- How to optimize the solution by iterating through the array only once for each parity.
- The trade-off between time and space complexity in the optimal approach.

**Mistakes to Avoid:**
- Not considering the parity of the indices when making the array zigzag.
- Not keeping track of the minimum moves required for each parity.
- Not optimizing the solution to reduce the time complexity.