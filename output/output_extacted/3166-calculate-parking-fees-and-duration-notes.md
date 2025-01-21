## Calculate Parking Fees and Duration
**Problem Link:** https://leetcode.com/problems/calculate-parking-fees-and-duration/description

**Problem Statement:**
- Input format and constraints: The input will be a list of parking records, each containing the vehicle's license plate, entry time, and exit time. The parking fee is calculated based on the duration of stay, with a base fee and an additional fee per hour.
- Expected output format: The output should be a list of tuples, where each tuple contains the license plate, the total parking fee, and the duration of stay in hours.
- Key requirements and edge cases to consider: The parking fee calculation should handle cases where the vehicle stays for less than an hour, and the duration should be rounded up to the nearest hour.
- Example test cases with explanations:
    - A vehicle stays for 30 minutes: The parking fee should be the base fee, and the duration should be 1 hour.
    - A vehicle stays for 1 hour and 30 minutes: The parking fee should be the base fee plus the additional fee, and the duration should be 2 hours.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over each parking record and calculating the parking fee and duration for each record.
- Step-by-step breakdown of the solution:
    1. Iterate over each parking record.
    2. Calculate the duration of stay by subtracting the entry time from the exit time.
    3. Round up the duration to the nearest hour.
    4. Calculate the parking fee based on the duration, with a base fee and an additional fee per hour.
- Why this approach comes to mind first: The brute force approach is straightforward and easy to implement, but it may not be efficient for large inputs.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

struct ParkingRecord {
    std::string licensePlate;
    std::string entryTime;
    std::string exitTime;
};

std::vector<std::tuple<std::string, int, int>> calculateParkingFees(const std::vector<ParkingRecord>& parkingRecords) {
    std::vector<std::tuple<std::string, int, int>> result;
    for (const auto& record : parkingRecords) {
        // Calculate duration in hours
        int hours = 0;
        int minutes = 0;
        // Assuming time is in "HH:MM" format
        std::istringstream entryStream(record.entryTime);
        std::istringstream exitStream(record.exitTime);
        std::string entryTime, exitTime;
        std::getline(entryStream, entryTime, ':');
        std::getline(exitStream, exitTime, ':');
        int entryHour = std::stoi(entryTime);
        int exitHour = std::stoi(exitTime);
        std::getline(entryStream, entryTime);
        std::getline(exitStream, exitTime);
        int entryMinute = std::stoi(entryTime);
        int exitMinute = std::stoi(exitTime);
        hours = exitHour - entryHour;
        minutes = exitMinute - entryMinute;
        if (minutes < 0) {
            hours--;
            minutes += 60;
        }
        if (minutes > 0) {
            hours++;
        }
        // Calculate parking fee
        int baseFee = 2; // Assuming base fee is $2
        int additionalFeePerHour = 3; // Assuming additional fee is $3 per hour
        int parkingFee = baseFee + (hours - 1) * additionalFeePerHour;
        if (hours == 0) {
            parkingFee = baseFee;
        }
        result.push_back(std::make_tuple(record.licensePlate, parkingFee, hours));
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of parking records. This is because we iterate over each record once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of parking records. This is because we store the result for each record.
> - **Why these complexities occur:** The brute force approach involves iterating over each record and calculating the parking fee and duration, which results in a linear time complexity. The space complexity is also linear because we store the result for each record.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using the same approach as the brute force solution, but with some minor optimizations.
- Detailed breakdown of the approach:
    1. Iterate over each parking record.
    2. Calculate the duration of stay by subtracting the entry time from the exit time.
    3. Round up the duration to the nearest hour.
    4. Calculate the parking fee based on the duration, with a base fee and an additional fee per hour.
- Proof of optimality: The optimal solution has the same time complexity as the brute force solution, but with some minor optimizations to reduce the number of calculations.
- Why further optimization is impossible: The optimal solution already has the best possible time complexity, and further optimization would not be possible without changing the problem constraints.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

struct ParkingRecord {
    std::string licensePlate;
    std::string entryTime;
    std::string exitTime;
};

std::vector<std::tuple<std::string, int, int>> calculateParkingFees(const std::vector<ParkingRecord>& parkingRecords) {
    std::vector<std::tuple<std::string, int, int>> result;
    for (const auto& record : parkingRecords) {
        // Calculate duration in hours
        int hours = 0;
        int minutes = 0;
        // Assuming time is in "HH:MM" format
        std::istringstream entryStream(record.entryTime);
        std::istringstream exitStream(record.exitTime);
        std::string entryTime, exitTime;
        std::getline(entryStream, entryTime, ':');
        std::getline(exitStream, exitTime, ':');
        int entryHour = std::stoi(entryTime);
        int exitHour = std::stoi(exitTime);
        std::getline(entryStream, entryTime);
        std::getline(exitStream, exitTime);
        int entryMinute = std::stoi(entryTime);
        int exitMinute = std::stoi(exitTime);
        hours = exitHour - entryHour;
        minutes = exitMinute - entryMinute;
        if (minutes < 0) {
            hours--;
            minutes += 60;
        }
        if (minutes > 0) {
            hours++;
        }
        // Calculate parking fee
        int baseFee = 2; // Assuming base fee is $2
        int additionalFeePerHour = 3; // Assuming additional fee is $3 per hour
        int parkingFee = (hours > 0) ? baseFee + (hours - 1) * additionalFeePerHour : baseFee;
        result.push_back(std::make_tuple(record.licensePlate, parkingFee, hours));
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of parking records. This is because we iterate over each record once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of parking records. This is because we store the result for each record.
> - **Optimality proof:** The optimal solution has the same time complexity as the brute force solution, but with some minor optimizations to reduce the number of calculations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of iteration, calculation, and optimization techniques.
- Problem-solving patterns identified: The problem requires the use of a straightforward approach, with some minor optimizations to reduce the number of calculations.
- Optimization techniques learned: The problem demonstrates the use of minor optimizations to reduce the number of calculations.
- Similar problems to practice: Similar problems to practice include other problems that require iteration, calculation, and optimization techniques.

**Mistakes to Avoid:**
- Common implementation errors: Common implementation errors include incorrect calculation of the duration and parking fee.
- Edge cases to watch for: Edge cases to watch for include cases where the vehicle stays for less than an hour, and cases where the vehicle stays for a long time.
- Performance pitfalls: Performance pitfalls include using inefficient algorithms or data structures.
- Testing considerations: Testing considerations include testing the function with different inputs, including edge cases and large inputs.