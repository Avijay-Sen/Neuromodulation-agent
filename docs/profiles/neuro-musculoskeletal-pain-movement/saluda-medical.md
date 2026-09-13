# Saluda Medical

## Company Profile

**Company Name:** Saluda Medical, Inc.  
**HQ Location:** Sydney, Australia (headquarters); US operations: Boston, Massachusetts  
**Founded:** 2013  
**Funding Raised:** $100+ million (Series B, 2018); backed by venture investors and strategic partners  
**Website:** https://www.saludamedical.com

---

## Clinical Indication

**Disorder Category:** Neuro-Musculoskeletal / Pain / Movement  
**Primary Indication:** Chronic back and leg pain (failed back surgery syndrome, post-laminectomy pain)  
**Secondary Indications:** Peripheral neuropathic pain, failed neck surgery syndrome

---

## Target Nerve or Mechanism

**Anatomical Target:** Dorsal root ganglia (DRG) or dorsal column spinal cord  
**Delivery Mechanism:** Implantable spinal cord stimulation (SCS) lead with closed-loop feedback  
**Modality:** Electrical stimulation via percutaneous epidural lead; evoked compound action potential (ECAP) recording for feedback
**Device Name:** Evoke System

---

## Biological Basis

Chronic pain involves sensitized nociceptors and aberrant spinal dorsal horn processing. Spinal cord stimulation (SCS) is thought to work via "gate control theory" — electrical stimulation of large-diameter sensory fibers (Aβ) activates inhibitory interneurons in the dorsal horn, thereby blocking pain-signal transmission (C-fiber mediated pain). Closed-loop SCS adjusts stimulation parameters in real-time based on neural feedback (ECAP amplitude), potentially optimizing pain relief and reducing over-stimulation.

**Key Reference:**  
- Melzack, R., & Wall, P.D. (1965). "Pain mechanisms: A new theory." *Science*, 150(3699), 971–979. DOI: 10.1126/science.150.3699.971

**Modern Understanding:**  
- SCS mechanisms involve supraspinal and descending modulatory pathways (not just local gating)
- Patient-specific optimization of stimulation (e.g., frequency, pulse width) improves clinical outcomes; closed-loop systems promise automated optimization

---

## Market Size & Affected Population

**Prevalence:**  
- Chronic back pain: ~540 million globally; ~100 million in US  
- Failed back surgery syndrome (FBSS): 10–40% of back surgery patients (~5–20M globally)  
- Neuropathic pain: ~50–100 million globally

**Addressable Population:**  
- Candidates for SCS: ~5–10% of chronic pain population (~10–50M globally)  
- Refractory to medical management: ~2–5M in US alone  

**Market Size Estimate:**  
- Global SCS market: ~$3–4 billion annually (2024)  
- Closed-loop SCS devices (Saluda, others): emerging segment, projected $500M–2B by 2030  
- Saluda market share estimate: ~5–15% if regulatory approval and reimbursement succeed  

**Sources:**  
- Allied Market Research, Spinal Cord Stimulation Market Report, 2024  
- WHO Global Pain Report, 2023

---

## Technology Description

### How It Works (Step-by-Step)

1. **Surgical Implantation:**  
   - Minimally invasive percutaneous procedure: neurosurgeon inserts thin catheter epidurally via lumbar approach  
   - Lead (electrode array) threaded into epidural space; positioned at spinal level corresponding to pain distribution (T8-L1 for lower back pain)
   - External trial phase: Patient tests SCS efficacy with external pulse generator for 7 days; if ≥50% pain relief, proceeds to permanent implant
   - Permanent implant: Receiver/stimulator implanted subcutaneously (buttock or abdomen); lead remains in spinal canal

2. **Baseline Evoked Response Recording:**  
   - System measures evoked compound action potential (ECAP) — the electrical response of spinal cord to stimulation
   - Baseline ECAP amplitude established for each stimulation parameter set
   - Higher ECAP amplitude typically correlates with better clinical pain relief

3. **Closed-Loop Feedback Algorithm:**  
   - During each stimulation train, system records ECAP amplitude in real-time
   - Algorithm compares current ECAP to baseline:  
     - If ECAP decreases (e.g., due to electrode drift or tissue changes), stimulation intensity automatically increases to maintain target ECAP
     - If ECAP increases, intensity can be reduced to minimize over-stimulation
   - Adjustments occur dynamically over hours/days

4. **Patient Use:**  
   - Wireless remote allows patient to turn device on/off and adjust stimulation intensity
   - Typical usage: 4–12 hours/day depending on pain pattern (e.g., more during work hours)
   - Rechargeable battery in implanted unit; external charger placed on skin nightly

5. **Long-term Monitoring:**  
   - Clinic visits every 3–6 months: firmware updates, pain reassessment, ECAP trending
   - ECAP data allows clinician to predict device adjustment needs before patient reports problems

### Hardware Components

- **Implantable Stimulator:** Compact (~65 cm³), titanium-sealed
- **Lead:** Quadripolar or octo-pole electrode array (~40–60 mm long)
- **Telemetry:** Wireless communication to external remote (Bluetooth, proprietary protocol)
- **Battery:** Rechargeable lithium-ion; 5–8 year lifespan (replacement requires surgery)
- **Firmware:** Proprietary algorithms for ECAP recording, threshold setting, and closed-loop adjustment

---

## Novelty & Differentiation

### vs. Standard of Care (Open-Loop SCS)

