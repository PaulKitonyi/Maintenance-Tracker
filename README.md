# Maintenance-Tracker :hammer:

The Andela Developer Challenge one

![GitHub last commit](https://img.shields.io/github/last-commit/paulkitonyi/Maintenance-Tracker/develop.svg)
![GitHub top language](https://img.shields.io/github/languages/top/paulkitonyi/Maintenance-Tracker.svg)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/paulkitonyi/Maintenance-Tracker.svg)
![GitHub contributors](https://img.shields.io/github/contributors/paulkitonyi/Maintenance-Tracker.svg)
[![Build Status](https://travis-ci.org/PaulKitonyi/Maintenance-Tracker.svg?branch=develop)](https://travis-ci.org/PaulKitonyi/Maintenance-Tracker)
[![Coverage Status](https://coveralls.io/repos/github/PaulKitonyi/Maintenance-Tracker/badge.svg?branch=develop)](https://coveralls.io/github/PaulKitonyi/Maintenance-Tracker?branch=develop)
# Table of Contents
* [Introduction](#introduction)
    * [Project Overview](#project-overview)
    * [Required Features](#required-features)
* [API Installation and setup](#api-installation-and-setup)
    * [Navigate to the Maintenance-Tracker-API folder](#navigate-to-the-maintenance-tracker-api-folder)
    * [Create a virtual Environment](#create-virtual-environment)
    * [Activate a virtual Environment](#activate-a-virtual-environment)
    * [Install Requirements](#install-requirements)
    * [Running the API](#running-the-api)
    * [Endpoints](#endpoints)
    * [Testing](#testing)
    * [Available Endpoints](#available-endpoints)
* [UI Template](#ui-template)
* [Pivotal Tracker Project](#pivotal-tracker-project)
* [Home page with login form](#home-page-with-login-form)
* [Sign up Page](#sign-up-page)
* [User make request](#user-make-request)
* [User view requests](#user-view-request)
* [User Edit account](#user-edit-account)
* [Admin login](#admin-login)
* [Admin view requests](#admin-view-requests)
* [Admin Edit account](#admin-edit-account)
* [Admin view approved](#admin-view-approved)
* [Admin view resolved](#admin-view-resolved)
* [Admin view rejected](#admin-view-rejected)
* [Installation and use](#installation-and-use)
* [Contribution](#contribution)

# Introduction

## Project Overview
- Maintenance Tracker App is an application that provides users with the ability to reach out to
operations or repairs department regarding repair or maintenance requests and monitor the
status of their requests.

## Required Features
1. Users can [create an account](#sign-up-page) and [log in](#home-page-with-login-form).
1. The users should be able to [make maintenance or repairs request](#user-make-request).
1. An admin should be able to [approve/reject a repair/maintenance request](#admin-view-requests).
1. The admin should be able to [mark request as resolved](#admin-view-approved) once it is done.
1. The admin should be able to [view all maintenance/repairs requests](#admin-view-requests) on the application.
1. The admin should be able to filter requests.
1. The user can [view all his/her requests](#user-view-request).
1. The admin should be able to [provide feedback to the users](#admin-view-approved).

# API Installation and Setup
First clone the application by typing on your terminal 'git clone' then add the following url.
```bash
https://github.com/PaulKitonyi/Maintenance-Tracker.git
```
# Navigate to the Maintenance-Tracker-API folder
```bash
cd Maintenance-Tracker/Maintenance-Tracker-API
```
# Create a virtual Environment
On UNIX Based system you can type
```bash
virtualenv venv --python=python3
```
or on windows
```bash
python -m venv venv
```

# Activate the virtual Enviroment
Before you begin you will need to activate the virtual environment we have created on the above step.
On UNIX Based systems
```bash
source venv/bin/activate
```
On windows
```bash
venv\Scripts\activate
```

# Install Requirements
On your terminal type
```bash
$ pip install -r requirements.txt
```

# Run the Application
After the settingup the app, you will run it
```bash
$ python run.py
```

# Endpoints
You can now access the available endpoints now from the following url on your local computer
```bash
http://localhost:5000/api/v1/
```
or online from heroku
```bash
https://maintenance-tracker-apiv1.herokuapp.com/api/v1/
```

# Testing
After successfully installing the application, the endpoints can be tested by running
```bash
nosetests tests
```
or with coverage
```bash
nosetests --with-coverage --cover-package tests
```

# Available Endpoints
| Endpoint | Functionality |
| --- | --- |
| `GET /users/requests` | Fetch all the requests of a logged in user |
| `GET /users/requests/<requestId>` | Fetch a request that belongs to a logged in user |
| `POST /users/requests` | Create a request |
| `PUT /users/requests/<requestId>` | Modify a request |
| `DELETE /users/requests/<requestId>` | Delete a request |

# UI Templates
You can view the UI templates on [Github Pages](https://paulkitonyi.github.io/Maintenance-Tracker/)

# Pivotal Tracker Project
You can view the pivotal tracker stories [here](https://www.pivotaltracker.com/n/projects/2173306)

## Home page with login form
Users will provide their email and Password in-order to access the Application.
![screenshot from 2018-05-28 23-59-32](https://user-images.githubusercontent.com/21083657/40629352-3d49e8d4-62d3-11e8-91ce-0ec8c8a4be90.png)

## Sign up Page
New users can create their accounts using this form.
![screenshot from 2018-05-29 00-02-51](https://user-images.githubusercontent.com/21083657/40629424-af2b625c-62d3-11e8-9faf-a8597661a356.png)

## User make request
An authorised user can make a request using this form.
![screenshot from 2018-05-29 00-09-13](https://user-images.githubusercontent.com/21083657/40629549-8f96492e-62d4-11e8-814e-e6cb3631cb3a.png)

## User view requests
An authorised user can view all the requests made in the application.
![screenshot from 2018-05-29 00-11-13](https://user-images.githubusercontent.com/21083657/40629587-e127e41e-62d4-11e8-9bc2-bf0e2110b3ca.png)

## User Edit account
An authorised user can edit his/her account.
![screenshot from 2018-05-29 00-13-19](https://user-images.githubusercontent.com/21083657/40629630-44b92970-62d5-11e8-9a9a-91dd851f4968.png)

## Admin login
An authorised admin can login using this form.
![screenshot from 2018-05-29 00-16-51](https://user-images.githubusercontent.com/21083657/40629686-c7c706c0-62d5-11e8-8829-41854cd56bce.png)

## Admin view requests
An authorised admin can view all request made in this application.
![screenshot from 2018-05-29 00-28-43](https://user-images.githubusercontent.com/21083657/40630316-641cee82-62da-11e8-9d45-6a7c945f713b.png)

## Admin Edit account
An authorised admin can edit his/her account.
![screenshot from 2018-05-29 00-29-45](https://user-images.githubusercontent.com/21083657/40629979-6d729c64-62d7-11e8-9fa1-8e6a9a06e070.png)

## Admin view approved
An admin can view all the approved requests in the application.
![screenshot from 2018-05-29 00-27-49](https://user-images.githubusercontent.com/21083657/40630262-e644a928-62d9-11e8-96a7-9dfe7cf38f31.png)

## Admin view resolved
An admin can view all the resolved requests in the application.
![screenshot from 2018-05-29 00-36-13](https://user-images.githubusercontent.com/21083657/40630100-5733312e-62d8-11e8-80a7-9a6703c1acde.png)

## Admin view rejected
An admin can view all the rejected requests in the application.
![screenshot from 2018-05-29 00-33-44](https://user-images.githubusercontent.com/21083657/40630070-1644d28a-62d8-11e8-9675-958a7b9ee80d.png)

## Installation and use
- To use this application,in your terminal type ```git clone https://github.com/PaulKitonyi/Maintenance-Tracker.git```and press Enter.
- Navigate to the Maintenance tracker application and then cd to UI and click the index.html file to view it on your browser.

## Contribution
If you want to contribute to this project:
 - Fork it!
 - Create your feature branch: git checkout -b my-new-feature
 - Commit your changes: git commit -m 'Add some feature'
 - Push to the branch: git push origin my-new-feature
 - Create a pull request.

