## The Airport with the Most Traffic
**Problem Link:** https://leetcode.com/problems/the-airport-with-the-most-traffic/description

**Problem Statement:**
- Input format and constraints: The input will be a list of flights where each flight is represented as an array of three elements: `[source, destination, passengers]`. The `source` and `destination` are airport codes, and `passengers` is the number of passengers on the flight. The task is to find the airport with the most total traffic, which is defined as the sum of the number of passengers arriving and departing at that airport.
- Expected output format: The output should be a list of airport codes with the most traffic.
- Key requirements and edge cases to consider: Handling ties (multiple airports with the same maximum traffic), ensuring that airports are correctly identified even when they appear as both source and destination, and efficiently calculating traffic for each airport.
- Example test cases with explanations:
  - Example 1: `[["ATL","JFK",100],["JFK","ATL",100],["ATL","LAX",100]]` should return `["ATL","JFK"]` because both ATL and JFK have a total traffic of 200.
  - Example 2: `[["JFK","SFO",100],["JFK","ATL",100],["SFO","ATL",100],["ATL","JFK",100]]` should return `["JFK","ATL"]` because both have a total traffic of 300.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: For each flight, add the number of passengers to both the source and destination airports' traffic counts. Then, find the maximum traffic count among all airports.
- Step-by-step breakdown of the solution:
  1. Create a dictionary (or map) to store the traffic count for each airport.
  2. Iterate through each flight, adding the passengers to the traffic count of both the source and destination airports.
  3. Find the maximum traffic count.
  4. Return all airports with the maximum traffic count.
- Why this approach comes to mind first: It directly addresses the problem by counting traffic for each airport and then finding the maximum.

```cpp
#include <vector>
#include <unordered_map>
#include <string>

std::vector<std::string> findAirportsWithMostTraffic(std::vector<std::vector<int>>& flights) {
    std::unordered_map<std::string, int> airportTraffic;
    for (const auto& flight : flights) {
        // Assuming flight[0] is source, flight[1] is destination, and flight[2] is passengers
        airportTraffic[flight[0]] += flight[2];
        airportTraffic[flight[1]] += flight[2];
    }
    
    int maxTraffic = 0;
    for (const auto& pair : airportTraffic) {
        if (pair.second > maxTraffic) {
            maxTraffic = pair.second;
        }
    }
    
    std::vector<std::string> result;
    for (const auto& pair : airportTraffic) {
        if (pair.second == maxTraffic) {
            result.push_back(pair.first);
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of flights and $m$ is the number of unique airports. This is because we iterate through all flights once to calculate traffic and then through all airports to find the maximum traffic.
> - **Space Complexity:** $O(m)$ for storing the traffic count of each airport.
> - **Why these complexities occur:** The iteration through flights and airports directly contributes to the time complexity, while storing traffic counts for each airport contributes to the space complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already quite efficient for this problem, as it involves a single pass through the flights to calculate traffic and then a pass through the airports to find the maximum. However, we can slightly optimize the code by combining the traffic count calculation and the maximum traffic finding into a single pass through the flights, but the overall time complexity remains the same due to the need to iterate through all flights and airports.
- Detailed breakdown of the approach:
  1. Create a dictionary to store the traffic count for each airport and initialize the maximum traffic count.
  2. Iterate through each flight, updating the traffic count of both the source and destination airports and updating the maximum traffic count if necessary.
  3. After iterating through all flights, iterate through the airport traffic counts to find all airports with the maximum traffic.
- Proof of optimality: This approach is optimal because it only requires a single pass through the flights to calculate traffic counts and find the maximum traffic, and then a pass through the airports to find all airports with the maximum traffic, which cannot be avoided given the problem requirements.

```cpp
#include <vector>
#include <unordered_map>
#include <string>

std::vector<std::string> findAirportsWithMostTraffic(std::vector<std::vector<int>>& flights) {
    std::unordered_map<std::string, int> airportTraffic;
    int maxTraffic = 0;
    
    for (const auto& flight : flights) {
        airportTraffic[flight[0]] += flight[2];
        airportTraffic[flight[1]] += flight[2];
        
        maxTraffic = std::max(maxTraffic, airportTraffic[flight[0]]);
        maxTraffic = std::max(maxTraffic, airportTraffic[flight[1]]);
    }
    
    std::vector<std::string> result;
    for (const auto& pair : airportTraffic) {
        if (pair.second == maxTraffic) {
            result.push_back(pair.first);
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of flights and $m$ is the number of unique airports. This is because we still need to iterate through all flights and then through all airports.
> - **Space Complexity:** $O(m)$ for storing the traffic count of each airport.
> - **Optimality proof:** The approach is optimal because it minimizes the number of iterations required to find the solution, given the need to process each flight and airport at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, dictionary usage for efficient lookups, and optimization by reducing unnecessary iterations.
- Problem-solving patterns identified: Calculating aggregates (traffic counts) and finding maximum values.
- Optimization techniques learned: Combining operations to reduce iterations.
- Similar problems to practice: Other problems involving aggregate calculations and finding maximum or minimum values in a dataset.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize variables, not handling edge cases (like empty input), and not validating inputs.
- Edge cases to watch for: Empty input, flights with zero passengers, and airports with no flights.
- Performance pitfalls: Using inefficient data structures (like lists for lookup-intensive operations) and unnecessary iterations.
- Testing considerations: Thoroughly test with various inputs, including edge cases, to ensure correctness and efficiency.