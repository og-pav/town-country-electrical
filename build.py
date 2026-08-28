#!/usr/bin/env python3
"""Town & Country Electrical Co. — static site generator."""
import os, re, sys, urllib.parse, datetime

BASE = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "https://towncountryelectrical.com.au"
OUT = os.path.dirname(os.path.abspath(__file__))
TODAY = datetime.date.today().isoformat()

BIZ = {
    "name": "Town & Country Electrical Co.",
    "short": "Town & Country Electrical",
    "owner": "Jordan Giuffre",
    "phone": "0405 305 671",
    "phone_href": "tel:+61405305671",
    "email": "jordan@towncountryelectrical.com.au",
    "town": "Mullumbimby", "state": "NSW", "postcode": "2482",
    "region": "Northern Rivers",
    "fb": "https://www.facebook.com/507848365754516",
    "ig": "https://www.instagram.com/town_and_country_electrical_co",
}
AREAS_ALL = ["Mullumbimby","Byron Bay","Brunswick Heads","Ocean Shores","Bangalow","Pottsville","Lennox Head","Ballina","Kingscliff","Lismore"]

CDN = "https://img1.wsimg.com/isteam/ip/52ef02e5-fc83-4602-a76e-29188a0fe99f/"
def IMG(name, w=1400):
    return CDN + urllib.parse.quote(name) + f"/:/rs=w:{w}"

LOGO = IMG("town & country(3).png", 500)
PHOTOS = {
    "hero": IMG("MULLUM.jpg", 1920),
    "owner": IMG("blob-07fcf8c.png", 900),
    "ev": IMG("ev charger.jpg"), "garden": IMG("garden lighting.jpg"),
    "avoca": IMG("lights work avoca.jpg"), "fan": IMG("lights fan.jpg"),
    "vanity": IMG("bath vanity strip lt.jpg"), "bath": IMG("bath.jpg"),
    "bar": IMG("bar.jpg"), "pendant": IMG("PENDANT.jpg"), "pendant2": IMG("PENDANT 2.jpg"),
    "w1": IMG("work photo 1.jpg"), "w3": IMG("work photo 3.jpg"),
    "w4": IMG("work photo 4.jpg"), "w5": IMG("work photo 5.jpg"),
    "i5879": IMG("IMG_5879.jpg"), "i6370": IMG("IMG_6370.jpg"),
    "i5713": IMG("IMG_5713.jpg"), "i0773": IMG("IMG_0773 2.JPG"),
    "og": IMG("MULLUM.jpg", 1200),
}
ALT = "Electrical work completed by Town & Country Electrical Co. in the Northern Rivers"

# ---------------------------------------------------------------- services
SERVICES = {
 "residential-electrical": {
   "name":"Residential Electrical","img":PHOTOS["w1"],
   "tag":"New builds & renovations",
   "blurb":"Full electrical fit-outs for new builds, renovations and extensions — planned properly, wired cleanly, finished with care.",
   "body":"From first-fix wiring to final fit-off, Jordan handles the complete electrical scope of your build or renovation. That means power and lighting layouts that actually suit how you live, clean switchboard work, and coordination with your builder so nothing holds the job up. Every install is completed to Australian standards by a licensed and insured electrician, with a Certificate of Compliance supplied.",
   "points":["Complete new build and renovation wiring","Power, lighting and data layout design","Coordination with builders and trades","Certificate of Compliance with every job"],
   "gallery":["w1","w3","i6370","i0773"],
   "kw":"residential electrician"},
 "electrical-repairs": {
   "name":"Electrical Repairs & Fault Finding","img":PHOTOS["w3"],
   "tag":"Repairs & diagnostics",
   "blurb":"Tripping switches, dead power points, flickering lights — found fast, fixed properly, explained in plain English.",
   "body":"Electrical faults rarely announce themselves politely. Whether it's a safety switch that keeps tripping, a circuit that's gone dead or a burning smell you can't place, Jordan diagnoses the actual cause rather than patching symptoms. You'll get an honest explanation of what's wrong, what it costs to fix, and what can safely wait.",
   "points":["Safety switch and circuit breaker faults","Dead power points and lighting circuits","Fault finding and testing","Honest advice on repair vs replace"],
   "gallery":["w3","i5879","w4","w5"],
   "kw":"electrical repairs and fault finding"},
 "lighting-and-power": {
   "name":"Lighting & Power","img":PHOTOS["pendant"],
   "tag":"Lighting design & installation",
   "blurb":"Pendants, downlights, garden and outdoor lighting, extra power points — lighting that changes how your home feels.",
   "body":"Good lighting is the cheapest renovation there is. Jordan installs everything from statement pendants and LED downlights to outdoor and garden lighting that makes your place feel resort-level after dark. Add the power points where you actually need them and stop living off double adaptors.",
   "points":["Pendant, downlight and feature lighting","Garden and outdoor lighting","Ceiling fans and smart switches","Additional power points and USB outlets"],
   "gallery":["pendant","pendant2","garden","avoca","fan","bar"],
   "kw":"lighting installation"},
 "ev-charger-installation": {
   "name":"EV Charger Installation","img":PHOTOS["ev"],
   "tag":"Future-ready charging",
   "blurb":"Home EV charging installed safely — the right charger, the right circuit, charging overnight without a second thought.",
   "body":"Charging from a standard power point is slow and pushes a circuit that was never designed for it. Jordan installs dedicated EV charging circuits and wall chargers matched to your car, your switchboard and your usage — including load management so your charger and your home share power intelligently.",
   "points":["Dedicated EV charging circuits","Wall charger supply and installation","Switchboard capacity assessment","Load management setup"],
   "gallery":["ev","i5879","w1"],
   "kw":"EV charger installation"},
 "hot-water-repairs": {
   "name":"Hot Water Repairs","img":PHOTOS["i5713"],
   "tag":"Electric hot water",
   "blurb":"No hot water is not a tomorrow problem. Electric hot water faults diagnosed and repaired promptly.",
   "body":"When an electric hot water system stops heating, the fault is often electrical — a failed element, thermostat or circuit issue. Jordan tests and repairs electric hot water systems and can advise honestly on whether a repair or replacement makes better long-term sense.",
   "points":["Element and thermostat replacement","Hot water circuit faults","Off-peak wiring issues","Repair vs replacement advice"],
   "gallery":["i5713","w4","w3"],
   "kw":"hot water repairs"},
 "switchboard-upgrades": {
   "name":"Switchboard Upgrades","img":PHOTOS["i5879"],
   "tag":"Safety & capacity",
   "blurb":"Old fuse boards weren't built for modern life. Upgrade to a safe, compliant switchboard with full safety switch protection.",
   "body":"If your board still runs ceramic fuses, has no safety switches, or trips every time the kettle and heater run together, it's overdue. A modern switchboard protects every circuit with RCD safety switches and gives your home the capacity for today's loads — induction cooking, air conditioning, EV charging.",
   "points":["Full switchboard replacement","Safety switch (RCD) protection on all circuits","Defect rectification","Capacity for EV charging, aircon and induction"],
   "gallery":["i5879","w5","w1"],
   "kw":"switchboard upgrades"},
 "smoke-alarms": {
   "name":"Smoke Alarm Installation","img":PHOTOS["w5"],
   "tag":"Compliance & safety",
   "blurb":"Interconnected photoelectric smoke alarms installed and maintained to keep your family and your compliance covered.",
   "body":"Working smoke alarms are a legal requirement in NSW homes — and hardwired, interconnected photoelectric alarms are the standard worth having. Jordan installs, replaces and services smoke alarms for homeowners, landlords and property managers across the Northern Rivers.",
   "points":["Hardwired photoelectric alarms","Interconnected alarm systems","Replacement of expired alarms","Landlord and rental compliance"],
   "gallery":["w5","w3","i6370"],
   "kw":"smoke alarm installation"},
 "appliance-installation": {
   "name":"Appliance Installation","img":PHOTOS["bath"],
   "tag":"Kitchens, bathrooms & laundry",
   "blurb":"Ovens, cooktops, rangehoods, heated towel rails — installed and connected safely by a licensed electrician.",
   "body":"New appliances deserve better than a hopeful DIY connection. Jordan installs and hard-wires ovens, cooktops, rangehoods, bathroom heating, heated towel rails and more — with the correct circuit protection and a Certificate of Compliance for your records.",
   "points":["Oven, cooktop and rangehood connection","Bathroom heat, light and fan units","Heated towel rails and floor heating","Correct circuits and compliance certificates"],
   "gallery":["bath","vanity","bar","i0773"],
   "kw":"appliance installation"},
 "emergency-electrician": {
   "name":"24/7 Emergency Electrician","img":PHOTOS["w4"],
   "tag":"Around the clock",
   "blurb":"Power out, burning smell, sparking outlet? Call any hour — a local emergency electrician for the Northern Rivers.",
   "body":"Some electrical problems can't wait for business hours. Town & Country Electrical Co. offers 24/7 emergency call-outs across the Northern Rivers for loss of power, storm damage, burning smells, sparking outlets and any fault that makes your home unsafe. Call first — Jordan will talk you through making the situation safe, then get there.",
   "points":["24/7 emergency call-outs","Loss of power and storm damage","Burning smells and sparking outlets","Safety-first advice over the phone"],
   "gallery":["w4","w5","i5879"],
   "kw":"emergency electrician"},
}

