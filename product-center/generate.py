#!/usr/bin/env python3
"""Generate all product category pages for Matrix Technology Product Center."""

CATEGORIES = [
    {
        "id": "dc-power-supply",
        "name": "DC Power Supply",
        "emoji": "⚡",
        "badge_label": "Category 01",
        "tagline": "Programmable Precision DC Sources",
        "description": "From benchtop programmable supplies to high-power industrial systems, Matrix DC Power Supplies deliver unmatched accuracy, stability, and reliability. Ideal for R&D labs, production testing, and burn-in applications.",
        "color_from": "#0a1c3a",
        "color_to": "#0f2d5e",
        "glow_color": "rgba(0,194,255,0.15)",
        "products": [
            {
                "model": "MPS-3005D",
                "name": "Programmable DC Power Supply 30V/5A",
                "desc": "High-precision benchtop supply with 4-digit LED display, CV/CC modes, and USB/RS232 interface.",
                "features": ["30V / 5A", "4-Wire Sensing", "USB Interface", "OVP/OCP"],
                "type": "benchtop",
            },
            {
                "model": "MPS-6003D",
                "name": "Dual-Channel DC Supply 60V/3A",
                "desc": "Independent dual-output programmable supply with tracking modes and isolated channels.",
                "features": ["Dual Output", "60V / 3A", "Tracking Mode", "GPIB"],
                "type": "benchtop",
            },
            {
                "model": "MPS-1530T",
                "name": "Triple-Output DC Supply",
                "desc": "Three independent outputs: ±15V/3A fixed + 0–30V/5A variable. Perfect for analog circuit testing.",
                "features": ["Triple Output", "±15V Fixed", "Variable 30V", "Low Ripple"],
                "type": "benchtop",
            },
            {
                "model": "MPH-600W",
                "name": "High-Power Programmable Supply 600W",
                "desc": "Rack-mount 600W supply with LAN/GPIB interface, CC/CV operation, and remote sense.",
                "features": ["600W", "Rack Mount", "LAN/GPIB", "Remote Sense"],
                "type": "rack",
            },
            {
                "model": "MPH-2KW",
                "name": "2kW System Power Supply",
                "desc": "Modular 2kW supply designed for automated test systems, fuel cell simulation, and battery formation.",
                "features": ["2000W", "Modular", "RS485 Bus", "4Q Output"],
                "type": "rack",
            },
            {
                "model": "MBT-500",
                "name": "Battery Test Power Supply 500W",
                "desc": "Optimised for battery charge/discharge cycling with cell balancing and data logging.",
                "features": ["Battery Test", "500W", "Data Logger", "4-Ch Monitor"],
                "type": "battery",
            },
        ],
    },
    {
        "id": "ac-power-supply",
        "name": "AC Power Supply",
        "emoji": "〜",
        "badge_label": "Category 02",
        "tagline": "Programmable AC Sources & Frequency Converters",
        "description": "Matrix AC Power Supplies simulate real-world grid conditions — voltage sags, frequency deviations, and harmonics — enabling comprehensive compliance testing to IEC, UL, and EN standards.",
        "color_from": "#1a0a3a",
        "color_to": "#2d0f5e",
        "glow_color": "rgba(100,0,255,0.15)",
        "products": [
            {
                "model": "MAP-1000S",
                "name": "1kVA Programmable AC Source",
                "desc": "Single-phase programmable AC source, 0–300 Vrms, 15–1000 Hz. Ideal for IEC 61000-3-2 testing.",
                "features": ["1kVA", "0–300Vrms", "15–1000Hz", "USB Control"],
                "type": "single",
            },
            {
                "model": "MAP-3000T",
                "name": "3kVA Three-Phase AC Source",
                "desc": "Balanced three-phase AC source with independent phase amplitude/angle control.",
                "features": ["3kVA", "3-Phase", "Phase Angle", "GPIB/LAN"],
                "type": "three-phase",
            },
            {
                "model": "MAP-6000T",
                "name": "6kVA Three-Phase AC Power System",
                "desc": "Rack-mount 6 kVA three-phase system with arbitrary waveform generation and IEC compliance testing.",
                "features": ["6kVA", "Arbitrary Wave", "IEC Tests", "Rack Mount"],
                "type": "three-phase",
            },
            {
                "model": "MFC-2000",
                "name": "2kVA Frequency Converter",
                "desc": "Convert 50Hz to 60Hz (and vice versa) with stabilized output for international equipment testing.",
                "features": ["50/60Hz", "2kVA", "Stabilized", "Compact"],
                "type": "frequency",
            },
            {
                "model": "MAP-500M",
                "name": "500VA Benchtop AC Source",
                "desc": "Compact benchtop AC source for lab use. 0–300 V, 40–500 Hz, color touchscreen.",
                "features": ["500VA", "Touchscreen", "40–500Hz", "Data Log"],
                "type": "single",
            },
            {
                "model": "MAP-15KT",
                "name": "15kVA High-Power 3-Phase Source",
                "desc": "High-power three-phase AC system for aviation, military, and industrial equipment testing.",
                "features": ["15kVA", "3-Phase", "High Power", "LAN/RS485"],
                "type": "three-phase",
            },
        ],
    },
    {
        "id": "electronic-loads",
        "name": "Electronic Loads",
        "emoji": "🔌",
        "badge_label": "Category 03",
        "tagline": "DC & AC Electronic Load Systems",
        "description": "Simulate realistic loads on power supplies, batteries, chargers, and inverters. Matrix Electronic Loads offer CC/CV/CR/CP modes, dynamic loading, and parallel expansion for high-power applications.",
        "color_from": "#0a2a1a",
        "color_to": "#0f5e2d",
        "glow_color": "rgba(0,255,100,0.12)",
        "products": [
            {
                "model": "MEL-300W",
                "name": "DC Electronic Load 300W",
                "desc": "Programmable DC electronic load with CC/CV/CR/CP modes and LED display for benchtop use.",
                "features": ["300W", "CC/CV/CR/CP", "Dynamic Mode", "USB"],
                "type": "dc",
            },
            {
                "model": "MEL-1200W",
                "name": "DC Electronic Load 1200W",
                "desc": "High-power single-channel DC load with parallel operation capability for up to 6kW system.",
                "features": ["1200W", "Parallel", "OCP Test", "LAN"],
                "type": "dc",
            },
            {
                "model": "MEL-ACH",
                "name": "AC/DC Electronic Load",
                "desc": "Dual-mode AC/DC load for testing inverters, UPS, and AC/DC converters with PF simulation.",
                "features": ["AC+DC", "PF Control", "Inverter Test", "UPS Test"],
                "type": "ac",
            },
            {
                "model": "MEL-BAT",
                "name": "Battery Discharge Load Tester",
                "desc": "Dedicated battery discharge tester with capacity analysis, internal resistance, and cycle testing.",
                "features": ["Battery Test", "Capacity Calc", "IR Measure", "Cycle Mode"],
                "type": "battery",
            },
            {
                "model": "MEL-MCH",
                "name": "Multi-Channel Electronic Load",
                "desc": "4-channel independent programmable loads in a single rack unit for multi-output PSU testing.",
                "features": ["4-Channel", "Independent", "Rack 1U", "GPIB/LAN"],
                "type": "dc",
            },
            {
                "model": "MEL-6KW",
                "name": "High-Power Load System 6kW",
                "desc": "Modular 6 kW DC system built from 1200W modules. Fully parallel/series configurable.",
                "features": ["6kW System", "Modular", "Auto-Range", "Master/Slave"],
                "type": "dc",
            },
        ],
    },
    {
        "id": "lcr-meter",
        "name": "LCR Meter",
        "emoji": "📡",
        "badge_label": "Category 04",
        "tagline": "Precision Impedance & Component Analyzers",
        "description": "Matrix LCR Meters provide fast, accurate measurement of inductance (L), capacitance (C), and resistance (R) across a wide frequency range. Essential for component sorting, QC, and materials research.",
        "color_from": "#2a1a0a",
        "color_to": "#5e2d0f",
        "glow_color": "rgba(255,150,0,0.12)",
        "products": [
            {
                "model": "MLR-100",
                "name": "Handheld LCR Meter",
                "desc": "Portable LCR meter for quick component checks. 100Hz/1kHz/10kHz test frequencies.",
                "features": ["Handheld", "3 Frequencies", "Auto-Range", "Backlight"],
                "type": "handheld",
            },
            {
                "model": "MLR-821A",
                "name": "Benchtop LCR Meter 20Hz–300kHz",
                "desc": "High-accuracy benchtop LCR meter with 0.05% basic accuracy and component sorting bins.",
                "features": ["0.05% Accuracy", "20Hz–300kHz", "Binning", "Handler"],
                "type": "benchtop",
            },
            {
                "model": "MLR-822A",
                "name": "Precision LCR Meter 1MHz",
                "desc": "Extended frequency range to 1 MHz for RF component characterisation. 7-inch colour display.",
                "features": ["1MHz Range", "7\" Display", "0.02% Acc.", "USB/LAN"],
                "type": "benchtop",
            },
            {
                "model": "MIA-500",
                "name": "Impedance Analyzer 5MHz",
                "desc": "Full impedance analysis up to 5 MHz with Z, θ, L, C, R, Q, D sweep and graphing.",
                "features": ["5MHz", "Sweep Graph", "Z/θ/L/C/R", "GPIB"],
                "type": "analyzer",
            },
            {
                "model": "MLR-PRO",
                "name": "In-Circuit LCR Meter",
                "desc": "Measures components in-circuit without desoldering using anti-interference guard technology.",
                "features": ["In-Circuit", "Guard Terminal", "Auto-LCR", "Fast 7ms"],
                "type": "benchtop",
            },
            {
                "model": "MLR-TF",
                "name": "Transformer Tester",
                "desc": "Specialised instrument for transformer turns ratio, leakage inductance, and magnetizing current.",
                "features": ["Turns Ratio", "Leakage L", "Mag Current", "Winding Test"],
                "type": "special",
            },
        ],
    },
    {
        "id": "withstand-voltage-tester",
        "name": "Withstand Voltage Tester",
        "emoji": "⚠",
        "badge_label": "Category 05",
        "tagline": "Hipot & Electrical Safety Test Equipment",
        "description": "Ensure electrical safety compliance with Matrix Hipot Testers. Our range covers AC/DC withstanding voltage, insulation resistance, ground continuity, and leakage current — meeting IEC, UL, and CE requirements.",
        "color_from": "#2a0a0a",
        "color_to": "#5e0f0f",
        "glow_color": "rgba(255,50,50,0.12)",
        "products": [
            {
                "model": "MHT-501",
                "name": "AC Hipot Tester 5kVAC",
                "desc": "5kVAC withstanding voltage tester with adjustable ramp, dwell, and breakdown detection.",
                "features": ["5kVAC", "Ramp Mode", "0.1mA Res.", "Safety Interlock"],
                "type": "hipot",
            },
            {
                "model": "MHT-502",
                "name": "AC/DC Hipot Tester",
                "desc": "Combined AC and DC hipot tester: 5kVAC / 6kVDC with automatic discharge and arc detection.",
                "features": ["5kVAC/6kVDC", "Arc Detect", "Auto Discharge", "USB Log"],
                "type": "hipot",
            },
            {
                "model": "MIR-5000",
                "name": "Insulation Resistance Tester",
                "desc": "Digital megohmmeter for insulation testing: 50V–5000V test voltage, 0.01MΩ–1TΩ range.",
                "features": ["50–5000V", "0.01MΩ–1TΩ", "PI/DAR Test", "Bluetooth"],
                "type": "insulation",
            },
            {
                "model": "MGC-100",
                "name": "Ground Continuity Tester",
                "desc": "Tests ground/earth bond continuity with 25A/30A AC test current. Dual clamp connections.",
                "features": ["25A Test", "Dual Clamp", "Auto-Scan", "Pass/Fail LED"],
                "type": "ground",
            },
            {
                "model": "MES-3IN1",
                "name": "3-in-1 Electrical Safety Tester",
                "desc": "All-in-one unit combining hipot, insulation resistance, and ground continuity into a single instrument.",
                "features": ["3-in-1", "Auto Sequence", "IEC/UL Tests", "LAN/RS232"],
                "type": "combo",
            },
            {
                "model": "MHT-10K",
                "name": "High Voltage AC Tester 10kVAC",
                "desc": "Heavy-duty 10kVAC tester for HV transformers, cable assemblies, and switchgear testing.",
                "features": ["10kVAC", "High Power", "Arc Detect", "Rack Mount"],
                "type": "hipot",
            },
        ],
    },
    {
        "id": "oscilloscope",
        "name": "Oscilloscope",
        "emoji": "📊",
        "badge_label": "Category 06",
        "tagline": "Digital Storage Oscilloscopes & Signal Analyzers",
        "description": "Matrix oscilloscopes deliver deep memory, high sample rates, and advanced triggering in a compact design. From 50 MHz entry-level models to 1 GHz mixed-signal workhorses — the right scope for every engineer.",
        "color_from": "#0a1a2a",
        "color_to": "#0f365e",
        "glow_color": "rgba(0,194,255,0.15)",
        "products": [
            {
                "model": "MDS-100",
                "name": "50MHz Digital Oscilloscope",
                "desc": "2-channel 50MHz DSO with 1GSa/s sample rate, 7\" colour display, and USB storage.",
                "features": ["50MHz", "1GSa/s", "2CH", "7\" Colour"],
                "type": "dso",
            },
            {
                "model": "MDS-200",
                "name": "200MHz 4-Channel Oscilloscope",
                "desc": "4-channel 200MHz scope with 2GSa/s, 128Mpts memory, and advanced maths/FFT analysis.",
                "features": ["200MHz", "2GSa/s", "4CH", "128Mpts"],
                "type": "dso",
            },
            {
                "model": "MDS-500",
                "name": "500MHz Mixed-Signal Oscilloscope",
                "desc": "MSO with 2 analog + 16 digital channels. Protocol decode: I2C, SPI, UART, CAN, LIN.",
                "features": ["500MHz", "2+16CH MSO", "Protocol Decode", "Logic Analyser"],
                "type": "mso",
            },
            {
                "model": "MDS-1G",
                "name": "1GHz High-Bandwidth Oscilloscope",
                "desc": "4-channel 1 GHz DSO with 5GSa/s, 250Mpts deep memory, and segmented acquisition.",
                "features": ["1GHz", "5GSa/s", "250Mpts", "Segmented Acq."],
                "type": "dso",
            },
            {
                "model": "MDO-200",
                "name": "Digital Oscilloscope + DMM",
                "desc": "Combo instrument: 200MHz oscilloscope + 6000-count multimeter sharing a single 8\" screen.",
                "features": ["200MHz", "DMM Built-in", "8\" Screen", "Portable"],
                "type": "combo",
            },
            {
                "model": "MHO-70",
                "name": "Handheld Oscilloscope 70MHz",
                "desc": "Rugged handheld 70MHz oscilloscope/multimeter for field use. Battery operated, IP51 rated.",
                "features": ["70MHz", "Handheld", "IP51 Rated", "Battery Op."],
                "type": "handheld",
            },
        ],
    },
]


