/**
 * Vedic Numerology Studio - Frontend Controller
 * Handles live calculations, trilingual UI switching, and automated PDF downloads.
 */

let currentLang = 'en';
let currentProfile = null;
let currentVibrationMode = 'period'; // 'period' (active dasha) or 'natal' (baseline)
let latestAnalysisData = null;

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', () => {
    initEventListeners();
    initCrmListeners();
    updateWeekdayDisplay();
    fetchAnalysis(false);
    refreshHistory();
});

function initEventListeners() {
    // Form submission
    const form = document.getElementById('numerology-form');
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        fetchAnalysis(true);
    });

    // Mobile View Switcher (Client Setup <-> Kundali & Reports)
    document.querySelectorAll('.mobile-nav-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const view = btn.dataset.view;
            switchMobileView(view);
        });
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
            fetchAnalysis(false);
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

// Switch between Client Setup and Kundali Dashboard on Mobile
function switchMobileView(view) {
    const sidebar = document.getElementById('panel-sidebar');
    const dashboard = document.getElementById('panel-dashboard');
    const formBtn = document.querySelector('.mobile-nav-btn[data-view="form"]');
    const dashBtn = document.querySelector('.mobile-nav-btn[data-view="dashboard"]');

    if (view === 'dashboard') {
        if (formBtn) formBtn.classList.remove('active');
        if (dashBtn) dashBtn.classList.add('active');
        if (sidebar) sidebar.classList.remove('active-mobile');
        if (dashboard) {
            dashboard.classList.add('active-mobile');
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    } else {
        if (dashBtn) dashBtn.classList.remove('active');
        if (formBtn) formBtn.classList.add('active');
        if (dashboard) dashboard.classList.remove('active-mobile');
        if (sidebar) {
            sidebar.classList.add('active-mobile');
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    }
}

// Fetch Full Calculation Analysis
async function fetchAnalysis(autoSwitch = false) {
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

        // On mobile devices, auto-switch to Kundali & Reports view when user calculates
        if (autoSwitch && window.innerWidth <= 991) {
            switchMobileView('dashboard');
        }
    } catch (err) {
        showStatus(`Error: ${err.message}`, 'error');
    }
}

// Render Complete UI Dashboard from Profile
function renderDashboard(data) {
    latestAnalysisData = data;
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

    // 3x3 Vedic Natal Grid Cells (Inborn Matrix)
    const natalGrid = data.natal_grid || grid;
    for (let cell of natalGrid.cells) {
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

    // 3x3 Vedic Dasha & Transit Grid Cells (MD • AD • PD Infusion with Multi-Color Chips)
    const dashaGrid = data.dasha_grid || natalGrid;
    for (let cell of dashaGrid.cells) {
        const el = document.getElementById(`gdc-${cell.num}`);
        if (el) {
            const wrap = el.querySelector('.chips-wrap');
            if (cell.items && cell.items.length > 0) {
                el.classList.add('active');
                wrap.innerHTML = cell.items.map(it => `<span class="chip chip-${it.source}">${it.val}</span>`).join('');
            } else {
                el.classList.remove('active');
                wrap.textContent = '-';
            }
        }
    }

    // Dynamic UI Labels & Color Legend
    if (data.color_legend) {
        if (document.getElementById('leg-natal')) document.getElementById('leg-natal').textContent = data.color_legend.natal.name;
        if (document.getElementById('leg-md')) document.getElementById('leg-md').textContent = data.color_legend.md.name;
        if (document.getElementById('leg-ad')) document.getElementById('leg-ad').textContent = data.color_legend.ad.name;
        if (document.getElementById('leg-pd')) document.getElementById('leg-pd').textContent = data.color_legend.pd.name;
    }
    if (data.ui) {
        if (document.getElementById('web-natal-grid-title')) document.getElementById('web-natal-grid-title').textContent = data.ui.natal_grid_title;
        if (document.getElementById('web-natal-grid-sub')) document.getElementById('web-natal-grid-sub').textContent = data.ui.natal_grid_sub;
        if (document.getElementById('web-dasha-grid-title')) document.getElementById('web-dasha-grid-title').textContent = data.ui.dasha_grid_title;
        if (document.getElementById('web-dasha-grid-sub')) document.getElementById('web-dasha-grid-sub').textContent = data.ui.dasha_grid_sub;
    }

    // Vibrations Breakdown (Active Dasha vs Lifetime Natal Baseline)
    renderVibrations(data, currentVibrationMode);

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

    // 3-Tier Horizon Precision Predictions
    const threeTier = data.three_tier_forecast || {};
    const md = threeTier.mahadasha || {};
    const ad = threeTier.antardasha || {};
    const pd = threeTier.pratyantar_dasha || {};

    // Tier 1: Mahadasha
    if (document.getElementById('tier-md-title')) document.getElementById('tier-md-title').textContent = md.title || `🌌 Mahadasha ${dasha.active_md.number}`;
    if (document.getElementById('tier-md-dates')) document.getElementById('tier-md-dates').textContent = `${md.start_str || dasha.active_md.start_str} to ${md.end_str || dasha.active_md.end_str} (${md.duration || ''})`;
    if (document.getElementById('tier-md-tone')) {
        const toneEl = document.getElementById('tier-md-tone');
        toneEl.textContent = md.financial_tone || 'Active';
        toneEl.className = md.financial_tone && md.financial_tone.includes('+') ? 'tone-badge text-green' : 'tone-badge text-orange';
    }
    if (document.getElementById('tier-md-desc')) document.getElementById('tier-md-desc').textContent = md.description || '';
    if (document.getElementById('tier-md-rule')) document.getElementById('tier-md-rule').innerHTML = `<strong>Vedic Principle:</strong> ${md.rule_note || ''}`;

    // Tier 2: Antardasha
    if (document.getElementById('tier-ad-title')) document.getElementById('tier-ad-title').textContent = ad.title || `📅 Antardasha ${dasha.active_ad.ad_number}`;
    if (document.getElementById('tier-ad-dates')) document.getElementById('tier-ad-dates').textContent = `${ad.start_str || dasha.active_ad.start_str} to ${ad.end_str || dasha.active_ad.end_str} (${ad.duration || '1 Year'})`;
    if (document.getElementById('tier-ad-theme')) document.getElementById('tier-ad-theme').textContent = ad.annual_theme || '';
    if (document.getElementById('tier-ad-travel')) document.getElementById('tier-ad-travel').textContent = ad.travel_forecast || 'Standard';
    if (document.getElementById('tier-ad-assets')) document.getElementById('tier-ad-assets').textContent = ad.asset_forecast || 'Standard';

    // Tier 3: Pratyantar Dasha
    if (document.getElementById('tier-pd-title')) document.getElementById('tier-pd-title').textContent = pd.title || `🌙 Pratyantar Dasha ${dasha.active_pd.number}`;
    if (document.getElementById('tier-pd-dates')) document.getElementById('tier-pd-dates').textContent = `${pd.start_str || dasha.active_pd.start_str} to ${pd.end_str || dasha.active_pd.end_str} (${pd.duration_days || ''} Days)`;
    
    const pdDosList = document.getElementById('tier-pd-dos');
    if (pdDosList && pd.dos) {
        pdDosList.innerHTML = pd.dos.map(d => `<li>${d}</li>`).join('');
    }
    const pdDontsList = document.getElementById('tier-pd-donts');
    if (pdDontsList && pd.donts) {
        pdDontsList.innerHTML = pd.donts.map(d => `<li>${d}</li>`).join('');
    }

    // 9-Phase Pratyantar Dasha Calendar Table
    const pdBody = document.getElementById('pd-roadmap-body');
    if (pdBody && threeTier.pd_roadmap) {
        pdBody.innerHTML = '';
        for (let r of threeTier.pd_roadmap) {
            const tr = document.createElement('tr');
            if (r.is_active) tr.className = 'active-phase';
            const badgeClass = r.is_active ? 'status-chip active' : 'status-chip';
            const badgeTxt = r.is_active ? '★ CURRENT' : r.tone;
            tr.innerHTML = `
                <td style="font-weight:700;">Phase ${r.phase} (${r.planet})</td>
                <td style="text-align:center;"><strong>No. ${r.number}</strong></td>
                <td style="text-align:center;">${r.duration_days} Days</td>
                <td style="text-align:center;">${r.start_str}</td>
                <td style="text-align:center;">${r.end_str}</td>
                <td style="text-align:center;"><span class="${badgeClass}">${badgeTxt}</span></td>
            `;
            pdBody.appendChild(tr);
        }
    }

    // Lifetime Mahadasha 45-Year Cyclic Table

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

    // Auspicious Yogas & Challenging Doshas
    const ausContainer = document.getElementById('auspicious-yogas-container');
    const inausContainer = document.getElementById('inauspicious-yogas-container');
    const yogasContainer = document.getElementById('yogas-container');

    const auspiciousList = data.auspicious_yogas || (data.yogas ? data.yogas.filter(y => y.category !== 'inauspicious') : []);
    const inauspiciousList = data.inauspicious_yogas || (data.yogas ? data.yogas.filter(y => y.category === 'inauspicious') : []);

    // Localized Headers for Tab 3
    if (data.ui) {
        if (document.getElementById('txt-auspicious-title') && data.ui.auspicious_yogas_title) {
            document.getElementById('txt-auspicious-title').textContent = data.ui.auspicious_yogas_title;
        }
        if (document.getElementById('txt-inauspicious-title') && data.ui.inauspicious_yogas_title) {
            document.getElementById('txt-inauspicious-title').textContent = data.ui.inauspicious_yogas_title;
        }
    }

    if (ausContainer) {
        ausContainer.innerHTML = '';
        for (let y of auspiciousList) {
            const yCard = document.createElement('div');
            const isRaj = y.id === 'raj_yog';
            yCard.className = `yoga-display-card auspicious ${isRaj ? 'raj-yog' : ''}`;
            yCard.innerHTML = `
                <div class="c-header">
                    <span class="c-title">✦ ${y.name}</span>
                    <span class="c-tag">${y.tag}</span>
                </div>
                <div class="c-desc">${y.desc}</div>
            `;
            ausContainer.appendChild(yCard);
        }
    }

    if (inausContainer) {
        inausContainer.innerHTML = '';
        if (inauspiciousList && inauspiciousList.length > 0) {
            for (let y of inauspiciousList) {
                const yCard = document.createElement('div');
                yCard.className = 'yoga-display-card inauspicious';
                const remedyLabel = (data.ui && data.ui.mitigation_remedy) ? data.ui.mitigation_remedy : 'Remedial Mitigation Key:';
                const remedyHtml = y.remedy ? `
                    <div class="yoga-remedy-box">
                        <strong>🛡️ ${remedyLabel}</strong> ${y.remedy}
                    </div>
                ` : '';
                yCard.innerHTML = `
                    <div class="c-header">
                        <span class="c-title" style="color: #f87171;">⚠ ${y.name}</span>
                        <span class="c-tag yoga-tag-mini ruby">${y.tag}</span>
                    </div>
                    <div class="c-desc">${y.desc}</div>
                    ${remedyHtml}
                `;
                inausContainer.appendChild(yCard);
            }
        } else {
            const noDoshaBanner = document.createElement('div');
            noDoshaBanner.className = 'no-dosha-banner';
            const msg = (data.client && data.client.lang === 'hi')
                ? '✔ जन्म चक्र में कोई प्रतिकूल ग्रहीय दोष सक्रिय नहीं है। ग्रह ऊर्जा पूर्णतः शांत एवं अनुकूल बनी हुई है।'
                : ((data.client && data.client.lang === 'gu')
                    ? '✔ જન્મ કુંડળીમાં કોઈ પ્રતિકૂળ ગ્રહીય દોષ સક્રિય નથી. ગ્રહ ઉર્જા પૂર્ણપણે શાંત અને અનુકૂળ રહે છે.'
                    : '✔ No Adverse Karmic Doshas Active in Chart • The planetary frequencies remain protected by divine harmony.');
            noDoshaBanner.innerHTML = msg;
            inausContainer.appendChild(noDoshaBanner);
        }
    }

    if (yogasContainer) {
        yogasContainer.innerHTML = '';
        for (let y of (data.yogas || [])) {
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

// Switch between Active Dasha Period Vibrations and Lifetime Natal Baseline
function switchVibrationView(mode) {
    currentVibrationMode = mode;
    const btnPeriod = document.getElementById('btn-vibe-period');
    const btnNatal = document.getElementById('btn-vibe-natal');
    if (btnPeriod && btnNatal) {
        if (mode === 'period') {
            btnPeriod.classList.add('active');
            btnNatal.classList.remove('active');
        } else {
            btnPeriod.classList.remove('active');
            btnNatal.classList.add('active');
        }
    }
    if (latestAnalysisData) {
        renderVibrations(latestAnalysisData, mode);
    }
}

// Render Vibrations Breakdown List with Dynamic Dasha Shift Indicators
function renderVibrations(data, mode = 'period') {
    const vibContainer = document.getElementById('vibrations-list');
    const disclaimerBanner = document.getElementById('vibrations-disclaimer-banner');
    if (!vibContainer) return;

    const list = (mode === 'period')
        ? (data.period_vibrations || data.vibrations || [])
        : (data.natal_vibrations || []);

    if (disclaimerBanner) {
        if (mode === 'period') {
            const shiftInfo = data.vibration_shifts || {};
            const discText = shiftInfo.disclaimer || (data.ui && data.ui.vibrations_disclaimer) ||
                'Vedic vibrations dynamically fluctuate across Dasha cycles. During this queried active period, numbers shift counts and signs (+/-). These are cyclical planetary activations, not permanent lifetime curses.';
            disclaimerBanner.innerHTML = `<strong>★ Active Dasha Dynamic Vibrations:</strong> ${discText}`;
            disclaimerBanner.style.display = 'block';
        } else {
            disclaimerBanner.innerHTML = `<strong>👑 Lifetime Inborn Matrix (Baseline):</strong> Permanent karmic baseline frequencies inherited from the exact date of birth prior to cyclical Dasha period activations.`;
            disclaimerBanner.style.display = 'block';
        }
    }

    vibContainer.innerHTML = '';
    for (let v of list) {
        const box = document.createElement('div');
        box.className = `vibe-box ${v.type === '+' ? 'badge-pos' : 'badge-neg'}`;

        let shiftBadgeHtml = '';
        if (mode === 'period' && v.shifted) {
            let pillCls = 'pill-dasha-active';
            let pillIcon = '⚡';
            if (v.shift_type === 'neg_to_pos') {
                pillCls = 'pill-transformed-pos';
                pillIcon = '★';
            } else if (v.shift_type === 'pos_to_neg') {
                pillCls = 'pill-shifted-neg';
                pillIcon = '⚠';
            }
            shiftBadgeHtml = `<div class="vibe-shift-pill ${pillCls}">${pillIcon} ${v.shift_label || 'Active Dasha Shift'}</div>`;
        }

        box.innerHTML = `
            <div class="vibe-box-header">
                <div class="vibe-box-title">
                    <span>Number ${v.number} (${v.count}x)</span>
                </div>
                <span class="vibe-tag">${v.type_label}</span>
            </div>
            ${shiftBadgeHtml}
            <div class="vibe-desc">${v.text}</div>
        `;
        vibContainer.appendChild(box);
    }
}

/* ==========================================================================
   Studio CRM & Customer Database Controller
   ========================================================================== */

let crmSearchTimeout = null;

function initCrmListeners() {
    const tabCrmBtn = document.getElementById('tab-btn-crm');
    if (tabCrmBtn) {
        tabCrmBtn.addEventListener('click', () => {
            loadCrmOrders();
        });
    }

    const refreshBtn = document.getElementById('btn-crm-refresh');
    if (refreshBtn) {
        refreshBtn.addEventListener('click', loadCrmOrders);
    }

    const searchInput = document.getElementById('crm-search-input');
    if (searchInput) {
        searchInput.addEventListener('input', () => {
            clearTimeout(crmSearchTimeout);
            crmSearchTimeout = setTimeout(loadCrmOrders, 350);
        });
    }

    const tierFilter = document.getElementById('crm-tier-filter');
    if (tierFilter) {
        tierFilter.addEventListener('change', loadCrmOrders);
    }
}

async function loadCrmOrders() {
    const tbody = document.getElementById('crm-orders-tbody');
    if (!tbody) return;

    const searchVal = document.getElementById('crm-search-input') ? document.getElementById('crm-search-input').value.trim() : '';
    const tierVal = document.getElementById('crm-tier-filter') ? document.getElementById('crm-tier-filter').value : 'all';

    try {
        const query = new URLSearchParams({
            search: searchVal,
            tier: tierVal,
            limit: 100,
            offset: 0
        });

        const res = await fetch(`/api/studio/orders?${query.toString()}`);
        if (!res.ok) throw new Error('Failed to load CRM data');

        const data = await res.json();
        renderCrmStats(data.stats);
        renderCrmTable(data.orders);
    } catch (err) {
        console.error('[CRM Load Error]', err);
        tbody.innerHTML = `<tr><td colspan="7" style="text-align: center; color: #f87171; padding: 20px;">Error loading orders: ${err.message}</td></tr>`;
    }
}

function renderCrmStats(stats) {
    if (!stats) return;

    const elRev = document.getElementById('crm-total-revenue');
    const elOrders = document.getElementById('crm-total-orders');
    const el299 = document.getElementById('crm-cnt-299');
    const el499 = document.getElementById('crm-cnt-499');
    const el1199 = document.getElementById('crm-cnt-1199');
    const elPending = document.getElementById('crm-pending-meetings');

    if (elRev) elRev.textContent = `₹${(stats.total_revenue || 0).toLocaleString('en-IN')}`;
    if (elOrders) elOrders.textContent = stats.total_orders || 0;
    if (el299) el299.textContent = (stats.tier_counts && stats.tier_counts.essential_299) || 0;
    if (el499) el499.textContent = (stats.tier_counts && stats.tier_counts.complete_499) || 0;
    if (el1199) el1199.textContent = (stats.tier_counts && stats.tier_counts.vip_1199) || 0;
    if (elPending) elPending.textContent = stats.pending_meetings || 0;
}

function escapeHtml(str) {
    if (!str) return '';
    return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
}

function renderCrmTable(orders) {
    const tbody = document.getElementById('crm-orders-tbody');
    if (!tbody) return;

    if (!orders || orders.length === 0) {
        tbody.innerHTML = `<tr><td colspan="7" style="text-align: center; padding: 30px; color: var(--text-secondary);">No customer orders found matching your search.</td></tr>`;
        return;
    }

    const tierBadges = {
        'test_1': '<span class="tier-tag" style="background:rgba(34,197,94,0.2);color:#4ade80;border:1px solid rgba(34,197,94,0.4);">🧪 Trial (₹1)</span>',
        'essential_299': '<span class="tier-tag tier-tag-essential">Essential (₹299)</span>',
        'complete_499': '<span class="tier-tag tier-tag-complete">Complete (₹499)</span>',
        'vip_1199': '<span class="tier-tag tier-tag-vip">👑 VIP 1-on-1 (₹1,199)</span>'
    };

    let html = '';
    orders.forEach(order => {
        const dateStr = order.created_at ? order.created_at.replace('T', ' ').substring(0, 16) : 'Recently';
        const rawPhone = (order.phone || '').replace(/[^0-9]/g, '');
        const cleanPhone = rawPhone.length === 10 ? `91${rawPhone}` : rawPhone;

        // Pre-composed WhatsApp Client Message
        let waMsg = '';
        if (order.tier === 'vip_1199') {
            waMsg = `Namaste ${order.client_name} ji! This is Jigar Thakkar (Certified Vedic Numerologist). Thank you for booking the VIP 1-on-1 Personal Consultation package. When is a convenient date and time for our personalized online meeting?`;
        } else {
            waMsg = `Namaste ${order.client_name} ji! This is Jigar Thakkar (Certified Vedic Numerologist). Thank you for ordering your Vedic Numerology Blueprint. Hope your 10-page report was insightful! Feel free to connect if you need any clarity.`;
        }
        const waLink = cleanPhone ? `https://wa.me/${cleanPhone}?text=${encodeURIComponent(waMsg)}` : '#';

        // VIP Status Selector
        let vipCell = '';
        if (order.tier === 'vip_1199') {
            vipCell = `
                <select class="status-select-sm" onchange="updateMeetingStatus('${order.id}', this.value)" style="${order.meeting_status === 'pending' ? 'border-color: #ef4444; color: #fca5a5;' : (order.meeting_status === 'completed' ? 'border-color: #22c55e; color: #86efac;' : '')}">
                    <option value="pending" ${order.meeting_status === 'pending' ? 'selected' : ''}>⏳ Pending</option>
                    <option value="scheduled" ${order.meeting_status === 'scheduled' ? 'selected' : ''}>📅 Scheduled</option>
                    <option value="completed" ${order.meeting_status === 'completed' ? 'selected' : ''}>✔ Completed</option>
                </select>
            `;
        } else {
            vipCell = `<span style="color: #64748b; font-size: 11px;">N/A</span>`;
        }

        const pdfFilename = order.pdf_filename || '';
        const htmlFilename = pdfFilename.replace('.pdf', '.html');

        html += `
            <tr>
                <td>
                    <div style="font-weight: 600; color: #f1f5f9;">${dateStr}</div>
                    <div style="font-size: 10.5px; color: #64748b; font-family: monospace;">${order.order_id || 'ID: #' + order.id}</div>
                </td>
                <td>
                    <div style="font-weight: 700; color: #fbbf24;">${escapeHtml(order.client_name)}</div>
                    <div style="font-size: 11px; color: var(--text-secondary);">DOB: ${order.dob} (${order.gender || 'M'}) • ${order.lang ? order.lang.toUpperCase() : 'EN'}</div>
                </td>
                <td>
                    <div><a href="tel:${order.phone}" style="color: #93c5fd; text-decoration: none;">📞 ${order.phone || 'N/A'}</a></div>
                    <div style="font-size: 11px; color: #64748b;">${order.email || ''}</div>
                </td>
                <td>
                    ${tierBadges[order.tier] || `<span class="tier-tag">${order.tier}</span>`}
                </td>
                <td>
                    <strong style="color: #4ade80; font-size: 13px;">₹${order.amount || 499}</strong>
                </td>
                <td>
                    ${vipCell}
                </td>
                <td>
                    <div style="display: flex; gap: 4px; flex-wrap: wrap;">
                        ${pdfFilename ? `<a href="/api/download/${encodeURIComponent(pdfFilename)}" class="crm-btn-sm crm-btn-pdf" title="Download 10-Page PDF">📥 PDF</a>` : ''}
                        ${pdfFilename ? `<a href="/api/view-html/${encodeURIComponent(htmlFilename)}" target="_blank" class="crm-btn-sm crm-btn-view" title="View in Browser">👁️</a>` : ''}
                        ${cleanPhone ? `<a href="${waLink}" target="_blank" class="crm-btn-sm crm-btn-wa" title="Message Client on WhatsApp">💬 WA</a>` : ''}
                    </div>
                </td>
            </tr>
        `;
    });

    tbody.innerHTML = html;
}

async function updateMeetingStatus(orderId, status) {
    try {
        const res = await fetch('/api/studio/update-meeting', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ order_id: orderId, status: status })
        });
        if (res.ok) {
            showStatus('VIP meeting status updated', 'success');
            loadCrmOrders();
        } else {
            alert('Could not update meeting status.');
        }
    } catch (e) {
        console.error(e);
        alert('Network error updating meeting status.');
    }
}
