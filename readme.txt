Assessment 4 - Craigslist Junior
Skills Assessed

    Rubric
    Create/design a schema using Django ORM
    Use Django Associations & Validations on the models
    Being able to fully implement CRUD for Categories and Posts

Description

Everyone loves going on Craigslist to find interesting people and interesting items. The joy of Craigslist is that it doesn't upgrade itself to stay up to date with the times - its the same old Craigslist that everyone knows and loves. This works out well for us as our client has asked for no styling. The core schema has also remained relatively unchanged over the years. Today, you will build a basic Craigslist app. We will call this Craigslist Junior because it'll just contain a small bit of the functionality.

For this assessment, you have two routes you can take: fullstack Django or Django as an API with React on the frontend. Here are the requirements for both:
Fullstack Django (using Templates for the front-end)

If you are going to solve this in fullstack Django (i.e., no React), we expect nested routes. Here's a list of routes/actions that we'd like to see:

    /categories: A list of all the categories
    /categories/new: The form for a new category
    /categories/:id: See a specific category and a list of all of its associated posts
    /categories/:id/edit: Edit page for a specific category
    Also, the ability to update/destroy categories
    /categories/:category_id/posts/new: The form for a new post under a specific category
    /categories/:category_id/posts/:post_id: See a specific post for a specific category, have the ability go back to all of the post's category's other posts (/categories/:category_id/posts)
    /categories/:category_id/posts/:post_id/edit: Edit page for a specific post under a specific category
    Also, the ability to update/destroy posts

Django API (backend) / React Frontend

This is largely the same as above, with a few route changes:

    /categories: A list of all the categories
    /categories/new: The form for a new category
    /categories/:id: See a specific category and a list of its associated posts
    /categories/:id/edit: Edit page for a specific category
    Also, the ability to update/destroy categories
    /posts: A list of posts for a specific category
    /posts/new: The form for a new post under a specific category
    /posts/:post_id: See a specific post for a specific category. Also have the ability to go back to the post's category (/category/:id). This is a real challenge!
    /posts/:post_id/edit: Edit page for a specific post under a specific category
    Also, the ability to update/destroy posts

The key difference is here is that you don't have to create nested routes in the Django API because we haven't had practice with it or learned it in class. If you'd like to, this is your friend. Otherwise, just ensure you're able to keep track of the post's category to take care of the /posts/:post_id route.




<!-- <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title> Categories and Posts </title>
  <meta name="description" content="">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>Document</title>
</head>
<body>
          {% block content %}
          {% endblock %}
</body>
</html> -->