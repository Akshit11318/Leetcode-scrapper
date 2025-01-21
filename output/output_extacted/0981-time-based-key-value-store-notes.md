## Time Based Key-Value Store
**Problem Link:** https://leetcode.com/problems/time-based-key-value-store/description

**Problem Statement:**
- Input format and constraints: The problem involves a `TimeKey` class with `set` and `get` methods. The `set` method takes a key, a value, and a timestamp as input, while the `get` method takes a key and a timestamp as input. The constraints specify that the `set` method should store the value with the given key at the given timestamp, and the `get` method should return the value associated with the given key at or before the given timestamp.
- Expected output format: The `get` method should return the value associated with the given key at or before the given timestamp. If no such value exists, it should return an empty string.
- Key requirements and edge cases to consider:
  - The `set` method should store the value with the given key at the given timestamp.
  - The `get` method should return the value associated with the given key at or before the given timestamp.
  - If no such value exists, the `get` method should return an empty string.
- Example test cases with explanations:
  - `TimeKey timeKey = new TimeKey(); timeKey.set("foo", "bar", 1); timeKey.get("foo", 1); // returns "bar"`
  - `timeKey.get("foo", 3); // returns "bar" because "bar" is the value associated with "foo" at or before timestamp 3`
  - `timeKey.set("foo", "bar2", 4); timeKey.get("foo", 3); // returns "bar" because "bar" is the value associated with "foo" at or before timestamp 3`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can use a map to store the values for each key at different timestamps. The map can be a dictionary where the key is the actual key from the problem, and the value is another dictionary that maps timestamps to values.
- Step-by-step breakdown of the solution:
  1. Create a map to store the values for each key at different timestamps.
  2. In the `set` method, store the value with the given key at the given timestamp in the map.
  3. In the `get` method, find the most recent timestamp that is less than or equal to the given timestamp for the given key. If such a timestamp exists, return the value associated with it; otherwise, return an empty string.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, as it directly addresses the requirements of the problem.

```cpp
class TimeKey {
public:
    map<string, map<int, string>> store;

    void set(string key, string value, int timestamp) {
        store[key][timestamp] = value;
    }

    string get(string key, int timestamp) {
        if (store.find(key) == store.end()) return "";
        auto it = store[key].upper_bound(timestamp);
        if (it == store[key].begin()) return "";
        it--;
        return it->second;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(log n)$ for the `get` method, where $n$ is the number of timestamps for a given key. This is because we use the `upper_bound` method to find the most recent timestamp that is less than or equal to the given timestamp.
> - **Space Complexity:** $O(n)$, where $n$ is the total number of key-timestamp pairs. This is because we store all the key-timestamp pairs in the map.
> - **Why these complexities occur:** The time complexity occurs because we use a map to store the timestamps for each key, and the `upper_bound` method has a time complexity of $O(log n)$. The space complexity occurs because we store all the key-timestamp pairs in the map.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach, as it is already efficient and easy to implement.
- Detailed breakdown of the approach: The approach is the same as the brute force approach.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(log n)$ for the `get` method, which is the best we can achieve using a map to store the timestamps for each key.
- Why further optimization is impossible: Further optimization is impossible because we are already using the most efficient data structure (a map) to store the timestamps for each key, and we are using the most efficient method (the `upper_bound` method) to find the most recent timestamp that is less than or equal to the given timestamp.

```cpp
class TimeKey {
public:
    map<string, map<int, string>> store;

    void set(string key, string value, int timestamp) {
        store[key][timestamp] = value;
    }

    string get(string key, int timestamp) {
        if (store.find(key) == store.end()) return "";
        auto it = store[key].upper_bound(timestamp);
        if (it == store[key].begin()) return "";
        it--;
        return it->second;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(log n)$ for the `get` method, where $n$ is the number of timestamps for a given key.
> - **Space Complexity:** $O(n)$, where $n$ is the total number of key-timestamp pairs.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(log n)$ for the `get` method, which is the best we can achieve using a map to store the timestamps for each key.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a map to store timestamps for each key, and using the `upper_bound` method to find the most recent timestamp that is less than or equal to the given timestamp.
- Problem-solving patterns identified: Using a map to store key-value pairs, and using the `upper_bound` method to find the most recent timestamp that is less than or equal to the given timestamp.
- Optimization techniques learned: Using the most efficient data structure (a map) to store the timestamps for each key, and using the most efficient method (the `upper_bound` method) to find the most recent timestamp that is less than or equal to the given timestamp.
- Similar problems to practice: Problems that involve using a map to store key-value pairs, and using the `upper_bound` method to find the most recent timestamp that is less than or equal to the given timestamp.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the key exists in the map before trying to access its value, and not checking if the timestamp exists in the map before trying to access its value.
- Edge cases to watch for: When the key does not exist in the map, and when the timestamp does not exist in the map.
- Performance pitfalls: Using a data structure that is not efficient for storing key-value pairs, and using a method that is not efficient for finding the most recent timestamp that is less than or equal to the given timestamp.
- Testing considerations: Testing the `set` and `get` methods with different inputs, including edge cases, to ensure that they work correctly.