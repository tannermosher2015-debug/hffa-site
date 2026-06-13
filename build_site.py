"""Generator for the HFFA Local 1463 multi-page site.
Writes every .html file from shared chrome + per-page content.
Run:  python build_site.py
This is a local dev tool — it is NOT needed by Netlify at runtime."""
import os
OUT = os.path.dirname(os.path.abspath(__file__))

NAV_ITEMS = [("index.html", "Home"), ("about.html", "About"), ("members.html", "Members"),
             ("wellness.html", "Wellness"), ("news.html", "News"), ("retirees.html", "Retirees"),
             ("in-memoriam.html", "In Memoriam"), ("shop.html", "Shop"), ("contact.html", "Contact")]

SPRITE = (
'<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>'
'<symbol id="i-phone" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3-8.6A2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.3 1.8.6 2.6a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.5-1.1a2 2 0 0 1 2.1-.5c.8.3 1.7.5 2.6.6a2 2 0 0 1 1.7 2Z"/></symbol>'
'<symbol id="i-menu" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M4 6h16M4 12h16M4 18h16"/></symbol>'
'<symbol id="i-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></symbol>'
'<symbol id="i-a11y" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="4" r="2"/><path d="M5 8h14M12 8v6m0 0-3 6m3-6 3 6"/></symbol>'
'<symbol id="i-fb" viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.4v7A10 10 0 0 0 22 12Z"/></symbol>'
'<symbol id="i-ig" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor" stroke="none"/></symbol>'
'</defs></svg>\n')

A11Y_PANEL = '''
<button type="button" class="a11y-fab" id="a11yFab" aria-label="Open accessibility settings" aria-haspopup="dialog" aria-controls="a11yPanel"><svg aria-hidden="true"><use href="#i-a11y"/></svg></button>
<div class="a11y-overlay" id="a11yOverlay"></div>
<div class="a11y-panel" id="a11yPanel" role="dialog" aria-modal="true" aria-labelledby="a11yTitle" hidden>
  <div class="a11y-header">
    <h2 id="a11yTitle"><svg aria-hidden="true"><use href="#i-a11y"/></svg> Accessibility</h2>
    <button type="button" class="a11y-close" id="a11yClose" aria-label="Close accessibility settings"><svg aria-hidden="true"><use href="#i-close"/></svg></button>
  </div>
  <div class="a11y-body">
    <div class="a11y-group">
      <h3>Text Size</h3>
      <div class="seg" role="group" aria-label="Text size">
        <button type="button" class="s1 textsize" data-size="100" aria-pressed="true">A</button>
        <button type="button" class="s2 textsize" data-size="112" aria-pressed="false">A</button>
        <button type="button" class="s3 textsize" data-size="125" aria-pressed="false">A</button>
        <button type="button" class="s4 textsize" data-size="140" aria-pressed="false">A</button>
      </div>
    </div>
    <div class="a11y-group">
      <h3>Display &amp; Reading</h3>
      <div class="toggle-row"><span class="toggle-label"><b>High contrast</b><span>Maximum contrast colors</span></span>
        <label class="switch"><input type="checkbox" id="tHc" aria-label="High contrast mode"><span class="track" aria-hidden="true"></span><span class="thumb" aria-hidden="true"></span></label></div>
      <div class="toggle-row"><span class="toggle-label"><b>Readable font</b><span>Atkinson Hyperlegible + spacing</span></span>
        <label class="switch"><input type="checkbox" id="tReadable" aria-label="Readable font"><span class="track" aria-hidden="true"></span><span class="thumb" aria-hidden="true"></span></label></div>
      <div class="toggle-row"><span class="toggle-label"><b>Reduce motion</b><span>Pause animations &amp; transitions</span></span>
        <label class="switch"><input type="checkbox" id="tMotion" aria-label="Reduce motion"><span class="track" aria-hidden="true"></span><span class="thumb" aria-hidden="true"></span></label></div>
      <div class="toggle-row"><span class="toggle-label"><b>Underline links</b><span>Underline every hyperlink</span></span>
        <label class="switch"><input type="checkbox" id="tUnderline" aria-label="Underline links"><span class="track" aria-hidden="true"></span><span class="thumb" aria-hidden="true"></span></label></div>
    </div>
  </div>
  <div class="a11y-footer">
    <button type="button" class="a11y-reset" id="a11yReset">Reset all</button>
    <button type="button" class="a11y-done" id="a11yDone">Done</button>
  </div>
</div>
<div aria-live="polite" aria-atomic="true" class="sr-only" id="liveRegion"></div>
'''

def head(title, desc):
    return ('<!doctype html>\n<html lang="en">\n<head>\n'
      '<meta charset="UTF-8" />\n<meta name="viewport" content="width=device-width, initial-scale=1.0" />\n'
      f'<title>{title}</title>\n<meta name="description" content="{desc}" />\n'
      '<meta name="theme-color" content="#7a0a0e" />\n'
      '<link rel="preconnect" href="https://fonts.googleapis.com" />\n'
      '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />\n'
      '<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=Barlow+Condensed:wght@500;600;700;800;900&family=Barlow:wght@300;400;500;600;700&display=swap" rel="stylesheet" />\n'
      '<link rel="stylesheet" href="styles.css" />\n</head>\n<body>\n')

def utility_bar():
    return ('<div class="util"><div class="wrap">'
      '<span class="util-left">HFFA Local 1463 · IAFF · AFL-CIO</span>'
      '<div class="util-right">'
      '<a class="util-phone" href="tel:+18089491566"><svg aria-hidden="true"><use href="#i-phone"/></svg> 808-949-1566</a>'
      '</div></div></div>\n')

