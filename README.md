<h1 align="center">
<br>
  <img src="static/img/res.PNG" width="600">
  <br>
    <br>
  Tasty Things - Dine On Demand
  <br>
</h1>

<h3 align="center">Data Centric Development</h3>

<h4 align="center">A Recipe Manager, Accessible Online, Which Enables Users to Create, Read, Update and Delete Recipes</h4>

- [Live link](http://tasty-and-things.herokuapp.com/)
- [Github Link](https://github.com/sree0831/MSP-3.git)
<hr><hr>
<a id="top"></a>

## Table of Contents

<!--ts-->

1. [About](#About)

    - [Goal](#Goal)

2. [UX](#UX)

    - [Layout Pro](#Layout-Pro-Boundless-Adaptability)
    - [Layout Con](#Layout-Con-Moderate-Speed-and-Execution)
    - [Additional Note](#Additional-Note)
    - [template style](#template-Style)
    - [Navigation](#Navigation)
    - [Database Structure](#Database-Structure)

3. [Technologies](#Technologies)

    - [Languages Frameworks Tools](#Languages-Frameworks-Tools)
    - [Other-Resources](#Other-Resources)

    - [Features](#Features)

    - [Existing Features](#Existing-Features)
    - [Features-Left-to-Implement](#Features-Left-to-Implement)

4. [Testing](#Testing)

    - [Tools-and-Methods-Used-for-Testing](#Tools-and-Methods-Used-for-Testing)
    - [Tested Sections 1 HTML & CSS](#Tested-Sections-1-HTML-&-CSS)
    - [Tested Sections 2 Python](#Tested-Sections-2-Python)
    - [Unresolved Bugs](#Unresolved-Bugs)

5. [Deployment](#Deployment)

    - [How the project got deployed to Heroku](#How-the-project-got-deployed-to-Heroku)
    - [Cloning the repository](#Cloning-the-repository)
    - [How to access the live application](#How-to-access-the-live-application)
    - [How to run things locally](#How-to-run-things-locally)

6. [Credits](#Credits)
7. [Content](#Content)
8. [Acknowledgements](#Acknowledgements)
    <!--te-->
## About

 **TastyThings** web application is related to restaurant based recipe site where  users can add ,edit ,delete , access cooking recipes and book a table .

#### Goal

A full stack CRUD application that allows users to register and log in to create, edit, update and delete recipes.

This application uses Python on the back-end with the Flask web framework, and uses MongoDB for the database. It also uses the Materialize framework on the front-end.

Built for Milestone Project no.3 in the Full Stack Software Development at Code Institute, in the Data Centric Development module.

The core focus of this project is on functional app logic created with **Python** while utilising the **Flask** framework and **MongoDB** NoSQL database.
## UX
 
This application was built to allow users create and share recipes, as well as updating and deleting them as necessary. The application provides a registration page for new users to register on the site, a log in page to sign in after they have registered and a contact page where users can book a table.
As a user I can:
- register as a user on the site
- log in to the site once registered
- add new recipes to the site (when logged in)
- edit recipes I create on the site (when logged in)
- delete any recipes I created on the site (when logged in)
- view a list of recipes stored on the site
- click on a recipe to see information about the recipe
- read the method for preparing the recipe
- book a table in our restaurant


#### Layout Pro 

- Choosing a **multiple page application (MPA)** takes into consideration the choice to make new content and spot it on new pages. Multi-page applications can incorporate as much data as required.
#### Layout Con 

- Being as this is a multi-page application, a server needs to reload most assets, for example, HTML, CSS, and **Python** with each interaction. When loading another page, the browser completely reloads page information and downloads all assets once more, even rehashed segments throughout all pages (for example the header/navigation) which influences Speed and Execution.

#### Template Style

- I opted for the business -casual  framework. As a tool, Bootstrap is excellent to get started, but I feel it cannot create a real quality UI without the need to write a considerable amount of custom CSS to get anywhere close to the look.

#### Navigation

- A navigation bar takes up space and a fixed one even more. That being the case, and that there is a lot of content to display in the form of recipes, etc., 
The navbar will be available to users at the top of the application on every page.
Unregistered users will see links to Sign In,contact and Recipes
Registered users will see links to Sign Out, Recipes, Add Recipe and Recipes.

### Database structure
- I separated my users from the recipes to create two separate entities.
As a recipe document is created in the recipes collection, the author of the recipe (the user who was logged in) is recorded against the recipe under the author field(STR).
**Sample Recipe doc**
```
{"_id":{"$oid":"5efe36b8c56aa8e45ef15430"},
"recipe_name":"Fudgy chocolate brownies",
"author":" Usha",
"recipe_intro":"These lower-fat brownies taste totally lush and are worth every calorie! ",
"ingredients":"400g tin black beans, drained and rinsed (235g/8½oz drained weight)80g/3oz light vegetable oil spread,4 large free-range eggs60g/2¼oz good-quality cocoa powder, plus 1 tsp for dusting50g/1¾oz ground almonds1 tbsp vanilla extract2½ tbsp maple syrup1 tsp instant coffee granules4 tbsp granulated sweetener60g/2¼oz dark chocolate chips",
"description":"Preheat the oven to 180C/160C Fan/Gas 4. Line a 20cm/8in square baking tin with baking paper.Put the black beans and vegetable spread into a food processor and blend until smooth. Add the eggs and blend again briefly, until well combined. Transfer the mixture to a large bowl.Add the cocoa powder, ground almonds, vanilla extract, maple syrup, coffee granules, sweetener and half of the chocolate chips. Whisk to combine evenly.Pour the mixture into the lined tin and sprinkle the remaining chocolate chips over the surface. Bake on the middle shelf of the oven for 18–20 minutes, or until just firm to the touch.Remove from the oven and leave to cool slightly before carefully lifting the brownie out of the tin and cutting it into squares. Enjoy while still warm, sprinkled with a little sifted cocoa.","preparation_time":"20 mins",
"photo_url":"https://ichef.bbci.co.uk/food/ic/food_16x9_1600/recipes/fudgy_chocolate_brownies_64180_16x9.jpg"}
```
**Sample User doc**
```
{"_id":{"$oid":"5effb3c3545eea5dcb08d73c"},
"name":"",
"email":"",
"password":""}
```
## Technologies

#### Languages, Libraries & Frameworks

- [HTML](https://www.w3.org/TR/html5/ "HTML5 Official Site")
    - is a semantic markup language utilised as the shell of the site.

- [CSS](https://www.w3.org/Style/CSS/ "Cascading Style Sheets Official Site")
    - means Cascading Style Sheets and was used on the design of the site.

- [Python](www.python.org) 
    - This project uses Python as the server-side programming language to provide back-end logic and serve dynamic web pages to the browser.

- [Flask](https://flask.palletsprojects.com/en/1.0.x/) 
    - This project uses Flask as the back-end framework to simplify configuration of the application and routing, to render HTML templates, work with client requests and to assist with user session management.

- [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
    - This project uses **Flask-PyMongo** to connect the application to MongoDB and for retrieving, inserting, updating and deleting data to and from the database.
- [MongoDB](https://www.mongodb.com/) 
    - is a NoSQL database program, to implement a data-store using JSON-like documents with schema. 

- [Jinja2](http://jinja.pocoo.org/docs/2.10/) 
    - was utilised to render HTML templates, imparting between front-end and back-end.

- [jQuery](http://jquery.com/ "jQuery Official Site") 
    - is used for HTML document traversal and manipulation, event handling.

- [javascript](https://www.javascript.com/ "Javascript Official Site") 
    - is used to create responsive, interactive elements for web pages, enhancing the user experience.

- [Materialize icons](https://material.io/resources/icons/?style=baseline "Materialize icons") 
    - is utilised for developing the  Material Design Icons .

- [Bootstrap](https://startbootstrap.com/ "Google Fonts Official Site") 
    - is used as a template with changes across the entire website



  #### Other Resources

- [w3schools](https://www.w3schools.com/)
- [Slack](https://slack.com/)
