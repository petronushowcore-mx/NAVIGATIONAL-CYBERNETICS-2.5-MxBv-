"""Construct one projection-preserving NC2.5/Crown continuation expansion.

Membership of the NC reduct in the published load-bearing class is imported
from the cited NC2.5 formal witness.  This module rechecks the numerical
instance and certifies the finite expansion; it does not claim full A1--A61
conformance or independently reproduce the source membership proof.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction
from typing import Callable


Q = Fraction


@dataclass(frozen=True)
class NCState:
    theta: Fraction
    burden: Fraction


@dataclass(frozen=True)
class NCActionRealisation:
    pre: NCState
    action: str
    post: NCState


@dataclass(frozen=True)
class NC25CoreWitness:
    capacity: Fraction
    initial_burden: Fraction
    floor: Fraction
    pressure: Fraction
    spin_rate: Fraction
    action_costs: tuple[tuple[str, Fraction], ...]
    safe_actions: tuple[str, ...]
    execution_order: tuple[str, ...]
    gate_writers: tuple[str, ...]
    runtime_actor: str
    initial_state: NCState


@dataclass(frozen=True)
class CrownHistory:
    states: tuple[str, ...]
    active: bool
    admitted: bool


@dataclass(frozen=True)
class CrownContinuationWitness:
    states: tuple[str, ...]
    initial_state: str
    admitted_edges: tuple[tuple[str, str], ...]
    histories: tuple[CrownHistory, ...]
    candidate_rows: tuple[tuple[str, tuple[str, ...]], ...] | None
    k_edges: tuple[tuple[str, str], ...]
    pre_state: str
    post_state: str
    next_states: tuple[str, ...]
    identity_preserved: bool
    pre_unit: str
    post_unit: str
    pre_history: tuple[str, ...]
    post_history: tuple[str, ...]
    # Crown-side cumulative holding record: a functional on admissible
    # histories, nondecreasing under prefix extension.  Kept separate from the
    # NC burden -- no map between them is declared.
    hold_contributions: tuple[tuple[tuple[str, str], Fraction], ...]
    hold_records: tuple[tuple[tuple[str, ...], Fraction], ...]


@dataclass(frozen=True)
class ProductState:
    nc: NCState
    crown: str


@dataclass(frozen=True)
class ProductEvent:
    occurrence_id: str
    pre: ProductState
    post: ProductState
    nc_action: str


@dataclass(frozen=True)
class CombinedWitness:
    nc: NC25CoreWitness
    crown: CrownContinuationWitness
    action_realisations: tuple[NCActionRealisation, ...]
    event: ProductEvent


def default_witness() -> CombinedWitness:
    s0 = NCState(theta=Q(0), burden=Q(3))
    nc = NC25CoreWitness(
        capacity=Q(12),
        initial_burden=Q(3),
        floor=Q(2),
        pressure=Q(2),
        spin_rate=Q(1),
        action_costs=(("u0", Q(0)), ("u1", Q(4))),
        safe_actions=("u0",),
        execution_order=("gate", "event"),
        gate_writers=("declared-boundary",),
        runtime_actor="runtime",
        initial_state=s0,
    )
    crown = CrownContinuationWitness(
        states=("x0", "x1", "old", "new", "aux", "empty"),
        initial_state="x0",
        admitted_edges=(("x0", "x1"), ("x0", "empty")),
        histories=(
            CrownHistory(("x0",), active=True, admitted=True),
            CrownHistory(("x0", "x1"), active=True, admitted=True),
            CrownHistory(("x0", "empty"), active=True, admitted=True),
        ),
        candidate_rows=(
            ("x0", ("x1", "old")),
            ("x1", ("new", "aux")),
            ("old", ()),
            ("new", ()),
            ("aux", ()),
            ("empty", ()),
        ),
        k_edges=(
            ("x0", "x1"),
            ("x0", "old"),
            ("x0", "empty"),
            ("x1", "new"),
            ("x1", "aux"),
            ("empty", "x0"),
        ),
        pre_state="x0",
        post_state="x1",
        next_states=("x1",),
        identity_preserved=True,
        pre_unit="unit-i",
        post_unit="unit-i",
        pre_history=("x0",),
        post_history=("x0", "x1"),
        hold_contributions=(
            (("x0", "x1"), Q(3)),
            (("x0", "empty"), Q(0)),
        ),
        hold_records=(
            (("x0",), Q(0)),
            (("x0", "x1"), Q(3)),
            (("x0", "empty"), Q(0)),
        ),
    )
    event = ProductEvent(
        occurrence_id="shift-1",
        pre=ProductState(nc=s0, crown="x0"),
        post=ProductState(nc=s0, crown="x1"),
        nc_action="u1",
    )
    return CombinedWitness(
        nc=nc,
        crown=crown,
        action_realisations=(NCActionRealisation(s0, "u1", s0),),
        event=event,
    )


def _action_costs(nc: NC25CoreWitness) -> dict[str, Fraction]:
    return dict(nc.action_costs)


def gate_value(
    nc: NC25CoreWitness, action: str, state: NCState | None = None
) -> bool:
    costs = _action_costs(nc)
    if action not in costs:
        return False
    burden = nc.initial_burden if state is None else state.burden
    return nc.capacity - burden - costs[action] >= nc.floor


def admissible_field(
    crown: CrownContinuationWitness, state: str
) -> frozenset[str]:
    rows = dict(crown.candidate_rows or ())
    candidates = rows.get(state, ())
    edges = set(crown.k_edges)
    return frozenset(
        target for target in candidates if (state, target) in edges
    )


def _history_domain_valid(
    crown: CrownContinuationWitness, history: CrownHistory
) -> bool:
    states = set(crown.states)
    return (
        isinstance(history.states, tuple)
        and bool(history.states)
        and history.states[0] == crown.initial_state
        and set(history.states).issubset(states)
        and isinstance(history.active, bool)
        and isinstance(history.admitted, bool)
    )


def _history_path_k_connected(
    crown: CrownContinuationWitness, history: CrownHistory
) -> bool:
    k_edges = set(crown.k_edges)
    return _history_domain_valid(crown, history) and all(
        edge in k_edges
        for edge in zip(history.states, history.states[1:])
    )


def _history_path_admitted(
    crown: CrownContinuationWitness, history: CrownHistory
) -> bool:
    admitted_edges = set(crown.admitted_edges)
    return _history_path_k_connected(crown, history) and all(
        edge in admitted_edges
        for edge in zip(history.states, history.states[1:])
    )


def active_admitted_histories(
    crown: CrownContinuationWitness,
) -> tuple[CrownHistory, ...]:
    return tuple(
        history
        for history in crown.histories
        if history.active
        and history.admitted
        and _history_path_admitted(crown, history)
    )


def active_admitted_terminal_states(
    crown: CrownContinuationWitness,
) -> frozenset[str]:
    return frozenset(
        history.states[-1] for history in active_admitted_histories(crown)
    )


def project_nc_event(event: ProductEvent) -> NCActionRealisation:
    return NCActionRealisation(event.pre.nc, event.nc_action, event.post.nc)


def project_crown_event(event: ProductEvent) -> tuple[str, str]:
    return (event.pre.crown, event.post.crown)


def _nc_parameter_instance(witness: CombinedWitness) -> bool:
    nc = witness.nc
    costs = _action_costs(nc)
    return (
        nc.capacity > 0
        and 0 < nc.floor < nc.capacity
        and 0 <= nc.initial_burden < nc.capacity - nc.floor
        and nc.initial_state.burden == nc.initial_burden
        and nc.pressure > 0
        and nc.spin_rate > 0
        and len(costs) == len(nc.action_costs)
        and all(cost >= 0 for cost in costs.values())
        and nc.pressure * (1 - nc.initial_burden / nc.capacity) > 0
    )


def _safe_fallback(witness: CombinedWitness) -> bool:
    nc = witness.nc
    costs = _action_costs(nc)
    return (
        bool(nc.safe_actions)
        and "u0" in nc.safe_actions
        and costs.get("u0") == 0
        and all(
            action in costs and gate_value(nc, action, nc.initial_state)
            for action in nc.safe_actions
        )
    )


def _gate_prior(witness: CombinedWitness) -> bool:
    order = witness.nc.execution_order
    return (
        order.count("gate") == 1
        and order.count("event") == 1
        and order.index("gate") < order.index("event")
    )


def _gate_immutable(witness: CombinedWitness) -> bool:
    nc = witness.nc
    return bool(nc.gate_writers) and nc.runtime_actor not in nc.gate_writers


def _finite_generator(witness: CombinedWitness) -> bool:
    crown = witness.crown
    rows = crown.candidate_rows
    states = set(crown.states)
    if not isinstance(rows, tuple) or not states or len(states) != len(crown.states):
        return False
    if crown.initial_state not in states:
        return False
    if not isinstance(crown.admitted_edges, tuple) or any(
        source not in states or target not in states
        for source, target in crown.admitted_edges
    ):
        return False
    if len(set(crown.admitted_edges)) != len(crown.admitted_edges):
        return False
    sources: list[str] = []
    for row in rows:
        if not isinstance(row, tuple) or len(row) != 2:
            return False
        source, candidates = row
        if source not in states or not isinstance(candidates, tuple):
            return False
        if any(target not in states for target in candidates):
            return False
        sources.append(source)
    if len(sources) != len(set(sources)) or set(sources) != states:
        return False
    if any(source not in states or target not in states for source, target in crown.k_edges):
        return False
    return len(set(crown.k_edges)) == len(crown.k_edges)


def _history_declarations(witness: CombinedWitness) -> bool:
    crown = witness.crown
    return (
        isinstance(crown.histories, tuple)
        and bool(crown.histories)
        and all(
            isinstance(history, CrownHistory)
            and _history_path_k_connected(crown, history)
            and (not history.admitted or _history_path_admitted(crown, history))
            for history in crown.histories
        )
        and len({history.states for history in crown.histories})
        == len(crown.histories)
    )


def _k_nondegenerate(witness: CombinedWitness) -> bool:
    crown = witness.crown
    edges = set(crown.k_edges)
    return any(
        (source, target) not in edges
        for source in crown.states
        for target in crown.states
    )


def _realized_unique(witness: CombinedWitness) -> bool:
    crown = witness.crown
    return (
        isinstance(crown.next_states, tuple)
        and len(crown.next_states) == 1
        and crown.next_states[0] in set(crown.states)
    )


def _realized_admissible(witness: CombinedWitness) -> bool:
    crown = witness.crown
    return (
        len(crown.next_states) == 1
        and crown.next_states[0] in admissible_field(crown, crown.pre_state)
    )


def _identity_preserved(witness: CombinedWitness) -> bool:
    return witness.crown.identity_preserved is True


def _unit_retained(witness: CombinedWitness) -> bool:
    crown = witness.crown
    return bool(crown.pre_unit) and crown.pre_unit == crown.post_unit


def _history_terminals_aligned(witness: CombinedWitness) -> bool:
    crown = witness.crown
    return (
        bool(crown.pre_history)
        and bool(crown.post_history)
        and crown.pre_history[-1] == crown.pre_state
        and crown.post_history[-1] == crown.post_state
    )


def _history_extended(witness: CombinedWitness) -> bool:
    crown = witness.crown
    if len(crown.next_states) != 1:
        return False
    realized = crown.next_states[0]
    return (
        crown.post_state == realized
        and crown.post_history == crown.pre_history + (realized,)
    )


def _fields_nonempty(witness: CombinedWitness) -> bool:
    crown = witness.crown
    return bool(admissible_field(crown, crown.pre_state)) and bool(
        admissible_field(crown, crown.post_state)
    )


def _fields_incomparable(witness: CombinedWitness) -> bool:
    crown = witness.crown
    pre_field = admissible_field(crown, crown.pre_state)
    post_field = admissible_field(crown, crown.post_state)
    return bool(pre_field - post_field) and bool(post_field - pre_field)


def _holding_contributions(witness: CombinedWitness) -> bool:
    """Every active admitted edge has one nonnegative contribution.

    The focal realised edge must carry a strictly positive contribution.
    """
    crown = witness.crown
    contributions = dict(crown.hold_contributions)
    active_edges = {
        edge
        for history in active_admitted_histories(crown)
        for edge in zip(history.states, history.states[1:])
    }
    focal = (crown.pre_state, crown.post_state)
    return (
        len(contributions) == len(crown.hold_contributions)
        and set(contributions) == active_edges
        and all(value >= 0 for value in contributions.values())
        and contributions.get(focal, Q(0)) > 0
    )


def _cumulative_holding(witness: CombinedWitness) -> bool:
    """The record starts at zero and then accumulates edge contributions."""
    crown = witness.crown
    contributions = dict(crown.hold_contributions)
    records = dict(crown.hold_records)
    histories = active_admitted_histories(crown)
    if (
        len(records) != len(crown.hold_records)
        or set(records) != {history.states for history in histories}
        or any(value < 0 for value in records.values())
    ):
        return False
    roots = [history.states for history in histories if len(history.states) == 1]
    if roots != [(crown.initial_state,)] or records[roots[0]] != Q(0):
        return False
    for history in histories:
        states = history.states
        if len(states) <= 1:
            continue
        prefix = states[:-1]
        edge = (states[-2], states[-1])
        if prefix not in records or edge not in contributions:
            return False
        if records[states] != records[prefix] + contributions[edge]:
            return False
    return True


def _focal_action(witness: CombinedWitness) -> bool:
    nc = witness.nc
    action = witness.event.nc_action
    costs = _action_costs(nc)
    return (
        action in costs
        and costs[action] > 0
        and action not in nc.safe_actions
        and gate_value(nc, action, witness.event.pre.nc)
    )


def _product_event_commutes(witness: CombinedWitness) -> bool:
    event = witness.event
    crown = witness.crown
    return (
        bool(event.occurrence_id)
        and event.pre.nc == witness.nc.initial_state
        and event.pre.crown == crown.pre_state
        and event.post.crown == crown.post_state
        and project_nc_event(event) in witness.action_realisations
        and project_crown_event(event) in crown.admitted_edges
    )


def _nc_reduct_preserved(witness: CombinedWitness) -> bool:
    source_state = witness.nc.initial_state
    event = witness.event
    return event.pre.nc == source_state and event.post.nc == source_state


def _focal_reachable(witness: CombinedWitness) -> bool:
    crown = witness.crown
    histories = {history.states for history in active_admitted_histories(crown)}
    return crown.pre_history in histories and crown.post_history in histories


def _crown_composite_nondegenerate(witness: CombinedWitness) -> bool:
    crown = witness.crown
    terminals = active_admitted_terminal_states(crown)
    fields = [admissible_field(crown, state) for state in terminals]
    return bool(fields) and any(not field for field in fields) and any(
        bool(field) for field in fields
    )


Check = tuple[str, Callable[[CombinedWitness], bool]]
CHECKS: tuple[Check, ...] = (
    ("NC_PARAMETER_INSTANCE", _nc_parameter_instance),
    ("SAFE_FALLBACK", _safe_fallback),
    ("GATE_PRIOR", _gate_prior),
    ("RUNTIME_NOT_GATE_WRITER", _gate_immutable),
    ("FINITE_GENERATOR", _finite_generator),
    ("HISTORY_DECLARATIONS", _history_declarations),
    ("K_NONDEGENERATE", _k_nondegenerate),
    ("REALIZED_UNIQUE", _realized_unique),
    ("REALIZED_ADMISSIBLE", _realized_admissible),
    ("ID_PRESERVED", _identity_preserved),
    ("UNIT_RETAINED", _unit_retained),
    ("HISTORY_TERMINALS_ALIGNED", _history_terminals_aligned),
    ("HISTORY_EXTENDED", _history_extended),
    ("FIELDS_NONEMPTY", _fields_nonempty),
    ("FIELDS_INCOMPARABLE", _fields_incomparable),
    ("FOCAL_ACTION", _focal_action),
    ("PRODUCT_EVENT_COMMUTES", _product_event_commutes),
    ("NC_REDUCT_PRESERVED", _nc_reduct_preserved),
    ("FOCAL_REACHABLE", _focal_reachable),
    ("CROWN_COMPOSITE_NONDEGENERATE", _crown_composite_nondegenerate),
    ("HOLDING_CONTRIBUTIONS", _holding_contributions),
    ("CUMULATIVE_HOLDING", _cumulative_holding),
)


def failed_markers(witness: CombinedWitness) -> list[str]:
    return [marker for marker, check in CHECKS if not check(witness)]


def _q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def _nc_state_json(state: NCState) -> dict[str, str]:
    return {"theta": _q(state.theta), "burden": _q(state.burden)}


def certificate(witness: CombinedWitness) -> dict[str, object]:
    failures = failed_markers(witness)
    nc = witness.nc
    crown = witness.crown
    event = witness.event
    pre_field = admissible_field(crown, crown.pre_state)
    post_field = admissible_field(crown, crown.post_state)
    return {
        "claim": (
            "The published NC2.5 load-bearing witness admits a projection-preserving "
            "Crown-continuation expansion carrying a unique identity-preserving "
            "realised continuer whose generator-relative field changes and stays "
            "inclusion-incomparable while a positive holding contribution accumulates "
            "exactly; hence the corresponding subclass is non-empty."
        ),
        "status": "PASS" if not failures else "FAIL",
        "failed_markers": failures,
        "scope": {
            "nc25_source_membership": {
                "status": "imported_from_published_formal_witness",
                "recomputed_here": False,
                "load_bearing_profile": [
                    "A7",
                    "A29",
                    "A31",
                    "A43-restricted",
                    "A49",
                    "A60",
                    "A61",
                    "T62-conditions",
                ],
            },
            "executable_nc_scope": "parameter_instance_and_expansion_only",
            "nc_reduct_preserved": _nc_reduct_preserved(witness),
            "crown_profile": [
                "finite-candidate-generator",
                "K-connected-declared-histories",
                "admission-consistent-declared-histories",
                "non-identically-unit-K",
                "active-admitted-history-composite-nondegeneracy",
                "K-derived-generator-bounded-field",
                "unique-realised-successor",
                "identity-preservation",
                "unit-retention",
                "focal-history-terminal-state-binding",
                "exact-prefix-history-extension",
                "nonnegative-edge-holding-contributions",
                "neutral-zero-edge-holding-base",
                "exact-prefix-holding-accumulation",
            ],
            "full_A1_A61_conformance_claimed": False,
            "empirical_human_model_claimed": False,
        },
        "source_identity": {
            "title": "Navigational Cybernetics 2.5 v2.1 — Axiomatic Core",
            "doi": "10.17605/OSF.IO/NHTC5",
        },
        "nc25_factor": {
            "domain": "S^1 x [0,C]",
            "C": _q(nc.capacity),
            "b0": _q(nc.initial_burden),
            "tau0": _q(nc.capacity - nc.initial_burden),
            "tau_min": _q(nc.floor),
            "pressure_at_b0": _q(
                nc.pressure * (1 - nc.initial_burden / nc.capacity)
            ),
            "spin_rate": _q(nc.spin_rate),
            "safe_fallback": "u0",
            "safe_fallback_gate_value": int(
                gate_value(nc, "u0", nc.initial_state)
            ),
            "focal_action": event.nc_action,
            "focal_action_gate_value": int(
                gate_value(nc, event.nc_action, event.pre.nc)
            ),
            "gate_precedes_event": _gate_prior(witness),
            "runtime_is_declared_gate_writer": nc.runtime_actor in nc.gate_writers,
            "boundary_provenance_recomputed": False,
        },
        "crown_factor": {
            "states": list(crown.states),
            "initial_state": crown.initial_state,
            "admitted_edges": [list(edge) for edge in crown.admitted_edges],
            "active_admitted_histories": [
                list(history.states)
                for history in active_admitted_histories(crown)
            ],
            "active_admitted_terminal_states": sorted(
                active_admitted_terminal_states(crown)
            ),
            "pre_field": sorted(pre_field),
            "post_field": sorted(post_field),
            "lost": sorted(pre_field - post_field),
            "gained": sorted(post_field - pre_field),
            "realised_successor": crown.next_states[0]
            if len(crown.next_states) == 1
            else list(crown.next_states),
            "identity_preserved": crown.identity_preserved,
            "unit_retained": crown.pre_unit == crown.post_unit,
            "history_before": list(crown.pre_history),
            "history_after": list(crown.post_history),
            "history_before_terminal": crown.pre_history[-1],
            "history_after_terminal": crown.post_history[-1],
            "history_terminals_aligned": _history_terminals_aligned(witness),
            "field_definition": (
                "F_W(x)=Cand_W^[R_W](x)\\cap{x'|K_{ell,W}(x,x')=1}"
                "=Succ_adm^[R_W,c](x)"
            ),
            "holding_contributions": [
                {"edge": list(edge), "value": _q(value)}
                for edge, value in crown.hold_contributions
            ],
            "holding_records": [
                {"history": list(history), "value": _q(value)}
                for history, value in crown.hold_records
            ],
        },
        "product_event": {
            "occurrence_id": event.occurrence_id,
            "product_pre": {
                "nc": _nc_state_json(event.pre.nc),
                "crown": event.pre.crown,
            },
            "product_post": {
                "nc": _nc_state_json(event.post.nc),
                "crown": event.post.crown,
            },
            "nc_projection": {
                "pre": _nc_state_json(project_nc_event(event).pre),
                "action": project_nc_event(event).action,
                "post": _nc_state_json(project_nc_event(event).post),
            },
            "crown_projection": list(project_crown_event(event)),
            "projections_commute": _product_event_commutes(witness),
        },
        "primitive_inventory": [
            "burden",
            "remaining budget",
            "admissibility gate",
            "finite candidate generator",
            "continuation relation",
            "addressed identity",
            "history",
            "product event",
            "realised successor",
            "holding contribution",
            "cumulative holding record",
        ],
        "checks": [
            {"marker": marker, "pass": check(witness)}
            for marker, check in CHECKS
        ],
    }


def main() -> int:
    result = certificate(default_witness())
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