def nav_links(active_id):
    links = [
        ("index.html", "Product Center", "home"),
        ("dc-power-supply.html", "DC Power Supply", "dc-power-supply"),
        ("ac-power-supply.html", "AC Power Supply", "ac-power-supply"),
        ("electronic-loads.html", "Electronic Loads", "electronic-loads"),
        ("lcr-meter.html", "LCR Meter", "lcr-meter"),
        ("withstand-voltage-tester.html", "Withstand Voltage Tester", "withstand-voltage-tester"),
        ("oscilloscope.html", "Oscilloscope", "oscilloscope"),
        ("all-products.html", "All Products", "all-products"),
    ]
    items = ""
    for href, label, lid in links:
        ac = ' class="active"' if lid == active_id else ""
        items += f'<li><a href="{href}"{ac}>{label}</a></li>\n'
    return items


def sidebar_nav(active_id):
    items = [
        ("dc-power-supply.html", "⚡", "DC Power Supply", "dc-power-supply"),
        ("ac-power-supply.html", "〜", "AC Power Supply", "ac-power-supply"),
        ("electronic-loads.html", "🔌", "Electronic Loads", "electronic-loads"),
        ("lcr-meter.html", "📡", "LCR Meter", "lcr-meter"),
        ("withstand-voltage-tester.html", "⚠", "Withstand Voltage Tester", "withstand-voltage-tester"),
        ("oscilloscope.html", "📊", "Oscilloscope", "oscilloscope"),
    ]
    out = ""
    for href, icon, label, lid in items:
        ac = " active" if lid == active_id else ""
        out += f"""<li><a href="{href}" class="{ac.strip()}"><span class="icon">{icon}</span>{label}</a></li>\n"""
    return out


