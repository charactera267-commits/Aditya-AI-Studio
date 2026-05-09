 from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

# System Directories
os.makedirs("exports", exist_ok=True)
app.mount("/exports", StaticFiles(directory="exports"), name="exports")

@app.get("/", response_class=HTMLResponse)
def ultimate_os():
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ADITYA AI | QUANTUM INTERFACE</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&family=Orbitron:wght@400;900&family=Sora:wght@300;600&display=swap" rel="stylesheet">
        <style>
            :root {{
                --black: #050505;
                --neon-blue: #00F0FF;
                --electric-purple: #7B2FFF;
                --glass: rgba(255, 255, 255, 0.03);
                --glass-border: rgba(255, 255, 255, 0.08);
                --shadow: 0 0 30px rgba(0, 240, 255, 0.1);
            }}

            * {{ margin: 0; padding: 0; box-sizing: border-box; cursor: crosshair; }}
            
            body {{
                background-color: var(--black);
                color: #F5F5F5;
                font-family: 'Sora', sans-serif;
                height: 100vh;
                overflow: hidden;
                display: flex;
            }}

            /* --- CINEMATIC BACKGROUND --- */
            .quantum-bg {{
                position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                background: radial-gradient(circle at 20% 30%, #0d0d2b 0%, #050505 100%);
                z-index: -2;
            }}
            .grid-overlay {{
                position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                background-image: linear-gradient(var(--glass-border) 1px, transparent 1px), 
                                  linear-gradient(90deg, var(--glass-border) 1px, transparent 1px);
                background-size: 40px 40px; z-index: -1; opacity: 0.2;
            }}

            /* --- LEFT SIDEBAR (APPLE-TESLA STYLE) --- */
            aside {{
                width: 90px; height: 100vh; background: rgba(0,0,0,0.6);
                backdrop-filter: blur(40px); border-right: 1px solid var(--glass-border);
                display: flex; flex-direction: column; align-items: center; padding: 40px 0; gap: 40px;
                transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1); z-index: 100;
            }}
            aside:hover {{ width: 260px; }}
            .nav-icon {{
                width: 50px; height: 50px; display: flex; align-items: center; justify-content: center;
                border-radius: 15px; transition: 0.3s; color: rgba(255,255,255,0.4);
                text-decoration: none; position: relative; overflow: hidden;
            }}
            .nav-icon span {{
                display: none; position: absolute; left: 70px; white-space: nowrap;
                font-family: 'Space Grotesk', sans-serif; letter-spacing: 2px; font-size: 12px;
            }}
            aside:hover .nav-icon span {{ display: block; }}
            .nav-icon:hover, .nav-icon.active {{
                background: var(--glass); color: var(--neon-blue); box-shadow: var(--shadow);
            }}

            /* --- MAIN INTERFACE --- */
            main {{ flex: 1; height: 100vh; overflow-y: scroll; padding: 40px; scrollbar-width: none; }}
            main::-webkit-scrollbar {{ display: none; }}

            /* --- TOP HEADER --- */
            header {{
                display: flex; justify-content: space-between; align-items: center; margin-bottom: 60px;
            }}
            .status-indicator {{
                display: flex; align-items: center; gap: 12px; font-size: 10px;
                letter-spacing: 3px; color: var(--neon-blue); font-family: 'Orbitron';
            }}
            .pulse-dot {{
                width: 6px; height: 6px; background: var(--neon-blue); border-radius: 50%;
                animation: pulse 2s infinite; box-shadow: 0 0 10px var(--neon-blue);
            }}
            @keyframes pulse {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0.3; }} 100% {{ opacity: 1; }} }}

            /* --- HERO CORE (THE ORB) --- */
            .ai-core-container {{
                text-align: center; position: relative; margin: 40px 0;
            }}
            .orb-glow {{
                position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
                width: 300px; height: 300px; background: radial-gradient(circle, var(--neon-blue) 0%, transparent 70%);
                filter: blur(80px); opacity: 0.2; animation: float 6s ease-in-out infinite;
            }}
            .orb-visual {{
                width: 140px; height: 140px; border: 2px solid var(--neon-blue);
                border-radius: 50%; margin: 0 auto; position: relative;
                box-shadow: inset 0 0 20px var(--neon-blue), 0 0 40px rgba(0, 240, 255, 0.2);
                display: flex; align-items: center; justify-content: center;
                animation: rotate 20s linear infinite;
            }}
            @keyframes rotate {{ from {{ transform: rotate(0deg); }} to {{ transform: rotate(360deg); }} }}
            @keyframes float {{ 0%, 100% {{ transform: translate(-50%, -55%); }} 50% {{ transform: translate(-50%, -45%); }} }}

            .welcome-text h1 {{
                font-family: 'Orbitron'; font-weight: 900; font-size: 56px; 
                letter-spacing: 15px; margin-top: 20px; text-shadow: 0 0 20px rgba(255,255,255,0.1);
            }}
            .motto {{
                font-family: 'Space Grotesk'; font-size: 12px; letter-spacing: 8px;
                opacity: 0.4; text-transform: uppercase; margin-top: 10px;
            }}

            /* --- STUDIO DASHBOARD (Billion Dollar Look) --- */
            .studio-grid {{
                display: grid; grid-template-columns: 1.5fr 1fr; gap: 30px; margin-top: 80px;
            }}
            .glass-panel {{
                background: var(--glass); backdrop-filter: blur(40px); border: 1px solid var(--glass-border);
                border-radius: 35px; padding: 40px; transition: 0.4s;
            }}
            .glass-panel:hover {{ border-color: rgba(0, 240, 255, 0.3); transform: translateY(-5px); }}

            .upload-zone {{
                border: 1px dashed rgba(255,255,255,0.1); border-radius: 25px; padding: 60px 20px;
                text-align: center; cursor: pointer; transition: 0.3s;
            }}
            .upload-zone:hover {{ background: rgba(255,255,255,0.02); border-color: var(--neon-blue); }}

            .neon-button {{
                width: 100%; background: white; color: black; border: none; padding: 20px;
                border-radius: 100px; font-family: 'Orbitron'; font-weight: 900; font-size: 14px;
                letter-spacing: 3px; cursor: pointer; margin-top: 30px; transition: 0.4s;
            }}
            .neon-button:hover {{ background: var(--neon-blue); transform: scale(1.02); box-shadow: 0 10px 40px rgba(0, 240, 255, 0.3); }}

            /* --- ANALYTICS BARS --- */
            .analytics-bar {{
                height: 4px; background: rgba(255,255,255,0.05); border-radius: 10px; margin: 20px 0;
                position: relative; overflow: hidden;
            }}
            .bar-fill {{
                position: absolute; height: 100%; background: linear-gradient(90deg, var(--neon-blue), var(--electric-purple));
                box-shadow: 0 0 15px var(--neon-blue);
            }}

            /* --- SOCIAL DOCK --- */
            .social-dock {{
                position: fixed; bottom: 40px; right: 40px; display: flex; gap: 20px;
            }}
            .social-link {{
                width: 55px; height: 55px; background: var(--glass); border: 1px solid var(--glass-border);
                border-radius: 18px; display: flex; align-items: center; justify-content: center;
                color: white; font-size: 22px; transition: 0.4s; backdrop-filter: blur(20px);
            }}
            .social-link:hover {{ border-color: var(--electric-purple); transform: translateY(-10px); color: var(--electric-purple); }}

        </style>
    </head>
    <body>
        <div class="quantum-bg"></div>
        <div class="grid-overlay"></div>

        <aside>
            <a href="#" class="nav-icon active"><i class="fas fa-layer-group"></i><span>DASHBOARD</span></a>
            <a href="#" class="nav-icon"><i class="fas fa-wand-magic-sparkles"></i><span>AI STUDIO</span></a>
            <a href="#" class="nav-icon"><i class="fas fa-video"></i><span>VIDEO EDITOR</span></a>
            <a href="#" class="nav-icon"><i class="fas fa-brain"></i><span>NEURAL VOICE</span></a>
            <a href="#" class="nav-icon" style="margin-top: auto;"><i class="fas fa-sliders"></i><span>SETTINGS</span></a>
        </aside>

        <main>
            <header>
                <div class="status-indicator">
                    <div class="pulse-dot"></div> SYSTEM ENCRYPTED // ADITYA TRIPATHI OS 2030
                </div>
                <div style="display:flex; gap: 30px; align-items:center;">
                    <i class="fas fa-search" style="opacity:0.3; font-size: 18px;"></i>
                    <div style="width: 45px; height: 45px; border-radius: 14px; border: 1px solid var(--neon-blue); background: rgba(0,240,255,0.1);"></div>
                </div>
            </header>

            <div class="ai-core-container">
                <div class="orb-glow"></div>
                <div class="orb-visual">
                    <i class="fas fa-atom" style="font-size: 40px; color: var(--neon-blue); transform: rotate(-20deg);"></i>
                </div>
                <div class="welcome-text">
                    <h1>ADITYA</h1>
                    <div class="motto">CREATE. AUTOMATE. DOMINATE.</div>
                    <p style="margin-top: 15px; opacity: 0.4; font-size: 11px; letter-spacing: 2px;">BY ADITYA TRIPATHI // CHHATTISGARH'S FIRST AI ENGINE</p>
                </div>
            </div>

            <div class="studio-grid">
                <div class="glass-panel">
                    <h3 style="font-family: 'Orbitron'; font-size: 14px; letter-spacing: 3px; margin-bottom: 30px;">NEURAL BYPASS ENGINE</h3>
                    <div class="upload-zone" onclick="document.getElementById('f').click()">
                        <i class="fas fa-dna" style="font-size: 40px; opacity: 0.2; margin-bottom: 20px; color: var(--neon-blue);"></i>
                        <p style="font-size: 12px; opacity: 0.5; letter-spacing: 1px;">DRAG ANIME CLIPS TO INITIALIZE QUANTUM PROCESSING</p>
                        <form action="/process" method="post" enctype="multipart/form-data">
                            <input type="file" id="f" name="file" hidden onchange="form.submit()">
                        </form>
                    </div>
                    <button class="neon-button">EXECUTE BYPASS</button>
                </div>

                <div class="glass-panel">
                    <h3 style="font-family: 'Orbitron'; font-size: 14px; letter-spacing: 3px; margin-bottom: 30px;">SYSTEM ANALYTICS</h3>
                    
                    <p style="font-size: 10px; opacity: 0.4;">NEURAL LOAD</p>
                    <div class="analytics-bar"><div class="bar-fill" style="width: 42%;"></div></div>

                    <p style="font-size: 10px; opacity: 0.4; margin-top: 25px;">GPU RENDERING POWER</p>
                    <div class="analytics-bar"><div class="bar-fill" style="width: 89%;"></div></div>

                    <p style="font-size: 10px; opacity: 0.4; margin-top: 25px;">VIRAL PROPENSITY INDEX</p>
                    <div style="margin-top: 15px; font-family: 'Orbitron'; color: var(--neon-blue); font-size: 24px;">98.2% <span style="font-size: 10px; opacity:0.5;">CRITICAL MATCH</span></div>
                </div>
            </div>
        </main>

        <div class="social-dock">
            <a href="https://www.instagram.com/goku80242" target="_blank" class="social-link"><i class="fab fa-instagram"></i></a>
            <a href="https://www.facebook.com/profile.php?id=100082403413385" target="_blank" class="social-link"><i class="fab fa-facebook-f"></i></a>
        </div>
    </body>
    </html>
    """
           