AREA_PAGES = {
 "mullumbimby":{"name":"Mullumbimby","intro":"Home base. Town & Country Electrical Co. is based right here in Mullumbimby, which means fast response times, no travel surcharges and an electrician who knows the town's housing stock — from Federation-era homes with ageing wiring to brand-new builds in the hills."},
 "byron-bay":{"name":"Byron Bay","intro":"From beach shacks to architectural builds, Byron Bay homes ask a lot of their electrics. Jordan works across Byron Bay and Suffolk Park on renovations, lighting design, EV chargers and everyday repairs — with the reliable communication Byron tradies are famous for lacking."},
 "brunswick-heads":{"name":"Brunswick Heads","intro":"Minutes up the road from our Mullumbimby base, Brunswick Heads gets true local service — same-week bookings for most jobs, and 24/7 coverage when something can't wait."},
 "ocean-shores":{"name":"Ocean Shores","intro":"Ocean Shores and South Golden Beach homes deal with salt air, storms and growing households. From switchboard upgrades to ceiling fans and outdoor lighting, Jordan keeps homes here safe and comfortable."},
 "lennox-head":{"name":"Lennox Head","intro":"Town & Country Electrical Co. services Lennox Head for renovations, repairs, smoke alarm compliance and EV charger installs — quality workmanship backed by a genuine guarantee."},
 "ballina":{"name":"Ballina","intro":"Ballina households and landlords rely on Town & Country Electrical Co. for honest fault finding, switchboard safety upgrades and smoke alarm compliance — with upfront pricing before work starts."},
}

REVIEWS = [
 {"stars":5,"text":"“Jordan did a great job installing some ceiling fans for us…”","who":"Lachlan Mackintosh","meta":"Verified review · Aug 2026"},
 {"stars":5,"text":"“I had electrical work completed in my home… great communication and quality work.”","who":"Erina","meta":"Verified review · Jul 2026"},
 {"stars":5,"text":"Five-star rating left after a completed job.","who":"Stefano","meta":"Verified review · Jul 2026"},
]

BLOG = {
 "ev-charger-installation-northern-rivers":{
  "title":"EV Charger Installation in the Northern Rivers: What to Know Before You Buy",
  "desc":"Thinking about home EV charging in Byron Bay, Mullumbimby or the Northern Rivers? Here's what matters: charger types, switchboard capacity and installation.",
  "img":"ev","date":"2026-08-10","tagline":"EV Charging",
  "body":"""<p>Electric cars are turning up in Northern Rivers driveways faster than most people expected — and the first question every new owner asks is the same: <em>how do I charge this thing at home?</em></p>
<h2>The three ways to charge at home</h2>
<p>A standard power point will charge an EV, slowly — usually 10–15&nbsp;km of range per hour. Fine as a stopgap, not a long-term plan, and it works a circuit that was never designed for an eight-hour continuous load. A dedicated wall charger on its own circuit delivers 40–100&nbsp;km of range per hour, charges overnight comfortably, and is the setup most households land on.</p>
<h2>Your switchboard matters more than your charger</h2>
<p>Before any charger goes on the wall, your switchboard needs a capacity check. Many Northern Rivers homes — especially older ones around Mullumbimby, Bangalow and Lismore — run boards that predate safety switches, let alone EV loads. If yours is one of them, a <a href="/services/switchboard-upgrades.html">switchboard upgrade</a> is the first step, and it improves the safety of the whole house at the same time.</p>
<h2>Load management: the clever bit</h2>
<p>Modern chargers can share power intelligently with the rest of your home, backing off while the oven and aircon run and ramping up overnight. If you have solar, charging can be timed to soak up your excess generation instead of exporting it for cents.</p>
<h2>What installation involves</h2>
<p>A typical install includes a dedicated circuit from the switchboard, appropriate protection, the wall charger mounted where your car actually parks, and testing with a Certificate of Compliance. Most installs are done in a day.</p>
<p>Thinking about it? <a href="/contact.html">Get in touch</a> for straight answers on what your home needs — no jargon, no upsell.</p>"""},
 "signs-you-need-a-switchboard-upgrade":{
  "title":"7 Signs Your Home Needs a Switchboard Upgrade",
  "desc":"Ceramic fuses, tripping switches, flickering lights? Here are the signs your Northern Rivers home's switchboard is overdue for a safety upgrade.",
  "img":"i5879","date":"2026-07-28","tagline":"Home Safety",
  "body":"""<p>Your switchboard is the heart of your home's electrical system — and in a lot of Northern Rivers homes, it's the oldest thing in the house still doing a full-time job. Here's how to know when it's time.</p>
<h2>1. It still has ceramic fuses</h2><p>Rewirable ceramic fuses were state of the art in the 1960s. They offer no protection against electric shock — only against gross overloads — and they have no place in a modern home.</p>
<h2>2. No safety switches (RCDs)</h2><p>Safety switches cut power in milliseconds when electricity leaks to earth — the thing that saves lives. Every circuit in your home should have one. Many older boards protect one or two circuits at best.</p>
<h2>3. Breakers trip when you use two appliances</h2><p>Kettle plus heater shouldn't equal darkness. Regular tripping means circuits are overloaded or the board can't handle modern demand.</p>
<h2>4. Flickering or dimming lights</h2><p>Lights that dip when the aircon starts can indicate loose connections or an undersized supply — both worth investigating promptly.</p>
<h2>5. Buzzing, heat or burning smells</h2><p>A switchboard should be silent and cool. Any buzzing, warmth or odour is a call-us-today situation — or after hours, a <a href="/services/emergency-electrician.html">24/7 emergency call</a>.</p>
<h2>6. You're adding big new loads</h2><p>Induction cooking, ducted aircon, a pool pump, an <a href="/services/ev-charger-installation.html">EV charger</a> — modern additions often exceed what an old board can safely supply.</p>
<h2>7. Your home is 25+ years old and the board's never been touched</h2><p>Even without symptoms, an inspection is cheap insurance.</p>
<p>Not sure where your board stands? <a href="/contact.html">Book an assessment</a> — you'll get an honest verdict, not a scare campaign.</p>"""},
 "smoke-alarm-rules-nsw-homes":{
  "title":"Smoke Alarm Requirements for NSW Homes: A Plain-English Guide",
  "desc":"What NSW law requires for smoke alarms in homes and rentals, why photoelectric interconnected alarms are the standard worth having, and when to replace them.",
  "img":"w5","date":"2026-07-14","tagline":"Compliance",
  "body":"""<p>Smoke alarms are one of those things nobody thinks about until an inspection, a sale or — worst case — a fire. Here's the plain-English version of what NSW homes need.</p>
<h2>The baseline</h2>
<p>NSW law requires working smoke alarms on every level of every home. For rentals, landlords must ensure alarms are working, are replaced within 10 years of manufacture, and have batteries replaced annually (or as required for the alarm type).</p>
<h2>Why photoelectric, and why interconnected</h2>
<p>Photoelectric alarms detect smouldering, smoky fires — the kind that kill people in their sleep — significantly faster than older ionisation alarms. Interconnected alarms all sound together, so a fire in the garage wakes you in the bedroom. Hardwired (240V) alarms with battery backup remove the flat-battery problem entirely.</p>
<h2>Where alarms should go</h2>
<p>At minimum: between sleeping areas and the rest of the home, and on every level. Better practice puts an alarm in every bedroom and living space. Placement matters — dead corners and spots near kitchens and bathrooms cause missed detections and false alarms.</p>
<h2>When to replace</h2>
<p>Every smoke alarm has a manufacture date printed on it. Ten years is the limit — after that the sensor is no longer reliable, test button or not.</p>
<p>Whether you're a homeowner, landlord or property manager across the Northern Rivers, <a href="/services/smoke-alarms.html">smoke alarm installation and compliance</a> is a quick, inexpensive job that Jordan can sort in a single visit. <a href="/contact.html">Get it booked</a>.</p>"""},
 "best-lighting-upgrades-northern-rivers-homes":{
  "title":"The Lighting Upgrades That Transform Northern Rivers Homes",
  "desc":"From garden lighting to statement pendants and ceiling fans — the lighting and power upgrades that make the biggest difference, from a local electrician.",
  "img":"garden","date":"2026-06-30","tagline":"Lighting & Power",
  "body":"""<p>Lighting is the cheapest renovation there is. No walls move, no council forms, and the whole feel of a home changes in a day or two of work. These are the upgrades we install most across the Northern Rivers — and the ones owners rave about after.</p>
<h2>Garden and outdoor lighting</h2>
<p>Northern Rivers evenings are made for being outdoors. Warm, low-glare garden lighting extends your living space past sunset and makes paths and steps safe. Done properly, it's subtle — you notice the garden, not the fittings.</p>
<h2>Statement pendants</h2>
<p>One well-placed pendant over a kitchen bench or dining table does more for a room than a repaint. We install everything from featherweight rattan to serious sculptural pieces — safely supported and on a dimmer where it counts.</p>
<h2>LED downlight conversions</h2>
<p>Still running halogens? Modern LEDs cut the running cost dramatically, run cool, and last for years. Whole-house conversions are quick and pay for themselves.</p>
<h2>Ceiling fans</h2>
<p>The Northern Rivers summer essential. A quality DC ceiling fan moves serious air for cents a day and takes the edge off humid nights without the aircon bill.</p>
<h2>Dimmers and smart switching</h2>
<p>Scenes, timers, and lights that come on before you get home — modern switching is inexpensive and genuinely useful, no proprietary hub required.</p>
<p>Got a room that never feels right? It's probably the lighting. <a href="/contact.html">Ask Jordan</a> what would make the difference — <a href="/services/lighting-and-power.html">lighting and power</a> is our favourite kind of work.</p>"""},
 "what-to-do-when-power-goes-out":{
  "title":"Power Gone Out? Here's What to Check Before You Call an Electrician",
  "desc":"A step-by-step guide for Northern Rivers households: what to check when the power goes out, when it's the network, and when you need an emergency electrician.",
  "img":"w4","date":"2026-06-12","tagline":"Emergency",
  "body":"""<p>The power's out. Before you assume the worst (or sit in the dark waiting), run through this five-minute checklist — it solves the mystery more often than not.</p>
<h2>1. Is it just you?</h2>
<p>Check the street. If the neighbours are dark too, it's a network outage — check the Essential Energy outage map and report it. No electrician can fix the grid.</p>
<h2>2. Check your switchboard</h2>
<p>If it's just your place, open the switchboard and look for a tripped safety switch or breaker — a lever sitting down or in the middle. Flip it fully off, then back on.</p>
<h2>3. If it trips again, find the culprit</h2>
<p>A safety switch that won't stay on is doing its job — something connected is leaking current. Unplug everything on that circuit (think kettles, toasters, outdoor gear, anything that's copped moisture) and try again. If it holds, plug things back in one at a time until you find the offender.</p>
<h2>4. When it's time to call</h2>
<p>Call an electrician when a switch won't reset with everything unplugged, when only part of the house is dead, or when you notice burning smells, buzzing, or scorch marks. Those last three are call-now territory, any hour — that's exactly what our <a href="/services/emergency-electrician.html">24/7 emergency line</a> is for.</p>
<h2>What NOT to do</h2>
<p>Don't hold a tripping safety switch on. Don't open the meter box wiring. Don't run extension leads from the neighbour's place through a window in the rain. (Yes, it's been done.)</p>
<p>Storm season in the Northern Rivers keeps every electrician busy — save the number now: <a href="tel:+61405305671">0405&nbsp;305&nbsp;671</a>, any hour.</p>"""},
}

