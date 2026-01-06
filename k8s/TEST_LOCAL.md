# Tester Kubernetes en Local

Ce guide explique comment tester le déploiement Kubernetes localement avec **minikube** ou **kind**.

## Option 1 : Minikube (recommandé pour débuter)

### Installation

**Windows** :
```powershell
# Avec Chocolatey
choco install minikube

# Ou télécharge depuis: https://minikube.sigs.k8s.io/docs/start/
```

### Démarrage

```powershell
# Démarrer minikube
minikube start

# Vérifier que ça fonctionne
kubectl get nodes
```

### Déployer l'application

```powershell
# 1. Builder l'image dans l'environnement minikube
minikube image build -t dcwf:latest .

# 2. Mettre à jour deployment.yaml pour utiliser l'image locale
# Remplace: image: your-dockerhub-username/dcwf:latest
# Par: image: dcwf:latest

# 3. Déployer
kubectl apply -k k8s/

# 4. Exposer le service
minikube service dcwf-service -n dcwf
```

## Option 2 : Kind (Kubernetes in Docker)

### Installation

```powershell
# Avec Chocolatey
choco install kind

# Ou télécharge depuis: https://kind.sigs.k8s.io/docs/user/quick-start/
```

### Démarrage

```powershell
# Créer un cluster
kind create cluster --name dcwf

# Vérifier
kubectl cluster-info --context kind-dcwf
```

### Déployer l'application

```powershell
# 1. Builder l'image
docker build -t dcwf:latest .

# 2. Charger l'image dans kind
kind load docker-image dcwf:latest --name dcwf

# 3. Mettre à jour deployment.yaml pour utiliser l'image locale
# Remplace: image: your-dockerhub-username/dcwf:latest
# Par: image: dcwf:latest

# 4. Déployer
kubectl apply -k k8s/

# 5. Port-forward pour accéder à l'application
kubectl port-forward svc/dcwf-service 8000:80 -n dcwf
```

Puis ouvre `http://localhost:8000`

## Option 3 : Docker Desktop Kubernetes

Si tu as Docker Desktop, tu peux activer Kubernetes directement dedans.

### Activation

1. Ouvre Docker Desktop
2. Va dans Settings → Kubernetes
3. Coche "Enable Kubernetes"
4. Clique sur "Apply & Restart"

### Déployer

```powershell
# 1. Builder l'image
docker build -t dcwf:latest .

# 2. Mettre à jour deployment.yaml pour utiliser l'image locale
# Remplace: image: your-dockerhub-username/dcwf:latest
# Par: image: dcwf:latest

# 3. Déployer
kubectl apply -k k8s/

# 4. Port-forward
kubectl port-forward svc/dcwf-service 8000:80 -n dcwf
```

## Vérification

```powershell
# Voir les pods
kubectl get pods -n dcwf

# Voir les services
kubectl get svc -n dcwf

# Voir les logs
kubectl logs -f deployment/dcwf-deployment -n dcwf

# Décrire un pod pour voir les détails
kubectl describe pod <nom-du-pod> -n dcwf
```

## Nettoyage

### Minikube

```powershell
minikube stop
minikube delete
```

### Kind

```powershell
kind delete cluster --name dcwf
```

### Docker Desktop

Désactive Kubernetes dans les paramètres de Docker Desktop.

## Dépannage

### Pod en état ImagePullBackOff

Assure-toi d'avoir chargé l'image dans le cluster :
- **Minikube** : `minikube image build -t dcwf:latest .`
- **Kind** : `kind load docker-image dcwf:latest --name dcwf`
- **Docker Desktop** : L'image doit être dans Docker Desktop

### Port-forward ne fonctionne pas

Vérifie que le service est bien créé :
```powershell
kubectl get svc -n dcwf
```

### Les pods ne démarrent pas

Vérifie les logs :
```powershell
kubectl logs <nom-du-pod> -n dcwf
```

Et les événements :
```powershell
kubectl get events -n dcwf --sort-by='.lastTimestamp'
```
