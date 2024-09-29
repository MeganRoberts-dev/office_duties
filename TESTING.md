# Testing

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| templates | add_duty.html | ![screenshot](/static/documentation/validation/html-add-duty.png) | |
| templates | edit_duty.html | ![screenshot](/static/documentation/validation/html-edit.png) | |
| templates | home.html | ![screenshot](/static/documentation/validation/html-home.png) | |
| templates | login.html | ![screenshot](/static/documentation/validation/html-login.png) | |
| templates | profile.html | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| templates | register.html | ![screenshot](/static/documentation/validation/html-register.png) | |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | styles.css | ![screenshot](/static/documentation/validation/css.png) | |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | main.js | ![screenshot](/static/documentation/validation/javscript.png) | Two minor warnings |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
|  | app.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MeganRoberts-dev/office_duties/main/app.py) | ![screenshot](/static/documentation/validation/python.png) | A few minor warnings but nothing to cause conern|

## Browser Compatibility

| Browser | Site |  Notes |
| --- | --- | --- |
| Chrome | ![screenshot](/static/documentation/features/login-page.png) | Works as expected |
| Firefox | ![screenshot](/static/documentation/browsers/firefox.png) | Works as expected |
| Edge | ![screenshot](/static/documentation/browsers/edge.png) | Works as expected |
| Opera | ![screenshot](/static/documentation/browsers/opera.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Login | Register | Home | Add Duty | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](/static/documentation/responsivness/login-response-mobile.png) | ![screenshot](/static/documentation/responsivness/resgister-response-mobile.png) | ![screenshot](/static/documentation/responsivness/home-response-mobile.png) | ![screenshot](/static/documentation/responsivness/add-duty-response-mobile.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](/static/documentation/responsivness/tablet-login-response.png) | ![screenshot](/static/documentation/responsivness/register-tablet-response.png) | ![screenshot](/static/documentation/responsivness/tablet-home-response.png) | ![screenshot](/static/documentation/responsivness/tablet-add-duty-response.png) | Works as expected |
| Desktop | ![screenshot](/static/documentation/features/login-page.png) | ![screenshot](/static/documentation/features/register-page.png) | ![screenshot](/static/documentation/features/home-page.png) | ![screenshot](/static/documentation/features/add-duty-page.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Login | ![screenshot](/static/documentation/lighthouse/mobile-login.png) | ![screenshot](/static/documentation/lighthouse/desktop-login.png) | No warnings |
| Add Duty| ![screenshot](/static/documentation/lighthouse/add-duty.png) | ![screenshot](/static/documentation/lighthouse/add-duty-desktop.png) | No warnings |

> [!NOTE]  
> Due to login and security credentials, I am unable to perform a Lighthouse audit on the home page directly; however, based on the successful results from auditing the login and add duty pages, I can reasonably assume that the home page would also meet the same performance and accessibility standards.

## Defensive Programming

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Defensive programming (defensive design) is extremely important!

When building projects that accept user inputs or forms, you should always test the level of security for each.
Examples of this could include (not limited to):

Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses

PP3 (Python-only):
- Users must enter a valid letter/word/string when prompted
- Users must choose from a specific list only

MS3 (Flask) | MS4/PP4/PP5 (Django):
- Users cannot brute-force a URL to navigate to a restricted page
- Users cannot perform CRUD functionality while logged-out
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers

You'll want to test all functionality on your application, whether it's a standard form,
or uses CRUD functionality for data manipulation on a database.
Make sure to include the `required` attribute on any form-fields that should be mandatory.
Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser).

You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable.
Ideally, tests cases should focus on each individual section of every page on the website.
Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine,
consider documenting tests on each element of the page
(ie. button clicks, input box validation, navigation links, etc.) by testing them in their happy flow,
and also the bad/exception flow, mentioning the expected and observed results,
and drawing a parallel between them where applicable.

Consider using the following format for manual test cases:

Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature01.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature02.png) |
| About | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature03.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature04.png) |
| Gallery | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature05.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature06.png) |
| Contact | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature07.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature08.png) |
| repeat for all remaining pages | x | x | x | x | x |

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Another way of performing defensive testing is a simple Pass/Fail for each test.
The assessors prefer the above method, with the full test explained, but this is also acceptable in most cases.

When in doubt, use the above method instead, and delete the table below.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Gallery | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | |
| | Load gallery images | All images load as expected | Pass | |
| Contact | | | | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | Click the Submit button | Redirects user to form-dump | Pass | User must click 'Back' button to return |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Profile | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on the Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |
| repeat for all remaining pages | x | x | x | x |

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Repeat for all other tests, as applicable to your own site.
The aforementioned tests are just an example of a few different project scenarios.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to register to the site, so that I can enter and use the application. | ![screenshot](/static/documentation/features/register-page.png) |
| As a new site user, I would like to log in securely, so that I can manage my duties privately and access them from any device | ![screenshot](/static/documentation/features/login-page.png) |
| As a new site user, I would like to create and organize my tasks easily, so that I can stay on top of my work responsibilities without hassle. | ![screenshot](/static/documentation/features/task-sheets.png) |
| As a new site user, I would like to edit or delete completed tasks, so that I can keep my task list up-to-date and clutter-free | ![screenshot](/static/documentation/features/edit-page.png) |
| As a new site user, I would like to mark my tasks as completed, so that I can track my progress and feel a sense of accomplishment. | ![screenshot](/static/documentation/features/task-sheets.png) |
| As a new site user, I would like to receive motivational prompts, so that I can stay focused and productive throughout the day.| ![screenshot](/static/documentation/features/motivational-header.png) |

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

## Bugs

- Aria-describedby tag bug

    ![screenshot](/static/documentation/bugs/bug-1.png)

    - To fix this, I add aria-describedby="usernameHelp". This ensures that the input field points to an element that provides additional information about the input..

- Unnecessary backrground-attachmeent tag.


    ![screenshot](/static/documentation/bugs/bug-2.png)

    - To fix this, I removed the backrgound-attachment fixed line.

- Conflicting bootstrap code.

    ![screenshot](/static/documentation/bugs/bug-3.png)

    - To fix this, I named the container a different class name, this way I could edit the ccs wwithout it conflicting with boostrap syntax. 

- Python not checking username.

    ![screenshot](/static/documentation/bugs/bug-4.png)

    - To fix this, I enusred the code was retrieving and comparing the session["user"] value with the correct field (e.g., "username") from the database, using session.get("user") == owner["username"] for a proper comparison..


## Unfixed Bugs

> [!NOTE]  
> There are no remaining bugs that I am aware of.