def product_cards(cid, products):
    cards = ""
    for p in products:
        features_html = "".join(f'<span class="card-feature">{f}</span>' for f in p["features"])
        cards += f"""
<article class="product-card" data-type="{p['type']}">
  <div class="card-image">
    <img src="https://placehold.co/600x400/112040/00C2FF.png?text={p['model']}" alt="{p['name']}" style="width:100%; height:100%; object-fit:cover; opacity: 0.8;">
    <span class="card-badge">{p['type'].upper()}</span>
    <div class="card-image-overlay"></div>
  </div>
  <div class="card-body">
    <div class="card-model">{p['model']}</div>
    <h3 class="card-title">{p['name']}</h3>
    <p class="card-desc">{p['desc']}</p>
    <div class="card-features">{features_html}</div>
  </div>
  <div class="card-footer">
    <a href="#" class="btn-view"><i class="bi bi-eye"></i> View Details</a>
    <a href="#" class="btn-quote"><i class="bi bi-envelope"></i> Quote</a>
  </div>
</article>"""
    return cards


def footer_links():
    items = [
        ("dc-power-supply.html", "DC Power Supply"),
        ("ac-power-supply.html", "AC Power Supply"),
        ("electronic-loads.html", "Electronic Loads"),
        ("lcr-meter.html", "LCR Meter"),
        ("withstand-voltage-tester.html", "Withstand Voltage Tester"),
        ("oscilloscope.html", "Oscilloscope"),
        ("all-products.html", "All Products"),
    ]
    return "".join(f'<li><a href="{h}">{l}</a></li>' for h, l in items)


