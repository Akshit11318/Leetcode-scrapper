## Find K Pairs with Smallest Sums

**Problem Link:** https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description

**Problem Statement:**
- Given two integer arrays `nums1` and `nums2`, return the k pairs of numbers (one from `nums1` and one from `nums2`) with the smallest sums.
- Input format: `nums1`, `nums2`, and `k` as integers.
- Expected output format: A list of pairs, where each pair contains one element from `nums1` and one element from `nums2`.
- Key requirements and edge cases to consider:
  - The input arrays `nums1` and `nums2` are non-empty and contain distinct elements.
  - The value of `k` is within the range of possible pairs, i.e., `1 <= k <= nums1.size() * nums2.size()`.
- Example test cases with explanations:
  - `nums1 = [1,7,11]`, `nums2 = [2,4,6]`, `k = 3`. The output should be `[[1,2],[1,4],[1,6]]`.
  - `nums1 = [1,1,2]`, `nums2 = [1,2,3]`, `k = 2`. The output should be `[[1,1],[1,1]]`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible pairs of numbers from `nums1` and `nums2`, calculate their sums, and then sort these pairs based on their sums.
- Step-by-step breakdown of the solution:
  1. Initialize an empty list to store all pairs.
  2. Iterate over each element in `nums1`.
  3. For each element in `nums1`, iterate over each element in `nums2`.
  4. Calculate the sum of the current pair and store the pair along with its sum.
  5. Sort the list of pairs based on their sums.
  6. Return the first `k` pairs from the sorted list.

```cpp
vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
    vector<vector<int>> pairs;
    for (int i = 0; i < nums1.size(); i++) {
        for (int j = 0; j < nums2.size(); j++) {
            pairs.push_back({nums1[i], nums2[j]});
        }
    }
    sort(pairs.begin(), pairs.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] + a[1] < b[0] + b[1];
    });
    if (k > pairs.size()) k = pairs.size();
    return vector<vector<int>>(pairs.begin(), pairs.begin() + k);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot \log(n \cdot m))$, where $n$ and $m$ are the sizes of `nums1` and `nums2`, respectively. This is because we generate $n \cdot m$ pairs and then sort them.
> - **Space Complexity:** $O(n \cdot m)$, as we store all pairs in memory.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, while storing all pairs contributes to the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a min-heap to store pairs. We start by pushing the first pair of each element in `nums1` with all elements in `nums2` into the heap. Then, we pop the smallest pair from the heap, add it to the result, and push the next pair from the same element in `nums1` into the heap.
- Detailed breakdown of the approach:
  1. Initialize a min-heap to store pairs along with their indices in `nums1` and `nums2`.
  2. Push the first pair of each element in `nums1` with the first element in `nums2` into the heap.
  3. Initialize an empty list to store the result.
  4. While the heap is not empty and we have not found `k` pairs:
    - Pop the smallest pair from the heap and add it to the result.
    - If the popped pair's element from `nums2` is not the last element in `nums2`, push the next pair into the heap.
  5. Return the result.

```cpp
vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
    auto cmp = [](const pair<int, pair<int, int>>& a, const pair<int, pair<int, int>>& b) {
        return a.first > b.first;
    };
    priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, decltype(cmp)> pq(cmp);
    for (int i = 0; i < nums1.size(); i++) {
        pq.push({nums1[i] + nums2[0], {i, 0}});
    }
    vector<vector<int>> result;
    while (!pq.empty() && result.size() < k) {
        auto [sum, indices] = pq.top(); pq.pop();
        result.push_back({nums1[indices.first], nums2[indices.second]});
        if (indices.second + 1 < nums2.size()) {
            pq.push({nums1[indices.first] + nums2[indices.second + 1], {indices.first, indices.second + 1}});
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot \log(n))$, where $n$ is the size of `nums1`. This is because we perform a heap operation for each of the `k` pairs, and each heap operation takes $\log(n)$ time.
> - **Space Complexity:** $O(n)$, as we store at most $n$ pairs in the heap.
> - **Optimality proof:** This approach is optimal because it uses a min-heap to efficiently find the smallest pair at each step, avoiding the need to sort all pairs or generate all possible pairs.