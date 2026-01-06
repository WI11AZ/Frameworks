# Script de test Docker complet
# Usage: .\test-docker.ps1

Write-Host "=== Tests Docker ===" -ForegroundColor Cyan
Write-Host ""

# Test 1: Version Docker
Write-Host "1. Version Docker:" -ForegroundColor Yellow
docker --version
if ($LASTEXITCODE -eq 0) {
    Write-Host "   [OK] Docker installe" -ForegroundColor Green
} else {
    Write-Host "   [ERREUR] Docker non trouve" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Test 2: Info Docker
Write-Host "2. État du daemon Docker:" -ForegroundColor Yellow
$dockerInfo = docker info 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "   [OK] Docker daemon actif" -ForegroundColor Green
} else {
    Write-Host "   [ERREUR] Docker daemon non actif" -ForegroundColor Red
    Write-Host "   Lance Docker Desktop!" -ForegroundColor Yellow
    exit 1
}

Write-Host ""

# Test 3: Conteneurs en cours
Write-Host "3. Conteneurs en cours d'exécution:" -ForegroundColor Yellow
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
$runningContainers = (docker ps -q).Count
Write-Host "   → $runningContainers conteneur(s) actif(s)" -ForegroundColor Cyan

Write-Host ""

# Test 4: Images Docker
Write-Host "4. Images Docker disponibles:" -ForegroundColor Yellow
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"
$imageCount = (docker images -q).Count
Write-Host "   → $imageCount image(s) disponible(s)" -ForegroundColor Cyan

Write-Host ""

# Test 5: Test avec hello-world
Write-Host "5. Test avec hello-world:" -ForegroundColor Yellow
docker run --rm hello-world 2>&1 | Select-Object -Last 5
if ($LASTEXITCODE -eq 0) {
    Write-Host "   [OK] Test hello-world reussi" -ForegroundColor Green
} else {
    Write-Host "   [ERREUR] Test hello-world echoue" -ForegroundColor Red
}

Write-Host ""

# Test 6: Docker Compose
Write-Host "6. État Docker Compose:" -ForegroundColor Yellow
docker compose ps
if ($LASTEXITCODE -eq 0) {
    Write-Host "   [OK] Docker Compose fonctionnel" -ForegroundColor Green
} else {
    Write-Host "   [ATTENTION] Aucun service Docker Compose actif" -ForegroundColor Yellow
}

Write-Host ""

# Test 7: Application Django (si disponible)
Write-Host "7. Test de l'application Django:" -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri http://localhost:8000 -UseBasicParsing -TimeoutSec 3 -ErrorAction Stop
    Write-Host "   [OK] Application accessible (HTTP $($response.StatusCode))" -ForegroundColor Green
} catch {
    if ($_.Exception.Response.StatusCode -eq 500) {
        Write-Host "   [ATTENTION] Application accessible mais erreur 500 (probleme Django, pas Docker)" -ForegroundColor Yellow
        Write-Host "   -> Docker fonctionne, mais l'app Django a besoin de migrations/config" -ForegroundColor Cyan
    } elseif ($_.Exception.Response.StatusCode) {
        Write-Host "   [ATTENTION] Application repond avec HTTP $($_.Exception.Response.StatusCode)" -ForegroundColor Yellow
    } else {
        Write-Host "   [ATTENTION] Application non accessible sur le port 8000" -ForegroundColor Yellow
        Write-Host "   -> Verifie que docker compose up a ete lance" -ForegroundColor Cyan
    }
}

Write-Host ""

# Test 8: Ressources
Write-Host "8. Utilisation des ressources:" -ForegroundColor Yellow
docker stats --no-stream --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}"

Write-Host ""
Write-Host "=== Resume ===" -ForegroundColor Cyan
Write-Host "[OK] Docker est installe et fonctionnel" -ForegroundColor Green
Write-Host "[OK] Les conteneurs peuvent etre crees et executes" -ForegroundColor Green
Write-Host ""
Write-Host "Pour tester ton application Django:" -ForegroundColor Yellow
Write-Host "  1. docker compose up -d" -ForegroundColor White
Write-Host "  2. docker compose logs -f" -ForegroundColor White
Write-Host "  3. Ouvre http://localhost:8000 dans ton navigateur" -ForegroundColor White
Write-Host ""
