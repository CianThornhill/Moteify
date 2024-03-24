# Moteify

<img src="https://i.imgur.com/RGodzSJ.jpeg">

---
## Introduction

Moteify is an emote sharing platform where artists can upload and share their creations for others to favourite and download, for use with emote supporting sites and platforms such as Twitch and Discord.

The project was developed as part of Code Institute's 16 week Full Stack Development course as my final individual capstone project, bringing together the knowledge I've learned over the course of my study.

The project focuses on the use of Django and Bootstrap frameworks to aid in the production of a functional web app with database manipulation and CRUD functionality.

<a href="https://moteify-5e8f7613a374.herokuapp.com"> <h4 align="center">Moteify live site</h4> </a>
---
## Project Overview

Moteify was designed as a way to allow artists to upload their emote creations for download and use online by others on various emote supporting platforms.

The idea was to create a site that fufills the educational project purposes of implementing CRUD functionality in a short project completion window of 2 weeks, while retaining a relevant business use case.

In this regard, rather than a fully functioning emote marketplace, Moteify aims to serve as an emote **sharing platform** which enables artists to upload, favourite and view other artists emote creations on a publically available space, allowing user's to download their creations and share them with friends and implement them on their own emote supported streams and servers.

User's of Moteify can:

- Register, log in and log out.
  - _(Log in is Required to favourite and upload emotes)._
- Upload Emotes
  - _(Emote aspect ratio is locked to ensure compatibility for use on apps such as Discord and Twitch. size lock for site display purposes)._
- Favourite Emotes
  - _Users can favourite emotes they find that they like for future reference and to more easily find them within their favourites list._
- Search for Emotes by category:
  - _Emotes are assigned categories when uploaded, allowing users to filter for specific emotions._
- Create their User Profile
  - _(Future implementations planned to allow users to view other user profiles, enabling artists to share their portfolios etc.)._
- Manage their emotes, favourites and User Profile.
  - _Full CRUD functionality has been implemented to allow users to edit, and delete uploaded emotes or their account as a whole._
---
## User Stories

All below User stories can be found within the GitHub Projects Kanban board linked to this project, which was used to track completion and fufillment.

### Non logged in user:
| I want to | acceptance criteria |
| -------- | ------- |
| Create an account so that I can log in | 1. User can create an account <br> 2. User's can log in. <br> 3.Users can log out. |
|Browse Emotes available | 1. Users can view the emotes available on the site. <br> 2. Non Logged in users can only view emotes and need to register and log in to upload or favourite. |
| | |

### Logged in user:
|I want to  | acceptance criteria |
| -------- | ------- |
| Log in and log out of my account | 1. Users can log in to their account they registered. <br> 2. Users can log out of their account.    |
| Browse emotes that are available on the site  | 1. Users can visit the Emotes page to see all of the emotes uploaded on the site.     |
| Upload my emotes to share them with everyone | 1. Users can upload emotes to the site. <br> 2. Users can view the emotes they have uploaded. <br> 3. Emotes that users upload are displayed on the emotes page.   |
| Be able to edit or delete my emote uploads   | 1. Users can edit their emote uploads. <br> 2. Users can delete their emote uploads.  |
| Find the kinds of emotes I'm looking for    | 1. Users can search for specific kinds of emotes by filtering for desired emotions.  |
| Be able to favourite and unfavourite emotes | 1. Users can favourite emotes that they like. <br> 2. Users can view their list of favourite emotes. <br> 3. Users can remove items from their favourites.   |
| Create my own Profile    |  1. Users can create a profile. <br> 2. Users can add a profile photo and profile info. <br> 3. Users can edit their profile bio and photo. |
| Be able to Download Emotes that I like    | 1. Users can save emotes from the site for use on their discord / twitch.    |
| Be notified of important actions so that I know they completed.    | 1. Users receive message notifications to let them know actions have been completed <br> - Registered, Logged in, Logged out <br> - Emote Uploaded, Edited, Deleted <br> - Emote favourited, unfavourited <br> - Profile Edited, Deleted   |
| Easily navigate the site so I can find what I'm looking for    | 1. Users can easily navigate the site using a nav bar <br> 2. All relevant public pages on the site are accessible through links and are clearly labelled.    |
| Delete my account if I no longer want it    | 1. Users can delete their account. <br> 2. All content associated with the User is also deleted.    |

