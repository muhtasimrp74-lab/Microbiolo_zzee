# Import notes — Matrix 3rd Prof, 18th ed. (July 2026)

Source: `Matrix_3rd_Prof___18th_Ed__July_2026.pdf`, 62 scanned pages (book pp. 73–148). No text layer, so every page was OCR'd and checked against the page images.

## What was imported

**Written DU questions (book pp. 73–112).** 765 numbered items, 1,027 wordings, across Parasitology, General Bacteriology, Systemic Bacteriology, Clinical Microbiology, Virology, Immunology and Mycology. The full transcription is in `matrix_written_questions.md`.

- **Stars** (the book's ★/★★/★★★) were checked item by item against crops of the left margin of every page. They are stored as `mx` and shown as the gold star badge.
- **Sitting codes** were parsed and normalised (N → Nov; `08/07Ju` → 08Ju, 07Ju; `22N/M` → 22Nov, 22M; `20N/Ju` → 20Nov/July). Codes the book prints oddly (e.g. `25k`) are kept as printed. Existing site tags were normalised the same way (DU-22N → DU-22Nov).
- **Pages typed from the image:** pp. 105, 109, 110, 111 (PDF 33, 37, 38, 39), where OCR was unusable.
- **Book quirks kept and flagged in the text:** Immunology › Hypersensitivity item 1 is printed as "Define (DU-10/09Ja,08Ju)" with the term missing ("allergy" assumed); Antibody item 7 is printed "secretory IgG" (shown as IgA, noted).
- About 15 case questions are printed with no DU code; they are imported with no sitting.

**Merging with the existing bank (second-term parts).** Each of the 470 second-term wordings was matched against the existing 383 answered questions and reviewed by hand (`source/` keeps the outcome, not the tooling):

- 135 wordings were already present with all their sittings (no change).
- 129 existing questions gained 331 older sittings (DU 2003–2017 and a few missed recent ones). Their answers are unchanged.
- 82 genuinely new second-term questions were added to the matching topics.
- Existing question IDs are unchanged, so saved progress, notes and handwriting stay attached. Display numbers (Q1…Q860) are renumbered in book order.

**First-term parts (new).** Part V General Bacteriology (134), Part VI Systemic Bacteriology (160), Part VII Immunology (101). Each book item is one entry; extra wordings under the same book number appear as *Also asked*.

**MCQs (book pp. 127–148).** 260 items, 13 papers × 20: May 2026, Nov 2025, May 2025, Nov 2024, then DU-24M, 23Nov, 23M, 22Nov, 22M, 21M, 20Nov/M, 19Nov, 19M. 235 True/False, 20 SBA (May 2026 and Nov 2025 papers have SBA sections). Full text in `matrix_mcq.md`.

- Every key was re-read at higher resolution and compared; the two reads never disagreed on a T/F letter.
- Four questions had lost their own key to the next question in a first pass (a missed question number); all four were traced and fixed (DU-24M Q14 and Q20, DU-23M Q7, DU-20Nov/M Q19).
- Five questions swallowed by page headers were restored (May 2026 Q1, DU-24M Q15, DU-23Nov Q1, DU-23M Q8, DU-20Nov/M Q20).
- The book misnumbers DU-24M Q16–19 as 6–9; renumbered.

## Book keys corrected (shown as "Key corrected" on the site)

Where the printed key contradicts standard textbooks, the site shows the corrected key and the note under the option says what the book printed. 25 MCQs, 30 options:

- May 2025 Q4 — Regarding Neisseria gonorrhoeae: d) Blood agar is used to culture the bacteria → **F**
- May 2025 Q14 — Vector borne parasites are: c) Entamoeba histolytica → **F**
- May 2025 Q16 — Regarding hookworm: e) Ova contain four blastomeres → **T**
- November 2024 Q14 — Malaria can be transmitted by: c) placental defect to fetus → **T**
- November 2024 Q16 — Helminthes infections caused by ingestion of ova are: e) Necator americanus → **F**
- November 2024 Q18 — Vibrio cholerae: a) possesses peritrichous flagella → **F**
- November 2023 Q6 — False positive tuberculin test is seen in-: c) BCG vaccination → **T**
- May 2023 Q2 — High-level disinfectants are: a) alcohol → **F**; b) glutaraldehyde → **T**
- May 2023 Q3 — Helicobacter pylori: c) is a facultative anaerobe → **F**
- May 2023 Q4 — Botulinum toxin: b) is relatively heat stable → **F**
- May 2023 Q12 — Acquired immunity: d) exhibits similar pattern of primary and secondary immune response → **F**
- May 2022 Q2 — Pseudomonas aeruginosa: d) infection is treated by Ceftriaxone. → **F**
- May 2021 Q6 — Macrophage: b) express both MHC class | and II molecule → **T**
- May 2021 Q11 — Regarding malarial parasites: b) Plasmodium malariae causes benign tertian malaria → **F**
- 2020 Q11 — Human immunodeficiency virus: e) can be confirmed by ELISA test → **F**
- November 2019 Q5 — Hepatitis A virus: d) can be treated by antiviral drug → **F**
- November 2019 Q11 — Mycobacterium leprae: e) causes multibacillary leprosy in patients having intact CMI. i ra → **F**
- November 2019 Q17 — Intestinal trematodes are: e) Strongyloides stercoralis → **F**
- May 2019 Q1 — Anaerobic bacteria: b) possess superoxide dismutase → **F**; d) are resistant to metronidazole → **F**
- May 2019 Q3 — Sporicidal chemical agents are: b) Formaldehyde gas → **T**
- May 2019 Q4 — Enveloped viruses are: b) Hepatitis C Virus → **T**
- May 2019 Q5 — Reverse transcriptase enzymes are possessed by: a) Hepatitis B Virus → **T**
- May 2019 Q9 — Anaerobic cocci are: e) Peptococcus → **T**
- May 2019 Q10 — Protein synthesis inhibiting exotoxins are: b) Verotoxin → **T**; e) Tetanus toxin → **F**
- May 2019 Q13 — Bacterial causes of meningitis in neonates include: a) Streptococcus pneumoniae → **F**; b) Haemophilus influenzae → **F**; d) Streptococcus agalactiae → **T**

Left as printed (debatable, not clearly wrong): "C3 deficiency is associated with SLE" (DU-22M Q13), dengue vaccine availability (DU-22M Q19, reflects the time of the exam), S. pyogenes "ferments mannitol" (DU-25M).

## Model answers — progress

| Part | Questions | Answer pending |
|---|---:|---:|
| Part I — Virology | 138 | 28 |
| Part II — Mycology | 74 | 5 |
| Part III — Parasitology | 190 | 34 |
| Part IV — Clinical Microbiology | 63 | 15 |
| Part V — General Bacteriology | 134 | 134 |
| Part VI — Systemic Bacteriology | 160 | 160 |
| Part VII — Immunology | 101 | 101 |

Pending questions show an **Answer pending** badge; **Ask AI** gives an answer meanwhile. Next batches: write answers part by part, ★★★ items first, removing `pend` as each answer is added.
