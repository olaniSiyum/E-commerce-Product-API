# E-commerce-Product-API

## Overview
The E-commerce Product API is a RESTful API built using Django and Django REST Framework that facilitates the management of an online store's product offerings, user accounts, shopping carts, and order processing. This project allows users to interact with an e-commerce platform, enabling them to view products, manage their shopping carts, and place orders.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [ER Diagram](#ERDiagram)
- [API Endpoints](#api-endpoints)
- [References](#References)

## Features
- User authentication with registration and login functionality.
- CRUD operations for products, shopping carts, and orders.
- Support for multiple user roles and permissions.
- Secure API endpoints with JWT authentication.
- Detailed error handling and validation for all requests.

## Technologies
- **Backend:** Django, Django REST Framework
- **Database:** MySQL
- **Tools:** Postman for API testing, Git for version control

## Installation
To set up the project locally, follow these steps:

1. **Clone the repository:**
```bash
   git clone https://github.com/olaniSiyum/E-commerce-Product-API.git
   cd E-commerce-Product-API
```
2. **Create and activate a virtual environment:**
```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use .venv\Scripts\activate
```
3. **Install dependencies**
```bash
   pip install -r requirements.txt
```
4. **Set up the database:**
- Configure your database settings in `settings.py`.
- Run migrations:
```bash
python manage.py migrate
```
5. **Run the development server:**
```bash
python manage.py runserver
```
## Usage
Once the server is running, you can access the API at `http://127.0.0.1:8000/api/`.
## ER Diagram
## API Endpoints
