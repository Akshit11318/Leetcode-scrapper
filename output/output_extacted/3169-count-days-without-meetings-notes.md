## Count Days Without Meetings
**Problem Link:** https://leetcode.com/problems/count-days-without-meetings/description

**Problem Statement:**
- Input: Two arrays `day1` and `day2` representing the start and end days of meetings, respectively.
- Constraints: Each meeting is represented as a pair of integers `[day1[i], day2[i]]`, where `day1[i]` is the start day and `day2[i]` is the end day.
- Expected output: Return the number of days where there are no meetings.
- Key requirements: Meetings can be represented as intervals, and we need to find the days that are not covered by any meeting.
- Example test cases:
  - `day1 = [1,2,3], day2 = [3,4,5]`, Output: `2`
  - `day1 = [1,2,3], day2 = [2,3,4]`, Output: `1`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over all possible days and check if each day falls within any meeting interval.
- Step-by-step breakdown:
  1. Create a set of all days that have meetings.
  2. Iterate over each meeting interval and add all days within the interval to the set.
  3. Count the number of days that are not in the set.
- Why this approach comes to mind first: It's a straightforward way to solve the problem by checking each day individually.

```cpp
int countDaysWithoutMeetings(vector<int>& day1, vector<int>& day2) {
    set<int> daysWithMeetings;
    for (int i = 0; i < day1.size(); i++) {
        for (int j = day1[i]; j <= day2[i]; j++) {
            daysWithMeetings.insert(j);
        }
    }
    int maxDay = *max_element(day2.begin(), day2.end());
    int count = 0;
    for (int i = 1; i <= maxDay; i++) {
        if (daysWithMeetings.find(i) == daysWithMeetings.end()) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m + m \cdot maxDay)$, where $n$ is the number of meetings, $m$ is the average length of a meeting, and $maxDay$ is the maximum end day of all meetings.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of meetings and $m$ is the average length of a meeting.
> - **Why these complexities occur:** The time complexity is due to the nested loops used to add days to the set and count the days without meetings. The space complexity is due to the storage of days in the set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of iterating over all possible days, we can sort the meetings by their end days and use a sweep line approach to count the days without meetings.
- Detailed breakdown:
  1. Sort the meetings by their end days.
  2. Initialize a variable to keep track of the current day and the number of days without meetings.
  3. Iterate over the sorted meetings and update the current day and the count of days without meetings.
- Proof of optimality: This approach has a time complexity of $O(n \log n)$, which is optimal because we need to sort the meetings.

```cpp
int countDaysWithoutMeetings(vector<int>& day1, vector<int>& day2) {
    vector<pair<int, int>> meetings;
    for (int i = 0; i < day1.size(); i++) {
        meetings.push_back({day1[i], day2[i]});
    }
    sort(meetings.begin(), meetings.end(), [](pair<int, int>& a, pair<int, int>& b) {
        return a.second < b.second;
    });
    int currentDay = 1;
    int count = 0;
    for (auto& meeting : meetings) {
        if (currentDay < meeting.first) {
            count += meeting.first - currentDay;
            currentDay = meeting.second + 1;
        } else {
            currentDay = max(currentDay, meeting.second + 1);
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of meetings.
> - **Space Complexity:** $O(n)$, where $n$ is the number of meetings.
> - **Optimality proof:** This approach is optimal because we need to sort the meetings, and the sweep line approach allows us to count the days without meetings in a single pass.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Sorting, sweep line approach.
- Problem-solving patterns: Using a sweep line approach to count days without meetings.
- Optimization techniques: Sorting the meetings by their end days to reduce the time complexity.

**Mistakes to Avoid:**
- Not sorting the meetings, which can lead to incorrect results.
- Not using a sweep line approach, which can lead to inefficient counting of days without meetings.
- Not handling edge cases, such as meetings that start and end on the same day.