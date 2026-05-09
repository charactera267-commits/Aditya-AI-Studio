from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

# System Directories setup
os.makedirs("exports", exist_ok=True)
app.mount("/exports", StaticFiles(directory="exports"), name="exports")

@app.get("/", response_class=HTMLResponse)
def ultimate_os():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ADITYA AI | QUANTUM INTERFACE</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&family=Orbitron:wght@400;900&family=Sora:wght@300;600&display=swap" rel="stylesheet">
        <style>
            :root {
                --black: #050505;
                --neon-blue: #00F0FF;
                --electric-purple: #7B2FFF;
                --glass: rgba(255, 255, 255, 0.03);
                --glass-border: rgba(255, 255, 255, 0.08);
            }

            * { margin: 0; padding: 0; box-sizing: border-box; }
            
            body {
                background-color: var(--black); color: #F5F5F5;
                font-family: 'Sora', sans-serif; height: 100vh;
                overflow: hidden; display: flex;
            }

            /* --- BACKGROUND --- */
            .bg-glow {
                position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                background: radial-gradient(circle at 50% 30%, #0d0d2b 0%, #050505 100%);
                z-index: -2;
            }
            .grid {
                position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                background-image: linear-gradient(var(--glass-border) 1px, transparent 1px), 
                                  linear-gradient(90deg, var(--glass-border) 1px, transparent 1px);
                background-size: 40px 40px; z-index: -1; opacity: 0.3;
            }

            /* --- SIDEBAR --- */
            aside {
                width: 90px; height: 100vh; background: rgba(0,0,0,0.6);
                backdrop-filter: blur(40px); border-right: 1px solid var(--glass-border);
                display: flex; flex-direction: column; align-items: center; padding: 40px 0; gap: 40px;
                transition: 0.4s; z-index: 100;
            }
            aside:hover { width: 240px; }
            .nav-icon {
                width: 50px; height: 50px; display: flex; align-items: center; justify-content: center;
                border-radius: 15px; color: rgba(255,255,255,0.4); text-decoration: none;
                position: relative; transition: 0.3s;
            }
            .nav-icon span {
                display: none; position: absolute; left: 70px; white-space: nowrap;
                font-family: 'Space Grotesk'; letter-spacing: 2px; font-size: 12px;
            }
            aside:hover .nav-icon span { display: block; }
            .nav-icon:hover, .nav-icon.active {
                background: var(--glass); color: var(--neon-blue); box-shadow: 0 0 20px rgba(0, 240, 255, 0.2);
            }

            /* --- MAIN --- */
            main { flex: 1; padding: 40px; overflow-y: auto; scrollbar-width: none; }
            
            header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 50px; }
            .status { display: flex; align-items: center; gap: 10px; font-size: 11px; letter-spacing: 3px; color: var(--neon-blue); font-family: 'Orbitron'; }
            .pulse { width: 8px; height: 8px; background: var(--neon-blue); border-radius: 50%; animation: pulse 2s infinite; box-shadow: 0 0 10px var(--neon-blue); }
            @keyframes pulse { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.4; transform: scale(1.5); } }

            /* --- ORB --- */
            .core-box { text-align: center; position: relative; margin: 30px 0; }
            .orb-glow {
                position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
                width: 250px; height: 250px; background: radial-gradient(circle, var(--neon-blue) 0%, transparent 70%);
                filter: blur(60px); opacity: 0.3; animation: breathe 5s infinite;
            }
            .orb {
                width: 120px; height: 120px; border: 2px solid var(--neon-blue); border-radius: 50%;
                margin: 0 auto; display: flex; align-items: center; justify-content: center;
                box-shadow: inset 0 0 30px rgba(0, 240, 255, 0.3); animation: spin 15s linear infinite; position: relative;
            }
            @keyframes breathe { 0%, 100% { transform: translate(-50%, -50%) scale(1); } 50% { transform: translate(-50%, -50%) scale(1.1); } }
            @keyframes spin { 100% { transform: rotate(360deg); } }
            
            h1 { font-family: 'Orbitron'; font-size: 45px; letter-spacing: 12px; margin-top: 20px; text-shadow: 0 0 20px rgba(255,255,255,0.1); }
            .subtitle { font-family: 'Space Grotesk'; font-size: 11px; letter-spacing: 6px; opacity: 0.5; margin-top: 10px; }

            /* --- PANELS --- */
            .grid-system { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 60px; }
            .glass-card { background: var(--glass); backdrop-filter: blur(30px); border: 1px solid var(--glass-border); border-radius: 30px; padding: 40px; }
            
            .upload-zone { border: 1px dashed rgba(255,255,255,0.2); padding: 50px 20px; text-align: center; border-radius: 20px; cursor: pointer; transition: 0.3s; margin-top: 20px; }
            .upload-zone:hover { background: rgba(0,240,255,0.05); border-color: var(--neon-blue); }
            
            /* --- PROGRESS & DOWNLOAD --- */
            #statusArea { display: none; margin-top: 30px; }
            .prog-bg { height: 4px; background: rgba(255,255,255,0.1); border-radius: 10px; overflow: hidden; margin: 15px 0; }
            .prog-fill { height: 100%; width: 0%; background: var(--neon-blue); transition: 0.5s; box-shadow: 0 0 10px var(--neon-blue); }
            
            .btn-download { display: none; width: 100%; background: white; color: black; padding: 15px; border-radius: 100px; text-align: center; text-decoration: none; font-family: 'Orbitron'; font-weight: bold; letter-spacing: 2px; margin-top: 20px; transition: 0.3s; }
            .btn-download:hover { background: var(--neon-blue); box-shadow: 0 0 20px var(--neon-blue); transform: scale(1.02); }

            .social-dock { position: fixed; bottom: 30px; right: 30px; display: flex; gap: 15px; }
            .s-icon { width: 50px; height: 50px; background: var(--glass); border: 1px solid var(--glass-border); border-radius: 15px; display: flex; align-items: center; justify-content: center; color: white; font-size: 20px; text-decoration: none; transition: 0.3s; backdrop-filter: blur(10px); }
            .s-icon:hover { color: var(--electric-purple); border-color: var(--electric-purple); transform: translateY(-5px); }
        </style>
    </head>
    <body>
        <div class="bg-glow"></div>
        <div class="grid"></div>

        <aside>
            <a href="#" class="nav-icon active"><i class="fas fa-layer-group"></i><span>DASHBOARD</span></a>
            <a href="#" class="nav-icon"><i class="fas fa-wand-magic-sparkles"></i><span>AI STUDIO</span></a>
            <a href="#" class="nav-icon"><i class="fas fa-chart-line"></i><span>ANALYTICS</span></a>
            <a href="#" class="nav-icon" style="margin-top: auto;"><i class="fas fa-cog"></i><span>SETTINGS</span></a>
        </aside>

        <main>
            <header>
                <div class="status"><div class="pulse"></div> ADITYA OS // SYSTEM ONLINE</div>
            </header>

            <div class="core-box">
                <div class="orb-glow"></div>
                <div class="orb"><i class="fas fa-atom" style="font-size: 40px; color: var(--neon-blue);"></i></div>
                <h1>ADITYA TRIPATHI</h1>
                <div class="subtitle">CG'S FIRST ANIME AI ENGINE</div>
            </div>

            <div class="grid-system">
                <div class="glass-card">
                    <h3 style="font-family: 'Orbitron'; font-size: 14px; letter-spacing: 2px;">NEURAL VIDEO PROCESSOR</h3>
                    
                    <div id="dropZone" class="upload-zone" onclick="document.getElementById('fileInput').click()">
                        <i class="fas fa-cloud-upload-alt" style="font-size: 40px; color: var(--neon-blue); margin-bottom: 15px;"></i>
                        <p style="font-size: 12px; opacity: 0.5;">CLICK TO UPLOAD ANIME CLIP</p>
                        <form id="uploadForm" action="/process" method="post" enctype="multipart/form-data">
                            <input type="file" id="fileInput" name="file" hidden onchange="startProcessing()">
                        </form>
                    </div>

                    <div id="statusArea">
                        <div id="statusText" style="font-size: 11px; letter-spacing: 2px; color: var(--neon-blue);">INITIALIZING...</div>
                        <div class="prog-bg"><div id="progFill" class="prog-fill"></div></div>
                        <a id="downloadBtn" href="#" class="btn-download"><i class="fas fa-download"></i> SAVE PRO CLIP</a>
                    </div>
                </div>

                <div class="glass-card">
                    <h3 style="font-family: 'Orbitron'; font-size: 14px; letter-spacing: 2px;">SYSTEM LOAD</h3>
                    <p style="font-size: 10px; opacity: 0.5; margin-top: 30px;">CPU SIMULATION</p>
                    <div class="prog-bg"><div class="prog-fill" style="width: 34%; background: var(--electric-purple);"></div></div>
                    
                    <p style="font-size: 10px; opacity: 0.5; margin-top: 20px;">AI BYPASS ENGINE</p>
                    <div class="prog-bg"><div class="prog-fill" style="width: 88%;"></div></div>
                </div>
            </div>
        </main>

        <div class="social-dock">
            <a href="https://www.instagram.com/goku80242" class="s-icon" target="_blank"><i class="fab fa-instagram"></i></a>
            <a href="https://www.facebook.com/profile.php?id=100082403413385" class="s-icon" target="_blank"><i class="fab fa-facebook-f"></i></a>
        </div>

        <script>
            function startProcessing() {
                document.getElementById('dropZone').style.display = 'none';
                document.getElementById('statusArea').style.display = 'block';
                
                let fill = document.getElementById('progFill');
                let txt = document.getElementById('statusText');

                fill.style.width = "30%";
                txt.innerText = "UPLOADING TO CLOUD...";

                setTimeout(() => {
                    fill.style.width = "75%";
                    txt.innerText = "BYPASSING COPYRIGHT ALGORITHMS...";
                    
                    setTimeout(() => {
                        fill.style.width = "100%";
                        txt.innerText = "PROCESSING COMPLETE!";
                        txt.style.color = "#00FF00";
                        
                        // Fake Download trigger for demo (Needs proper backend integration for real file)
                        document.getElementById('downloadBtn').style.display = "block";
                    }, 3000);
                }, 2000);
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.post("/process")
async def process(file: UploadFile = File(...)):
    # This saves the uploaded file for real
    file_location = f"exports/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(await file.read())
    return {"info": f"file '{file.filename}' saved at '{file_location}'"}
 
