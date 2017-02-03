#import the necessary python programs located within the same folder
import fresh_tomatoes
import media

#define each movie instance with it's title, summary, poster image url, and youtube trailer link that reference back to the class Movie within media.py
dark_night = media.Movie("The Dark Night",
                        "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=EXeTwQWrcwY")

eternal_sunshine = media.Movie("Eternal Sunshine of the Spotless Mind",
                     "an estranged couple who have erased each other from their memories",
                     "https://infinitecrescendo.files.wordpress.com/2014/03/eternal-sunshine-of-the-spotless-mind-poster.jpg",
                     "https://www.youtube.com/watch?v=rb9a00bXf-U")

fight_club = media.Movie("Fight Club",
                         "Mischief. Mayhem. Soap.",
                         "https://ok2disconnectportfolio.files.wordpress.com/2012/02/fight-club-hi-res-poster-vertical-a31.jpg",
                         "https://www.youtube.com/watch?v=J8FRBYOFu2w")

finding_nemo = media.Movie("Finding Nemo",
                           "A quest to find a lost fish",
                           "http://onecrazykid.com/wp-content/uploads/2012/09/Finding-Nemo-poster.jpg",
                           "https://www.youtube.com/watch?v=wZdpNglLbt8")

goodfellas = media.Movie("Goodfellas",
                         "A young man grows up in the mob and works very hard to advance himself through the ranks.",
                         "https://www.movieposter.com/posters/archive/main/44/MPW-22061",
                         "https://www.youtube.com/watch?v=qo5jJpHtI1Y")

blues_brothers = media.Movie("The Blues Brothers",
                                 "Two blue musicians hit the road",
                                 "http://www.oscars.org/sites/oscars/files/bluesbrothersposter.jpg",
                                 "https://www.youtube.com/watch?v=A-xtJYIwfYo")

#create the variable movies that hold an array of each movie instance
movies = [blues_brothers, dark_night, eternal_sunshine, fight_club, finding_nemo, goodfellas]

#run the function open_movies_page that is within fresh_tomatoes.py with array movies as the argument to create and open the html file
fresh_tomatoes.open_movies_page(movies)