def nav(active):
    links = "".join(
      f'<a class="nav-link" href="{href}"' + (' aria-current="page"' if href == active else '') + f'>{label}</a>'
      for href, label in NAV_ITEMS)
    mlinks = "".join(f'<a class="nav-link" href="{href}">{label}</a>' for href, label in NAV_ITEMS)
    return (utility_bar() +
      '<header class="masthead-bar"><nav class="wrap topnav" aria-label="Primary">'
      '<a class="logo-link" href="index.html" aria-label="HFFA Local 1463 home">'
      '<img class="logo-badge" src="logo.png" alt="HFFA Local 1463 Maltese cross emblem" />'
      '<span class="logo-text"><strong>Hawaii Fire Fighters Association</strong><span>HFFA Local 1463 · IAFF</span></span></a>'
      f'<div class="nav-desktop">{links}</div>'
      '<div class="nav-actions">'
      '<button type="button" class="icon-btn" id="a11yOpen" aria-label="Open accessibility settings" aria-haspopup="dialog"><svg aria-hidden="true"><use href="#i-a11y"/></svg></button>'
      '<a class="btn btn-gold nav-desktop-cta" href="contact.html#register">Become a Member</a>'
      '<button type="button" class="icon-btn nav-toggle" id="navToggle" aria-label="Open menu" aria-expanded="false" aria-controls="mobileNav"><svg aria-hidden="true"><use href="#i-menu"/></svg></button>'
      '</div></nav></header>\n'
      '<div class="mobile-overlay" id="mobileOverlay" hidden></div>'
      '<nav class="mobile-nav" id="mobileNav" hidden aria-label="Mobile navigation"><div class="mn-head"><strong>HFFA 1463</strong>'
      '<button type="button" class="icon-btn" id="navClose" aria-label="Close menu"><svg aria-hidden="true"><use href="#i-close"/></svg></button></div>'
      f'{mlinks}<a class="btn btn-gold" href="contact.html#register">Become a Member</a></nav>\n')

def footer():
    return ('<footer id="footer"><div class="wrap"><div class="footer-top">'
      '<div class="footer-brand"><div class="logo-row"><img src="logo.png" alt="HFFA Local 1463" />'
      '<strong>Hawaii Fire Fighters Association</strong></div>'
      '<div class="meta">HFFA Local 1463 · IAFF · AFL-CIO</div>'
      '<div class="meta">1018 Palm Drive, Honolulu HI 96814</div>'
      '<div class="meta">Office Hours: 8:00 a.m.–4:30 p.m., Mon–Fri</div>'
      '<div class="phone">808-949-1566 · 800-310-1566 (toll-free) · Fax 808-952-6003</div>'
      '<div class="phone"><a href="mailto:info@iafflocal1463.org" style="color:var(--gold)">info@iafflocal1463.org</a></div>'
      '<div class="social-row" aria-label="HFFA on social media">'
      '<a href="https://www.instagram.com/hffa1463/" target="_blank" rel="noopener" aria-label="HFFA on Instagram"><svg aria-hidden="true"><use href="#i-ig"/></svg></a>'
      '<a href="https://www.facebook.com/HFFA1463" target="_blank" rel="noopener" aria-label="HFFA on Facebook"><svg aria-hidden="true"><use href="#i-fb"/></svg></a>'
      '</div></div>'
      '<div class="footer-cols">'
      '<div class="footer-col"><span class="label">Members</span>'
      '<a href="members.html">Members</a><a href="benefits.html">Benefits</a><a href="wellness.html">Wellness</a><a href="retirees.html">Retirees</a></div>'
      '<div class="footer-col"><span class="label">Association</span>'
      '<a href="about.html">About Us</a><a href="news.html">News</a><a href="in-memoriam.html">In Memoriam</a><a href="shop.html">Shop</a><a href="contact.html">Contact</a></div>'
      '</div></div>'
      '<div class="footer-bottom"><span class="copy">© <span id="yr">2026</span> Hawaii Fire Fighters Association</span>'
      '<span class="strong-tag">Local 1463 Strong</span></div></div></footer>\n')

def page(filename, title, desc, active, main_html):
    html = (head(title, desc)
      + '<a class="skip-link" href="#main">Skip to main content</a>\n'
      + SPRITE
      + nav(active)
      + f'<main id="main">\n{main_html}\n</main>\n'
      + footer()
      + A11Y_PANEL
      + '<script src="site.js" defer></script>\n</body>\n</html>')
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename, len(html), "bytes")


# ======================= PAGE CONTENT =======================

