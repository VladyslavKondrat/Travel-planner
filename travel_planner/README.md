# Travel Planner RESTful API

A CRUD application built with Django REST Framework for planning travel projects and managing places to visit. This project integrates with the Art Institute of Chicago API to validate locations.

## Features Included
- **CRUD Operations:** Complete management of Projects and nested Places.
- **Third-Party API Validation:** External IDs are verified against the Art Institute of Chicago API before saving.
- **Business Logic Enforcement:** 
  - Max 10 places per project.
  - A project automatically marks as `is_completed=True` when all places are visited.
  - Projects cannot be deleted if any associated places are marked as visited.
- **Extended Features:**
  - **Dockerized:** Fully configured with `docker-compose`.
  - **Caching:** Art Institute API validations are cached to optimize performance.
  - **Basic Auth:** All endpoints are protected via Basic Authentication.
  - **OpenAPI Documentation:** Auto-generated Swagger UI.
  - **Pagination & Filtering:** Built-in DRF pagination and filtering.

## Setup & Running the Application with Docker

1. **Clone the repository and navigate to the directory.**
2. **Build and start the container:**
   ```bash
   docker-compose up --build
   http://localhost:8000/api/docs/