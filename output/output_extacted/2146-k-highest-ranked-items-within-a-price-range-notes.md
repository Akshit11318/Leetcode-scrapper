## K-Highest Ranked Items Within a Price Range
**Problem Link:** https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/description

**Problem Statement:**
- Input format: 
  - `grid`: a 2D array of integers representing the prices of items at different stores.
  - `price`: an array of integers representing the price range.
  - `start`: an array of integers representing the starting coordinates.
  - `k`: an integer representing the number of items to return.
- Expected output format: 
  - A list of arrays, where each array contains the store index, item index, and price of an item.
- Key requirements and edge cases to consider:
  - All items in the grid have a price within the given range.
  - The start coordinates are within the bounds of the grid.
  - The grid can be empty.
  - The price range can be empty.
- Example test cases with explanations:
  - `grid = [[1,2,0],[1,3,0],[0,2,5]]`, `price = [2,5]`, `start = [0,0]`, `k = 3`
  - The output should be `[[0,1,2],[1,0,1],[2,1,5]]`

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to iterate over the entire grid, checking each item's price to see if it falls within the given range.
- For each item that meets the price criteria, calculate its Manhattan distance from the starting coordinates.
- Store all items that meet the price criteria, along with their distances and prices.
- Sort the stored items based on their prices and distances.
- Return the top `k` items.

```cpp
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Item {
    int store, item, price, distance;
};

struct Compare {
    bool operator()(const Item& a, const Item& b) {
        if (a.price == b.price) {
            return a.distance > b.distance;
        }
        return a.price < b.price;
    }
};

vector<vector<int>> highestRankedKItems(vector<vector<int>>& grid, vector<int>& price, vector<int>& start, int k) {
    int rows = grid.size(), cols = grid[0].size();
    priority_queue<Item, vector<Item>, Compare> pq;
    
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] != 0 && price[0] <= grid[i][j] && grid[i][j] <= price[1]) {
                Item item;
                item.store = i;
                item.item = j;
                item.price = grid[i][j];
                item.distance = abs(i - start[0]) + abs(j - start[1]);
                pq.push(item);
            }
        }
    }
    
    vector<vector<int>> result;
    while (!pq.empty() && k-- > 0) {
        Item item = pq.top();
        pq.pop();
        result.push_back({item.store, item.item, item.price});
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(R \cdot C \cdot \log(R \cdot C))$, where $R$ and $C$ are the number of rows and columns in the grid. This is because we iterate over the entire grid and then use a priority queue to sort the items.
> - **Space Complexity:** $O(R \cdot C)$, where $R$ and $C$ are the number of rows and columns in the grid. This is because in the worst case, we store all items in the priority queue.
> - **Why these complexities occur:** The time complexity occurs because of the iteration over the grid and the use of a priority queue. The space complexity occurs because we store all items in the priority queue.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a priority queue to store items as we explore the grid, rather than storing all items and then sorting them.
- We can use a `BFS` approach to explore the grid, starting from the given coordinates.
- As we explore each cell, we check if the item's price falls within the given range. If it does, we add it to the priority queue.
- We use a visited set to keep track of cells we've already visited, to avoid revisiting them.
- We continue exploring until we've found `k` items or we've explored the entire grid.

```cpp
#include <vector>
#include <queue>
#include <algorithm>
#include <set>

using namespace std;

struct Item {
    int store, item, price, distance;
};

struct Compare {
    bool operator()(const Item& a, const Item& b) {
        if (a.price == b.price) {
            return a.distance > b.distance;
        }
        return a.price < b.price;
    }
};

vector<vector<int>> highestRankedKItems(vector<vector<int>>& grid, vector<int>& price, vector<int>& start, int k) {
    int rows = grid.size(), cols = grid[0].size();
    priority_queue<Item, vector<Item>, Compare> pq;
    set<pair<int, int>> visited;
    vector<vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    
    queue<pair<int, int>> bfs;
    bfs.push({start[0], start[1]});
    visited.insert({start[0], start[1]});
    
    while (!bfs.empty()) {
        int x = bfs.front().first;
        int y = bfs.front().second;
        bfs.pop();
        
        if (grid[x][y] != 0 && price[0] <= grid[x][y] && grid[x][y] <= price[1]) {
            Item item;
            item.store = x;
            item.item = y;
            item.price = grid[x][y];
            item.distance = abs(x - start[0]) + abs(y - start[1]);
            pq.push(item);
        }
        
        for (auto& dir : directions) {
            int nx = x + dir[0];
            int ny = y + dir[1];
            
            if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && visited.find({nx, ny}) == visited.end()) {
                bfs.push({nx, ny});
                visited.insert({nx, ny});
            }
        }
        
        if (pq.size() >= k) {
            break;
        }
    }
    
    vector<vector<int>> result;
    while (!pq.empty() && k-- > 0) {
        Item item = pq.top();
        pq.pop();
        result.push_back({item.store, item.item, item.price});
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(R \cdot C \cdot \log(k))$, where $R$ and $C$ are the number of rows and columns in the grid. This is because we use a priority queue to store items, and we only store up to `k` items.
> - **Space Complexity:** $O(R \cdot C)$, where $R$ and $C$ are the number of rows and columns in the grid. This is because in the worst case, we store all cells in the visited set.
> - **Optimality proof:** This approach is optimal because we only store items that are within the given price range and we use a priority queue to efficiently select the top `k` items.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: `BFS`, priority queues, and efficient sorting.
- Problem-solving patterns identified: using a priority queue to efficiently select the top `k` items.
- Optimization techniques learned: using a visited set to avoid revisiting cells, and only storing up to `k` items in the priority queue.
- Similar problems to practice: other problems that involve finding the top `k` items in a grid or graph.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, such as an empty grid or an invalid starting position.
- Edge cases to watch for: an empty grid, an invalid starting position, or a price range that is outside the range of item prices.
- Performance pitfalls: using an inefficient sorting algorithm or storing all items in the priority queue.
- Testing considerations: testing the algorithm with different grid sizes, price ranges, and starting positions to ensure it works correctly in all cases.