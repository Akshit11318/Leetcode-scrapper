## Number of Recent Calls
**Problem Link:** https://leetcode.com/problems/number-of-recent-calls/description

**Problem Statement:**
- Input format and constraints: The problem involves implementing a class called `RecentCounter` which has a method `ping(t: int)` that increments the timestamp `t` and returns the number of calls `ping` that have timestamps not older than `3000` milliseconds.
- Expected output format: The `ping` method returns an integer representing the number of recent calls.
- Key requirements and edge cases to consider: 
    - The `ping` method is called multiple times with different timestamps.
    - The method should return the correct count of recent calls.
    - Edge cases include when the queue is empty, when a new call is added, and when the queue size exceeds the limit.
- Example test cases with explanations:
    - `RecentCounter()`
    - `ping(1) // returns 1`
    - `ping(100) // returns 2`
    - `ping(3001) // returns 3`
    - `ping(3002) // returns 3`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To solve this problem, we can use a queue data structure to store the timestamps of the calls. When a new call is made, we add the timestamp to the queue. Then, we remove the timestamps that are older than `3000` milliseconds from the front of the queue.
- Step-by-step breakdown of the solution:
    1. Create a queue to store the timestamps of the calls.
    2. When a new call is made, add the timestamp to the queue.
    3. Remove the timestamps that are older than `3000` milliseconds from the front of the queue.
    4. Return the size of the queue as the number of recent calls.

```cpp
class RecentCounter {
private:
    queue<int> q;
public:
    RecentCounter() {}
    
    int ping(int t) {
        q.push(t);
        while (!q.empty() && t - q.front() > 3000) {
            q.pop();
        }
        return q.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of calls made. This is because in the worst case, we might need to remove all the elements from the queue.
> - **Space Complexity:** $O(n)$, where $n$ is the number of calls made. This is because we are storing all the timestamps in the queue.
> - **Why these complexities occur:** These complexities occur because we are using a queue to store the timestamps and we are removing the old timestamps from the queue.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is to use a queue to store the timestamps of the calls. When a new call is made, we add the timestamp to the queue. Then, we remove the timestamps that are older than `3000` milliseconds from the front of the queue.
- Detailed breakdown of the approach: 
    1. Create a queue to store the timestamps of the calls.
    2. When a new call is made, add the timestamp to the queue.
    3. Remove the timestamps that are older than `3000` milliseconds from the front of the queue.
    4. Return the size of the queue as the number of recent calls.
- Proof of optimality: This solution is optimal because it uses a queue to store the timestamps, which allows us to efficiently remove the old timestamps.

```cpp
class RecentCounter {
private:
    queue<int> q;
public:
    RecentCounter() {}
    
    int ping(int t) {
        q.push(t);
        while (!q.empty() && t - q.front() > 3000) {
            q.pop();
        }
        return q.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of calls made. This is because in the worst case, we might need to remove all the elements from the queue.
> - **Space Complexity:** $O(n)$, where $n$ is the number of calls made. This is because we are storing all the timestamps in the queue.
> - **Optimality proof:** This solution is optimal because it uses a queue to store the timestamps, which allows us to efficiently remove the old timestamps.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a queue to store the timestamps of the calls.
- Problem-solving patterns identified: Removing the old timestamps from the queue when a new call is made.
- Optimization techniques learned: Using a queue to efficiently remove the old timestamps.
- Similar problems to practice: Problems that involve using a queue to store data and remove old data.

**Mistakes to Avoid:**
- Common implementation errors: Not removing the old timestamps from the queue.
- Edge cases to watch for: When the queue is empty, when a new call is added, and when the queue size exceeds the limit.
- Performance pitfalls: Using a data structure that is not efficient for removing old data.
- Testing considerations: Testing the solution with different inputs and edge cases.