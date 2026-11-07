#!/usr/bin/env python3
"""Merge source/answers/*.md into the question bank embedded in index.html.

Answer files hold sections keyed by question id:

    ## 604
    **Answer**

    ...markdown...

    ## 605
    ...

For every id found, the matching question's "a" field is set and its
"pend" flag removed. Ids that match no question, and duplicate ids across
files, are reported as errors and nothing is written.

Usage:
    python3 tools/merge_answers.py            # merge and report
    python3 tools/merge_answers.py --check    # report only, write nothing
"""

import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "index.html")
ANSWERS = os.path.join(ROOT, "source", "answers", "*.md")
OPEN_TAG = '<script type="application/json" id="data">'
CLOSE_TAG = "</script>"


def load_answers():
    """Return {id: answer_text}, plus a list of duplicate-id errors."""
    answers, seen_in, errors = {}, {}, []
    for path in sorted(glob.glob(ANSWERS)):
        name = os.path.basename(path)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        # split on headings of the form "## <digits>" at line start
        parts = re.split(r"^## (\d+)\s*$", text, flags=re.M)
        # parts[0] is any preamble; then (id, body) pairs
        for qid, body in zip(parts[1::2], parts[2::2]):
            body = body.strip()
            if not body:
                errors.append(f"{name}: question {qid} has an empty answer")
                continue
            if qid in answers:
                errors.append(
                    f"duplicate id {qid} in {name} (already in {seen_in[qid]})"
                )
                continue
            answers[qid] = body
            seen_in[qid] = name
    return answers, errors


def read_index():
    with open(INDEX, encoding="utf-8") as fh:
        html = fh.read()
    start = html.index(OPEN_TAG) + len(OPEN_TAG)
    end = html.index(CLOSE_TAG, start)
    return html, start, end, json.loads(html[start:end])


def main():
    check_only = "--check" in sys.argv

    answers, errors = load_answers()
    if not answers:
        sys.exit("no answers found under source/answers/*.md")

    html, start, end, data = read_index()

    # index every question by id
    questions = {}
    for part in data["parts"]:
        for topic in part["topics"]:
            for q in topic["qs"]:
                questions[q["id"]] = q

    unknown = sorted(set(answers) - set(questions), key=int)
    if unknown:
        errors.append("ids with no matching question: " + ", ".join(unknown))

    if errors:
        for e in errors:
            print("ERROR:", e, file=sys.stderr)
        sys.exit(1)

    merged = overwritten = 0
    for qid, body in answers.items():
        q = questions[qid]
        if q.get("a"):
            overwritten += 1
        q["a"] = body
        q.pop("pend", None)
        merged += 1

    still_pending = sorted(
        (qid for qid, q in questions.items() if q.get("pend")), key=int
    )

    print(f"answers found:      {len(answers)}")
    print(f"merged:             {merged} (overwrote {overwritten} existing)")
    print(f"questions in bank:  {len(questions)}")
    print(f"still pending:      {len(still_pending)}")
    if still_pending:
        preview = ", ".join(still_pending[:20])
        more = " ..." if len(still_pending) > 20 else ""
        print(f"  {preview}{more}")

    if check_only:
        print("\n--check: nothing written")
        return

    blob = json.dumps(data, ensure_ascii=False)
    if CLOSE_TAG in blob or "</" in blob:
        sys.exit("refusing to write: data contains '</', which would end the tag")

    with open(INDEX, "w", encoding="utf-8") as fh:
        fh.write(html[:start] + blob + html[end:])
    print(f"\nwrote {INDEX}")


if __name__ == "__main__":
    main()
