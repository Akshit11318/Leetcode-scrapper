## Design Parking System
**Problem Link:** https://leetcode.com/problems/design-parking-system/description

**Problem Statement:**
- Input format and constraints: The system has three types of parking spaces: big, medium, and small, with `big`, `medium`, and `small` spaces available, respectively.
- Expected output format: The system should return `true` if a car can be parked and `false` otherwise.
- Key requirements and edge cases to consider: Cars of different sizes can only be parked in spaces of the same size or larger.
- Example test cases with explanations:
  - `ParkingSystem(1, 2, 3)`: Initialize the system with 1 big, 2 medium, and 3 small spaces.
  - `addCar(1)`: Add a big car to the system.
  - `addCar(2)`: Add a medium car to the system.
  - `addCar(3)`: Add a small car to the system.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Initialize the parking system with the given number of spaces for each type of car.
- Step-by-step breakdown of the solution:
  1. Initialize variables to keep track of the available spaces for each type of car.
  2. When a car is added, check if there are available spaces of the same type or larger.
  3. If there are available spaces, decrement the count and return `true`.
  4. If not, return `false`.
- Why this approach comes to mind first: It's a straightforward implementation that directly addresses the problem statement.

```cpp
class ParkingSystem {
public:
    int big, medium, small;
    ParkingSystem(int big, int medium, int small) {
        this->big = big;
        this->medium = medium;
        this->small = small;
    }
    
    bool addCar(int carType) {
        if (carType == 1) {
            if (big > 0) {
                big--;
                return true;
            }
        } else if (carType == 2) {
            if (medium > 0) {
                medium--;
                return true;
            }
        } else if (carType == 3) {
            if (small > 0) {
                small--;
                return true;
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, as we only perform constant-time operations.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the available spaces for each type of car.
> - **Why these complexities occur:** The operations are simple and don't depend on the input size, resulting in constant time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use an array to store the available spaces for each type of car, and use the car type as an index to access the corresponding count.
- Detailed breakdown of the approach:
  1. Initialize an array with the given number of spaces for each type of car.
  2. When a car is added, check if there are available spaces of the same type or larger by accessing the corresponding index in the array.
  3. If there are available spaces, decrement the count and return `true`.
  4. If not, return `false`.
- Proof of optimality: This approach is optimal because it uses a constant amount of space and performs constant-time operations.

```cpp
class ParkingSystem {
public:
    int spaces[3];
    ParkingSystem(int big, int medium, int small) {
        spaces[0] = big;
        spaces[1] = medium;
        spaces[2] = small;
    }
    
    bool addCar(int carType) {
        carType--;
        if (spaces[carType] > 0) {
            spaces[carType]--;
            return true;
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, as we only perform constant-time operations.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the available spaces for each type of car.
> - **Optimality proof:** This approach is optimal because it uses a constant amount of space and performs constant-time operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using arrays to store and access data, and performing constant-time operations.
- Problem-solving patterns identified: Using the problem constraints to determine the optimal data structure and approach.
- Optimization techniques learned: Using arrays to reduce the number of variables and improve code readability.
- Similar problems to practice: Other problems that involve using arrays and performing constant-time operations.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the array correctly, or not checking for available spaces before decrementing the count.
- Edge cases to watch for: Cars of different sizes can only be parked in spaces of the same size or larger.
- Performance pitfalls: Using a non-constant amount of space or performing non-constant-time operations.
- Testing considerations: Test the system with different inputs and edge cases to ensure it works correctly.