def main_home():
    return r'''<div id="fb-root"></div>
<script async defer crossorigin="anonymous" src="https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v19.0"></script>
<div class="masthead">
  <section class="wrap hero" id="top" aria-labelledby="hero-h">
    <div class="hero-main">
      <span class="label">Representing ~1,900 firefighters statewide</span>
      <h1 id="hero-h">You Can <span class="gold">Count On Us.</span></h1>
      <p class="hero-lead">HFFA Local 1463 has fought for Hawaii's fire service since 1963 — at the bargaining table, in the legislature, and alongside our members every single shift.</p>
      <div class="hero-cta">
        <a class="btn btn-gold" href="contact.html#register">Become a Member</a>
        <a class="btn btn-ghost" href="members.html">Contract Updates</a>
      </div>
    </div>
    <div class="hero-logo-wrap" aria-hidden="true"><img class="hero-logo" src="logo.png" alt="" /></div>
  </section>
  <div class="quicklinks"><div class="wrap" aria-label="Quick links">
    <a class="quick-btn" href="members.html"><span class="emoji" aria-hidden="true">📅</span> Shift Calendar</a>
    <a class="quick-btn" href="members.html"><span class="emoji" aria-hidden="true">📋</span> File a Grievance</a>
    <a class="quick-btn" href="members.html"><span class="emoji" aria-hidden="true">📄</span> CBA Documents</a>
    <a class="quick-btn" href="benefits.html"><span class="emoji" aria-hidden="true">💊</span> Benefits Portal</a>
    <a class="quick-btn" href="wellness.html"><span class="emoji" aria-hidden="true">🆘</span> Crisis Support</a>
  </div></div>
</div>

<div class="wrap content">
  <section aria-labelledby="notices-h" style="margin-bottom:36px">
    <span class="red-bar" aria-hidden="true"></span>
    <h2 class="hl" id="notices-h" style="font-size:22px;margin-bottom:14px">Latest Notices</h2>
    <div class="notice-list">
      <div class="notice"><span class="emoji" aria-hidden="true">🏛️</span><div><b>Office Closed — King Kamehameha I Day</b><span>The HFFA office is closed Thursday, June 11, reopening Friday. Enjoy the parades across the State and stay safe. Mahalo!</span></div></div>
      <div class="notice"><span class="emoji" aria-hidden="true">🚗</span><div><b>Drive Pono — School's Out</b><span>Summer break and graduation season are here. Watch for our keiki, avoid distracted or impaired driving, and use a designated driver. Drive pono and arrive alive.</span></div></div>
    </div>
  </section>

  <div class="two-col">
    <section class="feed" id="feed" aria-labelledby="feed-h">
      <div class="feed-head">
        <div><span class="red-bar" aria-hidden="true"></span><span class="label">Live from the field</span><h2 class="hl" id="feed-h">Your Union, Right Now</h2></div>
        <a class="btn btn-outline-dark no-ul" href="https://www.instagram.com/hffa1463/" target="_blank" rel="noopener"><span class="emoji" aria-hidden="true">📸</span> Follow @hffa1463</a>
      </div>
      <div class="social-embeds">
        <div class="social-col">
          <h3 class="social-col-h">Latest on Instagram</h3>
          <div class="ig-embed" id="ig-feed">
            <!-- ===== BEHOLD INSTAGRAM WIDGET =====
                 Paste the two lines from your Behold.so dashboard between these markers
                 (then re-run: python build_site.py). They look like:
                 <script src="https://w.behold.so/widget.js" type="module"></script>
                 <behold-widget feed-id="YOUR_FEED_ID"></behold-widget>
            -->
            <a class="social-fallback" href="https://www.instagram.com/hffa1463/" target="_blank" rel="noopener">
              <span class="emoji" aria-hidden="true">📸</span>
              <b>Follow @hffa1463 on Instagram</b>
              <span>See our latest photos &amp; reels →</span>
            </a>
          </div>
        </div>
        <div class="social-col">
          <h3 class="social-col-h">Latest on Facebook</h3>
          <div class="fb-page" data-href="https://www.facebook.com/HFFA1463" data-tabs="timeline" data-width="500" data-height="640" data-small-header="true" data-adapt-container-width="true" data-hide-cover="false" data-show-facepile="true">
            <blockquote cite="https://www.facebook.com/HFFA1463" class="fb-xfbml-parse-ignore"><a href="https://www.facebook.com/HFFA1463">Hawaii Fire Fighters Association on Facebook</a></blockquote>
          </div>
          <a class="social-fallback" href="https://www.facebook.com/HFFA1463" target="_blank" rel="noopener" style="margin-top:12px">
            <span class="emoji" aria-hidden="true">📘</span>
            <b>Follow us on Facebook</b>
            <span>HFFA Local 1463 →</span>
          </a>
        </div>
      </div>
    </section>

    <aside class="sidebar" id="sidebar" aria-labelledby="side-h">
      <div class="sidebar-head"><span class="red-bar" aria-hidden="true"></span><span class="label">Notices &amp; Updates</span><h2 class="hl" id="side-h">What's Happening</h2></div>
      <div class="contract-card">
        <h3><span class="emoji" aria-hidden="true">📜</span> Contract Negotiations</h3>
        <p>Active negotiations are ongoing. Member updates and documents are available through the secure portal.</p>
        <a class="btn btn-gold" href="members.html">View Contract Updates →</a>
      </div>
      <div class="notice-card">
        <h3><span class="emoji" aria-hidden="true">🕊️</span> In Memoriam</h3>
        <p class="mem-item">Ret. Hawaii County FF George Sugi — passed May 6, 2026 (retired HFD 1985)</p>
        <p class="mem-item">Ret. Honolulu Capt. Albert Young — 25 yrs, Quint 12; private service</p>
        <p class="mem-item">Ret. Hawaii County FEO Darrel Sato — age 71, 25+ yrs of service</p>
        <a class="card-link" href="in-memoriam.html">View In Memoriam →</a>
      </div>
      <div class="notice-card">
        <h3><span class="emoji" aria-hidden="true">📅</span> Upcoming Events</h3>
        <div class="event"><div class="event-date">Sat. Sept 19, 2026</div><div class="event-name">IAFF Fallen Fire Fighter Memorial</div><div class="event-loc">Colorado Springs, CO — honoring FF Jeffrey Fiala</div></div>
        <div class="event"><div class="event-date">October 2026</div><div class="event-name">HFF Signature Chefs Food Festival</div><div class="event-loc">13th annual — HFD Headquarters</div></div>
      </div>
      <div class="cancer-card">
        <h3><span class="emoji" aria-hidden="true">🎗️</span> Wellness &amp; Cancer Support</h3>
        <p>Occupational cancer is the #1 cause of firefighter LODD. 247 of 311 IAFF line-of-duty deaths in 2025 were cancer-related.</p>
        <a href="wellness.html">Wellness &amp; Support →</a>
      </div>
    </aside>
  </div>

  <section class="stats" aria-label="HFFA by the numbers">
    <div class="stat"><div class="stat-num"><span class="count" data-target="1900" data-suffix="+">0</span></div><div class="stat-label">Active Members</div></div>
    <div class="stat"><div class="stat-num"><span class="count" data-target="63">0</span></div><div class="stat-label">Years Representing Hawaii</div></div>
    <div class="stat"><div class="stat-num"><span class="count" data-target="5">0</span></div><div class="stat-label">Departments Served</div></div>
    <div class="stat"><div class="stat-num"><span class="count" data-target="21">0</span></div><div class="stat-label">Contracts Negotiated</div></div>
  </section>

  <section aria-labelledby="res-h">
    <div class="res-head"><span class="label">Member Resources</span><h2 class="hl" id="res-h">Everything You Need</h2></div>
    <div class="res-grid">
      <a class="res-card" href="benefits.html"><div class="res-ico" aria-hidden="true">📋</div><h3>Member Benefits</h3><p>HFFA MetLife Group Plan, PEC portal, legal coverage, and IAFF FIREPAC.</p><span class="card-link">View Benefits →</span></a>
      <a class="res-card" href="members.html"><div class="res-ico" aria-hidden="true">📋</div><h3>Member Resources</h3><p>Shift calendar, CBA documents, grievances, and contract updates.</p><span class="card-link">View Members →</span></a>
      <a class="res-card" href="wellness.html"><div class="res-ico" aria-hidden="true">💙</div><h3>Wellness &amp; Support</h3><p>Cancer awareness, behavioral health, and crisis &amp; peer support.</p><span class="card-link">Get Support →</span></a>
    </div>
  </section>

  <section class="about-band" aria-labelledby="about-teaser-h" style="margin-top:48px">
    <div class="about-copy">
      <h2 id="about-teaser-h">Working For You 24/7</h2>
      <p>Since 1963, HFFA Local 1463 has been the exclusive collective-bargaining representative for all City, State, and County firefighters in Hawai'i — an affiliate of the IAFF, AFL-CIO. When seconds count, our members protect lives knowing their Union is looking out for them.</p>
    </div>
    <a class="btn btn-gold" href="about.html">Learn About Us →</a>
  </section>
</div>'''


