# Table of contents
1. [Welcome](#welcome)
2. [UX Design](#uxdesign)
3. [Features](#features)
    - [Navigation](#navigation)
    - [Accounts](#accounts)
    - [Products](#products)
    - [Cart](#cart)
    - [Checkout](#checkout)
4. [Testing](#testing)
    - [Feature testing](#featuretesting)
    - [Validator](#validatortesting)
    - [Responsiveness](#responsivetesting)
    - [Lighthouse](#lighthousetesting)
    - [Other testing](#othertesting)
5. [Technologies](#technologies)
6. [Deployment](#deployment)
7. [Content Credits](#credits)

![Mockup]( "Mockup")

Live site link: https://.herokuapp.com/

<a name="uxdesign"></a>
## UX Design and project rationale

E-commerce business model

This website is an e-commerce store that sells books. The e-commerce model is B2C, business to customer. Different categories of books are sold on this site and users can browse by a specific category or by all books. 

The site's targeted user is therefore anyone who is interested in reading or in collecting books, and is therefore looking to purchase new books. The site offers a delivery service, at an additional cost, which users are made aware of when viewing their basket and checking out.

The B2C business model that the application is built on allows customers to order goods through the website. These orders are then received by the business and processed according to the information submitted by the customer. Once the order processing is complete, the business supplies the goods to the customer through a delivery service. The customer then receives the items that they ordered, completing the business model cycle. This process is then repeated for each new order that the business receives. This application provides physical books to customers and the value of them books is the price shown on the website.

The purpose of this website is the sale of physical books, which are then delivered to customers who complete the purchase on the website.

User Stories

The User Stories can be found in Github Projects (pp5-ecommerce-store -> Projects -> pp5-eccomerce-store or ) and are displayed in the Kanban board format. Each user story has an acceptance criteria and tasks. The User Stories are divided by site role, as different roles can perform different actions:

Site users
- As a site user I can create an account so that I can have a profile and checkout
- As a site user I can browse products so that I can get more information about them
- As a site user I can select a category to view so that I only see relevant products
- As a site user I can select a product I want to buy and add it to cart so that I can purchase it
- As a site user I can edit and remove products from cart so that I only purchase what I need
- As a site user I can checkout from cart so that I can complete the purchase of the items


Registered users
- As a registered user I can login and out of my account so that I can see my profile, keep shopping and leave when I want
- As a registered user I can review products so that I can inform others about my experience
- As a registered user I can view my profile so that I can see my past orders

Admin users
- As an admin user I can create, view, update and delete products so that I can manage the store
- As a site admin I can delete reviews so that old or spam reviews can be removed

Wireframes and design

The design is a simple layout, but with some bright colours to keep the pages interesting. The header image contains pages of books, to keep with the theme of the book shop. The colour palatte was chosen from coolors.co, based on the colours from the header image.

SEO and digital marketing

![Alt text](/media/wireframe_fb.jpg "Optional Title")

<a name="features"></a>
## Features

<a name="navigation"></a>
### Navigation bar

The navigation bar is the place where site users can access all of the features of the website. Using the 'books' dropdown arrow, they can select to either view all books or view by category. Using the 'account' dropdown, they can either register for an account, login, or view their profile and logout.

The cart option on the navigation bar allows site users to click into their cart and view what they have added to it. 

This navigation bar is available on all pages of the website, so users are never confused as to how to get back to a certain page or how to login/logout.

<a name="accounts"></a>
### Accounts

If a user is not registered or login, the account dropdown will show them the options 'register' and 'login'. Once user's are logged in, they will see 'my profile' and 'logout' in the account dropdown menu.

The benefits of creating an account and having access to the profile page are:
- This shows users a history of their past orders
- Links they can click to see the full details of the orders
- The option to udpate their delivery information 
- Ability to leave reviews on products. Once users have an account, they can navigate to any product and click on 'review this book'. There is no approval process for reviews, so these are visible in real time as soon as the user submits the form. 

These benefits are explained on the homepage of the website, so users are aware of the reasons why they would need to create an account.

<a name="products"></a>
### Products

Products can be accessed either by the 'shop now' button on the homepage or through the dropdown menu 'books' on the navigation bar. If accessed through the navigation bar, users will see the option to browse by category or by all books.

For the purposes of this website, stock images have been used as the book images.

On the products page, both for all books and for each category, users see cards with brief information about each book. This information is the title, author, category and price, along with an image. For each book, there is an option to click on 'see more', which brings to the product details page. There is an option on this page to add new products. This is available to admins only and allows them to add new products to the store.

The product details page contains more detailed information about each book, such as a description, ISBN number and reviews. There is an option to add the book to cart, along with a quantity box to specify how many of each product the user wants.

There are two admin buttons on this page, edit and delete. These are accessible to admins only and allow to either update the product or delete it. 

<a name="cart"></a>
### Cart

Users can get to the cart page from the navigation menu by clicking on 'cart'.

If there are no items in the cart, users will see text saying 'Your cart is empty.' and a button to go back to the products page.

Once users have added in an item, they will see an image of the item, the title and author, quantity and price. Users can interact with this page by either updating the quantity (changing the number in the box and then clicking update), or deleting the item from the basket by clicking on the bin icon. The price displayed here is for one of each item, so the price will stay the same regardless of quantity.

Under this box, users see the delivery and total cost information. This will update automatically when the quantity is changed (the 'cart total' heading). There is a fixed delivery cost of 5 EURO per order, this can be seen after the 'delivery' heading. There is then a total, which is the total of the cart plus the delivery fee. Users are also provided with information about free delivery, and how much more they would need to spend to qualify for it.

Clicking on 'secure checkout' will take site users to the checkout page.

<a name="checkout"></a>
### Checkout

The checkout page consists of a form and card payment box, along with a summary of the order that is being placed. If the user is logged out or not registered, there is an option under the form to create an account or sign in to save the information they have put in the form. If the user is logged in, this gives them the option to check a box to save this information to their profile.

If users have previously saved delivery or contact information to their profile, this will display automatically in the form.

The payment box connects to Stripe and processes the card payment. For the purposes of this project, the Stripe test card number was used.

When users have entered in their information and reviewed their order, they can click on complete order which takes them to a success page if the form and payment go through. The checkout success page gives them a summary of the order along with an order number. Details are also sent by email to the email address provided in the form.

<a name="technologies"></a>
## Technologies

<a name="testing"></a>
## Testing

<a name="featuretesting"></a>
### Feature testing

Feature testing was done manually by going through each feature and ensuring it works as intended. Below are details of this manual testing:

Homepage

| Action        | Expected Behaviour  | Result | 
| ------------- | ------------- | ------------- | 
| Enter url of site in browser  | site shows homepage | pass | 

Role-based functionality

<a name="validatortesting"></a>
### Validator testing

HTML validator testing passed (https://validator.w3.org/)

![HTML](static/media/htmlpp4.jpg "HTML")

CSS validator testing passed (https://jigsaw.w3.org/css-validator/)

![CSS](static/media/csspp4.jpg "CSS")

Python testing was done in Gitpod, with errors showing a red underscore and also in the 'problems' tab. These could then be easily corrected as they arose. Currently there are no issues in the 'problems' tab and no errors showing on any of the pages.

<a name="responsivetesting"></a>
### Responsiveness

<a name="lighthousetesting"></a>
### Lighthouse


<a name="othertesting"></a>
### Other testing

<a name="deployment"></a>
## Deployment

<a name="credits"></a>
## References

https://mdbootstrap.com/docs/standard/extended/shopping-carts/