### Stories not in Scope for this release:
|I want to  | acceptance criteria |
| -------- | ------- |
| I want to be able to view other Users profiles and their emotes specifically    | 1. Users can click on an emote uploader while viewing an emote and be shown that user's profile page and emotes. <br> 2. Users can filter emotes by uploader.  |
|  I want to download emotes directly to my local storage.   | 1. Users can download directly to their pc with a download button <br> - Displayed emotes otherwise converted to webp.
| I want to be able to like or dislike emotes | 1. Users can like or dislike emotes <br> 2. Users can remove likes and dislikes. |
| I want to be able to link people to my portfolio and art services from my profile | 1. User Profiles are publically viewable by other registered users while remaining secure.|

---
## Workflow and Methodologies
---

For this project I implemented an Agile Methodology using the MOSCOW prioritization workflow. Having made use of these workflows and methodologies during Hackathon projects, I was familiar with the process and found that they were still very useful in the context of an individual project: 

- In combination with the development of my ERD and Wireframes, they forced me to think about what features were truly needed and if I was viewing them from the perspective of a user through creating the tasks based largely on a set of extensive user stories.
- During the completion of the project, checking my board and breaking down each segment into maneagable tasks allowed me to keep track of what I was working on, and what I could move on to when I was done.
- Initial planning and management of my Kanban board allowed me to better timekeep and prevent scope creep.

