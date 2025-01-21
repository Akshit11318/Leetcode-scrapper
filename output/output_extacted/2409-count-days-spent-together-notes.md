## Count Days Spent Together

**Problem Link:** https://leetcode.com/problems/count-days-spent-together/description

**Problem Statement:**
- Input format: Two arrays `arr1` and `arr2` representing the days when two people are together, with `m` and `n` elements respectively.
- Constraints: `1 <= m, n <= 10^5`, `1 <= arr1[i], arr2[j] <= 10^6`.
- Expected output format: The number of days the two people are together.
- Key requirements and edge cases to consider: Days are counted from `1` to `10^6`, and the two people are together only on days when both are present.

**Example Test Cases:**
- `arr1 = [1,2,3]`, `arr2 = [2,3,4]`, Output: `2`
- `arr1 = [1,2,3]`, `arr2 = [4,5,6]`, Output: `0`

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through all days from `1` to `10^6` and check if both people are present on each day.
- We create two sets from the input arrays to efficiently check for presence.

```cpp
class Solution {
public:
    int countDaysTogether(string arrivalDay1, string departureDay1, string arrivalDay2, string departureDay2) {
        int m = 0, n = 0, p = 0, q = 0;
        string months = "031012042053055036037038039040041042043044045046047048049050051052053054055056057058059060061062063064065066067068069070071072073074075076077078079080081082083084085086087088089090091092093094095096097098099100101102103104105106107108109110111112";
        for (int i = 0; i < 12; i++) {
            string a = months.substr(i * 3, 3);
            if (a == arrivalDay1.substr(0, 3)) m = i;
            if (a == departureDay1.substr(0, 3)) n = i;
            if (a == arrivalDay2.substr(0, 3)) p = i;
            if (a == departureDay2.substr(0, 3)) q = i;
        }
        int start = max(m, p);
        int end = min(n, q);
        if (start > end) return 0;
        int days = 0;
        for (int i = start; i <= end; i++) {
            int a = stoi(arrivalDay1.substr(3)) + (i - m) * 30;
            int b = stoi(departureDay1.substr(3)) + (i - m) * 30;
            int c = stoi(arrivalDay2.substr(3)) + (i - p) * 30;
            int d = stoi(departureDay2.substr(3)) + (i - p) * 30;
            if (a <= d && c <= b) {
                days += min(b, d) - max(a, c) + 1;
            }
        }
        return days;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, as we are only iterating through a fixed number of months and days.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the months and the input arrays.
> - **Why these complexities occur:** The time and space complexities are constant because we are dealing with a fixed number of months and days, and we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to calculate the start and end days of the overlap between the two people's stays.
- We can do this by finding the maximum of the two start days and the minimum of the two end days.

```cpp
class Solution {
public:
    int countDaysTogether(string arrivalDay1, string departureDay1, string arrivalDay2, string departureDay2) {
        int m = 0, n = 0, p = 0, q = 0;
        string months = "031012042053055036037038039040041042043044045046047048049050051052053054055056057058059060061062063064065066067068069070071072073074075076077078079080081082083084085086087088089090091092093094095096097098099100101102103104105106107108109110111112";
        for (int i = 0; i < 12; i++) {
            string a = months.substr(i * 3, 3);
            if (a == arrivalDay1.substr(0, 3)) m = i;
            if (a == departureDay1.substr(0, 3)) n = i;
            if (a == arrivalDay2.substr(0, 3)) p = i;
            if (a == departureDay2.substr(0, 3)) q = i;
        }
        int start = max(m, p);
        int end = min(n, q);
        if (start > end) return 0;
        int days = 0;
        for (int i = start; i <= end; i++) {
            int a = stoi(arrivalDay1.substr(3)) + (i - m) * 30;
            int b = stoi(departureDay1.substr(3)) + (i - m) * 30;
            int c = stoi(arrivalDay2.substr(3)) + (i - p) * 30;
            int d = stoi(departureDay2.substr(3)) + (i - p) * 30;
            if (a <= d && c <= b) {
                days += min(b, d) - max(a, c) + 1;
            }
        }
        return days;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$, as we are only iterating through a fixed number of months and days.
> - **Space Complexity:** $O(1)$, as we are using a constant amount of space to store the months and the input arrays.
> - **Optimality proof:** This solution is optimal because we are directly calculating the overlap between the two people's stays, without using any unnecessary data structures or operations.

---

### Final Notes

**Learning Points:**
- The key to solving this problem is to calculate the start and end days of the overlap between the two people's stays.
- We can use a constant amount of space to store the months and the input arrays, making the space complexity $O(1)$.
- The time complexity is also $O(1)$, as we are only iterating through a fixed number of months and days.

**Mistakes to Avoid:**
- Not accounting for the months and days correctly, leading to incorrect calculations.
- Using unnecessary data structures or operations, leading to increased time and space complexities.
- Not checking for edge cases, such as when the two people do not overlap at all.