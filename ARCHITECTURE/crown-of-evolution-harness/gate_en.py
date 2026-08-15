# -*- coding: utf-8 -*-
"""Standalone structural gate for the English manuscript.

Run:  python -B gate_en.py          checks
      python -B gate_en.py --teeth  mutation battery
"""

import io
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
DOC = os.environ.get(
    "CROWN_MANUSCRIPT",
    os.path.join(HERE, os.pardir, "CROWN-OF-EVOLUTION-EN.md"),
)

REQUIRED_DECLARATIONS = [
    "K_\\ell", "\\operatorname{Cand}", "\\operatorname{IdPres}", "C_X",
    "\\operatorname{Adm}_R", "\\operatorname{car}_R", "z_R", "d_R", "G_R",
    "c_{\\mathrm{sys}}", "\\operatorname{InitHist}", "\\operatorname{ProcDef}",
    "U_{12}", "\\operatorname{rep}_\\ell^{[R]}", "\\oplus_q",
]
CONTRACT_ANCHOR = "is obliged to declare the level"
GUILL_OPEN, GUILL_CLOSE = chr(171), chr(187)
CURLY_OPEN, CURLY_CLOSE = chr(8220), chr(8221)
SINGLE_OPEN, SINGLE_CLOSE = chr(8216), chr(8217)
DQUOTE = chr(34)
BSLASH = chr(92)
FENCE = chr(96) * 3
LEGACY_INLINE_DELIMITERS = (BSLASH + "(", BSLASH + ")")
LEGACY_DISPLAY_DELIMITERS = (BSLASH + "[", BSLASH + "]")
QUOTE_CHARS = (DQUOTE + CURLY_OPEN + CURLY_CLOSE + GUILL_OPEN + GUILL_CLOSE
               + SINGLE_OPEN + SINGLE_CLOSE)


def read_lines(path):
    with io.open(path, encoding="utf-8", newline="") as fh:
        return fh.read().split("\n")


def check(name, ok, detail=""):
    return (name, bool(ok), detail)


def strip_frontmatter(text):
    lines = text.split("\n")
    if lines and lines[0].strip() == "---":
        for j in range(1, len(lines)):
            if lines[j].strip() == "---":
                return "\n".join(lines[j + 1:])
    return text


def prose_lines(text):
    out, code = [], False
    for line in strip_frontmatter(text).split("\n"):
        if line.lstrip().startswith(FENCE):
            code = not code
            continue
        if not code:
            out.append(line)
    return out


def is_cyrillic_body(text):
    cyr = sum(1 for c in text if chr(1024) <= c <= chr(1279))
    return cyr > len(text) * 0.02 if text else False


def c_escape_artefact(text, lines):
    folded = text.replace("\r\n", "\n")
    ctrl = sorted({"U+%04X" % ord(c) for c in folded
                   if ord(c) < 32 and c != "\n"})
    backslash_quote = re.compile(re.escape(BSLASH) + "[" + re.escape(QUOTE_CHARS) + "]")
    inline_code = re.compile(chr(96) + "+[^" + chr(96) + "]*" + chr(96) + "+")
    hits = [line.strip()[:40] for line in lines
            if backslash_quote.search(inline_code.sub("", line))]
    return check("ESCAPE_ARTEFACT", not ctrl and not hits,
                 "control chars: %s; backslash-quote lines: %d %s" %
                 (", ".join(ctrl) or "none", len(hits), hits[:2] or ""))


def c_brace_balance(text, lines):
    hits, i = [], 0
    while True:
        i = text.find(BSLASH + "{", i)
        if i < 0:
            break
        j = text.find("}", i + 2)
        if j > 0 and text[j - 1] != BSLASH and "{" not in text[i + 2:j]:
            hits.append(text[i:j + 1][:40])
        i += 2
    return check("BRACE_BALANCE", not hits,
                 "escaped-open closed by bare brace: %d %s" %
                 (len(hits), hits[:3] or ""))