def generate_page(cat):
    cid = cat["id"]
    unique_types = list(dict.fromkeys(p["type"] for p in cat["products"]))
    filter_btns = '<button class="filter-btn active" data-filter="all">All</button>\n'
    for t in unique_types:
        label = t.title().replace("-", " ")
        filter_btns += f'<button class="filter-btn" data-filter="{t}">{label}</button>\n'

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{cat['name']} | MATRIX Technology Product Center</title>
  <meta name="description" content="Explore Matrix Technology's {cat['name']} range. {cat['tagline']}.">
  <link rel="stylesheet" href="awesome.css">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css" rel="stylesheet">
</head>
<body>

<!-- NAVBAR -->
<nav class="navbar">
  <div class="container">
    <a href="index.html" class="brand">
      <span class="brand-strips"><i></i><i></i><i></i></span>
      <span>MATRIX</span>
    </a>
    <ul class="nav-links">
      <li><a href="index.html">Product Center</a></li>
      <li class="nav-dropdown">
        <a href="#" class="active">Categories <svg class="chevron" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 6 8 10 12 6"/></svg></a>
        <ul class="dropdown-menu">
          <li><a href="dc-power-supply.html" {"class=\"active\"" if cid=="dc-power-supply" else ""}><span class="dropdown-icon">⚡</span> DC Power Supply</a></li>
          <li><a href="ac-power-supply.html" {"class=\"active\"" if cid=="ac-power-supply" else ""}><span class="dropdown-icon">〜</span> AC Power Supply</a></li>
          <li><a href="electronic-loads.html" {"class=\"active\"" if cid=="electronic-loads" else ""}><span class="dropdown-icon">🔌</span> Electronic Loads</a></li>
          <li><a href="lcr-meter.html" {"class=\"active\"" if cid=="lcr-meter" else ""}><span class="dropdown-icon">📡</span> LCR Meter</a></li>
          <li><a href="withstand-voltage-tester.html" {"class=\"active\"" if cid=="withstand-voltage-tester" else ""}><span class="dropdown-icon">⚠</span> Withstand Voltage Tester</a></li>
          <li><a href="oscilloscope.html" {"class=\"active\"" if cid=="oscilloscope" else ""}><span class="dropdown-icon">📊</span> Oscilloscope</a></li>
          <li><div class="divider"></div></li>
          <li><a href="all-products.html"><span class="dropdown-icon">🗂</span> All Products</a></li>
        </ul>
      </li>
      <li><a href="#">About</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
    <div class="nav-end">
      <button class="btn-nav-search" aria-label="Search"><i class="bi bi-search"></i></button>
      <a href="#" class="btn-contact-nav">Get Quote</a>
    </div>
    <button class="hamburger" id="hamburger" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>

