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
    initMatchMakingListeners();
    initBusinessPartnershipListeners();
    initNameAndMobileListeners();
    initSavedClientsListeners();
    initBabyNamesListeners();
    initPropertyVehicleListeners();
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
        const tw = p.timing_windows;
        let timingBlock = '';
        if (tw) {
            const chip = (txt) => `<span style="display:inline-block;padding:2px 8px;margin:2px 4px 2px 0;border-radius:5px;background:rgba(255,255,255,0.06);border:1px solid rgba(234,179,8,0.28);font-size:11px;color:#f1f5f9;">${escapeHtml(txt)}</span>`;
            const noteTag = tw.note ? `<span style="font-size:10.5px;font-weight:700;color:#fca5a5;margin-left:6px;">(${escapeHtml(tw.note)})</span>` : '';
            timingBlock = `
            <div style="margin-top:10px;padding:10px 12px;border-radius:8px;background:rgba(15,23,42,0.65);border:1px solid rgba(234,179,8,0.22);font-size:11.5px;">
                <div style="font-weight:700;color:#fde68a;margin-bottom:6px;">📅 Activation Timing Windows ${noteTag}</div>
                <div style="margin-bottom:5px;"><span style="color:#94a3b8;font-weight:600;display:block;font-size:10.5px;margin-bottom:2px;">${escapeHtml(tw.pd_label)}:</span>${(tw.pratyantar || []).map(chip).join('')}</div>
                <div style="margin-bottom:5px;"><span style="color:#94a3b8;font-weight:600;display:block;font-size:10.5px;margin-bottom:2px;">${escapeHtml(tw.ad_label)}:</span>${(tw.antardasha_years || []).map(chip).join('')}</div>
                <div><span style="color:#94a3b8;font-weight:600;display:block;font-size:10.5px;margin-bottom:2px;">${escapeHtml(tw.md_label)}:</span>${(tw.mahadasha || []).map(chip).join('')}</div>
            </div>`;
        } else if (p.timing) {
            timingBlock = `<div style="margin-top:8px;padding:7px 10px;border-radius:6px;background:rgba(234,179,8,0.09);border:1px solid rgba(234,179,8,0.28);font-size:11.5px;color:#fde68a;line-height:1.4;">${escapeHtml(p.timing)}</div>`;
        }
        pCard.innerHTML = `
            <div class="c-header">
                <span class="c-title">${p.title}</span>
                <span class="c-tag">Forecast</span>
            </div>
            <div class="c-desc">${p.desc}</div>
            ${timingBlock}
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

// ==========================================
// Match Making Report (5-Pillar Vedic Method)
// ==========================================
function initMatchMakingListeners() {
    const analyzeBtn = document.getElementById('btn-mm-analyze');
    if (analyzeBtn) {
        analyzeBtn.addEventListener('click', runMatchMakingAnalysis);
    }
    document.querySelectorAll('.mm-pdf-btn').forEach(btn => {
        btn.addEventListener('click', () => downloadMatchMakingPdf(btn.dataset.lang || 'en'));
    });
    const mmLangSel = document.getElementById('mm-lang');
    if (mmLangSel) {
        mmLangSel.addEventListener('change', () => {
            if (document.getElementById('mm-results-container')?.innerHTML) {
                runMatchMakingAnalysis();
            }
        });
    }
}

function getMatchMakingPayload(overrideLang) {
    return {
        boy_name: (document.getElementById('mm-boy-name')?.value || '').trim(),
        boy_dob: document.getElementById('mm-boy-dob')?.value || '',
        girl_name: (document.getElementById('mm-girl-name')?.value || '').trim(),
        girl_dob: document.getElementById('mm-girl-dob')?.value || '',
        lang: overrideLang || document.getElementById('mm-lang')?.value || 'en'
    };
}

async function runMatchMakingAnalysis() {
    const payload = getMatchMakingPayload();
    if (!payload.boy_name || !payload.boy_dob || !payload.girl_name || !payload.girl_dob) {
        showStatus('Please enter both names and dates of birth for Match Making.', 'error');
        return;
    }
    showStatus('Computing 5-Pillar Match Making compatibility...', 'loading');
    try {
        const res = await fetch('/api/matchmaking/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        const json = await res.json();
        if (!res.ok || !json.success) {
            throw new Error(json.detail || 'Match making analysis failed');
        }
        renderMatchMakingResults(json.data);
        hideStatus();
    } catch (err) {
        showStatus(`Match Making error: ${err.message}`, 'error');
    }
}

async function downloadMatchMakingPdf(langOverride) {
    const payload = getMatchMakingPayload(langOverride);
    if (!payload.boy_name || !payload.boy_dob || !payload.girl_name || !payload.girl_dob) {
        showStatus('Please enter both names and dates of birth first.', 'error');
        return;
    }
    const langLabel = payload.lang === 'hi' ? 'Hindi' : (payload.lang === 'gu' ? 'Gujarati' : 'English');
    showStatus(`Generating ${langLabel} Match Making PDF...`, 'loading');
    try {
        const res = await fetch('/api/matchmaking/generate-pdf', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        const json = await res.json();
        if (!res.ok || !json.success) {
            throw new Error(json.detail || 'PDF generation failed');
        }
        if (json.data) renderMatchMakingResults(json.data);
        showStatus(`Match Making PDF ready! <a href="${json.download_url}" target="_blank" style="color:#fbbf24;text-decoration:underline;margin-left:8px;">Download PDF ↗</a>`, 'success');
        window.open(json.download_url, '_blank');
    } catch (err) {
        showStatus(`Match Making PDF error: ${err.message}`, 'error');
    }
}

function renderMatchMakingResults(m) {
    const container = document.getElementById('mm-results-container');
    if (!container) return;

    const bannerGrad = m.verdict_level === 'good'
        ? 'linear-gradient(90deg, #059669, #10b981)'
        : (m.verdict_level === 'moderate'
            ? 'linear-gradient(90deg, #d97706, #f59e0b)'
            : 'linear-gradient(90deg, #991b1b, #db2777)');

    const renderMiniGrid = (grid) => {
        const cells = (grid.cells || []).map(c =>
            `<div style="border:1px solid rgba(212,175,55,0.4);padding:4px;text-align:center;min-height:36px;">
                <div style="font-size:9px;color:#d4af37;">${c.num}</div>
                <div style="font-weight:700;font-size:13px;">${c.count > 0 ? c.str : ''}</div>
            </div>`
        ).join('');
        return `<div style="display:grid;grid-template-columns:repeat(3,1fr);border:1.5px solid #d4af37;border-radius:4px;width:135px;flex-shrink:0;">${cells}</div>`;
    };

    const renderPerson = (p, role) => {
        const pills = (p.vibrations || []).map(v => {
            const bg = v.type === '+' ? 'rgba(34,197,94,0.2)' : 'rgba(239,68,68,0.2)';
            const fg = v.type === '+' ? '#4ade80' : '#f87171';
            const sign = v.type === '+' ? '+' : '−';
            return `<span style="background:${bg};color:${fg};padding:1px 6px;border-radius:999px;font-size:11px;font-weight:700;margin-right:4px;">${sign}${v.number}</span>`;
        }).join('');
        return `
        <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.1);border-radius:10px;padding:12px;">
            <div style="font-size:11px;color:#a78bfa;font-style:italic;">${role}</div>
            <div style="font-size:16px;font-weight:700;margin-bottom:2px;">${p.name}</div>
            <div style="font-size:11px;color:var(--text-secondary);margin-bottom:10px;">Born ${p.dob} · age ${p.age}</div>
            <div style="display:flex;gap:12px;align-items:flex-start;">
                ${renderMiniGrid(p.grid)}
                <div style="font-size:12px;">
                    <div><strong>Basic ${p.bn}</strong> · ${p.bn_planet}</div>
                    <div style="margin-top:4px;"><strong>Destiny ${p.dn}</strong> · ${p.dn_planet}</div>
                    <div style="margin-top:8px;">${pills}</div>
                </div>
            </div>
        </div>`;
    };

    const pillarsHtml = (m.pillars || []).map(p => {
        const pct = Math.round((p.score / p.max) * 100);
        const barCol = p.score >= 15 ? '#22c55e' : (p.score >= 10 ? '#f59e0b' : '#475569');
        return `
        <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:8px;padding:10px 12px;margin-bottom:8px;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">
                <strong style="font-size:13px;">${p.title}</strong>
                <strong style="font-size:14px;color:${p.score >= 15 ? '#4ade80' : '#fbbf24'};">${p.score}/${p.max}</strong>
            </div>
            <div style="height:6px;background:rgba(255,255,255,0.1);border-radius:999px;overflow:hidden;margin-bottom:5px;">
                <div style="width:${pct}%;height:100%;background:${barCol};"></div>
            </div>
            <div style="font-size:11.5px;color:var(--text-secondary);">${p.desc}</div>
        </div>`;
    }).join('');

    const renderRuleCard = (rc) => {
        const isRejSec = rc.category === 'rejection';
        const bg = isRejSec
            ? (rc.status === 'reject' ? '#b91c1c' : '#991b1b')
            : (rc.status === 'ok' ? '#15803d' : (rc.status === 'reject' ? '#b91c1c' : '#d97706'));
        const boxBorder = isRejSec
            ? (rc.status === 'reject' ? 'rgba(239,68,68,0.65)' : 'rgba(239,68,68,0.35)')
            : (rc.status === 'ok' ? 'rgba(34,197,94,0.35)' : (rc.status === 'reject' ? 'rgba(239,68,68,0.45)' : 'rgba(245,158,11,0.4)'));
        const boxBg = isRejSec
            ? (rc.status === 'reject' ? 'rgba(239,68,68,0.16)' : 'rgba(239,68,68,0.06)')
            : (rc.status === 'ok' ? 'rgba(34,197,94,0.08)' : (rc.status === 'reject' ? 'rgba(239,68,68,0.10)' : 'rgba(245,158,11,0.08)'));
        const icon = rc.status === 'ok' ? '✓' : (rc.status === 'reject' ? '✕' : '!');
        const stLbl = isRejSec
            ? (rc.status === 'reject' ? 'Rejected' : 'Clear (No Rejection)')
            : (rc.status === 'ok' ? 'Matched' : (rc.status === 'reject' ? 'Rejected' : 'Caution'));
        return `
        <div style="display:flex;gap:10px;align-items:flex-start;margin-bottom:8px;padding:10px 12px;border-radius:8px;border:1px solid ${boxBorder};background:${boxBg};">
            <span style="width:20px;height:20px;border-radius:50%;background:${bg};color:#fff;font-weight:700;font-size:11px;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px;">${icon}</span>
            <div style="font-size:12px;flex:1;">
                <div style="display:flex;justify-content:space-between;align-items:center;gap:8px;">
                    <strong>${rc.rule} · ${rc.title}</strong>
                    <span style="font-size:10.5px;font-weight:700;padding:2px 8px;border-radius:999px;background:${bg};color:#fff;">${stLbl}</span>
                </div>
                <div style="color:var(--text-secondary);font-size:11.5px;margin-top:2px;">${rc.detail}</div>
                ${rc.why_important ? `<div style="font-size:11.5px;color:#cbd5e1;margin-top:4px;"><strong>Why Important:</strong> ${rc.why_important}</div>` : ''}
                ${rc.couple_effect ? `<div style="font-size:11.5px;color:#f1f5f9;margin-top:2px;"><strong>Effect on Couple:</strong> ${rc.couple_effect}</div>` : ''}
            </div>
        </div>`;
    };
    const matchingRulesHtml = (m.rules_checks || []).filter(rc => rc.category !== 'rejection').map(renderRuleCard).join('');
    const rejectionRulesHtml = (m.rules_checks || []).filter(rc => rc.category === 'rejection').map(renderRuleCard).join('');

    const lit = m.litigation_check || {};
    const litWarns = [];
    if (lit.boy && lit.boy.risk) litWarns.push(`${lit.boy.name}: ${lit.boy.years.join(', ')}`);
    if (lit.girl && lit.girl.risk) litWarns.push(`${lit.girl.name}: ${lit.girl.years.join(', ')}`);
    const litHtml = litWarns.length
        ? `<div style="background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.4);border-radius:8px;padding:8px 12px;font-size:12px;color:#fca5a5;margin-top:8px;"><strong>⚠️ 5-Year Litigation Check:</strong> Litigation triggers active for 2+ years (${litWarns.join(' | ')}).</div>`
        : `<div style="background:rgba(34,197,94,0.12);border:1px solid rgba(34,197,94,0.3);border-radius:8px;padding:8px 12px;font-size:12px;color:#86efac;margin-top:8px;"><strong>✓ 5-Year Litigation Check:</strong> No 2+ year litigation activation detected in the next 5 years.</div>`;

    container.innerHTML = `
        <div style="background:${bannerGrad};color:#fff;border-radius:12px;padding:16px 20px;display:flex;align-items:center;gap:18px;margin-bottom:14px;">
            <div style="font-size:32px;font-weight:800;line-height:1;">${m.total_score}<span style="font-size:15px;opacity:0.85;">/100</span></div>
            <div>
                <div style="font-size:17px;font-weight:700;">${m.verdict}</div>
                <div style="font-size:12.5px;opacity:0.92;">${m.verdict_sub}</div>
            </div>
        </div>
        <div class="resp-grid-2" style="margin-bottom:14px;">
            ${renderPerson(m.boy, 'Boy · Groom')}
            ${renderPerson(m.girl, 'Girl · Bride')}
        </div>
        <div style="margin-bottom:12px;">
            <h4 style="margin:0 0 8px 0;color:#fbbf24;">The Five Pillars (100 Points)</h4>
            ${pillarsHtml}
        </div>
        <div style="background:rgba(34,197,94,0.05);border:1px solid rgba(34,197,94,0.3);border-radius:10px;padding:12px;margin-bottom:12px;">
            <h4 style="margin:0 0 8px 0;color:#4ade80;">✓ Basic Matching Rules (Compatibility &amp; Support)</h4>
            ${matchingRulesHtml}
        </div>
        <div style="background:rgba(239,68,68,0.06);border:1px solid rgba(239,68,68,0.35);border-radius:10px;padding:12px;">
            <h4 style="margin:0 0 8px 0;color:#f87171;">⛔ Basic Rejection Rules &amp; Red-Flag Checks</h4>
            ${rejectionRulesHtml}
            ${litHtml}
        </div>
    `;
}

// ==========================================
// Name Suggestion & Mobile Matching Tabs
// ==========================================
function initNameAndMobileListeners() {
    const nmBtn = document.getElementById('btn-nm-analyze');
    const mobBtn = document.getElementById('btn-mob-analyze');
    if (nmBtn) nmBtn.addEventListener('click', runNameAnalysis);
    if (mobBtn) mobBtn.addEventListener('click', runMobileAnalysis);
    document.querySelectorAll('.nm-pdf-btn').forEach(btn => {
        btn.addEventListener('click', () => downloadNamePdf(btn.dataset.lang || 'en'));
    });
    document.querySelectorAll('.mob-pdf-btn').forEach(btn => {
        btn.addEventListener('click', () => downloadMobilePdf(btn.dataset.lang || 'en'));
    });
}

async function downloadNamePdf(lang = 'en') {
    const name = (document.getElementById('nm-name')?.value || '').trim();
    const dob = document.getElementById('nm-dob')?.value || '';
    const gender = document.getElementById('nm-gender')?.value || 'Male';
    const alpha = (document.getElementById('nm-alpha')?.value || '').trim();
    if (!name || !dob) {
        showStatus('Please enter both Full Name and Date of Birth first.', 'error');
        return;
    }
    const langLabel = lang === 'hi' ? 'Hindi' : (lang === 'gu' ? 'Gujarati' : 'English');
    showStatus(`Generating ${langLabel} Name Correction PDF...`, 'loading');
    try {
        const res = await fetch('/api/studio/name-generate-pdf', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, dob, alpha, gender, lang })
        });
        const json = await res.json();
        if (!res.ok || !json.success) throw new Error(json.detail || 'PDF generation failed');
        if (json.data) renderNameResults(json.data);
        showStatus(`Name Correction PDF ready! <a href="${json.download_url}" target="_blank" style="color:#fbbf24;text-decoration:underline;margin-left:8px;">⬇ Download PDF ↗</a> <a href="${json.html_url}" target="_blank" style="color:#93c5fd;text-decoration:underline;margin-left:8px;">👁 View HTML</a>`, 'success');
        window.open(json.download_url, '_blank');
    } catch (err) {
        showStatus(`Name PDF error: ${err.message}`, 'error');
    }
}

async function downloadMobilePdf(lang = 'en') {
    const mobile = (document.getElementById('mob-number')?.value || '').trim();
    const compare_mobile = (document.getElementById('mob-compare')?.value || '').trim();
    const dob = document.getElementById('mob-dob')?.value || '';
    if (!mobile || !dob) {
        showStatus('Please enter Mobile Number and Date of Birth first.', 'error');
        return;
    }
    const langLabel = lang === 'hi' ? 'Hindi' : (lang === 'gu' ? 'Gujarati' : 'English');
    showStatus(`Generating ${langLabel} Mobile & DOB PDF...`, 'loading');
    try {
        const res = await fetch('/api/studio/mobile-generate-pdf', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ mobile, dob, compare_mobile, lang })
        });
        const json = await res.json();
        if (!res.ok || !json.success) throw new Error(json.detail || 'PDF generation failed');
        if (json.data) renderMobileResults(json.data);
        showStatus(`Mobile & DOB PDF ready! <a href="${json.download_url}" target="_blank" style="color:#fbbf24;text-decoration:underline;margin-left:8px;">⬇ Download PDF ↗</a> <a href="${json.html_url}" target="_blank" style="color:#93c5fd;text-decoration:underline;margin-left:8px;">👁 View HTML</a>`, 'success');
        window.open(json.download_url, '_blank');
    } catch (err) {
        showStatus(`Mobile PDF error: ${err.message}`, 'error');
    }
}

async function runNameAnalysis() {
    const name = (document.getElementById('nm-name')?.value || '').trim();
    const dob = document.getElementById('nm-dob')?.value || '';
    const gender = document.getElementById('nm-gender')?.value || 'Male';
    const alpha = (document.getElementById('nm-alpha')?.value || '').trim();
    if (!name || !dob) {
        showStatus('Please enter both Full Name and Date of Birth.', 'error');
        return;
    }
    showStatus('Analyzing Chaldean name vibrations & generating suggestions...', 'loading');
    try {
        const res = await fetch('/api/studio/name-suggest', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, dob, alpha, gender })
        });
        const json = await res.json();
        if (!res.ok || !json.success) throw new Error(json.detail || 'Name analysis failed');
        renderNameResults(json.data);
        hideStatus();
    } catch (err) {
        showStatus(`Name analysis error: ${err.message}`, 'error');
    }
}

function renderNameResults(d) {
    const el = document.getElementById('nm-results-container');
    if (!el) return;
    const cur = d.current;
    const chips = (cur.breakdown || []).map(b =>
        `<span style="display:inline-flex;flex-direction:column;align-items:center;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);border-radius:6px;padding:3px 7px;margin:2px;">
            <strong style="font-size:12px;">${b.ch}</strong>
            <span style="font-size:10px;color:#fbbf24;">${b.val}</span>
        </span>`
    ).join('');

    const spellRows = (d.spelling_suggestions || []).map(s => `
        <tr>
            <td><strong>${s.name}</strong></td>
            <td>${s.compound} → <strong style="color:#38bdf8;">${s.namank}</strong></td>
            <td style="color:var(--text-secondary);font-size:12px;">${s.change_note}</td>
            <td><span style="background:rgba(34,197,94,0.18);color:#4ade80;padding:2px 8px;border-radius:999px;font-size:11px;font-weight:700;">${s.is_best ? 'Best Match' : 'Harmonious'}</span></td>
        </tr>`).join('') || '<tr><td colspan="4" style="color:var(--text-secondary);">No minor spelling tweaks needed or found.</td></tr>';

    const alphaCards = (d.alphabet_suggestions || []).map(a => `
        <div style="background:rgba(255,255,255,0.04);border:1px solid rgba(56,189,248,0.25);border-radius:8px;padding:8px 10px;">
            <div style="font-weight:700;font-size:13.5px;">${a.name}</div>
            <div style="font-size:11.5px;color:#fbbf24;">Total ${a.compound} → Namank ${a.namank} ${a.is_best ? '★ Best' : ''}</div>
        </div>`).join('') || '<div style="color:var(--text-secondary);font-size:12px;">No matching curated names found for that alphabet.</div>';

    el.innerHTML = `
        <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.12);border-radius:10px;padding:14px;margin-bottom:14px;">
            <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px;margin-bottom:8px;">
                <div>
                    <div style="font-size:12px;color:#38bdf8;">Current Name Vibration</div>
                    <div style="font-size:18px;font-weight:700;">${cur.name} — Compound <strong>${cur.compound}</strong> → Namank <strong style="color:#fbbf24;">${cur.namank}</strong></div>
                </div>
                <div style="font-size:12px;color:var(--text-secondary);">DOB ${d.dob} · BN <strong>${d.bn}</strong> · DN <strong>${d.dn}</strong> · Target Best: <strong style="color:#4ade80;">${d.best_targets.join(', ')}</strong></div>
            </div>
            <div style="margin-bottom:8px;">${chips}</div>
            <div style="font-size:12.5px;color:${cur.harmony.status === 'conflict' ? '#fca5a5' : '#86efac'};">${cur.harmony.text}</div>
        </div>

        <h4 style="margin:0 0 8px 0;color:#fbbf24;">Spelling Corrections (Without Changing Meaning)</h4>
        <div class="crm-table-container" style="margin-bottom:16px;">
            <table class="crm-table">
                <thead><tr><th>Suggested Spelling</th><th>Compound → Namank</th><th>Adjustment</th><th>Status</th></tr></thead>
                <tbody>${spellRows}</tbody>
            </table>
        </div>

        <h4 style="margin:0 0 8px 0;color:#38bdf8;">New ${d.gender} Name Suggestions Starting With "${d.alphabet_query}"</h4>
        <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:10px;">
            ${alphaCards}
        </div>
    `;
}

async function runMobileAnalysis() {
    const mobile = (document.getElementById('mob-number')?.value || '').trim();
    const compare_mobile = (document.getElementById('mob-compare')?.value || '').trim();
    const dob = document.getElementById('mob-dob')?.value || '';
    if (!mobile || !dob) {
        showStatus('Please enter both Existing Mobile Number and Date of Birth.', 'error');
        return;
    }
    showStatus('Checking mobile number vibrations & DOB harmony...', 'loading');
    try {
        const res = await fetch('/api/studio/mobile-check', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ mobile, dob, compare_mobile })
        });
        const json = await res.json();
        if (!res.ok || !json.success) throw new Error(json.detail || 'Mobile check failed');
        renderMobileResults(json.data);
        hideStatus();
    } catch (err) {
        showStatus(`Mobile check error: ${err.message}`, 'error');
    }
}

function renderMobileResults(d) {
    const el = document.getElementById('mob-results-container');
    if (!el) return;

    const renderMobCard = (m, title) => {
        const scoreCol = m.score >= 75 ? '#4ade80' : (m.score >= 50 ? '#fbbf24' : '#f87171');
        return `
        <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.12);border-radius:10px;padding:14px;margin-bottom:12px;">
            <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;">
                <div>
                    <div style="font-size:12px;color:#34d399;">${title}</div>
                    <div style="font-size:20px;font-weight:700;font-family:monospace;">${m.mobile} <span style="font-size:13px;font-family:inherit;color:var(--text-secondary);">— Sum ${m.compound} → Root <strong style="color:#fbbf24;">${m.root}</strong></span></div>
                    <div style="font-size:12px;color:var(--text-secondary);margin-top:4px;">DOB ${d.dob} · BN <strong>${d.bn}</strong> · DN <strong>${d.dn}</strong> · Best Targets: <strong style="color:#4ade80;">${d.best_targets.join(', ')}</strong></div>
                </div>
                <div style="text-align:right;">
                    <div style="font-size:28px;font-weight:800;color:${scoreCol};line-height:1;">${m.score}<span style="font-size:13px;opacity:0.8;">/100</span></div>
                    <div style="font-size:12px;font-weight:700;color:${scoreCol};">${m.verdict}</div>
                </div>
            </div>
            <div class="resp-grid-2" style="margin-top:10px;font-size:12px;">
                <div style="background:rgba(34,197,94,0.1);border:1px solid rgba(34,197,94,0.25);border-radius:8px;padding:8px;">
                    <strong>Lucky Pairs:</strong> ${m.good_pairs.length ? m.good_pairs.join(', ') : 'None'}<br>
                    <strong>Fills Missing Grid Numbers:</strong> ${m.fills_missing.length ? m.fills_missing.join(', ') : 'None'}
                </div>
                <div style="background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.25);border-radius:8px;padding:8px;">
                    <strong>Harmful Pairs (28/48/49/etc.):</strong> ${m.bad_pairs.length ? m.bad_pairs.join(', ') : 'None ✓'}<br>
                    <strong>Ends on Lucky Digit (1,3,5,6,9):</strong> ${m.ends_well ? 'Yes ✓' : 'No (avoid ending in 4/8)'}
                </div>
            </div>
        </div>`;
    };

    const compareHtml = d.compare
        ? `${renderMobCard(d.compare, 'Candidate / New Mobile Number')}
           <div style="background:rgba(52,211,153,0.12);border:1px solid rgba(52,211,153,0.35);border-radius:8px;padding:10px 14px;font-size:12.5px;color:#6ee7b7;margin-bottom:10px;">
               <strong>Comparison Verdict:</strong> ${d.comparison_summary}
           </div>`
        : `<div style="background:rgba(255,255,255,0.03);border:1px dashed rgba(255,255,255,0.2);border-radius:8px;padding:10px 14px;font-size:12px;color:var(--text-secondary);">
               Want to test another mobile number? Enter it in the <strong>"Another Mobile Number (Optional)"</strong> box above and click <strong>Match Mobile Number(s)</strong> to compare both side-by-side.
           </div>`;

    el.innerHTML = renderMobCard(d.current, 'Existing Mobile Number') + compareHtml;
}

// ==========================================
// Business Partnership Match Making (1, 2, 3, N Partners)
// ==========================================
function initBusinessPartnershipListeners() {
    const listEl = document.getElementById('biz-partners-list');
    if (listEl && listEl.children.length === 0) {
        addBizPartnerRow('Partner 1', '1990-05-14');
        addBizPartnerRow('Partner 2', '1992-11-23');
    }
    const addBtn = document.getElementById('btn-biz-add-partner');
    if (addBtn) {
        addBtn.addEventListener('click', () => addBizPartnerRow('', ''));
    }
    const analyzeBtn = document.getElementById('btn-biz-analyze');
    if (analyzeBtn) {
        analyzeBtn.addEventListener('click', runBusinessPartnershipAnalysis);
    }
    document.querySelectorAll('.biz-pdf-btn').forEach(btn => {
        btn.addEventListener('click', () => downloadBusinessPartnershipPdf(btn.dataset.lang || 'en'));
    });
    const langSel = document.getElementById('biz-lang');
    if (langSel) {
        langSel.addEventListener('change', () => {
            if (document.getElementById('biz-results-container')?.innerHTML) {
                runBusinessPartnershipAnalysis();
            }
        });
    }
}

function addBizPartnerRow(defaultName = '', defaultDob = '') {
    const listEl = document.getElementById('biz-partners-list');
    if (!listEl) return;
    const idx = listEl.children.length + 1;
    const row = document.createElement('div');
    row.className = 'biz-partner-row';
    row.innerHTML = `
        <input type="text" class="biz-p-name" placeholder="Partner ${idx} Full Name" value="${escapeHtml(defaultName)}" style="width:100%;">
        <input type="date" class="biz-p-dob" value="${escapeHtml(defaultDob)}" style="width:100%;">
        <button type="button" class="btn-secondary biz-p-remove" style="padding:8px 10px; font-size:12px;" title="Remove Partner">✕</button>
    `;
    row.querySelector('.biz-p-remove').addEventListener('click', () => {
        if (listEl.children.length > 1) {
            row.remove();
        } else {
            showStatus('At least 1 partner is required.', 'error');
        }
    });
    listEl.appendChild(row);
}

function getBusinessPartnershipPayload(overrideLang) {
    const rows = document.querySelectorAll('#biz-partners-list .biz-partner-row');
    const partners = [];
    rows.forEach(r => {
        const name = (r.querySelector('.biz-p-name')?.value || '').trim();
        const dob = r.querySelector('.biz-p-dob')?.value || '';
        if (name && dob) partners.push({ name, dob });
    });
    return {
        partners,
        business_name: (document.getElementById('biz-firm-name')?.value || '').trim(),
        lang: overrideLang || document.getElementById('biz-lang')?.value || 'en'
    };
}

async function runBusinessPartnershipAnalysis() {
    const payload = getBusinessPartnershipPayload();
    if (!payload.partners.length) {
        showStatus('Please enter at least 1 partner Name and Date of Birth.', 'error');
        return;
    }
    showStatus('Analyzing Business Partnership Grids, Yogas & Dashas...', 'loading');
    try {
        const res = await fetch('/api/business-partnership/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        const json = await res.json();
        if (!res.ok || !json.success) {
            throw new Error(json.detail || 'Business partnership analysis failed');
        }
        renderBusinessPartnershipResults(json.data);
        hideStatus();
    } catch (err) {
        showStatus(`Business Partnership error: ${err.message}`, 'error');
    }
}

async function downloadBusinessPartnershipPdf(langOverride) {
    const payload = getBusinessPartnershipPayload(langOverride);
    if (!payload.partners.length) {
        showStatus('Please enter at least 1 partner Name and Date of Birth first.', 'error');
        return;
    }
    const langLabel = payload.lang === 'hi' ? 'Hindi' : (payload.lang === 'gu' ? 'Gujarati' : 'English');
    showStatus(`Generating ${langLabel} Business Partnership PDF...`, 'loading');
    try {
        const res = await fetch('/api/business-partnership/generate-pdf', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        const json = await res.json();
        if (!res.ok || !json.success) {
            throw new Error(json.detail || 'PDF generation failed');
        }
        if (json.data) renderBusinessPartnershipResults(json.data);
        showStatus(`Business Partnership PDF ready! <a href="${json.download_url}" target="_blank" style="color:#fbbf24;text-decoration:underline;margin-left:8px;">Download PDF ↗</a>`, 'success');
        window.open(json.download_url, '_blank');
    } catch (err) {
        showStatus(`Business Partnership PDF error: ${err.message}`, 'error');
    }
}

function renderBusinessPartnershipResults(b) {
    const el = document.getElementById('biz-results-container');
    if (!el) return;

    const bannerGrad = b.verdict_level === 'good'
        ? 'linear-gradient(90deg, #059669, #10b981)'
        : (b.verdict_level === 'moderate' ? 'linear-gradient(90deg, #d97706, #f59e0b)' : 'linear-gradient(90deg, #991b1b, #db2777)');

    const st = b.strongest_partner;
    const partnerCards = (b.partners || []).map(p => {
        const isAnc = p.name === st.name;
        const cellsHtml = (p.grid?.cells || []).map(c =>
            `<div style="border:1px solid rgba(212,175,55,0.35);padding:3px;text-align:center;min-height:28px;">
                <div style="font-size:8.5px;color:#94a3b8;">${c.num}</div>
                <div style="font-size:12px;font-weight:700;color:#fde68a;">${c.count > 0 ? c.str : ''}</div>
            </div>`
        ).join('');
        return `
        <div style="background:rgba(255,255,255,0.03);border:1px solid ${isAnc ? '#eab308' : 'rgba(255,255,255,0.1)'};border-radius:10px;padding:12px;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
                <strong style="font-size:14px;">${escapeHtml(p.name)} ${isAnc ? '★ Anchor' : ''}</strong>
                <span style="font-size:12px;font-weight:700;color:#4ade80;">${p.strength_score}/100</span>
            </div>
            <div style="font-size:11.5px;color:var(--text-secondary);margin-bottom:8px;">DOB: ${p.dob} · BN <strong>${p.bn}</strong> · DN <strong>${p.dn}</strong> · MD ${p.active_md}/AD ${p.active_ad}</div>
            <div style="display:grid;grid-template-columns:repeat(3,1fr);border:1px solid rgba(212,175,55,0.5);margin-bottom:8px;">${cellsHtml}</div>
            <div style="font-size:12px;"><strong>Role:</strong> ${escapeHtml(p.role)}</div>
        </div>`;
    }).join('');

    const pairHtml = (b.pairwise_matrix || []).length ? `
        <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.1);border-radius:10px;padding:12px;margin-top:12px;">
            <h4 style="margin:0 0 8px 0;color:#fde68a;">Pairwise Partner Compatibility</h4>
            ${b.pairwise_matrix.map(pm => `
                <div style="padding:6px 0;border-bottom:1px solid rgba(255,255,255,0.06);font-size:12px;">
                    <div style="display:flex;justify-content:space-between;">
                        <strong>${escapeHtml(pm.partner_a)} × ${escapeHtml(pm.partner_b)}</strong>
                        <strong style="color:${pm.score >= 75 ? '#4ade80' : (pm.score >= 55 ? '#fbbf24' : '#f87171')};">${pm.score}/100</strong>
                    </div>
                    <div style="color:var(--text-secondary);font-size:11.5px;">${escapeHtml(pm.note)}</div>
                </div>
            `).join('')}
        </div>` : '';

    const bizListHtml = (b.recommended_businesses || []).map(rb => `
        <div style="background:rgba(139,92,246,0.08);border:1px solid rgba(139,92,246,0.28);border-radius:8px;padding:10px 12px;margin-bottom:8px;">
            <strong style="font-size:13px;color:#ddd6fe;">Number ${rb.number} (${escapeHtml(rb.planet)}) — ${escapeHtml(rb.title)}</strong>
            <div style="font-size:12px;margin-top:2px;">${escapeHtml(rb.sectors)}</div>
            <div style="font-size:11px;color:var(--text-secondary);margin-top:2px;">Supported by: ${rb.supporters.map(escapeHtml).join(', ')}</div>
        </div>`).join('');

    el.innerHTML = `
        <div style="background:${bannerGrad};color:#fff;border-radius:12px;padding:16px 20px;display:flex;align-items:center;gap:18px;margin-bottom:12px;">
            <div style="font-size:32px;font-weight:800;line-height:1;">${b.overall_score}<span style="font-size:15px;opacity:0.85;">/100</span></div>
            <div>
                <div style="font-size:17px;font-weight:700;">${escapeHtml(b.verdict)}</div>
                <div style="font-size:12px;opacity:0.9;">Partners Evaluated: ${b.partner_count} · Best Business Namank: ${b.best_biz_namank.join(', ')}</div>
            </div>
        </div>
        <div style="background:rgba(234,179,8,0.12);border:1px solid rgba(234,179,8,0.45);border-radius:10px;padding:12px 14px;margin-bottom:14px;">
            <strong style="color:#fde68a;font-size:13.5px;">★ Strongest Anchor Partner: ${escapeHtml(st.name)} (${st.score}/100)</strong>
            <div style="font-size:12px;color:#fef3c7;margin-top:4px;">${escapeHtml(st.reason)}</div>
        </div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(250px, 1fr));gap:12px;">${partnerCards}</div>
        ${pairHtml}
        <div style="margin-top:14px;">
            <h4 style="margin:0 0 8px 0;color:#fde68a;">Common Recommended Businesses Together</h4>
            ${bizListHtml}
        </div>
    `;
}

// ==========================================
// 6. SAVED CLIENT DIRECTORY
// ==========================================
let savedClientsCache = [];

function initSavedClientsListeners() {
    const saveBtn = document.getElementById('btn-save-client');
    const refreshBtn = document.getElementById('btn-refresh-clients');
    const searchInput = document.getElementById('saved-clients-search');
    if (saveBtn) saveBtn.addEventListener('click', saveCurrentClient);
    if (refreshBtn) refreshBtn.addEventListener('click', () => loadSavedClients(searchInput ? searchInput.value : ''));
    if (searchInput) {
        let timer = null;
        searchInput.addEventListener('input', () => {
            clearTimeout(timer);
            timer = setTimeout(() => loadSavedClients(searchInput.value), 250);
        });
    }
    loadSavedClients('');
}

async function loadSavedClients(search = '') {
    const listEl = document.getElementById('saved-clients-list');
    if (!listEl) return;
    try {
        const res = await fetch(`/api/studio/clients?search=${encodeURIComponent(search.trim())}`);
        const json = await res.json();
        if (!res.ok || !json.success) return;
        savedClientsCache = json.clients || [];
        if (!savedClientsCache.length) {
            listEl.innerHTML = `<div class="empty-state">${search ? 'No matching saved clients.' : 'No saved clients yet. Click 💾 Save above to add.'}</div>`;
            return;
        }
        listEl.innerHTML = savedClientsCache.map(c => `
            <div class="report-item saved-client-row" data-client-id="${c.id}" style="display:flex;align-items:center;justify-content:space-between;gap:8px;cursor:pointer;padding:8px 10px;">
                <div class="load-client-area" data-client-id="${c.id}" style="flex:1;min-width:0;">
                    <div style="font-size:12.5px;font-weight:700;color:#fef3c7;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">${escapeHtml(c.client_name)}</div>
                    <div style="font-size:11px;color:var(--text-secondary);">${escapeHtml(c.dob)}${c.phone ? ' · ' + escapeHtml(c.phone) : ''}</div>
                </div>
                <button type="button" class="btn-icon-mini del-client-btn" data-client-id="${c.id}" title="Delete client" style="color:#f87171;padding:2px 6px;">×</button>
            </div>
        `).join('');

        listEl.querySelectorAll('.load-client-area').forEach(area => {
            area.addEventListener('click', () => {
                const cid = Number(area.getAttribute('data-client-id'));
                const client = savedClientsCache.find(x => x.id === cid);
                if (!client) return;
                document.getElementById('client-name').value = client.client_name || '';
                document.getElementById('client-phone').value = client.phone || '';
                document.getElementById('client-dob').value = client.dob || '';
                document.getElementById('client-gender').value = client.gender || 'Male';
                document.getElementById('consultant-notes').value = client.notes || '';
                updateWeekdayDisplay();
                fetchAnalysis(true);
                showStatus(`Loaded client: ${client.client_name}`, 'success');
            });
        });

        listEl.querySelectorAll('.del-client-btn').forEach(btn => {
            btn.addEventListener('click', async (e) => {
                e.stopPropagation();
                const cid = Number(btn.getAttribute('data-client-id'));
                const r = await fetch(`/api/studio/clients/${cid}`, { method: 'DELETE' });
                if (r.ok) {
                    loadSavedClients(document.getElementById('saved-clients-search')?.value || '');
                    showStatus('Client removed from directory.', 'success');
                }
            });
        });
    } catch (err) {
        console.warn('loadSavedClients error:', err);
    }
}

async function saveCurrentClient() {
    const name = document.getElementById('client-name')?.value.trim();
    const dob = document.getElementById('client-dob')?.value;
    const gender = document.getElementById('client-gender')?.value || 'Male';
    const phone = document.getElementById('client-phone')?.value.trim() || '';
    const notes = document.getElementById('consultant-notes')?.value.trim() || '';
    if (!name || !dob) {
        showStatus('Please enter Client Name and Date of Birth before saving.', 'error');
        return;
    }
    try {
        const res = await fetch('/api/studio/clients', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, dob, gender, phone, notes })
        });
        const json = await res.json();
        if (!res.ok || !json.success) throw new Error(json.detail || 'Save failed');
        showStatus(`Saved "${name}" to Client Directory!`, 'success');
        loadSavedClients(document.getElementById('saved-clients-search')?.value || '');
    } catch (err) {
        showStatus(`Error saving client: ${err.message}`, 'error');
    }
}

// ==========================================
// 7. BABY NAME NUMEROLOGY GENERATOR
// ==========================================
function initBabyNamesListeners() {
    const btn = document.getElementById('btn-baby-analyze');
    if (btn) btn.addEventListener('click', runBabyNames);
    document.querySelectorAll('.baby-pdf-btn').forEach(b => {
        b.addEventListener('click', () => downloadBabyNamesPdf(b.getAttribute('data-lang') || 'en'));
    });
}

function getBabyNamesPayload() {
    return {
        dob: document.getElementById('baby-dob')?.value || '',
        surname: document.getElementById('baby-surname')?.value.trim() || '',
        gender: document.getElementById('baby-gender')?.value || 'Male',
        alpha: document.getElementById('baby-alpha')?.value.trim() || ''
    };
}

async function runBabyNames() {
    const payload = getBabyNamesPayload();
    if (!payload.dob) {
        showStatus('Please enter Baby Date of Birth.', 'error');
        return;
    }
    showStatus('Generating auspicious baby names...', 'loading');
    try {
        const res = await fetch('/api/studio/baby-names', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        const json = await res.json();
        if (!res.ok || !json.success) throw new Error(json.detail || 'Generation failed');
        renderBabyNamesResults(json.data);
        showStatus('Baby name suggestions ready!', 'success');
    } catch (err) {
        showStatus(`Baby name error: ${err.message}`, 'error');
    }
}

async function downloadBabyNamesPdf(lang) {
    const payload = { ...getBabyNamesPayload(), lang };
    if (!payload.dob) {
        showStatus('Please enter Baby Date of Birth.', 'error');
        return;
    }
    const langLabel = lang === 'hi' ? 'Hindi' : (lang === 'gu' ? 'Gujarati' : 'English');
    showStatus(`Generating ${langLabel} Baby Name PDF...`, 'loading');
    try {
        const res = await fetch('/api/studio/baby-names/generate-pdf', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        const json = await res.json();
        if (!res.ok || !json.success) throw new Error(json.detail || 'PDF generation failed');
        if (json.data) renderBabyNamesResults(json.data);
        showStatus(`Baby Name PDF ready! <a href="${json.download_url}" target="_blank" style="color:#fbbf24;text-decoration:underline;margin-left:8px;">Download PDF ↗</a>`, 'success');
        window.open(json.download_url, '_blank');
    } catch (err) {
        showStatus(`Baby Name PDF error: ${err.message}`, 'error');
    }
}

function renderBabyNamesResults(d) {
    const el = document.getElementById('baby-results-container');
    if (!el || !d) return;
    const rows = (d.suggestions || []).map((s, idx) => `
        <div style="background:rgba(255,255,255,0.03);border:1px solid ${s.is_best ? 'rgba(16,185,129,0.45)' : 'rgba(212,175,55,0.28)'};border-radius:10px;padding:12px;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">
                <strong style="font-size:15px;color:#fef3c7;">${idx + 1}. ${escapeHtml(s.full_name)}</strong>
                <span style="font-size:11px;font-weight:700;padding:2px 8px;border-radius:12px;background:rgba(16,185,129,0.18);color:#4ade80;">Namank ${s.namank}${s.is_best ? ' ★ Best' : ''}</span>
            </div>
            <div style="font-size:12px;color:var(--text-secondary);">First Name: <strong>${escapeHtml(s.first_name)}</strong> · Full Chaldean Compound: <strong>${s.compound}</strong> → <strong>${s.namank}</strong></div>
            <div style="font-size:11.5px;color:#cbd5e1;margin-top:4px;">Ruling Planet: <strong>${escapeHtml(s.planet)}</strong> · Starts with <strong>${escapeHtml(s.starts_with)}</strong></div>
        </div>
    `).join('');

    el.innerHTML = `
        <div style="background:linear-gradient(90deg, rgba(139,92,246,0.25), rgba(212,175,55,0.18));border:1px solid rgba(212,175,55,0.45);border-radius:12px;padding:14px 16px;margin-bottom:14px;">
            <div style="font-size:15px;font-weight:700;color:#fde68a;">Baby Chart: Basic Number ${d.bn} (${escapeHtml(d.bn_planet)}) · Destiny Number ${d.dn} (${escapeHtml(d.dn_planet)})</div>
            <div style="font-size:12.5px;color:#e2e8f0;margin-top:4px;">Target Lucky Namank Numbers: <strong>${(d.best_targets || []).join(', ')}</strong> · Gender: <strong>${escapeHtml(d.gender)}</strong></div>
        </div>
        <div class="resp-grid-2" style="gap:10px;">${rows || '<div class="empty-state">No matching names found for that letter filter. Try clearing the starting letter.</div>'}</div>
    `;
}

// ==========================================
// 8. HOUSE, SHOP & VEHICLE NUMBER CHECKER
// ==========================================
function initPropertyVehicleListeners() {
    const btn = document.getElementById('btn-pv-analyze');
    if (btn) btn.addEventListener('click', runPropertyVehicle);
    document.querySelectorAll('.pv-pdf-btn').forEach(b => {
        b.addEventListener('click', () => downloadPropertyVehiclePdf(b.getAttribute('data-lang') || 'en'));
    });
}

function getPropertyVehiclePayload() {
    return {
        dob: document.getElementById('pv-dob')?.value || '',
        property_type: document.getElementById('pv-prop-type')?.value || 'Home / Flat',
        house_number: document.getElementById('pv-house')?.value.trim() || '',
        vehicle_number: document.getElementById('pv-vehicle')?.value.trim() || '',
        lang: currentLang || 'en'
    };
}

async function runPropertyVehicle() {
    const payload = getPropertyVehiclePayload();
    if (!payload.dob) {
        showStatus('Please enter Owner Date of Birth.', 'error');
        return;
    }
    showStatus('Analyzing House & Vehicle compatibility...', 'loading');
    try {
        const res = await fetch('/api/studio/property-vehicle-check', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        const json = await res.json();
        if (!res.ok || !json.success) throw new Error(json.detail || 'Analysis failed');
        renderPropertyVehicleResults(json.data);
        showStatus('House & Vehicle analysis ready!', 'success');
    } catch (err) {
        showStatus(`Property/Vehicle error: ${err.message}`, 'error');
    }
}

async function downloadPropertyVehiclePdf(lang) {
    const payload = { ...getPropertyVehiclePayload(), lang };
    if (!payload.dob) {
        showStatus('Please enter Owner Date of Birth.', 'error');
        return;
    }
    const langLabel = lang === 'hi' ? 'Hindi' : (lang === 'gu' ? 'Gujarati' : 'English');
    showStatus(`Generating ${langLabel} House & Vehicle PDF...`, 'loading');
    try {
        const res = await fetch('/api/studio/property-vehicle-pdf', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        const json = await res.json();
        if (!res.ok || !json.success) throw new Error(json.detail || 'PDF generation failed');
        if (json.data) renderPropertyVehicleResults(json.data);
        showStatus(`House & Vehicle PDF ready! <a href="${json.download_url}" target="_blank" style="color:#fbbf24;text-decoration:underline;margin-left:8px;">Download PDF ↗</a>`, 'success');
        window.open(json.download_url, '_blank');
    } catch (err) {
        showStatus(`House & Vehicle PDF error: ${err.message}`, 'error');
    }
}

function renderPropertyVehicleCard(item, title) {
    if (!item) return '';
    const isGood = item.status === 'auspicious' || item.score >= 70;
    const isMod = !isGood && (item.status === 'neutral' || item.score >= 50);
    const color = isGood ? '#4ade80' : (isMod ? '#fbbf24' : '#f87171');
    const border = isGood ? 'rgba(16,185,129,0.5)' : (isMod ? 'rgba(245,158,11,0.45)' : 'rgba(239,68,68,0.5)');
    const bgTint = isGood ? 'rgba(16,185,129,0.06)' : (isMod ? 'rgba(245,158,11,0.05)' : 'rgba(239,68,68,0.06)');
    return `
        <div style="background:${bgTint};border:1px solid ${border};border-radius:12px;padding:16px;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;gap:8px;">
                <strong style="font-size:15px;color:#fde68a;">${escapeHtml(title)}: ${escapeHtml(item.raw || '')}</strong>
                <span style="font-size:16px;font-weight:800;color:${color};white-space:nowrap;">${item.score}/100</span>
            </div>
            <div style="font-size:12.5px;color:${color};font-weight:700;margin-bottom:4px;">${escapeHtml(item.verdict)} · Root ${item.root} (${escapeHtml(item.planet)}) · Compound ${item.compound}</div>
            ${item.breakdown ? `<div style="font-size:11px;color:var(--text-secondary);margin-bottom:8px;">Calculation: ${escapeHtml(item.breakdown)}</div>` : ''}
            <div style="font-size:12.5px;color:#e2e8f0;line-height:1.5;margin-bottom:10px;">${escapeHtml(item.meaning)}</div>
            ${item.vastu_tips ? `
            <div style="font-size:12px;color:#e9d5ff;background:rgba(139,92,246,0.12);border-left:3px solid #a855f7;padding:8px 10px;border-radius:4px;margin-bottom:8px;">
                <strong>🏛️ Vastu Guidance (For Harmony &amp; Improvement):</strong> ${escapeHtml(item.vastu_tips)}
            </div>` : ''}
            <div style="font-size:12px;color:#fef3c7;background:rgba(212,175,55,0.1);border-left:3px solid ${color};padding:8px 10px;border-radius:4px;">
                <strong>🕉️ Vedic Remedy (For Prosperity &amp; Protection):</strong> ${escapeHtml(item.vedic_remedies || item.remedy || '')}
            </div>
        </div>
    `;
}

function renderPropertyVehicleResults(d) {
    const el = document.getElementById('pv-results-container');
    if (!el || !d) return;
    el.innerHTML = `
        <div style="background:linear-gradient(90deg, rgba(139,92,246,0.25), rgba(212,175,55,0.18));border:1px solid rgba(212,175,55,0.45);border-radius:12px;padding:14px 16px;margin-bottom:14px;">
            <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;">
                <div style="font-size:15px;font-weight:700;color:#fde68a;">Owner Chart: Basic ${d.bn} (${escapeHtml(d.bn_planet || '')}) · Destiny ${d.dn} (${escapeHtml(d.dn_planet || '')})</div>
                <div style="font-size:11.5px;background:rgba(15,23,42,0.55);padding:4px 10px;border-radius:8px;border:1px solid rgba(255,255,255,0.12);">
                    <span style="color:#4ade80;font-weight:700;">● 70+ Good Match</span> &nbsp;|&nbsp;
                    <span style="color:#fbbf24;font-weight:700;">● 50–69 Moderate</span> &nbsp;|&nbsp;
                    <span style="color:#f87171;font-weight:700;">● &lt;50 Needs Remedy</span>
                </div>
            </div>
            <div style="font-size:12.5px;color:#e2e8f0;margin-top:4px;">Most Auspicious Numbers for Owner: <strong>${(d.best_numbers || []).join(', ')}</strong></div>
        </div>
        <div class="resp-grid-2" style="gap:14px;">
            ${renderPropertyVehicleCard(d.house, d.property_type || 'Property')}
            ${renderPropertyVehicleCard(d.vehicle, 'Vehicle')}
        </div>
    `;
}
