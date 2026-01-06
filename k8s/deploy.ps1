# Script PowerShell pour déployer l'application sur Kubernetes
# Usage: .\k8s\deploy.ps1

param(
    [string]$DockerHubUsername = "your-dockerhub-username",
    [string]$ImageTag = "latest",
    [switch]$BuildImage = $false,
    [switch]$PushImage = $false,
    [switch]$SkipNamespace = $false
)

Write-Host "=== Déploiement Kubernetes pour DCWF ===" -ForegroundColor Cyan
Write-Host ""

# Vérifier que kubectl est installé
try {
    $kubectlVersion = kubectl version --client --short 2>&1
    Write-Host "✓ kubectl trouvé" -ForegroundColor Green
} catch {
    Write-Host "✗ ERREUR: kubectl n'est pas installé ou pas dans le PATH" -ForegroundColor Red
    Write-Host "Installe kubectl depuis: https://kubernetes.io/docs/tasks/tools/" -ForegroundColor Yellow
    exit 1
}

# Étape 1: Builder et pousser l'image Docker (si demandé)
if ($BuildImage -or $PushImage) {
    Write-Host "Étape 1: Préparation de l'image Docker..." -ForegroundColor Yellow
    
    if ($BuildImage) {
        Write-Host "  → Build de l'image..." -ForegroundColor Cyan
        docker build -t "${DockerHubUsername}/dcwf:${ImageTag}" .
        if ($LASTEXITCODE -ne 0) {
            Write-Host "✗ Erreur lors du build Docker" -ForegroundColor Red
            exit 1
        }
        Write-Host "  ✓ Image buildée avec succès" -ForegroundColor Green
    }
    
    if ($PushImage) {
        Write-Host "  → Push de l'image sur Docker Hub..." -ForegroundColor Cyan
        docker push "${DockerHubUsername}/dcwf:${ImageTag}"
        if ($LASTEXITCODE -ne 0) {
            Write-Host "✗ Erreur lors du push Docker. Es-tu connecté? (docker login)" -ForegroundColor Red
            exit 1
        }
        Write-Host "  ✓ Image poussée avec succès" -ForegroundColor Green
    }
}

# Étape 2: Mettre à jour l'image dans deployment.yaml
Write-Host ""
Write-Host "Étape 2: Configuration des manifests..." -ForegroundColor Yellow

$deploymentFile = "k8s\deployment.yaml"
if (Test-Path $deploymentFile) {
    $content = Get-Content $deploymentFile -Raw
    $content = $content -replace "your-dockerhub-username/dcwf:latest", "${DockerHubUsername}/dcwf:${ImageTag}"
    Set-Content -Path $deploymentFile -Value $content -NoNewline
    Write-Host "  ✓ Image mise à jour dans deployment.yaml" -ForegroundColor Green
} else {
    Write-Host "  ✗ Fichier deployment.yaml introuvable" -ForegroundColor Red
    exit 1
}

# Étape 3: Déployer sur Kubernetes
Write-Host ""
Write-Host "Étape 3: Déploiement sur Kubernetes..." -ForegroundColor Yellow

if (-not $SkipNamespace) {
    Write-Host "  → Création du namespace..." -ForegroundColor Cyan
    kubectl apply -f k8s\namespace.yaml
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  ⚠ Namespace peut-être déjà existant, continuons..." -ForegroundColor Yellow
    }
}

Write-Host "  → Création du ConfigMap..." -ForegroundColor Cyan
kubectl apply -f k8s\configmap.yaml
if ($LASTEXITCODE -ne 0) {
    Write-Host "  ✗ Erreur lors de la création du ConfigMap" -ForegroundColor Red
    exit 1
}

Write-Host "  → Création du Secret..." -ForegroundColor Cyan
kubectl apply -f k8s\secret.yaml
if ($LASTEXITCODE -ne 0) {
    Write-Host "  ✗ Erreur lors de la création du Secret" -ForegroundColor Red
    exit 1
}

Write-Host "  → Création du Deployment..." -ForegroundColor Cyan
kubectl apply -f k8s\deployment.yaml
if ($LASTEXITCODE -ne 0) {
    Write-Host "  ✗ Erreur lors de la création du Deployment" -ForegroundColor Red
    exit 1
}

Write-Host "  → Création du Service..." -ForegroundColor Cyan
kubectl apply -f k8s\service.yaml
if ($LASTEXITCODE -ne 0) {
    Write-Host "  ✗ Erreur lors de la création du Service" -ForegroundColor Red
    exit 1
}

Write-Host "  → Création de l'Ingress (optionnel)..." -ForegroundColor Cyan
kubectl apply -f k8s\ingress.yaml
if ($LASTEXITCODE -ne 0) {
    Write-Host "  ⚠ Ingress non créé (peut nécessiter un ingress controller)" -ForegroundColor Yellow
}

# Étape 4: Vérification
Write-Host ""
Write-Host "Étape 4: Vérification du déploiement..." -ForegroundColor Yellow

Write-Host ""
Write-Host "Pods:" -ForegroundColor Cyan
kubectl get pods -n dcwf

Write-Host ""
Write-Host "Services:" -ForegroundColor Cyan
kubectl get svc -n dcwf

Write-Host ""
Write-Host "=== Déploiement terminé! ===" -ForegroundColor Green
Write-Host ""
Write-Host "Commandes utiles:" -ForegroundColor Yellow
Write-Host "  Voir les logs: kubectl logs -f deployment/dcwf-deployment -n dcwf" -ForegroundColor White
Write-Host "  Voir le statut: kubectl get pods -n dcwf" -ForegroundColor White
Write-Host "  Redémarrer: kubectl rollout restart deployment/dcwf-deployment -n dcwf" -ForegroundColor White
Write-Host "  Supprimer: kubectl delete -k k8s/" -ForegroundColor White
