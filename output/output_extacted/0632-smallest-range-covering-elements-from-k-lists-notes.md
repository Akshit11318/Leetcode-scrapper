## Smallest Range Covering Elements from K Lists

**Problem Link:** https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description

**Problem Statement:**
- Input format and constraints: Given `k` sorted lists of integers, find the smallest range that covers at least one integer from each of the `k` lists.
- Expected output format: Return a list of two integers representing the smallest range.
- Key requirements and edge cases to consider:
  - Each list has at least one integer.
  - The input lists are non-empty and sorted in ascending order.
- Example test cases with explanations:
  - Example 1: Input: `nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]`. Output: `[20,24]`. Explanation: The range `[20,24]` covers `20` from the first list, `20` from the second list, and `22` from the third list.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each possible range, check if it covers at least one integer from each list.
- Step-by-step breakdown of the solution:
  1. Iterate over all possible ranges.
  2. For each range, check if it covers at least one integer from each list.
  3. If a range covers all lists, update the smallest range.
- Why this approach comes to mind first: It's a straightforward way to solve the problem by checking all possible solutions.

```cpp
#include <vector>
#include <algorithm>

std::vector<int> smallestRange(std::vector<std::vector<int>>& nums) {
    int minVal = *std::min_element(nums[0].begin(), nums[0].end());
    int maxVal = *std::max_element(nums[0].begin(), nums[0].end());
    for (auto& list : nums) {
        minVal = std::min(minVal, *std::min_element(list.begin(), list.end()));
        maxVal = std::max(maxVal, *std::max_element(list.begin(), list.end()));
    }
    
    std::vector<int> smallestRange = {minVal, maxVal};
    for (int i = minVal; i <= maxVal; ++i) {
        for (int j = i; j <= maxVal; ++j) {
            bool coversAll = true;
            for (auto& list : nums) {
                if (!std::any_of(list.begin(), list.end(), [i, j](int x){ return i <= x && x <= j; })) {
                    coversAll = false;
                    break;
                }
            }
            if (coversAll) {
                if (j - i < smallestRange[1] - smallestRange[0]) {
                    smallestRange = {i, j};
                }
            }
        }
    }
    return smallestRange;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 * k * m)$, where $n$ is the range of values, $k$ is the number of lists, and $m$ is the maximum size of a list. This is because for each possible range, we check all lists.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the smallest range.
> - **Why these complexities occur:** The brute force approach checks all possible ranges and for each range, it checks all lists, resulting in high time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a priority queue to keep track of the smallest range that covers all lists.
- Detailed breakdown of the approach:
  1. Initialize a priority queue with the first element from each list along with its list index and element index.
  2. Initialize the smallest range to the maximum possible range.
  3. While the priority queue is not empty:
    - Dequeue the smallest element.
    - If the current range (from the smallest to the largest element in the priority queue) is smaller than the smallest range, update the smallest range.
    - If the dequeued element is the last element in its list, break the loop.
    - Enqueue the next element from the same list.
- Proof of optimality: This approach ensures that we always consider the smallest possible range that covers all lists, resulting in the optimal solution.

```cpp
#include <queue>
#include <vector>

struct Node {
    int val, i, j;
    bool operator<(const Node& other) const {
        return val > other.val;
    }
};

std::vector<int> smallestRange(std::vector<std::vector<int>>& nums) {
    std::priority_queue<Node> pq;
    int maxVal = INT_MIN;
    for (int i = 0; i < nums.size(); ++i) {
        pq.push({nums[i][0], i, 0});
        maxVal = std::max(maxVal, nums[i][0]);
    }
    
    int range = INT_MAX;
    std::vector<int> res = {-100000, 100000};
    while (true) {
        Node node = pq.top();
        pq.pop();
        if (maxVal - node.val < range) {
            range = maxVal - node.val;
            res = {node.val, maxVal};
        }
        if (node.j + 1 == nums[node.i].size()) break;
        pq.push({nums[node.i][node.j + 1], node.i, node.j + 1});
        maxVal = std::max(maxVal, nums[node.i][node.j + 1]);
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \log k)$, where $N$ is the total number of elements and $k$ is the number of lists. This is because we perform a heap operation for each element.
> - **Space Complexity:** $O(k)$, as we use a priority queue to store the current elements from each list.
> - **Optimality proof:** This approach ensures that we always consider the smallest possible range that covers all lists, resulting in the optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queue, range searching.
- Problem-solving patterns identified: Using a priority queue to keep track of the smallest range.
- Optimization techniques learned: Avoiding unnecessary checks by using a priority queue.
- Similar problems to practice: Range searching, interval scheduling.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the maximum value correctly, not handling the case where a list is empty.
- Edge cases to watch for: Lists with a single element, lists with duplicate elements.
- Performance pitfalls: Using a brute force approach, not using a priority queue.
- Testing considerations: Test cases with different list sizes, test cases with duplicate elements.