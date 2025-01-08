# Manual Testing Documentation

## User Story Testing
| User Story | Test Performed | Evidence | Result |
|------------|---------------|-----------|---------|
| User Registration | Complete registration process | ![Register](/static/readme-images/registertest2.png) | ✅ |
| User Login/Logout | Test login and logout functionality | ![Login](/static/readme-images/logintest2.png) ![Login](/static/readme-images/logintest3.png)  | ✅ |
| Cart Management | Add/remove items from cart | ![Cart](/static/readme-images/carttest1.png) ![Cart](/static/readme-images/carttest3.png) ![Cart](/static/readme-images/carttest5.png) ![Cart](/static/readme-images/carttest6.png)  | ✅ |
| Checkout Process | Complete purchase with test card | ![Checkout](/static/readme-images/checktest1.png) ![Checkout](/static/readme-images/checktest2.png) | ✅ |

## Functionality Testing

### Authentication Testing
#### Registration Process
- Test Description: User account creation
- Steps Taken:
  1. Navigate to registration page
  2. Enter valid details
  3. Submit form
- Evidence: 
  - ![Register](/static/readme-images/registertest.png)
  - ![Register](/static/readme-images/registertest2.png)

#### Login/Logout Process
- Test Description: User authentication
- Evidence:
  - ![Logout](/static/readme-images/logouttest2.png)
  - ![Login](/static/readme-images/logintest2.png)
  - ![Login](/static/readme-images/logintest3.png)

### Navigation Testing
- Test Description: Menu and navigation functionality
- Areas Tested:
  - Desktop navigation
  - Mobile responsiveness
  - Dropdown menus
- Evidence:
  - ![Account dropdown](/static/readme-images/logintest1.png)
  - ![Cart dropdown](/static/readme-images/navbar-desktop.png)
  - ![Mobile](/static/readme-images/navbar-mobile.png)

### Shopping Cart Features
- Test Description: Cart functionality
- Tests Performed:
  1. Adding products
  2. Updating quantities
  3. Removing items
  4. Cart calculations
- Evidence:
  - ![Cart](/static/readme-images/carttest1.png)
  - ![Cart](/static/readme-images/carttest2.png)
  - ![Cart](/static/readme-images/carttest3.png)
  - ![Cart](/static/readme-images/carttest6.png)

### Payment Testing
| Test Case | Steps | Expected Result | Evidence | Status |
|-----------|-------|-----------------|-----------|---------|
| Successful Payment | Use valid test card | Order confirmation | ![Checkout](/static/readme-images/cartsucess.png) | ✅ |
| Failed Payment | Use invalid card | Error message | ![Checkout](/static/readme-images/cartend.png) | ✅ |

### Profile Management
- Test Description: User profile functionality
- Tests Performed:
  1. Update profile information
  2. View order history
  3. Manage addresses
- Evidence:
  - ![Profile](/static/readme-images/profileup.png)
  - ![Profile](/static/readme-images/addressadd.png)

### Admin Features
- Test Description: Admin functionality
- Areas Tested:
  1. Product management
  2. User management
- Evidence:
  - ![Admin](/media/readme-images/admintest1.png)
  - ![Admin](/media/readme-images/admintest2.png)

## Responsiveness Testing
| Device Type | Test Performed | Evidence | Status |
|-------------|---------------|-----------|---------|
| Mobile | Layout and functionality | ![Mobile](/static/readme-images/mobiletest.png) | ✅ |
| Tablet | Layout and functionality | ![Tablet](/static/readme-images/tablettest.png) | ✅ |
| Desktop | Layout and functionality | ![Desktop](/static/readme-images/desktoptest.png) | ✅ |

## Cross-Browser Testing
| Browser | Version | Evidence | Status |
|---------|---------|-----------|---------|
| Chrome | Latest | ![Chrome](/static/readme-images/chrome.jpeg) | ✅ |
| Safari | Latest | ![Safari](/static/readme-images/safari.jpeg) | ✅ |
| Brave | Latest | ![Brave](/static/readme-images/brave.jpeg) | ✅ |
| Firefox | Latest | Tested | ✅ |
