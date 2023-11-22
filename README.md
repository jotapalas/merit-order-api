# merit-order-api

This is a simple Django project to  implement a custom merit order algorithm.

## Getting started

To run the project you just have to open a terminal, navigate to the root folder and type: 
```
docker-compose up -d --build
```

This will get the server up and running at port `8888`.

## Running tests

If you want to run the unit tests before testing it manually, you just have to type:

```
docker exec -it meritorder_django python manage.py test
```

## Testing it manually

You can perform a `POST` request to `localhost:8888/productionplan` using an example payload from the folder `example_payloads`.


# About the project structure

If you want to navigate through the structure, here is a little guide.

You'll notice two main modules: `users` and `core`. The module `users` is just there because I've used my personal Django template and I like to have them separated from the rest of the project. Anyway, the endpoint is unauthenticated, so this module is not really needed.

## core

The `core` module is where everything happens. We have two important folders and one `utils` file here:

### serializers folder

Simple serializers for validating that the input given by the user is correct.

### views folder

The main view lives here. It's just a simple view that handles the input and delegates validation and business logic to serializers and utils, respectively.

### utils

Here is where the merit order algorithm lives.

# TBD work

Some things that would be nice to do in the future:
- Using the database to "caching" the powerplants. I didn't do this because I assumed that every power plant given in the payload is different, but if powerplants had an unique ID we could have them in database and perform the MWh cost calculation in a separate model for them.

- Logging errors. Using a tool like Sentry or Lumigo.
