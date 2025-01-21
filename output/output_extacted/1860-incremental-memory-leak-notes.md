## Incremental Memory Leak
**Problem Link:** https://leetcode.com/problems/incremental-memory-leak/description

**Problem Statement:**
- Input: Two integer arrays `mem1` and `mem2`, representing the memory usage of two different systems at each time step.
- Constraints: Both arrays will have the same length, and each element will be in the range `[0, 100]`.
- Expected Output: The time step at which the total memory usage of the first system exceeds the total memory usage of the second system by more than `m` units, or -1 if this never occurs.
- Key Requirements:
  - Compare the cumulative sum of `mem1` and `mem2` at each time step.
  - Determine the first time step where the difference in cumulative sums exceeds `m`.

**Example Test Cases:**
- `mem1 = [1,2,3,4,5]`, `mem2 = [1,2,3,4,5]`, `m = 1`. Output: `-1`
- `mem1 = [10,5,4,9]`, `mem2 = [3,1,2,8]`, `m = 2`. Output: `3`

---

### Brute Force Approach

**Explanation:**
- Calculate the cumulative sum of `mem1` and `mem2` at each time step.
- Compare the difference in cumulative sums with `m`.
- Return the first time step where the difference exceeds `m`, or -1 if this never occurs.

```cpp
class Solution {
public:
    int memLeak(int memory1, int memory2) {
        int n = memory1.size();
        vector<int> mem1(n), mem2(n);
        mem1[0] = memory1[0];
        mem2[0] = memory2[0];
        for (int i = 1; i < n; i++) {
            mem1[i] = mem1[i-1] + memory1[i];
            mem2[i] = mem2[i-1] + memory2[i];
        }
        for (int i = 0; i < n; i++) {
            if (abs(mem1[i] - mem2[i]) > m) {
                return i + 1;
            }
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input arrays.
> - **Space Complexity:** $O(n)$, for storing the cumulative sums of `mem1` and `mem2`.
> - **Why these complexities occur:** The brute force approach involves iterating over the input arrays to calculate the cumulative sums and then iterating over the cumulative sums to find the first time step where the difference exceeds `m`.

---

### Optimal Approach (Required)

**Explanation:**
- Use a single loop to calculate the cumulative sums of `mem1` and `mem2` and compare their difference with `m`.
- Return the first time step where the difference exceeds `m`, or -1 if this never occurs.

```cpp
class Solution {
public:
    int memLeak(int memory1, int memory2) {
        int n = memory1.size();
        int sum1 = 0, sum2 = 0;
        for (int i = 0; i < n; i++) {
            sum1 += memory1[i];
            sum2 += memory2[i];
            if (abs(sum1 - sum2) > m) {
                return i + 1;
            }
        }
        return -1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input arrays.
> - **Space Complexity:** $O(1)$, as only a constant amount of space is used.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the input arrays and uses a minimal amount of extra space.

---

### Final Notes

**Learning Points:**
- The importance of cumulative sums in solving problems involving sequences of numbers.
- How to optimize brute force approaches by reducing unnecessary computations and memory usage.
- The trade-off between time and space complexity in algorithm design.

**Mistakes to Avoid:**
- Failing to consider the cumulative sums of the input sequences.
- Using unnecessary extra space to store intermediate results.
- Not optimizing the brute force approach to reduce time and space complexity.