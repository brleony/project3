# Project 3: Pizza Restaurant Website

This website is part of my homework for the course Web Programming with Python and JavaScript.
It is a website for a pizza restaurant in Cambridge, MA. Basic information about the restaurant can be found on the site.
The site can also be used to view the menu. After creating an account, users can add items to their shopping cart.

## Folders

### Pinocchios
Main Django project.

### Orders
Application for displaying the menu and adding items to the shopping cart.
In `models.py` it has the models for the menu, items in the cart and ordered items.
Folder `templates` has a template for the menu and for the shopping cart.

### Users
Application for creating an account, logging in, viewing an account and logging out.
Based on Django functionality, like `authenticate`, `login`, and `logout`.
Folder `templates` contains the templates for the account page, login page and register page.

### Static and Templates
These folders are not apps themselves.
`Templates` contains templates that don't belong to a particular app,
but rather to the whole website, like `base.html`, `index.html` and `about.html`.
`Static` contains a folder `photos` with some pictures that I have taken myself that are used on the site.
The other folder in static is `style`, which contains stylesheets.
Static also has two JavaScript files. `Main.js` has a function to highlight the active page in the navbar.
`Orders.js` has the code to make the menu modal that is necessary for placing an item in the cart work.

##### Leony Brok