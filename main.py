import json
import statistics

FILE_NAME = "movies.json"


def load_movies(file_name):
    """
    Loads movies data from a file.

    Args:
        file_name (str): The name of the file containing movies data.

    Returns:
        dict: A dictionary of movies or an empty dictionary if the file doesn't exist or is invalid.
    """
    try:
        with open(file_name, 'r') as file:
            movies = json.load(file)
            if not isinstance(movies, dict):
                print("Data format error. Resetting to an empty dictionary.")
                return {}
            return movies
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_movies(file_name, movies):
    """
    Saves movies data to a file.

    Args:
        file_name (str): The name of the file to save movies data.
        movies (dict): A dictionary of movies to save.
    """
    try:
        with open(file_name, 'w') as file:
            json.dump(movies, file, indent=4)
    except IOError:
        print("Error saving movies. Please try again.")


def add_movie(movies):
    """
    Adds a new movie to the collection.

    Args:
        movies (dict): The current dictionary of movies.
    """
    title = input("Enter movie title: ").strip()
    while not title:
        title = input("Title cannot be empty. Enter movie title: ").strip()

    try:
        rating = float(input("Enter movie rating (0.0 - 10.0): "))
        if not 0.0 <= rating <= 10.0:
            raise ValueError
    except ValueError:
        print("Invalid rating. Please enter a number between 0.0 and 10.0.")
        return

    try:
        year = int(input("Enter movie release year: "))
        if year < 1800 or year > 2024:
            raise ValueError
    except ValueError:
        print("Invalid year. Please enter a valid year.")
        return

    movies[title] = {'rating': rating, 'year': year}
    save_movies(FILE_NAME, movies)
    print(f"Movie '{title}' added successfully!")


def list_movies(movies):
    """
    Lists all movies in the collection.

    Args:
        movies (dict): The current dictionary of movies.
    """
    if not movies:
        print("No movies found.")
        return
    print("\nMovies in your collection:")
    for title, details in movies.items():
        print(f"  {title} - Rating: {details['rating']}, Year: {details['year']}")


def delete_movie(movies):
    """
    Deletes a movie from the collection.

    Args:
        movies (dict): The current dictionary of movies.
    """
    title = input("Enter movie title to delete: ").strip()
    if title in movies:
        del movies[title]
        save_movies(FILE_NAME, movies)
        print(f"Movie '{title}' deleted successfully!")
    else:
        print(f"Movie '{title}' not found.")


def display_statistics(movies):
    """
    Displays statistics for the movie collection, including average rating,
    median rating, best and worst movies.

    Args:
        movies (dict): The current dictionary of movies.
    """
    if not movies:
        print("No movies found.")
        return

    ratings = [details['rating'] for details in movies.values()]
    if ratings:
        avg_rating = round(statistics.mean(ratings), 1)
        median_rating = round(statistics.median(ratings), 1)

        max_rating = max(ratings)
        min_rating = min(ratings)

        best_movies = [title for title, details in movies.items() if details['rating'] == max_rating]
        worst_movies = [title for title, details in movies.items() if details['rating'] == min_rating]

        print(f"Average rating: {avg_rating}")
        print(f"Median rating: {median_rating}")
        print(f"Best movies ({max_rating}): {', '.join(best_movies)}")
        print(f"Worst movies ({min_rating}): {', '.join(worst_movies)}")
    else:
        print("No ratings available to calculate statistics.")


def main():
    """
    Main menu for the Movies App Reloaded.
    Provides options to list, add, delete movies, and show statistics.
    """
    movies = load_movies(FILE_NAME)

    while True:
        print("\nMenu:")
        print("0. Exit")
        print("1. List movies")
        print("2. Add movie")
        print("3. Delete movie")
        print("4. Show statistics")

        try:
            choice = int(input("\nChoose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 4.")
            continue

        if choice == 0:
            print("Goodbye! Movies App Reloaded.")
            break
        elif choice == 1:
            list_movies(movies)
        elif choice == 2:
            add_movie(movies)
        elif choice == 3:
            delete_movie(movies)
        elif choice == 4:
            display_statistics(movies)
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
