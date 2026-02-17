@echo off
echo ========================================================
echo          FINAL STEP: UPLOAD TO GITHUB
echo ========================================================
echo.
echo I have prepared your code. Now we need to send it to GitHub.
echo.
echo 1. I am opening the GitHub "Create Repository" page for you...
start https://github.com/new
echo.
echo 2. On that page:
echo    - Name the repository: FreelancersConnect
echo    - Do NOT check "Add a README"
echo    - Click "Create repository"
echo.
echo 3. Copy the URL that looks like: https://github.com/YOUR_NAME/FreelancersConnect.git
echo.
set /p REPO_URL="PASTE THE URL HERE AND PRESS ENTER: "

echo.
echo ========================================================
echo          Pushing code to %REPO_URL%...
echo ========================================================
git remote add origin %REPO_URL%
git branch -M main
git push -u origin main

echo.
echo ========================================================
echo          DEPLOYMENT COMPLETE!
echo ========================================================
pause