<!-- Mobile Nav -->
<nav class="mobile-nav" id="mobileNav">
  <ul>
    <li><a href="index.html">Product Center</a></li>
    <li><a href="dc-power-supply.html" {"class=\"active\"" if cid=="dc-power-supply" else ""}>DC Power Supply</a></li>
    <li><a href="ac-power-supply.html" {"class=\"active\"" if cid=="ac-power-supply" else ""}>AC Power Supply</a></li>
    <li><a href="electronic-loads.html" {"class=\"active\"" if cid=="electronic-loads" else ""}>Electronic Loads</a></li>
    <li><a href="lcr-meter.html" {"class=\"active\"" if cid=="lcr-meter" else ""}>LCR Meter</a></li>
    <li><a href="withstand-voltage-tester.html" {"class=\"active\"" if cid=="withstand-voltage-tester" else ""}>Withstand Voltage Tester</a></li>
    <li><a href="oscilloscope.html" {"class=\"active\"" if cid=="oscilloscope" else ""}>Oscilloscope</a></li>
    <li><a href="all-products.html">All Products</a></li>
  </ul>
</nav>

<!-- PAGE WRAPPER -->
<div class="page-wrapper">

  <!-- BREADCRUMB -->
  <div class="breadcrumb-bar">
    <div class="container">
      <ol class="breadcrumb">
        <li><a href="index.html">Home</a></li>
        <li><a href="index.html">Product Center</a></li>
        <li class="active">{cat['name']}</li>
      </ol>
    </div>
  </div>

  <!-- MAIN LAYOUT -->
  <div class="layout-with-sidebar">

    <!-- SIDEBAR -->
    <aside class="sidebar" id="sidebar">
      <div class="sidebar-title">Product Center</div>
      <ul class="sidebar-nav">
        {sidebar_nav(cid)}
      </ul>
      <div class="sidebar-all">
        <ul class="sidebar-nav">
          <li><a href="all-products.html"><span class="icon">🗂</span> All Products</a></li>
        </ul>
      </div>
    </aside>

    <!-- CONTENT -->
    <main class="main-content">

      <!-- Mobile sidebar trigger -->
      <button class="sidebar-mobile-trigger" id="sidebarTrigger" style="display:none;">
        <i class="bi bi-layout-sidebar-inset"></i> Browse Categories
      </button>

      <!-- HERO -->
      <section class="product-hero">
        <div class="hero-grid-pattern"></div>
        <div class="product-hero-inner">
          <div class="hero-badge"><span class="dot"></span> {cat['badge_label']}</div>
          <h1>{cat['name'].split()[0]} <span class="highlight">{' '.join(cat['name'].split()[1:]) or cat['name'].split()[0]}</span></h1>
          <p>{cat['tagline']}. {cat['description'][:120]}...</p>
          <div class="hero-stats">
            <div class="hero-stat"><div class="num">{len(cat['products'])}</div><p class="lbl">Models</p></div>
            <div class="hero-stat"><div class="num">CE</div><p class="lbl">Certified</p></div>
            <div class="hero-stat"><div class="num">2yr</div><p class="lbl">Warranty</p></div>
          </div>
        </div>
      </section>

      <!-- PRODUCTS SECTION -->
      <section class="products-section">
        <div class="products-section-header">
          <div>
            <span class="section-label">Products</span>
            <h2 class="section-title">{cat['name']} Series</h2>
          </div>
          <div class="filter-bar">
            {filter_btns}
          </div>
        </div>

        <!-- Search -->
        <div class="search-bar-wrap">
          <div class="search-bar">
            <span class="si"><i class="bi bi-search"></i></span>
            <input type="text" id="productSearch" placeholder="Search {cat['name'].lower()} models…">
          </div>
        </div>

        <!-- Cards -->
        <div class="products-grid" style="margin-top:24px;">
          {product_cards(cat['id'], cat['products'])}
        </div>
      </section>

      <!-- CTA -->
      <div class="cta-section">
        <div class="cta-inner">
          <div>
            <h2>Need a Custom Solution?</h2>
            <p>Our engineers can tailor {cat['name']} specifications to your application requirements.</p>
          </div>
          <div class="cta-buttons">
            <a href="#" class="btn-primary"><i class="bi bi-envelope"></i> Request Quote</a>
            <a href="#" class="btn-outline"><i class="bi bi-file-earmark-text"></i> Download Catalog</a>
          </div>
        </div>
      </div>

    </main>
  </div><!-- /layout-with-sidebar -->

  <!-- FOOTER -->
  <footer>
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="index.html" class="brand" style="margin-bottom:14px;display:inline-flex;">
            <span class="brand-strips"><i></i><i></i><i></i></span>
            <span>MATRIX</span>
          </a>
          <p style="font-size:0.875rem;color:var(--text-muted);">Precision test &amp; measurement instruments trusted by engineers worldwide.</p>
          <div class="footer-social" style="margin-top:16px;">
            <a href="#" class="social-icon"><i class="bi bi-facebook"></i></a>
            <a href="#" class="social-icon"><i class="bi bi-youtube"></i></a>
            <a href="#" class="social-icon"><i class="bi bi-linkedin"></i></a>
            <a href="#" class="social-icon"><i class="bi bi-envelope"></i></a>
          </div>
        </div>
        <div>
          <div class="footer-col-title">Products</div>
          <ul class="footer-links">
            {footer_links()}
          </ul>
        </div>
        <div>
          <div class="footer-col-title">Company</div>
          <ul class="footer-links">
            <li><a href="#">About Us</a></li>
            <li><a href="#">FAQ</a></li>
            <li><a href="#">Videos</a></li>
            <li><a href="#">Privacy Policy</a></li>
          </ul>
        </div>
        <div>
          <div class="footer-col-title">Contact</div>
          <div class="footer-contact-item"><span class="ic"><i class="bi bi-geo-alt"></i></span><span>Room 601, Block C, Huachuangda Industrial Park, Shenzhen, Guangdong</span></div>
          <div class="footer-contact-item"><span class="ic"><i class="bi bi-telephone"></i></span><span>0086 755 2836 4276</span></div>
          <div class="footer-contact-item"><span class="ic"><i class="bi bi-envelope"></i></span><span>sales@szmatrix.com</span></div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2025 MATRIX Technology Inc. All rights reserved.</p>
        <div style="display:flex;gap:16px;">
          <a href="#">Privacy</a>
          <a href="#">Terms</a>
        </div>
      </div>
    </div>
  </footer>

  <a href="#" class="floating-contact"><i class="bi bi-chat-fill"></i> Contact us</a>
