# Suggestions Web-app 🕸 :

## The Steps Needed To run the app in Docker 🐋:

1. Download Docker Desktop
2. Go to the app repertory
```
cd app
```
3. Build The Docker Image : 

```
docker build -t suggestion-flask-app .
```
4. Run The Container : 

```
docker run --name suggestion-flask-app -p 5000:5000 suggestion-flask-app
```
5. To Test The flask-app : http://localhost:5000/

6. Upload the image to Docker Hub:
    1. In Docker Hub : Select the Create Repository button.
    2. In the command line: ```docker build -t username/repository_name .```

    3. Sign in to Docker hub : ```docker login -u YOUR-USER-NAME```
    4. Push it  : ```docker push YOUR-USER-NAME/getting-started```


## The Steps Needed To Deploy to Minikube:

1. Download minikube
2. Download Kubectl 
3. write the deployment and services yaml files
4. Apply these deployments with kubectl:
```kubectl apply -f deployment.yaml```
5. 





🙅🏻‍♂️ UNFINISHED PROJECT  <br />
🚩IN THE PROCESS