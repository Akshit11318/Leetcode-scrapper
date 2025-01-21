## Number of Subarrays with GCD Equal to K

**Problem Link:** https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description

**Problem Statement:**
- Input: An integer array `nums` and an integer `k`.
- Output: The number of subarrays of `nums` where the greatest common divisor (`GCD`) of all the elements in the subarray is equal to `k`.
- Key requirements and edge cases:
  - `1 <= nums.length <= 1000`
  - `1 <= nums[i] <= 1000`
  - `1 <= k <= 1000`
- Example test cases:
  - Input: `nums = [9,3,1,2,6,3], k = 3`, Output: `4`
  - Input: `nums = [4], k = 7`, Output: `0`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every possible subarray of `nums`.
- For each subarray, calculate the GCD of its elements.
- If the GCD equals `k`, increment the count of such subarrays.
- This approach comes to mind first because it directly addresses the problem statement without requiring any optimization.

```cpp
class Solution {
public:
    int subarrayGCD(vector<int>& nums, int k) {
        int n = nums.size();
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int gcd = calculateGCD(nums, i, j);
                if (gcd == k) {
                    count++;
                }
            }
        }
        return count;
    }
    
    int calculateGCD(vector<int>& nums, int start, int end) {
        int gcd = nums[start];
        for (int i = start + 1; i <= end; i++) {
            gcd = findGCD(gcd, nums[i]);
        }
        return gcd;
    }
    
    int findGCD(int a, int b) {
        if (b == 0) return a;
        return findGCD(b, a % b);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `nums`. The reason is that we have two nested loops to generate all subarrays ($O(n^2)$), and for each subarray, we calculate the GCD which takes $O(n)$ time in the worst case (when the subarray is the entire array).
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output, because we only use a constant amount of space to store variables.
> - **Why these complexities occur:** These complexities occur because we are using a brute force approach that checks every possible subarray, leading to a high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a prefix array to store the GCD of all subarrays ending at each position.
- However, calculating the GCD for all subarrays directly is still inefficient.
- A more efficient approach involves using the property of GCD to reduce the number of calculations.
- Specifically, we can use the fact that the GCD of two numbers `a` and `b` is the same as the GCD of `b` and the remainder of `a` divided by `b`.
- But the most efficient way to solve this problem is to directly calculate the GCD for each possible subarray and compare it with `k`, utilizing the fact that GCD operations can be optimized using the Euclidean algorithm.
- We can further optimize by only considering subarrays where the first element is a multiple of `k`, since the GCD of the subarray must be `k`.

```cpp
class Solution {
public:
    int subarrayGCD(vector<int>& nums, int k) {
        int n = nums.size();
        int count = 0;
        for (int i = 0; i < n; i++) {
            int gcd = nums[i];
            for (int j = i; j < n; j++) {
                gcd = gcdHelper(gcd, nums[j]);
                if (gcd == k) {
                    count++;
                }
            }
        }
        return count;
    }
    
    int gcdHelper(int a, int b) {
        if (b == 0) return a;
        return gcdHelper(b, a % b);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \log m)$, where $n$ is the length of `nums` and $m$ is the maximum value in `nums`. The reason is that we have two nested loops to generate all subarrays ($O(n^2)$), and for each pair of numbers in the subarray, we calculate the GCD using the Euclidean algorithm, which takes $O(\log m)$ time.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output, because we only use a constant amount of space to store variables.
> - **Optimality proof:** This is the optimal solution because we must consider all possible subarrays to find those with a GCD of `k`, and calculating the GCD for each subarray using the Euclidean algorithm is the most efficient method.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: GCD calculation using the Euclidean algorithm, optimization of brute force approaches.
- Problem-solving patterns identified: Using properties of mathematical operations (like GCD) to reduce computational complexity.
- Optimization techniques learned: Applying the Euclidean algorithm for efficient GCD calculation, reducing the number of GCD calculations by considering properties of the problem.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect implementation of the Euclidean algorithm, not considering all possible subarrays.
- Edge cases to watch for: Subarrays of length 1, subarrays with all elements being `k`, empty input array.
- Performance pitfalls: Using a naive approach to calculate GCD, not optimizing the calculation of GCD for subarrays.
- Testing considerations: Test with arrays of varying lengths, test with `k` being a factor of some elements in the array, test with `k` not being a factor of any element in the array.