# Blackrock Neurotech

## Company Profile

**Company Name:** Blackrock Neurotech (formerly Blackrock Microsystems)  
**HQ Location:** Salt Lake City, Utah, USA  
**Founded:** 2006  
**Funding Raised:** Not publicly disclosed (private company)  
**Website:** https://www.blackrockmicro.com

---

## Clinical Indication

**Disorder Category:** Cognitive Disorders / Neural Interface  
**Primary Indication:** Paralysis/Spinal Cord Injury (communication and device control via brain-computer interface)  
**Secondary Indications:** ALS, locked-in syndrome, brainstem stroke

---

## Target Nerve or Mechanism

**Anatomical Target:** Primary motor cortex (M1) and other cortical areas involved in movement planning  
**Delivery Mechanism:** Surgical craniotomy followed by intracortical implantation of microelectrode arrays; no removable external implant housing (electrodes remain fixed to scalp connector)  
**Recording Type:** Single-unit action potentials from individual neurons within 0.1–1 mm of each electrode tip  
**Interface:** 96-channel or 128-channel microelectrode grid ("Utah Array")

---

## Biological Basis

Voluntary movement is encoded in the primary motor cortex via distributed neural population activity. Individual neurons fire at rates proportional to intended movement direction and speed (population vector coding). Blackrock's microelectrodes record extracellular action potentials from dozens of neurons simultaneously, allowing real-time decoding of motor intent.

**Key Reference:**  
- Georgopoulos, A.P., Schwartz, A.B., & Kettner, R.E. (1986). "Neuronal population coding of movement direction." *Science*, 233(4771), 1416–1419. DOI: 10.1126/science.3749885

**Additional Context:**  
- Paralysis disrupts corticospinal motor output but leaves motor cortex neurons intact; their activity can still encode intended movements (learned over weeks of training).
- Motor imagery activates M1 in a topographic, task-relevant manner even without limb movement; decoding algorithms exploit this.

---

## Market Size & Affected Population

**Prevalence:**  
- ~5.5 million Americans living with paralysis (CDC, 2024)  
- ~16,000 new traumatic spinal cord injuries per year in the US  
- ~200,000+ Americans with ALS at any given time  
- Global: ~80 million with some form of paralysis

**Addressable Population:**  
- High-severity paralysis (C1–C4 tetraplegia or advanced ALS with locked-in features): ~1–2 million globally who could benefit from BCI communication/control
- Most require non-invasive solutions first (eye gaze, speech synthesis); intracortical BCI targets those who lose all voluntary motor control

**Market Size Estimate:**  
- Intracortical BCI market (all players combined): ~$50–100 million currently (2026)
- Projected growth: $6–10 billion by 2030–2035 *if* clinical adoption accelerates and reimbursement resolves
- Per-patient cost of Blackrock system (device + surgery + training): estimated $100k–200k upfront + $5k–10k annual support

**Sources:**  
- Allied Market Research. "Brain-Computer Interface (BCI) Market Size, Share & Trends 2024–2031."  
- Grand View Research. "Neurostimulation Market Report 2024."

---

## Technology Description

### How It Works (Step-by-Step)

1. **Surgical Implantation:**  
   - Neurosurgeon performs craniotomy over primary motor cortex (typically left hemisphere for right-handed patients)
   - Utah Array (96-pin microelectrode grid) is inserted perpendicular to cortical surface to a depth of ~1.5 mm
   - Connectors are sutured to scalp; patient wears percutaneous pedestal or wireless headcap for signal transmission

2. **Signal Recording:**  
   - Electrodes detect extracellular action potentials (voltage transients when neurons fire near the electrode)
   - Amplifiers filter (300 Hz–10 kHz bandpass) and digitize signals at 30 kHz sampling rate
   - Real-time spike detection identifies action potentials from individual neurons ("units")

3. **Decoding Algorithm:**  
   - Linear or non-linear decoders (e.g., Kalman filter, neural networks) map neural activity to intended movement (cursor position, velocity, or joint angles)
   - Requires supervised training: patient watches cursor move to targets on screen while imagining corresponding limb movements; algorithm learns association between neural firing patterns and intended movements
   - Decoder is personalized per patient; recalibration needed every 2–4 weeks to track signal drift

4. **Output:**  
   - Decoded movement commands drive:  
     - Cursor on screen (for typing, communication)  
     - Robotic arm or prosthetic hand  
     - Environmental controls (lights, wheelchair, computer commands)

5. **Feedback Loop:**  
   - Visual feedback of cursor position helps patient refine decoding; over weeks, "brain-computer" adaptation improves performance

### Hardware Components

- **Electrode Array:** 96 or 128 silicon needles (1.5–5 mm long), spaced 400 µm apart in a square grid
- **Signal Conditioning:** Low-noise amplifiers, analog-to-digital converters
- **Wireless or Percutaneous Interface:** Data streamed to external computer for real-time processing
- **Software:** Proprietary decoding software; patient interface (cursor, app, robotic arm API)

---

## Novelty & Differentiation

### vs. Standard of Care for Paralysis

- **Before:** Paralyzed patients with no voluntary motor control rely on:  
  - Eye-gaze interfaces (slow, ~5–10 words/min)  
  - Speech-synthesis software with head switches  
  - Nursing assistance for most tasks
- **After Blackrock BCI:** Potential for >20 words/min typing speed, direct prosthetic control, improved independence

### vs. Non-invasive Alternatives

- **EEG-based BCIs (non-invasive):**  
  - Pros: No surgery, no infection risk  
  - Cons: Poor spatial resolution, high noise, slow (2–5 words/min), require intensive mental training  
- **fMRI-based BCIs (research only):** Even slower, limited to laboratory settings
- **Blackrock (invasive):** Higher bandwidth (~100x better signal-to-noise), faster, more robust, but requires surgery

