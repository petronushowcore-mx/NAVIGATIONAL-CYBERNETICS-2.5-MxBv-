# Crown of Evolution — executable verification

This standard-library companion checks the public English manuscript's structure, mathematical delimiter discipline, declared textual bindings, and mutation sensitivity. It does not replace mathematical reading or extend the manuscript's stated scope.

Requirements: Python 3.10 or later. From the repository root in PowerShell:

```powershell
$env:CROWN_MANUSCRIPT = "ARCHITECTURE/Architectural Evolution with Navigational Cybernetics. Part One - The Crown.md"
python -B ARCHITECTURE/crown-of-evolution-harness/gate_en.py
python -B ARCHITECTURE/crown-of-evolution-harness/gate_en.py --teeth
python -B -O ARCHITECTURE/crown-of-evolution-harness/gate_en.py
python -B -O ARCHITECTURE/crown-of-evolution-harness/gate_en.py --teeth
```

Every command must exit with status `0`; each mutation run ends with `teeth: 17/17`.

The files in this directory are licensed under the MIT License; see [LICENSE](LICENSE).