# ---------------------------------------------------------------- svg icons
IC = {
 "phone":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
 "chat":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
 "bolt":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
 "check":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>',
 "shield":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
 "clock":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
 "home":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>',
 "pin":'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
 "star":'<svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>',
 "chev":'<svg class="chev" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>',
}

# ---------------------------------------------------------------- partials
GHL_SLOT = """<div class="ghl-slot">
<!-- ============ GOHIGHLEVEL FORM EMBED ============
Paste your GHL form embed below and delete the fallback <form> above.
Example:
<iframe src="https://api.leadconnectorhq.com/widget/form/YOUR_FORM_ID" style="width:100%;height:560px;border:none;" id="inline-YOUR_FORM_ID" title="Enquiry form"></iframe>
<script src="https://link.msgsndr.com/js/form_embed.js"></script>
================================================== -->
</div>"""

def lead_form(idpfx, compact=False):
    note = "" if compact else '<div class="f-field"><label for="%s-msg">What do you need done?</label><textarea id="%s-msg" name="message" rows="3" placeholder="e.g. Ceiling fans in two bedrooms, Ocean Shores"></textarea></div>' % (idpfx, idpfx)
    return f"""<form class="lead-form form-grid" data-thanks="/thank-you.html" novalidate>
<div class="f-field"><label for="{idpfx}-name">Name*</label><input id="{idpfx}-name" name="name" type="text" required autocomplete="name" placeholder="Your name">
<span class="f-msg">Please enter your name so Jordan knows who to ask for.</span></div>
<div class="f-field"><label for="{idpfx}-phone">Phone*</label><input id="{idpfx}-phone" name="phone" type="tel" required autocomplete="tel" inputmode="tel" placeholder="04xx xxx xxx">
<span class="f-msg">A valid phone number is needed so we can call you back.</span></div>
<div class="f-field"><label for="{idpfx}-email">Email*</label><input id="{idpfx}-email" name="email" type="email" required autocomplete="email" placeholder="you@email.com">
<span class="f-msg">That email doesn't look right — mind checking it?</span></div>
{note}
<button class="btn btn-primary btn-lg" type="submit">Get My Free Quote</button>
<p style="font-size:.82rem;color:var(--muted)">Jordan replies to every enquiry within one business day — usually much faster.</p>
</form>
{GHL_SLOT}"""

def head(title, desc, path, extra_schema="", og_type="website"):
    canonical = BASE + path
    org = f"""{{"@context":"https://schema.org","@type":"Electrician","name":"{BIZ['name']}","url":"{BASE}/","telephone":"+61405305671","email":"{BIZ['email']}","image":"{PHOTOS['og']}","logo":"{LOGO}","priceRange":"$$","address":{{"@type":"PostalAddress","addressLocality":"Mullumbimby","addressRegion":"NSW","postalCode":"2482","addressCountry":"AU"}},"geo":{{"@type":"GeoCoordinates","latitude":-28.5525,"longitude":153.4997}},"openingHoursSpecification":[{{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"00:00","closes":"23:59"}}],"areaServed":[{','.join('{"@type":"City","name":"%s"}' % a for a in AREAS_ALL)}],"sameAs":["{BIZ['fb']}","{BIZ['ig']}"],"founder":{{"@type":"Person","name":"{BIZ['owner']}"}},"aggregateRating":{{"@type":"AggregateRating","ratingValue":"5.0","reviewCount":"4"}}}}"""
    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow">
<!-- GOOGLE SEARCH CONSOLE: paste your verification meta tag here -->
<!-- <meta name="google-site-verification" content="PASTE_TOKEN_HERE"> -->
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{PHOTOS['og']}">
<meta property="og:locale" content="en_AU">
<meta property="og:site_name" content="{BIZ['name']}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://img1.wsimg.com">
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@700;800;900&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/site.css?v=1787877868">
<script type="application/ld+json">{org}</script>
{extra_schema}
<script>
/* Google Analytics — loads only after cookie consent. Replace G-XXXXXXXXXX with your GA4 ID. */
window.loadGA=function(){{if(window.__ga)return;window.__ga=1;var s=document.createElement('script');s.async=1;s.src='https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX';document.head.appendChild(s);window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}window.gtag=gtag;gtag('js',new Date());gtag('config','G-XXXXXXXXXX');}};
</script>
</head>
<body>"""

def crumbs_schema(items):
    lis = ",".join(f'{{"@type":"ListItem","position":{i+1},"name":"{n}","item":"{BASE}{u}"}}' for i,(n,u) in enumerate(items))
    return f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{lis}]}}</script>'

def header_nav(active=""):
    return f"""<a class="skip" href="#main" style="position:absolute;left:-999px">Skip to content</a>
<header class="site-header">
 <div class="hdr-in">
  <a class="logo" href="/" aria-label="{BIZ['name']} — home"><img src="{LOGO}" alt="{BIZ['name']} logo" width="180" height="60"></a>
  <nav class="nav" aria-label="Main">
   <a href="/services.html">Services</a>
   <a href="/about.html">About</a>
   <a href="/case-studies.html">Our Work</a>
   <a href="/blog.html">Blog</a>
   <a class="hdr-call" href="{BIZ['phone_href']}">{IC['phone']} {BIZ['phone']}</a>
   <a class="btn btn-brass" href="/contact.html">Get a Free Quote</a>
  </nav>
  <button class="burger" aria-label="Open menu"><span></span><span></span><span></span></button>
 </div>
</header>
<div class="m-overlay" role="dialog" aria-label="Menu">
 <button class="m-close" aria-label="Close menu">×</button>
 <a href="/">Home</a><a href="/services.html">Services</a><a href="/about.html">About</a>
 <a href="/case-studies.html">Our Work</a><a href="/blog.html">Blog</a><a href="/contact.html">Contact</a>
 <a class="btn btn-brass" href="{BIZ['phone_href']}">Call {BIZ['phone']}</a>
