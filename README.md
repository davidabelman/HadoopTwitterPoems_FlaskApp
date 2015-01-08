# Using MapReduce to create poems from Twitter data

Intro
------
Flask App for poetry project. This repo contains the Flask side only (i.e. main page, and poems which are loaded by the app). See the other repo (with mapreduce code, at https://github.com/davidabelman/HadoopTwitterPoems) for details on how to generate the poems themselves.

Usage
------
Once generated, poems should be saved as Python scripts in the format seen in this folder. A link should also be added in the HTML within /templates/main.html. The hyperlink must be /poem/poemname (as with all the other poems already there). Poem.html contains the template to show the poems. Finally, app.py is the Flask app to display the main web page and featured poems.
