from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def dashboard():
    return f"""
    <html>
    <head><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{ background:#050505; color:white; font-family:sans-serif; text-align:center; padding:40px 20px; }}
        .glass {{ background:rgba(255,255,255,0.05); backdrop-filter:blur(10px); border-radius:30px; padding:40px; border:1px solid #00f2fe; box-shadow:0 0 20px #00f2fe33; max-width:500px; margin:auto; }}
        h1 {{ letter-spacing:5px; color:#00f2fe; text-shadow:0 0 10px #00f2fe; margin-bottom:10px; }}
        .subtitle {{ opacity:0.6; font-size:12px; letter-spacing:2px; margin-bottom:30px; }}
        .btn {{ display:inline-block; background:#00f2fe; color:black; padding:18px 50px; border-radius:50px; font-weight:bold; cursor:pointer; text-decoration:none; box-shadow: 0 5px 15px rgba(0,242,254,0.4); }}
    </style></head>
    <body>
        <div class="glass">
            <h1>ADITYA STUDIO</h1>
            <div class="subtitle">CG'S FIRST ANIME AI ENGINE</div>
            <form action="/process" method="post" enctype="multipart/form-data">
                <label for="v" class="btn">🚀 UPLOAD VIDEO</label>
                <input type="file" name="file" id="v" hidden onchange="form.submit()">
            </form>
        </div>
        <p style="margin-top:40px; opacity:0.3; font-size:10px;">Built by Aditya Tripathi | System Online</p>
    </body></html>
    """

@app.post("/process")
async def process(file: UploadFile = File(...)):
    return HTMLResponse("<script>alert('AI Engine Started!'); window.location.href='/';</script>")
  
