## All Oone Data Structure

**Problem Link:** https://leetcode.com/problems/all-oone-data-structure/description

**Problem Statement:**
- Input format and constraints: The problem requires designing a data structure to support the following operations:
  - `inc(key)`: Increments the count of the given key by 1.
  - `dec(key)`: Decrements the count of the given key by 1.
  - `getMaxKey()`: Returns one of the keys with the maximum count.
  - `getMinKey()`: Returns one of the keys with the minimum count.
- Expected output format: The return values of `getMaxKey()` and `getMinKey()` should be one of the keys with the maximum and minimum count respectively.
- Key requirements and edge cases to consider:
  - Handling empty data structure.
  - Handling keys with zero count.
- Example test cases with explanations:
  - `inc(1)`, `inc(1)`, `inc(2)`, `dec(1)`, `getMaxKey()`, `getMinKey()`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One might think to use a simple hash map to store the count of each key and then iterate over the map to find the maximum and minimum count keys.
- Step-by-step breakdown of the solution:
  1. Create a hash map to store the count of each key.
  2. Implement `inc(key)` by incrementing the count of the given key in the hash map.
  3. Implement `dec(key)` by decrementing the count of the given key in the hash map.
  4. Implement `getMaxKey()` by iterating over the hash map and finding the key with the maximum count.
  5. Implement `getMinKey()` by iterating over the hash map and finding the key with the minimum count.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it has a high time complexity for `getMaxKey()` and `getMinKey()` operations.

```cpp
class AllOne {
public:
    unordered_map<string, int> count;
    int min_count = INT_MAX;
    int max_count = INT_MIN;

    void inc(string key) {
        if (count.find(key) == count.end()) {
            count[key] = 1;
        } else {
            count[key]++;
        }
        max_count = max(max_count, count[key]);
    }

    void dec(string key) {
        if (count.find(key) != count.end()) {
            count[key]--;
            if (count[key] == 0) {
                count.erase(key);
            }
            if (count[key] < min_count) {
                min_count = INT_MAX;
                for (auto& pair : count) {
                    if (pair.second < min_count) {
                        min_count = pair.second;
                    }
                }
            }
            if (count[key] < max_count && count.size() == 0) {
                max_count = INT_MIN;
            }
        }
    }

    string getMaxKey() {
        if (count.size() == 0) return "";
        string max_key = "";
        for (auto& pair : count) {
            if (pair.second == max_count) {
                return pair.first;
            }
        }
        return max_key;
    }

    string getMinKey() {
        if (count.size() == 0) return "";
        string min_key = "";
        for (auto& pair : count) {
            if (pair.second == min_count) {
                return pair.first;
            }
        }
        return min_key;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for `inc`, `dec`, `getMaxKey`, and `getMinKey` operations, where $n$ is the number of keys in the data structure.
> - **Space Complexity:** $O(n)$ for storing the count of each key.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the iteration over the hash map in `getMaxKey()` and `getMinKey()` operations.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using a combination of a hash map and two doubly linked lists to store the keys with the same count.
- Detailed breakdown of the approach:
  1. Create a hash map to store the count of each key.
  2. Create two doubly linked lists, one for the keys with the maximum count and one for the keys with the minimum count.
  3. Implement `inc(key)` by incrementing the count of the given key in the hash map and updating the linked lists.
  4. Implement `dec(key)` by decrementing the count of the given key in the hash map and updating the linked lists.
  5. Implement `getMaxKey()` by returning the key at the head of the maximum count linked list.
  6. Implement `getMinKey()` by returning the key at the head of the minimum count linked list.
- Proof of optimality: The optimal approach has a time complexity of $O(1)$ for `inc`, `dec`, `getMaxKey`, and `getMinKey` operations.

```cpp
class AllOne {
public:
    unordered_map<string, int> count;
    unordered_map<int, list<string>> count_to_keys;
    int min_count = 1;
    int max_count = 1;

    void inc(string key) {
        if (count.find(key) == count.end()) {
            count[key] = 1;
            count_to_keys[1].push_back(key);
        } else {
            int old_count = count[key];
            count_to_keys[old_count].remove(key);
            if (count_to_keys[old_count].size() == 0) {
                count_to_keys.erase(old_count);
                if (old_count == min_count) {
                    min_count++;
                }
            }
            count[key]++;
            if (count_to_keys.find(count[key]) == count_to_keys.end()) {
                count_to_keys[count[key]] = list<string>();
            }
            count_to_keys[count[key]].push_back(key);
            if (count[key] > max_count) {
                max_count = count[key];
            }
        }
    }

    void dec(string key) {
        if (count.find(key) != count.end()) {
            int old_count = count[key];
            count_to_keys[old_count].remove(key);
            if (count_to_keys[old_count].size() == 0) {
                count_to_keys.erase(old_count);
                if (old_count == max_count) {
                    max_count--;
                }
            }
            count[key]--;
            if (count[key] > 0) {
                if (count_to_keys.find(count[key]) == count_to_keys.end()) {
                    count_to_keys[count[key]] = list<string>();
                }
                count_to_keys[count[key]].push_back(key);
                if (count[key] < min_count) {
                    min_count = count[key];
                }
            } else {
                count.erase(key);
            }
        }
    }

    string getMaxKey() {
        if (count_to_keys.find(max_count) != count_to_keys.end()) {
            return count_to_keys[max_count].front();
        }
        return "";
    }

    string getMinKey() {
        if (count_to_keys.find(min_count) != count_to_keys.end()) {
            return count_to_keys[min_count].front();
        }
        return "";
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for `inc`, `dec`, `getMaxKey`, and `getMinKey` operations.
> - **Space Complexity:** $O(n)$ for storing the count of each key and the linked lists.
> - **Optimality proof:** The optimal approach has a time complexity of $O(1)$ due to the use of hash maps and linked lists.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash maps, doubly linked lists, and their applications in data structures.
- Problem-solving patterns identified: Using a combination of data structures to achieve optimal time complexity.
- Optimization techniques learned: Using linked lists to store keys with the same count and updating them efficiently.
- Similar problems to practice: Implementing a data structure to support `inc`, `dec`, `getMaxKey`, and `getMinKey` operations with optimal time complexity.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the linked lists correctly, not handling edge cases properly.
- Edge cases to watch for: Handling empty data structure, handling keys with zero count.
- Performance pitfalls: Using a single data structure that leads to high time complexity.
- Testing considerations: Testing with different input scenarios, testing edge cases.