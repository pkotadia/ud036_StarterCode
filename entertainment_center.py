import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys which come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine in an alien world",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_martian = media.Movie("The Martian",
                          "A sotry about an astronaut stranded on Mars",
                          "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                          "https://www.youtube.com/watch?v=Ue4PCI0NamI")

harrypotter_part1 = media.Movie("Harry Potter And the Sorcerer's stone",
                                "A story about a young wizard and his magical adventures",
                                "https://upload.wikimedia.org/wikipedia/en/c/c0/Harry_Potter_and_the_Philosopher%27s_Stone_posters.JPG",
                                "https://www.youtube.com/watch?v=PbdM1db3JbY")

inception = media.Movie("Inception",
                        "dream within a dream",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

jurassic_park = media.Movie("Jurassic World",
                            "A story about a theme park of genetically engineered dinosaurs",
                            "https://upload.wikimedia.org/wikipedia/en/6/6e/Jurassic_World_poster.jpg",
                            "https://www.youtube.com/watch?v=RFinNxS5KN4")

movies = [toy_story, avatar, the_martian, harrypotter_part1, inception, jurassic_park]
fresh_tomatoes.open_movies_page(movies)
