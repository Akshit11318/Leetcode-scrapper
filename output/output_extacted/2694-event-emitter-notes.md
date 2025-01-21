## Event Emitter

**Problem Link:** https://leetcode.com/problems/event-emitter/description

**Problem Statement:**
- The problem requires designing an `EventEmitter` class that allows registering and triggering events.
- The class should have methods to `addEventListener` for a specific event type and to `emit` an event.
- The input format includes the event type and the listener function to be registered or the event type and arguments to be emitted.
- The expected output format is not explicitly defined, but the goal is to ensure that the registered listeners are called when an event is emitted.
- Key requirements include handling multiple event types, registering multiple listeners for the same event type, and passing arguments to the listeners when an event is emitted.
- Edge cases to consider include handling duplicate registrations, removing listeners, and emitting events with varying numbers of arguments.
- Example test cases include registering listeners for specific events and verifying that they are called when those events are emitted.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves creating a data structure to store event types and their corresponding listeners.
- A straightforward approach is to use a `map` where the keys are event types and the values are lists of listener functions.
- When `addEventListener` is called, the listener is added to the list of the corresponding event type.
- When `emit` is called, all listeners registered for the specified event type are called with the provided arguments.

```cpp
class EventEmitter {
public:
    void addEventListener(string eventType, function<void(vector<int>)> listener) {
        if (listeners.find(eventType) == listeners.end()) {
            listeners[eventType] = {};
        }
        listeners[eventType].push_back(listener);
    }

    void emit(string eventType, vector<int> args) {
        if (listeners.find(eventType) != listeners.end()) {
            for (auto listener : listeners[eventType]) {
                listener(args);
            }
        }
    }

private:
    unordered_map<string, vector<function<void(vector<int>)>>> listeners;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for both `addEventListener` and `emit`, where $n$ is the number of listeners for an event type. The `addEventListener` method has a constant time complexity for inserting into the map and appending to the vector, but in the worst case, it could be $O(n)$ if hash collisions occur. The `emit` method iterates over all listeners for an event type, resulting in a linear time complexity.
> - **Space Complexity:** $O(n)$, where $n$ is the total number of listeners across all event types. This is because each listener is stored in memory.
> - **Why these complexities occur:** The time complexity is primarily due to the iteration over listeners in the `emit` method, while the space complexity is due to storing all registered listeners.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight to the optimal solution is recognizing that the brute force approach is already quite efficient, given the requirements of the problem.
- However, to further optimize, we can ensure that the `map` operations are as efficient as possible by using `unordered_map` and minimizing the number of times we access or modify the map.
- Additionally, we can consider using a more efficient data structure for storing listeners, but given the constraints of the problem, a vector of listeners per event type is straightforward and efficient.

```cpp
class EventEmitter {
public:
    void addEventListener(string eventType, function<void(vector<int>)> listener) {
        listeners[eventType].emplace_back(listener);
    }

    void emit(string eventType, vector<int> args) {
        if (listeners.count(eventType)) {
            for (auto& listener : listeners[eventType]) {
                listener(args);
            }
        }
    }

private:
    unordered_map<string, vector<function<void(vector<int>)>>> listeners;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for `addEventListener` on average, assuming the hash function is well-distributed, and $O(n)$ for `emit`, where $n$ is the number of listeners for the event type.
> - **Space Complexity:** $O(n)$, where $n$ is the total number of listeners across all event types.
> - **Optimality proof:** This solution is optimal because it uses the most efficient data structures available in C++ for the task. The `unordered_map` provides constant time complexity for insertion and lookup on average, and the vector of listeners allows for efficient iteration. Further optimizations would require changing the problem's constraints or using more complex data structures that might not provide significant benefits for this specific use case.

---

### Final Notes

**Learning Points:**
- The importance of choosing the right data structures for the problem at hand.
- Understanding the trade-offs between time and space complexity.
- Recognizing when a brute force approach might already be close to optimal.

**Mistakes to Avoid:**
- Not considering the average case time complexity of hash-based data structures.
- Failing to minimize the number of operations on the data structure.
- Not accounting for edge cases such as duplicate registrations or removing listeners.