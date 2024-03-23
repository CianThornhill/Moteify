# Validation Testing

## HTML and CSS

I used https://validator.w3.org on my html and CSS files.

---

### Results:
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