</div><!-- /page-wrapper -->

<script src="main.js"></script>
</body>
</html>
"""

    html = '{% load static %}\n' + html
    html = html.replace('href="awesome.css"', 'href="{% static \'css/awesome.css\' %}"')
    html = html.replace('src="main.js"', 'src="{% static \'js/product_main.js\' %}"')
    for p in ['index', 'dc-power-supply', 'ac-power-supply', 'electronic-loads', 'lcr-meter', 'withstand-voltage-tester', 'oscilloscope', 'all-products']:
        html = html.replace(f'href="{p}.html"', f'href="{{% url \'products:center_page\' page_name=\'{p}\' %}}"')
    return html

    html = '{% load static %}\n' + html
    html = html.replace('href="awesome.css"', 'href="{% static \'css/awesome.css\' %}"')
    html = html.replace('src="main.js"', 'src="{% static \'js/product_main.js\' %}"')
    for p in ['index', 'dc-power-supply', 'ac-power-supply', 'electronic-loads', 'lcr-meter', 'withstand-voltage-tester', 'oscilloscope', 'all-products']:
        html = html.replace(f'href="{p}.html"', f'href="{{% url \'products:center_page\' page_name=\'{p}\' %}}"')
    return html


# ── All Products page ──────────────────────────────────────────────────────
def generate_all_products():
    tab_items = ""
    all_cards = ""
    for cat in CATEGORIES:
        tab_items += f'<a href="#{cat["id"]}" class="cat-tab" data-cat="{cat["id"]}">{cat["emoji"]} {cat["name"]} <span class="count">{len(cat["products"])}</span></a>\n'
    tab_items = f'<a href="#all" class="cat-tab active" data-cat="all">🗂 All Products <span class="count">{sum(len(c["products"]) for c in CATEGORIES)}</span></a>\n' + tab_items

    for cat in CATEGORIES:
        for p in cat["products"]:
            features_html = "".join(f'<span class="card-feature">{f}</span>' for f in p["features"])
            all_cards += f"""
