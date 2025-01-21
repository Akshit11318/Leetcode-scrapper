## Remove Stones to Minimize the Total

**Problem Link:** https://leetcode.com/problems/remove-stones-to-minimize-the-total/description

**Problem Statement:**
- Input: `piles` - a list of integers representing the number of stones in each pile, and `k` - an integer representing the number of stones to remove from each pile.
- Output: The minimum number of stones left after removing `k` stones from each pile.
- Key Requirements: Remove `k` stones from each pile to minimize the total number of stones left.
- Edge Cases: If `k` is greater than or equal to the number of stones in a pile, all stones from that pile can be removed.

**Example Test Cases:**
- Input: `piles = [4,5,9,4,4,6,1,1,3,5]`, `k = 3`
- Output: `12`
- Explanation: Remove 3 stones from each pile to get `[1,2,6,1,1,3,1,1,0,2]`. The total number of stones left is `1 + 2 + 6 + 1 + 1 + 3 + 1 + 1 + 0 + 2 = 18`. However, this is not the minimum possible total. A more optimal approach is required.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of removing `k` stones from each pile.
- However, this approach is impractical due to its high computational complexity.

```cpp
#include <vector>
#include <algorithm>
#include <numeric>

int minStoneSum(std::vector<int>& piles, int k) {
    // Generate all possible combinations of removing k stones from each pile
    // This approach is not practical due to its high computational complexity
    // and is not implemented here due to its inefficiency.
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of piles. This is because for each pile, we have two choices: remove `k` stones or do not remove any stones.
> - **Space Complexity:** $O(n)$, for storing the recursive call stack.
> - **Why these complexities occur:** The high time complexity occurs because we are trying all possible combinations, resulting in exponential time complexity. The space complexity is linear due to the recursive call stack.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a priority queue to keep track of the pile with the maximum number of stones.
- We remove `k` stones from the pile with the maximum number of stones and update the priority queue.
- We repeat this process until all piles have been processed.

```cpp
#include <queue>
#include <vector>

int minStoneSum(std::vector<int>& piles, int k) {
    // Create a max heap to store the piles
    std::priority_queue<int> maxHeap;
    for (int pile : piles) {
        maxHeap.push(pile);
    }
    
    // Remove k stones from the pile with the maximum number of stones
    for (int i = 0; i < k; i++) {
        int maxPile = maxHeap.top();
        maxHeap.pop();
        maxPile = (maxPile + 1) / 2;
        maxHeap.push(maxPile);
    }
    
    // Calculate the total number of stones left
    int totalStones = 0;
    while (!maxHeap.empty()) {
        totalStones += maxHeap.top();
        maxHeap.pop();
    }
    
    return totalStones;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + k \log n)$, where $n$ is the number of piles. This is because we are using a priority queue to keep track of the pile with the maximum number of stones, and we are removing `k` stones from the pile with the maximum number of stones.
> - **Space Complexity:** $O(n)$, for storing the priority queue.
> - **Optimality proof:** This approach is optimal because we are always removing stones from the pile with the maximum number of stones, resulting in the minimum total number of stones left.

---

### Final Notes

**Learning Points:**
- The importance of using a priority queue to keep track of the maximum or minimum element in a collection.
- The use of a max heap to efficiently remove the maximum element from a collection.
- The application of greedy algorithms to solve optimization problems.

**Mistakes to Avoid:**
- Not considering the use of a priority queue to efficiently solve the problem.
- Not updating the priority queue correctly after removing stones from a pile.
- Not calculating the total number of stones left correctly.

**Similar Problems to Practice:**
- [LeetCode 215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [LeetCode 703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)