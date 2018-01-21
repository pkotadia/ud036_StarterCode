import media
import fresh_tomatoes

# An empty list of movie objects
movies = []

def create_and_add_movies(title,storyline,image,trailer):
    # Creating instance of the movie object and adding them into the array. 
    movies.append(media.Movie(title,storyline,image,trailer))


create_and_add_movies("Toy Story",
                        "A story about a boy and his toys which come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

create_and_add_movies("Avatar",
                     "A marine in an alien world",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

create_and_add_movies("The Martian",
                          "A sotry about an astronaut stranded on Mars",
                          "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                          "https://www.youtube.com/watch?v=Ue4PCI0NamI")
create_and_add_movies("Harry Potter And the Sorcerer's stone",
                                "A story about a young wizard and his magical adventures",
                                "https://upload.wikimedia.org/wikipedia/en/c/c0/Harry_Potter_and_the_Philosopher%27s_Stone_posters.JPG",
                                "https://www.youtube.com/watch?v=PbdM1db3JbY")

create_and_add_movies("Inception",
                        "dream within a dream",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

create_and_add_movies("Jurassic World",
                            "A story about a theme park of genetically engineered dinosaurs",
                            "https://upload.wikimedia.org/wikipedia/en/6/6e/Jurassic_World_poster.jpg",
                            "https://www.youtube.com/watch?v=xhQKwJFRL1g")


fresh_tomatoes.open_movies_page(movies)
