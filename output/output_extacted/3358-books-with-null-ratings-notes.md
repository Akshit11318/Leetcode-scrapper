## Books with Null Ratings

**Problem Link:** https://leetcode.com/problems/books-with-null-ratings/description

**Problem Statement:**
- Input format: Two tables, `Books` and `Ratings`, where `Books` contains book information and `Ratings` contains user ratings for books.
- Constraints: 
    - The `Books` table contains columns `book_id` and `name`.
    - The `Ratings` table contains columns `book_id`, `user_id`, and `rating`.
    - There are no duplicate ratings for a user and a book.
- Expected output format: A list of book names that do not have any ratings.
- Key requirements and edge cases to consider: 
    - Handling books without ratings.
    - Ensuring that only books without any ratings are included in the output.

**Example Test Cases:**
- A book without any ratings should be included in the output.
- A book with one or more ratings should not be included in the output.
- If there are no books without ratings, the output should be an empty list.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can iterate over each book in the `Books` table and check if it has any ratings in the `Ratings` table. If a book does not have any ratings, we include it in the output.
- Step-by-step breakdown of the solution:
    1. Initialize an empty list to store the names of books without ratings.
    2. Iterate over each book in the `Books` table.
    3. For each book, iterate over the `Ratings` table to check if the book has any ratings.
    4. If a book does not have any ratings, add its name to the output list.

```cpp
#include <iostream>
#include <vector>
#include <string>

struct Book {
    int book_id;
    std::string name;
};

struct Rating {
    int book_id;
    int user_id;
    int rating;
};

std::vector<std::string> findBooksWithoutRatings(std::vector<Book>& books, std::vector<Rating>& ratings) {
    std::vector<std::string> booksWithoutRatings;

    for (const auto& book : books) {
        bool hasRating = false;
        for (const auto& rating : ratings) {
            if (book.book_id == rating.book_id) {
                hasRating = true;
                break;
            }
        }

        if (!hasRating) {
            booksWithoutRatings.push_back(book.name);
        }
    }

    return booksWithoutRatings;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of books and $m$ is the number of ratings. This is because in the worst case, we might need to iterate over all ratings for each book.
> - **Space Complexity:** $O(n)$, where $n$ is the number of books without ratings. This is because we need to store the names of books without ratings in the output list.
> - **Why these complexities occur:** The brute force approach has high time complexity because it involves nested iteration over the books and ratings tables. The space complexity is relatively low because we only store the names of books without ratings.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `std::unordered_set` to store the IDs of books that have ratings. This allows us to check if a book has a rating in constant time.
- Detailed breakdown of the approach:
    1. Create an `std::unordered_set` to store the IDs of books that have ratings.
    2. Iterate over the ratings and add the book IDs to the set.
    3. Iterate over the books and check if each book's ID is in the set. If not, add the book's name to the output list.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

struct Book {
    int book_id;
    std::string name;
};

struct Rating {
    int book_id;
    int user_id;
    int rating;
};

std::vector<std::string> findBooksWithoutRatings(std::vector<Book>& books, std::vector<Rating>& ratings) {
    std::unordered_set<int> booksWithRatings;
    for (const auto& rating : ratings) {
        booksWithRatings.insert(rating.book_id);
    }

    std::vector<std::string> booksWithoutRatings;
    for (const auto& book : books) {
        if (booksWithRatings.find(book.book_id) == booksWithRatings.end()) {
            booksWithoutRatings.push_back(book.name);
        }
    }

    return booksWithoutRatings;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of books and $m$ is the number of ratings. This is because we iterate over the ratings once to populate the set and then iterate over the books once to find the books without ratings.
> - **Space Complexity:** $O(m)$, where $m$ is the number of ratings. This is because we store the IDs of books with ratings in the set.
> - **Optimality proof:** This approach is optimal because we only iterate over the ratings and books once, and we use a data structure that allows us to check if a book has a rating in constant time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using an `std::unordered_set` to store unique IDs and check for membership in constant time.
- Problem-solving patterns identified: Iterating over data to populate a set and then using the set to filter out unwanted data.
- Optimization techniques learned: Using a data structure with constant-time lookup to improve the efficiency of the algorithm.
- Similar problems to practice: Problems that involve filtering data based on membership in a set.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases, such as an empty input list.
- Edge cases to watch for: Books without ratings, books with multiple ratings, and an empty ratings table.
- Performance pitfalls: Using a data structure with slow lookup times, such as a `std::vector`, to check for membership.
- Testing considerations: Testing the function with different input scenarios, including edge cases, to ensure it produces the correct output.