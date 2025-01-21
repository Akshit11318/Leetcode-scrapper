## Time Limit Cache
**Problem Link:** https://leetcode.com/problems/cache-with-time-limit/description

**Problem Statement:**
- Input format: The input will be a series of operations to perform on the cache.
- Constraints: The cache has a fixed size and a time limit.
- Expected output format: The output should reflect the state of the cache after each operation.
- Key requirements and edge cases to consider: The cache should have a limited size and a time limit for each key. When the cache reaches its size limit, the least recently used (LRU) key should be removed. If a key is not accessed within the time limit, it should be removed.
- Example test cases with explanations:
  - `Cache cache = new Cache(2, 1); cache.put(1, 1); cache.get(1); cache.put(2, 2); cache.get(1); cache.get(3); cache.put(3, 3); cache.get(2); cache.get(3); cache.put(4, 4);`
  - This test case demonstrates the LRU eviction policy and the time limit for each key.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Use a simple data structure like a map to store the cache keys and values, and a separate data structure to keep track of the time limit for each key.
- Step-by-step breakdown of the solution:
  1. Create a map to store the cache keys and values.
  2. Create a separate map to store the time limit for each key.
  3. When a key is accessed, update its time limit.
  4. When the cache reaches its size limit, remove the least recently used key.
- Why this approach comes to mind first: It is a straightforward solution that uses existing data structures.

```cpp
class Cache {
public:
    int capacity, timeLimit;
    unordered_map<int, int> cache;
    unordered_map<int, int> time;
    unordered_map<int, int> order;

    Cache(int capacity, int timeLimit) {
        this->capacity = capacity;
        this->timeLimit = timeLimit;
    }

    int get(int key) {
        if (cache.find(key) == cache.end()) return -1;
        if (time[key] + timeLimit < clock()) {
            cache.erase(key);
            time.erase(key);
            order.erase(key);
            return -1;
        }
        order.erase(key);
        order[key] = clock();
        return cache[key];
    }

    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            cache[key] = value;
            order.erase(key);
            order[key] = clock();
            time[key] = clock();
        } else {
            if (cache.size() == capacity) {
                int lruKey = -1;
                for (auto& pair : order) {
                    if (lruKey == -1 || pair.second < order[lruKey]) {
                        lruKey = pair.first;
                    }
                }
                cache.erase(lruKey);
                time.erase(lruKey);
                order.erase(lruKey);
            }
            cache[key] = value;
            order[key] = clock();
            time[key] = clock();
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of keys in the cache. This is because we are using a map to store the cache keys and values, and a separate map to keep track of the time limit for each key. The `get` and `put` operations have a time complexity of $O(1)$ on average, but in the worst case, we need to iterate over all the keys in the cache to find the least recently used key.
> - **Space Complexity:** $O(n)$, where $n$ is the number of keys in the cache. This is because we are using two maps to store the cache keys and values, and the time limit for each key.
> - **Why these complexities occur:** The time complexity occurs because we are using a map to store the cache keys and values, and a separate map to keep track of the time limit for each key. The space complexity occurs because we are using two maps to store the cache keys and values, and the time limit for each key.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a combination of a map and a doubly linked list to store the cache keys and values. The map can be used to store the cache keys and values, and the doubly linked list can be used to keep track of the order of the keys.
- Detailed breakdown of the approach:
  1. Create a map to store the cache keys and values.
  2. Create a doubly linked list to keep track of the order of the keys.
  3. When a key is accessed, update its position in the doubly linked list.
  4. When the cache reaches its size limit, remove the least recently used key.
- Proof of optimality: This approach has a time complexity of $O(1)$ for both the `get` and `put` operations, making it optimal.

```cpp
class Node {
public:
    int key, value;
    Node* prev, *next;
    Node(int key, int value) {
        this->key = key;
        this->value = value;
    }
};

class Cache {
public:
    int capacity, timeLimit;
    unordered_map<int, Node*> cache;
    Node* head, *tail;
    unordered_map<int, int> time;

    Cache(int capacity, int timeLimit) {
        this->capacity = capacity;
        this->timeLimit = timeLimit;
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head->next = tail;
        tail->prev = head;
    }

    int get(int key) {
        if (cache.find(key) == cache.end()) return -1;
        if (time[key] + timeLimit < clock()) {
            removeNode(cache[key]);
            cache.erase(key);
            time.erase(key);
            return -1;
        }
        Node* node = cache[key];
        removeNode(node);
        addNode(node);
        time[key] = clock();
        return node->value;
    }

    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            removeNode(cache[key]);
        }
        if (cache.size() == capacity) {
            Node* node = head->next;
            removeNode(node);
            cache.erase(node->key);
            time.erase(node->key);
        }
        Node* node = new Node(key, value);
        addNode(node);
        cache[key] = node;
        time[key] = clock();
    }

    void removeNode(Node* node) {
        Node* prev = node->prev;
        Node* next = node->next;
        prev->next = next;
        next->prev = prev;
    }

    void addNode(Node* node) {
        Node* prev = tail->prev;
        prev->next = node;
        tail->prev = node;
        node->prev = prev;
        node->next = tail;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, where $n$ is the number of keys in the cache. This is because we are using a map to store the cache keys and values, and a doubly linked list to keep track of the order of the keys.
> - **Space Complexity:** $O(n)$, where $n$ is the number of keys in the cache. This is because we are using a map to store the cache keys and values, and a doubly linked list to keep track of the order of the keys.
> - **Optimality proof:** This approach has a time complexity of $O(1)$ for both the `get` and `put` operations, making it optimal.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The use of a combination of a map and a doubly linked list to store the cache keys and values.
- Problem-solving patterns identified: The use of a map to store the cache keys and values, and a doubly linked list to keep track of the order of the keys.
- Optimization techniques learned: The use of a doubly linked list to keep track of the order of the keys, and the removal of the least recently used key when the cache reaches its size limit.
- Similar problems to practice: Other problems that involve the use of a cache, such as the LRU cache problem.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the position of the key in the doubly linked list when it is accessed.
- Edge cases to watch for: The case where the cache is empty, and the case where the cache is full.
- Performance pitfalls: Not using a doubly linked list to keep track of the order of the keys, which can result in a time complexity of $O(n)$ for the `get` and `put` operations.
- Testing considerations: Testing the cache with different inputs and edge cases to ensure that it is working correctly.