### vs. Other Intracortical BCI Startups

- **Blackrock vs. Paradromics:** Blackrock uses 96–128 channels (proven); Paradromics pursuing higher channel counts (1,024+) for higher bandwidth but not yet in human trials
- **Blackrock vs. Precision Neuroscience:** Precision's array is thinner/flexible but less proven; Blackrock has 20+ years of clinical data
- **Blackrock vs. Neuralink:** Neuralink's threads are thinner but still in early trials (as of 2026); Blackrock already deployed in research settings

### Distinctive Strengths

1. **Clinical Trial Data:** Longest track record of human implants; published results in high-impact journals (*Nature*, *Lancet*, etc.)
2. **Regulatory Relationships:** FDA familiar with Utah Array through multiple IDE trials
3. **Modularity:** 96-channel and 128-channel versions available; scalable
4. **Open Ecosystem:** Some systems can interface with third-party robotic arms and software

---

## Limitations: Practical

**Surgical Considerations:**  
- Requires open craniotomy; perioperative mortality risk ~0.5–1% (neurological surgery baseline)
- Infection risk (meningitis, encephalitis) ~1–2% despite prophylactic antibiotics
- Recovery period: 4–8 weeks post-implant before training begins

**Cost & Reimbursement:**  
- Device + surgery estimated at $100k–200k USD (not publicly disclosed)
- Insurance rarely covers investigational BCIs; most patients rely on research funding (NIH, NSF, VA) or out-of-pocket funding via crowdfunding
- Ongoing training and support: $5k–10k/year (technician time, software updates)

**User Burden:**  
- Requires 1–2 hours/week of active training and maintenance for first 3–6 months
- Percutaneous pedestal requires daily wound care; wireless versions reduce this but are less proven
- Patient must be cognitively intact and motivated (device not suitable for severe dementia or depression)

**Performance Variability:**  
- Some patients achieve >95% accuracy on 5-target cursor tasks; others plateau at 70–80%
- Factors: neural responsiveness, patient cognitive state, training intensity (unpredictable individual differences)

---

## Limitations: Theoretical & Readiness

**Signal Degradation Over Time:**  
- Recording quality declines 6–24 months post-implant due to glial scar formation and electrode fouling
- Long-term human data (>2 years) are sparse; animal studies show irreversible recording loss
- No proven solution yet; future arrays may use self-cleaning or regenerating electrode surfaces (research ongoing)

**Motor Remapping:**  
- Paralyzed brain undergoes plasticity; motor cortex may reorganize away from traditional hand/arm regions over months/years
- Unclear if decoder can track these changes indefinitely or if periodic re-surgery is needed

**Limited Channel Count:**  
- 96–256 channels sample <1% of motor cortex neurons
- Information bottleneck: unclear if higher channels → proportionally higher performance or asymptotic gains

**Ecosystem & Adoption Barriers:**  
- No established Clinical Procedure Terminology (CPT) codes; reimbursement pathway undefined
- Limited clinical infrastructure: only ~5–10 centers in the US can implant and support BCIs
- Regulatory uncertainty: FDA pathway for intracortical BCIs still evolving (likely De Novo or PMA, not yet formalized)

**Biocompatibility & Consent:**  
- 20-year implant durability unknown; patients must accept possibility of need for revision surgery
- Psychological impact of percutaneous implant (infection risk, appearance) not fully studied
- Consent challenges: high hopes vs. realistic limitations

---

## Regulatory Status

**FDA:**  
- **Current:** No intracortical BCI has received full FDA approval for clinical use (as of September 2026)
- **Pathways Under Exploration:** De Novo (novel device class) or PMA (Premarket Approval) for intracortical BCIs
- **IDE (Investigational Device Exemption) Trials:** Blackrock systems operating under IDE at multiple research centers (BrainGate partnership)
- **Timeline:** First De Novo approval likely 2027–2030 based on current trial progress

**Clinical Trials:**  
- **BrainGate Consortium:** Multi-site trial (Brown, Stanford, Mass General); published 4–6 year safety/efficacy data
- **Trial Identifiers:** Specific NCT numbers evolve; check ClinicalTrials.gov for active studies (search: "Utah Array," "BrainGate," "Blackrock")
- **Headline Results (published):** 1–3 bits/sec information transfer; >95% accuracy on visual feedback cursor tasks; >20 words/min typing potential with improved decoders

**International Approval:**  
- CE mark not applicable (US company, not pursuing European market currently)
- Some trial data accepted by Australian TGA for expanded access

**Key Milestones:**  
- 2004–2006: First human implants (BrainGate)
- 2015: Nature publication of 4-year safety data
- 2023–2025: Increased channel-count systems in trials
- 2027–2030 (projected): FDA De Novo approval, commercial market entry

---

## Sources

- **Blackrock Neurotech Official:** https://www.blackrockmicro.com  
- **BrainGate Consortium:** https://braingate.org (ongoing clinical trial and publications)
- **Key Publication:** Simeral, J.D., et al. (2015). "Neural control of a cursor using intracortical recordings in a human with tetraplegia." *Nature*, 533, 99–102. https://doi.org/10.1038/nature17108  
- **FDA CDRH Guidance:** https://www.fda.gov/medical-devices/ (search for neurotechnology guidance)
- **ClinicalTrials.gov:** https://clinicaltrials.gov (search: "Blackrock," "BrainGate," "intracortical")
- **Grand View Research:** BCI Market Report, 2024  
- **CDC Paralysis Statistics:** https://www.cdc.gov/ncbddd/paralysis/facts.html

---

**Profile Created:** 2026-09-13  
**Last Updated:** 2026-09-13
