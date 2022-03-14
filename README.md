# stream-source 0.0.1
 A python API to locate streaming sources for all movies and television shows
 ## How to install ?
 Open the terminal and type in the command
  > pip install stream-finder
 ## How to use ?
 To find the streaming source of movies call find_movie
 ### Movies
  >import streamfinder
  >sources = streamfinder.find_movie(title)
  #### find_movie(title) will return a list of streaming sources of the movie title passed as argument
   If there are no streaming sources available then the function will return False
   ### Television shows
   >import streamfinder
   >sources = streamfinder.find_tvseries(title)
  #### find_tvseries(title) will return a list of streaming sources of the television show title passed as argument
   If there are no streaming sources available then the function will return False