</div>"""

def footer():
    svc_links = "".join(f'<li><a href="/services/{s}.html">{d["name"]}</a></li>' for s,d in list(SERVICES.items())[:6])
    area_links = "".join(f'<li><a href="/areas/{s}.html">Electrician {d["name"]}</a></li>' for s,d in AREA_PAGES.items())
    return f"""<footer class="site-footer">
 <div class="wrap">
  <div class="foot-grid">
   <div class="foot-logo">
    <img src="{LOGO}" alt="{BIZ['name']} logo" loading="lazy">
    <p>Family run. Locally owned. Licensed &amp; insured electrician servicing the entire Northern Rivers, 24/7.</p>
    <div class="socials">
     <a href="{BIZ['fb']}" aria-label="Facebook" rel="noopener" target="_blank"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg></a>
     <a href="{BIZ['ig']}" aria-label="Instagram" rel="noopener" target="_blank"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg></a>
    </div>
   </div>
   <div><h4>Services</h4><ul>{svc_links}<li><a href="/services.html">All services →</a></li></ul></div>
   <div><h4>Service Areas</h4><ul>{area_links}</ul></div>
   <div><h4>Contact</h4><ul>
    <li><a href="{BIZ['phone_href']}">{BIZ['phone']}</a></li>
    <li><a href="mailto:{BIZ['email']}">{BIZ['email']}</a></li>
    <li>Mullumbimby NSW 2482</li>
    <li>Open 24/7 for emergencies</li>
    <li><a href="https://www.google.com/maps/dir/?api=1&destination=Mullumbimby+NSW+2482" rel="noopener" target="_blank">Get directions</a></li>
   </ul>
   <p style="margin-top:1rem;font-size:.85rem">Payment by bank transfer or card. Workmanship guaranteed.</p></div>
  </div>
  <div class="fine">
   <span>© 2026 {BIZ['name']} — Licensed &amp; insured electrician, Northern Rivers NSW.</span>
   <span><a href="/privacy-policy.html">Privacy Policy</a> · <a href="/terms.html">Terms of Service</a> · <a href="/sitemap.xml">Sitemap</a></span>
  </div>
 </div>
</footer>
<div class="m-cta">
 <a class="btn btn-ghost" href="{BIZ['phone_href']}">Call Now</a>
 <a class="btn btn-brass" href="/contact.html">Free Quote</a>
