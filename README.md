# [OFFICE DUTIES](https://office-duties-6b592fba2b58.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/MeganRoberts-dev/office_duties)](https://github.com/MeganRoberts-dev/office_duties/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/MeganRoberts-dev/office_duties)](https://github.com/MeganRoberts-dev/office_duties/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/MeganRoberts-dev/office_duties)](https://github.com/MeganRoberts-dev/office_duties)

---

![screenshot](/static/documentation/mockup.png)

---

source: [amiresponsive](https://ui.dev/amiresponsive?url=https://office-duties-6b592fba2b58.herokuapp.com)

## Website Overview

**Office Duties** is a sleek, modern task management app that puts users in full control of their work responsibilities with minimal effort. Adding, editing, and deleting tasks has never been this simple! Built for both efficiency and ease, Office Duties streamlines task management, transforming your workflow into something intuitive and stress-free. Plus, with motivational prompts running in the background to keep you inspired, you'll stay productive and focused throughout the day. Whether you're juggling multiple projects or just handling daily to-dos, this app ensures you remain organized, on top of your game, and in charge.

## UX

The design of Office Duties is purposefully crafted to create a calm and refreshing environment for managing tasks. The pastel color palette—featuring soft pinks, greens, purples, blues, and beige—offers a soothing visual experience, helping to ease the stress that often comes with work. Garden-inspired elements subtly remind users of the outdoors, boosting both mood and focus. To keep users motivated, uplifting prompts run throughout the app, ensuring productivity and positivity stay high as you navigate your daily duties.

### Colour Scheme

The primary coulors in **Office Duties** are pastel pinks, greens, purples, blues, and beige. These were chosen to match the subtle garden-themed background, which ties into the calming concept of the site. While softer tones dominate the overall design, darker shades are incorporated in the tasks sections for contrast, giving users a sense of accomplishment. This combination of colors and design elements offers a visually refreshing experience, promoting both focus and relaxation.

- `#2A2D34` used for the headers.
- `#4560A3` used for motivational header.
- `#C47886` used for Office Dutties title.

[coolors.co](https://coolors.co/e84610-009fe3-4a4a4f-445261-d63649-e6ecf0-000000) was used to generate the colour palette.

![screenshot](/static/documentation/coloured-pad.png)

### Typography

- [Fira Sans](https://fonts.google.com/specimen/Fira+Sans) was used for the primary text.

- [Playwrite Deutschland Grundschrift](https://fonts.google.com/specimen/Playwrite+DE+Grund) was used for the motivational header.

- [Bootstrap icons](https://icons.getbootstrap.com/?q=check) was used for icons on the incomplete and completed lists.


## User Stories

### New Site Users

- As a new site user, I would like to register to the site, so that I can enter and use the application.
- As a new site user, I would like to log in securely, so that I can manage my duties privately and access them from any device.
- As a new site user, I would like to create and organize my tasks easily, so that I can stay on top of my work responsibilities without hassle.
- As a new site user, I would like to edit or delete completed tasks, so that I can keep my task list up-to-date and clutter-free.
- As a new site user, I would like to mark my tasks as completed, so that I can track my progress and feel a sense of accomplishment.
- As a new site user, I would like to receive motivational prompts, so that I can stay focused and productive throughout the day.

### Returning Site Users

- As a returning site user, I would like to quickly view my pending tasks, so that I can prioritize my work for the day.
- As a returning site user, I would like to edit existing duties, so that I can update details or track changes in my responsibilities.
- As a returning site user, I would like to check off completed tasks, so that I can keep my to-do list current and organized.
- As a returning site user, I would like to access my duties seamlessly from different devices, so that I can manage my tasks anytime and anywhere.


### Site Admin

- As a site administrator, I should be able to manage user accounts, so that I can ensure proper access and security for all users.
- As a site administrator, I should be able to track user activity, so that I can monitor engagement and troubleshoot any issues.
- As a site administrator, I should be able to edit or update the app’s content, so that I can keep the platform relevant and functional for users.
- As a site administrator, I should be able to reset or assist with forgotten passwords, so that I can help users regain access quickly and securely.


## Wireframes

Wireframes for dekstop, tablet and mobile were created using the devleopling tool
[Figma](https://www.figma.com/).


 | Desktop  | Tablet  | Mobile |
| :------------ |:---------------:| -----:|
|  ![screenshot](/static/documentation/wireframe/desktop-wireframe.png)   | ![screenshot](/static/documentation/wireframe/tablet-wireframe.png)  |![screenshot](/static/documentation/wireframe/mobile-wireframe.png) |

## Features
### Existing Features
- **Register page**

    - The registration page provides a secure way for new users to create an account, ensuring their personal information is protected from the start. By requiring a strong password and validating user details, this feature helps maintain the integrity of the data stored in MongoDB. Users can quickly set up their accounts and gain access to a personalized task management experience, allowing them to efficiently manage their duties while keeping their information safe and secure.

![screenshot](/static/documentation/features/register-page.png)

- **Login page**

    - The login page ensures secure access to users' tasks by requiring authentication, protecting personal information with robust password safety measures. User data is stored securely in MongoDB, maintaining privacy and integrity. This feature allows users to manage their duties easily and access their accounts from any device, providing a seamless and secure experience for handling daily responsibilities.

![screenshot](/static/documentation/features/login-page.png)

- **Motivational header**

    - The motivational header enhances the user experience by delivering fresh, uplifting messages that change every five seconds. This feature keeps users inspired and engaged while they manage their tasks, providing a continuous boost of positivity. By integrating these dynamic prompts, the app creates an encouraging atmosphere that motivates users to stay focused and productive throughout their day.

![Motivational Header](/static/documentation/features/motivational-header.png) 


- **Task sheets**

    - The task sheets are designed to streamline task management by separating incomplete and completed tasks for better organization. Users can easily edit tasks in the incomplete sheet, allowing for quick updates or modifications. When a task is finished, clicking the tick icon moves it to the completed sheet, providing a clear visual of progress made. Additionally, users can delete tasks from the completed sheet by pressing the trash icon, ensuring their task lists remain tidy and relevant. This intuitive design simplifies the task management process, making it easy for users to stay on top of their responsibilities.

![screenshot](/static/documentation/features/task-sheets.png)

- **Add duty page**

    - The add duty page allows users to effortlessly create new tasks by entering a title and a detailed description. This intuitive interface ensures that all relevant information is captured, making it easy to define responsibilities clearly. Once a task is added, it is securely stored in MongoDB and seamlessly integrated into the user’s task list, enabling them to stay organized and on top of their workload. This straightforward functionality empowers users to take control of their task management by adding duties that align with their goals and priorities.

![screenshot](/static/documentation/features/add-duty-page.png)

- **Edit page**

    - The edit page provides users with the ability to easily modify the title or description of any task, ensuring their task lists remain accurate and up-to-date. In addition to these edits, users can also mark tasks as complete directly from this page. Any changes made will automatically reflect on the home page, allowing for seamless task management. This user-friendly interface makes it simple to keep responsibilities organized and aligned with current priorities, enhancing overall productivity and efficiency.

![screenshot](/static/documentation/features/edit-page.png)

### Future Features

- Recurring Tasks Feature
    - Implement a recurring tasks functionality that allows users to set daily, weekly, or monthly tasks. This would streamline task management for responsibilities that need to be completed regularly. Consider adding a user-friendly interface for selecting the recurrence frequency and duration.
- Collaborative Task Management
    - Introduce a feature that enables users to share tasks with team members or collaborate on duties. This could include assigning tasks to specific users, adding comments, and tracking progress collectively. This feature could enhance teamwork and improve accountability among users.

## Tools & Technologies Used

- [![Markdown Builder](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://tim.2bn.dev/markdown-builder) used to generate README and TESTING templates.
- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.
- ⚠️⚠️ IDE: CHOOSE ONLY ONE <-- delete me ⚠️⚠️
- [![Gitpod](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) used as a cloud-based IDE for development.
- [![Codeanywhere](https://img.shields.io/badge/Codeanywhere-grey?logo=ebox&logoColor=7F3F98)](https://codeanywhere.com) used as a cloud-based IDE for development.
- [![HTML](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [![CSS](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [![JavaScript](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) used for user interaction on the site.
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- [![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-grey?logo=githubpages&logoColor=222222)](https://pages.github.com) used for hosting the deployed front-end site.
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed back-end site.
- ⚠️⚠️ CSS FRAMEWORKS: CHOOSE ONLY ONE (if applicable) <-- delete me ⚠️⚠️
- [![Bootstrap](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [![Flask](https://img.shields.io/badge/Flask-grey?logo=flask&logoColor=000000)](https://flask.palletsprojects.com) used as the Python framework for the site.
- [![MongoDB](https://img.shields.io/badge/MongoDB-grey?logo=mongodb&logoColor=47A248)](https://www.mongodb.com) used as the non-relational database management with Flask.
- [![ChatGPT](https://img.shields.io/badge/ChatGPT-grey?logo=chromatic&logoColor=75A99C)](https://chat.openai.com) used to help debug, troubleshoot, and explain things.

## Database Design

My project uses a non-relational database with MongoDB, and therefore the database architecture
doesn't have actual relationships like a relational database would.

My database is called **office_duties**.

It contains 3 collections:

- **categories**
    | Key | Type | Notes |
    | --- | --- | --- |
    | _id | ObjectId() | |
    | category_name | String | |

- **tasks**
    | Key | Type | Notes |
    | --- | --- | --- |
    | _id | ObjectId() | |
    | category_name | String | selected from *categories* collection |
    | task_name | String | |
    | task_description | String | |
    | is_urgent | String | |
    | due_date | String | |
    | created_by | String | selected from the *users* collection |

- **users**
    | Key | Type | Notes |
    | --- | --- | --- |
    | _id | ObjectId() | |
    | username | String | |
    | password | String | uses Secure Hash Algorithm (SHA) |

I have also used Mermaid to build an interactive version of my database schema.

```mermaid
erDiagram
    CATEGORIES {
        ObjectId _id
        String category_name
    }
    
    TASKS {
        ObjectId _id
        String category_name
        String task_name
        String task_description
        String is_urgent
        String due_date
        String created_by
    }
    
    USERS {
        ObjectId _id
        String username
        String password
    }

    CATEGORIES ||--o TASKS : has
    USERS ||--o TASKS : "created by"
```

Source: [Mermaid](https://mermaid.live/edit#pako:eNqlUk1Lw0AQ_SthzmlJUkPN3ooWKR4KTb1IIGyzY7rW7Ib9QGPMf3fbBC2miOAcZuG9-Xgzsy0UkiEQQHXLaalolQnP2c1iu7xbb1bL1Gt75Gjr3TMWZsW8nLNvNDWKi9IrqMFSqiYXtMKe7fqn99tFev-vamesofrwC8NQF4rXhksxCuA6t6pEYUYMs5gz13asRaGDWb5rLoz1kC43fx_LalQXdddU61ep2FeH0R0-PiYT2Q5rJN6e6nMBP9gMBtGeEw3gQ4Wqopy5S5-kZmD26GTAMZRRdcggE52Lo9bItBEFEKMs-mDr40qGvwHkib5oh9ZUAGnhDUh4nUzDcB5GcZBE81k0j31ogASdD-9SuoxgmvR2FcySeBbH0Sn98UT2PZS05X6o3X0C8wvFkA) 


## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://office-duties-6b592fba2b58.herokuapp.com).

### MongoDB Non-Relational Database

This project uses [MongoDB](https://www.mongodb.com) for the Non-Relational Database.

To obtain your own MongoDB Database URI, sign-up on their site, then follow these steps:

- The name of the database on MongoDB should be called **insert-your-database-name-here**.
- The collection(s) needed for this database should be **insert-your-collection-names-here**.
- Click on the **Cluster** name created for the project.
- Click on the **Connect** button.
- Click **Connect Your Application**.
- Copy the connection string, and replace `password` with your own password (also remove the angle-brackets).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key | Value |
| --- | --- |
| `DATABASE_URL` | user's own value |
| `IP` | 0.0.0.0 |
| `MONGO_DBNAME` | user's own value |
| `MONGO_URI` | user's own value |
| `PORT` | 5000 |
| `SECRET_KEY` | user's own value |

Heroku needs three additional files in order to deploy properly.

- requirements.txt
- Procfile
- runtime.txt

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: python app.py > Procfile`
- *replace **app.py** with the name of your primary Flask app name; the one at the root-level*

The **runtime.txt** file needs to know which Python version you're using:
1. type: `python3 --version` in the terminal.
2. in the **runtime.txt** file, add your Python version:
	- `python-3.9.19`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/MeganRoberts-dev/office_duties) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git shell or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/MeganRoberts-dev/office_duties.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/MeganRoberts-dev/office_duties)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/MeganRoberts-dev/office_duties)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

## Credits
- [ToDoList.com website](https://todoist.com/)
- [Fit Horse](https://github.com/MeganRoberts-dev/fit_horse)
- [Honey Bee](https://github.com/mikiburgess/MP3-Honey-Bee)
- [To Do List API ](https://github.com/JeanMichelBB/ToDoListAPI)
- [YouTube How to create a to do list](https://www.youtube.com/watch?v=1ceS673MMwo)

### Content

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://tim.2bn.dev/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [YouTube](https://www.youtube.com/watch?v=PvMDWbAPPK4) | Entire site | I used this video to learn about applying mongoDB and building a to do list |
| [YouTube](https://www.youtube.com/watch?v=izQGdZvRs7I) | Entire site | I used this video to learn about building a to do list |
| [YouTube](https://www.youtube.com/watch?v=8DvywoWv6fI) | Entire site | I used this video to learn more about python |
| [Code Institute](https://learn.codeinstitute.net/dashboard) | Entire site| I would often refrences notes from the learning modules when writing parts of the site |

### Media

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [Pngtree](https://pngtree.com/) | Entire site | Bakcground and images| Source of backrgound image the pin and trophy images |
| [Freepik](https://www.freepik.com/) | 404 page | Backrgound | Office image |

### Acknowledgements
> [!IMPORTANT]  
> A heartfelt thank you to Code Institute for the exceptional learning material that inspired and guided this project. A special note of gratitude goes to my Code Institute mentor, TTim Nelson, for his steadfast support, encouragement, and invaluable advice throughout this rewarding journey. Additionally, I want to thank my co-wokers for prompting me with this grest idea.