#!/usr/bin/env python3
"""Report installed capabilities, without installing or calling providers."""
import json, os, shutil, subprocess
report = {'python':True,'node':shutil.which('node'),'ffmpeg':shutil.which('ffmpeg'),'ffprobe':shutil.which('ffprobe'),'fontconfig':shutil.which('fc-match'),'network_required_for_render':False,'browser_launch_tested':False}
if report['node']:
    js = "const fs=require('fs'),path=require('path');let p;try{p=require('playwright')}catch(e){p=require(path.join(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES||'', 'playwright'))}const exe=process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH||[p.chromium.executablePath(),'/usr/bin/chromium','/usr/bin/google-chrome'].find(x=>fs.existsSync(x));console.log(JSON.stringify({playwright:true,chromium:exe||null,browserInstalled:!!exe&&fs.existsSync(exe)}));"
    r = subprocess.run([report['node'],'-e',js],capture_output=True,text=True)
    report.update(json.loads(r.stdout) if r.returncode==0 else {'playwright':False,'detail':'Install local Playwright and Chromium outside offline execution.'})
    canvas_js = "const path=require('path');try{require('@napi-rs/canvas')}catch(e){require(path.join(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES||'','@napi-rs/canvas'))}"
    c = subprocess.run([report['node'],'-e',canvas_js],capture_output=True,text=True)
    report['local_canvas_adapter'] = c.returncode == 0
print(json.dumps(report,indent=2))
