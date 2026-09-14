# Changelog

All research batches are logged here, newest first.

## 2026-09-14 — Third batch (10 startups)

Researched 10 startups across all four categories, clearing the entire prior
backlog queue (11 entries, consolidated into 10 profiles — see note below):

- **Sleep Apnea (1):** LivaNova (aura6000 System, originally developed by
  ImThera Medical) — proximal hypoglossal nerve stimulation; FDA PMA approved
  March 19, 2026. **Note:** this profile consolidates two separate backlog
  entries ("ImThera Medical" and "LivaNova plc — aura6000 program") into one,
  since ImThera no longer operates independently — LivaNova acquired it
  outright in 2018 and owns the aura6000 program directly.
- **Cognitive Disorders / Neural Interface (3):** Precision Neuroscience
  (Layer 7 subdural cortical interface, FDA 510(k) cleared Apr 2025),
  Motif Neurotech (DOT epidural cortical microstimulator for
  treatment-resistant depression), Rune Labs (StrivePD — Apple Watch-based
  Parkinson's symptom monitoring + Medtronic DBS data integration; included
  as a non-stimulation software/data platform, flagged as an atypical fit
  for this tracker's mechanism-based taxonomy)
- **Mental Health / Psychiatric (3):** Sooma (at-home/clinic tDCS for
  depression, EU MDR certified, FDA IDE pivotal trial ongoing), Nexstim
  (navigated TMS — NBT System, FDA cleared for MDD since 2018), Neurolief
  (Relivion for migraine + Proliv Rx for MDD, FDA PMA approved Jan 2026;
  financially tied to BrainsWay via convertible loans + acquisition call
  option)
- **Neuro-Musculoskeletal / Pain / Movement (3):** Nalu Medical (micro-IPG
  PNS/SCS platform — acquired by Boston Scientific for ~$533M, closed Jan
  2026), SPR Therapeutics (SPRINT — percutaneous, temporary PNS for chronic
  and acute pain), Presidio Medical (ULF spinal cord stimulation — novel
  reversible conduction-block mechanism via sodium channel inactivation,
  FDA IDE pivotal trial underway)

**Tech-tree updates:** Added three new L3 branches under Electrical
Neurostimulation — "Percutaneous / Temporary Peripheral Nerve Stimulation"
(SPR Therapeutics) and "Surface / Epicortical Interface (ECoG, Non-Penetrating)"
(Precision Neuroscience, Motif Neurotech); added a new L3 "Navigated TMS
(nTMS)" branch under Magnetic Stimulation (Nexstim); added a new L2 branch
"Digital Health / Neurostimulation Data Platforms" → L3 "Wearable-based
Symptom Monitoring" for Rune Labs (non-stimulation). Added LivaNova and Nalu
Medical to the existing "Implanted Peripheral / Cranial Nerve" L3; Neurolief
to "Non-invasive / Transcutaneous Peripheral"; Presidio Medical to "Implanted
Spinal Cord"; Sooma to "Direct Current (tDCS)". Also corrected a factual
error carried over from the prior batch: the tech tree listed Paradromics as
"10,000+ channel" when its verified profile figure is 421 electrodes — fixed
to match.

**Comparison.html:** Appended 10 new entries to the embedded `companies`
array (verified valid JSON after edit — 30 total companies), each using the
full GitHub blob URL format for the `profile` field per established
convention.

**Backlog replenishment:** The prior backlog had only 11 unresearched entries
before this batch (below the ~15 threshold), so 14 new credible candidates
were sourced via live web search and appended across all four categories
(3 Sleep Apnea, 4 Cognitive, 3 Mental Health, 4 Neuro-Musculoskeletal) —
each verified as a real, currently-operating company via at least one
independent source before being added. Notably, SonoMind (focused ultrasound
for depression) would populate the tech tree's long-standing placeholder for
a "Low-Intensity Focused Ultrasound Neuromodulation" branch once researched.

**Citation discipline:** Every funding figure, regulatory date, and
mechanism claim in this batch's profiles is either linked to a live-verified
primary/credible-secondary source or explicitly marked `[unverified]` —
several founding years (ImThera, Motif Neurotech, Neurolief) and some
funding totals could not be pinned to a primary source in this pass and are
flagged accordingly rather than stated as fact.

## 2026-09-13 — Second batch (5 startups)

Researched 5 startups across three categories:

- **Cognitive Disorders / Neural Interface (2):** Blackrock Neurotech (U Utah Array, intracortical BCI), Paradromics (ultra-high-channel intracortical BCI with bidirectional feedback)
- **Mental Health / Psychiatric (1):** Soterix Medical (tDCS for depression, clinical-grade)
- **Neuro-Musculoskeletal / Pain / Movement (2):** Cala Health (wearable transcutaneous PNS for essential tremor), Saluda Medical (closed-loop spinal cord stimulation via ECAP feedback)

**Tech-tree updates:** Added new L3 branch "Intracortical BCI (Penetrating)" under Electrical Neurostimulation; populated with Blackrock and Paradromics. Added entries to existing Implanted Spinal Cord (Saluda), Non-invasive Transcutaneous Peripheral (Cala), and Direct Current tDCS (Soterix) branches. Removed placeholder for Intracortical BCI from "Notes for future branches."

**Spreadsheet update status:** Done (backfilled) — added Master sheet rows + rows
on the three relevant category sheets (`Cognitive - Neural Interface`,
`Mental Health - Psychiatric`, `Neuro-Musculoskeletal`) for all 5 companies in
this batch.

**Artifact refresh status:** Pending (diagram artifact refresh not available in
this session; tree source (`docs/technology-tree.md`) is up to date).

**Post-batch fix (2026-09-13, later same day):** The backfill above wrote its
5 rows with raw openpyxl, which used default styling (Calibri, no fill, no
wrap, no border, no row height) instead of matching the workbook's established
per-category look (Arial 10pt, category color fill, wrapped/top-aligned text,
thin borders, 130pt rows). Fixed by re-styling all 10 affected rows (5 in
Master + 5 across the category sheets). Added `scripts/update_xlsx.py` as the
one canonical way to add/fix spreadsheet rows going forward — the daily
automation is now required to use it instead of ad-hoc openpyxl code, so this
can't recur. Also removed stray `.DS_Store`/`.patch` files that a local
auto-push watcher had swept into a commit, and added `.gitignore`.

## 2026-09-07 — Initial batch (15 startups)

Seeded the tracker with 15 startups across four categories:

- **Sleep Apnea (3):** Inspire Medical Systems, Nyxoah, Signifier Medical Technologies (eXciteOSA)
- **Cognitive Disorders / Neural Interface (4):** NeuroPace, Cognito Therapeutics, Insightec, Synchron
- **Mental Health / Psychiatric (4):** Neuronetics, BrainsWay, Flow Neuroscience, NeuroSigma
- **Neuro-Musculoskeletal / Pain / Movement (4):** Nevro, SetPoint Medical, Neuros Medical, Onward Medical

Added: `data/neuromodulation_startups.xlsx`, `docs/profiles/**`, `docs/BACKLOG.md`.
