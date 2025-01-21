## Furthest Building You Can Reach
**Problem Link:** https://leetcode.com/problems/furthest-building-you-can-reach/description

**Problem Statement:**
- Input: `heights` (an array of integers representing the heights of buildings), `bricks` (the number of bricks you have), and `ladders` (the number of ladders you have).
- Constraints: `1 <= heights.length <= 10^5`, `1 <= heights[i] <= 10^6`, `0 <= bricks <= 10^9`, `0 <= ladders <= heights.length`.
- Expected output: The furthest building index that you can reach.
- Key requirements: You can use bricks to fill gaps between buildings and ladders to jump over gaps. You want to find the furthest building you can reach with the given bricks and ladders.
- Example test cases: 
  - Input: `heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1`, Output: `4`.
  - Input: `heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2`, Output: `7`.
  - Input: `heights = [14,3,19,3], bricks = 17, ladders = 0`, Output: `3`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to try all possible combinations of using bricks and ladders for each gap between buildings.
- Step-by-step breakdown:
  1. Calculate the height difference between each pair of adjacent buildings.
  2. For each height difference, decide whether to use bricks or a ladder.
  3. If using bricks, subtract the height difference from the total bricks.
  4. If using a ladder, decrement the ladder count.
  5. If at any point the bricks or ladders are insufficient, stop and return the current building index.
- Why this approach comes to mind first: It seems like a straightforward way to simulate the process of deciding how to fill or jump over gaps.

```cpp
class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        // Initialize the index of the furthest building that can be reached
        int furthest = 0;
        
        // Iterate over the heights of the buildings
        for (int i = 0; i < heights.size() - 1; ++i) {
            // Calculate the height difference between the current and next buildings
            int diff = heights[i + 1] - heights[i];
            
            // If the height difference is positive (i.e., we need to fill or jump over a gap)
            if (diff > 0) {
                // If we have enough bricks to fill the gap, use them
                if (bricks >= diff) {
                    bricks -= diff;
                }
                // If we have a ladder available, use it
                else if (ladders > 0) {
                    --ladders;
                }
                // If we don't have enough bricks or ladders, stop and return the current index
                else {
                    break;
                }
            }
            
            // Update the furthest building index
            furthest = i + 1;
        }
        
        return furthest;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of buildings, because we iterate over the heights of the buildings once.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the furthest building index, bricks, and ladders.
> - **Why these complexities occur:** The time complexity is linear because we only iterate over the heights of the buildings once. The space complexity is constant because we don't use any data structures that grow with the input size.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a priority queue to keep track of the largest height differences that we need to fill or jump over.
- Step-by-step breakdown:
  1. Initialize a priority queue to store the height differences.
  2. Iterate over the heights of the buildings, calculating the height difference between each pair of adjacent buildings.
  3. If the height difference is positive, push it onto the priority queue.
  4. If the size of the priority queue exceeds the number of ladders, pop the largest height difference from the queue and subtract it from the total bricks.
  5. If at any point the bricks are insufficient, stop and return the current building index.
- Why this approach is optimal: It ensures that we use the ladders for the largest height differences and the bricks for the smaller differences, which maximizes the distance we can reach.

```cpp
class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        // Initialize a priority queue to store the height differences
        priority_queue<int, vector<int>, greater<int>> pq;
        
        // Iterate over the heights of the buildings
        for (int i = 0; i < heights.size() - 1; ++i) {
            // Calculate the height difference between the current and next buildings
            int diff = heights[i + 1] - heights[i];
            
            // If the height difference is positive (i.e., we need to fill or jump over a gap)
            if (diff > 0) {
                // Push the height difference onto the priority queue
                pq.push(diff);
                
                // If the size of the priority queue exceeds the number of ladders
                if (pq.size() > ladders) {
                    // Pop the largest height difference from the queue and subtract it from the total bricks
                    bricks -= pq.top();
                    pq.pop();
                    
                    // If the bricks are insufficient, stop and return the current index
                    if (bricks < 0) {
                        return i;
                    }
                }
            }
        }
        
        // If we can reach all buildings, return the last index
        return heights.size() - 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log k)$, where $n$ is the number of buildings and $k$ is the number of ladders, because we iterate over the heights of the buildings and use a priority queue to keep track of the largest height differences.
> - **Space Complexity:** $O(k)$, because we use a priority queue to store the largest height differences.
> - **Optimality proof:** This approach is optimal because it ensures that we use the ladders for the largest height differences and the bricks for the smaller differences, which maximizes the distance we can reach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: priority queues, greedy algorithms.
- Problem-solving patterns: using a priority queue to keep track of the largest height differences.
- Optimization techniques: using ladders for the largest height differences and bricks for the smaller differences.

**Mistakes to Avoid:**
- Not using a priority queue to keep track of the largest height differences.
- Not checking if the bricks are sufficient before using them.
- Not returning the correct index when the bricks are insufficient.