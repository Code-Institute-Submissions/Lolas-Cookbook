Lola’s Cookbook - Recipe Manager
---------------------------------------
**Data Centric Development - Marjolein van Leeuwen**

This is my Data Centric Development project. 
I created Lola’s Cookbook for myself as a repice manager so I could store my family’s recipes. I have called it Lola’s cookbook, because we always called my mother Lola and she had a real talent in Filipino cooking. I also created a mealplanner, so I can organize my favorite meals.

Click [here][DEMO] for my deployed project.

![Lola's Cookbook demo](assets/images/cookbook.gif)

**User stories**

* As a user : As a new visitor to Lola's cookbook, I want the page to be easily navigated.
* As a user: As a new visitor I want clear instructions on how to add, view, update and delete recipes.
* As a user: I want a cookbook web app that responds quickly to my interaction.
* As a user: I want a search option so I can quickly find the recipe I'd like.
* As a user: I would like to easily organize my meals using the mealplanner

The ideal user:
* Someone who wants to store (family) recipes and likes to organize their meal with a mealplanner.

**Strategy**

* The goal of the website is to provide visitors the option the create their own database of family recipes and organize them in a mealplanner.
* The websites focuses on 4 main categories of recipes: Breakfast, Lunch, Dinner & Dessert. 
* Users are allowed to both edit/update recipes based on their experience when preparing the meal but also delete unwanted recipes. For the delete button a strong red color was used as a warning color. The edit button is a blue bolor.
* The add recipe form displays placeholder text in all of the formfields to give the user instructions for easier input.
* The edit recipe form is pre-populated with the recipe information that is pulled from the database.

**Database**

* The database chosen for this is a non-relational database hosted on MongoDB.
* The web application uses 3 database collections, 'categories', 'recipes' and 'mealplanner'.

**Structure**

* 

**Skeleton** 

I created a wireframe using the program “Mockflow”. 

![Wireframe1](static/wireframe/Wireframe1.png)
![Wireframe2](static/wireframe/Wireframe4.png)
![Wireframe3](static/wireframe/Wireframe3.png)
![Wireframe4](static/wireframe/Wireframe2.png)

**Surface**

* For the surface plane I wanted the design to be minimilistic.
* The colors are ...........
* I choose the Lato google font........
* Lola's cookbook logo.......
* My images carroussel on the homepage is build with materialize code and is also touch compatible. 
* The images are pictures of Philipino Cuisine

**Technologies**

*Languages*
* HTML5
* CSS3
* Javascript
* Python3

*Libraries*
* Materialize
* FontAwesome
* jQuery
* Dnspython
* Flask
* Flask-PyMongo
* PyMongo

*Database*
* MongoDB

*Hosting*
* Github
* Heroku

**Features**

The website has been built with a mobile-first approach and is responsive.
This is achieved by using the front end framework from Materialize and custom-written css.

* CRUD functions *

* Users can add their favorite family recipes to the database. (Create)

* Users can browse through all recipes contained in the database. (Read)

* Users can edit recipes in the database. (Update)

* Users can delete recipes in the database. (Delete)

**Testing**

* All testing carried out was done manually.
Testing problems I encountered:

* Code Validation

* Responsive design

* Screen size testing

* Navigation


**Features Left to Implement**

Going forward I would like to implement the following features:

* Storing user data: Storing user data (username) for each recipe, connecting the recipe to the user that created it.
* Login and registration feature: Enabling users to create an account and log in.
* Rating feature: Enabling users to vote on recipes.

**Deployment**

The project is stored in a GitHub repository and hosted on Heroku.

I followed the next steps to deploy my game on the GitHub pages:

* Log into GitHub.
* Select Sweetzia/Lolas-Recipe-Manager in the repository list.
* Go to Settings
* Scroll down to the GitHub Pages section.
* Select the Master Branch
* On selecting Master Branch the page is automatically refreshed, lola's cookbook is deployed.
* The link can be retrieved to the deployed website.

I followed the next steps to host lola's cookbook on Heroku:
* Created a new application using the Heroku dashboard.
* Go to settings tab, click on 'reveal config vars' and add config vars such as IP (0.0.0.0), PORT (5000), MongoDB Name, MongoDB URI (URL with DB name and password).
* Log into Heroku via the gitpod terminal using 'heroku login -i' and follow the on screen instructions to log in.
* Create a requirements.txt using 'pip3 freeze > requirements.txt'.
* Create a Procfile using 'echo web: python app.py > Procfile'.
* Connect GitHub to Heroku in deployment method in Heroku
* Deploy project to Heroku in the Gitpod terminal using 'git push heroku master'.
* Open app in Heroku, succesfully deployed app!


**Credits**

Content
All of the text content on the website was written by me.

Media
The recipe images used accross the page were obtained from Google Images.

The recipes that I've added to the database in order to display the functionality of the application are borrowed from:
*

**Acknowledgements**

***I want to thank my mentor Brian M for guiding me through the process of creating my own online cookbook and mealplanner.***
 

[DEMO]: <https://sweetzia.github.io/Lolas_cookbook/index.html>
[0]: <https://www.youtube.com/channel/UC5DNytAJ6_FISueUfzZCVsw>
[1]: <https://kenney.nl/>
[2]: <https://pngtree.com/freepng/hand-drawn-cartoon-bacteria-virus-microbe-corona-virus-image_5334155.html>
[3]: <https://nl.wikipedia.org/wiki/Space_Invaders>
[4]: <https://developer.mozilla.org/en-US/docs/Games/Techniques/Control_mechanisms/Desktop_with_mouse_and_keyboard>
[5]: <https://www.youtube.com/watch?v=XmqAPQsc1n4&t=3465s>
[6]: <https://www.youtube.com/watch?v=kSt2_YZzCec>
[7]: <https://codepen.io/kocsten/pen/rggjXp>
[8]: <https://www.youtube.com/watch?v=9TcU2C1AACw>