def c_quote_convention(text, lines):
    body = "\n".join(lines)
    if is_cyrillic_body(body):
        return check("QUOTE_CONVENTION", True, "Cyrillic body")
    used = {}
    for name, mark in (("guillemet", GUILL_OPEN), ("curly", CURLY_OPEN),
                       ("single", SINGLE_OPEN)):
        n = body.count(mark)
        if n:
            used[name] = n
    straight = body.count(DQUOTE) // 2
    if straight:
        used["straight"] = straight
    loose = body.count(SINGLE_CLOSE) - len(
        re.findall("(?<=[A-Za-z])" + re.escape(SINGLE_CLOSE) + "(?=[A-Za-z])", body))
    return check("QUOTE_CONVENTION", len(used) <= 1 and loose <= 0,
                 "conventions=%s non-apostrophe curly single=%d" %
                 (used or "none", loose))


PUNCT_IN_QUOTE = re.compile("[.,!?:;]" + re.escape(DQUOTE))


def c_quote_punct(text, lines):
    hits = PUNCT_IN_QUOTE.findall("\n".join(lines))
    return check("QUOTE_PUNCT", not hits,
                 "American-style hits: %d %s" %
                 (len(hits), sorted(set(hits)) or ""))


HEADING = re.compile(r"^#{2,3}\s*\d+\.\s*(.+)$")


def c_heading_case(text, lines):
    body = " ".join(line for line in lines if not line.lstrip().startswith("#"))
    title_case, sentence_case = [], []
    for line in lines:
        match = HEADING.match(line)
        if not match:
            continue
        words = re.findall(r"[A-Za-z]+", match.group(1))
        if len(words) < 2:
            continue
        caps = [word for word in words[1:]
                if word[0].isupper()
                and not re.search(r"(?<=[a-z,;:)] )" + re.escape(word) + r"\b", body)]
        (title_case if caps else sentence_case).append(match.group(1)[:38])
    mixed = len(title_case) >= 2 and len(sentence_case) >= 2
    detail = "title-case=%d sentence-case=%d" % (len(title_case), len(sentence_case))
    if mixed:
        detail += " e.g. %r vs %r" % (title_case[0], sentence_case[0])
    return check("HEADING_CASE", not mixed, detail)


DOI = re.compile(r"10\.\d{4,5}/[A-Za-z0-9./]+")
ITALIC = re.compile(r"(?<!\*)\*([^*\n]{6,90})\*(?!\*)")


def _titles(chunk):
    out = []
    for match in ITALIC.finditer(chunk):
        title = match.group(1).strip()
        if len(title.split()) < 2 or not title[0].isupper():
            continue
        if any(c in title for c in "$" + BSLASH):
            continue
        if "DOI" in title or DOI.search(title):
            continue
        if re.search(r"(?i)licen[cs]e|copyright|all rights|" + chr(169), title):
            continue
        if not any(word[0].isupper() for word in title.split()[1:]):
            continue
        out.append((match.start(), match.end(), title))
    return out


def c_cited_work_has_doi(text, lines):
    missing, cited_ok = [], set()
    for para in "\n".join(lines).split("\n\n"):
        if not DOI.search(para):
            continue
        para_lines = para.split("\n")
        if any(re.match(r"^\s*[-*+]\s", line) for line in para_lines):
            items, current = [], []
            for line in para_lines:
                if re.match(r"^\s*[-*+]\s", line):
                    if current:
                        items.append(" ".join(current))
                    current = [line]
                elif current:
                    current.append(line)
            if current:
                items.append(" ".join(current))
            for item in items:
                found = _titles(item)
                if not found:
                    continue
                if DOI.search(item):
                    cited_ok.add(found[0][2])
                else:
                    missing.append(found[0][2])
            continue
        spans = _titles(para)
        for k, (_start, end, title) in enumerate(spans):
            stop = spans[k + 1][0] if k + 1 < len(spans) else len(para)
            if DOI.search(para[end:stop]):
                cited_ok.add(title)
            else:
                missing.append(title)
    missing = sorted({item[:52] for item in missing if item not in cited_ok})
    return check("CITED_WORK_HAS_DOI", not missing,
                 "cited without DOI: %s" % (missing[:4] or "none"))


