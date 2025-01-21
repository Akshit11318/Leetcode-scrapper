## Maximum Number of Eaten Apples
**Problem Link:** https://leetcode.com/problems/maximum-number-of-eaten-apples/description

**Problem Statement:**
- Input format and constraints: The problem takes in two arrays, `apples` and `days`, where `apples[i]` is the number of apples and `days[i]` is the number of days until the apples at index `i` are rotten. The goal is to determine the maximum number of apples that can be eaten before they rot.
- Expected output format: The function should return the maximum number of apples that can be eaten.
- Key requirements and edge cases to consider: The problem requires finding the optimal way to eat the apples to maximize the number eaten before they rot. This involves sorting the apples based on their expiration dates and eating them in that order.
- Example test cases with explanations:
    - Example 1: `apples = [1,2,3,5,2]`, `days = [3,2,1,4,2]`. In this case, the optimal way to eat the apples is to eat the ones that expire first.
    - Example 2: `apples = [3,0,0,0,0,2]`, `days = [3,0,0,0,0,3]`. Here, the apples that expire first should be eaten first.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial thought is to try all possible combinations of eating the apples and see which combination results in the maximum number of apples eaten.
- Step-by-step breakdown of the solution: 
    1. Generate all possible combinations of eating the apples.
    2. For each combination, calculate the number of apples eaten before they rot.
    3. Keep track of the combination that results in the maximum number of apples eaten.
- Why this approach comes to mind first: This approach comes to mind first because it is a straightforward way to solve the problem. However, it is not efficient for large inputs.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int eatenApples(std::vector<int>& apples, std::vector<int>& days) {
    int n = apples.size();
    int maxApples = 0;
    // Try all possible combinations of eating the apples
    for (int mask = 0; mask < (1 << n); mask++) {
        int currApples = 0;
        std::vector<int> eaten(n, 0);
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                // Eat the apples at index i
                int eatenApples = std::min(apples[i], days[i]);
                eaten[i] = eatenApples;
                currApples += eatenApples;
            }
        }
        maxApples = std::max(maxApples, currApples);
    }
    return maxApples;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the number of apples. This is because we are trying all possible combinations of eating the apples.
> - **Space Complexity:** $O(n)$, where $n$ is the number of apples. This is because we are using a vector to keep track of the eaten apples.
> - **Why these complexities occur:** These complexities occur because we are using a brute force approach that tries all possible combinations of eating the apples.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a priority queue to keep track of the apples that expire first. We can use a pair to store the expiration date and the number of apples.
- Detailed breakdown of the approach: 
    1. Create a priority queue to store the apples that expire first.
    2. Iterate through the apples and add them to the priority queue.
    3. While the priority queue is not empty, eat the apples that expire first.
- Proof of optimality: This approach is optimal because it ensures that the apples that expire first are eaten first.

```cpp
#include <iostream>
#include <vector>
#include <queue>

struct Apple {
    int expirationDate;
    int numApples;
};

struct Compare {
    bool operator()(const Apple& a, const Apple& b) {
        return a.expirationDate > b.expirationDate;
    }
};

int eatenApples(std::vector<int>& apples, std::vector<int>& days) {
    int n = apples.size();
    int maxApples = 0;
    std::priority_queue<Apple, std::vector<Apple>, Compare> pq;
    int currDay = 0;
    for (int i = 0; i < n; i++) {
        // Add the apples to the priority queue
        Apple a = {currDay + days[i], apples[i]};
        pq.push(a);
        // Eat the apples that expire first
        while (!pq.empty()) {
            Apple top = pq.top();
            if (top.expirationDate <= currDay) {
                // The apples have expired, remove them from the queue
                pq.pop();
            } else {
                // Eat the apples
                int eatenApples = std::min(top.numApples, top.expirationDate - currDay);
                maxApples += eatenApples;
                // Update the number of apples
                top.numApples -= eatenApples;
                // Update the expiration date
                top.expirationDate = currDay + eatenApples;
                // Push the updated apple back into the queue
                pq.pop();
                pq.push(top);
                break;
            }
        }
        currDay++;
    }
    return maxApples;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of apples. This is because we are using a priority queue to keep track of the apples that expire first.
> - **Space Complexity:** $O(n)$, where $n$ is the number of apples. This is because we are using a priority queue to store the apples.
> - **Optimality proof:** This approach is optimal because it ensures that the apples that expire first are eaten first.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queues, greedy algorithms.
- Problem-solving patterns identified: Using priority queues to keep track of the most important items.
- Optimization techniques learned: Using a priority queue to ensure that the most important items are processed first.
- Similar problems to practice: Problems that involve using priority queues to solve optimization problems.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, not handling errors properly.
- Edge cases to watch for: Handling the case where the number of apples is zero, handling the case where the expiration date is zero.
- Performance pitfalls: Not using a priority queue to keep track of the apples that expire first.
- Testing considerations: Testing the function with different inputs, testing the function with edge cases.