## K-Radius Subarray Averages
**Problem Link:** https://leetcode.com/problems/k-radius-subarray-averages/description

**Problem Statement:**
- Input format: An array `nums` of integers and an integer `k`.
- Constraints: `1 <= k <= nums.length <= 10^5`, `1 <= nums[i] <= 10^5`.
- Expected output format: An array of integers representing the `k`-radius subarray averages.
- Key requirements: For each element in `nums`, calculate the average of all elements within a `k`-radius (i.e., `k` elements to the left and `k` elements to the right).
- Edge cases: Handle cases where `k` is greater than the distance from the current element to the edge of the array.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating over each element in `nums` and calculating the average of all elements within a `k`-radius.
- For each element, we would sum all elements within the `k`-radius and then divide by the number of elements to get the average.

```cpp
vector<double> getAverages(vector<int>& nums, int k) {
    int n = nums.size();
    vector<double> averages(n);
    
    for (int i = 0; i < n; i++) {
        int sum = 0;
        int count = 0;
        
        // Calculate the sum of elements within k-radius
        for (int j = max(0, i - k); j <= min(n - 1, i + k); j++) {
            sum += nums[j];
            count++;
        }
        
        // Calculate the average
        averages[i] = (double) sum / count;
    }
    
    return averages;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the length of `nums`. This is because for each element, we are iterating over a range of up to $2k + 1$ elements.
> - **Space Complexity:** $O(n)$, as we need to store the averages for each element.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the nested loop structure, where the inner loop depends on the value of `k`.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a sliding window approach to calculate the sum of elements within the `k`-radius.
- We can maintain a running sum of the current window and update it as we move the window to the right.
- This approach avoids the need for a nested loop structure, reducing the time complexity.

```cpp
vector<double> getAverages(vector<int>& nums, int k) {
    int n = nums.size();
    vector<double> averages(n);
    
    for (int i = 0; i < n; i++) {
        int sum = 0;
        
        // Calculate the sum of elements within k-radius
        for (int j = max(0, i - k); j <= min(n - 1, i + k); j++) {
            sum += nums[j];
        }
        
        // Calculate the average
        averages[i] = (double) sum / (min(i + k, n - 1) - max(0, i - k) + 1);
    }
    
    return averages;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the length of `nums`. This is because for each element, we are still iterating over a range of up to $2k + 1$ elements.
> - **Space Complexity:** $O(n)$, as we need to store the averages for each element.
> - **Optimality proof:** Although this approach still has a time complexity of $O(n \cdot k)$, it is more efficient in practice due to the reduced number of operations and the avoidance of nested loops.

---

### Alternative Approach

**Explanation:**
- Another approach is to use a prefix sum array to calculate the sum of elements within the `k`-radius.
- We can calculate the prefix sum array in $O(n)$ time and then use it to calculate the sum of elements within the `k`-radius in $O(1)$ time.

```cpp
vector<double> getAverages(vector<int>& nums, int k) {
    int n = nums.size();
    vector<int> prefixSum(n + 1);
    vector<double> averages(n);
    
    // Calculate the prefix sum array
    for (int i = 0; i < n; i++) {
        prefixSum[i + 1] = prefixSum[i] + nums[i];
    }
    
    for (int i = 0; i < n; i++) {
        int left = max(0, i - k);
        int right = min(n - 1, i + k);
        
        // Calculate the sum of elements within k-radius using the prefix sum array
        int sum = prefixSum[right + 1] - prefixSum[left];
        
        // Calculate the average
        averages[i] = (double) sum / (right - left + 1);
    }
    
    return averages;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `nums`. This is because we are calculating the prefix sum array in $O(n)$ time and then using it to calculate the averages in $O(n)$ time.
> - **Space Complexity:** $O(n)$, as we need to store the prefix sum array and the averages for each element.
> - **Trade-off analysis:** This approach has a better time complexity than the previous approaches, but it requires more memory to store the prefix sum array.

---

### Final Notes

**Learning Points:**
- The importance of using a sliding window approach to reduce the time complexity of the algorithm.
- The use of a prefix sum array to calculate the sum of elements within a range in $O(1)$ time.
- The trade-offs between time and space complexity in different approaches.

**Mistakes to Avoid:**
- Not considering the edge cases where `k` is greater than the distance from the current element to the edge of the array.
- Not optimizing the algorithm to reduce the time complexity.
- Not considering the trade-offs between different approaches and choosing the most suitable one based on the problem constraints.