def page_body(label, h1, lead, inner):
    return (f'<section class="page-hero"><div class="wrap"><span class="label">{label}</span>'
      f'<h1>{h1}</h1><p>{lead}</p></div></section>\n'
      f'<div class="wrap content"><div class="prose">\n{inner}\n</div></div>')


def main_benefits():
    inner = r'''<h2>HFFA MetLife Supplemental Group Benefit Plan</h2>
<p>Learn more about these voluntary, supplemental benefits — carefully designed and underwritten by MetLife to provide the highest level of coverage with the best group rates, specifically for our HFFA active-duty members. Premiums are paid conveniently through payroll deduction.</p>
<p><strong>Eligibility:</strong> All full-time members actively working a minimum of 30 hours are eligible to enroll during open enrollment. <em>Documents in the member portal are for members only.</em></p>

<h2>Plan Features</h2>
<div class="info-grid">
  <div class="info-card"><h3>Accident Insurance</h3><p>Helps manage medical costs from accidental injuries on and off the job. Benefits are paid directly to you for initial care, injuries, and follow-up — in addition to any other coverage.</p></div>
  <div class="info-card"><h3>Hospital Indemnity</h3><p>Expecting a newborn or planning a surgery? Ask about the hospital indemnity plan for help with unexpected hospital costs.</p></div>
  <div class="info-card"><h3>Legal Plan</h3><p>Participating Hawaii attorneys can assist with wills and trusts, family law, traffic, and more, organized by legal topic.</p></div>
  <div class="info-card"><h3>Critical Illness w/ Cancer</h3><p>Coverage that pays a benefit on diagnosis of a covered critical illness, including cancer.</p></div>
  <div class="info-card"><h3>Portable at Retirement</h3><p>Members who signed up while active duty can convert their plans to portable coverage. Ask about the details.</p></div>
</div>

<div class="callout callout-gold">
  <h3>🎁 Get $100 Health-Screening Credits</h3>
  <p>The Critical Illness w/Cancer, 24-Hour Accident, and Hospital Indemnity plans include a $100 health-screening credit for the employee and covered family members. See the eligible-screenings list, then submit the Health Screening Benefit Form. Register first on the MetLife MyBenefits page.</p>
</div>

<h3>MetLife Microsite</h3>
<p>For tutorials, FAQs, and more, visit the <a href="https://hffa.pecservices.info/" target="_blank" rel="noopener">HFFA MetLife Microsite</a>.</p>

<h3>Portals &amp; Claims</h3>
<p>MetLife plan participants should register on both portals. File claims at the <a href="https://servicing.online.metlife.com/public/site/presignin?grpNumber=231849" target="_blank" rel="noopener">MetLife MyBenefits page</a> (group&nbsp;#231849), and manage enrollment through the <a href="https://metlife.benselect.com/Enroll/Login.aspx" target="_blank" rel="noopener">PEC enrollment portal</a>.</p>

<div class="callout callout-red">
  <h3>📞 PEC — Your Benefits Plan Administrator</h3>
  <p>The PEC team can assist with questions about plan coverages. Email the dedicated HFFA line at <a href="mailto:hffacustomerservice@pecworksite.com">hffacustomerservice@pecworksite.com</a> — they understand shift work and will reply with the best time to reach you.</p>
  <p><strong>PEC Benefits Service Call Center: (800) 747-6009</strong><br>Mon–Fri 4 a.m.–3 p.m. HST · Sat 5–11 a.m. HST</p>
</div>

<h3>Dental Coverage</h3>
<p>Dental insurance is <strong>not</strong> included in the MetLife plan. For dental, contact <a href="https://eutf.hawaii.gov/" target="_blank" rel="noopener">EUTF</a> — Oahu (808) 586-7390, Toll-Free 1-800-295-0089. Note: if you carry the 24-Hour Accident plan, you are covered for certain dental repairs resulting from an accident (see your Accident Certificate).</p>

<p class="disclaimer">Anton Financial is not affiliated with Hawaii Fire Fighters Association.</p>'''
    return page_body("Member Resources", "Medical &amp; Group Benefits",
        "Voluntary supplemental coverage built for HFFA members — MetLife group benefits, PEC support, and health-screening credits.", inner)


