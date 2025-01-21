## Top K Frequent Elements

**Problem Link:** https://leetcode.com/problems/top-k-frequent-elements/description

**Problem Statement:**
- Input: An array of integers `nums` and an integer `k`.
- Constraints: $1 \leq k \leq n \leq 10^4$ and $1 \leq nums[i] \leq 10^4$.
- Expected output: The `k` most frequent elements in `nums`.
- Key requirements: The output should contain the `k` most frequent elements, and if there are multiple elements with the same frequency, any of them can be included in the output.
- Example test cases:
  - Input: `nums = [1,1,1,2,2,3], k = 2`
    Output: `[1,2]`
  - Input: `nums = [1], k = 1`
    Output: `[1]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can first count the frequency of each element in the `nums` array. Then, we can sort the elements based on their frequencies and return the top `k` elements.
- Step-by-step breakdown of the solution:
  1. Count the frequency of each element using a `map`.
  2. Create a vector of pairs where each pair contains an element and its frequency.
  3. Sort the vector of pairs in descending order based on the frequency.
  4. Return the top `k` elements from the sorted vector.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

vector<int> topKFrequent(vector<int>& nums, int k) {
    map<int, int> freq;
    for (int num : nums) {
        freq[num]++;
    }

    vector<pair<int, int>> pairs;
    for (auto& it : freq) {
        pairs.push_back({it.first, it.second});
    }

    sort(pairs.begin(), pairs.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        return a.second > b.second;
    });

    vector<int> result;
    for (int i = 0; i < k; i++) {
        result.push_back(pairs[i].first);
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ where $n$ is the number of unique elements in `nums`. This is because we are sorting the vector of pairs.
> - **Space Complexity:** $O(n)$ where $n$ is the number of unique elements in `nums`. This is because we are storing the frequency of each element in a `map`.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation, and the space complexity is due to the storage of the frequency of each element.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `priority_queue` to store the elements and their frequencies. The `priority_queue` will automatically keep the elements with the highest frequencies at the top.
- Detailed breakdown of the approach:
  1. Count the frequency of each element using a `map`.
  2. Create a `priority_queue` and push the elements and their frequencies into it.
  3. Pop the top `k` elements from the `priority_queue` and return them.

```cpp
#include <iostream>
#include <vector>
#include <map>
#include <queue>

vector<int> topKFrequent(vector<int>& nums, int k) {
    map<int, int> freq;
    for (int num : nums) {
        freq[num]++;
    }

    priority_queue<pair<int, int>> pq;
    for (auto& it : freq) {
        pq.push({it.second, it.first});
    }

    vector<int> result;
    for (int i = 0; i < k; i++) {
        result.push_back(pq.top().second);
        pq.pop();
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log k)$ where $n$ is the number of unique elements in `nums`. This is because we are pushing $n$ elements into the `priority_queue` and popping $k$ elements.
> - **Space Complexity:** $O(n)$ where $n$ is the number of unique elements in `nums`. This is because we are storing the frequency of each element in a `map`.
> - **Optimality proof:** This is the optimal solution because we are using a `priority_queue` to keep track of the top `k` elements, which reduces the time complexity from $O(n \log n)$ to $O(n \log k)$.

---

### Alternative Approach

**Explanation:**
- Different perspective or technique: We can use a `bucket` approach to solve this problem. The idea is to create an array of buckets where each bucket represents a frequency. We then iterate through the `nums` array and update the frequency of each element in the bucket.
- Unique trade-offs: This approach has a time complexity of $O(n)$ but requires extra space to store the buckets.
- Scenarios where this approach might be preferred: When the range of frequencies is small, this approach can be more efficient than the optimal approach.

```cpp
#include <iostream>
#include <vector>

vector<int> topKFrequent(vector<int>& nums, int k) {
    vector<vector<int>> buckets(nums.size() + 1);
    map<int, int> freq;
    for (int num : nums) {
        freq[num]++;
    }

    for (auto& it : freq) {
        buckets[it.second].push_back(it.first);
    }

    vector<int> result;
    for (int i = buckets.size() - 1; i >= 0; i--) {
        for (int num : buckets[i]) {
            result.push_back(num);
            if (result.size() == k) {
                return result;
            }
        }
    }

    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the size of the `nums` array. This is because we are iterating through the `nums` array and updating the frequency of each element in the bucket.
> - **Space Complexity:** $O(n)$ where $n$ is the size of the `nums` array. This is because we are storing the frequency of each element in a `map` and the buckets.
> - **Trade-off analysis:** This approach has a better time complexity than the optimal approach when the range of frequencies is small. However, it requires extra space to store the buckets.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: `priority_queue`, `map`, `bucket` approach.
- Problem-solving patterns identified: Counting frequency, sorting, using data structures to optimize time complexity.
- Optimization techniques learned: Using `priority_queue` to reduce time complexity, using `bucket` approach to reduce time complexity when the range of frequencies is small.
- Similar problems to practice: LeetCode problems 347, 451, 658.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not checking for overflow, not using `const` correctness.
- Edge cases to watch for: Empty input array, `k` is 0, `k` is greater than the size of the input array.
- Performance pitfalls: Using inefficient data structures, not optimizing time complexity.
- Testing considerations: Test with different input sizes, test with different values of `k`, test with edge cases.