<article class="product-card" data-type="{p['type']}" data-cat="{cat['id']}">
  <div class="card-image">
    <img src="https://placehold.co/600x400/112040/00C2FF.png?text={p['model']}" alt="{p['name']}" style="width:100%; height:100%; object-fit:cover; opacity: 0.8;">
    <span class="card-badge">{cat['emoji']}</span>
    <div class="card-image-overlay"></div>
  </div>
  <div class="card-body">
    <div class="card-model">{p['model']}</div>
    <h3 class="card-title">{p['name']}</h3>
    <p class="card-desc">{p['desc']}</p>
    <div class="card-features">{features_html}</div>
    <div style="font-size:0.72rem;color:var(--text-muted);margin-top:4px;">{cat['name']}</div>
  </div>
  <div class="card-footer">
    <a href="{cat['id']}.html" class="btn-view"><i class="bi bi-eye"></i> View Details</a>
    <a href="#" class="btn-quote"><i class="bi bi-envelope"></i> Quote</a>
  </div>
</article>"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>All Products | MATRIX Technology Product Center</title>
  <link rel="stylesheet" href="awesome.css">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css" rel="stylesheet">
</head>
<body>

<nav class="navbar">
  <div class="container">
    <a href="index.html" class="brand">
      <span class="brand-strips"><i></i><i></i><i></i></span>
      <span>MATRIX</span>
    </a>
    <ul class="nav-links">
      <li><a href="index.html">Product Center</a></li>
      <li class="nav-dropdown">
        <a href="#" class="active">Categories <svg class="chevron" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 6 8 10 12 6"/></svg></a>
        <ul class="dropdown-menu">
          <li><a href="dc-power-supply.html"><span class="dropdown-icon">⚡</span> DC Power Supply</a></li>
          <li><a href="ac-power-supply.html"><span class="dropdown-icon">〜</span> AC Power Supply</a></li>
          <li><a href="electronic-loads.html"><span class="dropdown-icon">🔌</span> Electronic Loads</a></li>
          <li><a href="lcr-meter.html"><span class="dropdown-icon">📡</span> LCR Meter</a></li>
          <li><a href="withstand-voltage-tester.html"><span class="dropdown-icon">⚠</span> Withstand Voltage Tester</a></li>
          <li><a href="oscilloscope.html"><span class="dropdown-icon">📊</span> Oscilloscope</a></li>
          <li><div class="divider"></div></li>
          <li><a href="all-products.html" class="active"><span class="dropdown-icon">🗂</span> All Products</a></li>
        </ul>
      </li>
      <li><a href="#">About</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
    <div class="nav-end">
      <button class="btn-nav-search"><i class="bi bi-search"></i></button>
      <a href="#" class="btn-contact-nav">Get Quote</a>
    </div>
    <button class="hamburger" id="hamburger" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>
<nav class="mobile-nav" id="mobileNav">
  <ul>
    <li><a href="index.html">Product Center</a></li>
    <li><a href="dc-power-supply.html">DC Power Supply</a></li>
    <li><a href="ac-power-supply.html">AC Power Supply</a></li>
    <li><a href="electronic-loads.html">Electronic Loads</a></li>
    <li><a href="lcr-meter.html">LCR Meter</a></li>
    <li><a href="withstand-voltage-tester.html">Withstand Voltage Tester</a></li>
    <li><a href="oscilloscope.html">Oscilloscope</a></li>
    <li><a href="all-products.html" class="active">All Products</a></li>
  </ul>
</nav>

