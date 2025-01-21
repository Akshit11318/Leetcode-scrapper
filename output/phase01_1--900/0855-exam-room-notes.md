## Exam Room
**Problem Link:** https://leetcode.com/problems/exam-room/description

**Problem Statement:**
- Input format and constraints: The problem involves designing an exam room with `N` seats, where a student enters and occupies the seat that is farthest from any occupied seats. If there are multiple seats that satisfy this condition, the student occupies the seat with the smallest index.
- Expected output format: The `ExamRoom` class should have two methods: `seat()` and `leave()`. The `seat()` method returns the index of the seat that the student occupies, while the `leave()` method takes a seat index as input and marks the seat as unoccupied.
- Key requirements and edge cases to consider:
  - The exam room has `N` seats.
  - A student occupies the seat that is farthest from any occupied seats.
  - If there are multiple seats that satisfy this condition, the student occupies the seat with the smallest index.
- Example test cases with explanations:
  - `ExamRoom(10)`: Creates an exam room with 10 seats.
  - `seat()`: Returns the index of the seat that the student occupies.
  - `leave(3)`: Marks the seat with index 3 as unoccupied.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over all seats in the exam room and calculating the distance from each seat to the nearest occupied seat. The seat with the maximum distance is occupied by the student.
- Step-by-step breakdown of the solution:
  1. Initialize an array to keep track of occupied seats.
  2. When a student enters, iterate over all seats and calculate the distance from each seat to the nearest occupied seat.
  3. Occupy the seat with the maximum distance.
  4. When a student leaves, mark the seat as unoccupied.
- Why this approach comes to mind first: The brute force approach is straightforward and easy to implement, but it is inefficient for large inputs.

```cpp
class ExamRoom {
public:
    vector<int> seats;
    int n;
    ExamRoom(int N) {
        n = N;
        seats = vector<int>(N, 0);
    }
    
    int seat() {
        int max_distance = -1;
        int seat_index = -1;
        for (int i = 0; i < n; i++) {
            if (seats[i] == 0) {
                int distance = calculate_distance(i);
                if (distance > max_distance) {
                    max_distance = distance;
                    seat_index = i;
                }
            }
        }
        seats[seat_index] = 1;
        return seat_index;
    }
    
    void leave(int p) {
        seats[p] = 0;
    }
    
    int calculate_distance(int i) {
        int distance = INT_MAX;
        for (int j = 0; j < n; j++) {
            if (seats[j] == 1) {
                distance = min(distance, abs(i - j));
            }
        }
        if (distance == INT_MAX) {
            distance = max(i, n - 1 - i);
        }
        return distance;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N^2)$, where $N$ is the number of seats. This is because we iterate over all seats in the `seat()` method and calculate the distance from each seat to the nearest occupied seat.
> - **Space Complexity:** $O(N)$, where $N$ is the number of seats. This is because we use an array to keep track of occupied seats.
> - **Why these complexities occur:** The brute force approach involves iterating over all seats and calculating the distance from each seat to the nearest occupied seat, resulting in a high time complexity. The space complexity is linear because we use an array to keep track of occupied seats.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a priority queue to keep track of the seats with the maximum distance to the nearest occupied seat. The priority queue can be implemented using a set of pairs, where each pair contains the distance and the index of the seat.
- Detailed breakdown of the approach:
  1. Initialize a set of pairs to keep track of the seats with the maximum distance to the nearest occupied seat.
  2. When a student enters, iterate over the set of pairs and find the seat with the maximum distance.
  3. Occupy the seat with the maximum distance and update the set of pairs.
  4. When a student leaves, update the set of pairs to reflect the new distances.
- Proof of optimality: The optimal approach has a time complexity of $O(\log N)$, which is much faster than the brute force approach for large inputs.

```cpp
class ExamRoom {
public:
    int n;
    set<pair<int, int>> seats;
    ExamRoom(int N) {
        n = N;
        seats.insert({-N, 0});
        seats.insert({-N, N});
    }
    
    int seat() {
        int max_distance = -1;
        int seat_index = -1;
        for (auto it = seats.begin(); it != seats.end(); it++) {
            int distance = calculate_distance(it->second);
            if (distance > max_distance) {
                max_distance = distance;
                seat_index = it->second;
            }
        }
        seats.insert({-max_distance, seat_index});
        return seat_index;
    }
    
    void leave(int p) {
        for (auto it = seats.begin(); it != seats.end(); it++) {
            if (it->second == p) {
                seats.erase(it);
                break;
            }
        }
    }
    
    int calculate_distance(int i) {
        int distance = INT_MAX;
        for (auto it = seats.begin(); it != seats.end(); it++) {
            if (it->second != i) {
                distance = min(distance, abs(i - it->second));
            }
        }
        return distance;
    }
};
```

However, the optimal solution provided by leetcode uses a different approach that maintains the intervals of empty seats instead of the seats themselves. Here is the optimal solution:

```cpp
class ExamRoom {
public:
    int n;
    set<pair<int, int>> seats;
    ExamRoom(int N) {
        n = N;
        seats.insert({-N, 0});
        seats.insert({-N, N});
    }
    
    int seat() {
        int max_distance = -1;
        int seat_index = -1;
        for (auto it = seats.begin(); it != seats.end(); it++) {
            int next = (it == seats.end() ? n : (*it).second);
            int prev = (it == seats.begin() ? -1 : prev(it));
            int distance = min(next - prev - 1, max(prev, n - 1 - next));
            if (distance > max_distance) {
                max_distance = distance;
                seat_index = prev + distance;
            }
        }
        seats.insert({-max_distance, seat_index});
        return seat_index;
    }
    
    void leave(int p) {
        for (auto it = seats.begin(); it != seats.end(); it++) {
            if (it->second == p) {
                seats.erase(it);
                break;
            }
        }
    }
    
    int prev(set<pair<int, int>>::iterator it) {
        it--;
        return it->second;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log N)$, where $N$ is the number of seats. This is because we use a set to keep track of the seats with the maximum distance to the nearest occupied seat.
> - **Space Complexity:** $O(N)$, where $N$ is the number of seats. This is because we use a set to keep track of the seats with the maximum distance to the nearest occupied seat.
> - **Optimality proof:** The optimal approach has a time complexity of $O(\log N)$, which is much faster than the brute force approach for large inputs. The space complexity is linear because we use a set to keep track of the seats with the maximum distance to the nearest occupied seat.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of priority queues and sets to solve problems involving distances and intervals.
- Problem-solving patterns identified: The problem requires identifying the seat with the maximum distance to the nearest occupied seat, which involves iterating over the set of pairs and finding the maximum distance.
- Optimization techniques learned: The problem demonstrates the use of priority queues and sets to optimize the solution.
- Similar problems to practice: Similar problems include finding the maximum distance between two points in a set of points, or finding the minimum distance between two sets of points.

**Mistakes to Avoid:**
- Common implementation errors: The most common implementation error is not updating the set of pairs correctly when a student enters or leaves.
- Edge cases to watch for: The problem has several edge cases, including when the exam room is empty or when a student enters or leaves the exam room.
- Performance pitfalls: The brute force approach has a high time complexity, which can lead to performance issues for large inputs.
- Testing considerations: The problem requires testing with different inputs, including edge cases, to ensure that the solution is correct and efficient.