![Moteify Board](https://i.imgur.com/qm7p7XY.png)

- Using Labels, I assigned MOSCOW priortization to each user story, I could then view these within my Project Kanban board at any time and edit them accordingly if required as time and scope became more in question.

<p align="center"><img src="https://i.imgur.com/22h7aun.png"></p>

- I also used markdown check boxes to allow me to tick off more maneable bites of larger User Story tasks which proved both satisfying and useful.

You can find my Kanban board publically linked within the "projects" section of this Github Repo.

---
## Ideation

### Project MVP Features
- User Sign up / log in / verification
- Emote Gallery Page which shows uploaded Emotes (paginated)
- Users can Upload emotes. They can then edit and delete their uploads on their “My Emotes” Page. (/ User profile page which can also let them upload a profile image and link to their portfolio’s with a bio)
- Users can save Emotes to their Favourites and view their Favourites from their my emotes page in “my favourites”(/ User profile page)


### Project Extended Features

- Clicking on a Link in Emote Gallery brings you to that Individual emotes page.
- On an individual Emote page, Users can Like or Dislike an upload.
- Emotes have a categories field, allowing for the creation of a “Category” filter in the Emote Gallery page to filter for “Happy”, “Sad”, “laughing”, “animated” etc.

---
## Design

### Wireframes

Once I had the general idea for the site figured out and developed a majority of the user stories, I set about creating wireframes with that information in mind.

For the wireframing of the site I used **Photoshop** to sketch my initial ideal visual appearance of the site to aim for.

Understanding that the main aim for this project was to showcase Django implementation and CRUD functionality, I focused on creating an idea for how the pages could function mainly, as well as how they would look visually in an ideal final product.

Through my ideation and user stories development, I had a clear idea of the kinds of pages and features I would need.

![Wireframes](https://i.imgur.com/zGTOM43.jpeg)

---
### Flow Chart

After creating my site wireframes and deciding on the scope of the project with user stories, I created and revised a site map and flow chart. This flow chart was informed by my wireframes and ideation and was developed and revised in tandem with my ERD during the initial stages of development:

![Flowchart](https://i.imgur.com/RCICSDo.png)

---
### Entity Relationship Diagram (ERD)

The ERD displayed below is a revised version of an earlier diagram that was updated following project scope reductions and a development of model requirements during production. As an example, the default image entity as a standard "ImageField" was required as a bugfix to enable a default image to be displayed from static without the use of Cloudinary for users who had not yet uploaded one. 

The overall layout and design however was established in the initial version and in combination with the flowchart and wireframes developed proved as invaluable resources to more easily visualize what I wanted to develop.

![ERD](https://i.imgur.com/KtKU3wa.png)

---

### Models

#### Built in
##### User / User Registration
- User Registration and log in was handled with Django's built in User Model in combination with Django AllAuth.

#### Custom Models
##### Emote Model
| Name  | Type |
| -------- | ------- |
| User  | ForeignKey |
| emote_img | CloudinaryField |
| title | Charfield |
| category | Charfield |
| favourites | ManyToMany |
| upload_date | DateTimeField |

##### Profile Model
| Name  | Type |
| -------- | ------- |
| User  | OneToOneField |
| profile_image | CloudinaryField |
| default_image | ImageField |
| display_name | Charfield |
| bio | RichTextField |

### Visual Design

#### Colour Scheme

For the color scheme of the site, I based it off a palette I discovered on https://colorhunt.co , a site for Designers and Artists to get color palette inspiration for their projects.

<p align="center"><img src="https://i.imgur.com/NDfr2at.png" width="500"></p>

- For the site, I wanted to go with a "Dark" scheme, as I find them much easier to look at and more appealing. I also think the site appeals to people who are commonly on PC watching streams, communication on discord servers, creating digital art etc. This target audience commonly prefers Dark web pages over standard schemes.
- Purple is a color associated commonly with both Twitch and Discord, the main platforms currently that are associated with emote use, and so I wanted to ensure that was my primary color.
- Bright mint and Blue worked as compliments to this to stand out from the dark backgrounds.
- I muted the colours and changed the hue's and saturations slightly to make them more web friendly, and then saved them as root variables within my CSS file to allow me to ensure that any changes I made to a color would cascade throughout the project.

#### Font

For my Font, I did some research on some commonly used font pairs for web design on sites such as: 
- https://elementor.com/blog/font-pairing/
- https://www.pagecloud.com/blog/best-google-fonts-pairings 

I decided that due to the content of this website, I wanted to use two sans-serif fonts that were easily ledgable at smaller sizes, and felt casual and functional.

In the end I settled on "Roboto" for the Headings and "Nunito" for the main font. 
These were gathered and imported to CSS using Google Fonts.

#### Logo and Display Content

Prior to re-skilling into coding, I studied Game Art and Design in college, and so I made use of these skills to generate some of my own content for the site so that I didn't need to fill the site with placeholder content.

For the logo I used Photoshop and a free online font called "QUARTZO" to develop a quick and simple logo for use in the navbar.

<p align="center"><img src="https://i.imgur.com/CUzZ7gO.png" width="500"></p>

For the emotes displayed on the site, I developed several emotes of varying styles and emotions using Procreate on my Ipad prior to beginning the project and continuing during project development at times when I needed to take a break from coding.

I found that I'm happy I did this, as it enabled me to show the use case of the site more clearly instead of with placeholder imagery, and also allows me to show my design skill when displaying the project as a portfolio piece.

<p align="center"><img src="https://i.imgur.com/9SuUA8U.png" width="500"></p>

----
## Site Showcase

![Homepage](https://i.imgur.com/PwlCCaD.png)

![Signin](https://i.imgur.com/vfoBZqw.png)

![Emotes](https://i.imgur.com/o79PweK.png)

![My Favourites and My Emotes](https://i.imgur.com/4yshmHD.png)

![Profile](https://i.imgur.com/HJGHpBj.png)

----
## Future Implementations

There were several features during the initial ideation of the project that were cut based on scope and timing considerations. A couple others were cut during production due to issues with functionality for features that were lower down on the MOSCOW prioritisation.

### Cut During Production but Planned for future iterations

- Direct download button which serves image directly to local storage.
  - I attempted several times to get this working in the project, but issues arose with Cloudinary serving the image directly to the users computer and so the download button was temporarily changed to the option to view the full res image for "save as" functionality.
  - Additionally, save as png / jpg should be prevented by converting uploaded images to non "image" formats such as webp to prevent ease of download and ensure only registered users are downloading proper image files.

- Profile Pages Viewable by other users.
  - In future I'd like users to be able to view other user's profiles and see that users bio and uploads from the view. In that way, users can benefit from sharing their porftolio and details if people who find their emotes good wish to comission them etc.

- Filter by User and Profile Page changes (emotes gallery, edit profile behind button / modal)
  - In the current iteration of the project, the Profile page serves as a simple CRUD functionality proof of concept. But in future I'd like to develop it further into a fully functioning aspect of the project
  - Users will be able to click "creators" of emotes and visit their profile page. The Profile page will display the users display name rather than their security name, and will contain a gallery of their emotes.
  - Users will be able to search for emotes based on User as well as category.

### Further down the Road

- Paid Download Support
  - In future, I'd like to enable users to create emote "packs" or place payment restrictions on emote downloads. This would require significant implementation and possibly a redesign of the project but the learnings I've learned here should be applicable.

- Full Email Verification and User password Reset
  - At the moment, user sign in and login has been purposely kept relatively light due to time constraints and the scope of the project. In future, I'd like to have a more robust user registration that ensures emails are valid and has sufficient password reset functionality that serves reset emails to users.


## Compatibility / Accessibility 

### Device Compatibility & Responsiveness

As shown in the site showcase and Project introduction image, Moteify has been fully responsively tested to ensure that nothing breaks based on screen sizes down to 320px in width which is widely accepted as the key mobile display width range to aim for. full responsivity with. 

Throughout the sites development, changes were made to ensure that all device widths were compatible, although Bootstrap does a great job of assistance with this as a framework. 

Manual fixes however were made throughout the process with an extensive css file.

- I ensured all elements were viewable and did not break or overflow from large resolutions down to 320px.
- I ensured pagination options were made bigger and more easily clickable on Mobile devices.
- I ensured that small "Sign in" links were replaced with more easily clickable buttons.
- I ensured a responsive navbar was implemented and that all dropdowns functioned.
- I ensured that elements scaled responsively while retaining readability.

![Compatibility Display](https://i.imgur.com/ajc6wRL.png)

### Accessibility

I also ensured that elements on the page were labelled with aria labels appropriately to ensure the site functioned in collaboration with screen readers. Additionally, I ensured that buttons were clearly visible, and that messages informed users of actions taken.

## Bug Documentation

### Bug Documentation can be found here : [Bug Documentation](bugs.md)

## Technologies Used
- HTML
- CSS
- Python
- Javascript
- Git - Version control.
- Gitpod - Online cloudbased IDE for development.
- GitHub - Storage and management of code repository.
- GitHub Projects - Task Management and Agile workflow implementation.
- Django - Python Framework used as core pillar of project.
- Bootstrap - Framework for HTML elements.
- Cloudinary - Cloud-based media storage.
- ElephantSQL - Free option to host PostgresSQL database for the project.
- Heroku - Host the deployed Moteify app site.
- LucidChart - Development of the ERD and Flowcharts for the site.
- Procreate - Emote and asset creation
- Photoshop - Logo, Wireframing and ReadMe display images.
- Code Institute CI Python Linter - Python Manual Testing
- W3 Markup Validation Service - HTML & CSS Validation Testing.


## Libraries and Frameworks
- Bootstrap v5.3.2
- Django v 4.2.11
- Django AllAuth
- Django Crispy Forms
- Crispy Bootstrap
- Django RichTextField
- Whitenoise
- Gunicorn
- Pillow 

## Additional Tools
- tinypng - image webP-ification
- Autopep8 - Python Formatter
- GoogleFonts - Font searching and importing
- FontAwesome - Favicons
- ChatGPT - Debugging assistance and documentation research assistance.
- Imgur - ReadMe Image hosting

----
## Testing


### Extensive Validation and Manual Testing Performed and documented.<br> Test Documentation can be found here: [Testing Documentation](testing.md)

----
### Deployment

Django & Heroku Deployment was set up following the PDF provided by Code Institute below:
[Deployment Guide](documentation/Deployment.pdf)

----
### Credits & References 
- [Django Official Documenation](https://www.djangoproject.com)
- [Bootstrap Official Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Cloudinary Documentation](https://cloudinary.com/documentation)
- Code Institute - Code institutes Bootcamp Course Learning Platform content was referenced often during the project.
- [Daisy McGirr's Django Recipe App tutorial](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy) - Highly referenced resource in the development of the structure of this project.
- [Amylour's Free Fido Project](https://github.com/amylour/FreeFido_v2) - Amy linked this project to us as an example as a former student of Code institute. I used it for ReadMe Structure reference and to get ideas for how django apps similar to my own had been implemented.
- [Very Academy's Simple Blog app](https://www.youtube.com/watch?v=AF4ji8bb1M8&t=2s) - A great simple introductory lesson in Django which was a great reference.
- [Very Academy Favourites Features](https://www.youtube.com/watch?v=H4QPHLmsZMU) - I built a lot of my understanding on how to get favourites implemented with this tutorial.


----
### Acknowledgements
- Many thanks to **my colleagues** on the **TIAS Bootcamp 2023 - 2024** course. I've learned so much through our collaboration during Hackathon's and during meetings where we discussed bugs and difficulties we were experiencing. <br>
I feel as though our class was very supportive, always propping eachother up and looking out for one another and that community has really helped me get to where I am today and to get this project to the state that its in.

- Thank you to our facilitator **David Calikes**, who's unwavering support and transparency throughout this course was nothing short of wonderful. He has left an impression on me and I'm sure all of us on the course.

- Thank you to **Code Institute**, for providing me with an opportunity to reskill and enter the world of software development by collaborating with TIAS. Before starting this course, I was at a difficult point in my life, and I'm now looking forward to a future where I can reasonably begin to seek employment in an engaging and interesting industry.

- Thank you to **my partner and family** also who continued to support me through days where I was stuck in my room without seeing sunlight for these last 2 weeks of the course!

