## Least Number of Unique Integers after K Removals

**Problem Link:** https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description

**Problem Statement:**
- Input: An array of integers `arr` and an integer `k`.
- Constraints: `1 <= arr.length <= 10^5`, `1 <= arr[i] <= 10^5`, `0 <= k <= arr.length`.
- Expected Output: The least number of unique integers after removing `k` elements from `arr`.
- Key Requirements: Minimize the number of unique integers after removals.
- Edge Cases: Empty array, `k` equals the length of the array, all elements are unique.

**Example Test Cases:**
- `arr = [5,5,4], k = 1` -> Output: `1` (Remove one of the `5`s to get `[5, 4]`, then remove the `4` to get `[5]`).
- `arr = [4,3,1,1,3,3,2], k = 3` -> Output: `2` (Remove two `3`s and one `1` to get `[4, 1, 1, 2]`).

---

### Brute Force Approach

**Explanation:**
- Sort the array and use a frequency map to count occurrences of each integer.
- Iterate through the frequency map and remove the smallest frequency integers first.
- Update the count of unique integers after each removal.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

int findLeastNumOfUniqueInts(vector<int>& arr, int k) {
    unordered_map<int, int> freqMap;
    for (int num : arr) {
        freqMap[num]++;
    }
    vector<pair<int, int>> freqs;
    for (auto& pair : freqMap) {
        freqs.push_back({pair.second, pair.first});
    }
    sort(freqs.begin(), freqs.end());
    int uniqueCount = freqs.size();
    for (auto& pair : freqs) {
        if (k >= pair.first) {
            k -= pair.first;
            uniqueCount--;
        } else {
            break;
        }
    }
    return uniqueCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of unique integers. This is due to sorting the frequency vector.
> - **Space Complexity:** $O(n)$, where $n$ is the total number of elements in the array. This is for storing the frequency map and the sorted frequency vector.
> - **Why these complexities occur:** The brute force approach involves sorting the frequency vector, which dominates the time complexity. The space complexity is due to the extra space needed for the frequency map and the sorted frequency vector.

---

### Optimal Approach (Required)

**Explanation:**
- Use a similar approach as the brute force but optimize the sorting step by using a priority queue or a multiset to store the frequency map.
- This allows for efficient removal of the smallest frequency integers.

```cpp
#include <iostream>
#include <vector>
#include <queue>

int findLeastNumOfUniqueInts(vector<int>& arr, int k) {
    unordered_map<int, int> freqMap;
    for (int num : arr) {
        freqMap[num]++;
    }
    priority_queue<int, vector<int>, greater<int>> pq;
    for (auto& pair : freqMap) {
        pq.push(pair.second);
    }
    while (!pq.empty() && k >= pq.top()) {
        k -= pq.top();
        pq.pop();
    }
    return pq.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of unique integers. This is due to inserting elements into the priority queue.
> - **Space Complexity:** $O(n)$, where $n$ is the total number of elements in the array. This is for storing the frequency map and the priority queue.
> - **Optimality proof:** This approach is optimal because it efficiently removes the smallest frequency integers first, minimizing the number of unique integers after removals.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: frequency mapping, sorting, priority queues.
- Problem-solving patterns identified: optimizing brute force approaches, using data structures for efficient operations.
- Optimization techniques learned: using priority queues for efficient removal of smallest elements.
- Similar problems to practice: other frequency-based problems, optimization problems using data structures.

**Mistakes to Avoid:**
- Common implementation errors: incorrect use of data structures, inefficient sorting or removal operations.
- Edge cases to watch for: empty arrays, `k` equals the length of the array, all elements are unique.
- Performance pitfalls: using inefficient data structures or algorithms, not optimizing brute force approaches.
- Testing considerations: thoroughly testing edge cases, verifying correctness of the solution.