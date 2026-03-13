---
title: "ONTOΣ VII: From Formal Verification to Admissibility Architecture"
date: "2026-02-17"
description: "Admissibility as the Next Layer of Formal Methods."
author: "Max Barzenkov"
tags: ["NC2.5", "PETRONUS", "cybernetics", "admissibility"]
cover: "/blog/covers/onto-vii-from-formal-verification-to-admissibility-architecture-cover.jpg"
doi: ""
license: "CC BY-NC-ND 4.0"
medium: "https://medium.com/@MxBv/onto%CF%82-vii-from-formal-verification-to-admissibility-architecture-993ae89f2f36"
---

### Admissibility as the Next Layer of Formal Methods.

Maksim Barziankou (MxBv)

![](https://petronus.eu/blog/images/onto-vii-from-formal-verification-to-admissibility-architecture-01.jpg)

### Formal Methods Through the Lens of Navigational Cybernetics 2.5

### I. The Problem Formal Methods Do Not Know They Have

Formal methods were built to answer a clean question: does this system satisfy this property? The tools are mature. TLA+ specifies transitions and checks invariants. Alloy searches for structural counterexamples. Coq and Isabelle prove theorems mechanically. Dafny enforces contracts at the boundary of code.

These tools assume that the specification is the hard part and that enforcement is settled once the specification is written. For short-horizon systems, this assumption holds. A protocol either satisfies its safety invariant or it does not. A compiler either preserves semantics or it does not.

But for long-horizon adaptive systems — systems that interact with open environments over irreversible timescales — a different failure mode appears. It is not that specifications go unverified. It is that specifications, once made operational, begin to function as optimization targets.

This is the architectural problem that Navigational Cybernetics 2.5 identifies as the collapse of admissibility into optimization: the moment a boundary condition becomes causally actionable, the system learns to exploit it rather than respect it. Formal methods, as currently practiced, have no defense against this failure. They verify *that* a property holds, but they do not address *what happens to the property when it enters the causal loop of a learning, adapting, or self-modifying system.*

This article argues that formal methods need an architectural theory of admissibility — and that admissibility needs formal methods as the only mechanism capable of holding the line between constraint and objective.

### II. What Admissibility Is (And What It Is Not)

In Navigational Cybernetics 2.5, admissibility is defined as a non-causal structural predicate that constrains which continuations are permitted, without ranking them, scoring them, or providing gradient signal.

This is not a constraint in the Lagrangian sense. It is not a penalty term. It is not a soft boundary that trades off against reward. It is a categorical exclusion: certain classes of transition are forbidden, and the system receives no information about *how forbidden* they are or *how close* it is to the boundary.

The distinction matters because every other formal object degrades under optimization pressure:

A penalty becomes a price. If violating a constraint costs 0.3 units of reward, the system will violate it whenever the gain exceeds 0.3. The constraint is now a variable in a trade-off.

A metric becomes a target. Goodhart’s Law is not a curiosity; it is a structural inevitability. Any measurable proxy for viability will be optimized against, and the optimization will diverge from the original intent exactly where it matters most — at the long horizon.

A soft constraint becomes a negotiation surface. Constraint relaxation, slack variables, and epsilon-tolerance all convert a boundary into a geometry. Once the geometry is known, it can be navigated instrumentally.

Admissibility, as defined in this framework, resists all three failure modes by refusing to participate in the causal dynamics of the system. It does not score. It does not rank. It does not inform the agent about its distance from the boundary. It only excludes.

### III. Why This Matters for Formal Verification

In formal methods, the closest existing construct to admissibility is the *safety invariant*: a predicate over states that must hold at every reachable point in the execution.

Safety invariants have a critical structural property: they are binary. A state either satisfies the invariant or it does not. There is no gradient, no partial satisfaction, no “degree of compliance”. The model checker either finds a counterexample or it does not. The proof assistant either verifies the invariant or the proof fails.

This binary character is exactly what admissibility requires. A safety invariant, properly formulated, does not degrade into an optimization signal because it provides no signal at all — only a gate.

But here is the gap that current practice does not close: *safety invariants are verified at specification time, not at adaptation time.* The invariant is checked once, against a fixed model. If the system subsequently adapts, learns, or self-modifies, the verified model no longer corresponds to the running system. The invariant was proven about an abstraction that has drifted away from the reality.

For short-horizon systems, this gap is manageable. The system does not change. The proof holds.

For long-horizon adaptive systems, this gap is fatal. The system accumulates structural drift. Its internal organization shifts under sustained interaction. The invariant that was verified against the initial model now constrains a system that no longer matches that model.

This is not a bug in formal methods. It is a missing architectural layer.

### IV. The Three Layers

Navigational Cybernetics 2.5 provides the architectural theory. Formal methods provide the enforcement mechanism. Neither is sufficient alone. Together, they suggest a three-layer structure for long-horizon admissibility:

**Layer 1: Verified Safety Invariants (Static Admissibility)**

This is what formal methods already do well. State predicates, transition guards, and temporal safety formulas are specified and verified — by TLC, by SPIN, by nuXmv, by Coq — before the system operates.

In TLA+ notation, this is the canonical form:

> Init ⇒ Admissible*, and *Admissible ∧ Next ⇒ Admissible’

Every reachable state satisfies the admissibility predicate. Every permitted transition preserves it. This layer is the skeleton: it defines the space within which continuation is structurally permitted.

**Layer 2: Runtime Enforcement (Dynamic Admissibility)**

Because long-horizon systems drift, static verification alone is insufficient. A runtime layer intercepts actions and checks them against admissibility predicates before execution.

This is not reinforcement learning with a safety wrapper. The runtime monitor does not score actions, does not provide reward signal, and does not inform the agent about which admissible actions are “better”. It only blocks. The agent sees a reduced action space; it does not see the shape of the reduction.

Runtime verification, as described in the monitoring literature, provides the operational mechanism. The architectural requirement — that the monitor must not leak information about the boundary geometry — comes from Navigational Cybernetics 2.5 and specifically from its non-reconstructibility bounds (NR-ε).

**Layer 3: Structural Budget Enforcement (Temporal Admissibility)**

This is the layer that has no precedent in standard formal methods.

In Navigational Cybernetics 2.5, internal time is defined as a bounded budget: τ = C − Φ, where Φ is the accumulated irreversible structural burden. As the system operates, Φ increases monotonically. The admissible continuation space must contract.

This means that admissibility is not a fixed predicate. It tightens over the system’s lifetime. What was admissible at time t₀ may not be admissible at time t₁, not because the rules changed, but because the budget shrank.

Formal methods do not currently model this. An invariant is either true forever or it is violated. There is no standard construct for “this invariant holds, but the set of states satisfying it contracts monotonically under an irreversible load functional”.

Formalizing this would require a Lyapunov-like structure within the specification language: a nonnegative, monotonically depleted quantity that governs which predicates remain active. TLA+ can express this (internal time as an explicit state variable with monotone constraints), but current practice does not treat it as an architectural pattern. It should.

### V. What Formal Methods Gain

If formal methods incorporate the admissibility architecture of Navigational Cybernetics 2.5, three things become possible that are not possible today:

> **Verified non-degradation of constraints.** Currently, formal methods verify that a constraint holds. With an admissibility architecture, they can verify that a constraint *cannot be converted into an optimization signal *— that the system has no causal pathway from the boundary predicate to the action selection mechanism. This is a second-order property: not “does the invariant hold?” but “is the invariant structurally isolated from the optimization loop?”.

**Bounded revision.** Meta-level changes to the constraint set (policy updates, rule revisions, boundary adjustments) can be formalized as Lyapunov-bounded: each revision incurs irreversible structural cost, and the total number of revisions is bounded by the budget. This prevents the “specification churn” problem, where rules are continuously relaxed under operational pressure until nothing remains.

**Falsification criteria.** Navigational Cybernetics 2.5 provides explicit tests: if the system can distinguish between two admissibility boundaries through its observable transcript, the non-reconstructibility bound is violated and the architecture has failed. These tests can be formalized as properties in a model checker: “there exists no execution trace of length T in which the agent’s identification success exceeds the bound derived from KL divergence and Fano’s inequality”.

### VI. What Admissibility Gains

If Navigational Cybernetics 2.5 adopts formal methods as its enforcement layer, two risks are mitigated:

**The rhetoric-to-mechanism gap.** The most dangerous failure mode for an admissibility-first architecture is that “non-causal constraint” remains a philosophical position rather than an engineered structure. Formal methods close this gap. A safety invariant verified by TLC or proven in Coq is not a recommendation. It is a mechanically checked fact. Either the system preserves admissibility at every step, or the verifier produces a counterexample showing exactly how it fails.

**Refinement across layers.** Real architectures are layered. An abstract admissibility specification at Level 0 must be correctly implemented by Level 1, which must be correctly compiled to Level 2. Each layer can introduce violations invisible from above. Formal refinement — the technique of proving that a concrete specification implements an abstract one — is exactly the mechanism needed to ensure that admissibility survives the descent from theory to implementation. The seL4 microkernel verification and the Verdi distributed systems framework demonstrate that this is practical, not theoretical.

### VII. The Line That Must Not Move

At the core of this architecture lies a single requirement:

> **Admissibility-relevant structure must be fully visible to verification, yet categorically unavailable for instrumental use by the system being constrained.**

The verifier — whether a model checker, runtime monitor, or proof assistant — may inspect, check, and enforce the boundary.
The adaptive system may not use that boundary as a signal, a metric, or an optimization guide.

This is where formal methods become essential.

Among standard formal constructs, safety invariants possess a structural property that makes them especially resistant to degradation into optimization signals: they are binary. A state either satisfies the invariant or it does not. There is no gradient, no partial compliance, no measurable distance to the boundary.

Because of this binary character, invariants do not provide an instrumental interface to the constraint. They can be verified, but they cannot be optimized against as objectives.

This structural feature makes safety invariants a natural formal template for implementing admissibility within Navigational Cybernetics 2.5.

The theory of admissibility specifies **what must be held**. Formal verification specifies **how it is held**.

Neither is sufficient alone. Together, they define the minimal formal skeleton for systems that aim to survive across long horizons while preserving structural integrity.

Full research corpus: [https://github.com/petronushowcore-mx/NAVIGATIONAL-CYBERNETICS-2.5-MxBv-](https://github.com/petronushowcore-mx/NAVIGATIONAL-CYBERNETICS-2.5-MxBv-)
