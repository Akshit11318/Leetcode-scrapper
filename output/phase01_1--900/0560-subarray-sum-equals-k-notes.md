## Subarray Sum Equals K

**Problem Link:** https://leetcode.com/problems/subarray-sum-equals-k/description

**Problem Statement:**
- Input: An integer array `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 2 * 10^4`, `-1000 <= nums[i] <= 1000`, `-1 * 10^7 <= k <= 1 * 10^7`.
- Expected Output: The number of continuous subarrays where the sum of the elements equals `k`.
- Key Requirements: Find all subarrays with sum equal to `k`, including empty subarrays if any, but since the problem asks for continuous subarrays and given the constraints, we focus on non-empty subarrays.
- Example Test Cases: 
    - Input: `nums = [1,1,1]`, `k = 2`
    Output: `2`
    Explanation: `[1,1]` appears twice.
    - Input: `nums = [1,2,3]`, `k = 3`
    Output: `2`
    Explanation: `[1,2]` and `[3]` are the subarrays with sum `3`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every possible subarray of the given array to see if its sum equals `k`.
- Step-by-step breakdown:
    1. Generate all possible subarrays.
    2. For each subarray, calculate its sum.
    3. If the sum equals `k`, increment the count of such subarrays.
- This approach comes to mind first because it directly addresses the problem statement without requiring additional insights or optimizations.

```cpp
int subarraySum(vector<int>& nums, int k) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i; j < nums.size(); j++) {
            int sum = 0;
            for (int l = i; l <= j; l++) {
                sum += nums[l];
            }
            if (sum == k) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of elements in `nums`. This is because for each starting index $i$, we potentially iterate over the array again to calculate the sum of the subarray from $i$ to $j$, and we do this for all possible ending indices $j$.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output. This is because we only use a constant amount of space to store the count and indices.
> - **Why these complexities occur:** The cubic time complexity arises from the nested loops used to generate all possible subarrays and calculate their sums. The constant space complexity is due to not using any additional data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution involves using a prefix sum array and a hashmap to store the cumulative sums and their frequencies, respectively.
- Detailed breakdown:
    1. Calculate the prefix sum array `prefixSum` where `prefixSum[i]` is the sum of elements from index `0` to `i`.
    2. Initialize a hashmap `sumCount` to store the frequency of each cumulative sum.
    3. Initialize the count of subarrays with sum `k` to `0`.
    4. Iterate through the `prefixSum` array. For each `prefixSum[i]`, check if `prefixSum[i] - k` exists in `sumCount`. If it does, add the frequency of `prefixSum[i] - k` to the count because this means there's a subarray ending at `i` with sum `k`.
    5. Update the frequency of `prefixSum[i]` in `sumCount`.
- This approach is optimal because it reduces the time complexity to $O(n)$ by avoiding the need to recalculate sums for subarrays.

```cpp
int subarraySum(vector<int>& nums, int k) {
    unordered_map<int, int> sumCount;
    sumCount[0] = 1; // For the case where the sum of the subarray equals k and starts from the beginning
    int currentSum = 0;
    int count = 0;
    for (int num : nums) {
        currentSum += num;
        if (sumCount.find(currentSum - k) != sumCount.end()) {
            count += sumCount[currentSum - k];
        }
        sumCount[currentSum]++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in `nums`. This is because we make a single pass through the array.
> - **Space Complexity:** $O(n)$, because in the worst case, every prefix sum could be unique, requiring space in the hashmap.
> - **Optimality proof:** This approach is optimal because it processes each element exactly once, which is necessary to find all subarrays with sum `k`. The use of a hashmap allows for constant time lookups and updates, making the overall time complexity linear.

---

### Final Notes

**Learning Points:**
- The importance of prefix sums in solving array and subarray problems efficiently.
- The use of hashmaps for storing and quickly retrieving frequencies of elements or sums.
- The concept of reducing time complexity by avoiding redundant calculations.

**Mistakes to Avoid:**
- Not considering the edge case where the subarray starts at the beginning of the array.
- Failing to update the frequency of cumulative sums correctly.
- Not initializing the hashmap with a base case (e.g., sum `0` for an empty subarray).