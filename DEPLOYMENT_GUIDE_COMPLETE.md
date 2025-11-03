# 🚀 Complete Deployment Guide - Step by Step

## Overview
This guide will walk you through creating a new GitHub repository and deploying your EcoView backend to Render.

---

## 📍 **STEP 1: Create New GitHub Repository**

### 1.1 Create Repository on GitHub

1. Open your browser and go to: **https://github.com/new**

2. Fill in the form:
   ```
   Repository name: ecoview-backend
   Description: EcoView Greenhouse Monitoring - Flask Backend API
   Visibility: ✓ Public (or Private if you prefer)
   ✓ Add a README file
   Add .gitignore: Choose "Python"
   Choose a license: MIT License (optional)
   ```

3. Click **"Create repository"**

4. Copy your repository URL. It will look like:
   ```
   https://github.com/YOUR_USERNAME/ecoview-backend.git
   ```

---

## 📍 **STEP 2: Push Your Backend Code to GitHub**

### 2.1 Open PowerShell and Navigate to Deployment Folder

```powershell
cd c:\Users\griff\Downloads\ecoview-backend-deploy
```

### 2.2 Initialize Git Repository

```powershell
git init
```

### 2.3 Add All Files

```powershell
git add .
```

### 2.4 Create First Commit

```powershell
git commit -m "Initial commit - EcoView Backend API"
```

### 2.5 Link to Your GitHub Repository

**⚠️ Replace `YOUR_USERNAME` with your actual GitHub username:**

```powershell
git remote add origin https://github.com/YOUR_USERNAME/ecoview-backend.git
```

### 2.6 Push to GitHub

```powershell
git branch -M main
git push -u origin main
```

**If GitHub asks for credentials:**
- Use your GitHub username
- For password, use a **Personal Access Token** (not your GitHub password)
- Create token at: https://github.com/settings/tokens

---

## 📍 **STEP 3: Deploy to Render**

### 3.1 Sign Up / Log In to Render

1. Go to: **https://render.com**
2. Click **"Get Started"** or **"Sign In"**
3. Sign up with GitHub (easiest option)

### 3.2 Create New Web Service

1. In Render Dashboard, click **"New +"** button (top right)
2. Select **"Web Service"**

### 3.3 Connect Your Repository

1. Click **"Connect a repository"**
2. If first time: Click **"Configure account"** to give Render access to your GitHub
3. Find and select **`ecoview-backend`** from the list
4. Click **"Connect"**

### 3.4 Configure the Service

Fill in these settings:

```
Name: ecoview-backend
(or any name you prefer - this will be part of your URL)

Region: Oregon (US West)
(or choose closest to you: Frankfurt, Singapore, etc.)

Branch: main

Root Directory: (leave blank)

Runtime: Python 3

Build Command:
pip install -r requirements.txt

Start Command:
gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 120

Instance Type: Free
(or paid if you need 24/7 uptime)
```

### 3.5 Add Environment Variables

Scroll down to **"Environment Variables"** section and add these:

Click **"Add Environment Variable"** for each:

| Key | Value |
|-----|-------|
| `ORACLE_APEX_URL` | `https://oracleapex.com/ords/g3_data/iot/greenhouse/` |
| `ORACLE_APEX_SOIL_URL` | `https://oracleapex.com/ords/g3_data/groups/data/10` |
| `ORACLE_APEX_POLL_INTERVAL` | `3` |
| `GEMINI_API_KEY` | `your_actual_gemini_api_key` |
| `FLASK_ENV` | `production` |
| `PYTHON_VERSION` | `3.11.0` |

**⚠️ Important:** Replace the ORACLE_APEX URLs with your actual APEX endpoints if different.

### 3.6 Create Web Service

1. Review all settings
2. Click **"Create Web Service"** button at the bottom
3. Render will now:
   - ✅ Clone your repository
   - ✅ Install dependencies
   - ✅ Start your Flask app
   - ✅ Assign a public URL

### 3.7 Wait for Deployment

You'll see logs streaming:
```
==> Cloning from https://github.com/YOUR_USERNAME/ecoview-backend...
==> Running build command: pip install -r requirements.txt
==> Starting service with command: gunicorn app:app...
==> Your service is live 🎉
```

