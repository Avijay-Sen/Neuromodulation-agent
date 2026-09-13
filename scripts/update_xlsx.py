#!/usr/bin/env python3
"""
Canonical helper for adding/fixing startup rows in data/neuromodulation_startups.xlsx.

Why this exists: an earlier automated run appended new rows using default
openpyxl styling (Calibri 11, no fill, no wrap, no border, no row height)
instead of matching the workbook's established per-category style. This
script is the single place that knows the correct style, so every future
row — added by hand or by the daily research automation — looks the same
as the original rows.

Usage:
    # Fix any already-added rows that don't match their sheet's established style
    python3 scripts/update_xlsx.py --fix-formatting

    # Append a new startup row (Master + the matching category sheet), correctly styled
    python3 scripts/update_xlsx.py --add-row startup.json

Where startup.json looks like:
    {
      "category": "Neuro-Musculoskeletal / Pain / Movement",
      "sheet": "Neuro-Musculoskeletal",
      "values": {
        "Company": "...", "Category": "...", "HQ": "...", "Founded": "...",
        "Funding / Company Status": "...", "Target Nerve / Mechanism": "...",
        "Biological Basis (Nerve Demand)": "...",
        "Market Size / Affected Population": "...", "Technology": "...",
        "Novelty / Differentiation": "...", "Limitations - Practical": "...",
        "Limitations - Theoretical / Readiness": "...",
        "Regulatory & Clinical Status": "...",
        "Full Profile (docs/profiles/...)": "..."
      }
    }
"""

import argparse
import copy
import json
import sys
from pathlib import Path

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

XLSX_PATH = Path(__file__).resolve().parent.parent / "data" / "neuromodulation_startups.xlsx"

# The one true style for a data row, matching the original 15-startup seed.
ROW_FONT = Font(name="Arial", size=10)
ROW_ALIGNMENT = Alignment(wrap_text=True, vertical="top")
ROW_BORDER = Border(
    left=Side(style="thin"), right=Side(style="thin"),
    top=Side(style="thin"), bottom=Side(style="thin"),
)
ROW_HEIGHT = 130.0

# Category -> fill color, taken directly from the existing Master sheet rows.
CATEGORY_FILL = {
    "Sleep Apnea": "D9E1F2",
    "Cognitive Disorders / Neural Interface": "E2EFDA",
    "Mental Health / Psychiatric": "FCE4D6",
    "Neuro-Musculoskeletal / Pain / Movement": "FFF2CC",
}

CATEGORY_TO_SHEET = {
    "Sleep Apnea": "Sleep Apnea",
    "Cognitive Disorders / Neural Interface": "Cognitive - Neural Interface",
    "Mental Health / Psychiatric": "Mental Health - Psychiatric",
    "Neuro-Musculoskeletal / Pain / Movement": "Neuro-Musculoskeletal",
}


def style_row(ws, row_num, category):
    """Apply the canonical data-row style to every populated column in row_num."""
    fill_color = CATEGORY_FILL[category]
    fill = PatternFill(start_color=fill_color, end_color=fill_color, fill_type="solid")
    for col in range(1, ws.max_column + 1):
        cell = ws.cell(row=row_num, column=col)
        cell.font = copy.copy(ROW_FONT)
        cell.fill = fill
        cell.alignment = copy.copy(ROW_ALIGNMENT)
        cell.border = copy.copy(ROW_BORDER)
    ws.row_dimensions[row_num].height = ROW_HEIGHT


def is_correctly_styled(ws, row_num):
    """Heuristic: a correctly-styled data row is Arial (not the openpyxl default Calibri)."""
    cell = ws.cell(row=row_num, column=1)
    return cell.font.name == "Arial"


def fix_formatting(wb):
    """Find any trailing rows that don't match their sheet's established style and fix them."""
    fixed = []

    ws = wb["Master"]
    for row_num in range(2, ws.max_row + 1):
        if is_correctly_styled(ws, row_num):
            continue
        category = ws.cell(row=row_num, column=2).value
        if category not in CATEGORY_FILL:
            print(f"WARNING: Master row {row_num} has unrecognized category {category!r}, skipping", file=sys.stderr)
            continue
        style_row(ws, row_num, category)
        fixed.append(("Master", row_num, ws.cell(row=row_num, column=1).value))

    for category, sheet_name in CATEGORY_TO_SHEET.items():
        if sheet_name not in wb.sheetnames:
            continue
        ws = wb[sheet_name]
        for row_num in range(2, ws.max_row + 1):
            if is_correctly_styled(ws, row_num):
                continue
            style_row(ws, row_num, category)
            fixed.append((sheet_name, row_num, ws.cell(row=row_num, column=1).value))

    return fixed


def add_row(wb, category, sheet_name, values):
    """Append one new startup row to Master and its category sheet, correctly styled."""
    for target_sheet in ("Master", sheet_name):
        ws = wb[target_sheet]
        header = [c.value for c in ws[1]]
        row_num = ws.max_row + 1
        for col_idx, col_name in enumerate(header, start=1):
            ws.cell(row=row_num, column=col_idx).value = values.get(col_name, "")
        style_row(ws, row_num, category)
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fix-formatting", action="store_true",
                         help="Fix any rows whose style doesn't match the sheet's established look")
    parser.add_argument("--add-row", metavar="JSON_FILE",
                         help="Append one new, correctly-styled startup row from a JSON file")
    parser.add_argument("--path", default=str(XLSX_PATH), help="Path to the workbook (default: data/neuromodulation_startups.xlsx)")
    args = parser.parse_args()

    if not args.fix_formatting and not args.add_row:
        parser.error("Specify --fix-formatting and/or --add-row JSON_FILE")

    wb = openpyxl.load_workbook(args.path)

    if args.fix_formatting:
        fixed = fix_formatting(wb)
        if fixed:
            print(f"Fixed formatting on {len(fixed)} row(s):")
            for sheet, row_num, name in fixed:
                print(f"  {sheet} row {row_num}: {name}")
        else:
            print("No misformatted rows found.")

    if args.add_row:
        with open(args.add_row) as f:
            spec = json.load(f)
        add_row(wb, spec["category"], spec["sheet"], spec["values"])
        print(f"Added row for {spec['values'].get('Company')!r} to Master + {spec['sheet']!r}")

    wb.save(args.path)
    print(f"Saved {args.path}")


if __name__ == "__main__":
    main()