def portable_checks(text):
    lines = prose_lines(text)
    return [
        c_escape_artefact(text, lines),
        c_brace_balance(text, lines),
        c_quote_convention(text, lines),
        c_quote_punct(text, lines),
        c_heading_case(text, lines),
        c_cited_work_has_doi(text, lines),
    ]


def _without_inline_code(line):
    return re.sub(r"`+[^`]*`+", "", line)


def _unescaped_dollars(line):
    return len(re.findall(r"(?<!\\)\$", line))


def math_syntax_errors(lines):
    errors = []
    fenced = False
    displayed = False
    inline_pairs = 0
    display_pairs = 0
    for number, line in enumerate(lines, 1):
        stripped = line.strip()
        if line.lstrip().startswith(FENCE):
            fenced = not fenced
            continue
        if fenced:
            continue
        if stripped in LEGACY_DISPLAY_DELIMITERS:
            errors.append("legacy-display@%d" % number)
        if stripped == "$$":
            displayed = not displayed
            if not displayed:
                display_pairs += 1
            continue
        clean = _without_inline_code(line)
        if "$$" in clean:
            errors.append("embedded-display@%d" % number)
        if displayed:
            continue
        if any(token in clean for token in LEGACY_INLINE_DELIMITERS):
            errors.append("legacy-inline@%d" % number)
        dollars = _unescaped_dollars(clean)
        if dollars % 2:
            errors.append("unbalanced-inline@%d" % number)
        else:
            inline_pairs += dollars // 2
    if fenced:
        errors.append("unclosed-fence")
    if displayed:
        errors.append("unclosed-display")
    if inline_pairs == 0:
        errors.append("no-inline-math")
    if display_pairs == 0:
        errors.append("no-display-math")
    return errors


def run_checks(lines):
    text = "\n".join(lines)
    res = []

    markers = [i for i, line in enumerate(lines, 1) if line.strip() == "$$"]
    opens = markers[::2]
    closes = markers[1::2]
    balanced = (bool(markers) and len(markers) % 2 == 0
                and all(opener < closer for opener, closer in zip(opens, closes)))
    res.append(check("DISPLAY_BALANCE", balanced,
                     "open=%d close=%d" % (len(opens), len(closes))))

    syntax = math_syntax_errors(lines)
    res.append(check("MATH_DELIMITER_SYNTAX", not syntax,
                     "errors=%s" % (syntax[:6] or "none")))

    nums = [int(match.group(1)) for match in
            (re.match(r"^#{1,3}\s*(\d+)\.", line) for line in lines) if match]
    gap = next((number for index, number in enumerate(nums, 1)
                if number != index), "none")
    res.append(check("HEADING_SEQUENCE", nums == list(range(1, len(nums) + 1)),
                     "sections=%d first gap: %s" % (len(nums), gap)))

    markers = sum(1 for char in set(text)
                  if ord(char) >= 0x2100
                  and (unicodedata.category(char) in ("So", "Cs", "Co")
                       or 0x1F000 <= ord(char) <= 0x1FAFF))
    res.append(check("NO_EDITORIAL_MARKER", markers == 0, "hits=%d" % markers))

    para = next((line for line in lines if CONTRACT_ANCHOR in line), "")
    missing = [declaration for declaration in REQUIRED_DECLARATIONS
               if declaration not in para]
    res.append(check("DECLARATION_CONTRACT", bool(para) and not missing,
                     "paragraph found=%s missing=%s" %
                     (bool(para), missing or "none")))

    refs = {int(match.group(1)) for match in re.finditer(r"§(\d+)", text)}
    bad = sorted(ref for ref in refs if ref < 1 or ref > len(nums))
    res.append(check("SECTION_REFS", not bad,
                     "out-of-range refs: %s" % (bad or "none")))
    res.extend(portable_checks(text))
    return res


