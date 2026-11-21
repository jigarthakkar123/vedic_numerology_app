/**
 * Vedic Numerology Studio - Frontend Controller
 * Handles live calculations, trilingual UI switching, and automated PDF downloads.
 */

let currentLang = 'en';
let currentProfile = null;

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', () => {
    initEventListeners();
    updateWeekdayDisplay();
    fetchAnalysis();
    refreshHistory();
});

function initEventListeners() {
    // Form submission
    const form = document.getElementById('numerology-form');
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        fetchAnalysis();
    });

    // Date picker change
    const dobInput = document.getElementById('client-dob');
    dobInput.addEventListener('change', updateWeekdayDisplay);

    // Language pills in header
    document.querySelectorAll('.lang-pill').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.lang-pill').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentLang = btn.dataset.lang;
            fetchAnalysis();
        });
    });

    // Tab buttons
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
            btn.classList.add('active');
            const targetId = btn.dataset.tab;
            document.getElementById(targetId).classList.add('active');
        });
    });

    // Single PDF Generation Buttons
    document.getElementById('btn-pdf-en').addEventListener('click', () => triggerPdfGeneration('en'));
    document.getElementById('btn-pdf-hi').addEventListener('click', () => triggerPdfGeneration('hi'));
    document.getElementById('btn-pdf-gu').addEventListener('click', () => triggerPdfGeneration('gu'));

    // Batch PDF Generation (All 3)
    document.getElementById('btn-pdf-all').addEventListener('click', triggerBatchPdfGeneration);

    // Refresh history
    document.getElementById('btn-refresh-history').addEventListener('click', refreshHistory);
}

function getFormData() {
    return {
        name: document.getElementById('client-name').value.trim() || 'Client',
        phone: document.getElementById('client-phone') ? document.getElementById('client-phone').value.trim() : '',
        dob: document.getElementById('client-dob').value,
        gender: document.getElementById('client-gender').value,
        target_date: document.getElementById('target-date').value,
        lang: currentLang,
        consultant_notes: document.getElementById('consultant-notes').value.trim()
    };
}

function updateWeekdayDisplay() {
    const dobVal = document.getElementById('client-dob').value;
    if (!dobVal) return;
    
    const d = new Date(dobVal + 'T00:00:00');
    const dayNames = {
        en: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
        hi: ['रविवार', 'सोमवार', 'मंगलवार', 'बुधवार', 'गुरुवार', 'शुक्रवार', 'शनिवार'],
        gu: ['રવિવાર', 'સોમવાર', 'મંગળવાર', 'બુધવાર', 'ગુરુવાર', 'શુક્રવાર', 'શનિવાર']
    };
    const dayIdx = d.getDay();
    const ind = document.getElementById('weekday-indicator');
    ind.textContent = `${dayNames.en[dayIdx]} (${dayNames.hi[dayIdx]} • ${dayNames.gu[dayIdx]})`;
}

function showStatus(message, type = 'loading') {
    const banner = document.getElementById('status-banner');
    banner.className = `status-banner ${type}`;
    banner.innerHTML = message;
    banner.style.display = 'flex';
}

function hideStatus() {
    const banner = document.getElementById('status-banner');
    banner.style.display = 'none';
}