def main_news():
    inner = r'''<h2>SSA · WEP-GPO Update</h2>
<h3>A Message from Congressman Ed Case</h3>
<p>In a February 27, 2025 letter to HFFA President Robert H. Lee, Congressman Ed Case shared an update on the <strong>Social Security Fairness Act</strong> — which repealed the Windfall Elimination Provision (WEP) and Government Pension Offset (GPO) that had reduced benefits for many public-service workers with pensions.</p>
<p>The SSA announced it would immediately begin paying retroactive benefits and increasing monthly payments for those impacted. Read the SSA's <a href="https://www.ssa.gov/benefits/retirement/social-security-fairness-act.html" target="_blank" rel="noopener">Social Security Fairness Act update</a> and subscribe for changes.</p>

<h2>In Support of Fire Fighters</h2>
<p>In Hawaii, two foundations are associated with HFFA:</p>
<div class="info-grid">
  <div class="info-card"><h3>Honolulu Firefighters Foundation (HFF)</h3><p>Originator of the annual <strong>Signature Chefs Food Festival</strong> — planning its 13th annual event this <strong>October</strong> at HFD Headquarters. Proceeds support HFD members, the Straub Burn Unit, and smoke-alarm installations in kupuna homes on O'ahu. Ticket sales are by mail and online only — no cold calls. Questions: <a href="mailto:lee-ann@pacificrimconcepts.com">lee-ann@pacificrimconcepts.com</a> (Pacific Rim Concepts).</p></div>
  <div class="info-card"><h3>Hawaiian Islands Fire Foundation (HIFF)</h3><p>A newly created statewide foundation to support all HFFA members. HIFF is not conducting a fundraiser at this time as it develops its programs.</p></div>
</div>
<p>Other legitimate mainland firefighter foundations we are familiar with:</p>
<ul>
  <li>International Association of Fire Fighters Foundation (IAFF)</li>
  <li>National Fallen Fire Fighters Foundation (NFFF)</li>
  <li>Firefighters Cancer Support Network (FCSN)</li>
</ul>'''
    return page_body("Latest News", "News &amp; Updates",
        "Legislative updates, foundation events, and news from Local 1463 and the IAFF.", inner)


def main_about():
    inner = r'''<h2>Working For You 24/7</h2>
<p>The Hawaii Fire Fighters Association (HFFA Local 1463) is an affiliate of the International Association of Fire Fighters (IAFF), AFL-CIO. Since <strong>1963</strong>, HFFA Local 1463 has been the exclusive collective-bargaining representative for all City, State, and County firefighters in Hawai'i.</p>
<p>Its primary role is to negotiate and administer the collective bargaining agreement that governs the terms and conditions of firefighter employment — while handling grievances and performing labor-related and legislative activities in the interest of its members.</p>

<h2>Part of a National Force</h2>
<p>As of May 1, 2024, IAFF membership rose to <strong>345,493 members</strong>, making it one of the largest and most influential labor unions in North America — committed to advancing the rights, safety, and future of firefighters, emergency medical workers, and rescue workers across the United States and Canada.</p>
<p>The IAFF is the driving force behind nearly every advance in the fire and emergency services in the 21st century. With headquarters in Washington, D.C., and Ottawa, Ontario, the IAFF represents full-time professional firefighters and paramedics in more than 3,500 affiliates, protecting more than 85 percent of the population in communities throughout the U.S. and Canada. Its Political Action Committee, <strong>FIREPAC</strong>, is among the top one-half of one percent of the nearly 6,000 federally registered PACs in the country.</p>

<h2>Second to None</h2>
<p>It is an undeniable fact that among labor organizations, HFFA and its parent union, the IAFF, are second to none when it comes to membership representation. Whether at the bargaining table or in the legislative halls of Washington, D.C.; from the county council to the Fire Chief's office; in the courts and throughout the 50th state — Hawai'i's firefighters are ably represented.</p>
<p>You can count on HFFA Local 1463 members to bravely protect lives and property, knowing that their Union is looking out for them. Because when seconds count, saving a life is all that matters.</p>'''
    return page_body("Working For You 24/7", "About HFFA Local 1463",
        "Representing Hawai'i's firefighters since 1963 — at the bargaining table, in the legislature, and on every shift.", inner)


def main_retirees():
    inner = r'''<div class="callout callout-red">
  <h3>☕ Retirement, Medicare &amp; the Windfall Act — Coffee Talk</h3>
  <p>Presented by representatives of the Hawaii State Health Insurance Assistance Program (SHIP) and the Social Security Administration. Space is limited at the HFFA Office. To sign up, email <a href="mailto:daisyfire@hawaiifirefighters.org">daisyfire@hawaiifirefighters.org</a>.</p>
</div>

<h2>Nā Lei Kukui — HFD Newsletter</h2>
<p>Sharing stories, building bonds, enriched with HFD culture. In August 2023, the Honolulu Fire Department published the inaugural issue of <em>Nā Lei Kukui</em>. Each issue keeps the HFD ʻOhana informed and engaged — stories of courage, department events, off-duty gatherings, and accounts of the Department's rich history and community involvement.</p>
<p>The goal of Nā Lei Kukui is <strong>for members, by our members</strong> — reach out to the working group with feedback and suggestions. To contribute or subscribe, email <a href="mailto:hfdnewsletter@honolulu.gov">hfdnewsletter@honolulu.gov</a>.</p>
<p><strong>Issues:</strong> March 2024 · November 2023 · August 2023</p>

<h2>Honolulu Magazine Spotlight</h2>
<h3>15 Trailblazing Women</h3>
<p>In the April issue of Honolulu Magazine, "Leading Wahine: Meet 15 Who Inspire and Push Honolulu Forward" featured retired Battalion Chief <strong>Debbi Eleneki</strong> who, 35 years ago, was the only female firefighter. Her path to serve was instilled by her father, Peter Akiona, a retired rescue firefighter who taught her to respect others, give back, and keep her word. Those ethics prepared her to enter the firehouse in 1987 with heart, humility, and hard work.</p>'''
    return page_body("For Our Retirees", "Retirees",
        "Resources, gatherings, and stories for HFFA Local 1463 retirees — Medicare and Windfall Act help, the HFD newsletter, and member spotlights.", inner)


