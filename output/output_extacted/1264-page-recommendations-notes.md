## Page Recommendations

**Problem Link:** [https://leetcode.com/problems/page-recommendations/description](https://leetcode.com/problems/page-recommendations/description)

**Problem Statement:**
- Input format: `user_id`, `page_id`, and `liked` status.
- Expected output format: List of recommended page IDs for each user.
- Key requirements and edge cases to consider: 
    - Users who have liked at least one page.
    - Pages that have been liked by at least one user.
- Example test cases with explanations:
    - User A likes pages 1 and 2, user B likes pages 2 and 3. The recommended pages for user A should include page 3.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Calculate the similarity between each pair of users based on their liked pages.
- Step-by-step breakdown of the solution:
    1. Create a map to store the pages liked by each user.
    2. Iterate over each pair of users and calculate the similarity between them using the Jaccard similarity coefficient.
    3. For each user, find the top N most similar users.
    4. Recommend pages liked by the top N most similar users.
- Why this approach comes to mind first: It's a straightforward way to calculate the similarity between users based on their liked pages.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>

using namespace std;

vector<int> bruteForce(vector<int>& user_id, vector<int>& page_id, vector<int>& liked) {
    unordered_map<int, set<int>> userPages;
    for (int i = 0; i < user_id.size(); i++) {
        if (liked[i] == 1) {
            userPages[user_id[i]].insert(page_id[i]);
        }
    }

    unordered_map<int, vector<int>> recommendations;
    for (auto& user : userPages) {
        vector<int> similarUsers;
        for (auto& otherUser : userPages) {
            if (user.first != otherUser.first) {
                set<int> intersection;
                set<int> unionSet;
                for (int page : user.second) {
                    unionSet.insert(page);
                }
                for (int page : otherUser.second) {
                    unionSet.insert(page);
                    if (user.second.find(page) != user.second.end()) {
                        intersection.insert(page);
                    }
                }
                double similarity = (double)intersection.size() / unionSet.size();
                if (similarity > 0) {
                    similarUsers.push_back(otherUser.first);
                }
            }
        }
        set<int> recommendedPages;
        for (int similarUser : similarUsers) {
            for (int page : userPages[similarUser]) {
                if (userPages[user.first].find(page) == userPages[user.first].end()) {
                    recommendedPages.insert(page);
                }
            }
        }
        recommendations[user.first] = vector<int>(recommendedPages.begin(), recommendedPages.end());
    }
    return vector<int>();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the number of users and $m$ is the average number of pages liked by each user.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of users and $m$ is the average number of pages liked by each user.
> - **Why these complexities occur:** The brute force approach involves iterating over each pair of users and calculating the similarity between them, resulting in a quadratic time complexity. The space complexity is linear with respect to the number of users and pages.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a collaborative filtering approach to recommend pages based on the preferences of similar users.
- Detailed breakdown of the approach:
    1. Create a user-item matrix where each row represents a user and each column represents a page.
    2. Use a matrix factorization technique (e.g., SVD) to reduce the dimensionality of the user-item matrix.
    3. Calculate the similarity between users based on their latent factors.
    4. Recommend pages liked by the top N most similar users.
- Proof of optimality: This approach is optimal because it reduces the dimensionality of the user-item matrix, making it more efficient to calculate the similarity between users.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>
#include <Eigen/Dense>

using namespace std;
using namespace Eigen;

vector<int> optimal(vector<int>& user_id, vector<int>& page_id, vector<int>& liked) {
    unordered_map<int, set<int>> userPages;
    for (int i = 0; i < user_id.size(); i++) {
        if (liked[i] == 1) {
            userPages[user_id[i]].insert(page_id[i]);
        }
    }

    int numUsers = userPages.size();
    int numPages = 0;
    for (auto& user : userPages) {
        numPages = max(numPages, *user.second.rbegin());
    }
    numPages++;

    MatrixXd userItemMatrix(numUsers, numPages);
    userItemMatrix.setZero();
    int userIdx = 0;
    for (auto& user : userPages) {
        for (int page : user.second) {
            userItemMatrix(userIdx, page) = 1;
        }
        userIdx++;
    }

    // Perform SVD on the user-item matrix
    JacobiSVD<MatrixXd> svd(userItemMatrix, ComputeThinU | ComputeThinV);
    MatrixXd U = svd.matrixU();
    MatrixXd V = svd.matrixV();

    // Calculate the similarity between users based on their latent factors
    MatrixXd similarityMatrix = U * U.transpose();

    // Recommend pages liked by the top N most similar users
    int N = 10; // number of similar users to consider
    vector<int> recommendations;
    for (int i = 0; i < numUsers; i++) {
        vector<pair<int, double>> similarUsers;
        for (int j = 0; j < numUsers; j++) {
            if (i != j) {
                similarUsers.push_back(make_pair(j, similarityMatrix(i, j)));
            }
        }
        sort(similarUsers.begin(), similarUsers.end(), [](const pair<int, double>& a, const pair<int, double>& b) {
            return a.second > b.second;
        });
        set<int> recommendedPages;
        for (int k = 0; k < N; k++) {
            int similarUser = similarUsers[k].first;
            for (int page : userPages[similarUser + 1]) {
                if (userPages[i + 1].find(page) == userPages[i + 1].end()) {
                    recommendedPages.insert(page);
                }
            }
        }
        recommendations.insert(recommendations.end(), recommendedPages.begin(), recommendedPages.end());
    }
    return recommendations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m + n^2 \cdot k)$, where $n$ is the number of users, $m$ is the number of pages, and $k$ is the number of latent factors.
> - **Space Complexity:** $O(n \cdot m + n \cdot k)$, where $n$ is the number of users, $m$ is the number of pages, and $k$ is the number of latent factors.
> - **Optimality proof:** This approach is optimal because it reduces the dimensionality of the user-item matrix using SVD, making it more efficient to calculate the similarity between users.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Collaborative filtering, SVD, and matrix factorization.
- Problem-solving patterns identified: Reducing dimensionality to improve efficiency.
- Optimization techniques learned: Using SVD to reduce the dimensionality of the user-item matrix.
- Similar problems to practice: Recommendation systems, collaborative filtering, and matrix factorization.

**Mistakes to Avoid:**
- Common implementation errors: Not handling missing values in the user-item matrix.
- Edge cases to watch for: Users with no liked pages, pages with no liked users.
- Performance pitfalls: Using a brute force approach to calculate the similarity between users.
- Testing considerations: Evaluating the performance of the recommendation system using metrics such as precision, recall, and F1 score.