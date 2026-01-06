# Script PowerShell pour builder et lancer l'application Docker
# Utilise ce script si docker n'est pas dans le PATH

Write-Host "Recherche de Docker..." -ForegroundColor Yellow

# Tentative de trouver Docker dans les emplacements courants
$dockerPaths = @(
    "$env:ProgramFiles\Docker\Docker\resources\bin\docker.exe",
    "$env:ProgramFiles\Docker\Docker\resources\bin\docker-compose.exe",
    "${env:ProgramFiles(x86)}\Docker\Docker\resources\bin\docker.exe"
)

$dockerExe = $null
foreach ($path in $dockerPaths) {
    if (Test-Path $path) {
        $dockerExe = $path
        Write-Host "Docker trouvé: $dockerExe" -ForegroundColor Green
        break
    }
}

if (-not $dockerExe) {
    Write-Host "ERREUR: Docker n'a pas été trouvé. Assure-toi que Docker Desktop est installé." -ForegroundColor Red
    Write-Host "Ferme et rouvre PowerShell, ou utilise Docker Desktop directement." -ForegroundColor Yellow
    exit 1
}

# Ajouter au PATH pour cette session
$dockerDir = Split-Path $dockerExe -Parent
$env:Path = "$dockerDir;$env:Path"

Write-Host "`nConstruction de l'image Docker..." -ForegroundColor Cyan
& docker compose build

if ($LASTEXITCODE -eq 0) {
    Write-Host "`nDémarrage de l'application..." -ForegroundColor Cyan
    Write-Host "L'application sera accessible sur http://localhost:8000" -ForegroundColor Green
    Write-Host "Appuie sur Ctrl+C pour arrêter`n" -ForegroundColor Yellow
    & docker compose up
} else {
    Write-Host "`nERREUR lors du build. Vérifie les messages ci-dessus." -ForegroundColor Red
}


