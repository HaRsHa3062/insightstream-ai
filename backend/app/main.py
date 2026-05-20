from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="InsightStream AI")

@app.get("/")
async def home():
    html = """
    <html>
    <head>
        <title>InsightStream AI - MVP</title>
        <style>
            body { font-family: Arial; background: #0a0a0a; color: white; padding: 50px; text-align: center; }
            h1 { color: #22c55e; }
            .card { background: #1f1f1f; padding: 30px; margin: 20px auto; max-width: 700px; border-radius: 12px; border: 1px solid #333; }
            button { padding: 15px 30px; background: #22c55e; color: black; border: none; border-radius: 8px; font-size: 18px; cursor: pointer; }
        </style>
    </head>
    <body>
        <h1>✅ InsightStream AI</h1>
        <p>Live MVP Dashboard for Subscription Brands</p>
        
        <div class="card">
            <h2>Executive Command Center</h2>
            <p>Active Subscribers: <strong>87</strong></p>
            <p>Churn Rate: <strong style="color:orange">12.4%</strong></p>
            <p style="color:red">⚠️ Hazard: Month 3 Retention Drop Detected</p>
        </div>

        <div class="card">
            <h3>AI Solution Feed</h3>
            <p><strong>Recommendation:</strong> Fix delivery delays in South India to save $4,200 this month</p>
            <button onclick="alert('✅ Fix Deployed!')">Deploy Tactical Fix</button>
        </div>

        <p style="margin-top:60px; color:#888;">Sarah Jenkins • BloomBox Coffee</p>
    </body>
    </html>
    """
    return HTMLResponse(html)

@app.get("/health")
async def health():
    return {"status": "healthy"}
