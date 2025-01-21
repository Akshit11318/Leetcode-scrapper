## Maximum Average Pass Ratio
**Problem Link:** https://leetcode.com/problems/maximum-average-pass-ratio/description

**Problem Statement:**
- Input format and constraints: Given a list of `n` classes with `classes[i] = [pass_i, total_i]`, where `pass_i` is the number of students that passed the class and `total_i` is the total number of students in the class, find the maximum average pass ratio.
- Expected output format: The maximum average pass ratio.
- Key requirements and edge cases to consider: The pass ratio of a class is `pass_i / total_i`, and the average pass ratio is the sum of pass ratios of all classes divided by `n`. 
- Example test cases with explanations: For example, given `classes = [[1,2],[3,5],[2,2]]`, the maximum average pass ratio is `(1/2 + 3/5 + 1/1) / 3`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The brute force approach involves iterating over all possible combinations of classes and calculating the average pass ratio for each combination.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of classes.
  2. For each combination, calculate the average pass ratio.
  3. Keep track of the maximum average pass ratio found so far.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it has a high time complexity due to the generation of all possible combinations.

```cpp
#include <vector>
#include <algorithm>

double maxAverageRatio(std::vector<std::vector<int>>& classes, int extraStudents) {
    double maxRatio = 0.0;
    while (extraStudents > 0) {
        double maxIncrease = 0.0;
        int maxIndex = 0;
        for (int i = 0; i < classes.size(); i++) {
            double currentRatio = static_cast<double>(classes[i][0]) / classes[i][1];
            double newRatio = static_cast<double>(classes[i][0] + 1) / (classes[i][1] + 1);
            double increase = newRatio - currentRatio;
            if (increase > maxIncrease) {
                maxIncrease = increase;
                maxIndex = i;
            }
        }
        classes[maxIndex][0]++;
        classes[maxIndex][1]++;
        extraStudents--;
    }
    double sumRatio = 0.0;
    for (const auto& cls : classes) {
        sumRatio += static_cast<double>(cls[0]) / cls[1];
    }
    maxRatio = sumRatio / classes.size();
    return maxRatio;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot extraStudents)$, where $n$ is the number of classes and $extraStudents$ is the number of extra students.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum average pass ratio and other variables.
> - **Why these complexities occur:** The time complexity is high because we iterate over all classes for each extra student, and the space complexity is low because we only use a constant amount of space.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a priority queue to keep track of the classes with the maximum increase in pass ratio.
- Detailed breakdown of the approach:
  1. Initialize a priority queue to store the classes with the maximum increase in pass ratio.
  2. For each class, calculate the increase in pass ratio if one extra student is added.
  3. Add the class with the maximum increase in pass ratio to the priority queue.
  4. While there are extra students, remove the class with the maximum increase in pass ratio from the priority queue and add one extra student to the class.
- Proof of optimality: This approach is optimal because it always adds one extra student to the class with the maximum increase in pass ratio, which maximizes the average pass ratio.

```cpp
#include <vector>
#include <queue>
#include <algorithm>

struct Class {
    int pass;
    int total;
};

struct Compare {
    bool operator()(const Class& a, const Class& b) {
        double increaseA = (static_cast<double>(a.pass + 1) / (a.total + 1)) - (static_cast<double>(a.pass) / a.total);
        double increaseB = (static_cast<double>(b.pass + 1) / (b.total + 1)) - (static_cast<double>(b.pass) / b.total);
        return increaseA < increaseB;
    }
};

double maxAverageRatio(std::vector<std::vector<int>>& classes, int extraStudents) {
    std::priority_queue<Class, std::vector<Class>, Compare> pq;
    for (const auto& cls : classes) {
        Class c = {cls[0], cls[1]};
        pq.push(c);
    }
    while (extraStudents > 0) {
        Class c = pq.top();
        pq.pop();
        c.pass++;
        c.total++;
        pq.push(c);
        extraStudents--;
    }
    double sumRatio = 0.0;
    while (!pq.empty()) {
        Class c = pq.top();
        pq.pop();
        sumRatio += static_cast<double>(c.pass) / c.total;
    }
    return sumRatio / classes.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot extraStudents \cdot log(n))$, where $n$ is the number of classes and $extraStudents$ is the number of extra students.
> - **Space Complexity:** $O(n)$, as we use a priority queue to store the classes.
> - **Optimality proof:** This approach is optimal because it always adds one extra student to the class with the maximum increase in pass ratio, which maximizes the average pass ratio.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queue, greedy algorithm.
- Problem-solving patterns identified: Always choose the option that maximizes the increase in pass ratio.
- Optimization techniques learned: Using a priority queue to keep track of the classes with the maximum increase in pass ratio.
- Similar problems to practice: Other problems that involve maximizing or minimizing a ratio or average.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the pass ratio correctly after adding one extra student to a class.
- Edge cases to watch for: Handling the case where there are no extra students or no classes.
- Performance pitfalls: Using a brute force approach that has a high time complexity.
- Testing considerations: Testing the function with different inputs and edge cases to ensure it works correctly.