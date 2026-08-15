"""Realistic first-red mutations for every scientific check."""

from __future__ import annotations

from dataclasses import replace
from fractions import Fraction
from typing import Callable

from verify_nonemptiness import (
    CHECKS,
    CombinedWitness,
    CrownHistory,
    default_witness,
    failed_markers,
)


Mutation = Callable[[CombinedWitness], CombinedWitness]


def _replace_candidate_row(
    witness: CombinedWitness, state: str, candidates: tuple[str, ...]
) -> CombinedWitness:
    crown = witness.crown
    rows = crown.candidate_rows
    if rows is None:
        return witness
    new_rows = tuple(
        (source, candidates if source == state else existing)
        for source, existing in rows
    )
    return replace(witness, crown=replace(crown, candidate_rows=new_rows))


def _replace_history(
    witness: CombinedWitness,
    states: tuple[str, ...],
    *,
    active: bool | None = None,
    admitted: bool | None = None,
) -> CombinedWitness:
    crown = witness.crown
    histories = tuple(
        replace(
            history,
            active=history.active if active is None else active,
            admitted=history.admitted if admitted is None else admitted,
        )
        if history.states == states
        else history
        for history in crown.histories
    )
    return replace(witness, crown=replace(crown, histories=histories))


def break_nc_parameter_instance(witness: CombinedWitness) -> CombinedWitness:
    return replace(witness, nc=replace(witness.nc, floor=Fraction(0)))


def break_safe_fallback(witness: CombinedWitness) -> CombinedWitness:
    return replace(witness, nc=replace(witness.nc, safe_actions=()))


def break_gate_prior(witness: CombinedWitness) -> CombinedWitness:
    return replace(
        witness, nc=replace(witness.nc, execution_order=("event", "gate"))
    )


def break_gate_immutable(witness: CombinedWitness) -> CombinedWitness:
    nc = witness.nc
    return replace(
        witness,
        nc=replace(nc, gate_writers=nc.gate_writers + (nc.runtime_actor,)),
    )


def break_finite_generator(witness: CombinedWitness) -> CombinedWitness:
    return replace(witness, crown=replace(witness.crown, candidate_rows=None))


def break_finite_generator_domain(witness: CombinedWitness) -> CombinedWitness:
    crown = witness.crown
    return replace(
        witness,
        crown=replace(
            crown, admitted_edges=crown.admitted_edges + (("x0", "ghost"),)
        ),
    )


def break_history_domain(witness: CombinedWitness) -> CombinedWitness:
    crown = witness.crown
    bad = CrownHistory(("x0", "ghost"), active=False, admitted=False)
    return replace(
        witness, crown=replace(crown, histories=crown.histories + (bad,))
    )


def break_history_k_connection(witness: CombinedWitness) -> CombinedWitness:
    crown = witness.crown
    k_edges = tuple(
        edge for edge in crown.k_edges if edge != ("x0", "empty")
    )
    return replace(witness, crown=replace(crown, k_edges=k_edges))


def break_false_admitted_label(witness: CombinedWitness) -> CombinedWitness:
    crown = witness.crown
    mislabeled = CrownHistory(("x0", "old"), active=True, admitted=True)
    return replace(
        witness,
        crown=replace(crown, histories=crown.histories + (mislabeled,)),
    )


def break_k_nondegenerate(witness: CombinedWitness) -> CombinedWitness:
    crown = witness.crown
    complete = tuple(
        (source, target) for source in crown.states for target in crown.states
    )
    return replace(witness, crown=replace(crown, k_edges=complete))


def break_crown_composite(witness: CombinedWitness) -> CombinedWitness:
    return _replace_candidate_row(witness, "empty", ("x0",))


def break_crown_composite_reachability(
    witness: CombinedWitness,
) -> CombinedWitness:
    return _replace_history(witness, ("x0", "empty"), admitted=False)


def break_realized_unique(witness: CombinedWitness) -> CombinedWitness:
    return replace(
        witness,
        crown=replace(witness.crown, next_states=("x1", "old")),
    )


def break_realized_admissible(witness: CombinedWitness) -> CombinedWitness:
    return replace(
        witness, crown=replace(witness.crown, next_states=("empty",))
    )


def break_identity_preserved(witness: CombinedWitness) -> CombinedWitness:
    return replace(
        witness, crown=replace(witness.crown, identity_preserved=False)
    )


def break_unit_retained(witness: CombinedWitness) -> CombinedWitness:
    return replace(witness, crown=replace(witness.crown, post_unit="unit-j"))


def break_history_extended(witness: CombinedWitness) -> CombinedWitness:
    return replace(
        witness,
        crown=replace(witness.crown, post_history=("x0", "x0", "x1")),
    )


def break_history_terminal_alignment(witness: CombinedWitness) -> CombinedWitness:
    return replace(
        witness,
        crown=replace(witness.crown, pre_history=("x1",)),
    )