def main_contact():
    return r'''<section class="page-hero"><div class="wrap"><span class="label">Get in Touch</span>
<h1>Contact Us</h1><p>Questions, grievances, or membership updates — reach the HFFA Local 1463 office. We're here to help.</p></div></section>

<div class="wrap content">
  <div class="contact-grid">
    <div>
      <div class="form-section">
        <h2>Send Us a Message</h2>
        <p class="sub">Fill out the form and the HFFA office will get back to you.</p>
        <form class="form" name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="/thanks.html">
          <input type="hidden" name="form-name" value="contact" />
          <p class="hp"><label>Don't fill this out if you're human: <input name="bot-field" /></label></p>
          <div class="row two">
            <div class="field"><label for="c-name">Name <span class="req" aria-hidden="true">*</span></label>
              <input id="c-name" name="name" type="text" required autocomplete="name" />
              <span class="error" role="alert">Please enter your name.</span></div>
            <div class="field"><label for="c-email">Email <span class="req" aria-hidden="true">*</span></label>
              <input id="c-email" name="email" type="email" required autocomplete="email" />
              <span class="error" role="alert">Please enter a valid email address.</span></div>
          </div>
          <div class="row"><div class="field"><label for="c-phone">Phone</label>
            <input id="c-phone" name="phone" type="tel" autocomplete="tel" /></div></div>
          <div class="row"><div class="field"><label for="c-msg">Comment <span class="req" aria-hidden="true">*</span></label>
            <textarea id="c-msg" name="comment" required></textarea>
            <span class="error" role="alert">Please enter a message.</span></div></div>
          <button type="submit" class="btn btn-red">Submit</button>
          <p class="form-status" role="status" aria-live="polite"></p>
        </form>
      </div>
    </div>

    <aside aria-labelledby="cinfo-h">
      <h2 class="hl" id="cinfo-h" style="font-size:24px;margin-bottom:10px">Contact Info</h2>
      <dl class="contact-info">
        <dt>Mailing Address</dt><dd>1018 Palm Drive, Honolulu HI 96814</dd>
        <dt>Telephone</dt>
        <dd><a href="tel:+18089491566">808-949-1566</a> (Oahu)</dd>
        <dd><a href="tel:+18003101566">800-310-1566</a> (Toll-Free)</dd>
        <dd>808-952-6003 (Fax)</dd>
        <dt>Email</dt><dd><a href="mailto:info@iafflocal1463.org">info@iafflocal1463.org</a></dd>
        <dt>Office Hours</dt><dd>8:00 a.m.–4:30 p.m., Monday–Friday</dd>
      </dl>
      <div class="callout callout-gold" style="margin-top:20px">
        <h3>⚠️ Phone-Solicitation Notice</h3>
        <p>Hawaii Fire Fighters Association is <strong>not</strong> conducting phone solicitations. If contacted for donations, do not give out your information — verify the organization first.</p>
      </div>
      <p style="margin-top:16px"><a class="card-link" href="https://www.facebook.com/" target="_blank" rel="noopener">Visit our Facebook page →</a></p>
    </aside>
  </div>

  <div class="form-section" id="register" style="margin-top:48px">
    <span class="red-bar" aria-hidden="true"></span>
    <h2>Member Registration &amp; Info</h2>
    <p class="sub">New member or need to update your details? Submit your membership information below. <strong>Account login &amp; password setup are handled on our secure member portal</strong> — <a href="#" aria-label="Member portal (link to be provided)">log in to the member portal</a>.</p>
    <form class="form" name="membership-info" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="/thanks.html" style="max-width:100%">
      <input type="hidden" name="form-name" value="membership-info" />
      <p class="hp"><label>Don't fill this out if you're human: <input name="bot-field" /></label></p>
      <div class="row two">
        <div class="field"><label for="m-first">First Name <span class="req" aria-hidden="true">*</span></label><input id="m-first" name="first-name" type="text" required autocomplete="given-name" /><span class="error" role="alert">Required.</span></div>
        <div class="field"><label for="m-last">Last Name <span class="req" aria-hidden="true">*</span></label><input id="m-last" name="last-name" type="text" required autocomplete="family-name" /><span class="error" role="alert">Required.</span></div>
      </div>
      <div class="row"><div class="field"><label for="m-addr">Mailing Address</label><input id="m-addr" name="mailing-address" type="text" autocomplete="street-address" /></div></div>
      <div class="row two">
        <div class="field"><label for="m-city">City</label><input id="m-city" name="city" type="text" autocomplete="address-level2" /></div>
        <div class="field"><label for="m-state">State</label><input id="m-state" name="state" type="text" autocomplete="address-level1" /></div>
      </div>
      <div class="row two">
        <div class="field"><label for="m-zip">Zip Code</label><input id="m-zip" name="zip" type="text" inputmode="numeric" autocomplete="postal-code" /></div>
        <div class="field"><label for="m-empid">Employee ID</label><input id="m-empid" name="employee-id" type="text" /></div>
      </div>
      <div class="row two">
        <div class="field"><label for="m-iaff">IAFF Number</label><input id="m-iaff" name="iaff-number" type="text" /></div>
        <div class="field"><label for="m-email">Email <span class="req" aria-hidden="true">*</span></label><input id="m-email" name="email" type="email" required autocomplete="email" /><span class="error" role="alert">Valid email required.</span></div>
      </div>
      <div class="row two">
        <div class="field"><label for="m-phone">Phone</label><input id="m-phone" name="phone" type="tel" autocomplete="tel" /></div>
        <div class="field"><label for="m-mobile">Mobile</label><input id="m-mobile" name="mobile" type="tel" /></div>
      </div>
      <div class="row two">
        <div class="field"><label for="m-status">Membership Status</label>
          <select id="m-status" name="membership-status"><option value="">Select…</option><option>Active Duty</option><option>Retired</option><option>Other</option></select></div>
        <div class="field"><label for="m-shift">Shift</label>
          <select id="m-shift" name="shift"><option value="">Select…</option><option>1st Platoon</option><option>2nd Platoon</option><option>3rd Platoon</option><option>Day Staff</option></select></div>
      </div>
      <div class="row two">
        <div class="field"><label for="m-div">Division</label><input id="m-div" name="division" type="text" /></div>
        <div class="field"><label for="m-rank">Rank</label><input id="m-rank" name="rank" type="text" /></div>
      </div>
      <div class="row two">
        <div class="field"><label for="m-hire">Appointment / Hire Date</label><input id="m-hire" name="hire-date" type="date" /></div>
        <div class="field"><label for="m-ret">Retirement Date</label><input id="m-ret" name="retirement-date" type="date" /></div>
      </div>
      <button type="submit" class="btn btn-red">Submit Member Info</button>
      <p class="form-status" role="status" aria-live="polite"></p>
    </form>
  </div>
</div>'''


