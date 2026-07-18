#!/usr/bin/env python3
"""
Generates the individual service landing pages under services/ from the data
below, so every page shares the exact same header, footer, nav and styling.

Run:  python3 build_services.py
Edit content by changing the SERVICES list, then re-run.
"""
import os

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "services")

# (label used in nav/dropdown, slug)
CHIMNEY = [
    ("Chimney Cleaning", "chimney-cleaning"),
    ("Chimney Inspection", "chimney-inspection"),
    ("Installation & Repair", "chimney-installation-repair"),
    ("Chimney Liner Installation", "chimney-liner-installation"),
    ("Waterproofing & Sealing", "chimney-waterproofing-sealing"),
    ("Damper Caps & Chase Covers", "damper-caps-chase-covers"),
    ("Fireplace Masonry & Repair", "fireplace-masonry-repair"),
    ("Flashing Repair", "flashing-repair"),
]
RELATED = [
    ("Foundation Waterproofing & Repair", "foundation-waterproofing-repair"),
    ("Heating System Liner Services", "heating-system-liner-services"),
    ("Pellet Stove Cleaning & Install", "pellet-stove-cleaning-installation"),
    ("Stone Wall Repair", "stone-wall-repair"),
    ("Wood Stove Cleaning & Install", "wood-stove-cleaning-installation"),
]

