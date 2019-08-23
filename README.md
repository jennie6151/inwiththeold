[![Build Status](https://travis-ci.org/jennie6151/inwiththeold.svg?branch=master)](https://travis-ci.org/jennie6151/inwiththeold)

# Full Stack Frameworks with Django Milestone Project:
### Build a full-stack site based around business logic used to control a centrally-owned dataset. Set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.

## License
This project is licensed under the MIT License - see the [license.txt](license.txt) file for details

## Author & contributor list
*Jennifer Dick*

## Table of contents
1. [Overview](#overview)
2. [Deployment](#deploy)
3. [Features](#features)
4. [Technology used](#tech)
5. [Testing (including tester instructions on site and Stripe payment and user stories)](#testing)
6. [Known bugs](#bugs)
7. [Versioning](#version)
8. [Acknowledgements and credits](#credits)

<a name="overview"></a>

## Overview

### What is this website for?
This website is for individuals who wish to purchase an antique or a collectable. The site provides a clear and easy to use shopping experience for those individuals, including an antique name, creator, image, description and price.

The colour scheme and typography adopted reflects the vintage feel of the antiques and collectables to appeal to my desired target audience.

The search bar has prominence on the index page as this is the search style that I am encouraging users to employ.

The navigation bar is consistent across the site and has clear calls to action for sign up, login and logout features. It is important that there is a benefit to signing up to a website and in this case it is to have authorisation to purchase a product.

The whole user process from browsing to purchase of an item is clearly pathed out and adopts a logical shopping approach.

### What does this website do?
This website is motivated by the brief provided by [The Code Institute](https://codeinstitute.net/) and uses the criteria supplied. It was imperative that I create a site that enables users to:
* Search for an antique by name or creator
* Read information on the product
* See an image of the product
* Login or sign up to access authorisation to purchase
* Purchase an antique

### How does it work?
The site uses **HTML** and **CSS** to route users to search and filter antiques which, depending on their search style, controls which **Python** command runs.

**Django** has been used as the presentation engine to process data from the database to show it on screen.

This website uses **MySQL** which is a relational database to hold the data.

**Stripe** is used as the e-commerce tool for purchasing across the site.

The site is styled with **Bootstrap** and I have made the site responsive so users can use this application whilst on the go.

<a name="deploy"></a>

## Deployment

1. Enable Heroku.
2. Select Master Branch
3. Select Settings > Reveal Config Vars > Enter "IP" in left column and "0.0.0.0" in right column. Then in a new row enter "PORT" in left column and "8080" in right column.
4. Heroku URL is then produced. Copy this.
5. Clone code 

<a name="features"></a>

## Features

* Eye catching index page
* Authentication. Sign up, Login and Logout functionality meaning only members who have signed up can purchase an antique 
* Large easy to see and use search box
* Antique and creator statistics from across the site on the homepage
* Clear search result
* User friendly payment form
* Payment functionality supplied by Stripe

### Features left to implement
These features have not been included in stage 1 of development but would be implemented in future developments:
* Shopping cart feature was deemed unnecessary for first release as people buying antiques aren't likely to purchase multiple but this feature would be included in stage 2.


<a name="tech"></a>

## Technology used

* [Balsamiq](https://balsamiq.com/)
    * Used to create mock ups of the site which have been uploaded as PDF files
* **Html**, **CSS** and **JavaScript**
    * Base languages used to create the site
* [Visual Studio Code](https://visualstudio.microsoft.com/)
    * Code editor used to write above code
* [MySQL](https://www.mysql.com/)
    * Database program used
* [Remote MySQL](https://remotemysql.com/)
    * Cloud hosted version of MySQL used to store the data
* [Stripe](https://stripe.com/gb)
    * Used for online payment processing
* [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
    * Web framework used to help style this single page application
* [Ruby Lane](https://www.rubylane.com/)
    * Used for antique content and graphics
* [White Noise](http://whitenoise.evans.io/en/stable/#)
    * Used to serve static and media files
* [Travis](https://travis-ci.org/)
    * Used for continuous integration testing
* [Git](https://git-scm.com/)
    * Used for version control
* [Github](https://github.com/)
    * Used as hosting platform for Git
* [Heroku](https://www.heroku.com/)
    * Platform used to host website
* Other resources used: [Fontawesome v5.7.2](https://fontawesome.com/), [Google Fonts](https://fonts.google.com/)

<a name="testing"></a>

## Testing

* Automated testing was completed using **Travis**.
* HTML code checked via a [HTML code validator](https://validator.w3.org/)
* CSS code checked via a [CSS code validator](https://jigsaw.w3.org/css-validator/)
* Asked colleagues, friends and family to check this site and access from their own devices; any small changes were made and committed.
* Used a [website response tool](https://www.responsinator.com) to test how well the website responded to different device sizes.
*  Checked every feature worked (and looked consistent) in:
    * Google Chrome
    * Internet Explorer 10
    * Microsoft Edge
    * Opera
*  Used incognito mode on **Google Chrome** to remove all cached data.

## Test account website login details
If you do not wish to create a new user this is an existing user:
* Username: tester
* Password: testpassword

## Instructions given to testers
1. Please click on the heroku url and have a trial browse and attempt to buy an item (this should fail).
2. Select the "Sign up" button and create a username and password (or use the details above).
3. Thoroughly test the site (try and break it).
4. Select an item and click "Purchase item".
5. You should then be presented with a form for payment, fill this in with fictional details.
6. Select "Pay with card" (this should only appear once you've completed the form details).
7. You should be prompted to fill in card details. You can not use genuine card information in Stripe test mode. You may be directed to another pop up window advising to "Enter the verification code...."; please select "Fill in your card details manually". Here is a test card that is widely accepted for Stripe test mode:
* Credit card number: 4242 4242 4242 4242
* Expiration date: any date in the future with the format MM/YY
* CVC: any 3-digits number
8. You should then be redirected to a successful payment screen.
9. Select the "logout" button and be logged out.

## User stories as part of testing
As a user I want to...
1. search 'eight' and see 1 antique ("Eight flow blue cabinet plates") appear. Test performed and true.
2. search 'skater' and see 1 antique of ("Bunnykins - Boy Skater") and click on the result and it to open the antique details page. Test performed and true.
3. search 'beswick' and see antiques from "Beswick" and then from the Search Results page type 'Bristol' and my search to be updated. Test performed and true.
4. search 'royal' and see antiques from "Royal Doulton" and "Royal Albert". Test performed and true.
5. search 'donkey' and find 0 recipes and a warning message. Test performed and true.
6. click on "Sign up" and be prompted to enter a username and password and then be sent to the login screen and login successfully. Test performed and true.
7. click on "Logout" and successfully log out. Test performed and true.
8. click on "Purchase item" and be taken through to Stripe payment, click to enter details manually. Enter email: admin@example.com, account number: 4242 4242 4242 4242, expiry date: 11/20, CVC:123. A successful test payment is made. Test performed and true.

<a name="bugs"></a>

## Known bugs
* I am unable to switch debug to False as this crashes the site. After having spent six hours with Xavier from The Code Institute this is still an unresolved issue despite both our efforts. Due to time contraints it was decided to leave debug=True in order to have a finished product; this would not be the case if the site went live to the public.


<a name="version"></a>

## Versioning
I used **Git** for versioning on this project, hosted **Git** on **Github**. Hosted website on **Heroku**.

<a name="credits"></a>

## Acknowledgments/credits
* *www.rubylane.com* - All media content comes from this site.
* *Antonija Šimić* - Code Institute mentor.
* *Paul Lewis* - colleague (Software Developer) who tested finished site.
* *Mallory Bemrose* - colleague who tested finished site.
* *Michael Skelton* - family who tested finished site. 
* *Code Institute tutors* - for support with deployment to Heroku, secret keys/environment variables and search functionality.

#### *MIT © 2019 Jennifer Dick*

