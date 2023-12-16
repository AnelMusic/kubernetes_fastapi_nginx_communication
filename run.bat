@echo off
echo Building Docker image...
cd src
docker build . -t anemus/simple_fast_api
echo Done building Docker image

echo Pushing Docker image to Docker Hub...
docker push anemus/simple_fast_api
echo Done pushing Docker image to hub

echo Applying Kubernetes deployment...
cd ../deployments
kubectl apply -f nginx.yaml -f fastapi.yaml 
echo Done applying Kubernetes deployment
