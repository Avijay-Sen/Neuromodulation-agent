# Neuromodulation Technology Tree

The master taxonomy of neuromodulation technologies, built from every startup this
tracker has researched (see `docs/profiles/` and `CHANGELOG.md`). Organized by
**mechanism**, not by disease — the same taxonomy the visual diagram renders from.

**How to add to this tree** (works for you, for me, and for the daily research
automation — see `docs/BACKLOG.md` / the daily trigger):

1. Find the right **Level 2** (energy modality) the new technology belongs to. If
   none fits, add a new `## L2:` section.
2. Find or add the right **Level 3** (delivery approach/target) under it.
3. Add one bullet under Level 4 in this exact format so it's easy to parse:
   `- **Company Name** (product name if any) — one-line technique note — indication — added YYYY-MM-DD`
4. Tell me (or let the daily job note it in `CHANGELOG.md`) so the visual diagram
   artifact gets republished — the artifact is a rendering of this file, not a
   live database, so it only updates when someone (me, on request or via the
   daily job) regenerates it from this source.

Last synced to diagram: 2026-09-14

---

## L1: Neuromodulation

---

## L2: Electrical Neurostimulation
*Direct electrical current/pulses delivered to neural tissue — central, spinal, peripheral, cranial, or via an endovascular interface.*

### L3: Implanted Central (Brain)
- **NeuroPace** (RNS System) — closed-loop responsive stimulation at the seizure focus, continuous iEEG monitoring — Drug-resistant epilepsy — added 2026-09-07

### L3: Implanted Spinal Cord
- **Nevro** (Senza / HFX, 10kHz) — paresthesia-free high-frequency dorsal column stimulation — Chronic back/leg pain, painful diabetic neuropathy — added 2026-09-07
- **Onward Medical** (ARC-IM, investigational) — implantable epidural stimulation, spatiotemporally patterned to intended movement — Spinal cord injury (restorative) — added 2026-09-07
- **Saluda Medical** (Evoke) — closed-loop spinal cord stimulation with ECAP-based feedback, automatic adjustment to maintain pain relief — Chronic back/leg pain, failed back surgery syndrome — added 2026-09-13
- **Presidio Medical** (ULF Neuromodulation) — ultra-low frequency epidural stimulation, reversible conduction block via sodium channel inactivation (mechanistically distinct from paresthesia-masking/closed-loop SCS) — Chronic nociceptive low back pain — added 2026-09-14

### L3: Intracortical BCI (Penetrating)
- **Blackrock Neurotech** (Utah Array) — 96–128 channel intracortical microelectrode arrays, single-unit recording for motor intent decoding — Paralysis/SCI communication & prosthetic control — added 2026-09-13
- **Paradromics** (Connexus) — 421-electrode cortical array + wireless chest transceiver, motor/speech decoding — Paralysis/SCI communication, sensorimotor prosthetic control — added 2026-09-13 (channel count corrected 2026-09-14; see profile)

### L3: Implanted Peripheral / Cranial Nerve
- **Inspire Medical Systems** — unilateral hypoglossal nerve stimulation, breath-synchronized closed loop — Obstructive sleep apnea — added 2026-09-07
- **Nyxoah** (Genio) — bilateral hypoglossal nerve stimulation, leadless/battery-free implant — Obstructive sleep apnea — added 2026-09-07
- **SetPoint Medical** — cervical vagus nerve stimulation, cholinergic anti-inflammatory pathway — Rheumatoid arthritis (bioelectronic/neuroimmune) — added 2026-09-07
- **Neuros Medical** (Altius) — peripheral nerve cuff, on-demand high-frequency conduction block — Post-amputation phantom/residual limb pain — added 2026-09-07
- **LivaNova** (aura6000, originally ImThera Medical) — proximal hypoglossal nerve stimulation (multi-branch trunk cuff) — Obstructive sleep apnea — added 2026-09-14
- **Nalu Medical** (micro-IPG, acquired by Boston Scientific Jan 2026) — battery-free wirelessly-powered implantable pulse generator, PNS + SCS indications — Chronic peripheral-nerve-origin pain — added 2026-09-14

### L3: Percutaneous / Temporary Peripheral Nerve Stimulation
*Distinct from permanently implanted PNS above — a thin lead placed near a target nerve for a defined period (typically up to 60 days), then removed.*
- **SPR Therapeutics** (SPRINT PNS, endura/extensa) — percutaneous lead + external wearable pulse generator, up to 60-day use — Chronic and acute pain of the back/extremities/head/neck/torso — added 2026-09-14

### L3: Endovascular Neural Interface (BCI)
- **Synchron** (Stentrode) — 16-channel stent-electrode array delivered via jugular vein into the superior sagittal sinus, no craniotomy — Paralysis/ALS communication & device control — added 2026-09-07

### L3: Surface / Epicortical Interface (ECoG, Non-Penetrating)
*Electrode arrays placed on or just above the cortical surface (subdural or epidural) — distinct from both penetrating intracortical arrays and endovascular interfaces.*
- **Precision Neuroscience** (Layer 7) — 1,024-electrode subdural surface array, thinner-than-hair, records + stimulates — BCI communication/motor restoration, neurosurgical mapping — added 2026-09-14
- **Motif Neurotech** (DOT microstimulator) — millimeter-scale epidural cortical stimulator, wireless magnetoelectric power transfer — Treatment-resistant depression — added 2026-09-14