# Full content for each page, keyed by slug.
SERVICES = {
  "chimney-cleaning": dict(
    title="Chimney Cleaning", cat="chimney", icon="🧹",
    lead="Professional creosote and debris removal that keeps your fireplace safe, efficient, and ready to burn.",
    intro=[
      "Every fire you burn leaves creosote and debris behind inside your flue. Over time that buildup restricts airflow and becomes a serious fire hazard. Our CSIA-certified technicians remove it completely, then confirm your chimney is venting the way it should.",
      "We work cleanly and respectfully, protecting your floors and furniture and leaving no mess behind, just a chimney that's ready for the season.",
    ],
    why="Why regular cleaning matters",
    features=[
      ("🔥","Prevents chimney fires","Creosote is highly flammable and builds with every fire. Removing it is the single best way to prevent a destructive chimney fire."),
      ("🌬️","Protects your air","A clear flue lets dangerous carbon monoxide escape safely instead of backing up into your home."),
      ("♨️","Better efficiency","A clean chimney drafts properly, so your fireplace or stove heats better and burns cleaner."),
      ("🛡️","Longer lifespan","Routine cleaning prevents corrosive buildup that shortens the life of your chimney."),
    ],
    list_title="Signs it's time for a cleaning",
    items=["Thick black or shiny residue inside the flue","Smoke pushing back into the room","A strong odor coming from the fireplace","Trouble starting or keeping a fire going","Visible soot or creosote buildup","Animals or nesting in the chimney","It's been over a year since your last cleaning"],
    steps=[("Inspection first","We look over your chimney and flue so we know exactly what we're dealing with."),("Protect the space","Drop cloths and a sealed vacuum keep soot out of your home."),("Sweep & remove","Specialized brushes and rods clear creosote and debris top to bottom."),("Final check","We confirm the flue is clear and venting properly before we pack up.")],
    photo="Chimney cleaning in progress"),

  "chimney-inspection": dict(
    title="Chimney Inspection", cat="chimney", icon="🔍",
    lead="Thorough, certified inspections that catch small problems before they turn into expensive ones.",
    intro=[
      "A chimney can look fine from the ground and still hide cracks, blockages, or worn liners that put your home at risk. Our detailed inspections check the structure, flue, and connections inside and out.",
      "You get a clear, honest report of what we find, with straightforward recommendations and no scare tactics.",
    ],
    why="Why inspections matter",
    features=[
      ("🔍","Catch issues early","Small cracks and gaps are cheap to fix now and costly to ignore."),
      ("🏠","Buying or selling","Ideal before a home sale, or after a chimney fire or major storm."),
      ("🧯","Safety first","We verify your chimney vents safely and meets code."),
      ("📋","Clear documentation","A written summary you can keep for insurance or resale."),
    ],
    list_title="When you should schedule one",
    items=["Every year, before the heating season","Before buying or selling a home","After a chimney fire, storm, or earthquake","When adding or replacing a heating appliance","If you notice draft, odor, or moisture problems","If the chimney has never been inspected"],
    steps=[("Exterior review","We assess the crown, cap, masonry, and flashing from outside."),("Interior & flue","We check the firebox, damper, and flue for cracks, blockages, and buildup."),("Document findings","Everything is noted, with photos where they help."),("Walk you through it","We explain what we found and what, if anything, needs attention.")],
    photo="Technician inspecting a flue"),

  "chimney-installation-repair": dict(
    title="Chimney Installation & Repair", cat="chimney", icon="🧱",
    lead="Expert installation and repair that restores your chimney's safety, function, and curb appeal.",
    intro=[
      "Whether you're adding a new chimney, replacing worn components, or fixing damage from age and weather, we handle it with skilled craftsmanship and quality materials.",
      "From full rebuilds to targeted repairs, we make sure the finished work is safe, code-compliant, and built to last.",
    ],
    why="What we handle",
    features=[
      ("🧱","Rebuilds & repairs","Cracked, crumbling, or leaning masonry rebuilt to be sound and square."),
      ("🎩","Crowns & caps","Repair or replace the crown and cap that protect the top of your chimney."),
      ("🔧","Component replacement","Dampers, liners, and hardware swapped for quality parts."),
      ("🏗️","New installations","Complete chimney installation done right the first time."),
    ],
    list_title="Common signs of chimney damage",
    items=["Crumbling or missing mortar joints","Cracked or flaking (spalling) bricks","White staining on the masonry","A leaning or tilting chimney","Rust on the damper or firebox","Pieces of masonry in the firebox or on the roof"],
    steps=[("Assess","We inspect the full structure to scope exactly what's needed."),("Quote clearly","You get an honest, itemized estimate up front."),("Do the work","Skilled repairs or installation with quality materials."),("Guarantee it","Every job is backed by our workmanship guarantee.")],
    photo="Masonry chimney repair"),

  "chimney-liner-installation": dict(
    title="Chimney Liner Installation", cat="chimney", icon="🛡️",
    lead="Stainless steel liners sized and installed to protect your flue and improve draft and efficiency.",
    intro=[
      "The liner safely channels heat, smoke, and gases up and out of your home. A cracked, undersized, or missing liner is a real safety risk and hurts performance.",
      "We install code-compliant stainless steel liners sized precisely to your appliance, so your system drafts cleanly and vents safely.",
    ],
    why="Why the liner matters",
    features=[
      ("🛡️","Protects your home","Contains heat and gases so they can't reach nearby framing."),
      ("♨️","Improves draft","A correctly sized liner helps your fireplace or stove burn efficiently."),
      ("🧪","Resists corrosion","Stainless steel stands up to acidic combustion byproducts."),
      ("✅","Meets code","Required for many appliance installs and safety upgrades."),
    ],
    list_title="You may need a new liner if",
    items=["Your chimney has no liner or a damaged clay-tile liner","You're installing a new stove, insert, or furnace","An inspection found cracks or gaps in the flue","You've had a chimney fire","Your appliance and flue sizes don't match"],
    steps=[("Measure","We size the liner precisely to your appliance and flue."),("Prep the flue","The chimney is cleared and prepared for the new liner."),("Install","The stainless liner is set, connected, and insulated as needed."),("Verify","We confirm a safe, proper connection top to bottom.")],
    photo="Stainless liner installation"),

  "chimney-waterproofing-sealing": dict(
    title="Chimney Waterproofing & Sealing", cat="chimney", icon="💧",
    lead="Breathable sealants that lock out the moisture responsible for most chimney damage.",
    intro=[
      "Water is the number one enemy of masonry. Freeze-thaw cycles crack bricks and crumble mortar, and the damage only accelerates once it starts.",
      "We apply a breathable, industrial-grade sealant that keeps water out while letting the masonry release vapor, protecting your chimney for years.",
    ],
    why="Why waterproofing pays off",
    features=[
      ("💧","Stops water damage","Blocks the moisture that causes cracking and spalling."),
      ("❄️","Beats freeze-thaw","Prevents absorbed water from freezing and breaking apart brick."),
      ("🌬️","Breathable protection","Keeps water out while letting trapped vapor escape."),
      ("💵","Protects your investment","A small step now prevents costly masonry repairs later."),
    ],
    list_title="Consider sealing if",
    items=["Your chimney has never been waterproofed","You see white staining (efflorescence)","Mortar joints are starting to erode","You've had masonry repairs you want to protect","Your chimney takes heavy weather exposure"],
    steps=[("Inspect & clean","The masonry is checked and cleaned so the sealant bonds well."),("Repair first","Any open cracks or joints are addressed before sealing."),("Apply sealant","A breathable waterproofing agent is applied evenly."),("Seal the crown","We can treat the crown and joints for full coverage.")],
    photo="Applying chimney sealant"),

  "damper-caps-chase-covers": dict(
    title="Damper Caps & Chase Covers", cat="chimney", icon="🎩",
    lead="Custom caps and covers that keep rain, animals, and debris out of your chimney for good.",
    intro=[
      "The top of your chimney is its most vulnerable point. Without a proper cap or chase cover, water, leaves, and animals get straight in, leading to blockages, odors, and interior damage.",
      "We fit quality caps and custom chase covers that seal the top of your chimney while still letting it vent freely.",
    ],
    why="What they protect against",
    features=[
      ("🌧️","Rain & moisture","Keeps water out of the flue and off interior components."),
      ("🐿️","Animals & nests","Stops birds, squirrels, and raccoons from moving in."),
      ("🍂","Leaves & debris","Prevents blockages that hurt draft and safety."),
      ("🔥","Stray sparks","A spark-arresting cap helps keep embers off your roof."),
    ],
    list_title="Signs you need a cap or cover",
    items=["No cap, or a rusted and damaged existing cap","Water or moisture inside the firebox","Animals or nesting sounds in the chimney","Debris falling into the fireplace","A rusted or ill-fitting chase cover on a prefab chimney"],
    steps=[("Measure the flue","We size the cap or chase cover to your exact chimney."),("Choose materials","Durable stainless or galvanized options to fit your needs."),("Install securely","Fitted and fastened to stay put through the seasons."),("Confirm venting","We make sure it protects without restricting draft.")],
    photo="Chimney cap installation"),

  "fireplace-masonry-repair": dict(
    title="Fireplace Masonry & Repair", cat="chimney", icon="🔥",
    lead="Skilled brick, block, and mortar work to rebuild and beautify your fireplace and chimney.",
    intro=[
      "Masonry takes a beating from heat, weather, and time. Crumbling mortar, cracked brick, and a worn firebox aren't just cosmetic, they affect safety and performance.",
      "Our masons repair and rebuild fireplaces and chimneys with craftsmanship that looks great and holds up for the long haul.",
    ],
    why="What we restore",
    features=[
      ("🧱","Tuckpointing","Worn mortar joints ground out and repacked for strength."),
      ("🔥","Firebox repair","Cracked firebrick and mortar restored to burn safely."),
      ("🏛️","Rebuilds","Damaged sections rebuilt to match your existing masonry."),
      ("✨","Restoration","Cleaning and repair that brings tired masonry back to life."),
    ],
    list_title="Signs your masonry needs work",
    items=["Gaps or crumbling in the mortar joints","Cracked, chipped, or flaking bricks","Cracks in the firebox or hearth","White efflorescence staining","Loose or missing pieces of brick","A rough, uneven, or damaged appearance"],
    steps=[("Evaluate","We assess the masonry to plan the right repair."),("Match materials","Brick and mortar matched to your existing look."),("Restore","Careful tuckpointing, repair, or rebuild as needed."),("Finish clean","We leave the work tidy and looking sharp.")],
    photo="Fireplace masonry work"),

  "flashing-repair": dict(
    title="Flashing Repair", cat="chimney", icon="⚡",
    lead="Watertight flashing repair where your chimney meets the roof, stopping leaks at the source.",
    intro=[
      "Flashing is the metal seal between your chimney and roof. When it fails, water sneaks in around the chimney base and causes leaks, stains, and rot that are often blamed on the roof.",
      "We repair and reseal flashing so the connection is watertight again, protecting your ceilings, walls, and framing.",
    ],
    why="Why flashing matters",
    features=[
      ("💧","Stops leaks","Seals the most common spot water enters around a chimney."),
      ("🪵","Protects framing","Prevents hidden rot in the roof deck and structure."),
      ("🎨","Saves interiors","Avoids ceiling and wall stains from slow leaks."),
      ("🛡️","Long-lasting seal","Quality materials that hold up to weather."),
    ],
    list_title="Signs of failing flashing",
    items=["Water stains on ceilings or walls near the chimney","Dampness in the attic around the chimney base","Rusted, lifted, or missing flashing metal","Dried, cracked sealant at the roofline","Leaks that show up after heavy rain"],
    steps=[("Locate the leak","We find exactly where water is getting in."),("Remove old flashing","Failed metal and sealant are cleared away."),("Install new flashing","Fresh, properly layered flashing is fitted and sealed."),("Test & seal","We make sure the connection is fully watertight.")],
    photo="Chimney flashing repair"),

  "foundation-waterproofing-repair": dict(
    title="Foundation Waterproofing & Repair", cat="related", icon="🏠",
    lead="Keep water out of your foundation to protect the structure your whole home stands on.",
    intro=[
      "Water in a foundation leads to cracks, leaks, mold, and settling that threaten the entire house. Catching and sealing it early saves major structural headaches.",
      "We waterproof and repair foundations to keep basements and crawlspaces dry and your home solid from the ground up.",
    ],
    why="Why it matters",
    features=[
      ("🏠","Protects the structure","A dry foundation is a stable, long-lasting foundation."),
      ("🍄","Prevents mold","Keeps out the moisture that leads to mold and musty air."),
      ("💧","Dry basement","Stops seepage and leaks into living and storage space."),
      ("💵","Preserves value","Foundation problems are among the costliest to ignore."),
    ],
    list_title="Warning signs",
    items=["Cracks in foundation walls or floor","Water or dampness in the basement","Musty odors or visible mold","White mineral staining on walls","Bowing or leaning foundation walls","Pooling water around the foundation"],
    steps=[("Assess","We locate the source of water intrusion."),("Repair","Cracks and weak points are sealed and reinforced."),("Waterproof","Protective sealing keeps moisture out."),("Protect","Recommendations to keep it dry long term.")],
    photo="Foundation waterproofing"),

  "heating-system-liner-services": dict(
    title="Heating System Liner Services", cat="related", icon="♨️",
    lead="Proper liners for your furnace, boiler, or water heater venting, sized and installed for safe operation.",
    intro=[
      "Your heating appliances vent combustion gases through the chimney just like a fireplace does. An improperly sized or deteriorated liner can let dangerous gases back up into your home.",
      "We install and service heating system liners so your furnace, boiler, or water heater vents safely and efficiently.",
    ],
    why="Why it matters",
    features=[
      ("🧯","Safe venting","Keeps carbon monoxide and combustion gases moving out, not in."),
      ("♨️","Right-sized","A liner matched to your appliance for proper draft."),
      ("🧪","Corrosion resistant","Stands up to the acidic flue gases of modern appliances."),
      ("✅","Code compliant","Meets requirements for safe appliance venting."),
    ],
    list_title="You may need liner service if",
    items=["You're installing a new furnace, boiler, or water heater","Your appliance was upgraded to a higher-efficiency model","An inspection found a damaged or oversized flue","You notice odors or backdrafting near appliances","Your existing liner is corroded or deteriorating"],
    steps=[("Evaluate","We check your appliance and flue to size the liner correctly."),("Prep","The chimney is cleared and readied."),("Install","A properly sized, corrosion-resistant liner is fitted."),("Verify","We confirm safe, proper venting.")],
    photo="Heating system liner"),

  "pellet-stove-cleaning-installation": dict(
    title="Pellet Stove Cleaning & Installation", cat="related", icon="🌾",
    lead="Expert pellet stove installation and thorough cleaning to keep it running safely and efficiently.",
    intro=[
      "Pellet stoves are efficient and clean-burning, but they need regular cleaning to run their best, and correct installation to run safely.",
      "We install new pellet stoves and provide detailed cleaning and maintenance so yours stays reliable all season.",
    ],
    why="Why service matters",
    features=[
      ("🌾","Efficient heat","A clean stove burns pellets efficiently and puts out more heat."),
      ("🧯","Safe operation","Proper venting and cleaning prevent hazards."),
      ("🔧","Fewer breakdowns","Routine maintenance prevents mid-winter failures."),
      ("🛠️","Correct install","Set up to manufacturer and code requirements."),
    ],
    list_title="What we handle",
    items=["New pellet stove installation","Full seasonal cleaning and maintenance","Venting and exhaust cleaning","Ash and clinker removal","Inspection of gaskets and components","Troubleshooting performance issues"],
    steps=[("Assess","We review your stove or install location."),("Install or clean","New setup, or a thorough top-to-bottom cleaning."),("Check venting","Exhaust and intake verified for safe operation."),("Test run","We confirm it's running efficiently before we leave.")],
    photo="Pellet stove service"),

  "stone-wall-repair": dict(
    title="Stone Wall Repair", cat="related", icon="🪨",
    lead="Skilled repair and rebuilding of stone walls that restores both strength and character.",
    intro=[
      "Stone walls are beautiful and durable, but time, weather, and shifting ground eventually loosen stones and crumble mortar.",
      "Our masons repair and rebuild stone walls with an eye for craftsmanship, keeping the original character while making them solid again.",
    ],
    why="What we do",
    features=[
      ("🪨","Repointing","Failed mortar raked out and repacked to hold stones firm."),
      ("🧱","Resetting stones","Loose or fallen stones reset properly."),
      ("🏛️","Rebuilds","Collapsed sections rebuilt to match the original."),
      ("✨","Restoration","Cleaning and repair that revives the look."),
    ],
    list_title="Signs your wall needs attention",
    items=["Loose, shifting, or fallen stones","Crumbling or missing mortar","Leaning or bulging sections","Cracks running through the wall","Water pooling or drainage issues","General wear taking away from the look"],
    steps=[("Assess","We evaluate the wall's condition and the cause of damage."),("Match materials","Stone and mortar matched to the original."),("Repair or rebuild","Careful resetting, repointing, or rebuilding."),("Finish","Cleaned up and left looking its best.")],
    photo="Stone wall repair"),

  "wood-stove-cleaning-installation": dict(
    title="Wood Stove Cleaning & Installation", cat="related", icon="🪵",
    lead="Safe wood stove installation and deep cleaning to keep the heat coming and the risks out.",
    intro=[
      "A wood stove is a great source of heat, but creosote buildup and improper installation are real fire risks.",
      "We install wood stoves to code and provide thorough cleaning so yours burns safely and efficiently all winter.",
    ],
    why="Why it matters",
    features=[
      ("🪵","Efficient burning","A clean stove and flue draft properly and heat better."),
      ("🔥","Fire safety","Removing creosote prevents dangerous flue fires."),
      ("🧯","Safe venting","Proper install and clearances keep your home protected."),
      ("🛠️","Done right","Installed to manufacturer and code standards."),
    ],
    list_title="What we handle",
    items=["New wood stove installation","Full creosote cleaning of the stove and flue","Venting and connector pipe cleaning","Inspection of gaskets, bricks, and seals","Proper clearances and hearth protection","Draft and performance troubleshooting"],
    steps=[("Assess","We review the stove or planned install location."),("Install or clean","Code-compliant setup, or a thorough cleaning."),("Inspect venting","Flue and connectors checked for safe operation."),("Confirm","We verify a safe, efficient burn before finishing.")],
    photo="Wood stove service"),
}

