# Configuration Kubernetes

Ce dossier contient tous les fichiers nécessaires pour déployer l'application DCWF sur Kubernetes.

## Structure des fichiers

- **namespace.yaml** : Crée un namespace dédié `dcwf` pour isoler l'application
- **configmap.yaml** : Variables d'environnement non sensibles (DEBUG, ALLOWED_HOSTS, etc.)
- **secret.yaml** : Secrets sensibles (SECRET_KEY Django)
- **deployment.yaml** : Définit les pods de l'application (répliques, ressources, probes)
- **service.yaml** : Expose l'application via un LoadBalancer
- **ingress.yaml** : Routage HTTP/HTTPS avec domaine personnalisé (optionnel)
- **kustomization.yaml** : Configuration Kustomize pour gérer tous les ressources ensemble
- **deploy.ps1** : Script PowerShell pour automatiser le déploiement

## Déploiement rapide

### Méthode 1 : Script PowerShell (recommandé)

```powershell
# Builder l'image, la pousser et déployer
.\k8s\deploy.ps1 -DockerHubUsername "ton-username" -BuildImage -PushImage

# Juste déployer (si l'image existe déjà)
.\k8s\deploy.ps1 -DockerHubUsername "ton-username"
```

### Méthode 2 : Commandes manuelles

```bash
# 1. Builder et pousser l'image Docker
docker build -t ton-username/dcwf:latest .
docker push ton-username/dcwf:latest

# 2. Mettre à jour l'image dans deployment.yaml
# (remplacer "your-dockerhub-username" par ton vrai username)

# 3. Déployer
kubectl apply -k k8s/
```

### Méthode 3 : Fichier par fichier

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml  # Optionnel
```

## Configuration requise avant déploiement

1. **Mettre à jour l'image Docker** dans `deployment.yaml` :
   ```yaml
   image: ton-username/dcwf:latest
   ```

2. **Générer et mettre à jour la SECRET_KEY** dans `secret.yaml` :
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

3. **Configurer le domaine** dans `ingress.yaml` (si tu utilises un Ingress) :
   ```yaml
   host: ton-domaine.com
   ```

## Vérification

```bash
# Voir les pods
kubectl get pods -n dcwf

# Voir les services
kubectl get svc -n dcwf

# Voir les logs
kubectl logs -f deployment/dcwf-deployment -n dcwf
```

## Commandes utiles

```bash
# Redémarrer l'application
kubectl rollout restart deployment/dcwf-deployment -n dcwf

# Scale l'application
kubectl scale deployment dcwf-deployment --replicas=3 -n dcwf

# Mettre à jour l'image
kubectl set image deployment/dcwf-deployment dcwf=ton-username/dcwf:v1.1.0 -n dcwf

# Supprimer tout
kubectl delete -k k8s/
```

## Documentation complète

Voir [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) pour un guide détaillé avec dépannage.