### L3: Non-invasive / Transcutaneous Peripheral
- **NeuroSigma** (Monarch eTNS) — external trigeminal nerve stimulation, nightly during sleep — Pediatric ADHD — added 2026-09-07
- **Signifier Medical Technologies** (eXciteOSA) — transcutaneous neuromuscular stimulation (NMES) of the tongue, daytime use — Mild OSA / primary snoring — added 2026-09-07
- **Onward Medical** (ARC-EX) — transcutaneous spinal cord stimulation during rehab — Spinal cord injury (hand/arm function) — added 2026-09-07
- **Cala Health** (Cala Trio) — wearable transcutaneous peripheral nerve stimulation (radial/ulnar nerves), on-demand use — Essential tremor, Parkinson's tremor — added 2026-09-13
- **Neurolief** (Relivion / Proliv Rx) — multi-channel headset, 6 branches of occipital + trigeminal nerves — Acute migraine; major depressive disorder — added 2026-09-14

---

## L2: Magnetic Stimulation (TMS)
*Pulsed magnetic fields induce focal electric currents in cortical tissue — no implant, in-office use.*

### L3: Standard-coil rTMS
- **Neuronetics** (NeuroStar) — figure-8 coil over left DLPFC, 10Hz repetitive TMS — MDD, anxious depression, adjunct OCD, adolescent MDD — added 2026-09-07

### L3: Deep TMS (H-coil)
- **BrainsWay** — patented H-coil (H1/H7 variants), broader/deeper cortical field — MDD, OCD, smoking cessation — added 2026-09-07

### L3: Navigated TMS (nTMS)
- **Nexstim** (NBT System / SmartFocus) — real-time 3D MRI-based navigation of induced cortical electric field, individualized coil targeting — MDD; CE-marked also for stroke rehab & chronic neuropathic pain — added 2026-09-14

---

## L2: Transcranial Electrical Stimulation (tES)
*Weak constant or alternating current applied via scalp electrodes — lower cost, potentially non-clinical/home use.*

### L3: Direct Current (tDCS)
- **Flow Neuroscience** (FL-100) — at-home 2-electrode tDCS, anode over left DLPFC — MDD (non-treatment-refractory) — added 2026-09-07
- **Soterix Medical** — clinical-grade tDCS (conventional and HD variants), research & clinical devices — MDD, treatment-resistant depression, stroke rehabilitation — added 2026-09-13
- **Sooma** — at-home/clinic tDCS cap, bilateral DLPFC electrodes — MDD; also chronic pain (EU) — added 2026-09-14

---

## L2: Focused Ultrasound
*Acoustic energy focused non-invasively through the skull under real-time MRI guidance — thermal ablation or reversible bio-effects.*

### L3: Thermal Ablation (HIFU / MRgFUS)
- **Insightec** (Exablate Neuro) — incisionless thalamotomy/pallidotomy, >1,000-element phased transducer helmet — Essential tremor, Parkinson's tremor — added 2026-09-07

### L3: Blood-Brain-Barrier Opening (investigational)
- **Insightec** (Exablate Neuro, investigational arm) — low-intensity pulsed ultrasound + microbubbles, transient reversible BBB opening — Alzheimer's (antibody drug-delivery enhancement) — added 2026-09-07

---

## L2: Sensory / Multisensory Entrainment
*Non-electrical, non-magnetic sensory input (light, sound) timed to entrain neural oscillations.*

### L3: Gamma-frequency Light + Sound
- **Cognito Therapeutics** (Spectris) — synchronized 40Hz visual + auditory stimulation, EEG-calibrated — Alzheimer's disease — added 2026-09-07

---

## L2: Digital Health / Neurostimulation Data Platforms
*Not a stimulation modality — software/data platforms that monitor symptoms and/or interoperate with implanted neurostimulation devices. Included because they are integral to the neuromodulation ecosystem, tracked separately since they don't deliver energy to neural tissue.*

### L3: Wearable-based Symptom Monitoring
- **Rune Labs** (StrivePD) — Apple Watch accelerometer/gyroscope-based tremor & dyskinesia tracking, interoperates with Medtronic Percept PC DBS telemetry — Parkinson's disease symptom monitoring & DBS programming support — added 2026-09-14

---

## Notes for future branches (not yet populated)

Candidates already in `docs/BACKLOG.md` will likely need these new L2/L3 branches
once researched — added here as placeholders so the daily job/automation knows
where to file them rather than guessing:

- **L2: Electrical Neurostimulation → L3: Implanted DBS (Deep Brain Stimulation)** — none yet (Medtronic/Boston Scientific/Abbott are incumbents, not startups tracked here; watch for a DBS-focused startup)
- **L2: Ultrasound → L3: Low-Intensity Focused Ultrasound Neuromodulation (non-ablative, reversible)** — distinct from Insightec's thermal ablation; watch for a non-thermal neuromodulatory ultrasound startup