This usually takes **2-5 minutes**.

---

## 📍 **STEP 4: Get Your Backend URL**

### 4.1 Find Your URL

Once deployed, Render will show:
```
Your service is live at:
https://ecoview-backend-XXXX.onrender.com
```

Copy this URL! You'll need it for your Flutter app.

### 4.2 Test Your Backend

Open these URLs in your browser (replace with your actual URL):

```
https://ecoview-backend-XXXX.onrender.com/api/health
https://ecoview-backend-XXXX.onrender.com/api/sensor-data
https://ecoview-backend-XXXX.onrender.com/api/thresholds
```

You should see JSON responses!

---

## 📍 **STEP 5: Update Your Flutter App**

### 5.1 Open Flutter Project

```powershell
cd c:\Users\griff\Downloads\sturdy-giggle\sturdy-giggle-1\flutter_frontend
code .
```

### 5.2 Update API URL

Open: `lib/services/api_service.dart`

Find the line with `baseUrl` and replace it:

```dart
class ApiService {
  // OLD:
  // static const String baseUrl = 'http://127.0.0.1:5000/api';
  
  // NEW: Replace with your Render URL
  static const String baseUrl = 'https://ecoview-backend-XXXX.onrender.com/api';
  
  // ... rest of code
}
```

### 5.3 Test Flutter App

```powershell
flutter run -d chrome
```

Your Flutter app should now connect to the Render backend!

---

## 📍 **STEP 6: Monitor Your Deployment**

### 6.1 View Logs

In Render Dashboard:
1. Click on your service (**ecoview-backend**)
2. Click **"Logs"** tab
3. You should see:
   ```
   🔄 Starting continuous APEX poller...
   ✅ APEX poll successful! Got X readings.
   Flask API is running
   ```

### 6.2 Check Health

The backend should show:
```
Status: Live ✓
Health Check: Passing ✓
Last Deploy: 2 minutes ago
```

---

## 🎯 **Summary - Your Deployment**

✅ **GitHub Repository:** `https://github.com/YOUR_USERNAME/ecoview-backend`

✅ **Render Service:** `https://ecoview-backend-XXXX.onrender.com`

✅ **API Endpoints:**
- Health: `https://ecoview-backend-XXXX.onrender.com/api/health`
- Sensor Data: `https://ecoview-backend-XXXX.onrender.com/api/sensor-data`
- Alerts: `https://ecoview-backend-XXXX.onrender.com/api/alerts`
- Thresholds: `https://ecoview-backend-XXXX.onrender.com/api/thresholds`

---

## 🔧 **Troubleshooting**

### Problem: "Build failed"
**Solution:** 
- Check Render logs for error messages
- Verify `requirements.txt` is present
- Make sure all files were pushed to GitHub

### Problem: "Application failed to respond"
**Solution:**
- Check environment variables are set correctly
- Verify `ORACLE_APEX_URL` is accessible
- Look at Render logs for Python errors

### Problem: "503 Service Unavailable"
**Solution:**
- Free tier apps sleep after 15 minutes
- First request wakes it up (~30 seconds)
- This is normal behavior on free tier

### Problem: Can't push to GitHub
**Solution:**
- Make sure you created the repository first
- Check the remote URL: `git remote -v`
- Use Personal Access Token, not password

---

## 📱 **Next Steps**

1. ✅ Test all API endpoints
2. ✅ Update Flutter app with production URL
3. ✅ Deploy Flutter app (Firebase Hosting, Netlify, etc.)
4. ✅ Monitor backend logs for any issues
5. ✅ Consider upgrading to paid plan for 24/7 uptime ($7/month)

---

## 🎉 **You're Done!**

Your EcoView backend is now:
- ✅ Hosted on Render
- ✅ Accessible worldwide
- ✅ Automatically restarting if it crashes
- ✅ Free to use (with limitations)
- ✅ Easy to update (just push to GitHub)

**Need help?** Check the logs in Render Dashboard or review the README.md file.

---

**Happy Deploying! 🚀**
