# What Castaneda Did Not Say — executable verification

This standard-library companion reconstructs the finite projection-preserving product-event witness and checks its named conditions. Its isolated mutation battery demonstrates first failure for each encoded condition. It imports the published NC2.5 membership result; it does not reprove full A1–A61 conformance or model a human subject.

Requirements: Python 3.10 or later. From the repository root:

```powershell
python -B PHILOSOPHY/what-castaneda-did-not-say-harness/verify_nonemptiness.py
python -B PHILOSOPHY/what-castaneda-did-not-say-harness/negative_tests.py
python -B -O PHILOSOPHY/what-castaneda-did-not-say-harness/verify_nonemptiness.py
python -B -O PHILOSOPHY/what-castaneda-did-not-say-harness/negative_tests.py
```

Every command must exit with status `0`. The witness output contains `"status": "PASS"`, and each mutation run ends with `RESULT PASS isolated_mutations=31`.

The files in this directory are licensed under the MIT License; see [LICENSE](LICENSE).
