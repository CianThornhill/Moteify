# Validation Testing

## HTML and CSS

I used https://validator.w3.org on my html and CSS files.

---

### HTML Results:
| File | URL | Results |
|-----|-----|-----|
| Homepage |https://validator.w3.org/nu/?doc=https%3A%2F%2Fmoteify-5e8f7613a374.herokuapp.com%2F&showsource=yes| No Errors  |
| Signup  |https://validator.w3.org/nu/?doc=https%3A%2F%2Fmoteify-5e8f7613a374.herokuapp.com%2Faccounts%2Fsignup%2F&showsource=yes| No errors |
|Log in   |https://validator.w3.org/nu/?doc=https%3A%2F%2Fmoteify-5e8f7613a374.herokuapp.com%2Faccounts%2Flogin%2F&showsource=yes  | No Errors |
| Emotes |https://validator.w3.org/nu/?doc=https%3A%2F%2Fmoteify-5e8f7613a374.herokuapp.com%2Femotes%2F&showsource=yes| Warnings regarding possible misuse of aria-labels but have checked to ensure they are correct.|
| Add Emote  |https://validator.w3.org/nu/?doc=https%3A%2F%2Fmoteify-5e8f7613a374.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Femotes%2Fadd%2F&showsource=yes| No errors. Trailing slash on input marked as info  |
| Profile  |https://validator.w3.org/nu/?doc=https%3A%2F%2Fmoteify-5e8f7613a374.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Fprofiles%2F&showsource=yes| No errors. Trailing slash on input marked as info |
| Favourites  |https://validator.w3.org/nu/?doc=https%3A%2F%2Fmoteify-5e8f7613a374.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Femotes%2Ffavourite_emotes%2F&showsource=yes  |No errors. Trailing slash on input marked as info  |
| My Emotes |https://validator.w3.org/nu/?doc=https%3A%2F%2Fmoteify-5e8f7613a374.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Femotes%2Fmy_emotes%2F&showsource=yes| No errors. Trailing slash on input marked as info  |
|Log Out  |https://validator.w3.org/nu/?doc=https%3A%2F%2Fmoteify-5e8f7613a374.herokuapp.com%2F&showsource=yes| No errors  |
| Delete Account |https://validator.w3.org/nu/?doc=https%3A%2F%2Fmoteify-5e8f7613a374.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Fprofiles%2Fdelete_account%2F&showsource=yes| No errors. Trailing slash on input marked as info  |
|  |  |  |

### CSS Results
| File | Result | Notes |
| ---- | ---- | ---- |
| base.css | <img src="https://i.imgur.com/1fCQgsd.png"> | No errors found |
| | | |
Prior to completing the above tests, HTML validator had spotted 2 issues which were resolved prior to completing testing:

### Bug 1 
HTML validator spotted that alt tags were applied to the i elements in the footer that were not applicable and threw errors for them

### Bug 2
Validator was giving a warning related to how I had linked the Bootstrap 5.3.2 CDN, in that my sha512 link was using a shortened hash value (This was likely due to searching for answers related to my drop down not working on stack overflow etc.)

Attempted to use the up to date 5.3 bootstrap CDN directly from bootstraps site but this caused my drop down in my nav bar to stop working.

Found the exact CDN for the bootstrap version I was running in the project using:
https://cdnjs.com/libraries/bootstrap/5.3.2


Then added the appropriate script link with corect sha value to remove the validation errors.

----

## Python Validation

All Python Validation was completed by using https://pep8ci.herokuapp.com/# on my .py files. 

| File | Result | Notes |
| ---- | ---- | ---- |
| moteify: <br>settings.py | <img src="https://i.imgur.com/FuQBFx7.png"> | Line length note <br> however formatting was completed with autopep8 Python formatter |
| moetify:<br> urls.py  |<img src="https://i.imgur.com/X2n8oAS.png">  | No Errors  |
| emotes:<br> models.py | <img src="https://i.imgur.com/gNPmQ4X.png"> | Line length note <br> however formatting was completed with autopep8 Python formatter   |
| emotes:<br>views.py  | <img src="https://i.imgur.com/cM5f2m5.png"> | No errors  |
| emotes:<br>admin.py  | <img src="https://i.imgur.com/VrhotLS.png">| No errors  |
| emotes:<br>utils.py | <img src="https://i.imgur.com/QfSz9vb.png">  | No errors  |
| emotes:<br>forms.py | <img src="https://i.imgur.com/J5cNfO8.png"> | No errors  |
| home:<br>urls.py<br>views.py  | img not included due to small size of files and effect of app |No errors  |
| profiles:<br>models.py | <img src="https://i.imgur.com/vRtPqxE.png"> | No errors  |
| profiles:<br>urls.py | <img src="https://i.imgur.com/XcVxydp.png"> | No errors |
| profiles:<br> views.py | <img src="https://i.imgur.com/A6ZBPZL.png"> |  Line length note <br> however formatting was completed with autopep8 Python formatter  |
| python:<br>forms.py | <img src="https://i.imgur.com/9WwVW26.png"> | No errors  |
| python:<br>admin.py | <img src="https://i.imgur.com/zRLZ1tR.png"> | No errors  |
|  | |  |

