# Script pour générer une SECRET_KEY Django sécurisée
# Usage: .\k8s\generate-secret-key.ps1

Write-Host "Génération d'une SECRET_KEY Django sécurisée..." -ForegroundColor Cyan
Write-Host ""

try {
    $secretKey = python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
    
    if ($LASTEXITCODE -eq 0 -and $secretKey) {
        Write-Host "✓ SECRET_KEY générée:" -ForegroundColor Green
        Write-Host ""
        Write-Host $secretKey -ForegroundColor Yellow
        Write-Host ""
        Write-Host "Copie cette clé et mets-la dans k8s/secret.yaml" -ForegroundColor Cyan
        Write-Host ""
        
        # Proposer de mettre à jour automatiquement
        $update = Read-Host "Veux-tu mettre à jour automatiquement k8s/secret.yaml? (O/N)"
        if ($update -eq "O" -or $update -eq "o" -or $update -eq "Y" -or $update -eq "y") {
            $secretFile = "k8s\secret.yaml"
            if (Test-Path $secretFile) {
                $content = Get-Content $secretFile -Raw
                $content = $content -replace 'DJANGO_SECRET_KEY: ".*"', "DJANGO_SECRET_KEY: `"$secretKey`""
                Set-Content -Path $secretFile -Value $content -NoNewline
                Write-Host "✓ Fichier secret.yaml mis à jour!" -ForegroundColor Green
            } else {
                Write-Host "✗ Fichier secret.yaml introuvable" -ForegroundColor Red
            }
        }
    } else {
        Write-Host "✗ Erreur lors de la génération de la clé" -ForegroundColor Red
        Write-Host "Assure-toi que Python et Django sont installés" -ForegroundColor Yellow
    }
} catch {
    Write-Host "✗ Erreur: $_" -ForegroundColor Red
    Write-Host ""
    Write-Host "Alternative: Utilise cette commande manuellement:" -ForegroundColor Yellow
    Write-Host 'python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"' -ForegroundColor White
}
