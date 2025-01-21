## Count of Smaller Numbers After Self
**Problem Link:** https://leetcode.com/problems/count-of-smaller-numbers-after-self/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 10^5`, `0 <= nums[i] <= 10^5`.
- Expected output format: An array of integers where the `i-th` element is the number of elements in `nums` that are smaller than `nums[i]` and come after `nums[i]`.
- Key requirements and edge cases to consider: Handling duplicate elements, ensuring the output array has the same length as the input array.
- Example test cases with explanations:
  - `[5,2,6,1]`: Expected output `[2,1,1,0]`.
  - `[1,2,0]`: Expected output `[1,0,0]`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Compare each element with all elements after it and count the smaller ones.
- Step-by-step breakdown of the solution:
  1. Initialize an empty array `result` to store the count of smaller numbers after each element.
  2. Iterate over the input array `nums`.
  3. For each element `nums[i]`, iterate over the rest of the array (from `i+1` to the end).
  4. Count the elements that are smaller than `nums[i]`.
  5. Append the count to the `result` array.
- Why this approach comes to mind first: It directly addresses the problem statement by comparing each element with all subsequent elements.

```cpp
vector<int> countSmaller(vector<int>& nums) {
    vector<int> result;
    for (int i = 0; i < nums.size(); i++) {
        int count = 0;
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[j] < nums[i]) {
                count++;
            }
        }
        result.push_back(count);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input array `nums`, because for each element, we potentially iterate over the rest of the array.
> - **Space Complexity:** $O(n)$, as we need to store the result for each element in the `result` array.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity, and the need to store the result for each element leads to linear space complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Using a `Binary Indexed Tree` (BIT) or a `Fenwick Tree` to keep track of the cumulative count of elements smaller than the current element as we iterate through the array.
- Detailed breakdown of the approach:
  1. Initialize a BIT or Fenwick Tree with the size equal to the maximum possible value in the array plus one.
  2. Initialize an empty array `result` to store the count of smaller numbers after each element.
  3. Iterate over the input array `nums` in reverse order.
  4. For each element `nums[i]`, query the BIT to find the count of elements smaller than `nums[i]`.
  5. Append the count to the `result` array.
  6. Update the BIT by incrementing the count for `nums[i]`.
- Proof of optimality: The BIT allows us to query and update in $O(\log n)$ time, leading to an overall time complexity of $O(n \log n)$, which is optimal for this problem given the need to consider each element and its relation to others.

```cpp
vector<int> countSmaller(vector<int>& nums) {
    vector<int> ranks(nums.begin(), nums.end());
    sort(ranks.begin(), ranks.end());
    for (int i = 0; i < nums.size(); i++) {
        nums[i] = lower_bound(ranks.begin(), ranks.end(), nums[i]) - ranks.begin() + 1;
    }
    vector<int> result(nums.size());
    vector<int> bit(nums.size() + 1);
    for (int i = nums.size() - 1; i >= 0; i--) {
        result[i] = query(bit, nums[i] - 1);
        update(bit, nums[i]);
    }
    return result;
}

void update(vector<int>& bit, int i) {
    while (i < bit.size()) {
        bit[i]++;
        i += i & -i;
    }
}

int query(vector<int>& bit, int i) {
    int sum = 0;
    while (i > 0) {
        sum += bit[i];
        i -= i & -i;
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the size of the input array `nums`, due to the sorting and the use of the BIT for queries and updates.
> - **Space Complexity:** $O(n)$, for storing the ranks and the result array, as well as the BIT.
> - **Optimality proof:** This approach is optimal because it minimizes the time complexity by leveraging the efficient query and update operations of the BIT, making it suitable for large inputs.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Use of Binary Indexed Tree (BIT) for efficient cumulative counting.
- Problem-solving patterns identified: Transforming the problem into a form where a BIT can be applied.
- Optimization techniques learned: Reducing time complexity by using a data structure that supports fast query and update operations.
- Similar problems to practice: Other problems involving cumulative counts or ranks, such as finding the number of inversions in an array.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating or querying the BIT.
- Edge cases to watch for: Handling duplicate elements correctly by ensuring they are assigned the correct rank.
- Performance pitfalls: Not using the BIT or similar data structures when dealing with cumulative counts, leading to inefficient solutions.
- Testing considerations: Thoroughly testing the implementation with various inputs, including edge cases like empty arrays, arrays with duplicate elements, and arrays with a large range of values.