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

### 1. **Responsiveness Issues**
   - Some pages (e.g., profile, checkout) have layout problems on smaller screens (mobile/tablet).
   - **Temporary Fix**: No workaround available yet. Being addressed in future updates.

### 2. **CSS Styling Inconsistencies**
   - Certain styles (e.g., buttons, fonts) may not render correctly across all browsers and devices.
   - **Temporary Fix**: Best viewed on Chrome; other browsers may have display issues.

### 3. **Content Overlap on Small Screens**
   - Text and images might overlap or not wrap correctly on smaller devices.
   - **Temporary Fix**: Resize the browser or use the desktop version on mobile.

### 4. **Font Size Inconsistencies**
   - Fonts may be too large or small depending on screen size.
   - **Temporary Fix**: Currently investigating better responsive typography.

### 5. **Advanced Product Search and Filters**
   - The current product search and filter functionality is not working as expected. While the basic search feature is in place, the advanced filters (such as price range, category, rating, and brand) are either not returning accurate results or are not functioning properly in certain cases.
   - **Possible Causes**: 
     - Incorrect form handling or missing query parameters in the backend.
     - Frontend elements (filters) may not be properly linked to the product listing or may not trigger the search functionality correctly.
     - JavaScript or AJAX issues causing filters to not update the displayed results dynamically.
   - **Next Steps**: Investigating the backend query logic, ensuring proper AJAX handling, and validating the UI interactions for accurate filtering.

---

## Possible Future Features

### 1. **Payment Gateway Integration**
   - Integrate more popular payment gateways for a seamless and secure checkout experience.
   - **Benefits**: Faster, more flexible payment options for users; supports credit/debit card payments and PayPal.

### 2. **Advanced Product Search and Filters**
   - Implement an enhanced search functionality with advanced filtering options (e.g., price range, category, rating, brand).
   - **Benefits**: Users can quickly find products that match their preferences, improving user experience and conversion rates.

### 3. **Order Tracking**
   - Provide real-time order tracking to allow users to track the status of their orders from placement to delivery.
   - **Benefits**: Users can stay informed about their purchases, reducing customer service inquiries and improving user satisfaction.

### 4. **User Ratings and Reviews**
   - Add a feature for users to rate and review products they've purchased.
   - **Benefits**: Helps other users make informed purchasing decisions; builds a sense of community and trust around products.

### 5. **Wishlist Sharing**
   - Allow users to share their wishlist with friends and family via email or social media.
   - **Benefits**: Users can easily share their favorite products or wishlists with others, enhancing engagement and social sharing.

### 6. **Multi-Currency Support**
   - Implement support for multiple currencies to allow international users to view prices and complete transactions in their local currency.
   - **Benefits**: Expands your reach to international markets and improves accessibility for global customers.

### 7. **Discount and Promo Code System**
   - Introduce a discount and promo code system for marketing campaigns and special offers.
   - **Benefits**: Encourage repeat purchases, increase customer loyalty, and promote special deals or seasonal sales.

### 8. **Mobile App Integration**
   - Develop a mobile app version of the website to provide users with a more convenient, app-native experience.
   - **Benefits**: Push notifications, a smoother user interface, and access to features like barcode scanning or location-based services.

---

These features are intended to improve user experience, increase conversion rates, and enhance the functionality of the platform. They are planned for future updates and development.


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

### Frameworks and Libraries Used

* [Django](https://www.djangoproject.com/) - Web framework for building scalable web applications.
* [Django REST Framework](https://www.django-rest-framework.org/) - Toolkit for building APIs (if used, otherwise remove).
* [Stripe](https://stripe.com/) - Payment gateway integration.
* [Mailchimp Marketing API](https://mailchimp.com/developer/marketing/) - To handle newsletter subscriptions.
* [django-allauth](https://django-allauth.readthedocs.io/en/latest/) - Comprehensive authentication and account management (sign up, login, etc.).
* [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Beautiful forms with Bootstrap styling.
* [django-storages](https://django-storages.readthedocs.io/en/latest/) - Storage backends for Django (likely for handling static and media files).
* [whitenoise](http://whitenoise.evans.io/en/stable/) - Simplifies serving static files in production.

### Python Packages Used

* [psycopg2](https://pypi.org/project/psycopg2/) - PostgreSQL database adapter for Python.
* [psycopg2-binary](https://pypi.org/project/psycopg2-binary/) - Binary version of `psycopg2` for easy installation.
* [python-decouple](https://pypi.org/project/python-decouple/) - To manage configuration via environment variables.
* [PyJWT](https://pyjwt.readthedocs.io/en/stable/) - JSON Web Token authentication library.
* [oauthlib](https://oauthlib.readthedocs.io/en/latest/) - To handle OAuth-based authentication.
* [requests-oauthlib](https://requests-oauthlib.readthedocs.io/en/latest/) - OAuth 1 and OAuth 2 authentication with requests.

### Tools and Technologies for Deployment

* [Gunicorn](https://gunicorn.org/) - WSGI HTTP server for Python web apps.
* [Heroku](https://www.heroku.com/) - Cloud platform for deploying and managing applications.
* [Git](https://git-scm.com/) - Version control system.
* [GitHub](https://github.com/) - Platform for hosting code and collaborating.
* [VSCode](https://code.visualstudio.com/) - Code editor used for development.

### Frontend Tools and Libraries

* [Bootstrap 5](https://getbootstrap.com/) - Frontend framework for responsive design.
* [jQuery](https://jquery.com/) - JavaScript library for simplified DOM manipulation.
* [FontAwesome](https://fontawesome.com/) - Icon toolkit for web applications.

## Development & Testing

[Back to the top](#top)

### Manual Testing

For an overview of the manual tests conducted during the development of this project, please refer to the [Manual Testing Document](manual_testing.md).

### Validation Results

For detailed validation results, including screenshots from the HTML and PEP 8 validators, please refer to the following document:

- [Validation Screenshots](./validation-screenshots.md)

### Lighthouse Performance

![Lighthouse Accessibility Score](/media/readme-images/lighthouse.png)

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


