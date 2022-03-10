![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)
[See the live site here!](https://arin-beauty.herokuapp.com/)

# Educational Purposes
This website is for educational purposes and checkout functionality is set up to accept stripe test card details. Please don't enter your personal card details.

To process a test stripe payment at checkout, please use the following details.

card number : 4242 4242 4242 4242
Any date
Any CVV number


# Mission Statement
- To provide an easily accessible site for the promotion and sale of beauty products. To showcase the Arin Beauty Products Company and its history and sustainability.

# Target Audience
- The target audience for ARIN Beauty Products is consumers who love to find all their beauty needs met in one effective site. Here they can find beauty products for sale, makeup tutorials, reviews and more. They can make a profile, have an order history and leave comments on the blog.

# Table Of Contents
## 1. [User Experience (UX)](#ux-design)
   * [Strategy](#strategy)
   * [Scope](#scope) 
   * [Structure](#structure)
   * [Strategy](#strategy)
   * [Skeleton](#skeleton)
   * [Surface](#surface)
## 2.[Information Architecture](#information-architecture)
   * [Database](#database)
   * [Data Model](#data-model)
## 3.[Technologies Used in the project](#technologies)
  * [Languages](#languages)
  * [Databases ](#databases)
  * [Libraries and frameworks](#libraries-and-frameworks)
  * [Other technologies](#other-technologies)  
## 4.[Testing]()
  * Located in a seperate testing file.
## 5.[Deployment](#deployment)
  * [Deployment of the site](#site-deployment)
  * [How to run the code locally](#how-to-run-locally)
## 6.[Credits](#credits)
  * [Code](#code)
  * [Content](#content)
  * [Media](#media)
## 7.[Acknowledgment](#acknowledgments)

## [USER EXPERIENCE (UX)](#ux-design)
- ## [Strategy](#strategy)

  -  ## [Business Goals](#business-goals)
      * From a business point of view, I would like to have an attractive, trustworthy and fully functional website that is responsive on all devices.
      * I wish to have a website that immediately makes clear the purpose of it. In this case a website selling beauty products.
      * Products on the website can be easily modified using CRUD(create, read, update, delete) by the admin.
      * Users can easily register an account to promote revisits to the site.
      * An account will not be required however to visit the site, therefore maximizing the potential customer base.
      * Hold and secure information from all current and new customers so they may login to place orders.
      * I want to promote revisits by allowing customers who have purchased items to leave reviews and ratings.
      * I want a site that is easy to navigate using a search bar which will search using a product name or description.
      * I want the user to have the ability to break all products down into smaller categories. Such as eyes, face etc so it has high functionality and an overall high UX experience.
      * A trustworthy, safe and secure checkout and payment system to reassure customers that their private information is safe when used on this site.
      This is essential as no matter how good a product is if the payment system looks unsafe chances are I will lose sales and visits.

- ### [User Stories](#user-stories):
   
   - #### As a Shopper:
      1. I want to be able to view a list of products which relate to what I am searching for. E.g: moisturizer.
      2. I want to be able to select an individual product and access more information on that product. For example, an item which when clicked on will bring up a seperate page featuring an image, a description and a rating for the product I have clicked on.
      3. I want to be able to sort through the entire list of available products by breaking them into different categories. Example: eyes, face, lips etc.
      4. To make the site more user friendly I would like to be able to sort through the entire product content by rating, price low to high, price high to low, alphabetical order etc. This way I can quickly navigate to the item I am searching for.
      5. I would like to read reviews left by other customers who have purchased the same item.
      6. I also want to quickly search through the site. A search bar would help me easily navigate using a product name or description.
      7. My search results being at the top of the page would make usage clear and efficient.
      8. Should I decide to buy the product a clear 'Buy Now' button will be needed.
      9. A button to easily increase and decrease the quantity of the product I wish to buy is required.
      10. In the shopping cart I would like to see a running total so I can control my spending and avoid any nasty shocks caused by going over budget.
      11. Ability to edit quantity of items in the basket would increase the overall functionality of the site.
      12. The shopping cart should also feature a 'Continue Shopping' button.
      13. Once I've finished shopping I'd like to easily checkout and pay for my purchases.
      14. I want a payment method and process that is trustworthy, safe and secure.
      15. For added peace of mind, the ability to confirm my order before checkout to avoid mistakes. Example: ordering too high a quantity of a particular item.
      16. I want to recieve an email with confirmation of my order after purchase.
      17. After I have recieved my product, I want to be able to revisit the site to leave a review and a rating so other customers can benefit from my experience.

- ### As a site user:
     1. I would like the option to create an account for use on this site but as I might just want to browse I dont want this to be mandatory to access the sites content.
     2. Should I create an account I would like to easily login and logout to access my personal account info on my personalised account.
     3. I would like to receive an email confirmation after registering to be able to verify that registration was successful.
     4. I'd like to be able to easily recover my password incase I forget it so that I can recover access to my account.
     5. I'd like my profile to include my order history, order confirmation and the option to save my payment information.

- ### As a Store Owner:
     1. As admin , I want to have control of CRUD. I want to add new products when I choose.
     2. I want to edit and update a product when needed. Example: new make-up colours added etc.
     3. I want to be able to delete products when needed. Example: discontinued. Low sales due to negative reviews etc.


## [SCOPE](#scope)
The key features of the website is developed based on the user stories:
### For any site user:
 * A clear aim of the site. The home page features an image that shows some beauty products.
 * The logo in this case features the word beauty to highlight the products sold by the company.
 * The home page also features a banner which high-lights that delivery is free on orders above the amount shown.
 * A clear products page where users can view all items when the all products option is selected.
 * Clear pages to show each category when selected.
 * When the search bar is utilized, the top searches will be at the top of the page to maximize UX.
 * Product Detail page with detailed information about the selected product, this page will also be used to select the product for purchase and for increasing and decreasing the quantity required.
 * Shopping cart page, here customers can view their selected products for purchase. Edit quantity required and confirm their order before checkout.
 * Checkout page, allowing users to purchase products safely and securely.
 * Confirmation page which will show customers that their order was successful. An email will also be sent to the customers email account given while purchasing.
 * Contact page which can be used to contact the company when required.
 * About us page, where users can find the mission statement of the company.
 * A section where customers can review products that they have purchased.
 * A sign up page where users can register for an account. Here they will be able to veiw purchase history and have a personalised account.

## For registered users:
* Profile page, where users can update the default delivery information allowing ease of checkout.
* Users can see their order history from their profile page.
* Here customers can also leave a product review.
* Log out page, where users can securely log out of their page.

### For Store Owner:
  1. I would like to be able to add new products to the store.
  2. I would like to be able to edit and update a product from the store.
  3. I would like to be able to delete a product from the store.
  4. I would like to be able to delete reviews from users such as abusive or offensive messages left.
  5. Having control of CRUD will allow me to keep the site up to date and maintain a high standard of customer service.

## [STRUCTURE](#structure)
## Existing Features
### Allauth features
The sign up, register, password reset, email confirmation pages etc, have all been provided by Django allauth and formatted to suit the needs of the site.
### Base Template
* Delivery Banner - The delivery banner contains information about free delivery and the free delivery threshold. It is fixed to the top of the screen to allow for ease of access and improved user navigation. It will change color when hovered over to make it stand out more.
* Along the top of the screen is a search bar. This will use Q to search through products using names and/or descriptions.
* Also along the top of the site the user will find links that will take users to different parts of the site which are as follows:
 * Unregistered user:
   * Login link
   * Register link
 * Registered user:
   * Wishlist
   * My Account - Profile, Logout
   * Cart
 * Admin/ superuser
   * Wishlist
   * My Account - Product Management, Profile, Logout
### Navbar
The navbar will have all the product category links and is fully adjustable across screen sizes.
* All Products - here products may be sorted and selected based on rating, price and categories.
* Cosmetics
    - Face
    - Eyes
    - Lips
    - All Cosmetics
* Skin Type
    - Sensitive
    - Dry
    - Oily
    - Combination
    - All Skin Types
* Skin Care
    - Moisturiser
    - Cleanser
    - Serum
    - All Skin Care
* Christmas
    - Gift Sets
* Blog
    - Our Story
### Blog Navbar
The main site navbar leads to a blog. When the blog button is clicked it leads to a new navbar and dropdown menus. The blog is a place where the sustainability promise to customers is shared along with a brief history of the company and introduction to the team.
Here, users can also access makeup tutorials, read reviews of products and leave comments. For now adding and deleting blog posts is only for authenticated users(admin.) In later edits of the site the ability to add posts will be made public but deletion will still be admin only.
* Blog
    - Blog Content
* About Us
    - About Us
* Categories
    - Foundation
    - Makeup Tutorials
* Makeup Tutorials
    - Videos
* Sustainability Promise
    - Our Promise
### Back To Top Button
 * Due to the large volume of the site a back to top button is required for easy navigation throughtout.
### Footer
The footer has all the important shop information such as opening hours, contact details and all the important heading links.
#### Admin Features
  * Admin will have access to additional features across the site not accessible to other users. 
## [Skeleton](#skeleton)

### Technologies
#### Integrated Development Environment
* GitHub
* Languages
* HTML
* CSS
* JavaScript
* Python
* Database
#### Development - SQLite
* Deployed site - Heroku PostgreSQL
#### Storage
* Amazon AWS S3 - used to store static files.
#### Payments
* Stripe - fully integrated payments platform.
#### Frameworks
* Django - web development framework.
* Bootstrap - to assist with responsive design.
* jQuery - to assist with JavaScript coding and DOM manipulation.
#### Tools & Libraries
* Balsamiq - used to produce Wireframes.
* Font Awesome
* Google Fonts
* django-allauth - user authentication and account management.
* boto3 - Amazon Web Services SDK for python. Used to configure Amazon Web Services S3 storage of static files.
* django-crispy-forms - enables enhanced rendering of Django forms including integration with Bootstrap.
* dj-database-url - Django database configuration utility. Used to configure connection to the Heroku deployed postgres database.
* django-countries - Django application providing country choices for use with forms etc. Used to populate country choices on the Country dropdowns.
* django-extensions - Collection of custom extensions for Django. Used to automatically export the final data schema diagram for the Django model.
* django-storages - Custom storage backends for Django. Used to configure Amazon Web Services S3 storage of static files.
* gunicorn - Python WSGI HTTP Server for UNIX. Used as part of the Heroku deployment process.
* pillow - Python imaging library.
* psycopg2 - PostgreSQL database adapter for Python. Used as part of the Heroku deployment process.
* pydot - Graphviz interface used to parse the Django data model into a .dot file using django-extensions.
* Flake8 - for python code validation.
* flake8-django - Flake8 plug-in for Django, for python code validation.
* LAMBDATEST - cross browser testing cloud, for testing across multiple browsers and operating systems.
Browser Support
Arin Beauty Products supports the following browsers:

Google Chrome
Microsoft Edge
Safari
Firefox
Opera
For further information please see the Browser Compatibility section in TESTING.md.

[Structure](#structure)
Information Architecture

Database diagram made using [dbdiagram.io](https://dbdiagram.io/).
[Schema](media/schema.png)

Products Models
Products App -
  Product: Holds the information for each individual product.
  Category: Holds the available categories for the products.

Review - related to Product and User. Stores Product Reviews. A Django signal updates the Product rating field when a review is added, deleted or edited.

Checkout Models
 - Order - related to OrderLineItem and UserProfile. Stores Orders after successful checkout. Order order_number field is automatically added on save.
 - Order discount, order_total, previous_total, delivery and grand_total fields are automatically updated using a Django signal when an - - -  - OrderLineItem is added or deleted.

 - OrderLineItem - related to Order, Type, Product and Size. Stores each OrderLineItem after successful checkout.
 - OrderLineItem line_item_total field is automatically calculated on save.

Profiles Models
 - UserProfile - related to Order and User. Stores default delivery information. UserProfile is automatically created or updated using a Django receiver when a User object is updated or created.

Cart Models
Cart - related to User. Stripe webhooks.
 - Products App
    - Product: Holds the information for each individual product.
    - Category: Holds the available categories for the products.
    - Product Variations: Any variations of a specific product (sizes etc)

User
  - Created with django allauth containing the customer username, email and password.

User Profile App
  - User Profile: Holds user default delivery information


# Unfinished - ran out of time. Not all code officially credited.#
some code from codewithstein for blog/comments
snow banner made using online tutorials on youtube. (online tutorials is the company name)
gold snow image from adobe stock
serum bottle image from freepik
other pictures from unsplash
google font for fonts and font awesome for icons