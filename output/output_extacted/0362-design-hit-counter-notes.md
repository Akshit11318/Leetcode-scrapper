## Design Hit Counter

**Problem Link:** [https://leetcode.com/problems/design-hit-counter/description](https://leetcode.com/problems/design-hit-counter/description)

**Problem Statement:**
- Input format and constraints: The `HitCounter` class will receive a series of `hit` and `getHits` method calls with specific timestamps. Each `hit` method call takes a timestamp as input, and each `getHits` method call takes a timestamp as input and returns the number of hits in the last 5 minutes.
- Expected output format: The `getHits` method should return the number of hits in the last 5 minutes.
- Key requirements and edge cases to consider: The class should be able to handle a large number of `hit` and `getHits` method calls, and it should return the correct number of hits in the last 5 minutes for each `getHits` method call.
- Example test cases with explanations:
  - `hit(1)`: Record a hit at timestamp 1.
  - `getHits(2)`: Return the number of hits in the last 5 minutes (i.e., from timestamp -4 to 2). Since there is only one hit at timestamp 1, the method should return 1.
  - `hit(2)`: Record a hit at timestamp 2.
  - `getHits(3)`: Return the number of hits in the last 5 minutes (i.e., from timestamp -2 to 3). Since there are two hits at timestamps 1 and 2, the method should return 2.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can store all the hits in a list and then iterate over the list to count the hits in the last 5 minutes for each `getHits` method call.
- Step-by-step breakdown of the solution:
  1. Create a list to store all the hits with their timestamps.
  2. For each `hit` method call, add the hit with its timestamp to the list.
  3. For each `getHits` method call, iterate over the list and count the hits with timestamps within the last 5 minutes.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it is not efficient for a large number of hits.

```cpp
class HitCounter {
public:
    vector<pair<int, int>> hits;

    HitCounter() {}

    void hit(int timestamp) {
        hits.push_back({timestamp, 1});
    }

    int getHits(int timestamp) {
        int count = 0;
        for (auto& hit : hits) {
            if (timestamp - hit.first < 300) {
                count += hit.second;
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of hits. This is because we iterate over all the hits for each `getHits` method call.
> - **Space Complexity:** $O(n)$, where $n$ is the number of hits. This is because we store all the hits in a list.
> - **Why these complexities occur:** The brute force approach has high time and space complexities because it involves iterating over all the hits for each `getHits` method call and storing all the hits in a list.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a queue to store the hits in the last 5 minutes. When a new hit is added, we can remove the hits that are older than 5 minutes from the queue.
- Detailed breakdown of the approach:
  1. Create a queue to store the hits with their timestamps.
  2. For each `hit` method call, add the hit with its timestamp to the queue and remove the hits that are older than 5 minutes from the queue.
  3. For each `getHits` method call, return the size of the queue.
- Proof of optimality: This approach is optimal because it only stores the hits in the last 5 minutes and removes the hits that are older than 5 minutes, reducing the space complexity to $O(1)$ and the time complexity to $O(1)$ for each method call.

```cpp
class HitCounter {
public:
    queue<int> q;

    HitCounter() {}

    void hit(int timestamp) {
        q.push(timestamp);
        while (!q.empty() && timestamp - q.front() >= 300) {
            q.pop();
        }
    }

    int getHits(int timestamp) {
        while (!q.empty() && timestamp - q.front() >= 300) {
            q.pop();
        }
        return q.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, where $n$ is the number of hits. This is because we only remove the hits that are older than 5 minutes from the queue for each method call.
> - **Space Complexity:** $O(1)$, where $n$ is the number of hits. This is because we only store the hits in the last 5 minutes in the queue.
> - **Optimality proof:** This approach is optimal because it only stores the hits in the last 5 minutes and removes the hits that are older than 5 minutes, reducing the space complexity to $O(1)$ and the time complexity to $O(1)$ for each method call.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a queue to store the hits in the last 5 minutes and removing the hits that are older than 5 minutes.
- Problem-solving patterns identified: Using a data structure to store the relevant data and removing the irrelevant data to reduce the space complexity.
- Optimization techniques learned: Using a queue to store the hits in the last 5 minutes and removing the hits that are older than 5 minutes to reduce the space complexity.
- Similar problems to practice: Designing a data structure to store the relevant data and removing the irrelevant data to reduce the space complexity.

**Mistakes to Avoid:**
- Common implementation errors: Not removing the hits that are older than 5 minutes from the queue.
- Edge cases to watch for: Handling the case where the queue is empty.
- Performance pitfalls: Not using a queue to store the hits in the last 5 minutes and removing the hits that are older than 5 minutes.
- Testing considerations: Testing the `hit` and `getHits` methods with different timestamps and edge cases.