def report(results):
    width = max(len(name) for name, _, _ in results)
    failed = sum(1 for _, ok, _ in results if not ok)
    for name, ok, detail in results:
        print("%s %-*s  %s" % ("ok  " if ok else "FAIL", width, name, detail))
    return failed


def _drop_display_closer(lines):
    out = list(lines)
    markers = [i for i, line in enumerate(out) if line.strip() == "$$"]
    del out[markers[1]]
    return out


def _first_inline_pair(lines):
    displayed = False
    for index, line in enumerate(lines):
        if line.strip() == "$$":
            displayed = not displayed
            continue
        if displayed:
            continue
        start = line.find("$")
        stop = line.find("$", start + 1) if start >= 0 else -1
        if start >= 0 and stop > start:
            return index, start, stop
    raise ValueError("inline math unavailable")


def _restore_legacy_inline(lines):
    out = list(lines)
    index, start, stop = _first_inline_pair(out)
    line = out[index]
    out[index] = line[:start] + r"\(" + line[start + 1:stop] + r"\)" + line[stop + 1:]
    return out


def _drop_inline_closer(lines):
    out = list(lines)
    index, _start, stop = _first_inline_pair(out)
    out[index] = out[index][:stop] + out[index][stop + 1:]
    return out



def _restore_legacy_display(lines):
    out = list(lines)
    markers = [i for i, line in enumerate(out) if line.strip() == "$$"]
    out[markers[0]] = r"\["
    out[markers[1]] = r"\]"
    return out


def _renumber_section(lines):
    out = list(lines)
    for i, line in enumerate(out):
        match = re.match(r"^(#{1,3}\s*)(\d+)(\..*)$", line)
        if match and int(match.group(2)) == 3:
            out[i] = "%s%d%s" % (match.group(1), 4, match.group(3))
            break
    return out


def _append_to_prose(lines, suffix):
    out = list(lines)
    for i, line in enumerate(out):
        if line.startswith("The ") and len(line) > 80:
            out[i] = line + suffix
            break
    return out


def _inject_american_quote(lines):
    return _append_to_prose(lines, ' He said "so."')


def _inject_escape_artefact(lines):
    return _append_to_prose(lines, " " + BSLASH + DQUOTE + "quoted" + BSLASH + DQUOTE)


def _inject_control_character(lines):
    return _append_to_prose(lines, " damaged" + chr(8) + "text")


def _inject_editorial_marker(lines):
    return _append_to_prose(lines, " " + chr(0x1F534))


def _drop_declaration(lines):
    return [line.replace("\\operatorname{rep}_\\ell^{[R]}",
                         "\\operatorname{alt}_\\ell^{[R]}")
            if CONTRACT_ANCHOR in line else line for line in lines]


def _bad_section_ref(lines):
    out = list(lines)
    for i, line in enumerate(out):
        if "§15" in line:
            out[i] = line.replace("§15", "§37", 1)
            break
    return out


def _rephrase(lines):
    out = list(lines)
    for i, line in enumerate(out):
        if line.startswith("The ") and len(line) > 120:
            out[i] = line.replace("The ", "This ", 1)
            break
    return out


def _inject_stray_quote(lines):
    return _append_to_prose(lines, " " + GUILL_OPEN + "stray" + GUILL_CLOSE)


def _break_brace_pair(lines):
    return [line.replace("\\{P_3\\}", "\\{P_3}", 1)
            if "\\{P_3\\}" in line else line for line in lines]


def _title_case_a_heading(lines):
    out = list(lines)
    for i, line in enumerate(out):
        if line.startswith("## 6. "):
            out[i] = "## 6. Crowns Of Evolution"
        elif line.startswith("## 13. "):
            out[i] = "## 13. Isolation As Method"
    return out


def _drop_cited_doi(lines):
    out = list(lines)
    old = "(DOI: [10.17605/OSF.IO/7EUWK](https://doi.org/10.17605/OSF.IO/7EUWK))"
    for i, line in enumerate(out):
        if old in line:
            out[i] = line.replace(old, "(identifier omitted)", 1)
            break
    return out