- **Traditional SCS (open-loop):** Stimulation parameters fixed after implant; no feedback; efficacy plateaus over time as tissue changes occur  
  - Pain relief: ~50% at 1 year; ~30–40% at 5 years (due to tolerance, lead migration)  
  - Revision surgeries common: ~25–30% of patients need device adjustments or replacement within 5 years
- **Saluda (closed-loop):** Automatically adjusts to maintain optimal neural response  
  - Potential to sustain pain relief longer and reduce revision surgeries  
  - Patient-centered: reduced manual adjustments

### vs. Other Closed-Loop SCS Companies

- **Saluda vs. Stimwave:** Stimwave focuses on wireless, fully-implantable SCS; Saluda emphasizes ECAP-based feedback
- **Saluda vs. Boston Scientific/Medtronic:** Incumbents beginning to develop closed-loop systems; Saluda is focused innovator with first-to-market ECAP feedback
- **Distinctive:** Proprietary ECAP-based closed-loop algorithm; strongest clinical trial data for closed-loop safety/efficacy to date

### vs. Non-Invasive Alternatives

- **Topical analgesics, NSAIDs:** First-line; inadequate for severe pain
- **Opioids:** Effective but addiction risk, side effects, regulatory scrutiny
- **Physical therapy/psychology:** Important but insufficient for FBSS
- **Saluda Advantage:** Offers meaningful pain relief (50–70%) when other options exhausted; minimally invasive; reversible (removal possible, though not commonly done)

---

## Limitations: Practical

**Surgical Considerations:**  
- Requires neurosurgical expertise; limited availability in rural/developing areas
- Perioperative complications: infection (~1–3%), spinal fluid leak (~1–2%), lead migration (~5–10%)
- Recovery period: 2–4 weeks before full activity

**Cost & Reimbursement:**  
- Device + surgery: $25k–50k USD (varies by facility)
- Medicare/insurance coverage: available but prior authorization often required
- Trial-then-implant model: ~$500–2k cost to patient if trial fails and insurance doesn't cover

**Patient Selection:**  
- Psychological screening required (depression, active substance use are relative contraindications)
- Patients must be able to follow safety precautions (avoid MRI without proper device interrogation, high-voltage exposure)
- Age: typically used in patients >45 years; rare in younger patients

**Maintenance Burden:**  
- Nightly charging (~2 hours per night indefinitely)
- Periodic clinic visits (quarterly initially, then annual)
- Battery replacement surgery (~10 years)
- Cannot use certain diagnostic imaging (MRI) without specialized programming

---

## Limitations: Theoretical & Readiness

**ECAP Interpretation:**  
- ECAP reflects spinal cord excitability but does not directly measure pain pathway activity
- Relationship between ECAP amplitude and clinical pain relief is correlative, not causal
- Risk that closed-loop algorithm optimizes for "device function" rather than patient pain outcomes

**Tolerance & Long-term Efficacy:**  
- Open-loop SCS shows 30–40% efficacy at 5 years; unclear if closed-loop's automated adjustments truly prevent tolerance
- Long-term data (>5 years) for Saluda/closed-loop systems not yet published
- Potential for central sensitization to persist despite optimized peripheral stimulation

**Individual Variability:**  
- Responders vs. non-responders poorly predictable pre-operatively
- ~20% of patients experience inadequate pain relief even after perfect lead placement and tuning

**Reimbursement Uncertainties:**  
- Closed-loop SCS is more expensive than traditional SCS; payers may require demonstration of improved outcomes (cost-effectiveness)
- Evidence comparing closed-loop vs. optimized open-loop SCS with frequent clinic adjustments still limited (2026)

---

## Regulatory Status

**FDA:**  
- **Approval:** Traditional SCS devices (Boston Scientific, Medtronic, Abbott) approved for chronic pain via 510(k) predicate pathway  
- **Saluda Status:** Seeking breakthrough device designation for closed-loop SCS; formal FDA pathway (likely 510(k) or De Novo) in progress
- **Timeline:** FDA clearance expected 2026–2027 if trial data supportive

**Clinical Trials:**  
- **Pivotal Trial (Evoke system):** Randomized, multi-center comparison of closed-loop vs. open-loop SCS for FBSS; interim results show non-inferiority to standard SCS with trend toward superior efficacy  
- **Trial Name:** PROSPECT study (Predictive Optimal SCS Efficiency Trial)
- **Endpoints:** Pain reduction (VAS), function (Oswestry Disability Index), revision surgery rates
- **Timeline:** Final results expected mid-2026

**International Status:**  
- CE mark approval in EU (via Medical Device Regulation) for closed-loop SCS as of 2024
- Clinical adoption in Australia, EU: limited but growing
- FDA approval would expand North American market significantly

---

## Sources

- **Saluda Medical Official:** https://www.saludamedical.com  
- **Gate Control Theory (Foundational):** Melzack, R., & Wall, P.D. (1965). "Pain mechanisms: A new theory." *Science*, 150(3699), 971–979. https://doi.org/10.1126/science.150.3699.971  
- **PROSPECT Trial Information:** ClinicalTrials.gov identifier NCT03892876 (search online for protocol and results)
- **SCS Market Data:** Allied Market Research, "Spinal Cord Stimulation Market Report, 2024"  
- **FDA CDRH Guidance:** https://www.fda.gov/medical-devices/ (510(k) and breakthrough device guidance)
- **WHO Pain Guidelines:** https://www.who.int/news-room/fact-sheets

---

**Profile Created:** 2026-09-13  
**Last Updated:** 2026-09-13
