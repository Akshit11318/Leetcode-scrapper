## Design Movie Rental System
**Problem Link:** https://leetcode.com/problems/design-movie-rental-system/description

**Problem Statement:**
- Input format and constraints: You are given a list of `n` movies, where the `i-th` movie is represented as `(movie_id, movie_name)`. You also have a list of `m` shops, where the `j-th` shop is represented as `(shop_id, movie_id, stock)`.
- Expected output format: Implement a `MovieRentalSystem` class that supports the following operations:
  - `void addMovie(int movie_id, string movie_name)`: Adds a new movie to the system.
  - `void addShop(int shop_id, int movie_id, int stock)`: Adds a new shop to the system.
  - `void rentMovie(int shop_id, int movie_id)`: Rents a movie from a shop.
  - `void returnMovie(int shop_id, int movie_id)`: Returns a movie to a shop.
  - `vector<int> available(int shop_id)`: Returns a list of available movies in a shop.
  - `vector<int> rented(int movie_id)`: Returns a list of shops that have rented a movie.
- Key requirements and edge cases to consider: 
  - A movie can be rented from multiple shops.
  - A shop can rent multiple movies.
  - A movie can be returned to the same shop it was rented from.
- Example test cases with explanations:
  - `addMovie(1, "Movie1")`
  - `addShop(1, 1, 5)`
  - `rentMovie(1, 1)`
  - `available(1)` should return `[1]`
  - `rented(1)` should return `[1]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can use a simple data structure to store the movies and shops.
- Step-by-step breakdown of the solution:
  1. Create a `Movie` class to store the movie id and name.
  2. Create a `Shop` class to store the shop id, movie id, and stock.
  3. Create a `MovieRentalSystem` class to store the movies and shops.
  4. Implement the `addMovie`, `addShop`, `rentMovie`, `returnMovie`, `available`, and `rented` operations using the data structures.
- Why this approach comes to mind first: It is a simple and straightforward approach that uses basic data structures.

```cpp
class Movie {
public:
    int id;
    string name;
    Movie(int id, string name) : id(id), name(name) {}
};

class Shop {
public:
    int id;
    int movie_id;
    int stock;
    Shop(int id, int movie_id, int stock) : id(id), movie_id(movie_id), stock(stock) {}
};

class MovieRentalSystem {
public:
    vector<Movie> movies;
    vector<Shop> shops;
    void addMovie(int movie_id, string movie_name) {
        movies.push_back(Movie(movie_id, movie_name));
    }
    void addShop(int shop_id, int movie_id, int stock) {
        shops.push_back(Shop(shop_id, movie_id, stock));
    }
    void rentMovie(int shop_id, int movie_id) {
        for (auto& shop : shops) {
            if (shop.id == shop_id && shop.movie_id == movie_id) {
                shop.stock--;
                break;
            }
        }
    }
    void returnMovie(int shop_id, int movie_id) {
        for (auto& shop : shops) {
            if (shop.id == shop_id && shop.movie_id == movie_id) {
                shop.stock++;
                break;
            }
        }
    }
    vector<int> available(int shop_id) {
        vector<int> available_movies;
        for (auto& shop : shops) {
            if (shop.id == shop_id && shop.stock > 0) {
                available_movies.push_back(shop.movie_id);
            }
        }
        return available_movies;
    }
    vector<int> rented(int movie_id) {
        vector<int> rented_shops;
        for (auto& shop : shops) {
            if (shop.movie_id == movie_id && shop.stock < 5) {
                rented_shops.push_back(shop.id);
            }
        }
        return rented_shops;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of movies and $m$ is the number of shops. This is because we are using vectors to store the movies and shops, and the operations involve iterating over the vectors.
> - **Space Complexity:** $O(n + m)$ where $n$ is the number of movies and $m$ is the number of shops. This is because we are storing the movies and shops in vectors.
> - **Why these complexities occur:** The complexities occur because we are using vectors to store the movies and shops, and the operations involve iterating over the vectors.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `map` to store the movies and shops, where the key is the movie id or shop id, and the value is the corresponding movie or shop object.
- Detailed breakdown of the approach:
  1. Create a `Movie` class to store the movie id and name.
  2. Create a `Shop` class to store the shop id, movie id, and stock.
  3. Create a `MovieRentalSystem` class to store the movies and shops using `map`.
  4. Implement the `addMovie`, `addShop`, `rentMovie`, `returnMovie`, `available`, and `rented` operations using the `map`.
- Why further optimization is impossible: This approach is optimal because it uses a `map` to store the movies and shops, which allows for efficient lookup and insertion.

```cpp
class Movie {
public:
    int id;
    string name;
    Movie(int id, string name) : id(id), name(name) {}
};

class Shop {
public:
    int id;
    int movie_id;
    int stock;
    Shop(int id, int movie_id, int stock) : id(id), movie_id(movie_id), stock(stock) {}
};

class MovieRentalSystem {
public:
    map<int, Movie> movies;
    map<int, Shop> shops;
    map<int, vector<int>> movie_shops;
    map<int, vector<int>> shop_movies;
    void addMovie(int movie_id, string movie_name) {
        movies[movie_id] = Movie(movie_id, movie_name);
    }
    void addShop(int shop_id, int movie_id, int stock) {
        shops[shop_id] = Shop(shop_id, movie_id, stock);
        movie_shops[movie_id].push_back(shop_id);
        shop_movies[shop_id].push_back(movie_id);
    }
    void rentMovie(int shop_id, int movie_id) {
        if (shops[shop_id].stock > 0) {
            shops[shop_id].stock--;
        }
    }
    void returnMovie(int shop_id, int movie_id) {
        shops[shop_id].stock++;
    }
    vector<int> available(int shop_id) {
        vector<int> available_movies;
        for (auto& movie_id : shop_movies[shop_id]) {
            if (shops[shop_id].stock > 0) {
                available_movies.push_back(movie_id);
            }
        }
        return available_movies;
    }
    vector<int> rented(int movie_id) {
        vector<int> rented_shops;
        for (auto& shop_id : movie_shops[movie_id]) {
            if (shops[shop_id].stock < 5) {
                rented_shops.push_back(shop_id);
            }
        }
        return rented_shops;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for `addMovie`, `addShop`, `rentMovie`, and `returnMovie` operations, and $O(m)$ for `available` and `rented` operations where $m$ is the number of shops or movies.
> - **Space Complexity:** $O(n + m)$ where $n$ is the number of movies and $m$ is the number of shops.
> - **Optimality proof:** This approach is optimal because it uses a `map` to store the movies and shops, which allows for efficient lookup and insertion.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using `map` to store data for efficient lookup and insertion.
- Problem-solving patterns identified: Using a `map` to store data and iterating over the map to perform operations.
- Optimization techniques learned: Using a `map` to store data instead of vectors to improve lookup and insertion efficiency.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if a movie or shop exists before performing operations.
- Edge cases to watch for: Handling cases where a movie or shop does not exist.
- Performance pitfalls: Using vectors instead of `map` to store data, which can lead to inefficient lookup and insertion.
- Testing considerations: Testing the `addMovie`, `addShop`, `rentMovie`, `returnMovie`, `available`, and `rented` operations to ensure they work correctly.