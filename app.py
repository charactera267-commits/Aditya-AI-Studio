from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

# Folder Setup
EXPORT_DIR = "exports"
os.makedirs(EXPORT_DIR, exist_ok=True)
app.mount("/exports", StaticFiles(directory=EXPORT_DIR), name="exports")

@app.get("/", response_class=HTMLResponse)
def elite_dashboard():
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ADITYA AI | Elite OS</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&family=Orbitron:wght@400;700&display=swap" rel="stylesheet">
        <style>
            :root {{
                --bg: #050505;
                --neon-blue: #00F0FF;
                --neon-purple: #7B2FFF;
                --glass: rgba(255, 255, 255, 0.03);
                --glass-border: rgba(255, 255, 255, 0.1);
                --text: #F5F5F5;
            }}

            * {{ margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }}
            body {{ 
                background: var(--bg); 
                color: var(--text); 
                font-family: 'Space Grotesk', sans-serif; 
                overflow: hidden; 
                height: 100vh;
                display: flex;
            }}

            /* --- BACKGROUND EFFECTS --- */
            .bg-glow {{
                position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                background: radial-gradient(circle at 50% 50%, #1a1a2e 0%, #050505 100%);
                z-index: -1;
            }}
            .particles {{
                position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                background-image: radial-gradient(white 1px, transparent 1px);
                background-size: 50px 50px; opacity: 0.05; z-index: -1;
            }}

            /* --- SIDEBAR --- */
            nav {{
                width: 80px; height: 100vh; background: rgba(0,0,0,0.4);
                backdrop-filter: blur(20px); border-right: 1px solid var(--glass-border);
                display: flex; flex-direction: column; align-items: center; padding: 30px 0; gap: 30px;
                transition: 0.4s cubic-bezier(0.4, 0, 0.2, 1); z-index: 100;
            }}
            nav:hover {{ width: 240px; }}
            .nav-item {{
                width: 100%; display: flex; align-items: center; padding: 0 25px;
                color: rgba(255,255,255,0.4); text-decoration: none; font-size: 18px; transition: 0.3s;
                height: 50px; position: relative;
            }}
            .nav-item i {{ min-width: 30px; }}
            .nav-item span {{ margin-left: 20px; opacity: 0; white-space: nowrap; font-size: 14px; letter-spacing: 1px; }}
            nav:hover .nav-item span {{ opacity: 1; }}
            .nav-item:hover {{ color: var(--neon-blue); text-shadow: 0 0 10px var(--neon-blue); }}
            .nav-item.active {{ color: var(--neon-purple); border-right: 3px solid var(--neon-purple); }}

            /* --- MAIN CONTENT --- */
            main {{ flex: 1; height: 100vh; overflow-y: auto; padding: 40px; position: relative; scroll-behavior: smooth; }}
            
            /* --- TOP BAR --- */
            .top-bar {{
                display: flex; justify-content: space-between; align-items: center; margin-bottom: 50px;
            }}
            .status {{ display: flex; align-items: center; gap: 10px; font-size: 12px; letter-spacing: 2px; color: var(--neon-blue); }}
            .pulse {{ width: 8px; height: 8px; background: var(--neon-blue); border-radius: 50%; box-shadow: 0 0 10px var(--neon-blue); animation: pulse 2s infinite; }}
            @keyframes pulse {{ 0% {{ transform: scale(1); opacity: 1; }} 50% {{ transform: scale(1.5); opacity: 0.5; }} 100% {{ transform: scale(1); opacity: 1; }} }}
            
            .user-profile {{ 
                width: 45px; height: 45px; border-radius: 50%; border: 2px solid var(--neon-purple);
                background: url('https://www.facebook.com/profile.php?id=100082403413385') center/cover;
                box-shadow: 0 0 15px rgba(123, 47, 255, 0.3);
            }}

            /* --- HERO SECTION --- */
            .hero {{ text-align: center; margin: 60px 0; }}
            .orb-container {{ position: relative; width: 200px; height: 200px; margin: 0 auto 30px; }}
            .orb {{
                width: 100%; height: 100%; background: radial-gradient(circle, var(--neon-blue) 0%, var(--neon-purple) 100%);
                border-radius: 50%; filter: blur(40px); opacity: 0.5; animation: rotate 10s linear infinite;
            }}
            .orb-core {{
                position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
                width: 120px; height: 120px; background: rgba(0,0,0,0.8);
                border: 1px solid var(--neon-blue); border-radius: 50%; display: flex; align-items: center; justify-content: center;
                box-shadow: inset 0 0 20px var(--neon-blue);
            }}
            @keyframes rotate {{ from {{ transform: rotate(0deg); }} to {{ transform: rotate(360deg); }} }}

            h1 {{ font-family: 'Orbitron', sans-serif; font-size: 45px; letter-spacing: 8px; margin-bottom: 10px; }}
            .motto {{ opacity: 0.5; letter-spacing: 4px; font-size: 14px; text-transform: uppercase; }}

            /* --- STUDIO PANEL --- */
            .studio-grid {{
                display: grid; grid-template-columns: 2fr 1fr; gap: 30px; margin-top: 50px;
            }}
            .glass-panel {{
                background: var(--glass); backdrop-filter: blur(30px); border: 1px solid var(--glass-border);
                border-radius: 30px; padding: 30px; position: relative; overflow: hidden;
            }}
            .glass-panel::before {{
                content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%;
                background: linear-gradient(45deg, transparent, rgba(255,255,255,0.03), transparent);
                transform: rotate(45deg); animation: shimmer 6s infinite;
            }}
            @keyframes shimmer {{ 0% {{ left: -100%; }} 100% {{ left: 100%; }} }}

            /* --- UPLOAD AREA --- */
            .upload-zone {{
                border: 1px dashed var(--neon-blue); border-radius: 20px; padding: 60px 20px;
                text-align: center; cursor: pointer; transition: 0.3s; margin-top: 20px;
            }}
            .upload-zone:hover {{ background: rgba(0, 240, 255, 0.05); box-shadow: 0 0 30px rgba(0, 240, 255, 0.1); }}
            
            .btn-action {{
                background: linear-gradient(90deg, var(--neon-blue), var(--neon-purple));
                border: none; padding: 15px 40px; border-radius: 100px; color: white;
                font-weight: bold; cursor: pointer; margin-top: 20px; font-family: 'Orbitron', sans-serif;
                letter-spacing: 2px; transition: 0.3s;
            }}
            .btn-action:hover {{ transform: translateY(-3px); box-shadow: 0 10px 30px rgba(0, 240, 255, 0.4); }}

            /* --- STATS --- */
            .stat-row {{ display: flex; justify-content: space-between; margin-bottom: 15px; font-size: 12px; }}
            .progress-bg {{ height: 4px; background: #222; border-radius: 10px; overflow: hidden; }}
            .progress-bar {{ height: 100%; width: 75%; background: var(--neon-blue); box-shadow: 0 0 10px var(--neon-blue); }}

            /* --- SOCIALS --- */
            .social-dock {{
                position: fixed; bottom: 30px; right: 30px; display: flex; gap: 15px;
            }}
            .social-btn {{
                width: 50px; height: 50px; background: var(--glass); border: 1px solid var(--glass-border);
                border-radius: 15px; display: flex; align-items: center; justify-content: center;
                color: white; font-size: 20px; transition: 0.3s; backdrop-filter: blur(10px);
            }}
            .social-btn:hover {{ border-color: var(--neon-purple); color: var(--neon-purple); transform: scale(1.1); }}

            /* --- MOBILE ADAPTATION --- */
            @media (max-width: 768px) {{
                nav {{ width: 0; position: fixed; left: -80px; }}
                main {{ padding: 20px; }}
                h1 {{ font-size: 28px; }}
                .studio-grid {{ grid-template-columns: 1fr; }}
            }}
        </style>
    </head>
    <body>
        <div class="bg-glow"></div>
        <div class="particles"></div>

        <nav>
            <div class="nav-item" style="margin-bottom: 40px; color: var(--neon-blue);"><i class="fas fa-atom"></i><span>ADITYA CORE</span></div>
            <a href="#" class="nav-item active"><i class="fas fa-th-large"></i><span>DASHBOARD</span></a>
            <a href="#" class="nav-item"><i class="fas fa-film"></i><span>AI STUDIO</span></a>
            <a href="#" class="nav-item"><i class="fas fa-wand-magic-sparkles"></i><span>IMAGE GENERATOR</span></a>
            <a href="#" class="nav-item"><i class="fas fa-microphone-lines"></i><span>VOICE AI</span></a>
            <a href="#" class="nav-item" style="margin-top: auto;"><i class="fas fa-cog"></i><span>SETTINGS</span></a>
        </nav>

        <main>
            <div class="top-bar">
                <div class="status"><div class="pulse"></div> SYSTEM ONLINE: 2030 PROTOCOL</div>
                <div style="display:flex; gap: 20px; align-items:center;">
                    <i class="fas fa-search" style="opacity:0.4;"></i>
                    <div class="user-profile"></div>
                </div>
            </div>

            <div class="hero">
                <div class="orb-container">
                    <div class="orb"></div>
                    <div class="orb-core"><i class="fas fa-brain" style="font-size: 40px; color: var(--neon-blue);"></i></div>
                </div>
                <h1>ADITYA TRIPATHI</h1>
                <div class="motto">Create. Automate. Dominate.</div>
                <p style="opacity: 0.4; font-size: 12px; margin-top: 10px;">First AI Operating System from Chhattisgarh, India</p>
            </div>

            <div class="studio-grid">
                <div class="glass-panel">
                    <h3 style="letter-spacing: 2px;"><i class="fas fa-bolt" style="color: var(--neon-blue);"></i> NEURAL VIDEO ENGINE</h3>
                    <div class="upload-zone" id="dropZone" onclick="document.getElementById('fileInput').click()">
                        <i class="fas fa-cloud-arrow-up" style="font-size: 40px; opacity: 0.3; margin-bottom: 15px;"></i>
                        <p style="opacity: 0.6;">Initialize Neural Bypass: Drag & Drop Anime Clips</p>
                        <input type="file" id="fileInput" hidden onchange="startProcessing()">
                    </div>
                    <div id="processArea" style="display:none; margin-top: 30px;">
                        <div class="stat-row"><span>BYPASSING COPYRIGHT...</span><span>88%</span></div>
                        <div class="progress-bg"><div class="progress-bar" style="width: 88%;"></div></div>
                        <button class="btn-action" style="width: 100%;">EXPORT VIRAL CLIP</button>
                    </div>
                </div>

                <div class="glass-panel">
                    <h3 style="letter-spacing: 2px; font-size: 14px;">SYSTEM ANALYTICS</h3>
                    <div style="margin-top: 30px;">
                        <div class="stat-row"><span>NEURAL LOAD</span><span>42%</span></div>
                        <div class="progress-bg" style="margin-bottom: 20px;"><div class="progress-bar" style="width: 42%; background: var(--neon-purple);"></div></div>
                        
                        <div class="stat-row"><span>GPU SIMULATION</span><span>91%</span></div>
                        <div class="progress-bg" style="margin-bottom: 20px;"><div class="progress-bar" style="width: 91%;"></div></div>

                        <div class="stat-row"><span>VIRAL PREDICTION</span><span>🔥 HIGH</span></div>
                        <div style="height: 60px; background: rgba(255,255,255,0.02); border-radius: 15px; display:flex; align-items:center; justify-content:center; border: 1px solid rgba(123, 47, 255, 0.2);">
                             <i class="fas fa-chart-line" style="color: var(--neon-purple); margin-right: 10px;"></i> 98.4% Retainment
                        </div>
                    </div>
                </div>
            </div>
        </main>

        <div class="social-dock">
            <a href="https://www.instagram.com/goku80242?igsh=MWNudjhmNjh5dzEyNw==" target="_blank" class="social-btn"><i class="fab fa-instagram"></i></a>
            <a href="https://www.facebook.com/profile.php?id=100082403413385" target="_blank" class="social-btn"><i class="fab fa-facebook-f"></i></a>
        </div>

        <script>
            function startProcessing() {{
                document.getElementById('dropZone').style.display = 'none';
                document.getElementById('processArea').style.display = 'block';
            }}
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