def break_fields_nonempty(witness: CombinedWitness) -> CombinedWitness:
    crown = witness.crown
    new_edges = tuple(edge for edge in crown.k_edges if edge[0] != "x1")
    return replace(witness, crown=replace(crown, k_edges=new_edges))


def break_fields_incomparable(witness: CombinedWitness) -> CombinedWitness:
    changed = _replace_candidate_row(witness, "x1", ("old",))
    crown = changed.crown
    new_edges = tuple(edge for edge in crown.k_edges if edge[0] != "x1")
    return replace(
        changed,
        crown=replace(crown, k_edges=new_edges + (("x1", "old"),)),
    )


def break_focal_authorization(witness: CombinedWitness) -> CombinedWitness:
    return replace(witness, event=replace(witness.event, nc_action="u-forbidden"))


def break_focal_distinctness(witness: CombinedWitness) -> CombinedWitness:
    return replace(witness, event=replace(witness.event, nc_action="u0"))


def break_product_nc_projection(witness: CombinedWitness) -> CombinedWitness:
    bad_nc = replace(witness.event.pre.nc, burden=Fraction(4))
    return replace(
        witness,
        event=replace(
            witness.event, pre=replace(witness.event.pre, nc=bad_nc)
        ),
    )


def break_nc_reduct_preservation(witness: CombinedWitness) -> CombinedWitness:
    altered_post = replace(witness.event.post.nc, burden=Fraction(4))
    altered_record = replace(
        witness.action_realisations[0], post=altered_post
    )
    altered_event = replace(
        witness.event, post=replace(witness.event.post, nc=altered_post)
    )
    return replace(
        witness,
        action_realisations=(altered_record,),
        event=altered_event,
    )


def break_product_crown_projection(witness: CombinedWitness) -> CombinedWitness:
    return replace(
        witness,
        event=replace(
            witness.event, post=replace(witness.event.post, crown="old")
        ),
    )


def break_product_transition(witness: CombinedWitness) -> CombinedWitness:
    consistent = _replace_history(
        witness, witness.crown.post_history, admitted=False
    )
    crown = consistent.crown
    admitted = tuple(edge for edge in crown.admitted_edges if edge != ("x0", "x1"))
    return replace(consistent, crown=replace(crown, admitted_edges=admitted))


def break_holding_contribution_missing(witness: CombinedWitness) -> CombinedWitness:
    """Drop the contribution for an active admitted edge."""
    crown = witness.crown
    contributions = tuple(
        row for row in crown.hold_contributions if row[0] != ("x0", "empty")
    )
    return replace(witness, crown=replace(crown, hold_contributions=contributions))


def break_holding_contribution_zero(witness: CombinedWitness) -> CombinedWitness:
    """Erase the positive contribution of the realised focal edge."""
    crown = witness.crown
    contributions = tuple(
        (edge, Fraction(0) if edge == ("x0", "x1") else value)
        for edge, value in crown.hold_contributions
    )
    return replace(witness, crown=replace(crown, hold_contributions=contributions))

def break_cumulative_cost_monotone(witness: CombinedWitness) -> CombinedWitness:
    """The record is overwritten by the window value instead of accumulating.

    This is how the fact disappears in the countermodel: the post-history
    entry falls below its own prefix.  Nothing else in the witness moves.
    """
    crown = witness.crown
    records = tuple(
        (history, Fraction(1) if history == crown.post_history else value)
        for history, value in crown.hold_records
    )
    return replace(witness, crown=replace(crown, hold_records=records))


def break_cumulative_zero_base(witness: CombinedWitness) -> CombinedWitness:
    """Apply a uniform affine shift while preserving every edge recurrence."""
    crown = witness.crown
    records = tuple(
        (history, value + Fraction(7)) for history, value in crown.hold_records
    )
    return replace(witness, crown=replace(crown, hold_records=records))


def break_focal_reachability(witness: CombinedWitness) -> CombinedWitness:
    return _replace_history(witness, witness.crown.pre_history, active=False)


def mutation_registry_failures(
    checks: tuple[tuple[str, Callable[[CombinedWitness], bool]], ...] = CHECKS,
    cases: tuple[tuple[str, str, Mutation], ...] | None = None,
) -> list[str]:
    """Fail closed when a scientific check lacks a realistic mutation."""
    active_cases = CASES if cases is None else cases
    check_markers = [marker for marker, _ in checks]
    case_ids = [case_id for case_id, _, _ in active_cases]
    expected_markers = {marker for _, marker, _ in active_cases}
    failures: list[str] = []
    if len(check_markers) != len(set(check_markers)) or len(case_ids) != len(set(case_ids)):
        failures.append("MUTATION_REGISTRY_UNIQUE")
    if set(check_markers) != expected_markers:
        failures.append("MUTATION_REGISTRY_COVERS_CHECKS")
    return failures

