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

<img src=" https://i.imgur.com/qm7p7XY.png">

- Using Labels, I assigned MOSCOW priortization to each user story, I could then view these within my Project Kanban board at any time and edit them accordingly if required as time and scope became more in question.

<p align="center"><img src="https://i.imgur.com/22h7aun.png"></p>

- I also used markdown check boxes to allow me to tick off more maneable bites of larger User Story tasks which proved both satisfying and useful.

You can find my Kanban board publically linked within the "projects" section of this Github Repo.

---
## Ideation
---


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
---
### Wireframes

Once I had the general idea for the site figured out and developed a majority of the user stories, I set about creating wireframes with that information in mind.

For the wireframing of the site I used **Photoshop** to sketch my initial ideal visual appearance of the site to aim for.

Understanding that the main aim for this project was to showcase Django implementation and CRUD functionality, I focused on creating an idea for how the pages could function mainly, as well as how they would look visually in an ideal final product.

Through my ideation and user stories development, I had a clear idea of the kinds of pages and features I would need.

<img src="https://i.imgur.com/zGTOM43.jpeg">

---
### Flow Chart

After creating my site wireframes and deciding on the scope of the project with user stories, I created and revised a site map and flow chart. This flow chart was informed by my wireframes and ideation and was developed and revised in tandem with my ERD during the initial stages of development:

<img src="https://i.imgur.com/RCICSDo.png">

---
### Entity Relationship Diagram (ERD)

The ERD displayed below is a revised version of an earlier diagram that was updated following project scope reductions and a development of model requirements during production. As an example, the default image entity as a standard "ImageField" was required as a bugfix to enable a default image to be displayed from static without the use of Cloudinary for users who had not yet uploaded one. 

The overall layout and design however was established in the initial version and in combination with the flowchart and wireframes developed proved as invaluable resources to more easily visualize what I wanted to develop.

<img src="https://i.imgur.com/KtKU3wa.png">

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

### Site Showcase


### Future Implementations

### Device Compatibility / Responsiveness

### Bug Documentation

### Technologies Used

### Libraries and Frameworks

### Additional Tools

### Deployment

### Testing

#### Extensive Validation and Manual Testing Performed and documented. Documentation can be found here:<br> [Testing Documentation](testing.md)

### Credits & References 

### Acknowledgements

