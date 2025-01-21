## Sliding Window Maximum
**Problem Link:** [https://leetcode.com/problems/sliding-window-maximum/description](https://leetcode.com/problems/sliding-window-maximum/description)

**Problem Statement:**
- Input format: Given an array `nums` of integers and an integer `k`, return the maximum values in each subarray of length `k`.
- Constraints: `1 <= k <= nums.length <= 10^5`, `-10^4 <= nums[i] <= 10^4`.
- Expected output format: An array of integers where each element is the maximum value in the corresponding subarray of length `k`.
- Key requirements and edge cases to consider: Handling edge cases such as when `k` equals the length of `nums`, or when `nums` contains duplicate maximum values within a subarray.
- Example test cases with explanations: 
    - For `nums = [1,3,-1,-3,5,3,6,7]` and `k = 3`, the output should be `[3,3,5,5,6,7]` because the maximum values in each subarray of length `3` are `3, 3, 5, 5, 6, 7`.
    - For `nums = [1]` and `k = 1`, the output should be `[1]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over the array with a sliding window of size `k`, and for each window, find the maximum value.
- Step-by-step breakdown of the solution:
    1. Initialize an empty list to store the maximum values.
    2. Iterate over the array with a sliding window of size `k`.
    3. For each window, find the maximum value by iterating over all elements in the window.
    4. Append the maximum value to the list.
- Why this approach comes to mind first: It directly implements the problem statement, making it straightforward to understand and implement.

```cpp
vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    vector<int> result;
    for (int i = 0; i <= nums.size() - k; ++i) {
        int maxVal = nums[i];
        for (int j = i + 1; j < i + k; ++j) {
            if (nums[j] > maxVal) {
                maxVal = nums[j];
            }
        }
        result.push_back(maxVal);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the number of elements in `nums`, because for each of the $n - k + 1$ windows, we potentially scan `k` elements.
> - **Space Complexity:** $O(n - k + 1)$, for storing the maximum values in each window.
> - **Why these complexities occur:** The nested loop structure leads to the time complexity, while storing the results for each window leads to the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using a deque to keep track of indices of the elements in the current window that could be the maximum. This allows us to efficiently remove elements that are out of the window or smaller than the new element.
- Detailed breakdown of the approach:
    1. Initialize a deque to store indices of potential maximum elements.
    2. Iterate over the array. For each element:
        - Remove from the back of the deque any elements that are smaller than the current element, because they cannot be the maximum in the current window.
        - Remove from the front of the deque any elements that are out of the current window.
        - Add the current index to the back of the deque.
        - If the window is full (i.e., we have processed `k` elements), add the maximum element (at the front of the deque) to the result.
- Proof of optimality: This approach ensures that we only consider elements that could be the maximum in the current window, reducing unnecessary comparisons.

```cpp
vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    deque<int> dq;
    vector<int> result;
    for (int i = 0; i < nums.size(); ++i) {
        // Remove elements out of the current window
        while (!dq.empty() && dq.front() < i - k + 1) {
            dq.pop_front();
        }
        // Remove elements smaller than the current one
        while (!dq.empty() && nums[dq.back()] < nums[i]) {
            dq.pop_back();
        }
        // Add current index
        dq.push_back(i);
        // Add max to result if window is full
        if (i >= k - 1) {
            result.push_back(nums[dq.front()]);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in `nums`, because each element is pushed and popped from the deque exactly once.
> - **Space Complexity:** $O(k)$, for storing the indices in the deque.
> - **Optimality proof:** This approach minimizes the number of comparisons needed to find the maximum in each window, making it optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a deque for efficient removal of elements, maintaining a sliding window, and optimizing comparisons.
- Problem-solving patterns identified: Breaking down the problem into smaller, manageable parts (e.g., handling each window separately), and using data structures to reduce complexity.
- Optimization techniques learned: Minimizing unnecessary comparisons by only considering potential maximum elements.
- Similar problems to practice: Other sliding window problems, such as finding the minimum or sum in each window.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases (e.g., when `k` equals the length of `nums`), or failing to remove elements from the deque that are out of the current window.
- Edge cases to watch for: When `nums` contains duplicate maximum values within a subarray, or when `k` is 1.
- Performance pitfalls: Using a brute force approach for large inputs, leading to inefficient time complexity.
- Testing considerations: Thoroughly testing with various inputs, including edge cases, to ensure correctness and efficiency.