## Maximum Gap
**Problem Link:** https://leetcode.com/problems/maximum-gap/description

**Problem Statement:**
- Input format: An array of integers `nums` containing `n` elements, where `n >= 2`.
- Constraints: All elements in `nums` are distinct integers in the range `[1, 10^9]`.
- Expected output format: The maximum gap between any two adjacent numbers in the sorted array.
- Key requirements and edge cases to consider: The input array is not sorted, and we need to find the maximum gap after sorting it.
- Example test cases with explanations:
  - Input: `nums = [3,6,9,1]`
    Output: `3`
    Explanation: After sorting the array, we get `[1,3,6,9]`, and the maximum gap is between `6` and `3`, which is `3`.
  - Input: `nums = [10]`
    Output: `0`
    Explanation: Since there's only one element, the maximum gap is `0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Sort the array and then iterate through it to find the maximum gap.
- Step-by-step breakdown of the solution:
  1. Sort the input array in ascending order.
  2. Initialize the maximum gap to `0`.
  3. Iterate through the sorted array from the second element to the last element.
  4. For each element, calculate the gap between it and the previous element.
  5. Update the maximum gap if the current gap is larger.
- Why this approach comes to mind first: It's a straightforward solution that involves sorting and then iterating through the array.

```cpp
#include <algorithm>
int maximumGap(vector<int>& nums) {
    // Sort the input array
    sort(nums.begin(), nums.end());
    
    // Initialize the maximum gap
    int maxGap = 0;
    
    // Iterate through the sorted array
    for (int i = 1; i < nums.size(); i++) {
        // Calculate the gap between the current and previous elements
        int gap = nums[i] - nums[i - 1];
        
        // Update the maximum gap
        maxGap = max(maxGap, gap);
    }
    
    return maxGap;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting step, where $n$ is the number of elements in the input array.
> - **Space Complexity:** $O(1)$ if we sort the array in-place, or $O(n)$ if we use a sorting algorithm that requires extra space.
> - **Why these complexities occur:** The time complexity is dominated by the sorting step, which takes $O(n \log n)$ time in the worst case. The space complexity depends on the sorting algorithm used.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a bucketing approach to divide the range of the input array into buckets, and then find the maximum gap between the minimum and maximum values in each bucket.
- Detailed breakdown of the approach:
  1. Calculate the minimum and maximum values in the input array.
  2. Calculate the bucket size based on the range of the input array and the number of elements.
  3. Create an array of buckets, where each bucket represents a range of values.
  4. Iterate through the input array and assign each element to a bucket.
  5. Find the minimum and maximum values in each bucket.
  6. Iterate through the buckets and find the maximum gap between the minimum and maximum values in each bucket.
- Proof of optimality: This approach has a time complexity of $O(n)$, which is optimal because we need to iterate through the input array at least once to find the maximum gap.

```cpp
int maximumGap(vector<int>& nums) {
    // Calculate the minimum and maximum values
    int minVal = *min_element(nums.begin(), nums.end());
    int maxVal = *max_element(nums.begin(), nums.end());
    
    // Calculate the bucket size
    int bucketSize = max(1, (maxVal - minVal) / (nums.size() - 1));
    
    // Create an array of buckets
    int bucketCount = (maxVal - minVal) / bucketSize + 1;
    vector<pair<int, int>> buckets(bucketCount, {INT_MAX, INT_MIN});
    
    // Assign each element to a bucket
    for (int num : nums) {
        int bucketIndex = (num - minVal) / bucketSize;
        buckets[bucketIndex].first = min(buckets[bucketIndex].first, num);
        buckets[bucketIndex].second = max(buckets[bucketIndex].second, num);
    }
    
    // Find the maximum gap
    int maxGap = 0;
    int prevMax = buckets[0].second;
    for (int i = 1; i < bucketCount; i++) {
        if (buckets[i].first != INT_MAX) {
            maxGap = max(maxGap, buckets[i].first - prevMax);
            prevMax = buckets[i].second;
        }
    }
    
    return maxGap;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the input array.
> - **Optimality proof:** This approach has a time complexity of $O(n)$, which is optimal because we need to iterate through the input array at least once to find the maximum gap.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bucketing, sorting, and iteration.
- Problem-solving patterns identified: Using bucketing to divide a range of values into smaller ranges.
- Optimization techniques learned: Using a bucketing approach to reduce the time complexity.
- Similar problems to practice: Problems involving sorting, iteration, and bucketing.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input array or an array with a single element.
- Edge cases to watch for: An input array with a single element, or an array with duplicate elements.
- Performance pitfalls: Using a sorting algorithm with a high time complexity, such as bubble sort or insertion sort.
- Testing considerations: Testing the function with different input arrays, including edge cases and large input arrays.