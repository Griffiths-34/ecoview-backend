"""
Gunicorn configuration file
"""
import threading
import os

def on_starting(server):
    """
    Called just before the master process is initialized.
    Start the APEX poller thread here.
    """
    print("🔧 Gunicorn on_starting hook called")
    
    # Import app to start the background thread
    from app import start_apex_poller
    start_apex_poller()
    print("✅ APEX poller started from Gunicorn hook")

# Worker configuration
workers = 1
threads = 4
worker_class = 'gthread'
timeout = 120

# Binding
bind = f"0.0.0.0:{os.getenv('PORT', '5000')}"
