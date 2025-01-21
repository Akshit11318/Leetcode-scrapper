## Finding Pairs with a Certain Sum
**Problem Link:** https://leetcode.com/problems/finding-pairs-with-a-certain-sum/description

**Problem Statement:**
- Input format: Two integer arrays `nums1` and `nums2`, and an integer `target`.
- Constraints: `1 <= nums1.length, nums2.length <= 10^5` and `1 <= nums1[i], nums2[i] <= 10^6`.
- Expected output format: The number of pairs `(i, j)` where `i` is from `nums1` and `j` is from `nums2` such that `i + j == target`.
- Key requirements: Count the pairs efficiently.
- Example test cases:
  - `nums1 = [1, 2, 3]`, `nums2 = [2, 4]`, `target = 5`. Output: `1`.
  - `nums1 = [1, 2]`, `nums2 = [1, 2, 3]`, `target = 3`. Output: `2`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through each element in `nums1` and for each element, iterate through each element in `nums2` to check if their sum equals the target.
- This approach is straightforward but inefficient for large inputs.

```cpp
int countPairs(vector<int>& nums1, vector<int>& nums2, int target) {
    int count = 0;
    for (int i : nums1) {
        for (int j : nums2) {
            if (i + j == target) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ and $m$ are the lengths of `nums1` and `nums2`, respectively. This is because for each element in `nums1`, we potentially iterate through all elements in `nums2`.
> - **Space Complexity:** $O(1)$, not considering the space needed for input, as we only use a constant amount of space to store the count.
> - **Why these complexities occur:** The nested loops cause the time complexity to be the product of the sizes of the two input arrays, and the space complexity is constant because we only need a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a `unordered_map` to store the frequency of each number in `nums2`.
- Then, for each number in `nums1`, we can directly find how many numbers in `nums2` would sum up to the target by looking up the difference between the target and the current number in the map.
- This reduces the time complexity significantly.

```cpp
int countPairs(vector<int>& nums1, vector<int>& nums2, int target) {
    unordered_map<int, int> freq;
    for (int num : nums2) {
        freq[num]++;
    }
    int count = 0;
    for (int num : nums1) {
        if (freq.find(target - num) != freq.end()) {
            count += freq[target - num];
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the lengths of `nums1` and `nums2`, respectively. This is because we make a single pass through each array.
> - **Space Complexity:** $O(m)$, where $m$ is the length of `nums2`, because in the worst case, we might store every element of `nums2` in the map.
> - **Optimality proof:** This is optimal because we must at least look at each element once to determine the pairs, and using a hash map allows us to do this in linear time.

---

### Final Notes

**Learning Points:**
- Using hash maps (`unordered_map`) can significantly improve lookup times.
- Preprocessing data (in this case, counting frequencies) can simplify later computations.
- The choice of data structure can dramatically affect algorithm performance.

**Mistakes to Avoid:**
- Not considering the trade-offs between time and space complexity.
- Overlooking the possibility of using a more efficient data structure.
- Failing to account for edge cases, such as empty input arrays.