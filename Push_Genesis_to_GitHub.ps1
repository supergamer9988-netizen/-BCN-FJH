# 💎 GENESIS PUSH SCRIPT
# This script will automatically:
# 1. Initialize Git (if not done)
# 2. Add all BCN Files
# 3. Commit the God Tier Architecture
# 4. Prompt you for login and Push to: https://github.com/supergamer9988-netizen/-BCN-FJH

Write-Host "--- [ PROJECT GENESIS : ASCENDING TO GITHUB ] ---" -ForegroundColor Cyan

# 1. Config (You need this for Git to work)
git config user.email "genesis@godtier.com"
git config user.name "Genesis AI"

# 2. Status
Write-Host "Staging Files..." -ForegroundColor Yellow
git init
git add .

# 3. Commit
Write-Host "Committing Logic Gates and Hysteresis Analytics..." -ForegroundColor Yellow
git commit -m "Project GENESIS: Initial God Tier Ascension Branch"

# 4. Remote Sync
Write-Host "Linking to official Repo..." -ForegroundColor Yellow
if (!(git remote show origin)) {
    git remote add origin https://github.com/supergamer9988-netizen/-BCN-FJH.git
}

# 5. The Push
Write-Host "PUSHING TO CLOUD... (Login window may appear)" -ForegroundColor Green
git branch -M main
git push -u origin main

Write-Host "`n--- [ ASCENSION SUCCESSFUL ] ---" -ForegroundColor Green
Read-Host "Press Enter to finish..."
