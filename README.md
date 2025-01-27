# Kids-Art (Capstone Project) <a id="top"/>
![logo](https://github.com/user-attachments/assets/4fcfabb7-0fce-4784-8f55-7b6fc3a2a68b)


## Introduction
The "Kids-Art" has been designed and implemented the final project for the Code Institute's 16-week AI-Augmented Full Stack Development Bootstrap course.<br>
Live site: [https://kids-art-03ecd75b696a.herokuapp.com/](https://kids-art-03ecd75b696a.herokuapp.com/)

## Table of Contents
- [User Experience Design](#user-experience-design)
- [Project Brief](#project-brief)
- [Users](#users)
- [Project Plan](#project-plan)
- [User Stories](#user-stories)
- [Wireframes](#wireframes)
- [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
- [Website Features](#website-features)
    - [Homepage](#homepage)
    - [Single Javascript Makes Multiple Pages](#single-javascript-makes-multiple-pages)
    - [Footer](#footer)
- [Responsive Design](#responsive-design)
- [Future Features](#future-features)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Testing](#testing)
- [Credits](#credits)
    - [Code References](code-references)
    - [Use of AI](use-of-ai)
    - [Content References](content-references)
    - [Media References](media-references)
    - [Acknowledgements](acknowledgements)

[Back to top](#top)

## User Experience Design
For the develpmment of this site, I tried as mocuh as possible to follow user-centred approach throughout the inception and design of this site.

### Project Brief
The project goal is to provide .

The site user's goals are to provide .

### Users
In order :
- Persona 1: <br>



## Project Plan
On


### User Stories
Here are all the user stories that have been prioritised (all must have and some should have ones) for the current implementation of the site:
| User Stories                                    | MoSCoW priority           |  Status |
| ----------------------------------------------- |:-------------------------:| -------:|
| Homepage                                        | must have                 |   Done  |


All user stories were logged on the [GitHub Project Board](https://github.com/users/Carlos-n21/projects/16) on GitHub repo, .

As well as .

[Back to top](#top)

### Wireframes
Initial layout of website:

- Mobile view:<br>
  <img src="">
  
  
- Tablet view:<br>
  <img src=""> 
  
- Desktop/Laptop view:<br>
  <img src=""> 


[Back to top](#top)

## Design
### Colour Scheme


- Contrast check <br>
  <img src=""> 

### Typography
Initial website font-family 


### Imagery
- Background image<br>
  <img src="">

[Back to top](#top)

## Website Features
### Homepage
  <img src="assets/images/homepage-view.png">

The Homepage has 2 buttons, "Play" that takes the user to the Categories page.
And Rules, which will open the modal explaining hot to play/do the quiz.


### Footer
  <img src="">

The footer contains .



### Single Javascript Makes Multiple Pages
These 



[Back to top](#top)

## Responsive Design
Most 

## Future Features
- Add likes to posts.
- Share posts on social media.


## Technologies Used
### Languages and Technologies
![Static Badge](https://img.shields.io/badge/HTML5-Language-blue)
![Static Badge](https://img.shields.io/badge/CSS3-Language-blue)
![Static Badge](https://img.shields.io/badge/GitHub-RepoHosting-black)
![Static Badge](https://img.shields.io/badge/Gitpod-IDE-yellow)

### Libraries
![Static Badge](https://img.shields.io/badge/Bootstrap-5.3-purple)
![Static Badge](https://img.shields.io/badge/FontAwesome-icons-navy)
![Static Badge](https://img.shields.io/badge/GoogleFonts-Typography-blue)

### Tools and Programs
![Static Badge](https://img.shields.io/badge/LogoAI-LogoGenerator-red)
![Static Badge](https://img.shields.io/badge/Favicon.io-icons-navy)
![Static Badge](https://img.shields.io/badge/Balsamiq-Wireframes-green)
![Static Badge](https://img.shields.io/badge/MSCopilot-AI-orange)
![Static Badge](https://img.shields.io/badge/GitHubCopilot-AI-orange)

[Back to top](#top)

## Deployment

The process is as follows:
1. Log
 
Once the MVP 

[Back to top](#top)

## Testing
Validation of HTML/CSS, Lighthouse Audits, Bugs

### HTML Validation
- Used [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input) to test the HTML on all webpages and updated as needed. No errors found after fixing.
![HTML_validation]()

### CSS Validation

- Used [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input) to test CSS style and no errors found.
![CSS_validation]()


### Lighthouse Audit
- Used Chrome Dev Tools Lighthouse to audit the site for response time and accessibility.<br>
![lighthouse_home_mobile](https://github.com/user-attachments/assets/4f846639-51ad-42d9-aefc-46f2c09d5e4f)



### JSHint Linter

- Used [JS Hint](https://jshint.com/)) to test Javascript for ES version 6 and got no warnings.<br>
script.js
![JSHint]()<br>


## Test Results Summary

### 1. Test for Rendering the About Page with Collaboration Form

- **Test Name**: `test_render_about_page_with_collaborate_form`
- **Description**: Verifies that the About page is rendered correctly and contains the expected content, including the collaboration form.
- **Expected Outcome**:
  - Status code is 200 (OK).
  - Page content includes specific text: "About Kids-Art", "Welcome to Kids-Art", "Our Mission", "How It Works".
  - Collaboration form is included in the context.

### 2. Test for Submitting the Collaboration Form

- **Test Name**: `test_submit_collaborate_form`
- **Description**: Verifies that the collaboration form can be successfully submitted and processed.
- **Expected Outcome**:
  - Status code is 302 (redirect on successful form submission).

### 3. Test for Rendering the Blog Post Detail Page with Comment Form

- **Test Name**: `test_render_post_detail_page_with_comment_form`
- **Description**: Verifies that the blog post detail page is rendered correctly and contains the comment form.
- **Expected Outcome**:
  - Status code is 200 (OK).
  - Page content includes specific text: "Blog title", "Blog content".
  - Comment form is included in the context.

### 4. Test for Submitting a Comment on a Blog Post

- **Test Name**: `test_successful_comment_submission`
- **Description**: Verifies that a comment can be successfully submitted on a blog post.
- **Expected Outcome**:
  - Status code is 302 (redirect on successful comment submission).
  - Comment is created and needs approval.

### 5. Test for Required Name Field in Collaboration Form

- **Test Name**: `test_name_is_required`
- **Description**: Verifies that the name field is required in the collaboration form.
- **Expected Outcome**:
  - Form is invalid if the name field is empty.
  - Error message is present for the name field.

### 6. Test for Required Email Field in Collaboration Form

- **Test Name**: `test_email_is_required`
- **Description**: Verifies that the email field is required in the collaboration form.
- **Expected Outcome**:
  - Form is invalid if the email field is empty.
  - Error message is present for the email field.

### 7. Test for Required Message Field in Collaboration Form

- **Test Name**: `test_message_is_required`
- **Description**: Verifies that the message field is required in the collaboration form.
- **Expected Outcome**:
  - Form is invalid if the message field is empty.
  - Error message is present for the message field.

### 8. Test for Valid Collaboration Form

- **Test Name**: `test_form_is_valid`
- **Description**: Verifies that the collaboration form is valid when all required fields are provided.
- **Expected Outcome**:
  - Form is valid if all required fields are provided.

### 9. Test for Rendering the Blog Post List Page

- **Test Name**: `test_render_post_list_page`
- **Description**: Verifies that the blog post list page is rendered correctly.
- **Expected Outcome**:
  - Status code is 200 (OK).
  - Page content includes specific text related to blog posts.

### 10. Test for Rendering the User Profile Page

- **Test Name**: `test_render_profile_page`
- **Description**: Verifies that the user profile page is rendered correctly.
- **Expected Outcome**:
  - Status code is 200 (OK).
  - Page content includes specific text related to the user profile.


## Test Results Summary

### 1. Test for Rendering the Blog Post Detail Page with Comment Form

- **Test Name**: `test_render_post_detail_page_with_comment_form`
- **Description**: Verifies that the blog post detail page is rendered correctly and contains the comment form.
- **Expected Outcome**:
  - Status code is 200 (OK).
  - Page content includes specific text: "Blog title", "Blog content".
  - Comment form is included in the context.

### 2. Test for Submitting a Comment on a Blog Post

- **Test Name**: `test_successful_comment_submission`
- **Description**: Verifies that a comment can be successfully submitted on a blog post.
- **Expected Outcome**:
  - Status code is 200 (OK).
  - Page content includes specific text: "Comment submitted and awaiting approval".

### 3. Test for Submitting a Collaboration Request

- **Test Name**: `test_successful_collaboration_request_submission`
- **Description**: Verifies that a collaboration request can be successfully submitted.
- **Expected Outcome**:
  - Status code is 200 (OK).
  - Page content includes specific text: "Collaboration request received! I endeavour to respond within 2 working days."

### 4. Test for Search Functionality

- **Test Name**: `test_search_functionality`
- **Description**: Verifies that the search functionality works correctly and returns the expected results.
- **Expected Outcome**:
  - Status code is 200 (OK).
  - Page content includes search results matching the query.


# ERD
+----------------+       +----------------+       +----------------+
|     User       |       |     Post       |       |    Comment     |
+----------------+       +----------------+       +----------------+
| id (PK)        |<----->| id (PK)        |<----->| id (PK)        |
| username       |       | title          |       | post_id (FK)   |
| password       |       | author_id (FK) |       | author_id (FK) |
| email          |       | slug           |       | body           |
| ...            |       | content        |       | approved       |
+----------------+       | status         |       +----------------+
                         | ...            |
                         +----------------+

+----------------+       +----------------+
|     About      |       | CollaborateForm|
+----------------+       +----------------+
| id (PK)        |       | id (PK)        |
| title          |       | name           |
| content        |       | email          |
| updated_on     |       | message        |
| ...            |       | ...            |
+----------------+       +----------------+

### Bugs yet to be Fixed
- Comments update function on posts not working well, able to show updated comment but not deleting comment that was edited.
- When creating a new post, only able to publish and not safe as draft at the momment, site crashing, tried to debug, but unable to fix by the time of subimssion.


[Back to top](#top)

## Credits
### Code References
Many of the features were based on/inspired by examples in the [Code Institute Bootcamp LMS](https://learn.codeinstitute.net/dashboard) on the use of HTML, CSS and Javascript.
<br>
Other resources used as reference for the implementation:<br>


### Use of AI
#### Code Generation
The GitHub Copilot extension was installed in our local versions of Visual Studio Code. We were therefore able to write prompts or highlight functions in pseudocode and ask Copilot to suggest code snippets. Suggestions needed to be reviewed before they were included, as occassionally code may refer to

#### Debugging
Copilot was regularly used for debugging code using the inline editor. When using Chrome DevTools to inspect the preview or deployed pages.

#### Code Optimisation
When coding more complicated logical constructs, e.g. a complex iteration to loop through an array to generate innerHTML elements in a Bootstrap grid, the basic structure of the grid without the loop was assigned to the innerHTML of the target element. Once tested to run correctly, Copilot was prompted to optimise on the code. It suggested using a map method to loop through the options array to build the HTML for each element, and join them all together as a string. Again, this needed to be tested fully before it was incorporated into the code. Running the resultant code produces the same result as before. 

#### Impact on Workflow
On the whole, it has been useful to pair programme with Copilot and use it for debugging and testing as we code. Due to the tight timescale of the hackathon, the team tried to use AI wherever possible to reduce development time, from creating user stories to suggesting commit messages. It was also able to explain selected code written by other team members with a concise and accurate summary. Occassionally it can be annoying when Copilot suggests code in ghost text unnecessarily, or introduces additional closing tags or brackets unnecessarily. Nonetheless, when used with specific prompts and context, some of the results provided by Copilot have been mostly usable, thus speeding up development. 

### Content References


### Media References
[Pexels.com](https://www.pexels.com/) for some of the images used in the quiz questions<br>
Microsoft Copilot was used to generate some of the illustrations for the quiz questions<br>
The logo was generated using [Logo.ai](https://www.logoai.com/logo-maker).


### Acknowledgements
Everyone in our WECA group who have been so helpful and supportive leading up to this group project, and
Code Institute tutors (Dillon, Mark and Roo) for answering our questions

[Back to top](#top)