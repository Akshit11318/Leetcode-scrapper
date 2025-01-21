## Last Stone Weight
**Problem Link:** https://leetcode.com/problems/last-stone-weight/description

**Problem Statement:**
- Input format: An array of integers `stones` representing the weights of the stones.
- Constraints: `1 <= stones.length <= 30`, `1 <= stones[i] <= 1000`.
- Expected output format: The weight of the last stone remaining.
- Key requirements and edge cases to consider: If there are no stones left, return `0`. If there is only one stone left, return its weight.
- Example test cases with explanations:
  - `stones = [2,7,4,1,8,1]`: The last stone weight is `1`.
  - `stones = [1,2]`: The last stone weight is `1`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Simulate the process of smashing stones until only one or no stones are left.
- Step-by-step breakdown of the solution:
  1. Sort the array of stones in ascending order.
  2. While there are more than one stone, smash the two heaviest stones.
  3. If the two stones are not the same weight, add the difference back into the array.
  4. Repeat steps 1-3 until only one or no stones are left.
- Why this approach comes to mind first: It directly simulates the process described in the problem.

```cpp
#include <queue>
using namespace std;

int lastStoneWeight(vector<int>& stones) {
    priority_queue<int> pq;
    for (int stone : stones) {
        pq.push(stone);
    }
    
    while (pq.size() > 1) {
        int x = pq.top();
        pq.pop();
        int y = pq.top();
        pq.pop();
        if (x != y) {
            pq.push(abs(x - y));
        }
    }
    
    return pq.empty() ? 0 : pq.top();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of stones. The reason is that we are using a priority queue to sort the stones, and each insertion and deletion operation takes $O(\log n)$ time. We do this $n$ times, so the total time complexity is $O(n \log n)$.
> - **Space Complexity:** $O(n)$, as we are storing all stones in the priority queue.
> - **Why these complexities occur:** The priority queue operations (insertion and deletion) cause these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using a priority queue to efficiently select the heaviest stones to smash.
- Detailed breakdown of the approach:
  1. Create a max heap (priority queue) from the array of stones.
  2. While there are more than one stone, smash the two heaviest stones.
  3. If the two stones are not the same weight, add the difference back into the heap.
  4. Repeat steps 1-3 until only one or no stones are left.
- Proof of optimality: This approach ensures that we always smash the heaviest stones first, which is the optimal strategy.
- Why further optimization is impossible: This approach already uses the most efficient data structure (priority queue) for selecting the heaviest stones.

```cpp
#include <queue>
using namespace std;

int lastStoneWeight(vector<int>& stones) {
    priority_queue<int> pq;
    for (int stone : stones) {
        pq.push(stone);
    }
    
    while (pq.size() > 1) {
        int x = pq.top();
        pq.pop();
        int y = pq.top();
        pq.pop();
        if (x != y) {
            pq.push(abs(x - y));
        }
    }
    
    return pq.empty() ? 0 : pq.top();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of stones. The reason is that we are using a priority queue to sort the stones, and each insertion and deletion operation takes $O(\log n)$ time. We do this $n$ times, so the total time complexity is $O(n \log n)$.
> - **Space Complexity:** $O(n)$, as we are storing all stones in the priority queue.
> - **Optimality proof:** This approach ensures that we always smash the heaviest stones first, which is the optimal strategy.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a priority queue to efficiently select the heaviest stones.
- Problem-solving patterns identified: Simulating a process and optimizing it using the right data structure.
- Optimization techniques learned: Using a priority queue to reduce the time complexity of selecting the heaviest stones.
- Similar problems to practice: Other problems that involve simulating a process and optimizing it using the right data structure.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the priority queue is empty before popping an element.
- Edge cases to watch for: If there are no stones left, return `0`. If there is only one stone left, return its weight.
- Performance pitfalls: Using a data structure with a higher time complexity than necessary.
- Testing considerations: Test the function with different inputs, including edge cases.