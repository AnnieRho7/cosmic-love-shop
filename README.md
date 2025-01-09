# Cosmic Love

Cosmic Love is an e-commerce website dedicated to offering beautifully handcrafted wire-wrapped jewellery featuring semi-precious stones. Our mission is to provide unique, high-quality pieces that enhance your natural beauty and connect you to the energy of the cosmos.

## Live Site

A live version of the site can be found [here](https://cosmic-love-3fa571bb9ed2.herokuapp.com/).


## Business Model

### Value Proposition
- Unique, handcrafted wire-wrapped jewellery featuring semi-precious stones
- PersonalisSed, high-quality accessories that connect customers to cosmic energy
- Artisan-crafted pieces with attention to detail and individual stone properties

### Customer Segments
- Spiritual and wellness-oriented individuals
- Jewellery enthusiasts seeking unique, handmade pieces
- Gift-buyers looking for meaningful, one-of-a-kind accessories
- Target age range: 25-55, female
- Mid-to-high income bracket willing to invest in quality, artisan jewellery

### Revenue Streams
- Direct product sales through e-commerce platform
- Potential future revenue streams:
  - Custom design services
  - Workshops and jewellery-making classes
  - Wholesale to boutique stores
  - Affiliate marketing with wellness and fashion influencers

### Cost Structure
- Raw materials (stones, wire, packaging)
- Website maintenance and hosting
- Marketing and advertising
- Payment processing fees
- Shipping and logistics

## Marketing Strategy

### Social Media Marketing
- Created a Facebook business page to engage with customers and showcase products
- Implemented social media links in the footer for easy access
- Future plans to expand to Instagram and Pinterest for broader reach

### Email Marketing
- Newsletter subscription feature implemented using Mailchimp
- Allows customers to stay updated with:
  - New product launches
  - Special offers
  - Exclusive discounts
  - Collection updates

### Future Marketing Plans
- Expand social media presence to other platforms
- Implement influencer collaborations
- Develop content marketing strategy
- Create blog section for jewellery care tips and styling advice

[Back to the top](#top)

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

## CRUD Functionality

The Cosmic Love e-commerce platform incorporates CRUD functionality to manage products and user interactions. The following CRUD operations are implemented:

### Create
- Admin users can add new products to the inventory through the admin panel.
- Registered users can create an account to manage their orders and wishlist.

### Read
- Users can view the collection of handcrafted jewellery on the website.
- Detailed product descriptions and images are available for each item.
- Users can view their order history and track current orders.

### Update
- Admin users can edit product details, prices, and images through the admin panel.
- Registered users can update their account information and shipping address.
- Users can modify the quantities of items in their cart before checkout.

### Delete
- Admin users can remove products from the inventory if they are no longer available.
- Users can remove items from their cart if they no longer wish to purchase them.
- Registered users can delete products from their wishlist.

These CRUD operations ensure a dynamic and interactive user experience, allowing for efficient management of products and user data.

## Design

The design of this project follows a modern and elegant aesthetic to ensure a seamless shopping experience.

[Back to the top](#top)

## Wireframes

The wireframes below illustrate the initial layout and design for different sections of the website. These wireframes served as a blueprint during the development process to ensure a clean and user-friendly design.

### Desktop Wireframes

1. **Home Page**  
   ![Home Wireframe](/static/readme-images/home-wireframe.png)

2. **About Page**  
   ![About Wireframe](/static/readme-images/about-wireframe.png)

3. **Product Page**  
   ![Product Wireframe](/static/readme-images/product-wireframe.png)

4. **Cart Page**  
   ![Cart Wireframe](/static/readme-images/cart-wireframe.png)

5. **User Profile Page**  
   ![Profile Wireframe](/static/readme-images/profile-wireframe.png)

### Mobile Wireframe

1. **Mobile Layout**  
   ![Mobile Wireframe](/static/readme-images/mobile-wireframe.png)

---

The wireframes helped define the layout and functionality of the site, ensuring a user-friendly experience.

## Entity-Relationship Diagram (ERD)

The Entity-Relationship Diagram below illustrates the database structure and relationships between different entities in our e-commerce system. This ERD serves as a blueprint for our data model.

### ERD Diagram

![E-commerce System ERD](/static/readme-images/erd-diagram.png)

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
   - Stores the address details, such as street, city, country, and post code.


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

![Homepage](/static/readme-images/homepage.png)

### Navigation Desktop

* The navigation bar is consistent and responsive, adapting based on user authentication and roles.

![Navigation Desktop](/static/readme-images/navbar-desktop.png)

### Navigation Mobile

![Navigation Mobile](/static/readme-images/navbar-mobile.png)

### Product Details

* Users can view detailed information and images of individual products. Authenticated users can also add to wishlist

![Product Details](/static/readme-images/product-detail.png)

### Cart Functionality

* Users can add items to their cart and proceed to checkout seamlessly.

![Cart Page](/static/readme-images/checkout.png)

### Admin Backend

* Admin users manage products and view orders through the admin panel.

![Admin Backend](/static/readme-images/admin.png)

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
   - The product search and filter functionality is currently not returning accurate results. The filters (e.g., price range, category, rating, brand) are either malfunctioning or not updating the results dynamically.
   - **Temporary Fix**: Investigating the backend query logic, AJAX handling, and UI interactions to resolve the issues with the filters.

---

## Possible Future Features

### 1. **Payment Gateway Integration**
   - Integrate more popular payment gateways for a seamless and secure checkout experience.
   - **Benefits**: Faster, more flexible payment options for users; supports credit/debit card payments and PayPal.

### 2. **Advanced Product Search and Filters**
   - Implement an enhanced search functionality with advanced filtering options.
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
* [Stripe](https://stripe.com/) - Payment gateway integration.
* [Mailchimp Marketing API](https://mailchimp.com/developer/marketing/) - To handle newsletter subscriptions.
* [django-allauth](https://django-allauth.readthedocs.io/en/latest/) - Comprehensive authentication and account management
* [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Beautiful forms with Bootstrap styling.
* [django-storages](https://django-storages.readthedocs.io/en/latest/) - Storage backends for Django
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

For an overview of the manual tests conducted during the development of this project, please refer to the [Manual Testing Document](/manual_testing.md).

### Validation Results

For detailed validation results, including screenshots from the HTML and PEP 8 validators, please refer to the following document:

- [Validation Screenshots](/validation.md)

### Lighthouse Performance

![Lighthouse Accessibility Score](/static/readme-images/lighthouse.png)

## Deployment

[Back to the top](#top)

### Heroku

The project was deployed via [Heroku](https://www.heroku.com/). The live link can be found [here](https://cosmic-love-3fa571bb9ed2.herokuapp.com/).

To deploy:
* Log in to Heroku and create a new app.
* Add PostgreSQL database and set environment variables.
* Configure static files with WhiteNoise.
* Push code to Heroku and enable automatic deploys.

### Forking the GitHub Repo

To fork the repository:
1. Log in to your GitHub account.
2. Navigate to the repository [here](https://github.com/AnnieRho7/cosmic-love-shop).
3. Click the 'Fork' button in the top right corner.

### Cloning the Repo with GitPod

1. Log in to GitHub.
2. Navigate to the repository [here](https://github.com/AnnieRho7/cosmic-love-shop).
3. Click 'Code' and copy the URL.
4. Open a new workspace in GitPod and clone the repo.

### Download and Extract the Zip Directly from GitHub

1. Log in to GitHub.
2. Navigate to the repository [here](https://github.com/AnnieRho7/cosmic-love-shop).
3. Select 'Download Zip' and extract it.

## Credits

[Back to the top](#top)

* The project was inspired by **Code Institute's** tutorials and resources, which helped guide the development of the e-commerce functionality.
* The concept, design, and implementation are based on my personal vision for showcasing my handmade jewellery collection, blending creativity with a user-friendly shopping experience.
* All product images and visuals featured on the site are my own, capturing the intricate details and craftsmanship of each jewelry piece.
* Special thanks to **Code Institute** for the foundational knowledge and support throughout the learning process, which played a key role in bringing this project to life.
* I leveraged **AI tools** like ChatGPT and Perplexity to help with content creation, product descriptions, and problem-solving during the development stages.
* I found numerous helpful **YouTube tutorials**, especially from **Codemy** and other web development channels, which assisted in refining the front-end design and adding advanced features to the site.

## Acknowledgments

Thanks to [Code Institute](https://codeinstitute.net) for their resources and guidance. Special thanks to my mentor, Marko, for their support and the resources shared with me.


