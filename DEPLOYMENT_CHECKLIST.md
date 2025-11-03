# ✅ Deployment Checklist

Copy this and check off each step as you complete it!

## Pre-Deployment

- [ ] I have a GitHub account
- [ ] I have a Render account (sign up at render.com)
- [ ] I have my Oracle APEX URLs ready
- [ ] I have my Gemini API key (optional)

## Step 1: GitHub Repository

- [ ] Created new repo: `ecoview-backend` at github.com/new
- [ ] Chose "Public" visibility
- [ ] Added README file
- [ ] Added Python .gitignore
- [ ] Clicked "Create repository"
- [ ] Copied repository URL

## Step 2: Push Code to GitHub

Open PowerShell and run these commands:

```powershell
cd c:\Users\griff\Downloads\ecoview-backend-deploy
```

- [ ] `git init`
- [ ] `git add .`
- [ ] `git commit -m "Initial commit - EcoView Backend API"`
- [ ] `git remote add origin https://github.com/YOUR_USERNAME/ecoview-backend.git`
      (Replace YOUR_USERNAME with your GitHub username)
- [ ] `git branch -M main`
- [ ] `git push -u origin main`

**If it asks for credentials:**
- [ ] Created Personal Access Token at: https://github.com/settings/tokens
- [ ] Used token as password

## Step 3: Deploy to Render

- [ ] Went to: https://dashboard.render.com
- [ ] Clicked "New +" → "Web Service"
- [ ] Connected GitHub account
- [ ] Selected `ecoview-backend` repository
- [ ] Clicked "Connect"

**Configuration:**
- [ ] Name: `ecoview-backend`
- [ ] Region: Oregon (or closest to me)
- [ ] Branch: `main`
- [ ] Root Directory: (left blank)
- [ ] Runtime: Python 3
- [ ] Build Command: `pip install -r requirements.txt`
- [ ] Start Command: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 120`
- [ ] Instance Type: Free

**Environment Variables Added:**
- [ ] `ORACLE_APEX_URL` = (my APEX URL)
- [ ] `ORACLE_APEX_SOIL_URL` = (my soil APEX URL)
- [ ] `ORACLE_APEX_POLL_INTERVAL` = `3`
- [ ] `GEMINI_API_KEY` = (my Gemini key)
- [ ] `FLASK_ENV` = `production`
- [ ] `PYTHON_VERSION` = `3.11.0`

- [ ] Clicked "Create Web Service"
- [ ] Waited for deployment (2-5 minutes)
- [ ] Deployment succeeded!

## Step 4: Test Backend

My Backend URL: `https://_________________________.onrender.com`

Tested these URLs in browser:
- [ ] `/api/health` - Returns `{"status": "healthy"}`
- [ ] `/api/sensor-data` - Returns sensor data JSON
- [ ] `/api/thresholds` - Returns thresholds JSON
- [ ] `/api/alerts` - Returns alerts JSON

## Step 5: Update Flutter App

- [ ] Opened `flutter_frontend/lib/services/api_service.dart`
- [ ] Changed `baseUrl` to my Render URL
- [ ] Ran `flutter run -d chrome` to test
- [ ] Flutter app connects successfully!

## Step 6: Monitor

- [ ] Checked Render logs - seeing APEX polling messages
- [ ] Health check is passing
- [ ] No errors in logs

---

## 🎉 Deployment Complete!

**My Backend URL:** `https://_________________________.onrender.com`

**GitHub Repo:** `https://github.com/__________/ecoview-backend`

**Next Steps:**
- [ ] Share backend URL with team
- [ ] Deploy Flutter frontend
- [ ] Set up custom domain (optional)
- [ ] Consider upgrading to paid plan for 24/7 uptime

---

## 📝 Notes

Write any issues or notes here:

_____________________________________________

_____________________________________________

_____________________________________________
