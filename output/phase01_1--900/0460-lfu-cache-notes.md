## LFU Cache

**Problem Link:** [https://leetcode.com/problems/lfu-cache/description](https://leetcode.com/problems/lfu-cache/description)

**Problem Statement:**
- Design and implement a data structure for a Least Frequently Used (LFU) cache.
- The cache has a limited capacity, and when the cache is full and another key needs to be inserted, the key with the lowest frequency should be removed first. If there are multiple keys with the same lowest frequency, the least recently used key should be removed.
- Implement the `LFUCache` class:
  - `LFUCache(int capacity)`: Initializes the LFU cache with a given capacity.
  - `int get(int key)`: Returns the value of the key if the key exists in the cache. Otherwise, returns -1.
  - `void put(int key, int value)`: Sets or inserts the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item.

**Expected Output Format:**
- The `get` method should return the value associated with the key if it exists in the cache; otherwise, it should return -1.
- The `put` method should set or insert the value for the given key. If the cache is full, it should remove the least frequently used item before inserting the new item.

**Key Requirements and Edge Cases to Consider:**
- The cache has a limited capacity.
- The cache should remove the least frequently used key when it is full and a new key needs to be inserted.
- If there are multiple keys with the same lowest frequency, the least recently used key should be removed.
- The cache should handle `get` and `put` operations efficiently.

**Example Test Cases with Explanations:**
- `LFUCache cache = new LFUCache(2);` // capacity is 2
- `cache.put(1, 1);`
- `cache.put(2, 2);`
- `cache.get(1);` // returns 1
- `cache.put(3, 3);` // evicts key 2
- `cache.get(2);` // returns -1 (not found)
- `cache.get(3);` // returns 3
- `cache.put(4, 4);` // evicts key 1
- `cache.get(1);` // returns -1 (not found)
- `cache.get(3);` // returns 3
- `cache.get(4);` // returns 4

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to use a simple data structure like a `map` to store the key-value pairs and a separate data structure to keep track of the frequency of each key.
- However, this approach does not efficiently handle the removal of the least frequently used key when the cache is full.

```cpp
class LFUCache {
public:
    unordered_map<int, int> cache;
    unordered_map<int, int> freq;
    unordered_map<int, unordered_set<int>> freqToKeys;
    int capacity;
    int minFreq;

    LFUCache(int capacity) {
        this->capacity = capacity;
        minFreq = 0;
    }

    int get(int key) {
        if (cache.find(key) == cache.end()) {
            return -1;
        }
        int value = cache[key];
        freq[key]++;
        freqToKeys[freq[key] - 1].erase(key);
        if (freqToKeys[freq[key] - 1].empty()) {
            if (minFreq == freq[key] - 1) {
                minFreq = freq[key];
            }
        }
        freqToKeys[freq[key]].insert(key);
        return value;
    }

    void put(int key, int value) {
        if (capacity == 0) {
            return;
        }
        if (cache.find(key) != cache.end()) {
            cache[key] = value;
            get(key); // increase frequency
            return;
        }
        if (cache.size() == capacity) {
            // remove the least frequently used key
            int keyToRemove = *freqToKeys[minFreq].begin();
            cache.erase(keyToRemove);
            freq.erase(keyToRemove);
            freqToKeys[minFreq].erase(keyToRemove);
            if (freqToKeys[minFreq].empty()) {
                freqToKeys.erase(minFreq);
            }
        }
        cache[key] = value;
        freq[key] = 1;
        freqToKeys[1].insert(key);
        minFreq = 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for `get` and `put` operations on average, but $O(n)$ in the worst case when removing the least frequently used key.
> - **Space Complexity:** $O(n)$ for storing the key-value pairs, frequency of each key, and the mapping of frequency to keys.
> - **Why these complexities occur:** The brute force approach uses multiple data structures to keep track of the cache, frequency, and mapping of frequency to keys, resulting in a high space complexity. The time complexity is high in the worst case due to the removal of the least frequently used key.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach is to use a combination of a `map` to store the key-value pairs, a `map` to store the frequency of each key, and a `map` to store the keys for each frequency.
- We also use a `minFreq` variable to keep track of the minimum frequency.
- When the cache is full and a new key needs to be inserted, we remove the least frequently used key.

```cpp
class LFUCache {
public:
    unordered_map<int, pair<int, int>> cache;
    unordered_map<int, list<int>> freqToKeys;
    int capacity;
    int minFreq;

    LFUCache(int capacity) {
        this->capacity = capacity;
        minFreq = 0;
    }

    int get(int key) {
        if (cache.find(key) == cache.end()) {
            return -1;
        }
        int value = cache[key].first;
        int freq = cache[key].second;
        cache.erase(key);
        freqToKeys[freq].remove(key);
        if (freqToKeys[freq].empty() && minFreq == freq) {
            minFreq = freq + 1;
        }
        freqToKeys[freq + 1].push_back(key);
        cache[key] = {value, freq + 1};
        return value;
    }

    void put(int key, int value) {
        if (capacity == 0) {
            return;
        }
        if (cache.find(key) != cache.end()) {
            cache[key].first = value;
            get(key); // increase frequency
            return;
        }
        if (cache.size() == capacity) {
            int keyToRemove = freqToKeys[minFreq].front();
            cache.erase(keyToRemove);
            freqToKeys[minFreq].pop_front();
            if (freqToKeys[minFreq].empty()) {
                freqToKeys.erase(minFreq);
            }
        }
        freqToKeys[1].push_back(key);
        cache[key] = {value, 1};
        minFreq = 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for `get` and `put` operations on average.
> - **Space Complexity:** $O(n)$ for storing the key-value pairs, frequency of each key, and the mapping of frequency to keys.
> - **Optimality proof:** The optimal approach uses a combination of data structures to efficiently handle the cache, frequency, and mapping of frequency to keys, resulting in a low time complexity.

---

### Final Notes

**Learning Points:**
- The importance of using a combination of data structures to efficiently handle the cache, frequency, and mapping of frequency to keys.
- The need to keep track of the minimum frequency to efficiently remove the least frequently used key.
- The use of a `map` to store the key-value pairs and a `map` to store the frequency of each key.

**Mistakes to Avoid:**
- Not using a combination of data structures to efficiently handle the cache, frequency, and mapping of frequency to keys.
- Not keeping track of the minimum frequency to efficiently remove the least frequently used key.
- Not using a `map` to store the key-value pairs and a `map` to store the frequency of each key.