PHONE_TEL = "19783207778"

def dropdown_items(items, active_slug):
    rows = []
    for label, slug in items:
        cur = ' class="is-current"' if slug == active_slug else ""
        rows.append(f'              <a href="{slug}.html"{cur}>{label}</a>')
    return "\n".join(rows)

def aside_links(items, active_slug):
    rows = []
    for label, slug in items:
        cur = ' class="is-current"' if slug == active_slug else ""
        rows.append(f'          <a href="{slug}.html"{cur}>{label}</a>')
    return "\n".join(rows)

def build_page(slug, data):
    cat = data["cat"]
    same_cat = CHIMNEY if cat == "chimney" else RELATED
    cat_label = "Chimney Services" if cat == "chimney" else "Related Services"
    cat_anchor = "services" if cat == "chimney" else "related"

    features_html = "\n".join(
        f'''          <article class="feature-card reveal">
            <div class="ico-badge">{ic}</div>
            <h3>{t}</h3>
            <p>{p}</p>
          </article>''' for ic, t, p in data["features"])

    items_html = "\n".join(
        f'          <li><span class="check"></span> {it}</li>' for it in data["items"])

    steps_html = "\n".join(
        f'''          <div class="step reveal">
            <h3>{t}</h3>
            <p>{p}</p>
          </div>''' for t, p in data["steps"])

    intro_html = "\n          ".join(f"<p>{p}</p>" for p in data["intro"])

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{data["title"]} | Sam &amp; Ivan The Chimney Guys — MA &amp; NH</title>
  <meta name="description" content="{data["lead"]} Sam & Ivan The Chimney Guys, CSIA-certified and serving Massachusetts & New Hampshire. Free estimates, 24/7 emergency service." />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../styles.css?v=3" />
