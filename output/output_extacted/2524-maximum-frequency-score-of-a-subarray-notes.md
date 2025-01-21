## Maximum Frequency Score of a Subarray
**Problem Link:** https://leetcode.com/problems/maximum-frequency-score-of-a-subarray/description

**Problem Statement:**
- Input format: Given an integer array `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^5`, `1 <= k <= nums.length`.
- Expected output format: The maximum frequency score of a subarray with a length of `k`.
- Key requirements and edge cases to consider: The frequency score of a subarray is the maximum frequency of any integer in the subarray. The score is calculated by multiplying the frequency of the integer by the integer itself.

### Brute Force Approach

**Explanation:**
- Initial thought process: To find the maximum frequency score of a subarray with a length of `k`, we can consider all possible subarrays of length `k` and calculate their frequency scores.
- Step-by-step breakdown of the solution:
  1. Iterate over all possible subarrays of length `k`.
  2. For each subarray, calculate the frequency of each integer.
  3. Find the maximum frequency and the corresponding integer.
  4. Calculate the frequency score by multiplying the frequency and the integer.
  5. Keep track of the maximum frequency score found so far.
- Why this approach comes to mind first: It is a straightforward approach that considers all possible subarrays and calculates their frequency scores.

```cpp
int maxFrequencyScore(vector<int>& nums, int k) {
    int maxScore = 0;
    for (int i = 0; i <= nums.size() - k; i++) {
        unordered_map<int, int> freq;
        for (int j = i; j < i + k; j++) {
            freq[nums[j]]++;
        }
        int maxFreq = 0;
        int maxNum = 0;
        for (auto& pair : freq) {
            if (pair.second > maxFreq || (pair.second == maxFreq && pair.first > maxNum)) {
                maxFreq = pair.second;
                maxNum = pair.first;
            }
        }
        maxScore = max(maxScore, maxFreq * maxNum);
    }
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the length of the input array. This is because we are iterating over all possible subarrays of length `k` and calculating their frequency scores.
> - **Space Complexity:** $O(k)$, where $k$ is the length of the subarray. This is because we are using a hash map to store the frequency of each integer in the subarray.
> - **Why these complexities occur:** The time complexity occurs because we are considering all possible subarrays, and the space complexity occurs because we are using a hash map to store the frequency of each integer.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a sliding window approach to efficiently calculate the frequency score of each subarray.
- Detailed breakdown of the approach:
  1. Initialize a hash map to store the frequency of each integer in the current window.
  2. Iterate over the input array, expanding the window to the right by one element at a time.
  3. For each element, update the frequency map and calculate the frequency score of the current window.
  4. If the window size exceeds `k`, shrink the window from the left by one element at a time, updating the frequency map and calculating the frequency score.
  5. Keep track of the maximum frequency score found so far.
- Proof of optimality: This approach is optimal because it considers all possible subarrays of length `k` and calculates their frequency scores in linear time.

```cpp
int maxFrequencyScore(vector<int>& nums, int k) {
    int maxScore = 0;
    unordered_map<int, int> freq;
    for (int i = 0; i < nums.size(); i++) {
        freq[nums[i]]++;
        if (i >= k) {
            freq[nums[i - k]]--;
            if (freq[nums[i - k]] == 0) {
                freq.erase(nums[i - k]);
            }
        }
        if (i >= k - 1) {
            int maxFreq = 0;
            int maxNum = 0;
            for (auto& pair : freq) {
                if (pair.second > maxFreq || (pair.second == maxFreq && pair.first > maxNum)) {
                    maxFreq = pair.second;
                    maxNum = pair.first;
                }
            }
            maxScore = max(maxScore, maxFreq * maxNum);
        }
    }
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we are iterating over the input array once, updating the frequency map and calculating the frequency score for each subarray.
> - **Space Complexity:** $O(k)$, where $k` is the length of the subarray. This is because we are using a hash map to store the frequency of each integer in the current window.
> - **Optimality proof:** This approach is optimal because it considers all possible subarrays of length `k` and calculates their frequency scores in linear time, using a constant amount of extra space.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, frequency calculation, and maximum score tracking.
- Problem-solving patterns identified: Using a hash map to store frequency information and iterating over the input array to calculate the frequency score of each subarray.
- Optimization techniques learned: Using a sliding window approach to efficiently calculate the frequency score of each subarray.
- Similar problems to practice: Problems involving frequency calculation, sliding window approach, and maximum score tracking.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the frequency map correctly when shrinking the window, not calculating the frequency score correctly for each subarray.
- Edge cases to watch for: Handling cases where the input array is empty or has a length less than `k`.
- Performance pitfalls: Using a brute force approach that considers all possible subarrays, resulting in a high time complexity.
- Testing considerations: Testing the implementation with different input arrays and values of `k` to ensure correctness and efficiency.