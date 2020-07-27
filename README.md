### Development

1. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test it [http://localhost:5000]
    
### Production

Uses gunicorn + nginx.

1. Create *.env.prod* and *.env.prod.db*. Based on .env.dev Update the environment variables.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:1337]
    
    
    send post query with form data, where {'url' = example.com } on http://localhost:5000/api/v1
    if url is avaliable you will get an id of task
    
    send the adress get query with url, params 'id' from 'post' query http://localhost:1337?id=1
    will returned url, and parse website by requests lib.
