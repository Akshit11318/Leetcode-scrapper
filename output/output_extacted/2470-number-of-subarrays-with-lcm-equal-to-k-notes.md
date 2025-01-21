## Number of Subarrays with LCM Equal to K

**Problem Link:** https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/description

**Problem Statement:**
- Given an array of integers `nums` and an integer `k`, return the number of subarrays where the least common multiple (LCM) of the elements in the subarray is equal to `k`.
- Input format: `nums` array and `k` integer
- Constraints: `1 <= nums.length <= 1000`, `1 <= nums[i] <= 1000`, `1 <= k <= 1000`
- Expected output: Count of subarrays with LCM equal to `k`
- Key requirements: Calculate LCM of subarrays, compare with `k`, and count matches
- Edge cases: Empty array, single-element array, `k` not present in `nums`

### Brute Force Approach

**Explanation:**
- Calculate the LCM of every possible subarray in `nums` and compare it with `k`.
- Use the formula for LCM: `lcm(a, b) = (a * b) / gcd(a, b)`, where `gcd` is the greatest common divisor.
- For each subarray, calculate the LCM of its elements and check if it equals `k`.

```cpp
int subarrayLCM(vector<int>& nums, int k) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        long long lcm = nums[i];
        for (int j = i; j < nums.size(); j++) {
            lcm = (lcm * nums[j]) / gcd(lcm, nums[j]);
            if (lcm == k) count++;
            if (lcm > k) break; // Optimization: LCM increases as we add more elements
        }
    }
    return count;
}

long long gcd(long long a, long long b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot log(k))$ where $n$ is the size of `nums` and $log(k)$ is from the gcd calculation. This is because we are calculating the LCM for every possible subarray.
> - **Space Complexity:** $O(1)$ since we are using a constant amount of space to store the LCM and the count.
> - **Why these complexities occur:** The nested loops over the array elements and the gcd calculation contribute to the time complexity.

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is to use a similar strategy as the brute force but with a more efficient way to calculate the LCM for each subarray.
- We can maintain a running LCM as we extend the subarray to the right, which avoids redundant calculations.
- We still check every possible subarray but do so more efficiently by only updating the LCM when necessary.

```cpp
int subarrayLCM(vector<int>& nums, int k) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        long long lcm = nums[i];
        for (int j = i; j < nums.size(); j++) {
            lcm = lcm * nums[j] / gcd(lcm, nums[j]);
            if (lcm > k) break; // If LCM exceeds k, no need to continue this subarray
            if (lcm == k) count++;
        }
    }
    return count;
}

long long gcd(long long a, long long b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot log(k))$ due to the nested loops and the gcd calculation for each subarray.
> - **Space Complexity:** $O(1)$ as we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it checks every possible subarray exactly once and uses an efficient method to calculate the LCM, ensuring no redundant work is done.

### Final Notes

**Learning Points:**
- **LCM Calculation:** Understanding how to efficiently calculate the LCM of two numbers using the gcd.
- **Subarray Generation:** Recognizing how to generate all possible subarrays of a given array.
- **Optimization Techniques:** Applying optimizations such as breaking out of loops early when the LCM exceeds `k`.

**Mistakes to Avoid:**
- **Inefficient LCM Calculation:** Failing to use the formula `lcm(a, b) = (a * b) / gcd(a, b)` for LCM calculation.
- **Redundant Calculations:** Not maintaining a running LCM as the subarray is extended, leading to redundant calculations.
- **Missing Edge Cases:** Not considering edge cases such as an empty input array or `k` being larger than any element in `nums`.