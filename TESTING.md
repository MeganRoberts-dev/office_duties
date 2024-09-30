# Testing

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| Templates | add_duty.html | ![screenshot](/static/documentation/validation/html-add-duty.png) | Pass |
| Templates | edit_duty.html | ![screenshot](/static/documentation/validation/html-edit.png) | Pass |
| Templates | home.html | ![screenshot](/static/documentation/validation/html-home.png) | Pass |
| Templates | login.html | ![screenshot](/static/documentation/validation/html-login.png) | Pass |
| Templates | register.html | ![screenshot](/static/documentation/validation/html-register.png) | Pass |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| Static | styles.css | ![screenshot](/static/documentation/validation/css.png) | Pass |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| Static | main.js | ![screenshot](/static/documentation/validation/javscript.png) | Two minor warnings |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
|  | app.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/MeganRoberts-dev/office_duties/main/app.py) | ![screenshot](/static/documentation/validation/python-pep8.png) | Pass|

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

| Page | User Action | Expected Result | Pass/Fail | Screenshot |
| --- | --- | --- | --- | --- | 
| Home | | | | | 
| | Click on Logo | Redirection to Home page | Pass | ![screenshot](/static/documentation/CRUD/logo.png)|
| | Click on Logout| Returns user to login page and logs out of their profile | Pass | [screenshot](/static/documentation/CRUD/logout.png) |
| | Click on My Duty| Returns user to their profile | Pass | ![screenshot](/static/documentation/CRUD/my-duty.png) |
| | Click on edit and complete button | Edit button redirects user to Edit page and Complete button moves task to complete sheet | Pass | ![screenshot](/static/documentation/CRUD/edit-button.png) |
| | Click on delete button| Moves task to completed task sheet | Pass | ![screenshot](/static/documentation/CRUD/delete.png) |
| Add Duty Page | | | | | |
| | Enter form boxes and click add button | Field will accept freeform text and add button will add the task to home oage | Pass | ![screenshot](/static/documentation/CRUD/edit-button.png) |
| Edit page | | | | | |
| | Edit content | Ability to change content | Pass | ![screenshot](/static/documentation/CRUD/edit-text.png) |
| | Complete button | Move task to complete sheet | Pass | ![screenshot](/static/documentation/CRUD/edit-complete.png.png) |
| | Update button | Update the changed content on the home page | Pass | ![screenshot](/static/documentation/CRUD/edit-complete.png) |
| Register | | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | ![screenshot](/static/documentation/CRUD/register.png)|
| | Enter valid username | Field will only accept email address format | Pass | ![screenshot](/static/documentation/CRUD/register.png.png) |
| | Enter valid password | Field will only accept password format | Pass | ![screenshot](/static/documentation/CRUD/register.png)|
| | Click on register button | Redirects user to blank Sign In page and saves credentials | Pass | ![screenshot](/static/documentation/CRUD/register-btn.png) |
| Log In | | | | | |
| | Click on the Login link | Redirection to Login page | Pass | ![screenshot](/static/documentation/CRUD/login-btn.png) |
| | Enter valid username | Field will only accept username that has signed-up | Pass | ![screenshot](/static/documentation/CRUD/login-content.png) |
| | Enter valid password | Field will only accept password that has signed-up with matching username | Pass | ![screenshot](/static/documentation/CRUD/login-content.png) |
| | Click Login button | Redirects user to home page | Pass | ![screenshot](/static/documentation/CRUD/login-home.png)|
| Profile | | | | | |
| | Content | User tasks will all be saved since last sessions | Pass | ![screenshot](/static/documentation/CRUD/home-saves.png)|
| | Flash messages | Any incorrect login details, brute force, completed / edited or deleted tasks will prompt a flash message| Pass | ![screenshot](/static/documentation/CRUD/flash-message.png)  |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |


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
