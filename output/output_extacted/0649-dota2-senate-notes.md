## Dota2 Senate

**Problem Link:** [https://leetcode.com/problems/dota2-senate/description](https://leetcode.com/problems/dota2-senate/description)

**Problem Statement:**
- Input format and constraints: The input is a string `senate` consisting of characters 'R' and 'D', representing the senate with Radiant and Dire senators.
- Expected output format: The output should be a string indicating which party is in control after all senators have voted.
- Key requirements and edge cases to consider: The problem requires implementing a simulation of the voting process, considering the rules that a senator can only vote against a senator from the opposing party.
- Example test cases with explanations: For example, if the input is "RD", the output should be "Radiant" because the Radiant senator votes against the Dire senator first.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Implement a simulation of the voting process, using a queue to keep track of the senators and their voting order.
- Step-by-step breakdown of the solution: 
  1. Initialize two queues, one for Radiant senators and one for Dire senators.
  2. Add all senators to their respective queues.
  3. While both queues are not empty, have the senator at the front of one queue vote against the senator at the front of the other queue.
  4. Remove the voted senator from their queue.
  5. If one queue becomes empty, the party with the non-empty queue is in control.
- Why this approach comes to mind first: This approach is straightforward and directly simulates the voting process as described in the problem.

```cpp
#include <iostream>
#include <queue>
#include <string>

string predictPartyVictory(string senate) {
    queue<int> radiant, dire;
    for (int i = 0; i < senate.size(); i++) {
        if (senate[i] == 'R') {
            radiant.push(i);
        } else {
            dire.push(i);
        }
    }
    
    while (!radiant.empty() && !dire.empty()) {
        if (radiant.front() < dire.front()) {
            radiant.push(radiant.front() + senate.size());
            dire.pop();
        } else {
            dire.push(dire.front() + senate.size());
            radiant.pop();
        }
        radiant.pop();
        dire.pop();
    }
    
    return radiant.empty() ? "Dire" : "Radiant";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of senators and $m$ is the number of rounds. In the worst case, each senator can vote against every other senator.
> - **Space Complexity:** $O(n)$ for storing the senators in the queues.
> - **Why these complexities occur:** The time complexity is due to the simulation of the voting process, and the space complexity is due to the storage of the senators in the queues.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of simulating the voting process round by round, we can directly calculate the outcome by comparing the initial positions of the senators.
- Detailed breakdown of the approach: 
  1. Initialize two queues, one for Radiant senators and one for Dire senators, and store the initial positions of the senators.
  2. While both queues are not empty, compare the positions of the senators at the front of the queues.
  3. If the position of the Radiant senator is less than the position of the Dire senator, the Radiant senator votes against the Dire senator and wins. Otherwise, the Dire senator votes against the Radiant senator and wins.
  4. Update the position of the winning senator to be after the losing senator.
  5. Remove the losing senator from their queue.
- Proof of optimality: This approach is optimal because it directly calculates the outcome of the voting process without simulating each round, reducing the time complexity to $O(n)$.

```cpp
#include <iostream>
#include <queue>
#include <string>

string predictPartyVictory(string senate) {
    queue<int> radiant, dire;
    for (int i = 0; i < senate.size(); i++) {
        if (senate[i] == 'R') {
            radiant.push(i);
        } else {
            dire.push(i);
        }
    }
    
    while (!radiant.empty() && !dire.empty()) {
        if (radiant.front() < dire.front()) {
            radiant.push(radiant.front() + senate.size());
            radiant.pop();
            dire.pop();
        } else {
            dire.push(dire.front() + senate.size());
            dire.pop();
            radiant.pop();
        }
    }
    
    return radiant.empty() ? "Dire" : "Radiant";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of senators.
> - **Space Complexity:** $O(n)$ for storing the senators in the queues.
> - **Optimality proof:** This approach is optimal because it directly calculates the outcome of the voting process without simulating each round.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Simulation, queue data structure, and optimization techniques.
- Problem-solving patterns identified: Direct calculation of the outcome instead of simulation.
- Optimization techniques learned: Reducing the time complexity by directly calculating the outcome.
- Similar problems to practice: Problems involving simulation and optimization.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating the positions of the senators.
- Edge cases to watch for: Handling the case where one party has no senators.
- Performance pitfalls: Simulating each round of the voting process instead of directly calculating the outcome.
- Testing considerations: Testing the function with different input strings and edge cases.