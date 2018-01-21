# Movie Trailer Website
This website displays a list of movies with their poster. The visiter can click on the poster of the movie and the trailer for that particular movie is played.

## Prerequisites
You'll need to first install the **Python 2.7**.

## Run the Application
Run the `entertainment_center.py` script. This should open a HTML page in your default browser.

## Code
The file `media.py` has the **Movie** class.

In order to add more movies to the HTML page you need to create a new **Movie** object as below : 
`toy_story = media.Movie("Toy Story","A story about a boy and his toys which come to life","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")`

Update the list of movies in `entertainment_center.py` to include this new object.

The file `fresh_tomatoes.py` contains the `open_movies_page()` function that will take in your list of movies and generate an HTML file including this content, producing a website to showcase your favorite movies. 
