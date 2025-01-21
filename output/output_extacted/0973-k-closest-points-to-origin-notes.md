## K Closest Points to Origin

**Problem Link:** https://leetcode.com/problems/k-closest-points-to-origin/description

**Problem Statement:**
- Input format: An array of points where each point is an array of two integers representing x and y coordinates, and an integer k.
- Constraints: 1 <= k <= points.length <= 10^4, -10^4 < xi, yi < 10^4
- Expected output format: An array of the k points closest to the origin.
- Key requirements and edge cases to consider: The distance of a point from the origin is calculated using the Euclidean distance formula, and in case of a tie, any point can be chosen.
- Example test cases with explanations:
  - Example 1: Input: points = [[1,3],[-2,2]], k = 1. Output: [[-2,2]] because the point (-2,2) is the closest to the origin.
  - Example 2: Input: points = [[3,3],[5,-1],[-2,4]], k = 2. Output: [[3,3],[-2,4]] because these two points are the closest to the origin.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the distance of each point from the origin and store these distances along with their corresponding points.
- Step-by-step breakdown of the solution:
  1. Calculate the Euclidean distance of each point from the origin.
  2. Store these distances in an array or a data structure that also keeps track of the points.
  3. Sort the points based on their distances from the origin.
  4. Return the first k points from the sorted array.
- Why this approach comes to mind first: It directly addresses the problem by calculating distances and then sorting based on these distances.

```cpp
#include <vector>
#include <algorithm>

using namespace std;

struct Point {
    int x, y;
    int distance;
};

bool comparePoints(const Point& a, const Point& b) {
    return a.distance < b.distance;
}

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    vector<Point> pointsWithDistance;
    for (auto& point : points) {
        Point p;
        p.x = point[0];
        p.y = point[1];
        p.distance = p.x * p.x + p.y * p.y; // Calculate distance from origin
        pointsWithDistance.push_back(p);
    }
    
    sort(pointsWithDistance.begin(), pointsWithDistance.end(), comparePoints);
    
    vector<vector<int>> result;
    for (int i = 0; i < k; ++i) {
        result.push_back({pointsWithDistance[i].x, pointsWithDistance[i].y});
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of points.
> - **Space Complexity:** $O(n)$ for storing the points with their distances.
> - **Why these complexities occur:** The main operation is sorting, which in C++'s `std::sort` is typically implemented with a time complexity of $O(n \log n)$. The space complexity is due to the additional array of `Point` structures needed to store distances.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of sorting all points, we can use a partial sorting approach to find the k smallest elements (points closest to the origin).
- Detailed breakdown of the approach:
  1. Use a `std::priority_queue` (max heap) to store points based on their distances from the origin.
  2. Push the first k points into the heap.
  3. For each remaining point, if its distance is less than the distance of the point at the top of the heap (the point farthest from the origin among the current k points), remove the top point and push the new point into the heap.
- Proof of optimality: This approach ensures that we only consider the k closest points and do not need to sort the entire array, making it more efficient than the brute force approach for large inputs.
- Why further optimization is impossible: This approach has a time complexity of $O(n \log k)$, which is optimal because we must at least examine each point once.

```cpp
#include <vector>
#include <queue>

using namespace std;

struct Point {
    int x, y;
};

struct ComparePoints {
    bool operator()(const vector<int>& a, const vector<int>& b) {
        return a[0]*a[0] + a[1]*a[1] > b[0]*b[0] + b[1]*b[1];
    }
};

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    priority_queue<vector<int>, vector<vector<int>>, ComparePoints> maxHeap;
    
    for (auto& point : points) {
        if (maxHeap.size() < k) {
            maxHeap.push(point);
        } else if (point[0]*point[0] + point[1]*point[1] < maxHeap.top()[0]*maxHeap.top()[0] + maxHeap.top()[1]*maxHeap.top()[1]) {
            maxHeap.pop();
            maxHeap.push(point);
        }
    }
    
    vector<vector<int>> result;
    while (!maxHeap.empty()) {
        result.push_back(maxHeap.top());
        maxHeap.pop();
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log k)$, where $n$ is the number of points. This is because we perform a push or pop operation for each point, and each of these operations takes $O(\log k)$ time in the worst case.
> - **Space Complexity:** $O(k)$ for the priority queue.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations needed to find the k closest points, leveraging the properties of a max heap to efficiently maintain the set of closest points encountered so far.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Partial sorting, use of priority queues for efficient selection of k smallest elements.
- Problem-solving patterns identified: Leveraging data structures like heaps to reduce computational complexity.
- Optimization techniques learned: Avoiding unnecessary computations by only considering the relevant subset of data.
- Similar problems to practice: Other problems involving partial sorting or selection of k elements from a larger set.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect usage of priority queues or misunderstanding the comparison function.
- Edge cases to watch for: Handling cases where k is equal to the number of points, or where points have the same distance from the origin.
- Performance pitfalls: Using a full sort when a partial sort would suffice, leading to unnecessary computational overhead.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases and large datasets.