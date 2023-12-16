## Simple k8s setup for fastapi and nginx

Minikube-powered Kubernetes cluster setup showcasing internal and external pod communication. Demonstrates FastAPI and NGINX deployments utilizing LoadBalancer and ClusterIP services. Internal pod interaction via ClusterIP and external access through Restful API via LoadBalancer.

![nginx_fastapi](https://github.com/AnelMusic/kubernetes_fastapi_nginx_communication/assets/32487291/03a7daa1-62db-4b98-b09a-03aeba7220a8)

- **fastapi- Pod**:
  - Exposes port 8080 internally via the `fastapi-service` to enable communication within the cluster.
  - Exposes nodePort 3333 externally via the `fastapi-service` (LoadBlancer).
    
- **NGINX Pod**:
  - Communication occurs via the standard MongoDB port 80.
  - Does not allow direct external communication for security reasons, restricting access to the NGINX Pod from outside the Kubernetes cluster.

### Prerequisites
- **Minikube:** Ensure [Minikube](https://minikube.sigs.k8s.io/docs/start/) is installed. It helps create and manage local Kubernetes clusters.
- **kubectl:** Install [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/), the Kubernetes command-line tool, to interact with Kubernetes clusters.

### Directory structure
```bash
deployments/
├── fastapi-configmap.yaml                    
└── nginx.yaml                    

src/
├── Dockerfile
└── simple_restful_api.py

secrets/
└──mongodb-secret.yaml

README.md
run.bat
```

## Basic Workflows

#### 1. Fork project.
(https://github.com/AnelMusic/kubernetes_fastapi_nginx_communication/fork)

#### 2. Run convenienec script:
> Builds docker image tagged as anemus/simple_fast_api  <-- Chose tag you like </br>
> Pushes docker image tagged as anemus/simple_fast_api to dockerhub  <-- make sure your dockerhub is setup </br>
> Applies (Deploys) the fastapi and nginx deployments. </br>
> **Note**: In case you dont want to push your own image to dockerhub you can remove the first part from the bash file:</br> </br>
> echo Building Docker image... </br>
> cd src </br>
> docker build . -t anemus/simple_fast_api </br>
> cho Done building Docker image </br>
> 
> echo Pushing Docker image to Docker Hub... </br>
> docker push anemus/simple_fast_api </br>
> echo Done pushing Docker image to hub </br>

```bash
run.bat
```

#### Note: Make sure minikube is running + that on windows powershell is executed in admin mode



