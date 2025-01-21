## Beautiful Towers II

**Problem Link:** https://leetcode.com/problems/beautiful-towers-ii/description

**Problem Statement:**
- Given an array of integers `heights` representing the heights of towers, and an integer `k`, return the minimum number of moves required to make all towers have the same height, where a move is defined as increasing or decreasing the height of a tower by 1.
- Input format and constraints: 
  - `1 <= heights.length <= 10^5`
  - `1 <= heights[i] <= 10^9`
  - `1 <= k <= 10^9`
- Expected output format: The minimum number of moves required.
- Key requirements and edge cases to consider:
  - All towers must have the same height after the minimum number of moves.
  - The height of each tower can be increased or decreased by 1 in a single move.

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible heights for the towers and calculating the number of moves required for each height.
- We iterate over all possible heights from the minimum to the maximum height in the `heights` array.
- For each height, we calculate the total number of moves required to make all towers have that height.
- We keep track of the minimum number of moves required across all possible heights.

```cpp
#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int minMoves(vector<int>& heights) {
    int min_height = INT_MAX;
    int max_height = INT_MIN;
    for (int height : heights) {
        min_height = min(min_height, height);
        max_height = max(max_height, height);
    }
    
    int min_moves = INT_MAX;
    for (int height = min_height; height <= max_height; height++) {
        int total_moves = 0;
        for (int h : heights) {
            total_moves += abs(h - height);
        }
        min_moves = min(min_moves, total_moves);
    }
    
    return min_moves;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of towers and $m$ is the range of possible heights.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum and maximum heights, and the minimum number of moves.
> - **Why these complexities occur:** The time complexity occurs because we iterate over all possible heights for each tower, and the space complexity occurs because we only use a constant amount of space to store the necessary variables.

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is that the median of the heights array is the optimal height that minimizes the total number of moves.
- We can use the fact that the median is the value that minimizes the sum of absolute differences with all other values in the array.
- We can find the median of the heights array by sorting the array and taking the middle value (or the average of the two middle values if the length of the array is even).
- We then calculate the total number of moves required to make all towers have the median height.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int minMoves(vector<int>& heights) {
    sort(heights.begin(), heights.end());
    int median_height;
    if (heights.size() % 2 == 0) {
        median_height = (heights[heights.size() / 2 - 1] + heights[heights.size() / 2]) / 2;
    } else {
        median_height = heights[heights.size() / 2];
    }
    
    int total_moves = 0;
    for (int height : heights) {
        total_moves += abs(height - median_height);
    }
    
    return total_moves;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of towers.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the necessary variables.
> - **Optimality proof:** The median is the value that minimizes the sum of absolute differences with all other values in the array, which is equivalent to minimizing the total number of moves required to make all towers have the same height.

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of the median to minimize the sum of absolute differences.
- The problem-solving pattern identified is the use of sorting and median calculation to find the optimal solution.
- The optimization technique learned is the use of the median to reduce the time complexity of the solution.

**Mistakes to Avoid:**
- A common implementation error is to use a brute force approach that tries all possible heights, which can lead to a high time complexity.
- An edge case to watch for is when the length of the heights array is even, in which case the median is the average of the two middle values.
- A performance pitfall to avoid is using a sorting algorithm with a high time complexity, such as bubble sort or insertion sort.