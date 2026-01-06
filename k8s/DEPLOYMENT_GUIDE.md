# Guide de Déploiement Kubernetes

Ce guide explique comment déployer l'application Django DCWF sur un cluster Kubernetes.

## Prérequis

1. **Un cluster Kubernetes** fonctionnel (minikube, GKE, EKS, AKS, ou un cluster local)
2. **kubectl** installé et configuré pour se connecter à ton cluster
3. **Une image Docker** de l'application poussée sur Docker Hub (ou un autre registry)

## Étape 1 : Préparer l'image Docker

### 1.1 Builder l'image localement

```bash
docker build -t ton-username/dcwf:latest .
```

### 1.2 Tagger l'image pour Docker Hub

```bash
docker tag ton-username/dcwf:latest ton-username/dcwf:v1.0.0
```

### 1.3 Pousser l'image sur Docker Hub

```bash
docker login
docker push ton-username/dcwf:latest
docker push ton-username/dcwf:v1.0.0
```

## Étape 2 : Configurer les secrets

### 2.1 Générer une SECRET_KEY Django sécurisée

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 2.2 Mettre à jour le Secret Kubernetes

Édite `k8s/secret.yaml` et remplace `DJANGO_SECRET_KEY` par la clé générée :

```yaml
stringData:
  DJANGO_SECRET_KEY: "ta-cle-secrete-generee"
```

## Étape 3 : Configurer l'image Docker

Édite `k8s/deployment.yaml` et remplace :

```yaml
image: your-dockerhub-username/dcwf:latest
```

par :

```yaml
image: ton-username/dcwf:latest
```

## Étape 4 : Configurer le domaine (optionnel)

Si tu utilises un Ingress, édite `k8s/ingress.yaml` et remplace :

```yaml
host: dcwf.example.com
```

par ton vrai domaine.

## Étape 5 : Déployer sur Kubernetes

### Option A : Déploiement manuel (recommandé pour débuter)

```bash
# Créer le namespace
kubectl apply -f k8s/namespace.yaml

# Créer le ConfigMap
kubectl apply -f k8s/configmap.yaml

# Créer le Secret
kubectl apply -f k8s/secret.yaml

# Créer le Deployment
kubectl apply -f k8s/deployment.yaml

# Créer le Service
kubectl apply -f k8s/service.yaml

# Créer l'Ingress (optionnel)
kubectl apply -f k8s/ingress.yaml
```

### Option B : Déploiement avec Kustomize

```bash
kubectl apply -k k8s/
```

## Étape 6 : Vérifier le déploiement

### Vérifier les pods

```bash
kubectl get pods -n dcwf
```

Tu devrais voir quelque chose comme :

```
NAME                                READY   STATUS    RESTARTS   AGE
dcwf-deployment-xxxxxxxxxx-xxxxx    1/1     Running   0          30s
dcwf-deployment-xxxxxxxxxx-yyyyy    1/1     Running   0          30s
```

### Vérifier les services

```bash
kubectl get svc -n dcwf
```

### Vérifier les logs

```bash
kubectl logs -f deployment/dcwf-deployment -n dcwf
```

## Étape 7 : Accéder à l'application

### Avec LoadBalancer (cloud providers)

```bash
kubectl get svc dcwf-service -n dcwf
```

Récupère l'EXTERNAL-IP et accède à `http://EXTERNAL-IP`

### Avec minikube

```bash
minikube service dcwf-service -n dcwf
```

### Avec Ingress

Si tu as configuré un Ingress, accède à ton domaine configuré.

## Commandes utiles

### Mettre à jour l'application

```bash
# Après avoir poussé une nouvelle image
kubectl rollout restart deployment/dcwf-deployment -n dcwf
```

### Scale l'application

```bash
kubectl scale deployment dcwf-deployment --replicas=3 -n dcwf
```

### Supprimer le déploiement

```bash
kubectl delete -k k8s/
# ou
kubectl delete -f k8s/ -n dcwf
```

### Voir les événements

```bash
kubectl get events -n dcwf --sort-by='.lastTimestamp'
```

## Dépannage

### Pod en état CrashLoopBackOff

```bash
# Voir les logs
kubectl logs deployment/dcwf-deployment -n dcwf

# Voir les détails du pod
kubectl describe pod <nom-du-pod> -n dcwf
```

### ImagePullBackOff

Vérifie que :
- L'image existe sur Docker Hub
- Le nom de l'image dans `deployment.yaml` est correct
- Tu es connecté au registry si c'est privé

### Service non accessible

```bash
# Vérifier les endpoints
kubectl get endpoints dcwf-service -n dcwf

# Tester depuis un pod
kubectl run -it --rm debug --image=busybox --restart=Never -n dcwf -- wget -O- http://dcwf-service:80
```

## Configuration avancée

### Ajouter un volume pour la base de données

Si tu veux utiliser PostgreSQL au lieu de SQLite, ajoute un StatefulSet et un volume persistant.

### Activer HTTPS

1. Installe cert-manager
2. Configure un ClusterIssuer Let's Encrypt
3. Décommente la section `tls` dans `ingress.yaml`

### Monitoring

Ajoute Prometheus et Grafana pour surveiller l'application.

## Support

En cas de problème, vérifie les logs et les événements Kubernetes pour plus d'informations.