TEETH = [
    ("drop a display closer", _drop_display_closer, "RED", "DISPLAY_BALANCE"),
    ("restore a legacy inline wrapper", _restore_legacy_inline,
     "RED", "MATH_DELIMITER_SYNTAX"),
    ("drop an inline closer", _drop_inline_closer,
     "RED", "MATH_DELIMITER_SYNTAX"),
    ("restore legacy display wrappers", _restore_legacy_display,
     "RED", "MATH_DELIMITER_SYNTAX"),
    ("renumber a section", _renumber_section, "RED", "HEADING_SEQUENCE"),
    ("inject american quote punctuation", _inject_american_quote, "RED", "QUOTE_PUNCT"),
    ("inject a prose escape", _inject_escape_artefact, "RED", "ESCAPE_ARTEFACT"),
    ("inject a control character", _inject_control_character, "RED", "ESCAPE_ARTEFACT"),
    ("inject an editorial marker", _inject_editorial_marker, "RED", "NO_EDITORIAL_MARKER"),
    ("drop an object from the contract", _drop_declaration, "RED", "DECLARATION_CONTRACT"),
    ("reference a nonexistent section", _bad_section_ref, "RED", "SECTION_REFS"),
    ("inject a stray quote mark", _inject_stray_quote, "RED", "QUOTE_CONVENTION"),
    ("close an escaped brace with a bare one", _break_brace_pair, "RED", "BRACE_BALANCE"),
    ("title-case two headings", _title_case_a_heading, "RED", "HEADING_CASE"),
    ("drop a cited work's DOI", _drop_cited_doi, "RED", "CITED_WORK_HAS_DOI"),
    ("rephrase prose", _rephrase, "SURVIVE", None),
]


def registry_errors(results, teeth):
    checks = {name for name, _, _ in results}
    covered = {marker for _, _, expectation, marker in teeth
               if expectation == "RED" and marker}
    return sorted(checks - covered), sorted(covered - checks)


def run_teeth(lines):
    base = run_checks(lines)
    if any(not ok for _, ok, _ in base):
        print("teeth aborted: the battery needs a green baseline")
        return 1
    missing, unknown = registry_errors(base, TEETH)
    if missing or unknown:
        print("FAIL registry -> missing=%s unknown=%s" % (missing, unknown))
        return 1

    probe = [tooth for tooth in TEETH if tooth[3] != "CITED_WORK_HAS_DOI"]
    probe_missing, probe_unknown = registry_errors(base, probe)
    if probe_missing != ["CITED_WORK_HAS_DOI"] or probe_unknown:
        print("FAIL registry self-test -> missing=%s unknown=%s" %
              (probe_missing, probe_unknown))
        return 1
    print("ok   RED      %-38s -> %s" %
          ("remove one registered tooth", "CITED_WORK_HAS_DOI"))

    passed = 1
    for name, mutate, expectation, marker in TEETH:
        results = run_checks(mutate(lines))
        reds = [check_name for check_name, ok, _ in results if not ok]
        if expectation == "RED":
            if not reds:
                print("FAIL %-42s -> no check reddened" % name)
                continue
            if reds[0] != marker:
                print("FAIL %-42s -> shadowed by %s" % (name, reds[0]))
                continue
            print("ok   RED      %-38s -> %s" % (name, marker))
        else:
            if reds:
                print("FAIL %-42s -> reddened %s" % (name, reds))
                continue
            print("ok   SURVIVE  %-38s" % name)
        passed += 1
    total = len(TEETH) + 1
    print("teeth: %d/%d" % (passed, total))
    return 0 if passed == total else 1


if __name__ == "__main__":
    document = read_lines(DOC)
    if "--teeth" in sys.argv:
        raise SystemExit(run_teeth(document))
    raise SystemExit(1 if report(run_checks(document)) else 0)
