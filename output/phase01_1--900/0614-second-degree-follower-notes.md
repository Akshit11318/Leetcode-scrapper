## Second Degree Follower
**Problem Link:** https://leetcode.com/problems/second-degree-follower/description

**Problem Statement:**
- Input format: A table `follow` with columns `follower` and `followee`.
- Constraints: The table has no primary key, and each row may contain duplicate values.
- Expected output format: A table with `id` as the column name, containing the ids of all second-degree followers.
- Key requirements and edge cases to consider:
  - A second-degree follower is someone who follows a person who follows the target person.
  - The target person is not specified, so the solution must be generalizable to all possible target persons.
- Example test cases with explanations:
  - If the table contains `(1, 2)`, `(2, 3)`, and `(1, 3)`, then `1` is a first-degree follower of `2` and `3`, and a second-degree follower of `3`.
  - If the table contains `(1, 2)`, `(2, 3)`, and `(3, 4)`, then `1` is a second-degree follower of `3`, and a third-degree follower of `4`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over the table to find all pairs of followers and followees, then iterate again to find second-degree followers.
- Step-by-step breakdown of the solution:
  1. Create a set to store all second-degree followers.
  2. Iterate over the table to find all pairs of followers and followees.
  3. For each pair, iterate over the table again to find all second-degree followers.
  4. Add the second-degree followers to the set.
- Why this approach comes to mind first: It is a straightforward, naive solution that checks every possible combination of followers and followees.

```cpp
#include <iostream>
#include <set>
#include <vector>

using namespace std;

struct Follow {
    int follower;
    int followee;
};

void findSecondDegreeFollowers(vector<Follow>& follows) {
    set<int> secondDegreeFollowers;
    for (const auto& follow1 : follows) {
        for (const auto& follow2 : follows) {
            if (follow1.followee == follow2.follower) {
                secondDegreeFollowers.insert(follow1.follower);
            }
        }
    }

    // Print the second-degree followers
    for (const auto& id : secondDegreeFollowers) {
        cout << id << endl;
    }
}

int main() {
    vector<Follow> follows = {{1, 2}, {2, 3}, {1, 3}};
    findSecondDegreeFollowers(follows);
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of rows in the table, because we are iterating over the table twice.
> - **Space Complexity:** $O(n)$, where $n$ is the number of rows in the table, because we are storing all second-degree followers in a set.
> - **Why these complexities occur:** The brute force approach has high time complexity because it checks every possible combination of followers and followees, resulting in a quadratic number of operations. The space complexity is linear because we are storing all second-degree followers in a set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a hash map to store the followers for each person, and then iterate over the table to find second-degree followers.
- Detailed breakdown of the approach:
  1. Create a hash map to store the followers for each person.
  2. Iterate over the table to populate the hash map.
  3. Iterate over the table again to find second-degree followers.
  4. For each pair, check if the followee is in the hash map, and if so, add the follower to the set of second-degree followers.
- Proof of optimality: This approach has a time complexity of $O(n)$, which is the best possible time complexity because we must iterate over the table at least once.

```cpp
#include <iostream>
#include <set>
#include <vector>
#include <unordered_map>

using namespace std;

struct Follow {
    int follower;
    int followee;
};

void findSecondDegreeFollowers(vector<Follow>& follows) {
    unordered_map<int, set<int>> followers;
    set<int> secondDegreeFollowers;

    // Populate the hash map
    for (const auto& follow : follows) {
        followers[follow.followee].insert(follow.follower);
    }

    // Find second-degree followers
    for (const auto& follow : follows) {
        if (followers.find(follow.followee) != followers.end()) {
            for (const auto& secondDegreeFollower : followers[follow.followee]) {
                if (followers.find(secondDegreeFollower) != followers.end()) {
                    secondDegreeFollowers.insert(secondDegreeFollower);
                }
            }
        }
    }

    // Print the second-degree followers
    for (const auto& id : secondDegreeFollowers) {
        cout << id << endl;
    }
}

int main() {
    vector<Follow> follows = {{1, 2}, {2, 3}, {1, 3}};
    findSecondDegreeFollowers(follows);
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the table, because we are iterating over the table twice.
> - **Space Complexity:** $O(n)$, where $n$ is the number of rows in the table, because we are storing all followers in a hash map.
> - **Optimality proof:** This approach has the best possible time complexity because we must iterate over the table at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash maps, sets, and iteration.
- Problem-solving patterns identified: Using hash maps to store data and iterating over tables to find relationships.
- Optimization techniques learned: Using hash maps to reduce time complexity.
- Similar problems to practice: Finding third-degree followers, finding common followers, and finding followers with specific properties.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for duplicate values, not handling edge cases, and not optimizing the solution.
- Edge cases to watch for: Empty tables, tables with duplicate values, and tables with no followers.
- Performance pitfalls: Using brute force approaches, not optimizing the solution, and not using hash maps.
- Testing considerations: Testing with empty tables, tables with duplicate values, and tables with no followers.