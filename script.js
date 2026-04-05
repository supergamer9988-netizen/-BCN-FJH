document.addEventListener('DOMContentLoaded', () => {
    // Original Components Logic (Minimal fallback)
    const cards = document.querySelectorAll('.glass-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', () => card.style.transform = 'translateY(-10px) scale(1.02)');
        card.addEventListener('mouseleave', () => card.style.transform = 'translateY(0) scale(1)');
    });

    // --- Prism OS Canvas Logic ---
    const canvas = document.getElementById('prism-canvas');
    const ctx = canvas.getContext('2d');
    const btnMap = document.getElementById('btn-map');
    const btnExec = document.getElementById('btn-execute');
    const osStatus = document.getElementById('os-status');

    let paths = [];
    let isMapping = false;
    let isExecuting = false;

    // Resize canvas
    function resize() {
        canvas.width = canvas.offsetWidth;
        canvas.height = canvas.offsetHeight;
    }
    resize();
    window.addEventListener('resize', resize);

    // Draw BCN Lattice (Background)
    function drawLattice() {
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
        ctx.lineWidth = 1;
        const size = 30;
        for (let x = 0; x < canvas.width; x += size) {
            for (let y = 0; y < canvas.height; y += size) {
                ctx.beginPath();
                ctx.moveTo(x, y);
                ctx.lineTo(x + size/2, y + size/2);
                ctx.stroke();
            }
        }
    }

    function createPath() {
        const path = [];
        let x = 0;
        let y = Math.random() * canvas.height;
        path.push({x, y});
        
        while (x < canvas.width) {
            x += 20 + Math.random() * 40;
            y += (Math.random() - 0.5) * 60;
            path.push({x, y});
        }
        return path;
    }

    function animate() {
        ctx.fillStyle = 'rgba(0,0,0,0.1)';
        ctx.fillRect(0,0, canvas.width, canvas.height);
        drawLattice();

        paths.forEach((p, idx) => {
            ctx.beginPath();
            ctx.strokeStyle = isExecuting ? `hsl(${idx * 40}, 100%, 60%)` : 'rgba(0, 209, 255, 0.3)';
            ctx.lineWidth = isExecuting ? 3 : 1;
            if (isExecuting) ctx.shadowBlur = 15; ctx.shadowColor = ctx.strokeStyle;
            
            ctx.moveTo(p[0].x, p[0].y);
            for (let i = 1; i < p.length; i++) {
                ctx.lineTo(p[i].x, p[i].y);
            }
            ctx.stroke();
            ctx.shadowBlur = 0;
        });

        if (isMapping || isExecuting) requestAnimationFrame(animate);
    }

    btnMap.addEventListener('click', () => {
        isMapping = true;
        isExecuting = false;
        osStatus.textContent = "Prism.Map(): Scanning BCN Lattice for stable paths...";
        paths = [];
        for(let i=0; i<10; i++) paths.push(createPath());
        animate();
        setTimeout(() => {
            osStatus.textContent = "Status: Map Complete. 10 Topology Paths found.";
            isMapping = false;
        }, 2000);
    });

    btnExec.addEventListener('click', () => {
        if (paths.length === 0) {
            osStatus.textContent = "Error: No topology map. Run Prism.Map() first.";
            return;
        }
        isExecuting = true;
        osStatus.textContent = "Prism.Execute(): Routing asynchronous photon pulses...";
        animate();
        setTimeout(() => {
            osStatus.textContent = "Execution Results: 1.2 THz achieved. All gates synced.";
            isExecuting = false;
        }, 3000);
    });

    // --- Chaos Key Jitter Logic ---
    const jitterCanvas = document.getElementById('jitter-canvas');
    const jctx = jitterCanvas.getContext('2d');
    const keyText = document.getElementById('crypto-key');

    function resizeJitter() {
        jitterCanvas.width = jitterCanvas.offsetWidth;
        jitterCanvas.height = jitterCanvas.offsetHeight;
    }
    resizeJitter();

    let jitterOffset = 0;
    function animateJitter() {
        jctx.clearRect(0, 0, jitterCanvas.width, jitterCanvas.height);
        jctx.beginPath();
        jctx.strokeStyle = '#00D1FF';
        jctx.lineWidth = 2;
        
        jctx.moveTo(0, jitterCanvas.height / 2);
        let maxJitter = 0;
        for (let x = 0; x < jitterCanvas.width; x++) {
            const noise = (Math.random() - 0.5) * 20;
            maxJitter = Math.max(maxJitter, Math.abs(noise));
            const wave = Math.sin((x + jitterOffset) * 0.05) * 10;
            jctx.lineTo(x, jitterCanvas.height / 2 + wave + noise);
        }
        jctx.stroke();
        
        jitterOffset += 2;
        if (Math.random() > 0.95) {
            const randomID = Math.random().toString(36).substring(2, 10).toUpperCase();
            keyText.textContent = `Signature: BCX-${randomID}-GOD`;
            
            // Update Metrics
            const entropy = 60 + Math.random() * 30;
            document.getElementById('entropy-bar').style.width = entropy + '%';
            document.getElementById('jitter-val').textContent = (maxJitter * 1.5).toFixed(2) + ' mV';
        }
        
        requestAnimationFrame(animateJitter);
    }
    animateJitter();

    // --- Reservoir Learning Logic ---
    const learningBar = document.getElementById('learning-bar');
    const pA = document.getElementById('p-A');
    const pB = document.getElementById('p-B');
    const lStatus = document.getElementById('learning-status');

    let learnProgress = 0;
    function startLearning() {
        const interval = setInterval(() => {
            learnProgress += 1;
            learningBar.style.width = learnProgress + '%';
            
            if (learnProgress % 20 < 10) {
                pA.classList.add('active-pattern');
                pB.classList.remove('active-pattern');
                lStatus.textContent = "Learning: Mapping Signal A patterns...";
            } else {
                pA.classList.remove('active-pattern');
                pB.classList.add('active-pattern');
                lStatus.textContent = "Learning: Mapping Signal B patterns...";
            }

            if (learnProgress >= 100) {
                clearInterval(interval);
                lStatus.textContent = "Training Complete: Prism Kernel Synced to Hardware.";
                lStatus.style.color = "#00D1FF";
                pA.classList.remove('active-pattern');
                pB.classList.remove('active-pattern');
            }
        }, 100);
    }
    
    // Auto-start learning simulation
    setTimeout(startLearning, 2000);

    // --- Multi-Modal Sensing Logic ---
    const sBars = {
        clean: document.getElementById('s-clean'),
        alcohol: document.getElementById('s-alcohol'),
        smoke: document.getElementById('s-smoke'),
        laser: document.getElementById('s-laser')
    };
    const gateLabel = document.getElementById('gate-label');
    const sStatus = document.getElementById('sensing-status');

    function simulateSensing() {
        const rand = Math.random();
        
        // Reset
        Object.values(sBars).forEach(b => {
             b.classList.remove('hit');
             b.style.borderLeftColor = "#555";
        });

        if (rand < 0.6) {
            sBars.clean.style.borderLeftColor = "#00ff00";
            sStatus.textContent = "Status: Monitoring Environment (Clean)";
        } else if (rand < 0.8) {
            sBars.alcohol.style.borderLeftColor = "#ffcc00";
            sBars.alcohol.classList.add('hit');
            sStatus.textContent = "Status: VOCs Detected (Alcohol/Aromatic)";
        } else if (rand < 0.95) {
            sBars.smoke.style.borderLeftColor = "#ff4400";
            sBars.smoke.classList.add('hit');
            sStatus.textContent = "Status: Combustion Byproducts Detected (Smoke)";
        } else {
            sBars.laser.classList.add('hit');
            const state = gateLabel.classList.contains('diamene') ? 'graphene' : 'diamene';
            gateLabel.className = state;
            gateLabel.textContent = state === 'graphene' ? 'ON (GRAPHENE)' : 'OFF (DIAMENE)';
            sStatus.textContent = "Status: PHOTON-INDUCED GATE SWITCH!";
        }

        setTimeout(simulateSensing, 2000 + Math.random() * 2000);
    }
    simulateSensing();

    // --- Hybrid HDC-RNC Simulation ---
    const hdcCanvas = document.getElementById('hdc-canvas');
    if (hdcCanvas) {
        const hctx = hdcCanvas.getContext('2d');
        function drawHDC() {
            hctx.clearRect(0, 0, hdcCanvas.width, hdcCanvas.height);
            for (let i = 0; i < hdcCanvas.width; i += 2) {
                hctx.fillStyle = Math.random() > 0.5 ? '#00D1FF' : '#333';
                hctx.fillRect(i, 0, 1, hdcCanvas.height);
            }
            requestAnimationFrame(drawHDC);
        }
        drawHDC();
    }

    const xorInputs = [[0, 0], [0, 1], [1, 0], [1, 1]];
    const xorTargets = [0, 1, 1, 0];
    let xorIdx = 0;
    setInterval(() => {
        const inp = xorInputs[xorIdx];
        const target = xorTargets[xorIdx];
        const pred = target === 1 ? 0.9 + Math.random() * 0.1 : 0.0 + Math.random() * 0.1;
        
        document.querySelector('.xor-in').textContent = `[${inp[0]}, ${inp[1]}]`;
        document.querySelector('.xor-res').textContent = `PRED: ${pred.toFixed(4)}`;
        
        xorIdx = (xorIdx + 1) % xorInputs.length;
    }, 2000);

    // --- Hysteresis Loop Simulation ---
    const hysCanvas = document.getElementById('hysteresis-canvas');
    if (hysCanvas) {
        const hysCtx = hysCanvas.getContext('2d');
        let hysTime = 0;
        function drawHysteresis() {
            hysCtx.clearRect(0, 0, hysCanvas.width, hysCanvas.height);
            hysCtx.lineWidth = 2;
            
            // Draw UP Curve (Blue)
            hysCtx.beginPath();
            hysCtx.strokeStyle = '#00D1FF';
            for (let i = 0; i < hysCanvas.width; i++) {
                const y = hysCanvas.height - (Math.sin(i / 100 + hysTime) * 30 + 60);
                hysCtx.lineTo(i, y - 5);
            }
            hysCtx.stroke();
            
            // Draw DOWN Curve (Gold) - Offset for Hysteresis
            hysCtx.beginPath();
            hysCtx.strokeStyle = '#FFD700';
            for (let i = 0; i < hysCanvas.width; i++) {
                const y = hysCanvas.height - (Math.sin(i / 100 + hysTime) * 30 + 60);
                hysCtx.lineTo(i, y + 15);
            }
            hysCtx.stroke();
            
            hysTime += 0.05;
            requestAnimationFrame(drawHysteresis);
        }
        drawHysteresis();
    }

    setInterval(() => {
        const pred = 0.98 + Math.random() * 0.02;
        const predEl = document.getElementById('xor-pred');
        if (predEl) predEl.textContent = pred.toFixed(4);
    }, 1500);

    // --- Butterfly Logic (Figure-8) Simulation ---
    const bfCanvas = document.getElementById('butterfly-canvas');
    if (bfCanvas) {
        const bfCtx = bfCanvas.getContext('2d');
        let bfTime = 0;
        function drawButterfly() {
            bfCtx.clearRect(0, 0, bfCanvas.width, bfCanvas.height);
            bfCtx.lineWidth = 2;
            
            const midX = bfCanvas.width / 2;
            const midY = bfCanvas.height / 2;
            
            // Draw UP Curve (Cyan)
            bfCtx.beginPath();
            bfCtx.strokeStyle = '#00D1FF';
            for (let i = 0; i < bfCanvas.width; i++) {
                const y = midY + Math.sin((i - midX) / 40 + bfTime) * 30;
                bfCtx.lineTo(i, y);
            }
            bfCtx.stroke();
            
            // Draw DOWN Curve (Gold) - Inverse phase for Butterfly
            bfCtx.beginPath();
            bfCtx.strokeStyle = '#FFD700';
            for (let i = 0; i < bfCanvas.width; i++) {
                const y = midY - Math.sin((i - midX) / 40 + bfTime) * 30;
                bfCtx.lineTo(i, y);
            }
            bfCtx.stroke();
            
            // Draw Intersection Marker
            bfCtx.fillStyle = 'white';
            bfCtx.beginPath();
            bfCtx.arc(midX, midY, 4, 0, Math.PI * 2);
            bfCtx.fill();
            
            bfTime += 0.05;
            requestAnimationFrame(drawButterfly);
        }
        drawButterfly();
    }

    drawLattice();
});
