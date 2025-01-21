## Minimum Number of People to Teach

**Problem Link:** https://leetcode.com/problems/minimum-number-of-people-to-teach/description

**Problem Statement:**
- Input format: `n` (number of people), `languages` (list of languages spoken by each person), `target` (target language)
- Constraints: $1 \leq n \leq 10^5$, $1 \leq m \leq 10^5$ (number of languages), $1 \leq k \leq 10^5$ (number of languages spoken by each person)
- Expected output format: Minimum number of people needed to teach everyone the target language
- Key requirements and edge cases to consider: 
  - A person can speak multiple languages
  - A person can teach others only the languages they speak
  - If a person already speaks the target language, they don't need to be taught
- Example test cases with explanations:
  - Example 1: `n = 2`, `languages = [["english"], ["english", "spanish"]]`, `target = "spanish"` -> `1` (person 2 can teach person 1)
  - Example 2: `n = 3`, `languages = [["english", "spanish"], ["english"], ["spanish"]]`, `target = "english"` -> `0` (everyone already speaks english)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of people to teach and see which combination requires the minimum number of people.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of people.
  2. For each combination, check if everyone in the combination speaks the target language.
  3. If not, try to teach the target language to the people who don't speak it by using the people in the combination who do speak it.
  4. Keep track of the minimum number of people needed to teach everyone the target language.

```cpp
#include <iostream>
#include <vector>
#include <set>
using namespace std;

int minPeopleToTeach(int n, vector<vector<string>>& languages, string target) {
    // Generate all possible combinations of people
    int minPeople = n;
    for (int mask = 0; mask < (1 << n); mask++) {
        // Check if everyone in the combination speaks the target language
        bool everyoneSpeaksTarget = true;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) == 0) {
                bool speaksTarget = false;
                for (const auto& language : languages[i]) {
                    if (language == target) {
                        speaksTarget = true;
                        break;
                    }
                }
                if (!speaksTarget) {
                    everyoneSpeaksTarget = false;
                    break;
                }
            }
        }
        if (everyoneSpeaksTarget) {
            int peopleNeeded = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) == 0) {
                    bool canTeach = false;
                    for (int j = 0; j < n; j++) {
                        if ((mask & (1 << j)) != 0) {
                            for (const auto& language : languages[j]) {
                                if (language == target) {
                                    canTeach = true;
                                    break;
                                }
                            }
                        }
                        if (canTeach) break;
                    }
                    if (!canTeach) peopleNeeded++;
                }
            }
            minPeople = min(minPeople, peopleNeeded);
        }
    }
    return minPeople;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot m)$, where $n$ is the number of people and $m$ is the number of languages spoken by each person. This is because we generate all possible combinations of people and for each combination, we check if everyone speaks the target language.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of people and $m$ is the number of languages spoken by each person. This is because we need to store the languages spoken by each person.
> - **Why these complexities occur:** The time complexity is exponential because we generate all possible combinations of people. The space complexity is linear because we need to store the languages spoken by each person.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a greedy approach to find the minimum number of people needed to teach everyone the target language. We start by selecting the person who speaks the most languages, including the target language. We then remove this person from the list of people who need to be taught. We repeat this process until everyone speaks the target language.
- Detailed breakdown of the approach:
  1. Create a list of people who need to be taught the target language.
  2. Create a list of people who speak the target language.
  3. While there are still people who need to be taught, select the person who speaks the most languages, including the target language.
  4. Remove this person from the list of people who need to be taught.
  5. Repeat steps 3-4 until everyone speaks the target language.

```cpp
#include <iostream>
#include <vector>
#include <set>
#include <map>
using namespace std;

int minPeopleToTeach(int n, vector<vector<string>>& languages, string target) {
    // Create a list of people who need to be taught the target language
    set<int> peopleToTeach;
    for (int i = 0; i < n; i++) {
        bool speaksTarget = false;
        for (const auto& language : languages[i]) {
            if (language == target) {
                speaksTarget = true;
                break;
            }
        }
        if (!speaksTarget) peopleToTeach.insert(i);
    }
    
    // Create a list of people who speak the target language
    set<int> peopleWhoSpeakTarget;
    for (int i = 0; i < n; i++) {
        for (const auto& language : languages[i]) {
            if (language == target) {
                peopleWhoSpeakTarget.insert(i);
                break;
            }
        }
    }
    
    int minPeople = 0;
    while (!peopleToTeach.empty()) {
        // Select the person who speaks the most languages, including the target language
        int maxLanguages = 0;
        int personWithMaxLanguages = -1;
        for (int person : peopleWhoSpeakTarget) {
            int languagesSpoken = languages[person].size();
            if (languagesSpoken > maxLanguages) {
                maxLanguages = languagesSpoken;
                personWithMaxLanguages = person;
            }
        }
        
        // Remove this person from the list of people who need to be taught
        set<int> peopleTaughtByPerson;
        for (int person : peopleToTeach) {
            for (const auto& language : languages[personWithMaxLanguages]) {
                if (language == target) {
                    peopleTaughtByPerson.insert(person);
                    break;
                }
            }
        }
        for (int person : peopleTaughtByPerson) {
            peopleToTeach.erase(person);
        }
        
        // Increment the minimum number of people needed to teach
        minPeople++;
        
        // Update the list of people who speak the target language
        peopleWhoSpeakTarget.erase(personWithMaxLanguages);
        for (int person : peopleTaughtByPerson) {
            peopleWhoSpeakTarget.insert(person);
        }
    }
    return minPeople;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of people and $m$ is the number of languages spoken by each person. This is because we iterate over the people and their languages.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of people and $m$ is the number of languages spoken by each person. This is because we need to store the languages spoken by each person.
> - **Optimality proof:** This solution is optimal because it uses a greedy approach to select the person who speaks the most languages, including the target language. This ensures that we minimize the number of people needed to teach everyone the target language.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, set operations
- Problem-solving patterns identified: Selecting the person who speaks the most languages, including the target language
- Optimization techniques learned: Using a greedy approach to minimize the number of people needed to teach
- Similar problems to practice: [Minimum Number of People to Teach II](https://leetcode.com/problems/minimum-number-of-people-to-teach-ii/description)

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a person already speaks the target language before trying to teach them
- Edge cases to watch for: When there are no people who speak the target language
- Performance pitfalls: Using a brute force approach instead of a greedy approach
- Testing considerations: Test cases where there are multiple people who speak the target language, test cases where there are no people who speak the target language.