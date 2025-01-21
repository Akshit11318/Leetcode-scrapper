## Contains Duplicate III

**Problem Link:** https://leetcode.com/problems/contains-duplicate-iii/description

**Problem Statement:**
- Input: An array of integers `nums`, an integer `k`, and an integer `t`.
- Output: `true` if there exist two distinct indices `i` and `j` such that `nums[i]` equals `nums[j]` and the absolute difference between `i` and `j` is at most `k`, or if there exist two distinct indices `i` and `j` such that the absolute difference between `nums[i]` and `nums[j]` is at most `t` and the absolute difference between `i` and `j` is at most `k`.
- Expected output format: A boolean indicating whether the conditions are met.
- Key requirements and edge cases to consider: Handling large inputs, optimizing for time and space complexity, considering edge cases such as empty arrays, arrays with a single element, or when `k` or `t` are negative or zero.
- Example test cases:
  - `nums = [1,2,3,1], k = 3, t = 0`, should return `true`.
  - `nums = [1,0,1,1], k = 1, t = 2`, should return `true`.
  - `nums = [1,5,9,1,5,9], k = 2, t = 3`, should return `false`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to compare each element in the array with every other element.
- We then check if the absolute difference between the indices of any two equal elements is at most `k`, or if the absolute difference between the values of any two elements is at most `t` and the absolute difference between their indices is at most `k`.
- This approach comes to mind first because it directly addresses the conditions given in the problem statement.

```cpp
bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
    int n = nums.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n && j - i <= k; j++) {
            if (nums[i] == nums[j] || (abs((long long)nums[i] - (long long)nums[j]) <= t && j - i <= k)) {
                return true;
            }
        }
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, because in the worst case, for each of the $n$ elements, we are comparing it with up to $k$ other elements.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the variables.
> - **Why these complexities occur:** The nested loop structure leads to the time complexity, and since we are not using any data structures that scale with the input size, the space complexity is constant.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a data structure that allows for efficient checking of the conditions, specifically a `set` or a data structure that can efficiently handle range queries.
- We use a `set` to store the elements within the window of size `k`. This allows us to check for duplicates or values within a certain range in $O(1)$ time.
- For the condition involving the absolute difference between values being at most `t`, we can use a technique called "bucketing" where we divide the range of possible values into buckets of size `t+1`. This allows us to efficiently check if there's a value within `t` of a given value.

```cpp
bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
    if (t < 0) return false;
    unordered_set<long long> window;
    for (int i = 0; i < nums.size(); i++) {
        if (i > k) window.erase(nums[i-k-1]);
        long long remappedNum = (long long)nums[i] / ((long long)t + 1);
        if (window.find(remappedNum) != window.end()) return true;
        if (t != 0) {
            if (window.find(remappedNum - 1) != window.end() && abs((long long)nums[i] - (long long)((remappedNum - 1) * (t + 1))) <= t) return true;
            if (window.find(remappedNum + 1) != window.end() && abs((long long)nums[i] - (long long)(((remappedNum + 1) * (t + 1)))) <= t) return true;
        }
        window.insert(remappedNum);
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, because each element is processed once and the operations within the loop take constant time.
> - **Space Complexity:** $O(min(n, k))$, because in the worst case, we store up to $k$ elements in the window.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity to linear while maintaining a reasonable space complexity, leveraging the properties of the `set` data structure and the bucketing technique to efficiently handle the conditions given in the problem statement.

---

### Final Notes

**Learning Points:**
- The importance of choosing the right data structure for the problem at hand.
- How to apply the bucketing technique to handle range queries efficiently.
- The trade-offs between time and space complexity in algorithm design.
- The importance of considering edge cases and boundary conditions.

**Mistakes to Avoid:**
- Not considering the implications of integer overflow when dealing with large numbers.
- Failing to optimize the algorithm for the given constraints, leading to inefficient solutions.
- Not thoroughly testing the solution with various edge cases and boundary conditions.