## Ads Performance
**Problem Link:** https://leetcode.com/problems/ads-performance/description

**Problem Statement:**
- Input format and constraints: The problem involves analyzing the performance of ads based on their click-through rate (`click`) and impression (`impression`) data. The input is a table `Ads` with columns `id`, `click`, and `impression`, where each row represents an ad. The goal is to find the top 3 ads with the highest click-through rate.
- Expected output format: The output should be a table with the `id` of the top 3 ads with the highest click-through rate.
- Key requirements and edge cases to consider: The click-through rate is calculated as the ratio of `click` to `impression`. If two ads have the same click-through rate, they should be ranked based on their `id` in ascending order.
- Example test cases with explanations:
  - If an ad has 0 impressions, its click-through rate should be considered as 0.
  - If two ads have the same click-through rate, the one with the smaller `id` should be ranked higher.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can calculate the click-through rate for each ad and then sort them based on this rate and their `id`.
- Step-by-step breakdown of the solution:
  1. Calculate the click-through rate for each ad.
  2. Sort the ads based on their click-through rate in descending order and then by their `id` in ascending order.
  3. Select the top 3 ads from the sorted list.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

struct Ad {
    int id;
    int click;
    int impression;
    double rate;
};

bool compareAds(const Ad& a, const Ad& b) {
    if (a.rate == b.rate) return a.id < b.id;
    return a.rate > b.rate;
}

vector<int> getTopAds(vector<vector<int>>& ads) {
    vector<Ad> adList;
    for (const auto& ad : ads) {
        Ad newAd;
        newAd.id = ad[0];
        newAd.click = ad[1];
        newAd.impression = ad[2];
        if (newAd.impression == 0) newAd.rate = 0;
        else newAd.rate = (double)newAd.click / newAd.impression;
        adList.push_back(newAd);
    }

    sort(adList.begin(), adList.end(), compareAds);
    vector<int> topAds;
    for (int i = 0; i < 3 && i < adList.size(); i++) {
        topAds.push_back(adList[i].id);
    }
    return topAds;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of ads.
> - **Space Complexity:** $O(n)$ for storing the ads in the `adList` vector.
> - **Why these complexities occur:** The sorting step dominates the time complexity, and the space complexity is due to the additional data structure used to store the ads with their click-through rates.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a custom sorting comparator to directly compare the ads based on their click-through rate and `id` without needing to calculate and store the rate for each ad separately.
- Detailed breakdown of the approach:
  1. Define a custom comparator that compares two ads based on their click-through rate (calculated on the fly) and `id`.
  2. Use this comparator to sort the ads.
  3. Select the top 3 ads from the sorted list.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

bool compareAds(const vector<int>& a, const vector<int>& b) {
    double rateA = a[2] == 0 ? 0 : (double)a[1] / a[2];
    double rateB = b[2] == 0 ? 0 : (double)b[1] / b[2];
    if (rateA == rateB) return a[0] < b[0];
    return rateA > rateB;
}

vector<int> getTopAds(vector<vector<int>>& ads) {
    sort(ads.begin(), ads.end(), compareAds);
    vector<int> topAds;
    for (int i = 0; i < 3 && i < ads.size(); i++) {
        topAds.push_back(ads[i][0]);
    }
    return topAds;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation.
> - **Space Complexity:** $O(1)$ if we consider the input and output as given, since we are sorting in-place.
> - **Optimality proof:** This is the optimal solution because we must at least look at each ad once to determine its click-through rate, and sorting is necessary to find the top 3 ads. The custom comparator allows us to do this in a single pass, minimizing both time and space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Custom sorting comparators, efficient calculation of click-through rates.
- Problem-solving patterns identified: Using sorting to find top items based on a calculated metric.
- Optimization techniques learned: Minimizing unnecessary calculations and memory usage.
- Similar problems to practice: Other ranking or sorting problems based on calculated metrics.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect comparator logic, failure to handle edge cases like zero impressions.
- Edge cases to watch for: Ads with zero impressions, ties in click-through rates.
- Performance pitfalls: Using inefficient sorting algorithms or data structures.
- Testing considerations: Thoroughly testing with various input scenarios, including edge cases.