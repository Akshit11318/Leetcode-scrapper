## Generate Random Point in a Circle
**Problem Link:** https://leetcode.com/problems/generate-random-point-in-a-circle/description

**Problem Statement:**
- Given the radius and center of a circle, generate a random point within the circle.
- Input format: `radius` and `x_center`, `y_center` as integers.
- Constraints: `0 <= radius <= 10^8` and `-10^8 <= x_center, y_center <= 10^8`.
- Expected output format: A random point within the circle, represented as an array `[x, y]`.
- Key requirements: Ensure the generated point is uniformly distributed within the circle.
- Example test cases:
  - Input: `radius = 1, x_center = 0, y_center = 0`, Output: `[0.0, 0.0]` (one possible output).
  - Input: `radius = 1, x_center = 0, y_center = 0`, Output: `[0.5, 0.5]` (another possible output).

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate random points within the bounding box of the circle and check if they fall within the circle.
- Step-by-step breakdown:
  1. Generate random points within the square that bounds the circle.
  2. Check if the point is within the circle by calculating its distance from the center.
  3. If the point is within the circle, return it. Otherwise, repeat the process.
- Why this approach comes to mind first: It's straightforward and easy to implement, but inefficient due to the rejection sampling method.

```cpp
#include <random>
#include <cmath>

class Solution {
public:
    std::random_device rd;
    std::mt19937 gen;
    double radius;
    double x_center, y_center;

    Solution(double radius, double x_center, double y_center) : radius(radius), x_center(x_center), y_center(y_center), gen(rd()) {}

    vector<double> randPoint() {
        while (true) {
            std::uniform_real_distribution<double> dis(-radius, radius);
            double x = dis(gen) + x_center;
            double y = dis(gen) + y_center;
            if (pow(x - x_center, 2) + pow(y - y_center, 2) <= pow(radius, 2)) {
                return {x, y};
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\frac{1}{\pi})$ due to the rejection sampling, as the ratio of the area of the circle to the area of the bounding box is $\pi/4$.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the random number generator and the circle's parameters.
> - **Why these complexities occur:** The time complexity is high because we might need to generate many points before finding one within the circle. The space complexity is low because we don't store any additional data structures that scale with the input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Generate random points within the circle directly by using polar coordinates.
- Detailed breakdown:
  1. Generate a random angle $\theta$ between $0$ and $2\pi$.
  2. Generate a random radius $r$ between $0$ and the circle's radius, but with a weighting to ensure uniform distribution (i.e., $r^2$ should be uniformly distributed).
  3. Convert the polar coordinates to Cartesian coordinates using $x = r \cos(\theta) + x_{center}$ and $y = r \sin(\theta) + y_{center}$.
- Proof of optimality: This method ensures that points are uniformly distributed within the circle, as we're directly generating points within the circle without any rejection.

```cpp
class Solution {
public:
    std::random_device rd;
    std::mt19937 gen;
    double radius;
    double x_center, y_center;

    Solution(double radius, double x_center, double y_center) : radius(radius), x_center(x_center), y_center(y_center), gen(rd()) {}

    vector<double> randPoint() {
        std::uniform_real_distribution<double> theta_dis(0, 2 * 3.141592653589793);
        std::uniform_real_distribution<double> r_dis(0, radius);
        double theta = theta_dis(gen);
        double r = sqrt(r_dis(gen) * r_dis(gen) / r_dis(gen).max());
        double x = r * cos(theta) + x_center;
        double y = r * sin(theta) + y_center;
        return {x, y};
    }
};
```
However, to make the code more efficient and actually uniformly distributed we use the following code instead:
```cpp
class Solution {
public:
    std::random_device rd;
    std::mt19937 gen;
    double radius;
    double x_center, y_center;

    Solution(double radius, double x_center, double y_center) : radius(radius), x_center(x_center), y_center(y_center), gen(rd()) {}

    vector<double> randPoint() {
        std::uniform_real_distribution<double> theta_dis(0, 2 * 3.141592653589793);
        std::uniform_real_distribution<double> r_dis(0, radius);
        double theta = theta_dis(gen);
        double r = sqrt(r_dis(gen));
        double x = r * cos(theta) + x_center;
        double y = r * sin(theta) + y_center;
        return {x, y};
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, as we generate the point directly without any loops or recursive calls.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the random number generator and the circle's parameters.
> - **Optimality proof:** This method is optimal because it generates points uniformly within the circle without any rejection, ensuring the best possible time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Polar coordinates, uniform distribution, and rejection sampling.
- Problem-solving patterns identified: Direct generation of points within a shape to avoid rejection sampling.
- Optimization techniques learned: Using polar coordinates to generate points within a circle.
- Similar problems to practice: Generating random points within other shapes, such as rectangles or polygons.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing the rejection sampling method or the polar coordinate transformation.
- Edge cases to watch for: Points on the boundary of the circle, which should be included in the uniform distribution.
- Performance pitfalls: Using rejection sampling without considering the ratio of the areas, leading to inefficient algorithms.
- Testing considerations: Ensure that the generated points are indeed uniformly distributed within the circle by testing with a large number of points.