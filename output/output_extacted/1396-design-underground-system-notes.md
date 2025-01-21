## Design Underground System

**Problem Link:** https://leetcode.com/problems/design-underground-system/description

**Problem Statement:**
- Input format and constraints: The system will receive commands in the form of `checkIn`, `checkOut`, and `getAverageTime`. 
- Expected output format: The system should return the average time spent by a customer in a given station.
- Key requirements and edge cases to consider: 
  - A customer can check-in and check-out multiple times.
  - A customer can check-in to a station and then check-out from a different station.
  - The system should handle cases where a customer checks-in but does not check-out.
- Example test cases with explanations:
  - `checkIn(45, "Leyton", 3)`, `checkOut(45, "Waterloo", 15)`, `getAverageTime(45, "Leyton", "Waterloo")` should return `12.0`.
  - `checkIn(45, "Leyton", 3)`, `checkOut(45, "Waterloo", 15)`, `checkIn(45, "Leyton", 16)`, `checkOut(45, "Waterloo", 24)`, `getAverageTime(45, "Leyton", "Waterloo")` should return `11.0`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Store all check-in and check-out events for each customer and calculate the average time spent at each station.
- Step-by-step breakdown of the solution:
  1. Create a data structure to store check-in and check-out events for each customer.
  2. For each `checkIn` event, store the station and time.
  3. For each `checkOut` event, calculate the time spent at the station and store it.
  4. For each `getAverageTime` request, calculate the average time spent by the customer at the given stations.
- Why this approach comes to mind first: It is straightforward to store all events and calculate the average time spent at each station.

```cpp
class UndergroundSystem {
public:
    unordered_map<int, pair<string, int>> check_in;
    unordered_map<int, vector<pair<string, string, int>>> check_out;

    UndergroundSystem() {}

    void checkIn(int id, string stationName, int t) {
        check_in[id] = {stationName, t};
    }

    void checkOut(int id, string stationName, int t) {
        if (check_in.find(id) != check_in.end()) {
            check_out[id].push_back({check_in[id].first, stationName, t - check_in[id].second});
            check_in.erase(id);
        }
    }

    double getAverageTime(int startStation, string endStation) {
        double total_time = 0;
        int count = 0;
        for (auto& customer : check_out) {
            for (auto& trip : customer.second) {
                if (trip.first == startStation && trip.second == endStation) {
                    total_time += trip.third;
                    count++;
                }
            }
        }
        if (count == 0) return 0;
        return total_time / count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of customers and $m$ is the number of trips for each customer. This is because we iterate over all trips for each customer in the `getAverageTime` method.
> - **Space Complexity:** $O(n \cdot m)$ where $n$ is the number of customers and $m$ is the number of trips for each customer. This is because we store all trips for each customer.
> - **Why these complexities occur:** We store all events and calculate the average time spent at each station, which requires iterating over all trips for each customer.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of storing all trips for each customer, we can store the total time spent and the number of trips for each station pair.
- Detailed breakdown of the approach:
  1. Create a data structure to store the total time spent and the number of trips for each station pair.
  2. For each `checkIn` event, store the station and time.
  3. For each `checkOut` event, calculate the time spent at the station and update the total time spent and the number of trips for the station pair.
  4. For each `getAverageTime` request, return the average time spent by the customer at the given stations.
- Why further optimization is impossible: We need to store the total time spent and the number of trips for each station pair to calculate the average time spent.

```cpp
class UndergroundSystem {
public:
    unordered_map<int, pair<string, int>> check_in;
    unordered_map<string, pair<double, int>> total_time;

    UndergroundSystem() {}

    void checkIn(int id, string stationName, int t) {
        check_in[id] = {stationName, t};
    }

    void checkOut(int id, string stationName, int t) {
        if (check_in.find(id) != check_in.end()) {
            string start_station = check_in[id].first;
            string end_station = stationName;
            double time_spent = t - check_in[id].second;
            if (total_time.find(start_station + "," + end_station) == total_time.end()) {
                total_time[start_station + "," + end_station] = {time_spent, 1};
            } else {
                total_time[start_station + "," + end_station].first += time_spent;
                total_time[start_station + "," + end_station].second++;
            }
            check_in.erase(id);
        }
    }

    double getAverageTime(string startStation, string endStation) {
        if (total_time.find(startStation + "," + endStation) == total_time.end()) return 0;
        return total_time[startStation + "," + endStation].first / total_time[startStation + "," + endStation].second;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for `checkIn` and `checkOut` methods, $O(1)$ for `getAverageTime` method.
> - **Space Complexity:** $O(n)$ where $n$ is the number of unique station pairs.
> - **Optimality proof:** We only store the necessary information to calculate the average time spent, and we update it in constant time. This is the best possible complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a data structure to store the total time spent and the number of trips for each station pair.
- Problem-solving patterns identified: Optimizing the solution by reducing the amount of stored data and updating it in constant time.
- Optimization techniques learned: Using a dictionary to store the total time spent and the number of trips for each station pair.
- Similar problems to practice: Problems that involve calculating averages or totals for a given set of data.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the total time spent and the number of trips correctly.
- Edge cases to watch for: Handling cases where a customer checks-in but does not check-out.
- Performance pitfalls: Storing unnecessary data and iterating over it unnecessarily.
- Testing considerations: Testing the solution with different inputs and edge cases to ensure it works correctly.