# Bug Testing Documentation

This bug testing was initially documented during production and stored within a Google Doc which I am now transferring here to markdown.

<i>As a note, many other bugs were discovered and resolved during the production of this project, and were undocumented largely due to a flow state in resolving and continuing work on the project or due to project completion taking precedence as the project deadline neared.

This document therefore isin't a complete documentation of all bugs encountered but rather a list of those that stood out to me during production where I learned a lot, along with those for which I was able to quickly jot down or document for reference</i>

## Technical Bugs

### Bug 01 Unlinked App in settings.py
Was encountering an error involving not being able to find the template index.html:

<i> get_template<br>raise TemplateDoesNotExist(template_name, chain=chain)<br>
django.template.exceptions.TemplateDoesNotExist: index.html</i>

Went through URLS / Views multiple times checking connections, making the path more literal by adding a /home folder etc. within the Home/Templates and giving it an app name within urls etc.

Realised after the issue was just that I hadn’t added ‘home’ to INSTALLED_APPS.!

Confirmed afterwords that basic site was working and CSS was being applied with Font Color: 

![Bug01](https://i.imgur.com/yPztB4g.png)


### Bug 02 Reverse URL error

Through troubleshooting,  discovered issue was due to the fact that I was using namespaces in my home urls, I needed to specify \ namespace: name of url \ to get the url working.

![Bug02.1](https://i.imgur.com/BFvRaR7.png)
<br>
Solution:

![Bug02.2](https://i.imgur.com/Tan6VPA.png)

### Bug 03 Navbar Dropdown Burger menu not functioning
Navbar Dropdown burger menu was not functioning.<br> This was due to data-toggle value being different across bootstrap versions and code I was referencing hadn’t been updated.<br>
Updated to data-toggle to data-bs-toggle and data-target to data-bs-target to resolve issue.<br>

Issue later occurred again in relation to attempting to fix the Sha vale of my bootstrap import which is documented further down in "Validation bugs".

### Bug 04 Profile Image not saving followed by Default Image not displaying
#### For this Bug, I wrote down my issues in real time as they occurred for reference so the bug is documented being fixed step by step:

I add an image in the form submission and save <br> <br>
It doesnt go to cloudinary, it goes to the profiles root folder and the link also links there instead of the cloudinary url

![Bug04.1](https://i.imgur.com/36VY3K0.png)

![Bug04.2](https://i.imgur.com/M9D6O74.png)

<br>

Changing from ResizeImageField back to CloudinaryField resolved issue but the issue is now that the image is huge, need to figure out how to correct size:

<br>

![Bug04.3](https://i.imgur.com/7plEk7u.png)

<br>

I had to zero my migrations for profile and recreate them as they werent picking up the changes I had added to the model to resize the profile image. That is now working, however now the default image is not loading:

<br>

![Bug04.4](https://i.imgur.com/PvNjOwH.png)

<br>

The code remains the same and I collected static but it is still not showing and the “src” shows as nothing in inspect element.

<br>

![Bug04.5](https://i.imgur.com/SVFVGxF.png)

<br>

Checking the admin profile image url, it seems as though I may have broken the data base with a lot of migrates as the profile image urls are all out of whack. <br>I have tried to resolve it now, but the default image still isin’t working:

<br>

![Bug04.6](https://i.imgur.com/oXgFHr5.png)

<br>

Trying to get a default image to be displayed from my projects static folder on the "My Profile" page.


I am serving images from my static folder correctly already, as can be displayed from my logo being displayed with the home button that uses {% static 'img/logo_temp.png' %}.
However, when I try to add the url path `"/static/img/user_default.png"` in the profile image Cloudinary field of the Profile model, it doesnt work.


Inspecting the element it seems to be adding a CLoudinary url to the start of the value:<br>
`<img src="http://res.cloudinary.com/dnqo4l2bd/image/upload/v1//static/img/user_default.png">`<br>
This only occurs in the CloudinaryField of the Model, because when I use the same url in the profile.html for debugging it shows

when a user uploads an image, it works fine. It is just the Default image displaying that is not functioning default image url is not routing to static folder and is instead adding cloudinary url on to the static/img/user_default.png

![Bug04.7](https://i.imgur.com/P5iQKt1.png)

Found out the following information through Debugging research:

<i>Your CloudinaryField is configured with a default value pointing to a static image (/static/img/user_default.png). However, the transformation parameter indicates that the image will be transformed by Cloudinary before it's displayed.
The transformation specified will resize and crop the image to fit within a resized bounding box.


When this field is accessed in your Django templates, the CloudinaryField will automatically generate a URL pointing to the Cloudinary-hosted version of the image, with the specified transformations applied. This is why you're seeing a Cloudinary URL instead of a direct path to your static image.


If you want to serve the image directly from your static folder without Cloudinary's transformation, you should either remove the transformation parameter or provide an empty list ([]) to it.</i>

Updated the Models.py to have a default image field that it serves from static if the user hasn't uploaded an image, and now functions.

![Bug04.8](https://i.imgur.com/Yitnfcm.png)

<br>

### Bug 05 Add Image form wont submit, raises error

`'InMemoryUploadedFile' object has no attribute 'width'
Request Method:	POST
Request URL:	http://8000-cianthornhill-moteify-9xqp3rbpowy.ws-eu110.gitpod.io/emotes/
Django Version:	4.2.11
Exception Type:	AttributeError
Exception Value:	
'InMemoryUploadedFile' object has no attribute 'width'
Exception Location:	/workspace/Moteify/emotes/forms.py, line 16, in clean_emote_img
Raised during:	emotes.views.AddEmote`

![Bug05.1](https://i.imgur.com/8Oo4Th9.png)

<br>
(realised this wouldnt work as users will be uploading from their computer, so would need another way to verify the width data of the image.)

Found out about Pillow, installed and edited code to make use of Pillows .open capabilities:

![Bug05.1](https://i.imgur.com/RVtqduP.png)

### Bug 06 Clicking “Download” just brings to cloudinary url of image instead of downloading the image to PC

![Bug06](https://i.imgur.com/bvHCOvj.png)

Extensive research was done on this bug and why cloudinary wouldnt serve files directly to the users pc on clicking download. Different solutions documented online were attempted to be implemented but failed to resolve the issue

Fix 01:
Cloudinary documentation mentioned the use of various parameters within the href attribute to force the download of the image to occur
- `fl_attachment`
- `?dl=`

Fix 02:
Create a Javascript functionality to serve the download instead:
- Sources online suggested implementing a javascript function to fetch the image file as a blob using the url, create a download and then simulate a click event ont he link being triggered.
- base implementations of this were attempted but proved slightly too complex to accomplish within the time constraints I had.

As this was at a later stage in the project, I decided instead to reduce the scope of the project as it wasn't high on the MOSCOW prioritisation and instead decided to just allow users to view the full image and "Save as". This has been implemented on other sites for similar reasons so I think it is an okay compromoise

### Bug 07 Favourites List view not working

![Bug 07.1](https://i.imgur.com/7mNdJDS.png)

<br>I received some Tutor support on this issue to help identify was happening, as I was struggling with it for awhile, pouring over my views.py, models.py etc.<br>
The issue that was occuring was actually within urls.py and it was that the URLpatterns were matching in the background:

![Bug 07.2](https://i.imgur.com/93Lxpiq.png)

![Bug 07.3](https://i.imgur.com/1oBWDF4.png)


### Bug 08 Favourites list pagination not working

Tried to reuse the List View code I had created to paginate the favourites page but could not get the pagination to work despite combing over the code and double checking. 


Solution: Realised after checking the documentation and creating a function based view that I had already defined a user favourites function based view in the views.py file which was causing issues with the new one. Edited the existing view to resolve:

https://docs.djangoproject.com/en/5.0/topics/pagination/

![Bug08](https://i.imgur.com/74Eqtan.png)

### Bug 09 Account deletion bug after adding “success message”

![Bug09](https://i.imgur.com/mqoTtc2.png)

Realised passing self as a parameter was the issue, as request is the parameter passed to the view function.

## Styling Bugs

### Bug S01 Card height being pushed by large text
![]()

![BS01](https://i.imgur.com/EDBfHtO.png)
<br>
Want cards to be a fixed height and width that remains able to deal with small responsive screens. 

Solution: Text should be limited to a certain number of characters that fits within this.
<i>Implemented a 25 character limit for titles after testing the max length before card height was affected</i>


### Bug S02 Pagination controls off to side of emotes, causing them to be pushed to left.

![BS02](https://i.imgur.com/b2mjiK9.png)
<br>
Flex controls were being displayed to right of the emotes images, convoluted swathes of bootstrap classes within html for quick prototyping were causing issues. Recreated the container styling with some basic CSS, leaving the bootstrap styling to handle cards and forms.

Emotes were then displaying in one long row and the pagination results were not centered, so adjusted the list-container with a max-width property to re-establish the more appealing 4 cards x 4 cards look and then justified the pagination div which contains the controls.

Solution: Re-created html styling, removing in-line bootstrap styling and replacing with more direct CSS styling. 
![BS022](https://i.imgur.com/NxBYmzU.png)
![BS023](https://i.imgur.com/i6RDJZ5.png)

### Bug S03 Large profile image causing styling issue

![BS03](https://i.imgur.com/SE43TPi.png)
<br>
Why styling Profile Page, noticed that the image was not scaling with the container and causing the page to be incompatible with smaller screen sizes.

Solution:
Set up class names for various profile page containers and then ensured that the image width was set to 100% of its container held within the overall container.

### Bug S04 My Profile Page incompatible with Screen size smaller than 338px

![BS04](https://i.imgur.com/ITuxvDE.png)

My profile page is heavy with several Bio, image elements etc, there is an area of the profile that doesn’t want to shrink past 308px.

Solution:
Generally, responsiveness is designed down to 320px width as a base, so for now due to project scope, implementing an overflow: scroll support to Main {}. 

Solution V2:
This caused issues displaying a horizontal and vertical scrollbar on homepage at full resolution for some reason despite not needing it. adjusting to overflow:auto resolved both.

### Bug S05 Background-image not adding to home-container class

Background-image property of CSS wasn’t applying to the home container and couldn’t figure out why. Attempted to use both Django templating language and standard file pathing to no avail.

![BS051](https://i.imgur.com/ecL8tXG.png)

![BS052](https://i.imgur.com/J1aD1bh.png)
<br>
Solution: Debug was unknowingly set to False. Following this discovered that css wants the default file pathing url rather than django templating. Django templating does not seem compatible with a .css file.
<br>

### Bug S06 Home Page images, unable to fill space
Homepage issue causing a small number of responsive sizes (including vertical ipad) to have unintended space showing in between home images. This is occurring from around to 830px width to 768px width which includes Vertical Ipad size.

![BS061](https://i.imgur.com/psPmZgm.png)

<br>
Solution: Added media query to adjust text size before the flex wrap comes into effect.
<br>

![BS062](https://i.imgur.com/zhbATYL.png)


## Validation Bugs

### B_V01 alt=”” used on I fav icons
HTML validator spotted that alt tags were applied to the i elements in the footer that were not applicable and threw errors for them

### B_V02  Potentially bad value sha512-... for attribute integrity on element script
Validator was giving a warning related to how I had linked the Bootstrap 5.3.2 CDN, in that my sha512 link was using a shortened hash value (This was likely due to searching for answers related to my drop down not working on stack overflow etc.)

Attempted to use the up to date 5.3 bootstrap CDN directly from bootstraps site but this caused my drop down in my nav bar to stop working.

Found the exact CDN for the bootstrap version I was running in the project using:
https://cdnjs.com/libraries/bootstrap/5.3.2


Then imported the appropriate Sha value.

