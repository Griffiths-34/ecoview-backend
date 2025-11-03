# EcoView Backend API# Python Backend



Flask backend API for the EcoView Greenhouse Monitoring System. This service polls Oracle APEX for sensor data, provides threshold management, generates alerts, and offers AI-powered recommendations using Google Gemini.This folder contains the Flask backend for EcoView. There are two runnable entry points:



## 🚀 Features- app.py — production backend that the Flutter app connects to by default

- Saterday testing.py — an isolated testing backend for validating APEX data and PDF export without impacting production

- **Real-time Sensor Data**: Polls Oracle APEX every 3 seconds for latest greenhouse readings

- **Threshold Management**: Configurable thresholds for temperature, humidity, soil moisture, light, and gas sensors## app.py (production)

- **Smart Alerts**: Automatic alert generation based on sensor thresholds

- **Color-Coded Status**: Material Design colors for consistent UI representation- Purpose: connect to Oracle APEX, normalize sensor data, provide REST APIs, and export a PDF report

- **AI Analysis**: Optional Google Gemini integration for intelligent recommendations- Default port: 5000

- **CORS Support**: Full CORS configuration for web and mobile clients- APEX URL: set in `.env` via `ORACLE_APEX_URL`



## 📊 API EndpointsRun:



### Core Endpoints```powershell

- `GET /api/health` - Health checkcd python_backend

- `GET /api/sensor-data` - Latest sensor readings with color-coded statusespython app.py

- `GET /api/alerts` - Active alerts and warnings```

- `GET /api/thresholds` - Get configured thresholds

- `POST /api/thresholds` - Update thresholdsCore endpoints:

- GET /api/health

### Analysis Endpoints- GET /api/sensor-data

- `GET /api/sensor-analysis/<sensor_type>` - Detailed sensor analysis- GET /api/sensor-analysis/<sensor_type>

- `GET /api/sensor-analysis/<sensor_type>/ai` - AI-powered recommendations- GET /api/ai-recommendations

- GET /api/alerts

### Supported Sensor Types- GET /api/export-report

`temperature`, `humidity`, `soil_moisture`, `light`, `co2`, `air_quality`, `smoke`, `co`, `flame`, `pressure`

See `THRESHOLDS.md` for status bands.

## 🛠️ Tech Stack

## Saterday testing.py (isolated testing backend)

- **Framework**: Flask 3.0.0

- **Server**: Gunicorn- Purpose: a safe copy for testing against a Saturday/Oracle APEX testing URL without touching `app.py`

- **Data Source**: Oracle APEX REST APIs- Isolation: runs as a separate Python process; does not modify or get imported by `app.py`

- **AI**: Google Gemini API (optional)- Default port: 5000 (same as `app.py`) — do not run both at once on the same port

- **Storage**: JSON file-based threshold storage- Default APEX URL: `https://oracleapex.com/ords/at2/greenhouse/sensor` (override with `ORACLE_APEX_URL`)

- PDF export: mirrors production fixes (portrait layout, column widths, "CO2" text fix, consistent spacing)

## 📦 Installation

Run:

### Prerequisites

- Python 3.11+```powershell

- Oracle APEX URLs for sensor datacd python_backend

- Google Gemini API key (optional)python "Saterday testing.py"

```

### Local Development

To run both production and testing together, adjust one port:

1. **Clone the repository**

```bash```python

git clone https://github.com/YOUR_USERNAME/ecoview-backend.git# at the bottom of "Saterday testing.py"

cd ecoview-backendapp.run(host='0.0.0.0', port=5001, debug=True)

``````



2. **Create virtual environment**## Environment and dependencies

```bash

python -m venv venv- Create a virtual environment once and reuse for both entry points:

source venv/bin/activate  # On Windows: venv\Scripts\activate

``````powershell

cd python_backend

3. **Install dependencies**python -m venv .venv

```bash.venv\Scripts\Activate.ps1

pip install -r requirements.txtpip install -r requirements.txt

``````



4. **Configure environment variables**- Optional AI: set `GEMINI_API_KEY` in `.env` for AI analyses and recommendations

```bash

cp .env.example .env## Notes

# Edit .env with your actual values

```- The testing backend logs APEX pull timestamps and temperatures for quick verification

- Connection pooling is used to make APEX requests faster and more reliable

5. **Run the development server**- The testing backend does not affect `app.py`; stopping one does not affect the other

```bash
python app.py
```

Server will start at `http://localhost:5000`

## 🌐 Deploy to Render

### Quick Deploy

1. **Push this repository to GitHub**
2. **Go to [Render Dashboard](https://dashboard.render.com)**
3. **Click "New +" → "Web Service"**
4. **Connect your repository**
5. **Configure:**
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 120`

6. **Add Environment Variables:**
   ```
   ORACLE_APEX_URL=https://your-apex-url.com/ords/.../
   ORACLE_APEX_SOIL_URL=https://your-apex-url.com/ords/.../
   ORACLE_APEX_POLL_INTERVAL=3
   GEMINI_API_KEY=your_gemini_api_key
   FLASK_ENV=production
   ```

7. **Deploy!**

See [RENDER_QUICK_START.md](RENDER_QUICK_START.md) for detailed instructions.

## 🔧 Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `ORACLE_APEX_URL` | Yes | - | Main greenhouse sensor data endpoint |
| `ORACLE_APEX_SOIL_URL` | No | - | Soil moisture data endpoint |
| `ORACLE_APEX_POLL_INTERVAL` | No | `3` | Polling interval in seconds |
| `GEMINI_API_KEY` | No | - | Google Gemini API key for AI analysis |
| `FLASK_ENV` | No | `production` | Flask environment mode |
| `PORT` | No | `5000` | Server port (Render sets this automatically) |

## 📝 API Response Examples

### Sensor Data with Color Coding
```json
{
  "temperature": 23.8,
  "temperature_status": "Optimal",
  "temperature_color": "#4CAF50",
  "temperature_severity": "optimal",
  "humidity": 55.0,
  "humidity_status": "Optimal",
  "humidity_color": "#4CAF50",
  "humidity_severity": "optimal",
  "soil_moisture": 50,
  "soil_moisture_status": "Optimal",
  "soil_moisture_color": "#4CAF50",
  "soil_moisture_severity": "optimal"
}
```

## 🎨 Color Coding System

- 🟢 **Green (#4CAF50)**: Optimal/Good - Everything is normal
- 🟠 **Orange (#FF9800)**: Warning/Acceptable - Attention may be needed
- 🔴 **Red (#F44336)**: Critical/Poor - Immediate action required
- ⚪ **Gray (#9E9E9E)**: Unknown/Neutral - No data or neutral status

## 🧪 Testing

```bash
python test_color_coding.py
python test_gemini.py
```

## 📄 License

Part of the EcoView Greenhouse Monitoring System.

---

**Made with ❤️ for sustainable greenhouse monitoring**