</head>
<body>

  <div class="topbar" id="topbar">
    <div class="container topbar__inner">
      <div class="topbar__left">
        <span class="topbar__item"><svg viewBox="0 0 24 24" class="ico"><path d="M6.6 10.8a15.5 15.5 0 006.6 6.6l2.2-2.2a1 1 0 011-.24 11.3 11.3 0 003.5.56 1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1 11.3 11.3 0 00.56 3.5 1 1 0 01-.24 1z"/></svg>
          <a href="tel:19783207778">978-320-7778</a> <span class="topbar__sep">/</span> <a href="tel:19785903904">978-590-3904</a>
        </span>
        <span class="topbar__item topbar__hide"><svg viewBox="0 0 24 24" class="ico"><path d="M12 2a10 10 0 100 20 10 10 0 000-20zm1 10.4l4 2.3-.8 1.3-4.7-2.7V6h1.5z"/></svg>Mon-Sat 7:30am-5:30pm</span>
      </div>
      <div class="topbar__right">
        <span class="topbar__badge">Emergency Service 24/7/365</span>
      </div>
    </div>
  </div>

  <header class="header" id="header">
    <div class="container header__inner">
      <a href="../index.html#home" class="brand" aria-label="Sam and Ivan The Chimney Guys home">
        <img src="../images/logo-badge.jpg" alt="Sam &amp; Ivan Chimney Guys logo" class="brand__logo" />
        <span class="brand__text">
          <span class="brand__name">SAM &amp; IVAN</span>
          <span class="brand__sub">CHIMNEY GUYS</span>
        </span>
      </a>

      <nav class="nav" id="nav">
        <ul class="nav__list">
          <li><a href="../index.html#home" class="nav__link">Home</a></li>
          <li class="has-dropdown">
            <a href="../index.html#services" class="nav__link">Chimney Services <span class="caret"></span></a>
            <div class="dropdown">
{dropdown_items(CHIMNEY, slug)}
            </div>
          </li>
          <li class="has-dropdown">
            <a href="../index.html#related" class="nav__link">Related Services <span class="caret"></span></a>
            <div class="dropdown">
{dropdown_items(RELATED, slug)}
            </div>
          </li>
          <li><a href="../index.html#about" class="nav__link">About</a></li>
          <li><a href="../index.html#gallery" class="nav__link">Gallery</a></li>
          <li><a href="../index.html#areas" class="nav__link">Service Area</a></li>
          <li><a href="../index.html#contact" class="nav__link">Contact</a></li>
        </ul>
      </nav>

      <a href="../index.html#contact" class="btn btn--primary header__cta">Free Estimate</a>

      <button class="hamburger" id="hamburger" aria-label="Open menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <div class="mobile-menu" id="mobileMenu">
    <a href="../index.html#home">Home</a>
    <a href="../index.html#services">Chimney Services</a>
    <a href="../index.html#related">Related Services</a>
    <a href="../index.html#about">About</a>
    <a href="../index.html#gallery">Gallery</a>
    <a href="../index.html#areas">Service Area</a>
    <a href="../index.html#contact">Contact</a>
    <a href="tel:19783207778" class="mobile-menu__call">Call 978-320-7778</a>
  </div>

  <main>
    <section class="service-hero">
      <div class="container">
        <div class="breadcrumb">
          <a href="../index.html#home">Home</a><span class="sep">/</span>
          <a href="../index.html#{cat_anchor}">{cat_label}</a><span class="sep">/</span>
          <span class="current">{data["title"]}</span>
        </div>
        <div class="service-hero__grid">
          <div class="reveal">
            <span class="eyebrow">{cat_label}</span>
            <h1>{data["title"]}</h1>
            <p class="service-hero__lead">{data["lead"]}</p>
            <div class="hero__actions">
              <a href="../index.html#contact" class="btn btn--primary btn--lg">Request a Free Estimate</a>
              <a href="tel:{PHONE_TEL}" class="btn btn--ghost btn--lg">
                <svg viewBox="0 0 24 24" class="ico"><path d="M6.6 10.8a15.5 15.5 0 006.6 6.6l2.2-2.2a1 1 0 011-.24 11.3 11.3 0 003.5.56 1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1 11.3 11.3 0 00.56 3.5 1 1 0 01-.24 1z"/></svg>
                Call Now
              </a>
            </div>
          </div>
          <div class="service-hero__img image-frame reveal" data-photo="{data["photo"]}">
            <span class="frame__label">Photo coming soon</span>
          </div>
        </div>
      </div>
    </section>

    <section class="service-body">
      <div class="container service-layout">
        <div class="service-main">
          <h2>What we do</h2>
          {intro_html}

          <h2>{data["why"]}</h2>
          <div class="feature-cards">
{features_html}
          </div>

          <h2>{data["list_title"]}</h2>
          <ul class="signs-list">
{items_html}
          </ul>

          <h2>How it works</h2>
          <div class="steps">
{steps_html}
          </div>
        </div>

        <aside class="service-aside">
          <div class="aside-card aside-card--cta">
            <h3>Free, no-pressure estimate</h3>
            <p>Tell us what's going on and we'll get right back to you, usually same day.</p>
            <a href="../index.html#contact" class="btn btn--primary">Request an Estimate</a>
            <a href="tel:{PHONE_TEL}" class="aside-phone">📞 978-320-7778</a>
          </div>
          <div class="aside-card aside-card--links">
            <h3>{cat_label}</h3>
            <nav class="aside-links">
{aside_links(same_cat, slug)}
            </nav>
          </div>
        </aside>
      </div>
    </section>

    <section class="offer">
      <div class="container offer__inner reveal">
        <div class="offer__text">
          <h2>5% off for Veterans &amp; Seniors</h2>
          <p>Our thank-you to those who served and to our senior neighbors. Mention it when you book.</p>
        </div>
        <a href="../index.html#contact" class="btn btn--light btn--lg">Claim Your Discount</a>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container footer__grid">
      <div class="footer__brand">
        <div class="footer__logo-tile">
          <img src="../images/logo-badge.jpg" alt="Sam &amp; Ivan Chimney Guys logo" />
        </div>
        <p>Family-owned, CSIA-certified chimney &amp; masonry professionals serving Massachusetts &amp; New Hampshire.</p>
      </div>
      <div class="footer__col">
        <h4>Services</h4>
        <a href="chimney-cleaning.html">Chimney Cleaning</a>
        <a href="chimney-inspection.html">Inspection</a>
        <a href="fireplace-masonry-repair.html">Repair &amp; Masonry</a>
        <a href="chimney-liner-installation.html">Liners &amp; Caps</a>
        <a href="chimney-waterproofing-sealing.html">Waterproofing</a>
      </div>
      <div class="footer__col">
        <h4>Company</h4>
        <a href="../index.html#about">About Us</a>
        <a href="../index.html#gallery">Gallery</a>
        <a href="../index.html#reviews">Reviews</a>
        <a href="../index.html#areas">Service Area</a>
        <a href="../index.html#contact">Free Estimate</a>
      </div>
      <div class="footer__col">
        <h4>Contact</h4>
        <a href="tel:19783207778">978-320-7778</a>
        <a href="tel:19785903904">978-590-3904</a>
        <a href="mailto:inschimneyguys@gmail.com">inschimneyguys@gmail.com</a>
        <a href="https://instagram.com/sam_n_ivan_chimneyguys" target="_blank" rel="noopener">@sam_n_ivan_chimneyguys</a>
      </div>
    </div>
    <div class="footer__bar">
      <div class="container footer__bar-inner">
        <span>© <span id="year"></span> Sam &amp; Ivan The Chimney Guys. All rights reserved.</span>
        <span>Servicing MA &amp; NH • 24/7 Emergency Service</span>
      </div>
    </div>
  </footer>

  <a href="tel:19783207778" class="fab" aria-label="Call Sam and Ivan">
    <svg viewBox="0 0 24 24" class="ico"><path d="M6.6 10.8a15.5 15.5 0 006.6 6.6l2.2-2.2a1 1 0 011-.24 11.3 11.3 0 003.5.56 1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1 11.3 11.3 0 00.56 3.5 1 1 0 01-.24 1z"/></svg>
  </a>

  <script src="../script.js?v=4"></script>
</body>
</html>
'''

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for slug, data in SERVICES.items():
        path = os.path.join(OUT_DIR, slug + ".html")
        with open(path, "w") as f:
            f.write(build_page(slug, data))
        print("wrote", path)
    print(f"\nDone — {len(SERVICES)} service pages generated in {OUT_DIR}/")

if __name__ == "__main__":
    main()