<div class="page-wrapper">
  <div class="breadcrumb-bar">
    <div class="container">
      <ol class="breadcrumb">
        <li><a href="index.html">Home</a></li>
        <li><a href="index.html">Product Center</a></li>
        <li class="active">All Products</li>
      </ol>
    </div>
  </div>

  <!-- HERO -->
  <section class="product-hero">
    <div class="hero-grid-pattern"></div>
    <div class="product-hero-inner">
      <div class="hero-badge"><span class="dot"></span> Complete Product Catalog</div>
      <h1>All <span class="highlight">Products</span></h1>
      <p>Browse our complete range of precision test and measurement instruments across all categories.</p>
      <div class="hero-stats">
        <div class="hero-stat"><div class="num">{sum(len(c['products']) for c in CATEGORIES)}</div><p class="lbl">Total Models</p></div>
        <div class="hero-stat"><div class="num">{len(CATEGORIES)}</div><p class="lbl">Categories</p></div>
        <div class="hero-stat"><div class="num">CE</div><p class="lbl">Certified</p></div>
      </div>
    </div>
  </section>

  <!-- CATEGORY TABS -->
  <div class="category-tabs">
    {tab_items}
  </div>

  <!-- SEARCH -->
  <div class="search-bar-wrap">
    <div class="search-bar">
      <span class="si"><i class="bi bi-search"></i></span>
      <input type="text" id="productSearch" placeholder="Search all products, models, features…">
    </div>
  </div>

  <!-- PRODUCTS GRID -->
  <section class="products-section">
    <div class="products-grid">
      {all_cards}
    </div>
  </section>

  <footer>
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="index.html" class="brand" style="margin-bottom:14px;display:inline-flex;">
            <span class="brand-strips"><i></i><i></i><i></i></span>
            <span>MATRIX</span>
          </a>
          <p style="font-size:0.875rem;color:var(--text-muted);">Precision test &amp; measurement instruments trusted worldwide.</p>
        </div>
        <div>
          <div class="footer-col-title">Products</div>
          <ul class="footer-links">
            {footer_links()}
          </ul>
        </div>
        <div>
          <div class="footer-col-title">Company</div>
          <ul class="footer-links">
            <li><a href="#">About Us</a></li>
            <li><a href="#">FAQ</a></li>
          </ul>
        </div>
        <div>
          <div class="footer-col-title">Contact</div>
          <div class="footer-contact-item"><span class="ic"><i class="bi bi-telephone"></i></span><span>0086 755 2836 4276</span></div>
          <div class="footer-contact-item"><span class="ic"><i class="bi bi-envelope"></i></span><span>sales@szmatrix.com</span></div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2025 MATRIX Technology Inc. All rights reserved.</p>
      </div>
    </div>
  </footer>
  <a href="#" class="floating-contact"><i class="bi bi-chat-fill"></i> Contact us</a>
</div>

<script src="main.js"></script>
<script>
  // Category tab filter
  document.querySelectorAll('.cat-tab').forEach(tab => {{
    tab.addEventListener('click', function(e) {{
      e.preventDefault();
      document.querySelectorAll('.cat-tab').forEach(t => t.classList.remove('active'));
      this.classList.add('active');
      const cat = this.dataset.cat;
      document.querySelectorAll('.product-card').forEach(card => {{
        card.style.display = (cat === 'all' || card.dataset.cat === cat) ? '' : 'none';
      }});
    }});
  }});
</script>
</body>
</html>
"""

    html = '{% load static %}\n' + html
    html = html.replace('href="awesome.css"', 'href="{% static \'css/awesome.css\' %}"')
    html = html.replace('src="main.js"', 'src="{% static \'js/product_main.js\' %}"')
    for p in ['index', 'dc-power-supply', 'ac-power-supply', 'electronic-loads', 'lcr-meter', 'withstand-voltage-tester', 'oscilloscope', 'all-products']:
        html = html.replace(f'href="{p}.html"', f'href="{{% url \'products:center_page\' page_name=\'{p}\' %}}"')
    return html


import os
IMAGES_MAP = {
    "dc-power-supply": "https://www.szmatrix.com/wp-content/uploads/2025/07/\u6444\u56fe\u7f51_401758474_\u79d1\u6280\u667a\u80fd\u975e\u4f01\u4e1a\u5546\u7528-1024x683.jpg",
    "ac-power-supply": "https://www.szmatrix.com/wp-content/uploads/2025/07/\u6444\u56fe\u7f51_401758474_\u79d1\u6280\u667a\u80fd\u975e\u4f01\u4e1a\u5546\u7528-1024x683.jpg",
    "electronic-loads": "https://www.szmatrix.com/wp-content/uploads/2025/07/\u6444\u56fe\u7f51_401758474_\u79d1\u6280\u667a\u80fd\u975e\u4f01\u4e1a\u5546\u7528-1024x683.jpg",
    "lcr-meter": "https://www.szmatrix.com/wp-content/uploads/2025/07/\u6444\u56fe\u7f51_401758474_\u79d1\u6280\u667a\u80fd\u975e\u4f01\u4e1a\u5546\u7528-1024x683.jpg",
    "withstand-voltage-tester": "https://www.szmatrix.com/wp-content/uploads/2020/12/logo-2.png",
    "oscilloscope": "https://www.szmatrix.com/wp-content/uploads/2020/12/logo-2.png",
    "all-products": "https://www.szmatrix.com/wp-content/uploads/2020/12/logo-2.png"
}

OUT_DIR = "../templates/product-center"
os.makedirs(OUT_DIR, exist_ok=True)

for cat in CATEGORIES:
    fname = f"{cat['id']}.html"
    path = os.path.join(OUT_DIR, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(generate_page(cat))
    print(f"✅ {fname}")

all_path = os.path.join(OUT_DIR, "all-products.html")
with open(all_path, "w", encoding="utf-8") as f:
    f.write(generate_all_products())
print("✅ all-products.html")

print("\n🎉 All pages generated!")