</div>
<div class="cookie" id="cookie" role="dialog" aria-label="Cookie consent">
 <b>Cookies, briefly.</b>
 <p style="margin-top:.4rem">We use essential cookies, plus analytics cookies (only if you're okay with it) to see how the site is used.</p>
 <div class="row"><button class="ok">Accept all</button><button class="no">Essential only</button></div>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>
<script src="/assets/js/site.js?v=1787877868" defer></script>
</body></html>"""

def gal_html(keys):
    figs = "".join(f'<figure class="reveal"><img src="{PHOTOS[k]}" alt="{ALT}" loading="lazy"></figure>' for k in keys)
    return f'<div class="gal">{figs}</div>'

def write(path, html):
    if path.endswith((".html",)):
        html = re.sub(r'((?:href|src|data-thanks)=")/(?!/)', lambda m: m.group(1) + BASE + "/", html)
    full = os.path.join(OUT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f: f.write(html)
    print("wrote", path)

# ---------------------------------------------------------------- index
def build_index():
    faqs = [
     ("How quickly can you get to my job?","For most jobs across the Northern Rivers we can book you in within the week — often sooner. Genuine emergencies are answered 24/7, any day of the year. Every enquiry gets a response within one business day."),
     ("Which areas do you service?","We're based in Mullumbimby and service the entire Northern Rivers: Byron Bay, Brunswick Heads, Ocean Shores, Bangalow, Pottsville, Lennox Head, Ballina, Kingscliff, Lismore and everywhere in between."),
     ("Are you licensed and insured?","Yes. Town & Country Electrical Co. is a fully licensed and insured electrical business, and every job is completed to Australian standards with a Certificate of Compliance where applicable."),
     ("How does pricing work?","Upfront. You'll know what a job costs before work starts — clear, honest pricing with no surprise line items at the end. For larger jobs like renovations and switchboard upgrades, you'll get a written quote."),
     ("Do you do small jobs?","Absolutely. A single power point, one flickering light, a new ceiling fan — no job is too small, and small jobs get the same care as full renovations."),
     ("What happens in an electrical emergency?","Call 0405 305 671 any hour. Jordan will talk you through making the situation safe over the phone, then get to you. Burning smells, sparking outlets and repeated safety-switch trips should never wait until morning."),
     ("How do I pay?","By bank transfer or card. You'll receive an electronic invoice with clear line items — no cash-only mystery pricing."),
     ("Is your work guaranteed?","Yes. Our workmanship is guaranteed — if something we've installed or repaired isn't right, we come back and make it right. Our reputation runs on repeat customers and local word of mouth."),
    ]
    faq_html = "".join(f"""<div class="faq-item reveal"><button class="faq-q" aria-expanded="false">{q}{IC['chev']}</button><div class="faq-a"><p>{a}</p></div></div>""" for q,a in faqs)
    faq_schema = '<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' + ",".join(
        f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}' for q,a in faqs) + ']}</script>'

    tcards = "".join(f"""<div class="t-card"><span class="stars">★★★★★</span><p>{r['text']}</p><div class="who">{r['who']}<small>{r['meta']}</small></div></div>""" for r in REVIEWS)

    rows = ""
    for i,(slug,d) in enumerate([("residential-electrical",SERVICES["residential-electrical"]),("lighting-and-power",SERVICES["lighting-and-power"]),("ev-charger-installation",SERVICES["ev-charger-installation"]),("switchboard-upgrades",SERVICES["switchboard-upgrades"])]):
        flip = " flip" if i%2 else ""
        rows += f"""<div class="srv-row{flip}">
 <div class="media mask reveal"><img src="{d['img']}" alt="{d['name']} — {ALT}" loading="lazy"></div>
 <div class="reveal"><span class="tag">{d['tag']}</span><h3>{d['name']}</h3><p>{d['blurb']}</p>
 <a class="more" href="/services/{slug}.html">Explore {d['name'].lower()}</a></div>
</div>"""

    html = head(
      "Electrician Mullumbimby & Byron Bay | Town & Country Electrical Co.",
      "Family-run, licensed electrician servicing Mullumbimby, Byron Bay & the Northern Rivers. Upfront pricing, quality workmanship, 24/7 emergencies. Free quotes.",
      "/", faq_schema) + header_nav() + f"""
<main id="main">

<section class="hero" id="top">
 <div class="hero-bg"><img src="{PHOTOS['hero']}" alt="Mullumbimby, home of Town & Country Electrical Co." fetchpriority="high"></div>
 <div class="hero-orb" aria-hidden="true"></div>
 <div class="wrap">
  <span class="kicker hero-stagger" style="background:rgba(255,255,255,.1);border-color:rgba(255,255,255,.2);color:#F0C9A0">Mullumbimby · Byron Bay · Northern Rivers</span>
  <h1 class="hero-stagger">Your home's electrics, <em style="font-style:normal;color:#F0C9A0">done once, done right.</em></h1>
  <p class="lead hero-stagger">A family-run electrical company in the heart of the Northern Rivers. Upfront pricing, quality workmanship, and a licensed electrician who actually calls you back.</p>
  <div class="hero-stagger" style="display:flex;gap:1rem;flex-wrap:wrap">
   <a class="btn btn-brass btn-lg" href="/contact.html">Get a Free Quote</a>
   <a class="btn btn-ghost btn-lg" href="{BIZ['phone_href']}">{BIZ['phone']}</a>
  </div>
  <div class="proof-strip hero-stagger">
   <span><span class="stars">★★★★★</span> <b>5.0</b> from verified reviews</span>
   <span><b>Licensed</b> &amp; insured</span>
   <span><b>24/7</b> emergency call-outs</span>
   <span><b>Locally</b> owned &amp; operated</span>
  </div>
 </div>
</section>

<section class="problem">
 <div class="wrap reveal">
  <span class="kicker">Sound familiar?</span>
  <p class="big-lines">Tradies who don't show. Quotes that grow legs. Jobs left ninety-five percent finished.<br><br><em>You shouldn't have to chase your electrician.</em></p>
 </div>
</section>

<section id="difference">
 <div class="wrap split">
  <div class="media mask reveal"><img src="{PHOTOS['avoca']}" alt="Outdoor lighting installation by Town & Country Electrical Co." loading="lazy"></div>
  <div class="reveal">
   <span class="kicker">The Town &amp; Country difference</span>
   <h2>One electrician. Your job, start to finish.</h2>
   <p class="lead" style="margin-top:1rem">Deal directly with Jordan — the licensed electrician who quotes your job is the one who turns up and does it.</p>
   <ul class="check-list">
    <li><b>Reliable communication</b> — clear updates and honest advice at every step.</li>
    <li><b>Upfront pricing</b> — you know the cost before the work starts.</li>
    <li><b>Quality workmanship</b> — finished with care and respect for your home.</li>
    <li><b>Accountability</b> — a local reputation built on repeat customers.</li>
   </ul>
  </div>
 </div>
</section>

<section style="background:var(--surface)" id="how">
 <div class="wrap">
  <div class="reveal" style="text-align:center;max-width:640px;margin:0 auto">
   <span class="kicker">How it works</span>
   <h2>Three steps. Zero runaround.</h2>
  </div>
  <div class="steps">
   <div class="step-card reveal"><span class="step-num">1</span><div class="step-icon">{IC['chat']}</div><h3>Tell us the job</h3><p>Call or send the form — a couple of photos help. You'll hear back within one business day, usually much faster.</p></div>
   <div class="step-card reveal"><span class="step-num">2</span><div class="step-icon">{IC['check']}</div><h3>Get an upfront price</h3><p>Straight answers and a clear price before any work starts. No surprises, no padding, no jargon.</p></div>
   <div class="step-card reveal"><span class="step-num">3</span><div class="step-icon">{IC['bolt']}</div><h3>Job done properly</h3><p>Quality workmanship, a tidy finish, a <span class="tt" data-tt="An electrical safety certificate issued for notifiable work, for your records and insurance.">Certificate of Compliance</span> — and your place left cleaner than we found it.</p></div>
  </div>
 </div>
</section>

<section class="marquee-sec" id="reviews">
 <div class="wrap reveal">
  <span class="kicker">Word around the Rivers</span>
  <blockquote class="pullquote"><span class="stars">★★★★★ 5.0</span>“Jordan did a great job installing some ceiling fans for us…”<br><span style="font-size:.9rem;color:#F0C9A0;font-weight:600">— Lachlan Mackintosh, verified review</span></blockquote>
 </div>
 <div class="marquee reveal"><div class="marquee-track">{tcards}</div></div>
</section>

<section id="services-home">
 <div class="wrap">
  <div class="reveal"><span class="kicker">What we do</span><h2>Every residential job, covered.</h2></div>
  {rows}
  <div class="reveal" style="margin-top:2.5rem"><a class="btn btn-primary" href="/services.html">See all 9 services</a></div>
 </div>
</section>

<section style="background:var(--surface)" id="why">
 <div class="wrap">
  <div class="reveal" style="text-align:center;max-width:680px;margin:0 auto">
   <span class="kicker">Why locals choose us</span>
   <h2>Small business. Big standards.</h2>
  </div>
  <div class="bene">
   <div class="bene-card reveal"><div class="bene-ico">{IC['clock']}</div><h3>Response-time promise</h3><p>Every enquiry answered within one business day. Emergencies answered 24/7, full stop.</p></div>
   <div class="bene-card hot reveal"><div class="bene-ico">{IC['shield']}</div><h3>Workmanship guaranteed</h3><p>If something we've done isn't right, we come back and make it right. That's the whole policy.</p></div>
   <div class="bene-card reveal"><div class="bene-ico">{IC['pin']}</div><h3>Genuinely local</h3><p>Based in Mullumbimby, servicing the entire Northern Rivers. Your money stays in the community.</p></div>
   <div class="bene-card reveal"><div class="bene-ico">{IC['check']}</div><h3>Upfront pricing</h3><p>Clear pricing before work starts, and electronic invoices with honest line items. Card or bank transfer.</p></div>
   <div class="bene-card reveal"><div class="bene-ico">{IC['home']}</div><h3>Respect for your home</h3><p>Shoes off, drop sheets down, mess gone when we leave. It's your home, not a worksite.</p></div>
   <div class="bene-card reveal"><div class="bene-ico">{IC['star']}</div><h3>5.0-star rated</h3><p>Every review we have is five stars — earned one job at a time across the Northern Rivers.</p></div>
  </div>
 </div>
</section>

<section id="gallery">
 <div class="wrap">
  <div class="reveal"><span class="kicker">Recent work</span><h2>Our installation gallery</h2></div>
  {gal_html(["pendant","garden","vanity","fan","bar","i6370","w1","avoca"])}
  <div class="reveal" style="margin-top:2rem"><a class="more" style="font-weight:700;text-decoration:none" href="/case-studies.html">See project case studies →</a></div>
 </div>
</section>

<section style="background:var(--surface)" id="faq">
 <div class="wrap">
  <div class="reveal" style="text-align:center"><span class="kicker">Questions</span><h2>Fair questions, straight answers.</h2></div>
  <div class="faq">{faq_html}</div>
 </div>
</section>

<section class="inquiry" id="quote" style="background:var(--paper)">
 <div class="wrap split">
  <div class="reveal">
   <span class="kicker">Free quote</span>
   <h2>Tell us about the job.</h2>
   <p class="lead" style="margin:1rem 0 1.6rem">Name, number, email — that's it. Jordan will call you back to talk through the job and give you an upfront price.</p>
   <div class="promise-bar">{IC['clock']}<span>Response within one business day — guaranteed.</span></div>
   <p style="margin-top:1.6rem">Prefer to talk? <a href="{BIZ['phone_href']}"><b>{BIZ['phone']}</b></a><br>Or email <a href="mailto:{BIZ['email']}">{BIZ['email']}</a></p>
  </div>
  <div class="form-card reveal">{lead_form("hq")}</div>
 </div>
</section>

<section class="final-cta">
 <div class="wrap reveal">
  <span class="kicker" style="background:rgba(255,255,255,.1);border-color:rgba(255,255,255,.22);color:#F0C9A0">No obligation. No runaround.</span>
  <h2>Ready for an electrician who turns up?</h2>
  <p class="lead">Free quotes across the Northern Rivers. Upfront pricing. Workmanship guaranteed.</p>
  <div class="glow-wrap"><a class="btn btn-brass btn-lg" href="/contact.html">Get a Free Quote</a></div>
  <p class="sub">Or call Jordan now — <a href="{BIZ['phone_href']}" style="color:#F0C9A0;font-weight:700">{BIZ['phone']}</a> · 24/7 for emergencies</p>
 </div>
</section>
</main>""" + footer()
    write("/index.html", html)

# ---------------------------------------------------------------- contact (ads landing)
def build_contact():
    schema = crumbs_schema([("Home","/"),("Contact","/contact.html")])
    html = head(
      "Free Electrician Quote — Mullumbimby & Byron Bay | Town & Country Electrical",
      "Get a free quote from a licensed Northern Rivers electrician. Upfront pricing, response within one business day, 24/7 emergencies. Call 0405 305 671.",
      "/contact.html", schema) + header_nav("contact") + f"""
<div class="popup" id="lead-popup" role="dialog" aria-modal="true" aria-label="Get a free quote">
 <div class="popup-bg"></div>
 <div class="popup-card">
  <button class="popup-x" aria-label="Close">×</button>
  <span class="kicker">Free quote, fast</span>
  <h3 style="font-size:1.5rem;margin-bottom:.4rem">Get your free electrical quote</h3>
  <p style="color:var(--muted);margin-bottom:1.2rem">Leave your details and Jordan will call you back — usually same day.</p>
  {lead_form("pp", compact=True)}
 </div>
</div>
<main id="main">
<section class="page-hero">
 <div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">/</span>Contact</nav>
  <h1 style="font-size:clamp(2.2rem,4.6vw,4rem)">Let's get your job sorted.</h1>
  <p class="lead" style="color:rgba(255,255,255,.85);margin-top:1rem">Free quotes · Upfront pricing · Response within one business day</p>
 </div>
</section>
<section style="padding-top:clamp(48px,6vw,80px)">
 <div class="wrap split">
  <div class="form-card reveal">
   <h2 style="font-size:1.6rem;margin-bottom:.4rem">Request your free quote</h2>
   <p style="color:var(--muted);margin-bottom:1.4rem">Takes 30 seconds. No obligation.</p>
   {lead_form("cf")}
  </div>
  <div class="reveal">
   <span class="kicker">Direct lines</span>
   <h2 style="font-size:1.8rem">Talk to Jordan.</h2>
   <p style="margin:1rem 0">Owner, licensed electrician, and the person who actually answers this phone.</p>
   <p style="font-family:var(--font-display);font-weight:800;font-size:1.7rem"><a href="{BIZ['phone_href']}" style="text-decoration:none">{BIZ['phone']}</a></p>
   <p style="margin:.4rem 0 1.6rem"><a href="mailto:{BIZ['email']}">{BIZ['email']}</a></p>
   <div class="promise-bar">{IC['clock']}<span>Every enquiry answered within one business day. Emergencies: 24/7.</span></div>
   <h3 style="margin-top:2.2rem">Opening hours</h3>
   <div class="hours"><b>Mon–Sun</b><span>Open 24 hours — emergency electrician available every day</span></div>
   <h3 style="margin-top:2.2rem">Find us</h3>
   <p style="margin-bottom:1rem">Based in Mullumbimby NSW 2482, servicing the entire Northern Rivers.<br>
   <a href="https://www.google.com/maps/dir/?api=1&destination=Mullumbimby+NSW+2482" rel="noopener" target="_blank"><b>Get directions →</b></a></p>
   <div class="map-wrap"><iframe title="Map — Town & Country Electrical Co., Mullumbimby NSW" src="https://maps.google.com/maps?q=Mullumbimby%20NSW%202482&z=11&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
  </div>
 </div>
</section>
<section style="background:var(--surface);padding:clamp(48px,6vw,80px) 0">
 <div class="wrap reveal" style="text-align:center;max-width:720px;margin:0 auto">
  <span class="kicker">Service area</span>
  <h2 style="font-size:clamp(1.6rem,2.8vw,2.4rem)">Servicing the entire Northern Rivers</h2>
  <p style="margin-top:1rem;color:var(--muted)">{" · ".join(AREAS_ALL)} — and everywhere in between.</p>
 </div>
</section>
</main>""" + footer()
    write("/contact.html", html)

# ---------------------------------------------------------------- about
def build_about():
    schema = crumbs_schema([("Home","/"),("About","/about.html")])
    html = head(
      "About Us — Jordan Giuffre, Licensed Electrician | Town & Country Electrical Co.",
      "Meet Jordan Giuffre, owner of Town & Country Electrical Co. — a family-run, licensed and insured electrical business based in Mullumbimby, Northern Rivers NSW.",
      "/about.html", schema) + header_nav("about") + f"""
<main id="main">
<section class="page-hero">
 <div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">/</span>About</nav>
  <h1 style="font-size:clamp(2.2rem,4.6vw,4rem)">Family run. Northern Rivers born.</h1>
 </div>
</section>
<section>
 <div class="wrap split">
  <div class="media mask reveal"><img src="{PHOTOS['owner']}" alt="Jordan Giuffre, owner and licensed electrician at Town & Country Electrical Co." loading="lazy"></div>
  <div class="reveal prose">
   <span class="kicker">Our story</span>
   <h2 style="margin-top:0">Meet Jordan.</h2>
   <p>Town &amp; Country Electrical Co. is a locally owned and operated electrical business based in Mullumbimby, servicing Byron Bay and the surrounding Northern Rivers.</p>
   <p>Owner and licensed electrician <b>Jordan Giuffre</b> brings experience across residential construction, renovations, maintenance and architectural electrical work. Whether it's a small repair, a lighting upgrade or the complete electrical scope of a renovation, Jordan takes pride in delivering safe, practical solutions and quality workmanship.</p>
   <p>As an owner-operated business, you deal directly with Jordan from your first enquiry to the completion of your job — clear communication, honest advice and reliable service tailored to your home.</p>
   <ul class="check-list">
    <li>Locally owned and operated</li>
    <li>Licensed and insured electrician</li>
    <li>Friendly, personal service</li>
    <li>Clear and honest communication</li>
    <li>Quality workmanship with attention to detail</li>
   </ul>
  </div>
 </div>
</section>
<section style="background:var(--surface)">
 <div class="wrap">
  <div class="reveal" style="max-width:720px">
   <span class="kicker">The plus story</span>
   <h2>Why "Town &amp; Country"?</h2>
   <p style="margin-top:1rem">Because that's the patch. From town jobs in Mullumbimby and Byron Bay to properties tucked up in the hinterland — the Northern Rivers is both town <em>and</em> country, and we service every bit of it. It's the community we live in, shop in, and answer the phone for at 2am when a storm takes out someone's power.</p>
   <p style="margin-top:.8rem">Choosing a local owner-operator means your money stays in the region — and your electrician's reputation rides on every single job.</p>
  </div>
  <div class="promise-bar reveal" style="max-width:720px">{IC['shield']}<span><b>Our guarantee:</b> workmanship guaranteed on every job. If it's not right, we come back and make it right.</span></div>
 </div>
</section>
<section class="final-cta">
 <div class="wrap reveal">
  <h2>Work with a local you can count on.</h2>
  <div class="glow-wrap" style="margin-top:1.6rem"><a class="btn btn-brass btn-lg" href="/contact.html">Get a Free Quote</a></div>
  <p class="sub"><a href="{BIZ['phone_href']}" style="color:#F0C9A0;font-weight:700">{BIZ['phone']}</a> · {BIZ['email']}</p>
 </div>
</section>
</main>""" + footer()
    write("/about.html", html)

# ---------------------------------------------------------------- services hub + pages
def build_services():
    cards = ""
    for slug,d in SERVICES.items():
        cards += f"""<div class="blog-card reveal"><img src="{d['img']}" alt="{d['name']} — {ALT}" loading="lazy">
<div class="bc-body"><span class="meta">{d['tag']}</span><h3>{d['name']}</h3><p>{d['blurb']}</p>
<a href="/services/{slug}.html">View service &amp; gallery →</a></div></div>"""
    schema = crumbs_schema([("Home","/"),("Services","/services.html")])
    html = head(
      "Electrical Services Northern Rivers | Town & Country Electrical Co.",
      "Residential electrical, repairs, lighting, EV chargers, switchboards, smoke alarms & 24/7 emergencies across Mullumbimby, Byron Bay & the Northern Rivers.",
      "/services.html", schema) + header_nav("services") + f"""
<main id="main">
<section class="page-hero">
 <div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">/</span>Services</nav>
  <h1 style="font-size:clamp(2.2rem,4.6vw,4rem)">Every residential job, covered.</h1>
  <p class="lead" style="color:rgba(255,255,255,.85);margin-top:1rem">Nine services. One licensed electrician. Zero runaround.</p>
 </div>
</section>
<section><div class="wrap"><div class="card-grid">{cards}</div></div></section>
<section class="final-cta">
 <div class="wrap reveal"><h2>Not sure what you need?</h2>
 <p class="lead">Describe the problem — Jordan will tell you what it takes to fix it.</p>
 <div class="glow-wrap"><a class="btn btn-brass btn-lg" href="/contact.html">Get a Free Quote</a></div>
 <p class="sub"><a href="{BIZ['phone_href']}" style="color:#F0C9A0;font-weight:700">{BIZ['phone']}</a></p></div>
</section>
</main>""" + footer()
    write("/services.html", html)

    for slug,d in SERVICES.items():
        title = f"{d['name']} {BIZ['region']} | {BIZ['short']}"
        desc = (d['blurb'][:150] + " Servicing Mullumbimby, Byron Bay & Northern Rivers.")[:158]
        svc_schema = f"""<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Service","name":"{d['name']}","serviceType":"{d['kw']}","provider":{{"@type":"Electrician","name":"{BIZ['name']}","telephone":"+61405305671"}},"areaServed":"Northern Rivers NSW","url":"{BASE}/services/{slug}.html"}}</script>""" + crumbs_schema([("Home","/"),("Services","/services.html"),(d['name'],f"/services/{slug}.html")])
        points = "".join(f"<li>{p}</li>" for p in d["points"])
        related = [s for s in SERVICES if s != slug][:3]
        rel_html = " · ".join(f'<a href="/services/{r}.html">{SERVICES[r]["name"]}</a>' for r in related)
        html = head(title, desc, f"/services/{slug}.html", svc_schema) + header_nav("services") + f"""
<main id="main">
<section class="page-hero">
 <div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">/</span><a href="/services.html">Services</a><span class="sep">/</span>{d['name']}</nav>
  <span class="kicker" style="background:rgba(255,255,255,.1);border-color:rgba(255,255,255,.22);color:#F0C9A0">{d['tag']}</span>
  <h1 style="font-size:clamp(2.1rem,4.2vw,3.6rem)">{d['name']}</h1>
  <p class="lead" style="color:rgba(255,255,255,.85);margin-top:1rem">{d['blurb']}</p>
  <div style="margin-top:1.8rem;display:flex;gap:1rem;flex-wrap:wrap"><a class="btn btn-brass" href="/contact.html">Get a Free Quote</a><a class="btn btn-ghost" href="{BIZ['phone_href']}">{BIZ['phone']}</a></div>
 </div>
</section>
<section>
 <div class="wrap split">
  <div class="reveal prose">
   <h2 style="margin-top:0">What's included</h2>
   <p>{d['body']}</p>
   <ul class="check-list">{points}</ul>
   <div class="promise-bar">{IC['clock']}<span>Enquiries answered within one business day. Workmanship guaranteed.</span></div>
  </div>
  <div class="media mask reveal"><img src="{d['img']}" alt="{d['name']} — {ALT}" loading="lazy"></div>
 </div>
</section>
<section style="background:var(--surface)">
 <div class="wrap">
  <div class="reveal"><span class="kicker">Gallery</span><h2>{d['name']} — recent work</h2></div>
  {gal_html(d['gallery'])}
 </div>
</section>
<section class="final-cta">
 <div class="wrap reveal">
  <h2>Need {d['name'].lower()} in the Northern Rivers?</h2>
  <div class="glow-wrap" style="margin-top:1.4rem"><a class="btn btn-brass btn-lg" href="/contact.html">Get a Free Quote</a></div>
  <p class="sub">Related: {rel_html}</p>
 </div>
</section>
</main>""" + footer()
        write(f"/services/{slug}.html", html)

# ---------------------------------------------------------------- areas
def build_areas():
    for slug,d in AREA_PAGES.items():
        title = f"Electrician {d['name']} NSW | {BIZ['short']}"
        desc = f"Licensed local electrician servicing {d['name']} — repairs, lighting, switchboards, EV chargers & 24/7 emergencies. Upfront pricing. Call {BIZ['phone']}."
        schema = crumbs_schema([("Home","/"),(f"Electrician {d['name']}",f"/areas/{slug}.html")])
        svc_links = "".join(f'<div class="bene-card reveal"><h3><a href="/services/{s}.html" style="text-decoration:none">{v["name"]}</a></h3><p>{v["blurb"]}</p></div>' for s,v in list(SERVICES.items())[:6])
        html = head(title, desc, f"/areas/{slug}.html", schema) + header_nav() + f"""
<main id="main">
<section class="page-hero">
 <div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">/</span>Service Areas<span class="sep">/</span>{d['name']}</nav>
  <h1 style="font-size:clamp(2.1rem,4.2vw,3.6rem)">Your local electrician in {d['name']}</h1>
  <p class="lead" style="color:rgba(255,255,255,.85);margin-top:1rem">Licensed &amp; insured · Upfront pricing · 24/7 emergencies</p>
  <div style="margin-top:1.8rem;display:flex;gap:1rem;flex-wrap:wrap"><a class="btn btn-brass" href="/contact.html">Get a Free Quote</a><a class="btn btn-ghost" href="{BIZ['phone_href']}">{BIZ['phone']}</a></div>
 </div>
</section>
<section><div class="wrap reveal prose">
 <span class="kicker">{d['name']} · Northern Rivers</span>
 <h2 style="margin-top:.4rem">Electrical services in {d['name']}</h2>
 <p>{d['intro']}</p>
 <p>Every job is completed by owner and licensed electrician Jordan Giuffre, with upfront pricing, a Certificate of Compliance where applicable, and a workmanship guarantee. Read more <a href="/about.html">about the business</a> or browse <a href="/case-studies.html">recent project case studies</a>.</p>
</div></section>
<section style="background:var(--surface)"><div class="wrap">
 <div class="reveal"><h2>Popular services in {d['name']}</h2></div>
 <div class="bene" style="margin-top:2rem">{svc_links}</div>
</div></section>
<section class="final-cta"><div class="wrap reveal">
 <h2>Need an electrician in {d['name']}?</h2>
 <div class="glow-wrap" style="margin-top:1.4rem"><a class="btn btn-brass btn-lg" href="/contact.html">Get a Free Quote</a></div>
 <p class="sub"><a href="{BIZ['phone_href']}" style="color:#F0C9A0;font-weight:700">{BIZ['phone']}</a> · 24/7 emergencies</p>
</div></section>
</main>""" + footer()
        write(f"/areas/{slug}.html", html)

# ---------------------------------------------------------------- case studies
def build_cases():
    cases = [
     {"img":"avoca","img2":"garden","title":"Outdoor & Garden Lighting Transformation","where":"Northern Rivers","tag":"Lighting & Power",
      "challenge":"A dark outdoor area that went unused after sunset, with no existing outdoor circuits.",
      "work":"New weatherproof circuits, warm low-glare garden and feature lighting, and switching set up so the whole scene comes on with one press.",
      "result":"An outdoor space the owners actually use at night — safe paths, zero glare, and lighting that flatters the garden rather than floodlighting it."},
     {"img":"vanity","img2":"bath","title":"Bathroom Renovation Electrical Fit-out","where":"Northern Rivers","tag":"Renovation",
      "challenge":"A full bathroom renovation needing modern lighting, ventilation and power in a wet-area environment where compliance rules are strict.",
      "work":"LED strip lighting at the vanity, IP-rated fittings, heat-light-fan unit, and safe placement of power to meet wet-area zone requirements — coordinated with the builder and tiler.",
      "result":"A hotel-grade finish with every fitting compliant, documented and covered by a Certificate of Compliance."},
     {"img":"fan","img2":"pendant2","title":"Whole-Home Ceiling Fans & Lighting Upgrade","where":"Northern Rivers","tag":"Comfort upgrade",
      "challenge":"A warm Northern Rivers home relying entirely on aircon, with dated lighting throughout.",
      "work":"Quality DC ceiling fans installed through bedrooms and living areas, plus a lighting refresh including feature pendants.",
      "result":"Cooler rooms for cents a day and a five-star review from the owner — the exact job Lachlan praised in his verified review."},
    ]
    blocks = ""
    for i,c in enumerate(cases):
        flip = " flip" if i%2 else ""
        blocks += f"""<div class="srv-row{flip}">
 <div class="media mask reveal"><img src="{PHOTOS[c['img']]}" alt="{c['title']} — {ALT}" loading="lazy"></div>
 <div class="reveal"><span class="tag">{c['tag']} · {c['where']}</span><h3>{c['title']}</h3>
 <p><b>The brief:</b> {c['challenge']}</p>
 <p style="margin-top:.6rem"><b>The work:</b> {c['work']}</p>
 <p style="margin-top:.6rem"><b>The result:</b> {c['result']}</p></div>
</div>"""
    schema = crumbs_schema([("Home","/"),("Case Studies","/case-studies.html")])
    html = head(
      "Case Studies — Recent Electrical Projects | Town & Country Electrical Co.",
      "Recent electrical projects across the Northern Rivers: outdoor lighting, bathroom renovation fit-outs and whole-home comfort upgrades by Town & Country Electrical.",
      "/case-studies.html", schema) + header_nav() + f"""
<main id="main">
<section class="page-hero">
 <div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">/</span>Case Studies</nav>
  <h1 style="font-size:clamp(2.2rem,4.6vw,4rem)">The work speaks. We'll translate.</h1>
  <p class="lead" style="color:rgba(255,255,255,.85);margin-top:1rem">Real projects from around the Northern Rivers — what the job was, what we did, how it landed.</p>
 </div>
</section>
<section><div class="wrap">{blocks}</div></section>
<section style="background:var(--surface)"><div class="wrap">
 <div class="reveal"><span class="kicker">More from the tools</span><h2>Gallery</h2></div>
 {gal_html(["w1","w3","w4","w5","i5879","i6370","i5713","i0773"])}
</div></section>
<section class="final-cta"><div class="wrap reveal">
 <h2>Your place could be next.</h2>
 <div class="glow-wrap" style="margin-top:1.4rem"><a class="btn btn-brass btn-lg" href="/contact.html">Get a Free Quote</a></div>
 <p class="sub"><a href="{BIZ['phone_href']}" style="color:#F0C9A0;font-weight:700">{BIZ['phone']}</a></p>
</div></section>
</main>""" + footer()
    write("/case-studies.html", html)

# ---------------------------------------------------------------- blog
def build_blog():
    cards = ""
    for slug,p in BLOG.items():
        cards += f"""<article class="blog-card reveal"><img src="{PHOTOS[p['img']]}" alt="{p['title']}" loading="lazy">
<div class="bc-body"><span class="meta">{p['tagline']}</span><h3>{p['title']}</h3><p>{p['desc']}</p>
<a href="/blog/{slug}.html">Read article →</a></div></article>"""
    schema = crumbs_schema([("Home","/"),("Blog","/blog.html")])
    html = head(
      "Electrical Advice for Northern Rivers Homes | Town & Country Electrical Blog",
      "Practical electrical advice from a licensed Northern Rivers electrician — EV chargers, switchboards, smoke alarms, lighting and emergency know-how.",
      "/blog.html", schema) + header_nav("blog") + f"""
<main id="main">
<section class="page-hero"><div class="wrap">
 <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">/</span>Blog</nav>
 <h1 style="font-size:clamp(2.2rem,4.6vw,4rem)">Straight answers, written down.</h1>
 <p class="lead" style="color:rgba(255,255,255,.85);margin-top:1rem">Practical electrical advice for Northern Rivers homes — no jargon, no scare campaigns.</p>
</div></section>
<section><div class="wrap"><div class="card-grid">{cards}</div></div></section>
</main>""" + footer()
    write("/blog.html", html)

    for slug,p in BLOG.items():
        art_schema = f"""<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BlogPosting","headline":"{p['title']}","description":"{p['desc']}","image":"{PHOTOS[p['img']]}","datePublished":"{p['date']}","author":{{"@type":"Person","name":"{BIZ['owner']}"}},"publisher":{{"@type":"Organization","name":"{BIZ['name']}","logo":{{"@type":"ImageObject","url":"{LOGO}"}}}},"mainEntityOfPage":"{BASE}/blog/{slug}.html"}}</script>""" + crumbs_schema([("Home","/"),("Blog","/blog.html"),(p['title'],f"/blog/{slug}.html")])
        html = head(p['title'] + " | Town & Country Electrical", p['desc'], f"/blog/{slug}.html", art_schema, "article") + header_nav("blog") + f"""
<main id="main">
<section class="page-hero"><div class="wrap">
 <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">/</span><a href="/blog.html">Blog</a><span class="sep">/</span>{p['tagline']}</nav>
 <span class="kicker" style="background:rgba(255,255,255,.1);border-color:rgba(255,255,255,.22);color:#F0C9A0">{p['tagline']} · {p['date']}</span>
 <h1 style="font-size:clamp(1.9rem,3.8vw,3.2rem);max-width:22ch">{p['title']}</h1>
</div></section>
<section><div class="wrap">
 <div class="media reveal" style="max-width:900px;margin-bottom:3rem"><img src="{PHOTOS[p['img']]}" alt="{p['title']}" style="aspect-ratio:16/8"></div>
 <div class="prose reveal">{p['body']}
 <p style="margin-top:2rem;font-size:.9rem;color:var(--muted)">Written by {BIZ['owner']}, owner &amp; licensed electrician, {BIZ['name']} — Mullumbimby NSW. General information only, not advice for your specific installation.</p></div>
</div></section>
<section class="final-cta"><div class="wrap reveal">
 <h2>Got an electrical job on the list?</h2>
 <div class="glow-wrap" style="margin-top:1.4rem"><a class="btn btn-brass btn-lg" href="/contact.html">Get a Free Quote</a></div>
 <p class="sub"><a href="{BIZ['phone_href']}" style="color:#F0C9A0;font-weight:700">{BIZ['phone']}</a></p>
</div></section>
</main>""" + footer()
        write(f"/blog/{slug}.html", html)

# ---------------------------------------------------------------- utility pages
def build_util():
    # thank you
    html = head("Thanks — We're On It | Town & Country Electrical Co.",
      "Your enquiry has been received. Jordan will be in touch within one business day.",
      "/thank-you.html") + header_nav() + f"""
<main id="main"><section class="err-hero"><div class="wrap reveal">
 <span class="kicker">Enquiry received</span>
 <h1 style="font-size:clamp(2rem,5vw,3.6rem)">Beauty. You're on the list.</h1>
 <p class="lead" style="margin:1.2rem auto 2rem;max-width:44ch">Jordan will call or email you back within one business day — usually much faster. If it's urgent, don't wait:</p>
 <a class="btn btn-primary btn-lg" href="{BIZ['phone_href']}">Call {BIZ['phone']} now</a>
 <p style="margin-top:2rem"><a href="/blog.html">Read some electrical know-how while you wait →</a></p>
</div></section></main>""" + footer()
    # noindex thank-you
    html = html.replace('<meta name="robots" content="index, follow">','<meta name="robots" content="noindex, follow">')
    write("/thank-you.html", html)

    # 404
    html = head("Page Not Found | Town & Country Electrical Co.",
      "That page has tripped a breaker. Head back to the Town & Country Electrical homepage.",
      "/404.html") + header_nav() + f"""
<main id="main"><section class="err-hero"><div class="wrap">
 <div class="code">404</div>
 <h1 style="font-size:clamp(1.8rem,4vw,3rem)">This page has tripped a breaker.</h1>
 <p class="lead" style="margin:1.2rem auto 2rem;max-width:44ch">The page you're after isn't here — but the electrician you're after definitely is.</p>
 <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap">
  <a class="btn btn-primary" href="/">Back to home</a>
  <a class="btn btn-brass" href="/contact.html">Get a Free Quote</a>
 </div>
</div></section></main>""" + footer()
    html = html.replace('<meta name="robots" content="index, follow">','<meta name="robots" content="noindex, follow">')
    write("/404.html", html)

    # privacy
    body = f"""<p>Last updated: {TODAY}</p>
<p>Town &amp; Country Electrical Co. ("we", "us") respects your privacy. This policy explains how we handle personal information collected through this website and in the course of providing electrical services, in line with the Australian Privacy Principles under the Privacy Act 1988 (Cth).</p>
<h2>What we collect</h2>
<p>When you contact us we may collect your name, phone number, email address, property address and details of the work you're enquiring about. Our website also collects limited analytics data (pages visited, device type) if you consent to analytics cookies.</p>
<h2>How we use it</h2>
<ul><li>To respond to enquiries and provide quotes</li><li>To schedule, perform and invoice electrical work</li><li>To meet our legal obligations (including compliance certification records)</li><li>To improve this website (analytics, with your consent)</li></ul>
<h2>Forms and third parties</h2>
<p>Enquiry forms on this site may be processed by our customer-management platform, which stores your details securely so we can respond to you. We do not sell or rent personal information to anyone.</p>
<h2>Cookies</h2>
<p>Essential cookies keep the site working. Analytics cookies (Google Analytics) run only if you accept them in the cookie banner, and you can withdraw consent by clearing your browser data.</p>
<h2>Access and contact</h2>
<p>You can request access to, or correction of, the personal information we hold about you at any time — email <a href="mailto:{BIZ['email']}">{BIZ['email']}</a> or call {BIZ['phone']}.</p>"""
    html = head("Privacy Policy | Town & Country Electrical Co.",
      "How Town & Country Electrical Co. collects, uses and protects your personal information.",
      "/privacy-policy.html") + header_nav() + f"""
<main id="main"><section class="page-hero"><div class="wrap">
 <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">/</span>Privacy Policy</nav>
 <h1 style="font-size:clamp(2rem,4vw,3.2rem)">Privacy Policy</h1></div></section>
<section><div class="wrap prose reveal">{body}</div></section></main>""" + footer()
    write("/privacy-policy.html", html)

    # terms
    body = f"""<p>Last updated: {TODAY}</p>
<h2>About these terms</h2>
<p>These terms cover your use of this website and set out the general basis on which Town &amp; Country Electrical Co. provides residential electrical services across the Northern Rivers, NSW.</p>
<h2>Quotes and pricing</h2>
<p>Quotes are provided free of charge and remain valid for 30 days unless stated otherwise. Pricing is provided upfront before work begins. If unforeseen conditions change the scope (for example, concealed wiring faults discovered during work), we'll pause and discuss revised pricing with you before continuing.</p>
<h2>Payment</h2>
<p>Payment is accepted by bank transfer or card. Invoices are issued electronically with itemised line items and are payable within the terms stated on the invoice.</p>
<h2>Workmanship guarantee</h2>
<p>Our workmanship is guaranteed. If a fault arises from work we performed, contact us and we will return to rectify it at no charge. This guarantee sits alongside, and does not limit, your rights under the Australian Consumer Law and applicable manufacturer warranties on supplied products.</p>
<h2>Compliance</h2>
<p>All electrical work is performed by a licensed electrician and completed to Australian standards, with a Certificate of Compliance (CCEW) issued for notifiable work.</p>
<h2>Website content</h2>
<p>Content on this site is general information, not advice for your specific installation. While we keep it accurate and current, we make no warranties about completeness. Logos, images and text are the property of Town &amp; Country Electrical Co. and may not be reproduced without permission.</p>
<h2>Contact</h2>
<p>Questions about these terms: <a href="mailto:{BIZ['email']}">{BIZ['email']}</a> or {BIZ['phone']}.</p>"""
    html = head("Terms of Service | Town & Country Electrical Co.",
      "Terms of service for Town & Country Electrical Co. — quotes, payment, workmanship guarantee and compliance.",
      "/terms.html") + header_nav() + f"""
<main id="main"><section class="page-hero"><div class="wrap">
 <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span class="sep">/</span>Terms of Service</nav>
 <h1 style="font-size:clamp(2rem,4vw,3.2rem)">Terms of Service</h1></div></section>
<section><div class="wrap prose reveal">{body}</div></section></main>""" + footer()
    write("/terms.html", html)

# ---------------------------------------------------------------- static files
def build_static():
    pages = (["/", "/contact.html", "/about.html", "/services.html", "/case-studies.html", "/blog.html", "/privacy-policy.html", "/terms.html"]
             + [f"/services/{s}.html" for s in SERVICES]
             + [f"/areas/{s}.html" for s in AREA_PAGES]
             + [f"/blog/{s}.html" for s in BLOG])
    urls = "".join(f"<url><loc>{BASE}{p}</loc><lastmod>{TODAY}</lastmod></url>" for p in pages)
    write("/sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')

    write("/robots.txt", f"User-agent: *\nAllow: /\nDisallow: /thank-you.html\n\nSitemap: {BASE}/sitemap.xml\n")

    write("/llms.txt", f"""# {BIZ['name']}

> Family-run, licensed and insured residential electrician based in Mullumbimby NSW 2482, servicing the entire Northern Rivers: {", ".join(AREAS_ALL)}. Owner-operated by licensed electrician Jordan Giuffre. Upfront pricing, workmanship guaranteed, 24/7 emergency call-outs. Phone {BIZ['phone']}. Email {BIZ['email']}.

## Services
- [Residential Electrical]({BASE}/services/residential-electrical.html): new builds & renovation wiring
- [Electrical Repairs & Fault Finding]({BASE}/services/electrical-repairs.html)
- [Lighting & Power]({BASE}/services/lighting-and-power.html)
- [EV Charger Installation]({BASE}/services/ev-charger-installation.html)
- [Hot Water Repairs]({BASE}/services/hot-water-repairs.html)
- [Switchboard Upgrades]({BASE}/services/switchboard-upgrades.html)
- [Smoke Alarm Installation]({BASE}/services/smoke-alarms.html)
- [Appliance Installation]({BASE}/services/appliance-installation.html)
- [24/7 Emergency Electrician]({BASE}/services/emergency-electrician.html)

## Key pages
- [Contact / Free Quote]({BASE}/contact.html)
- [About — Jordan Giuffre]({BASE}/about.html)
- [Case Studies]({BASE}/case-studies.html)
- [Blog]({BASE}/blog.html)

## Facts
- Rated 5.0 from verified customer reviews
- Licensed & insured; Certificates of Compliance issued for notifiable work
- Response to all enquiries within one business day
- Payment: bank transfer or card
""")

    write("/favicon.svg", """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#701322"/><path d="M36 8 18 36h11l-3 20 20-30H34l2-18z" fill="#F0C9A0"/></svg>""")

    write("/.nojekyll", "")

for fn in (build_index, build_contact, build_about, build_services, build_areas, build_cases, build_blog, build_util, build_static):
    fn()
print("DONE — base:", BASE)
