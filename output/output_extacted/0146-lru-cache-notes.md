## LRU Cache
**Problem Link:** [https://leetcode.com/problems/lru-cache/description](https://leetcode.com/problems/lru-cache/description)

**Problem Statement:**
- Input format and constraints: The problem requires designing a data structure that follows the LRU (Least Recently Used) eviction policy. The cache is initialized with a given capacity. The operations that can be performed on the cache are `get(key)` and `put(key, value)`.
- Expected output format: For the `get(key)` operation, the value associated with the key should be returned if the key exists in the cache. Otherwise, -1 should be returned. For the `put(key, value)` operation, the key-value pair should be inserted or updated in the cache. If the key already exists, the value should be updated. If the key does not exist and the cache has reached its capacity, the least recently used item should be evicted.
- Key requirements and edge cases to consider: The cache should be able to handle a large number of `get` and `put` operations. The `get` operation should return the value associated with the key if it exists in the cache. The `put` operation should insert or update the key-value pair in the cache and evict the least recently used item if the cache has reached its capacity.
- Example test cases with explanations:
    - `LRUCache cache = new LRUCache(2);` 
    - `cache.put(1, 1);` 
    - `cache.put(2, 2);` 
    - `cache.get(1);` 
    - `cache.put(3, 3);` 
    - `cache.get(2);` 

---

### Brute Force Approach

**Explanation:**
- Initial thought process: A simple approach would be to use a vector to store the key-value pairs and a map to store the indices of the keys in the vector. For the `get(key)` operation, we can use the map to find the index of the key in the vector and return the corresponding value. For the `put(key, value)` operation, we can use the map to check if the key already exists in the vector. If it does, we can update the value at the corresponding index. If it does not, we can insert the key-value pair at the end of the vector. However, this approach does not follow the LRU eviction policy.
- Step-by-step breakdown of the solution:
    1. Create a vector to store the key-value pairs.
    2. Create a map to store the indices of the keys in the vector.
    3. For the `get(key)` operation:
        - Use the map to find the index of the key in the vector.
        - Return the value at the corresponding index in the vector.
    4. For the `put(key, value)` operation:
        - Use the map to check if the key already exists in the vector.
        - If it does, update the value at the corresponding index.
        - If it does not, insert the key-value pair at the end of the vector.

```cpp
class LRUCache {
public:
    LRUCache(int capacity) {
        cap = capacity;
    }
    
    int get(int key) {
        if (cache.find(key) != cache.end()) {
            int value = cache[key];
            cache.erase(key);
            cache[key] = value;
            return value;
        }
        return -1;
    }
    
    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            cache.erase(key);
        } else if (cache.size() == cap) {
            cache.erase(cache.begin());
        }
        cache[key] = value;
    }
private:
    int cap;
    std::map<int, int> cache;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where n is the number of elements in the cache. This is because in the worst-case scenario, we need to traverse the entire cache to find the key.
> - **Space Complexity:** $O(n)$, where n is the number of elements in the cache. This is because we need to store all the key-value pairs in the cache.
> - **Why these complexities occur:** These complexities occur because we are using a map to store the key-value pairs, which allows for fast lookup and insertion operations. However, the map does not follow the LRU eviction policy.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a combination of a doubly linked list and a map to implement the LRU cache. The doubly linked list will allow us to efficiently add and remove elements from the cache, while the map will allow us to quickly look up the keys.
- Detailed breakdown of the approach:
    1. Create a doubly linked list to store the key-value pairs.
    2. Create a map to store the pointers to the nodes in the linked list.
    3. For the `get(key)` operation:
        - Use the map to find the node corresponding to the key.
        - If the node exists, move it to the front of the linked list and return the value.
    4. For the `put(key, value)` operation:
        - Use the map to check if the key already exists in the linked list.
        - If it does, update the value and move the node to the front of the linked list.
        - If it does not, create a new node and add it to the front of the linked list. If the cache has reached its capacity, remove the last node from the linked list.

```cpp
class Node {
public:
    int key, value;
    Node* prev, *next;
    Node(int k, int v) : key(k), value(v), prev(nullptr), next(nullptr) {}
};

class LRUCache {
public:
    LRUCache(int capacity) {
        cap = capacity;
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if (cache.find(key) != cache.end()) {
            Node* node = cache[key];
            remove(node);
            add(node);
            return node->value;
        }
        return -1;
    }
    
    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            remove(cache[key]);
        }
        Node* node = new Node(key, value);
        add(node);
        cache[key] = node;
        if (cache.size() > cap) {
            Node* node = tail->prev;
            remove(node);
            cache.erase(node->key);
            delete node;
        }
    }
private:
    int cap;
    Node* head, *tail;
    std::unordered_map<int, Node*> cache;
    
    void remove(Node* node) {
        Node* prev = node->prev;
        Node* next = node->next;
        prev->next = next;
        next->prev = prev;
    }
    
    void add(Node* node) {
        Node* prev = head;
        Node* next = head->next;
        prev->next = node;
        next->prev = node;
        node->prev = prev;
        node->next = next;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, where n is the number of elements in the cache. This is because we can use the map to quickly look up the keys and the linked list to efficiently add and remove elements.
> - **Space Complexity:** $O(n)$, where n is the number of elements in the cache. This is because we need to store all the key-value pairs in the cache.
> - **Optimality proof:** This is the optimal solution because we are using a combination of a doubly linked list and a map to implement the LRU cache, which allows for efficient lookup, insertion, and removal operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The use of a doubly linked list and a map to implement the LRU cache.
- Problem-solving patterns identified: The use of a combination of data structures to solve a complex problem.
- Optimization techniques learned: The use of a doubly linked list to efficiently add and remove elements, and the use of a map to quickly look up the keys.
- Similar problems to practice: Other problems that involve implementing a cache or a queue, such as the "Implement Queue using Stacks" problem.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the edge cases correctly, such as when the cache is empty or when the key is not found.
- Edge cases to watch for: The cache reaching its capacity, and the key not being found in the cache.
- Performance pitfalls: Not using the most efficient data structures and algorithms, such as using a vector instead of a linked list.
- Testing considerations: Testing the cache with different scenarios, such as adding and removing elements, and checking that the cache is working correctly.