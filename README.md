# Minesweeper 

## Python 3 Project by Mateusz Leks
---
<br>

![ami.responsive](assets/readme_files/ami.responsivep3.png)

# Project introduction

This is a back end application with a purpose of creating a game of minesweeper in command-line using Python3.

Minesweeper is run in code institutes custom terminal running on the [Heroku](https://www.heroku.com/home) platform.


[Click here to access and play!](https://minesweeper-matt.herokuapp.com/)
-
<br>
(I recommend users to open links in this README with CTRL + left mouse button (Windows) Control + click, for Mac)

To find out more about [Minesweeper](https://en.wikipedia.org/wiki/Minesweeper_(video_game)) - Click here!!

# Content Navigation
- [UX](#ux)
  * [User stories](#user-stories)
  * [Features](#features)
- [Application design](#application-design)
- [Planning](#planning)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Validation](#validation)
- [Site Deployment](#site-deployment)
- [Credits](#credits)
- [Media](#media)
- [Acknowledgements](#acknowledgements)
# UX

## User stories
* New Users
    1. As a new user I want the game rules to be digestable.
    2. As a new user I want to receieve feedback in terminal for my input.
    3. As a new user I want to play a clearly laid out game.
    4. As a new user I want to be able to restart the game or quit if I wish.

* Returning Users
    1. As a returning user I want to see updated features and bug fixes.
    2. As a returning user I want to see more difficulty options to further test my skils.
    3. As a returning user I want to be able to time a playthrough.
    4. As a returning user I want to see a high scores / game score feature.

## Features
* Username selection
* Randomised Game grid
* Randomised Mine placement
* Flagging mines
* Game Restart 

# Application design


# Planning

# Technologies Used

# Testing

# Validation

# Site Deployment 
* Deploying project to Heroku - [Live Link](https://minesweeper-matt.herokuapp.com/)

    * This project was created with Code institutes Portfolio 3 template.

## Cloning using Github
* Log in to Github.
* Access my repository using above link.
* In repository page select code next to Gitpod.
* Button, make sure HTTPS is selected.
* Click on the copy button on the right (Two overlapping squares)
* Open a new workspace in Gitpod.
* Once the workspace loads in the terminal type.
```
git clone https://github.com/Matex600/minesweeper-matt
```
* This command will now clone this repo for use in your Gitpod.
* In Gitpod workspaces click the three dots and pin workspace to avoid losing it!
* Do not use the Gitpod button in Github again when you have your workspace already set up to avoid losing data.

## Deployment via Heroku
* Go to [Heroku](https://www.heroku.com/home).
* Log in to your account.
* Once in your Dashboard, Create new app
* Select an app name and a region and press create app
* You have now created a Heroku app
* Navigate to the settings tab
* Click on the Reveal Config Vars button
* If you have a creds.json file in gitpod add a 
Key with name CREDS
* In the Value section copy and paste contents from creds.json file.
* For the second key this one is required for the app to work once deployed
* In Key enter PORT for Value enter 8000.
* Select Add
* Scroll down to Buildpacks section
* Once in this section click on Add Buildpack, Select Python
* Repeat above action but select node.js instead.
* Once this is completed Ensure that Python is above node.js within the list.
* Navigate to the Deploy tab
* In the deployment section select Github
* Enter the Repo name and once you have found the corresponding repo confirm the selection.
* Scroll down to Enable Automatic Deploys and enable this feature to ensure automatic updates everytime you use git push in gitpod.
* Lastly to deploy click on deploy branch in manual deploy this could take up to a few minutes.
* Once deployed successfully a message will appear and a View button taking you to the deployed app if nothing is showing allow some time for Heroku to work.

# Credits

## Media
[amiresponsive](http://ami.responsivedesign.is/) - For use of their site to add image to top of my README.

## Acknowledgements

My mentor Maranatha Ilesanmi has helped motivate me throughout this project and offer useful advice on how to further improve my knowledge.

[Code Institute](https://codeinstitute.net/) - For providing me with learning material that has prepared me for this Python in terminal project.

[FreeCodeCamp](https://www.youtube.com/watch?v=rfscVS0vtbw) - For helping me understand Python further.

[Lucid Chart](https://www.lucidchart.com/pages/examples/flowchart-maker) - For helping my map out my code logic