// Fetch Full Calculation Analysis
async function fetchAnalysis() {
    const payload = getFormData();
    showStatus('Calculating planetary vibrations and assembling Vedic chart...', 'loading');

    try {
        const res = await fetch('/api/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const json = await res.json();
        if (!res.ok || !json.success) {
            throw new Error(json.detail || 'Calculation error occurred.');
        }

        currentProfile = json.data;
        renderDashboard(currentProfile);
        hideStatus();
    } catch (err) {
        showStatus(`Error: ${err.message}`, 'error');
    }
}

// Render Complete UI Dashboard from Profile
function renderDashboard(data) {
    const core = data.core_numbers;
    const grid = data.grid;
    const dasha = data.dasha;
    const client = data.client;

    // Quick Stats Cards
    document.getElementById('val-bn').textContent = core.bn;
    document.getElementById('sub-bn').textContent = core.bn_planet;
    document.getElementById('val-dn').textContent = core.dn;
    document.getElementById('sub-dn').textContent = core.dn_planet;
    document.getElementById('val-dasha').textContent = `MD: ${dasha.active_md.number} | AD: ${dasha.active_ad.ad_number} | PD: ${dasha.active_pd.number}`;
    document.getElementById('sub-dasha').textContent = `AD Active to ${dasha.active_ad.end_str}`;
    
    // Name Number (Namank)
    if (document.getElementById('val-namank')) {
        document.getElementById('val-namank').textContent = core.namank || 1;
        const hStatus = client.name_harmony ? client.name_harmony.status : 'harmonious';
        document.getElementById('sub-namank').textContent = hStatus === 'harmonious' ? 'Harmonious Alignment' : (hStatus === 'conflict' ? 'Name Tuning Advised' : 'Neutral Vibration');
    }

    // Compass Dashboard Banner
    if (data.compass) {
        if (document.getElementById('dash-friendly')) document.getElementById('dash-friendly').textContent = data.compass.friendly_nums;
        if (document.getElementById('dash-neutral')) document.getElementById('dash-neutral').textContent = data.compass.neutral_nums;
        if (document.getElementById('dash-enemy')) document.getElementById('dash-enemy').textContent = data.compass.enemy_nums;
        if (document.getElementById('dash-direction')) document.getElementById('dash-direction').textContent = data.compass.direction;
        if (document.getElementById('dash-metal')) document.getElementById('dash-metal').textContent = data.compass.metal;
        if (document.getElementById('dash-gem')) document.getElementById('dash-gem').textContent = core.gemstone;
    }
    if (client.name_harmony && document.getElementById('dash-name-harmony')) {
        document.getElementById('dash-name-harmony').innerHTML = `<strong>Name Vibration Audit:</strong> ${client.name_harmony.text}`;
    }

    // Charms
    document.getElementById('charm-days').textContent = core.favourable_days;
    document.getElementById('charm-nums').textContent = core.favourable_nums;
    document.getElementById('charm-colors').textContent = core.favourable_colors;

    // 3x3 Vedic Grid Cells
    // Order in grid cells: 3, 1, 9, 6, 7, 5, 2, 8, 4
    for (let cell of grid.cells) {
        const el = document.getElementById(`gc-${cell.num}`);
        if (el) {
            const valSpan = el.querySelector('.c-val');
            if (cell.count > 0) {
                el.classList.add('active');
                valSpan.textContent = cell.str;
            } else {
                el.classList.remove('active');
                valSpan.textContent = '-';
            }
        }
    }

    // Vibrations List
    const vibContainer = document.getElementById('vibrations-list');
    vibContainer.innerHTML = '';
    for (let v of data.vibrations) {
        const box = document.createElement('div');
        box.className = `vibe-box ${v.type === '+' ? 'badge-pos' : 'badge-neg'}`;
        box.innerHTML = `
            <div class="vibe-box-header">
                <span>Number ${v.number} (${v.count}x)</span>
                <span class="vibe-tag">${v.type_label}</span>
            </div>
            <div class="vibe-desc">${v.text}</div>
        `;
        vibContainer.appendChild(box);
    }

    // Moolank Traits & Precautions
    const mTraitsList = document.getElementById('list-moolank-traits');
    mTraitsList.innerHTML = data.moolank_qualities.map(q => `<li>${q}</li>`).join('');

    const mPrecList = document.getElementById('list-moolank-precautions');
    mPrecList.innerHTML = data.moolank_precautions.map(p => `<li>${p}</li>`).join('');

    // Dasha Cards & Table
    document.getElementById('dasha-md-num').textContent = `Mahadasha ${dasha.active_md.number}`;
    document.getElementById('dasha-md-dates').textContent = `${dasha.active_md.start_str} to ${dasha.active_md.end_str}`;
    document.getElementById('dasha-ad-num').textContent = `Antardasha ${dasha.active_ad.ad_number}`;
    document.getElementById('dasha-ad-dates').textContent = `${dasha.active_ad.start_str} to ${dasha.active_ad.end_str}`;
    document.getElementById('dasha-pd-num').textContent = `Pratyantar Dasha ${dasha.active_pd.number}`;
    document.getElementById('dasha-pd-dates').textContent = `${dasha.active_pd.start_str} to ${dasha.active_pd.end_str}`;

    const dBody = document.getElementById('dasha-timeline-body');
    dBody.innerHTML = '';
    for (let p of dasha.md_timeline) {
        const tr = document.createElement('tr');
        if (p.is_active) tr.className = 'active-row';
        tr.innerHTML = `
            <td>Mahadasha ${p.number}</td>
            <td>${p.duration} Years</td>
            <td>${p.start_str}</td>
            <td>${p.end_str}</td>
            <td>${p.is_active ? '★ Current Active Phase' : 'Inactive'}</td>
        `;
        dBody.appendChild(tr);
    }

    // Yogas
    const yogasContainer = document.getElementById('yogas-container');
    yogasContainer.innerHTML = '';
    for (let y of data.yogas) {
        const yCard = document.createElement('div');
        const isRaj = y.id === 'raj_yog';
        yCard.className = `yoga-display-card ${isRaj ? 'raj-yog' : ''}`;
        yCard.innerHTML = `
            <div class="c-header">
                <span class="c-title">${y.name}</span>
                <span class="c-tag">${y.tag}</span>
            </div>
            <div class="c-desc">${y.desc}</div>
        `;
        yogasContainer.appendChild(yCard);
    }

    // Life Predictions
    const predsContainer = document.getElementById('predictions-container');
    predsContainer.innerHTML = '';
    for (let key in data.predictions) {
        const p = data.predictions[key];
        const pCard = document.createElement('div');
        pCard.className = 'pred-display-card';
        pCard.innerHTML = `
            <div class="c-header">
                <span class="c-title">${p.title}</span>
                <span class="c-tag">Forecast</span>
            </div>
            <div class="c-desc">${p.desc}</div>
        `;
        predsContainer.appendChild(pCard);
    }

    // Remedies
    const remContainer = document.getElementById('remedies-container');
    remContainer.innerHTML = '';
    const remList = [
        { num: 1, label: data.ui.gemstone_remedy, text: `${data.remedies.moolank_gem} (Crystal: ${data.remedies.moolank_crystal})` },
        { num: 2, label: data.ui.mantra_remedy, text: data.remedies.moolank_mantra },
        { num: 3, label: data.ui.fasting_remedy, text: data.remedies.moolank_fasting },
        { num: 4, label: data.ui.donation_remedy, text: data.remedies.moolank_donation },
        { num: 5, label: data.ui.seva_remedy, text: data.remedies.moolank_seva },
        { num: 6, label: data.ui.general_remedies, text: `<strong>Health:</strong> ${data.remedies.general_health}<br><strong>Wealth & Cash Box:</strong> ${data.remedies.general_wealth}<br><strong>Harmony:</strong> ${data.remedies.general_harmony}` }
    ];

    for (let r of remList) {
        const rItem = document.createElement('div');
        rItem.className = 'remedy-display-item';
        rItem.innerHTML = `
            <div class="r-num">${r.num}</div>
            <div>
                <div class="r-label">${r.label}</div>
                <div class="r-text">${r.text}</div>
            </div>
        `;
        remContainer.appendChild(rItem);
    }
}

// Trigger Single PDF Generation
async function triggerPdfGeneration(lang) {
    const payload = getFormData();
    payload.lang = lang;
    const langNames = { en: 'English', hi: 'हिन्दी', gu: 'ગુજરાતી' };
    
    showStatus(`Generating print-ready ${langNames[lang]} PDF report via Microsoft Edge headless...`, 'loading');

    try {
        const res = await fetch('/api/generate-pdf', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const json = await res.json();
        if (!res.ok || !json.success) {
            throw new Error(json.detail || 'PDF generation failed.');
        }

        const sizeKb = Math.round(json.size / 1024);
        
        // Build WhatsApp Share Link
        const clientPhone = payload.phone.replace(/[^0-9]/g, '');
        const waMsg = `Namaste ${payload.name}, your personalized Vedic Numerology Report is prepared and certified by Jigar Thakkar (Certified Numerologist). You can download your report directly: ${window.location.origin}${json.download_url} \n\nFor consultations, contact Jigar Thakkar at +91 9377614772 / jigar93776@gmail.com.`;
        const waUrl = clientPhone 
            ? `https://api.whatsapp.com/send?phone=91${clientPhone.slice(-10)}&text=${encodeURIComponent(waMsg)}`
            : `https://api.whatsapp.com/send?text=${encodeURIComponent(waMsg)}`;

        showStatus(`
            <span>✔ ${json.lang_name} PDF Generated (${sizeKb} KB)!</span>
            <div style="display:inline-flex;gap:6px;align-items:center;">
                <a href="${json.download_url}" target="_blank" class="btn btn-gold" style="padding:4px 10px;">⬇ Download PDF</a>
                <a href="${json.html_url}" target="_blank" class="btn btn-gold" style="padding:4px 10px;">👁 View HTML</a>
                <a href="${waUrl}" target="_blank" class="btn btn-accent" style="padding:4px 10px;background:#25d366;color:#000;">📲 WhatsApp Client</a>
            </div>
        `, 'success');

        refreshHistory();
    } catch (err) {
        showStatus(`PDF Generation Error: ${err.message}`, 'error');
    }
}

// Trigger Batch PDF Generation (All 3)
async function triggerBatchPdfGeneration() {
    const payload = getFormData();
    showStatus('Generating all 3 language PDF reports (English, Hindi, Gujarati) simultaneously...', 'loading');

    try {
        const res = await fetch('/api/generate-all-pdfs', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const json = await res.json();
        if (!res.ok || !json.success) {
            throw new Error(json.detail || 'Batch generation failed.');
        }

        let linksHtml = json.reports.map(r => `
            <a href="${r.download_url}" target="_blank" class="btn btn-gold" style="display:inline-flex;margin-left:6px;padding:4px 8px;">
                ⬇ ${r.lang_name}
            </a>
        `).join('');

        showStatus(`<span>✔ All 3 Reports Successfully Generated!</span> <div>${linksHtml}</div>`, 'success');
        refreshHistory();
    } catch (err) {
        showStatus(`Batch Generation Error: ${err.message}`, 'error');
    }
}

// Refresh Session Reports History
async function refreshHistory() {
    try {
        const res = await fetch('/api/history');
        const json = await res.json();
        const listEl = document.getElementById('recent-reports-list');

        if (!json.reports || json.reports.length === 0) {
            listEl.innerHTML = '<div class="empty-state">No reports generated yet in this session.</div>';
            return;
        }

        listEl.innerHTML = json.reports.map(r => `
            <div class="report-item">
                <span class="r-name" title="${r.filename}">${r.filename}</span>
                <div class="r-links">
                    <a href="${r.download_url}" target="_blank">PDF (${r.size_kb}KB)</a>
                    <a href="${r.html_url}" target="_blank">HTML</a>
                </div>
            </div>
        `).join('');
    } catch (err) {
        console.error('Failed to load history:', err);
    }
}
