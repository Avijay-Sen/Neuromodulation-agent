# Neuromodulation Startup Research Tracker

A living due-diligence research tracker built for venture capital evaluation of
biomedical **neuromodulation** startups — companies developing devices/therapies
that electrically, magnetically, ultrasonically, or otherwise modulate nervous
system activity to treat disease.

This is a research aid, **not investment advice**. All figures (funding, market
size, regulatory status) should be independently re-verified before any
investment decision — company status, trial results, and clearances change
frequently, and some figures below are estimates drawn from public secondary
sources.

## What's in here

| Path | Contents |
|---|---|
| `data/neuromodulation_startups.xlsx` | Master comparison workbook — one row per startup, one sheet per disorder category, plus a master sheet and a legend/methodology sheet. This is the primary deliverable — open it first. |
| `docs/profiles/<category>/<company-slug>.md` | Extensive long-form profile per startup: biology/epidemiology, technology, novelty, limitations, regulatory status, sources. |
| `docs/BACKLOG.md` | Candidate startups queued for future research batches, grouped by category, with a done/not-done tracker. |
| `CHANGELOG.md` | Dated log of every research batch added (which startups, which categories). |

## Categories

Startups are grouped by the primary disorder they target:

1. **Sleep Apnea** — airway/upper-airway neuromuscular control (given special
   emphasis per fund request: minimum 3 companies covered at all times).
2. **Cognitive Disorders / Neural Interface** — epilepsy, Alzheimer's/dementia,
   movement disorders affecting cognition, brain-computer interfaces.
3. **Mental Health / Psychiatric** — depression, OCD, ADHD, and other
   neuropsychiatric conditions.
4. **Neuro-Musculoskeletal / Pain / Movement** — chronic pain, autoimmune/
   inflammatory disease via bioelectronic medicine, amputation-related nerve
   pain, spinal cord injury.

## Per-startup fields

Every profile (spreadsheet row and long-form doc) covers:

- **Biological basis** — the underlying pathophysiology, prevalence of the
  condition, and estimated affected population / addressable market ("nerve
  demand"), sourced from peer-reviewed literature (Google Scholar / PubMed)
  where possible.
- **Technology** — how the device/therapy works and what is mechanistically
  novel about this company's approach versus competitors and standard of care.
- **Limitations** — split into *practical* (cost, implantation risk, patient
  burden, adherence) and *theoretical/readiness* (open scientific questions,
  unproven long-term mechanisms, whether the surrounding ecosystem — clinical
  workflows, reimbursement, societal acceptance — is mature enough for the
  technology).
- **Regulatory & clinical status** — FDA clearance/approval pathway (510(k),
  PMA, De Novo, Breakthrough Device), CE marking, and clinical trial stage
  (with NCT numbers and headline results where available).
- **Sources** — every citation used, so claims are independently checkable.

## Data sources / methodology

- **Biology & epidemiology**: peer-reviewed literature located via Google
  Scholar and PubMed.
- **Regulatory status**: FDA.gov clearance/approval databases, ClinicalTrials.gov.
- **Business/market data**: company press releases and investor pages, SEC/EU
  regulatory filings, and trade press (MedTech Dive, Fierce Biotech, MassDevice,
  STAT News).

Where a figure could not be verified from a credible public source, the
profile says so explicitly ("not publicly disclosed" / "unable to verify")
rather than estimating silently.

## Update cadence

This tracker started with an initial batch of ~15 startups across the four
categories above (see `CHANGELOG.md` for the exact date). After that, it is
updated automatically in batches of **~5 new startups per day**, pulled from
`docs/BACKLOG.md`, each added with the same full research treatment and
appended to both the spreadsheet and the long-form profiles. Every batch is
committed to this branch with a changelog entry.

A Google Sheet snapshot of the master workbook was also generated for quick
sharing/viewing; this GitHub repository (and `data/neuromodulation_startups.xlsx`
in particular) is the version-controlled source of truth, since the sheet
cannot be edited in place by the automation.
