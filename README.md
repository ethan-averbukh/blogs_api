# Django Auth Lab

Let's build a blog API with django!

## Version 1

### Models

- User model

### Routes

- POST /sign-up - sign a user up
- POST /sign-in - sign a user in
- PATCH /changepassword (require token)
- DELETE /sign-out (require token)

## Version 2

### Models

- User model

- Blog model
  - title : string
  - content : string
  - author : user reference
  - updated_at/created_at


### Routes

- POST /sign-up - sign a user up
- POST /sign-in - sign a user in
- PATCH /changepassword (require token)
- DELETE /sign-out (require token)

- GET /blogs (require token)
- POST /blogs (require token)
- GET /blogs/:id (require token)
- DELETE /blogs/:id (require token)
- PATCH /blogs/:id (require token)

## Version 3

### Models

- User model

- Blog model
  - title : string
  - content : string
  - author : user reference
  - updated_at/created_at

- Comment Model
  - content : string
  - blog : blog reference
  - author : user reference
  - updated_at/created_at

### Routes

- POST /sign-up - sign a user up
- POST /sign-in - sign a user in
- PATCH /changepassword (require token)
- DELETE /sign-out (require token)

- GET /blogs (require token)
- POST /blogs (require token)
- GET /blogs/:id (require token)
- DELETE /blogs/:id (require token)
- PATCH /blogs/:id (require token)

- GET /comments (require token)
- POST /comments (require token)
- GET /comments/:id (require token)
- DELETE /comments/:id (require token)
- PATCH /comments/:id (require token)