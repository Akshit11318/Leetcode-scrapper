## Number of People Aware of a Secret
**Problem Link:** https://leetcode.com/problems/number-of-people-aware-of-a-secret/description

**Problem Statement:**
- Input format and constraints: The problem involves a secret that spreads through a population over time, with a person sharing the secret with another person each day. The constraints include the number of days (`days`) and the delay before the first person shares the secret with another person (`delay`).
- Expected output format: The expected output is the number of people who are aware of the secret on the `days`-th day.
- Key requirements and edge cases to consider: The key requirements include handling the spread of the secret over time, considering the delay before sharing, and accounting for the maximum number of people who can share the secret each day.
- Example test cases with explanations: For example, if `n = 6`, `delay = 2`, and `forget = 4`, the output should be `5`, because after `6` days, `5` people will know the secret.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves simulating the spread of the secret over time, keeping track of the number of people who are aware of the secret each day.
- Step-by-step breakdown of the solution: 
  1. Initialize a variable to keep track of the number of people who know the secret.
  2. Iterate over each day, starting from the `delay`-th day.
  3. For each day, increment the number of people who know the secret by the number of people who can share the secret.
  4. If a person forgets the secret, decrement the number of people who know the secret.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, as it directly simulates the spread of the secret over time.

```cpp
int peopleAwareOfSecret(int n, int delay, int forget) {
    int peopleAware = 0;
    int share = 0;
    queue<int> q;
    
    for (int i = 1; i <= n; i++) {
        if (i >= delay) {
            q.push(i);
            share++;
        }
        
        if (!q.empty() && q.front() + forget == i) {
            q.pop();
            share--;
        }
        
        peopleAware = share;
    }
    
    return peopleAware;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of days, because we iterate over each day once.
> - **Space Complexity:** $O(n)$, because in the worst case, the queue can contain up to $n$ elements.
> - **Why these complexities occur:** These complexities occur because we simulate the spread of the secret over time, keeping track of the number of people who are aware of the secret each day.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a queue to keep track of the days when each person shares the secret, and to update the number of people who know the secret based on the queue.
- Detailed breakdown of the approach:
  1. Initialize a queue to keep track of the days when each person shares the secret.
  2. Iterate over each day, starting from the `delay`-th day.
  3. For each day, add the day to the queue if it is the `delay`-th day or later.
  4. If a person forgets the secret, remove the day from the queue.
  5. Update the number of people who know the secret based on the queue.
- Proof of optimality: This approach is optimal because it uses a queue to efficiently keep track of the days when each person shares the secret, and it updates the number of people who know the secret based on the queue.

```cpp
int peopleAwareOfSecret(int n, int delay, int forget) {
    int peopleAware = 0;
    queue<int> q;
    
    for (int i = 1; i <= n; i++) {
        if (i >= delay) {
            q.push(i);
        }
        
        if (!q.empty() && q.front() + forget == i) {
            q.pop();
        }
        
        peopleAware = q.size();
    }
    
    return peopleAware;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of days, because we iterate over each day once.
> - **Space Complexity:** $O(n)$, because in the worst case, the queue can contain up to $n$ elements.
> - **Optimality proof:** This approach is optimal because it uses a queue to efficiently keep track of the days when each person shares the secret, and it updates the number of people who know the secret based on the queue.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of a queue to keep track of the days when each person shares the secret, and to update the number of people who know the secret based on the queue.
- Problem-solving patterns identified: The problem requires simulating the spread of the secret over time, and updating the number of people who know the secret based on the queue.
- Optimization techniques learned: The problem requires using a queue to efficiently keep track of the days when each person shares the secret, and to update the number of people who know the secret based on the queue.
- Similar problems to practice: Similar problems include simulating the spread of a disease, or modeling the growth of a population over time.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to not update the number of people who know the secret based on the queue.
- Edge cases to watch for: An edge case to watch for is when the `delay` is greater than the `forget` time, in which case the number of people who know the secret will decrease over time.
- Performance pitfalls: A performance pitfall is to use a naive approach that simulates the spread of the secret over time without using a queue, which can result in a time complexity of $O(n^2)$.
- Testing considerations: When testing the solution, it is important to consider different scenarios, such as when the `delay` is greater than the `forget` time, or when the number of days is large.