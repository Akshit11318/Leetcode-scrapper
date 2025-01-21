## Snapshot Array

**Problem Link:** https://leetcode.com/problems/snapshot-array/description

**Problem Statement:**
- Input format and constraints: The problem asks to implement a `SnapshotArray` class that supports two operations: `set(index, val)` which sets the value at a given index and `snap()` which creates a snapshot of the current state of the array, returning a unique id for the snapshot. The `get(index, snap_id)` operation retrieves the value at a given index in a specific snapshot.
- Expected output format: The output should be the value at the specified index in the specified snapshot.
- Key requirements and edge cases to consider: 
    - Multiple `set` operations before taking a snapshot.
    - Multiple `snap` operations.
    - `get` operations after multiple `snap` operations.
- Example test cases with explanations:
    - `SnapshotArray(3)` creates an array of length 3.
    - `set(0, 5)` sets the value at index 0 to 5.
    - `snap()` takes a snapshot and returns a unique id, e.g., 0.
    - `get(0, 0)` retrieves the value at index 0 in the snapshot with id 0.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create an array to store the current values and a list of snapshots, where each snapshot is a copy of the current array at the time of the snapshot.
- Step-by-step breakdown of the solution:
    1. Initialize an array of size `length` to store the current values.
    2. Create a list to store the snapshots.
    3. In the `set` operation, update the value at the given index in the current array.
    4. In the `snap` operation, create a copy of the current array and add it to the list of snapshots.
    5. In the `get` operation, retrieve the value at the given index from the snapshot with the specified id.
- Why this approach comes to mind first: It directly implements the required operations without considering optimization.

```cpp
class SnapshotArray {
public:
    vector<vector<int>> snapshots;
    vector<int> current;
    int id = 0;

    SnapshotArray(int length) {
        current.resize(length, 0);
    }

    void set(int index, int val) {
        current[index] = val;
    }

    int snap() {
        snapshots.push_back(current);
        return id++;
    }

    int get(int index, int snap_id) {
        return snapshots[snap_id][index];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for `set`, $O(n)$ for `snap` where $n$ is the length of the array, and $O(1)$ for `get`.
> - **Space Complexity:** $O(n \cdot s)$ where $n$ is the length of the array and $s$ is the number of snapshots.
> - **Why these complexities occur:** The `snap` operation requires copying the entire array, leading to a linear time complexity. The space complexity is due to storing all snapshots.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of storing entire snapshots, we can store the changes (index, value, snapshot_id) in a map for each index. This way, we only store the differences between snapshots.
- Detailed breakdown of the approach:
    1. Use a map to store the values for each index, where the key is the snapshot id and the value is the value at that index in the snapshot.
    2. In the `set` operation, update the value for the current index in the map with the current snapshot id.
    3. In the `snap` operation, increment the snapshot id.
    4. In the `get` operation, find the most recent value for the given index that is less than or equal to the given snapshot id.
- Why further optimization is impossible: This approach minimizes the amount of data stored while still allowing for efficient retrieval of values from any snapshot.

```cpp
class SnapshotArray {
public:
    vector<map<int, int>> data;
    int id = 0;

    SnapshotArray(int length) {
        data.resize(length);
    }

    void set(int index, int val) {
        data[index][id] = val;
    }

    int snap() {
        id++;
        return id - 1;
    }

    int get(int index, int snap_id) {
        auto it = data[index].upper_bound(snap_id);
        if (it != data[index].begin()) {
            --it;
            if (it->first <= snap_id) {
                return it->second;
            }
        }
        return 0;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for `set`, $O(1)$ for `snap`, and $O(log s)$ for `get` where $s$ is the number of snapshots.
> - **Space Complexity:** $O(n \cdot s)$ in the worst case, but typically much less since we only store changes.
> - **Optimality proof:** This approach minimizes storage while maintaining efficient query times, making it optimal for the given operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using maps to store changes and efficient lookup in maps.
- Problem-solving patterns identified: Minimizing storage by only storing differences.
- Optimization techniques learned: Reducing the amount of data stored while maintaining query efficiency.
- Similar problems to practice: Other problems involving version control or snapshotting data.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling the upper bound in the map.
- Edge cases to watch for: Handling the case where the given snapshot id is not found.
- Performance pitfalls: Storing unnecessary data, leading to increased space complexity.
- Testing considerations: Thoroughly testing the `get` operation with different snapshot ids and indices.