CASES: tuple[tuple[str, str, Mutation], ...] = (
    ("nc-floor", "NC_PARAMETER_INSTANCE", break_nc_parameter_instance),
    ("safe-set", "SAFE_FALLBACK", break_safe_fallback),
    ("event-order", "GATE_PRIOR", break_gate_prior),
    ("runtime-writer", "RUNTIME_NOT_GATE_WRITER", break_gate_immutable),
    ("finite-generator-removed", "FINITE_GENERATOR", break_finite_generator),
    ("event-domain", "FINITE_GENERATOR", break_finite_generator_domain),
    ("history-domain", "HISTORY_DECLARATIONS", break_history_domain),
    ("history-k-edge-removed", "HISTORY_DECLARATIONS", break_history_k_connection),
    ("false-admitted-label", "HISTORY_DECLARATIONS", break_false_admitted_label),
    ("complete-k", "K_NONDEGENERATE", break_k_nondegenerate),
    (
        "empty-field-erased",
        "CROWN_COMPOSITE_NONDEGENERATE",
        break_crown_composite,
    ),
    (
        "empty-history-not-admitted",
        "CROWN_COMPOSITE_NONDEGENERATE",
        break_crown_composite_reachability,
    ),
    ("two-successors", "REALIZED_UNIQUE", break_realized_unique),
    ("successor-outside-field", "REALIZED_ADMISSIBLE", break_realized_admissible),
    ("identity-flip", "ID_PRESERVED", break_identity_preserved),
    ("unit-replacement", "UNIT_RETAINED", break_unit_retained),
    (
        "history-terminal-misaligned",
        "HISTORY_TERMINALS_ALIGNED",
        break_history_terminal_alignment,
    ),
    ("history-extra-prefix", "HISTORY_EXTENDED", break_history_extended),
    ("empty-post-field", "FIELDS_NONEMPTY", break_fields_nonempty),
    ("mere-narrowing", "FIELDS_INCOMPARABLE", break_fields_incomparable),
    (
        "holding-contribution-missing",
        "HOLDING_CONTRIBUTIONS",
        break_holding_contribution_missing,
    ),
    (
        "holding-contribution-zero",
        "HOLDING_CONTRIBUTIONS",
        break_holding_contribution_zero,
    ),
    (
        "cumulative-record-overwritten",
        "CUMULATIVE_HOLDING",
        break_cumulative_cost_monotone,
    ),
    (
        "cumulative-record-affine-shift",
        "CUMULATIVE_HOLDING",
        break_cumulative_zero_base,
    ),
    ("focal-action-unauthorized", "FOCAL_ACTION", break_focal_authorization),
    ("focal-action-is-fallback", "FOCAL_ACTION", break_focal_distinctness),
    (
        "nc-event-projection-split",
        "PRODUCT_EVENT_COMMUTES",
        break_product_nc_projection,
    ),
    (
        "nc-reduct-co-mutated",
        "NC_REDUCT_PRESERVED",
        break_nc_reduct_preservation,
    ),
    (
        "crown-event-projection-split",
        "PRODUCT_EVENT_COMMUTES",
        break_product_crown_projection,
    ),
    (
        "focal-admitted-edge-removed",
        "PRODUCT_EVENT_COMMUTES",
        break_product_transition,
    ),
    ("focal-pre-history-inactive", "FOCAL_REACHABLE", break_focal_reachability),
)


def main() -> int:
    registry_failures = mutation_registry_failures()
    if registry_failures:
        print("REGISTRY_FAIL " + ",".join(registry_failures))
        return 1

    missing_probe = CHECKS + (("UNREGISTERED_CHECK", lambda _: True),)
    probe_failures = mutation_registry_failures(checks=missing_probe)
    if probe_failures != ["MUTATION_REGISTRY_COVERS_CHECKS"]:
        print("REGISTRY_SELF_TEST_FAIL " + ",".join(probe_failures))
        return 1
    print("REGISTRY_SELF_TEST_PASS marker=MUTATION_REGISTRY_COVERS_CHECKS")
    baseline = default_witness()
    baseline_failures = failed_markers(baseline)
    if baseline_failures:
        print("BASELINE_FAIL " + ",".join(baseline_failures))
        return 1

    failed_cases: list[str] = []
    for case_id, expected, mutate in CASES:
        failures = failed_markers(mutate(baseline))
        observed = failures[0] if failures else "NO_FAILURE"
        if observed != expected:
            failed_cases.append(f"{case_id}:{expected}->{observed}")
            print(f"MUTATION_FAIL case={case_id} expected={expected} first={observed}")
        else:
            print(f"MUTATION_PASS case={case_id} marker={expected}")

    if failed_cases:
        print("RESULT FAIL " + ";".join(failed_cases))
        return 1

    print(f"RESULT PASS isolated_mutations={len(CASES)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
