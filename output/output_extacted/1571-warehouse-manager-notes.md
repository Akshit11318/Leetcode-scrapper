## Warehouse Manager
**Problem Link:** https://leetcode.com/problems/warehouse-manager/description

**Problem Statement:**
- The problem requires designing a `WarehouseManager` class that manages the inventory of a warehouse. The class should support two operations: `receiveBarcodes` and `shipOrder`.
- `receiveBarcodes` takes a list of barcodes of items to be received into the warehouse.
- `shipOrder` takes a list of barcodes of items to be shipped out of the warehouse.
- The goal is to ensure that the warehouse manager can efficiently receive and ship items based on their barcodes.
- Key requirements include handling cases where an item is received or shipped multiple times and ensuring that the inventory remains accurate.
- Example test cases include receiving and shipping the same item multiple times, receiving an item that is already in the warehouse, and shipping an item that has not been received.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves using a data structure to store the inventory of the warehouse.
- A simple approach is to use a `std::vector` or `std::list` to store the received barcodes and then iterate through this list whenever an item needs to be shipped.
- This approach comes to mind first because it directly addresses the requirement of receiving and shipping items based on their barcodes.

```cpp
class WarehouseManager {
public:
    void receiveBarcodes(vector<int> barcodes) {
        for (int barcode : barcodes) {
            receivedBarcodes.push_back(barcode);
        }
    }

    int shipOrder(vector<int> barcodes) {
        int shipped = 0;
        for (int barcode : barcodes) {
            for (auto it = receivedBarcodes.begin(); it != receivedBarcodes.end(); ++it) {
                if (*it == barcode) {
                    receivedBarcodes.erase(it);
                    shipped++;
                    break;
                }
            }
        }
        return shipped;
    }

private:
    vector<int> receivedBarcodes;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of received barcodes and $m$ is the number of barcodes to be shipped. This is because in the worst case, for each item to be shipped, we might have to iterate through all received items.
> - **Space Complexity:** $O(n)$ where $n$ is the total number of received barcodes. This is because we store all received barcodes in the `receivedBarcodes` vector.
> - **Why these complexities occur:** These complexities occur because the brute force approach involves linear search and deletion in the vector, which can be inefficient for large numbers of items.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight for the optimal solution is to use a data structure that allows for efficient insertion, deletion, and lookup of barcodes.
- A `std::unordered_map` can be used to store the count of each barcode received, allowing for constant time operations.
- This approach is optimal because it minimizes the time complexity for both receiving and shipping items.

```cpp
class WarehouseManager {
public:
    void receiveBarcodes(vector<int> barcodes) {
        for (int barcode : barcodes) {
            if (inventory.find(barcode) != inventory.end()) {
                inventory[barcode]++;
            } else {
                inventory[barcode] = 1;
            }
        }
    }

    int shipOrder(vector<int> barcodes) {
        int shipped = 0;
        for (int barcode : barcodes) {
            if (inventory.find(barcode) != inventory.end() && inventory[barcode] > 0) {
                inventory[barcode]--;
                shipped++;
            }
        }
        return shipped;
    }

private:
    unordered_map<int, int> inventory;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of received barcodes and $m$ is the number of barcodes to be shipped. This is because both receiving and shipping operations can be performed in constant time using the unordered map.
> - **Space Complexity:** $O(n)$ where $n$ is the number of unique received barcodes. This is because we store the count of each unique barcode in the `inventory` map.
> - **Optimality proof:** This approach is optimal because it achieves the best possible time complexity for both receiving and shipping items, utilizing the efficient lookup and update capabilities of the unordered map.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated include the use of appropriate data structures for efficient operations and the importance of considering time and space complexity.
- Problem-solving patterns identified include recognizing when to use a specific data structure to optimize operations.
- Optimization techniques learned include choosing the right data structure for the problem and minimizing unnecessary operations.

**Mistakes to Avoid:**
- Common implementation errors include not handling edge cases properly (e.g., shipping an item that has not been received) and not validating inputs.
- Performance pitfalls include using inefficient data structures or algorithms for the problem at hand.
- Testing considerations include ensuring that all possible scenarios are covered, including receiving and shipping the same item multiple times and handling cases where an item is received or shipped but not the other.