## Dinner Plate Stacks
**Problem Link:** https://leetcode.com/problems/dinner-plate-stacks/description

**Problem Statement:**
- Input format: `stackSize`, an integer array where each element represents the size of a dinner plate stack, and `k`, the number of dinner plates.
- Constraints: `1 <= k <= 10^9`, `1 <= stackSize.length <= 10^5`, and `1 <= stackSize[i] <= 10^5`.
- Expected output format: The maximum number of dinner plates that can be stacked.
- Key requirements and edge cases to consider: 
  - The number of plates should not exceed `k`.
  - Each stack should have a size that does not exceed the corresponding element in `stackSize`.
- Example test cases with explanations:
  - For `stackSize = [3,5,2]` and `k = 7`, the maximum number of dinner plates that can be stacked is `9`.
  - For `stackSize = [2]` and `k = 2`, the maximum number of dinner plates that can be stacked is `2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of stacks to find the maximum number of plates that can be stacked.
- Step-by-step breakdown of the solution:
  1. Initialize a variable to store the maximum number of plates.
  2. Iterate over all possible combinations of stacks.
  3. For each combination, calculate the total number of plates that can be stacked.
  4. Update the maximum number of plates if the current combination has more plates.
- Why this approach comes to mind first: It's a straightforward way to solve the problem by trying all possible combinations.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maxNumber(vector<int>& stackSize, int k) {
    int maxPlates = 0;
    for (int i = 0; i < (1 << stackSize.size()); i++) {
        int currentPlates = 0;
        for (int j = 0; j < stackSize.size(); j++) {
            if ((i & (1 << j)) != 0) {
                currentPlates += stackSize[j];
            }
        }
        if (currentPlates <= k) {
            maxPlates = max(maxPlates, currentPlates);
        }
    }
    return maxPlates;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of stacks. This is because we're iterating over all possible combinations of stacks, which is $2^n$, and for each combination, we're calculating the total number of plates, which takes $O(n)$ time.
> - **Space Complexity:** $O(1)$, as we're only using a constant amount of space to store the maximum number of plates.
> - **Why these complexities occur:** The time complexity occurs because we're trying all possible combinations of stacks, which results in an exponential number of iterations. The space complexity is constant because we're only using a fixed amount of space to store the maximum number of plates.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a priority queue to store the stacks and always add plates to the stack with the most remaining capacity.
- Detailed breakdown of the approach:
  1. Initialize a priority queue to store the stacks, where each stack is represented by its remaining capacity.
  2. Iterate over the stacks and add them to the priority queue.
  3. Iterate over the plates and add them to the stack with the most remaining capacity.
  4. Update the remaining capacity of the stack after adding a plate.
- Proof of optimality: This approach is optimal because it always adds plates to the stack with the most remaining capacity, which maximizes the total number of plates that can be stacked.

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int maxNumber(vector<int>& stackSize, int k) {
    priority_queue<int> pq;
    for (int size : stackSize) {
        pq.push(size);
    }
    int maxPlates = 0;
    for (int i = 0; i < k; i++) {
        if (pq.empty()) break;
        int currentStack = pq.top();
        pq.pop();
        maxPlates++;
        if (currentStack > 1) {
            pq.push(currentStack - 1);
        }
    }
    return maxPlates;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k \cdot \log n)$, where $n$ is the number of stacks. This is because we're iterating over the plates and for each plate, we're adding it to the stack with the most remaining capacity, which takes $O(\log n)$ time using the priority queue.
> - **Space Complexity:** $O(n)$, as we're storing the stacks in the priority queue.
> - **Optimality proof:** This approach is optimal because it always adds plates to the stack with the most remaining capacity, which maximizes the total number of plates that can be stacked.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queues, greedy algorithms.
- Problem-solving patterns identified: Always add plates to the stack with the most remaining capacity.
- Optimization techniques learned: Using priority queues to efficiently select the stack with the most remaining capacity.
- Similar problems to practice: Other problems that involve maximizing or minimizing a quantity using a priority queue.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the remaining capacity of the stack after adding a plate.
- Edge cases to watch for: When the number of plates exceeds the total capacity of all stacks.
- Performance pitfalls: Using a brute force approach that tries all possible combinations of stacks.
- Testing considerations: Test the solution with different inputs, including edge cases and large inputs.