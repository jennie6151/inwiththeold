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
5. [Testing](#testing)
6. [Versioning](#version)
7. [Acknowledgements and credits](#credits)

<a name="overview"></a>

## Overview

### What is this website for?
This site uses business logic to control a 

### What does this website do?
This website is motivated by the brief provided by [The Code Institute](https://codeinstitute.net/) and uses the criteria supplied. It was imperative that I create a site that enables users to:
* Search for an antique
* Filter these antiques by specific criteria
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
* Large easy to see and use search box
* Clear search results with specific criteria to further filter by
* Add, edit and delete functionality for all recipes


### Features left to implement
These features have not been included in stage 1 of development but would be implemented in future developments:
* None


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
* [Stripe](https://stripe.com/gb)
    * Used for online payment processing
* [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
    * Web framework used to help style this single page application
* [Ruby Lane](https://www.rubylane.com/)
    * Used for antique content and graphics
* [S3](https://aws.amazon.com/s3/)
    * Used to serve static and media files
* [Travis](https://travis-ci.org/)
    * Used for continuous integration testing
* [Git](https://git-scm.com/)
    * Used for version control
* [Github](https://github.com/)
    * Used as hosting platform for Git
* [Heroku](https://www.heroku.com/)
    * Platform used to host website
* Other resources used: [Fontawesome v5.7.2](https://fontawesome.com/)

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

## User stories as part of testing
As a user I want to...
1. search 'eight' and see 1 antique ("Eight flow blue cabinet plates") appear. Test performed and true.
2. search 'skater' and see 1 antique of ("Bunnykins - Boy Skater") and click on the result and it to open the antique details page. Test performed and true.
3. search 'beswick' and see antiques from "Beswick" and then from the Search Results page type 'Spode' and my search to be updated. Test performed and true.
4. search 'royal' and see antiques from "Royal Doulton" and "Royal Albert". Test performed and true.
5. search 'donkey' and find 0 recipes and a warning message. Test performed and true.
6. click on "Low-fat" from the dropdown filter and see 3 results. Test performed and true.
7. click on the 'Add recipe' button and be able to add a recipe and for the mandatory fields to stop form submission if not completed. Recipe to appear on the index page in a new card. Test performed and true.
8. search 'soup' and use the 'Sort by' dropdown to change between alphabetical listing (ascending) or by number of likes (descending). Test performed and true.
9. from any chosen recipe click 'Like recipe' button and for the 'Recipe likes:' to update on the recipe and on the homepage card. Test performed and true.
10. from any chosen recipe click 'Edit recipe' button and to be taken to the edit page, make changes and for these to be reflected in recipe and index pages. Test performed and true.


<a name="version"></a>

## Versioning
I used **Git** for versioning on this project, hosted **Git** on **Github**. Hosted website on **Heroku**.

<a name="credits"></a>

## Acknowledgments/credits
* *Antonija Šimić* - Code Institute mentor.
* *Paul Lewis* - colleague (Software Developer) who tested finished site.
* *Mallory Bemrose* - colleague who tested finished site.
* *Michael Skelton* - family who tested finished site. 
* *Haley Schafer* - Code Institute tutor. For help with deployment to Heroku, secret keys and debug mode.

## Commands to remember

#### *MIT © 2019 Jennifer Dick*