## Manual Testing
### Unregistered / Non Logged in user
| Page / Element | Action | Expected Outcome | Result |
|----|----|----|----|
|  |  |  |  |
| Navbar | Click Logo | Links to Homepage | Pass |
| Navbar | Click "Home"| Links to Homepage| Pass |
| Navbar | Click "Emotes"| Links to Emotes page| Pass |
| Navbar | Click "Register" | Links to Registration | Pass |
| Navbar | Click "Login" | Links to Login Page  | Pass |
| Emotes | Select "category" from dropdown and click filter | Emotes are filtered to show only<br>emotes of that category  | Pass  |
| Emotes  | View individual emote by clicking | User is brought to individual emote page  | Pass |
| Emote_detail | View access only | User can view emote but not favourite or view full image.<br>User also cannot edit or delete emote. | Pass |
| Footer  | Click Social Icons  | Links to various socials in new tab | Pass  |
| Signup | Fill form with valid details and submit with "signup" button  | User is signed up, logged in and brought to their newly created profile page.  | Pass |
| Signup  | Click "Already have an account? [Sign in]"  | User is brought to log in page  | Pass |
| Login | Enter Correct Details and "sign in"| User is redirected to emotes  | Pass  |
| Login | Forgot Password link | redirects to forgot password reset workflow<br>[Password reset link not functioning at this time]<br>Temporary password reset info added | Pass <br> Reset not implemented  |

### Logged in User
| Page / Element | Action | Expected Outcome | Result |
|----|----|----|----|
|  |  |  |  |
| Navbar | Click Logo | Links to Homepage | Pass |
| Navbar | Click "Emotes"| Links to Emotes page| Pass |
| Navbar | Click "Add Emote" | Links to Emote Upload form  |  |
| Navbar | Click "My Profile" | Shows Dropdown options<br> - View profile <br> - My favourites <br> - My Emotes | Pass |
| Navbar | Click My Profile Drop down options | All options link to appropriate pages | Pass |
| Add Emote | Click "Save" after adding valid details | Emote added and displayed on "emotes" page<br>User is redirected to emotes  | Pass |
| Add Emote | Click "Save" after submitting invalid details | Form does not submit<br>-appropriate help text highlighted | Pass |
| Emote Detail  | Emote owner view | Emote owner can view Edit and Delete options | Pass |
| Emote Detail | Emote owner clicks "edit"  | Emote owner brought to edit form page  | Pass |
| Emote Edit  | Emote owner submits valid edit form | Emote is edited and user is redirected back to emotes | Pass |
| Emote Edit | Click "Save" after submitting invalid details | Form does not submit<br>-appropriate help text highlighted | Pass |
| Emote Detail  | Emote owner clicks "delete" | Emote owner brought to Delete page | Pass |
| Emote Delete | Emote owner clicks "confirm" | Emote is deleted from database and no longer shown<br>User is redirected back to emotes  | Pass |
| Profile  | User enters unedited Profile Page| User is shown default values and Edit Form | Pass |
| Profile  | User clicks submits valid Edit form | Profile is updated with new information and displayed | Pass |
| Profile | User clicks "favourites" or "my emotes"| User is brought to appropriate favourites or my emotes page  | Pass  |
| My Emotes | User views their emotes | User is shown only their uploads | Pass  |
| My Favourites | User views their favourites  | User is shown only their favourites  | Pass  |
| My Emotes | User clicks an emote  | User is brought to that emotes individual view | Pass |
| My Favourites | User clicks an emote  | User is brought to that emotes individual view | Pass |
| Emote Detail | User clicks "Favourite" button | Emote is Favourited or Unfavourited depending on status<br>- And is then displayed in user's favourites  | Pass  |
| Emote Detail | User clicks "View Full image" | User is shown full image view so that they can "save as" | Pass |
| Navbar  | User clicks "Logout" | User is brought to logout Page | Pass  |
| Logout | User clicks "Sign Out" | User is Signed Out and redirected to Homepae<br> - Navbar updated accordingly to non-logged in options | Pass |
| Profile | User clicks "delete account" button  | User is brought to delete account confirmation page | Pass |
| Delete Account | User confirms accoutn deletion | User's account and their associated content is also deleted<br> - Note: User is redirected to emotes instead of home for some reason but believe this is okay. | Pass |
|  |  |  |  |
