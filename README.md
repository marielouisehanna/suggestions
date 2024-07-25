# Suggestions Web-app 🕸 :

## The Steps Needed To run the app in Docker 🐋🐳:

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


## The Steps Needed To Deploy to Minikube ⏹️:

1. Download minikube
2. Download Kubectl 
3. Write the manifest.yaml files (deployment + services)
4. Run : 
```
minikube start
```
5. Apply these deployments with kubectl:
```
kubectl apply -f manifast.yaml
```
or run:
```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```
6. Test the Application:
```
minikube service suggestion-flask-app-service --url
```
7. Testing Kubernetes Features: 
    1. Scale the application up and down : <br />
    ```kubectl scale deployment web-app --replicas=4 ```
    2. Update the application by changing the Docker image version and reapplying the manifest.
    3. Use ConfigMaps and Secrets to manage application configuration.
    4. kubectl expose deployment suggestion-flask-app --type=LoadBalancer ?
<br />
Additional important commands to use:<br />
```
 kubectl get pods 
 kubectl get nodes 
 minikube stop 
 minikube delete
```

🙅🏻‍♂️ UNFINISHED PROJECT  <br />
🚩IN THE PROCESS <br />
✨ 