# A basic flask API

## Installation

To build the image run:
`docker build -t flask_api .`

## Local Execution

Run unittests:
`docker run --rm flask_api python -m unittest`

To run the container execute:
`docker run -p 80:80 --rm --name flask_api -v db:/app/db flask_api`
Note that the -v option is important here to ensure that data persists if the container has to be restarted. Note also to check that port 80 is free on your host machine.

You can now use the api on http://localhost:80 (e.g. via Postman or via Curl).

To insert a movie execute `curl localhost/movies/ -d director="x" -d title="y" -d language="z"`
To see the movie: `curl localhost/movies/`

Delete the database if you want to start from a clean slate:
`docker stop flask_api && docker volume rm -f db`

## Access API from local browser

The app can also be accessed from http://localhost:80/ inside your local browser.
To read the API documentation go to http://localhost:80/apidocs/

## Setup CI/CD pipeline in Azure

One fairly simple way to setup a CI/CD pipeline is as follows:

1) Create an Azure account

2) Create a new project.

3) Push the directory to an Azure DevOps Repo by running `git remote add origin <url_of_your_azure_repo>` and then `git push -u origin --all`

4) Create a new build pipeline as specified by `azure-pipelines.yml`. 

5) Create an Azure hosted Web App.

6) Setup a release pipeline by selecting the build pipeline from the last step as an artifact and create one stage (e.g. "to Azure")

7) Activate the continuous deployment trigger on the artifact to automate creating a new release for every new build.

8) Go to the web page of the app. 

Some comments about `azure-pipelines.yml` are in order:

- `pool: "local"` is chosen because it works nicely with the trial version and one gets get up and running quickly. It is clear, however, that this is only meant for testing or experimentation purposes and is no option for a production or even development environment. Explanation on how to setup a local pool can be found under Project Settings -> Agent pools -> New Agent.
- The build pipeline is comprised of three stages: Build, Test and Push.
- The Build stage simply builds the Docker image.
- The Test stage runs Unit tests as a Bash command (this is the best option I came up with).
- The Push Stage pushes the image to the Azure Container Registry if the tests passed (if not the Build pipeline fails).



