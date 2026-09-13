# Changelog

All research batches are logged here, newest first.

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