def main_shop():
    inner = r'''<h2>HFFA Local 1463 Gear &amp; Merchandise</h2>
<p>Show your Local 1463 pride. Official apparel, challenge coins, hats, towels, and more — with proceeds supporting our members and community programs.</p>
<div class="callout callout-red">
  <h3><span class="emoji" aria-hidden="true">🛒</span> Visit Our Official Store</h3>
  <p>Our full catalog — tees, polos, dri-fit gear, snapbacks, challenge coins, the 2026–2027 calendar and more — is available now on our secure Square store.</p>
  <a class="btn btn-gold" href="https://hawaii-fire-fighters-association.square.site" target="_blank" rel="noopener" style="margin-top:6px">Shop the HFFA Store →</a>
</div>
<p style="margin-top:18px"><strong>A built-in product gallery is coming soon to this page.</strong> For now, browse and order through the store above, or call the HFFA office at <a href="tel:+18089491566">808-949-1566</a> for assistance.</p>
<p class="disclaimer">The Local 1463 logo is a registered trademark of the Hawaii Fire Fighters Association and may not be used without express authorization.</p>'''
    return page_body("Member Store", "Shop", "Official HFFA Local 1463 apparel and gear — proceeds support our members and community.", inner)


def main_members():
    inner = r'''<p>Resources for active HFFA Local 1463 members. Most member documents are distributed through the office or the secure member system — <a href="contact.html">contact us</a> anytime and we'll get you what you need.</p>

<h2>Contract &amp; Negotiations</h2>
<div class="callout callout-red">
  <h3>📜 Contract Negotiations &amp; Updates</h3>
  <p>Active negotiations are ongoing. Member updates and the current collective bargaining agreement are shared with members directly. <a href="contact.html">Contact the office</a> for the latest status.</p>
</div>

<h2>Member Resources</h2>
<div class="info-grid">
  <div class="info-card"><h3>Shift Calendar</h3><p>Current 1st, 2nd, and 3rd Platoon schedules for all departments. Request the latest schedule from the office.</p></div>
  <div class="info-card"><h3>CBA Documents</h3><p>The collective bargaining agreement governing the terms and conditions of employment — available to members through the office.</p></div>
  <div class="info-card"><h3>File a Grievance</h3><p>Have a workplace issue? Reach out to your union steward or the HFFA office to start the grievance process.</p></div>
  <div class="info-card"><h3>Member Benefits</h3><p>Voluntary MetLife supplemental coverage, PEC support, and health-screening credits. <a href="benefits.html">See full Benefits →</a></p></div>
</div>

<div class="callout callout-gold">
  <h3>🤝 Need something specific?</h3>
  <p>For shift schedules, CBA documents, grievance help, or contract questions, <a href="contact.html">contact the HFFA office</a> at 808-949-1566 or info@iafflocal1463.org. Also see <a href="wellness.html">Wellness &amp; Support</a> for behavioral-health and cancer resources.</p>
</div>'''
    return page_body("For Our Members", "Members", "Shift schedules, CBA documents, grievances, contract updates, and benefits — everything for active Local 1463 members.", inner)


