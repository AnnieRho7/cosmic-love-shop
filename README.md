# Cosmic Love

Cosmic Love is an e-commerce website dedicated to offering beautifully handcrafted wire-wrapped jewellery featuring semi-precious stones. Our mission is to provide unique, high-quality pieces that enhance your natural beauty and connect you to the energy of the cosmos.

## Live Site

A live version of the site can be found [here](https://cosmic-love-3fa571bb9ed2.herokuapp.com/).


## User Experience - UX

[Back to the top](#top)

### User Stories

* As a website user, I can:
  - View a collection of handcrafted jewellery.
  - Filter products by category, price, and stone type.
  - View detailed product descriptions and images.
  - Add products to my cart for easy checkout.
  - Create and register an account to manage my orders.

* As an authenticated website user, I can:
  - Review my order history and track current orders.
  - Save my favorite products for future purchases.
  - Update my account information and shipping address.

* As an admin user, I can:
  - Add, edit, and delete products from the inventory.
  - Manage user accounts and orders.
  - View analytics on sales and user activity.
  
### Agile Methodology

The Agile Methodology was used to plan this project, utilizing GitHub’s Project Board. You can view the project board [here](https://github.com/users/AnnieRho7/projects/3/views/1).

### The Scope

* To create a user-friendly and visually appealing e-commerce platform for handmade jewellery.
* To facilitate user interaction through a wishlist feature.

## Design

The design of this project follows a modern and elegant aesthetic to ensure a seamless shopping experience.

[Back to the top](#top)

## Wireframes

The wireframes below illustrate the initial layout and design for different sections of the website. These wireframes served as a blueprint during the development process to ensure a clean and user-friendly design.

### Desktop Wireframes

1. **Home Page**  
   ![Home Wireframe](/media/readme-images/home-wireframe.png)

2. **About Page**  
   ![About Wireframe](/media/readme-images/about-wireframe.png)

3. **Product Page**  
   ![Product Wireframe](/media/readme-images/product-wireframe.png)

4. **Cart Page**  
   ![Cart Wireframe](/media/readme-images/cart-wireframe.png)

5. **User Profile Page**  
   ![Profile Wireframe](/media/readme-images/profile-wireframe.png)

### Mobile Wireframe

1. **Mobile Layout**  
   ![Mobile Wireframe](/media/readme-images/mobile-wireframe.png)

---

The wireframes helped define the layout and functionality of the site, ensuring a user-friendly experience.

## Entity-Relationship Diagram (ERD)

The Entity-Relationship Diagram below illustrates the database structure and relationships between different entities in our e-commerce system. This ERD serves as a blueprint for our data model.

### ERD Diagram

![E-commerce System ERD](/media/readme-images/erd-diagram.png)

### Entity Descriptions

1. **User**
   - Represents registered users of the site.
   - Stores essential user information like username and email.
   - Forms the basis for user authentication and authorization.

2. **Product**
   - Represents jewellery items available for sale.
   - Contains product details, images, and pricing.

3. **Cart**
   - Represents the user's shopping cart.
   - Stores items that the user intends to purchase.

4. **Order**
   - Represents completed purchases by users.
   - Contains order details, status, and payment information.

5. **Wishlist**
   - Represents the user's wishlist of products.
   - Stores the user-product associations for the wishlist.


6. **Address**
   - Represents the user's saved addresses.
   - Stores the address details, such as street, city, state, country, and post code.


### Database Relationships

#### User - Cart
- **One-to-Many Relationship**: A user can have multiple items in their cart.
- **One-to-One Relationship**: A cart is associated with a single user.

#### User - Wishlist
- **One-to-Many Relationship**: A user can add multiple items to their wishlist.
- **One-to-One Relationship**: Each wishlist belongs to a single user.

#### User - Order
- **One-to-Many Relationship**: A user can have multiple orders.
- **One-to-One Relationship**: An order is tied to a single user.

#### User - Address
- **One-to-Many Relationship**: A user can save multiple addresses.
- **One-to-One Relationship**: Each saved address is associated with a single user.

#### Cart - Product
- **Many-to-Many Relationship**: A cart can contain multiple products, and a product can be added to multiple carts.

#### Wishlist - Product
- **Many-to-Many Relationship**: A wishlist can contain multiple products, and a product can appear in multiple wishlists.

#### Order - Product
- **Many-to-Many Relationship (via `OrderLineItem` model)**: 
   - An order can include multiple products.
   - Each product can appear in multiple orders.

---

### Media

- The main hero image on the site was sourced from [Pexels](https://www.pexels.com).
- All product images were taken and edited by myself.

## Features

[Back to the top](#top)

### Homepage

* Displays featured products and collections.
* Provides a hero image with a call-to-action button to explore the shop.

![Homepage](/media/readme-images/homepage.png)

### Navigation Desktop

* The navigation bar is consistent and responsive, adapting based on user authentication and roles.

![Navigation Desktop](/media/readme-images/navbar-desktop.png)

### Navigation Mobile

![Navigation Mobile](/media/readme-images/navbar-mobile.png)

### Product Details

* Users can view detailed information and images of individual products. Authenticated users can also add to wishlist

![Product Details](/media/readme-images/product-detail.png)

### Cart Functionality

* Users can add items to their cart and proceed to checkout seamlessly.

![Cart Page](/media/readme-images/checkout.png)

### Admin Backend

* Admin users manage products and view orders through the admin panel.

![Admin Backend](/media/readme-images/admin.png)

## Known Bugs and Limitations

During the development and testing phase, a few issues were identified. These are documented here for transparency and future improvement.

### Validation Errors

* Document any known HTML/CSS validation errors encountered.

**Impact**: Low - May affect HTML validation scores.

### Responsiveness Issues

* Document any responsive design limitations, particularly on smaller screen sizes.

**Impact**: Medium - Affects user experience on mobile devices.

### Performance Optimization

* Document any performance-related issues or areas for improvement.

**Impact**: Low to Medium - Core functionality not affected.

---

### Possible Future Features

* Integration with payment gateways for easier checkout.
* Enhanced search functionality for products.

## Search Engine Optimization (SEO)

The following SEO features have been implemented to ensure better search engine visibility:

### Meta Tags

- **Custom meta descriptions** for all pages
- **Dynamic titles** that reflect current page content
- All key pages have relevant **meta descriptions** focused on handmade jewellery and gemstones

### Sitemap

A `sitemap.xml` file has been implemented that includes:

- All static pages (home, about, contact)
- Product listings and individual product pages
- Dynamically updates with new products
- Priority levels set higher (0.9) for product pages

### Robots.txt

A `robots.txt` file has been implemented to:

- Allow search engines to crawl main content pages
- Prevent crawling of private areas:
  - Cart
  - Checkout
  - Admin pages
  - User account pages
- Direct search engines to the `sitemap.xml`

These implementations help search engines better understand and index the site's content, improving visibility for potential customers searching for handmade jewellery and gemstone products.

## Technologies

[Back to the top](#top)

### Languages Used

* [HTML 5](https://en.wikipedia.org/wiki/HTML/)
* [CSS 3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://www.javascript.com/)
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)

### Django Packages Used

* List any Django packages you used for your project, e.g.,:
  - [django-allauth](https://django-allauth.readthedocs.io/en/latest/) - Comprehensive authentication and account management.
  - [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) - A Django app for beautiful forms styling.
  - [whitenoise](http://whitenoise.evans.io/en/stable/) - Simplifies serving static files in production.

### Frameworks - Libraries - Programs Used

* [Bootstrap](https://getbootstrap.com/)
* [JQuery](https://jquery.com/)
* [Git](https://git-scm.com/)
* [GitHub](https://github.com/)
* [Heroku](https://id.heroku.com)
* [VSCode](https://code.visualstudio.com/)
* [Fontawesome](https://fontawesome.com/)

## Development & Testing

[Back to the top](#top)

### Manual Testing

For an overview of the manual tests conducted during the development of this project, please refer to the [Manual Testing Document](manual_testing.md).

### Validation Results

For detailed validation results, including screenshots from the HTML and PEP 8 validators, please refer to the following document:

- [Validation Screenshots](./validation-screenshots.md)

### Lighthouse Performance

![Lighthouse Accessibility Score](./readme-images/light-house.png)

## Deployment

[Back to the top](#top)

### Heroku

The project was deployed via [Heroku](https://www.heroku.com/). The live link can be found [here](insert-live-link-here).

To deploy:
* Log in to Heroku and create a new app.
* Add PostgreSQL database and set environment variables.
* Configure static files with WhiteNoise.
* Push code to Heroku and enable automatic deploys.

### Forking the GitHub Repo

To fork the repository:
1. Log in to your GitHub account.
2. Navigate to the repository [here](insert-repo-link-here).
3. Click the 'Fork' button in the top right corner.

### Cloning the Repo with GitPod

1. Log in to GitHub.
2. Navigate to the repository [here](insert-repo-link-here).
3. Click 'Code' and copy the URL.
4. Open a new workspace in GitPod and clone the repo.

### Download and Extract the Zip Directly from GitHub

1. Log in to GitHub.
2. Navigate to the repository [here](insert-repo-link-here).
3. Select 'Download Zip' and extract it.

## Credits

[Back to the top](#top)

* The project was inspired by **Code Institute's** walkthroughs and tutorials.
* Blog content reflects my own knowledge and interests, enhanced with the help of **AI tools**.
* Images were sourced from [Pexels](https://pexels.com/).
* Acknowledgments to **Code Institute** students for their projects that influenced my work.
* Utilized **AI tools** like ChatGPT and Perplexity for content assistance.
* Various **YouTube tutorials**, particularly from **Codemy**, were helpful in the development process.

## Acknowledgments

Thanks to [Code Institute](https://codeinstitute.net) for their resources and guidance. Special thanks to my mentor, Marko, for their support and the resources they shared with me.


