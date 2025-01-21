## Human Traffic of Stadium
**Problem Link:** https://leetcode.com/problems/human-traffic-of-stadium/description

**Problem Statement:**
- Input format: A list of `stadium` records, each containing `id`, `visit_date`, `event_date`, `state`, `people`.
- Constraints: 
  - `stadium` contains at most `10000` records.
  - `id` is unique.
  - `visit_date` and `event_date` are in the format `YYYY-MM-DD`.
  - `state` is either `'id'`, `'name'`, or `'department'`.
  - `people` is an integer between `1` and `100000`.
- Expected output format: The number of visitors on the day of the event for each row.
- Key requirements and edge cases to consider: 
  - The number of visitors is the sum of `people` for all rows with the same `visit_date` and `event_date`.
  - The event date is the same as the visit date.
- Example test cases with explanations:
  - Example 1:
    - Input: `stadium = [["2016-03-15","2016-03-15","CA","10"],["2016-03-15","2016-03-15","CA","10"],["2017-06-11","2017-06-11","NY","5"],["2017-06-11","2017-06-11","NY","5"]]`
    - Output: `20, 20, 10, 10`
    - Explanation: For the first two rows, the visit date and event date are both "2016-03-15", and the number of visitors is 10 + 10 = 20. For the last two rows, the visit date and event date are both "2017-06-11", and the number of visitors is 5 + 5 = 10.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Calculate the total number of visitors for each row by summing up `people` for all rows with the same `visit_date` and `event_date`.
- Step-by-step breakdown of the solution:
  1. Create a dictionary to store the sum of `people` for each `visit_date` and `event_date`.
  2. Iterate over each row in the `stadium` list.
  3. For each row, check if the `visit_date` and `event_date` are already in the dictionary. If they are, add the `people` to the existing sum. If not, add a new entry to the dictionary with the `people` as the sum.
  4. After iterating over all rows, iterate over the `stadium` list again and calculate the total number of visitors for each row by looking up the sum in the dictionary.

```cpp
#include <vector>
#include <map>
#include <string>

using namespace std;

vector<int> stadium(vector<vector<string>>& stadium) {
    map<pair<string, string>, int> people_sum;
    for (auto& row : stadium) {
        string visit_date = row[0];
        string event_date = row[1];
        int people = stoi(row[4]);
        if (people_sum.find({visit_date, event_date}) != people_sum.end()) {
            people_sum[{visit_date, event_date}] += people;
        } else {
            people_sum[{visit_date, event_date}] = people;
        }
    }
    vector<int> result;
    for (auto& row : stadium) {
        string visit_date = row[0];
        string event_date = row[1];
        result.push_back(people_sum[{visit_date, event_date}]);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `stadium` list. This is because we iterate over the list twice: once to calculate the sum of `people` for each `visit_date` and `event_date`, and once to calculate the total number of visitors for each row.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique `visit_date` and `event_date` pairs. This is because we use a dictionary to store the sum of `people` for each `visit_date` and `event_date`.
> - **Why these complexities occur:** The time complexity occurs because we iterate over the list twice, and the space complexity occurs because we use a dictionary to store the sum of `people` for each `visit_date` and `event_date`.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a single pass over the `stadium` list to calculate the sum of `people` for each `visit_date` and `event_date`, and then use another pass to calculate the total number of visitors for each row.
- Detailed breakdown of the approach:
  1. Create a dictionary to store the sum of `people` for each `visit_date` and `event_date`.
  2. Iterate over each row in the `stadium` list, and for each row, add the `people` to the sum in the dictionary.
  3. After iterating over all rows, iterate over the `stadium` list again and calculate the total number of visitors for each row by looking up the sum in the dictionary.

```cpp
#include <vector>
#include <map>
#include <string>

using namespace std;

vector<int> stadium(vector<vector<string>>& stadium) {
    map<pair<string, string>, int> people_sum;
    for (auto& row : stadium) {
        string visit_date = row[0];
        string event_date = row[1];
        int people = stoi(row[4]);
        people_sum[{visit_date, event_date}] += people;
    }
    vector<int> result;
    for (auto& row : stadium) {
        string visit_date = row[0];
        string event_date = row[1];
        result.push_back(people_sum[{visit_date, event_date}]);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the `stadium` list. This is because we iterate over the list twice: once to calculate the sum of `people` for each `visit_date` and `event_date`, and once to calculate the total number of visitors for each row.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique `visit_date` and `event_date` pairs. This is because we use a dictionary to store the sum of `people` for each `visit_date` and `event_date`.
> - **Optimality proof:** This is the optimal solution because we only iterate over the list twice, and we use a dictionary to store the sum of `people` for each `visit_date` and `event_date`, which allows us to look up the sum in constant time.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Using a dictionary to store the sum of `people` for each `visit_date` and `event_date`, and iterating over the list twice to calculate the total number of visitors for each row.
- Problem-solving patterns identified: Using a dictionary to store intermediate results and iterating over the list multiple times to calculate the final result.
- Optimization techniques learned: Using a dictionary to store the sum of `people` for each `visit_date` and `event_date`, which allows us to look up the sum in constant time.
- Similar problems to practice: Problems that involve using a dictionary to store intermediate results and iterating over a list multiple times to calculate the final result.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dictionary before using it, and not checking if the `visit_date` and `event_date` are already in the dictionary before adding the `people` to the sum.
- Edge cases to watch for: The `visit_date` and `event_date` may be the same, and the `people` may be zero.
- Performance pitfalls: Iterating over the list multiple times without using a dictionary to store intermediate results, which can lead to a time complexity of $O(n^2)$.
- Testing considerations: Test the solution with different inputs, including edge cases, to ensure that it produces the correct output.