def main_wellness():
    inner = r'''<p>Your health and safety come first. HFFA Local 1463 and the IAFF provide resources for firefighter wellness — from occupational cancer to behavioral health.</p>

<h2>Firefighter Cancer Awareness</h2>
<div class="callout callout-gold">
  <h3>🎗️ Cancer is the #1 line-of-duty risk</h3>
  <p>Occupational cancer is the leading cause of firefighter line-of-duty deaths. In 2025, 247 of 311 IAFF line-of-duty deaths were cancer-related. If you need assistance, the Firefighter Cancer Support Network can help.</p>
  <p><a href="https://www.firefightercancersupport.org/request-assistance" target="_blank" rel="noopener">firefightercancersupport.org →</a></p>
</div>

<h2>Behavioral Health</h2>
<h3>You Are Not Alone</h3>
<p>The cumulative traumatic stresses faced by firefighters, paramedics, and EMTs can affect mental health and well-being. Support is available, and reaching out is a sign of strength.</p>

<h3>IAFF Center of Excellence</h3>
<p>The IAFF Center of Excellence for Behavioral Health Treatment and Recovery is an addiction-treatment facility built specifically for IAFF members — a safe place to recover alongside others who understand the job.</p>
<p>13400 Edgemeade Rd, Upper Marlboro, MD 20772 · (301) 327-1955 · <a href="https://www.iaffrecoverycenter.com" target="_blank" rel="noopener">iaffrecoverycenter.com</a></p>
<p>Learn more about IAFF <a href="https://www.iaff.org/behavioral-health/" target="_blank" rel="noopener">behavioral-health resources</a>.</p>

<div class="callout callout-red">
  <h3>📞 Need to talk now?</h3>
  <p>If you or a member of your ʻohana is in crisis, call or text <strong>988</strong> (Suicide &amp; Crisis Lifeline), or reach the HFFA office at 808-949-1566 to connect with peer support.</p>
</div>'''
    return page_body("Wellness & Support", "Wellness", "Firefighter cancer awareness, behavioral health, and crisis & peer support for Local 1463 members and their families.", inner)


def main_inmemoriam():
    inner = r'''<p>We honor the Hawai'i firefighters who served their communities with courage and dedication. Their watch is over; we hold the line in their memory.</p>

<h2>In Remembrance</h2>
<div class="info-grid">
  <div class="info-card"><h3>Ret. FF George Sugi</h3><p>Hawaii County Fire Department. Passed May 6, 2026; retired from HFD June 30, 1985. Our condolences to the Sugi ʻohana.</p></div>
  <div class="info-card"><h3>Ret. Capt. Albert Young</h3><p>Honolulu Fire Department. Appointed February 24, 1975 and served 25 years; last assigned to Quint 12, 3rd Platoon. A private service was held.</p></div>
  <div class="info-card"><h3>Ret. FEO Darrel Sato</h3><p>Hawaii County Fire Department, age 71. Served over 25 years until his retirement in December 2013. Keep his family in your thoughts.</p></div>
</div>

<h2>Fallen Fire Fighter Memorials</h2>
<div class="callout callout-red">
  <h3>🕊️ IAFF Fallen Fire Fighter Memorial</h3>
  <p>The IAFF's 40th Fallen Fire Fighter Memorial Observance is Saturday, September 19, 2026, in Colorado Springs. Honolulu FF1 <strong>Jeffrey Fiala</strong>'s name will be engraved on the IAFF Wall of Honor alongside others who made the ultimate sacrifice. <a href="https://www.iaff.org" target="_blank" rel="noopener">Learn more →</a></p>
</div>
<p><strong>National Fallen Firefighters Memorial</strong> — held May 2–3, 2026 in Emmitsburg, Maryland, honoring firefighters from 2025 and prior years. Learn more at the <a href="https://www.firehero.org" target="_blank" rel="noopener">National Fallen Firefighters Foundation</a>.</p>'''
    return page_body("In Memoriam", "In Memoriam", "Honoring the Hawai'i firefighters we have lost, and the IAFF and national fallen-firefighter memorials.", inner)


# ======================= BUILD =======================
if __name__ == "__main__":
    page("index.html", "HFFA Local 1463 — Hawaii Fire Fighters Association",
         "Hawaii Fire Fighters Association — HFFA Local 1463, IAFF/AFL-CIO. Representing ~1,900 firefighters statewide since 1963. You Can Count On Us.",
         "index.html", main_home())
    page("benefits.html", "Benefits — HFFA Local 1463",
         "HFFA MetLife supplemental group benefits, PEC portal, health-screening credits, and dental guidance for Local 1463 members.",
         "members.html", main_benefits())
    page("members.html", "Members — HFFA Local 1463",
         "Member resources for HFFA Local 1463 — shift calendar, CBA documents, grievances, contract updates, and benefits.",
         "members.html", main_members())
    page("wellness.html", "Wellness — HFFA Local 1463",
         "Firefighter wellness — cancer awareness, behavioral health, and crisis and peer support for Local 1463 members and families.",
         "wellness.html", main_wellness())
    page("in-memoriam.html", "In Memoriam — HFFA Local 1463",
         "Honoring the Hawai'i firefighters we have lost, and the IAFF and national fallen-firefighter memorials.",
         "in-memoriam.html", main_inmemoriam())
    page("news.html", "News & Updates — HFFA Local 1463",
         "HFFA Local 1463 news: SSA/WEP-GPO, foundations and the Signature Chefs Festival, scam alerts, and behavioral-health resources.",
         "news.html", main_news())
    page("about.html", "About — HFFA Local 1463",
         "About HFFA Local 1463 — Hawai'i's exclusive firefighter bargaining representative since 1963, an IAFF/AFL-CIO affiliate.",
         "about.html", main_about())
    page("retirees.html", "Retirees — HFFA Local 1463",
         "Retiree resources from HFFA Local 1463 — Medicare and Windfall Act help, the Nā Lei Kukui newsletter, and member spotlights.",
         "retirees.html", main_retirees())
    page("contact.html", "Contact — HFFA Local 1463",
         "Contact HFFA Local 1463 — 1018 Palm Drive, Honolulu HI 96814 · 808-949-1566 · info@iafflocal1463.org. Member registration & info.",
         "contact.html", main_contact())
    page("shop.html", "Shop — HFFA Local 1463",
         "Official HFFA Local 1463 store — apparel, challenge coins, hats, and gear. Proceeds support our members and community.",
         "shop.html", main_shop())
    print("done.")
