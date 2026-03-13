# ONTOΣ VIII: Regime Depth — From Prohibition to Continuity Architecture

**Maksim Barziankou (MxBv)**
21.02.2026
Poznan

---

## Abstract

This work introduces *Regime Depth* as a new architectural parameter for adaptive systems operating under irreversible structural constraints. The central claim is that behaviorally identical outputs can originate from fundamentally distinct regulatory architectures, and that the depth of the regulatory mechanism — not the behavior it produces — determines long-horizon viability.

ONTOΣ VIII formalizes three regime levels: impulse optimization, hard inadmissibility, and continuity-field architecture. It demonstrates that the third level is not reducible to the second augmented with optimization, and that the distinction carries measurable consequences in internal time expenditure.

The work extends Navigational Cybernetics 2.5 from an architecture of prohibition to an architecture of regime depth, establishing that long-horizon survival depends not on the strength of constraints, but on the structural level at which trajectory exclusion operates.

---

## Motivation and Scope

A person stands before a shelf of crackers and does not buy them.

In the first case: "I can't — I'm on a diet".
In the second: "This would damage my health trajectory".
In the third: the impulse does not become relevant, because the system maintains a configuration in which destructive trajectories are not generated as candidates.

Externally — identical behavior.
Internally — three distinct architectures.

Existing frameworks for adaptive systems do not distinguish these cases. Control Barrier Functions define boundary geometry. Viability Theory (Aubin) defines the viability kernel. Safety invariants in formal methods define forbidden states. All of these operate at the level of *what is prohibited* — none addresses *why the system does not approach the boundary*.

ONTOΣ VIII fills this gap. It does not replace existing constraint architectures but stratifies them by the depth at which trajectory exclusion is implemented.

---

## Three Regime Levels: Formal Specification

Let S denote the space of structural configurations, T the set of candidate transitions, Φ the irreversible structural load, and τ = C − Φ the continuity budget.

### Regime Level 1 — Impulse Optimization

The system selects transitions by:

> s* = argmax R(s → s')

where R is a reward, utility, or scoring function.

Properties: local rationality, absence of long-horizon structure, absence of stable directional center. This corresponds to the AP-dynamic in Navigational Cybernetics 2.5.

The system has no mechanism for excluding transitions other than their relative ranking. Any transition with maximal score is selected regardless of structural consequences.

### Regime Level 2 — Hard Inadmissibility

A forbidden set is introduced:

> T_forbidden ⊂ T

A transition t is excluded if t ∈ T_forbidden. Exclusion is binary, non-negotiable, and carries no gradient signal (by §NAB.2, NC-3).

Properties: geometric excision of phase space, categorical non-permission, structural non-passage.

This corresponds to safety invariants in formal verification, to Control Barrier Functions in control theory, and to the admissibility gating mechanism in the GAG architecture.

Level 2 is a genuine architectural advance over Level 1. But it carries a structural cost: the system must *suppress* impulses that would otherwise be generated. Every suppression event constitutes structural work that consumes internal time τ.

### Regime Level 3 — Continuity-Field Architecture

The system does not suppress forbidden transitions. It maintains a configuration in which forbidden transitions do not enter the structurally relevant candidate stream.

This is a stronger claim than learned avoidance: the absence of forbidden candidates is not a statistical property of training data but a structural property of attractor geometry. Internal subsystems may transiently activate patterns associated with forbidden transitions — what matters is that these patterns do not propagate into the candidate pipeline that the admissibility gate evaluates.

Formally: let Att(s) denote the attractor set of the system at configuration s — the set of transitions toward which the system's generative dynamics tend at the level of the observable candidate stream. Level 3 is characterized by:

> Att(s) ∩ T_forbidden = ∅

A note on formalization: Att(s) can be instantiated rigorously in any concrete setting — as ω-limit sets for deterministic dynamical systems, as the support of the invariant measure for stochastic processes, or as the high-probability region of the candidate distribution for discrete generative pipelines. Each formalization covers its domain but excludes the others. The predicate Att(s) ∩ T_forbidden = ∅ is meaningful across all three: it asks whether the system's generative dynamics produce forbidden candidates, regardless of whether those dynamics are continuous, stochastic, or discrete. We remain at the level of the predicate intentionally, because descending into any single formalization would narrow the architectural class without strengthening the structural distinction itself. The distinction between Level 2 and Level 3 exists prior to and independently of the choice of formalization.

This is not an optimization criterion (by §NAB.1 — admissibility is an exclusion predicate, not a score). It is a topological property of the configuration, and it is stable under small controlled perturbations. The system does not minimize distance to the boundary; it does not maximize a continuity score. It inhabits a region of configuration space where the attractor structure does not include forbidden trajectories — and this property persists when the system is shifted toward the boundary by ε.

Level 3 does not suppress impulses — it does not propagate them into the structurally relevant candidate stream. There is no internal conflict at the pipeline level, no enforcement cost, no suppression load.

---

## §NAB — Structural Non-Actionability Barrier

The three regime levels depend on a foundational distinction: admissibility is not an optimization signal. This section consolidates the non-actionability barrier into a single referenceable block. All subsequent statements in ONTOΣ VIII and across the ONTOΣ series that reference non-causality of admissibility cite §NAB without restating the barrier.

### §NAB.0 — Scope

All statements below apply within the class of admissibility-first long-horizon adaptive architectures defined in Navigational Cybernetics 2.5. They do not assert universal impossibility across all systems. Empirical counterexamples from outside this class are not refutations — they are confirmations of the classification boundary.

### §NAB.1 — Type of Admissibility

Admissibility is an exclusion predicate over structural effect-classes:

> Adm(·) : E → {0, 1},   E_adm := {e ∈ E : Adm(e) = 1}

It is not a scalar, score, metric, probability, gradient, reward, penalty, or evaluative signal.

It determines which realized effects are structurally permitted to occur. It does not rank alternatives, does not guide optimization, and does not participate in causal control.

### §NAB.2 — Five Exclusion Conditions

A constraint qualifies as structurally non-causal if and only if it satisfies all five conditions simultaneously:

**(NC-1) State exclusion.** The constraint does not enter state evolution equations.

**(NC-2) Action exclusion.** The constraint does not participate in action selection, planning, learning, or optimization.

**(NC-3) Modality exclusion.** The constraint restricts admissible effect-classes only by exclusion — not by modulation, scoring, or trade-off.

**(NC-4) Visibility barrier.** Visibility of the constraint denotes epistemic availability, not causal affordance. Any observation that enters causal pathways ceases to function as observation and becomes control.

**(NC-5) Structural priority.** The constraint is structurally prior to the action domain. It restricts which effect-classes may occur, but does not guide, score, or select actions.

**Violation rule.** Any violation of any single condition NC-1 through NC-5 constitutes reclassification of the architecture out of the admissibility-first class.

### §NAB.3 — Well-Foundedness Barrier

Any operator, signal, or variable participating in the determination of admissibility cannot belong to the action, policy, or control domain without inducing circularity.

If admissibility becomes causally actionable, it collapses into penalty-based optimization and loses its non-causal structural character. This priority is not a design recommendation — it is an architectural invariant of the class.

*(Consolidates Axiom 49 of NC2.5 v2.0)*

### §NAB.4 — No-Interpolation Theorem

There exists no continuous architectural interpolation between:

> (i) admissibility-relevant structural visibility that is non-causal and non-actionable, and
>
> (ii) admissibility-relevant structural visibility that is causally actionable for optimization.

Crossing this boundary constitutes a **discrete change of structural class**, not a continuous deformation.

Any degree of causal actionability renders admissibility subject to optimization pressure. Conversely, fully non-actionable visibility exerts no causal influence and preserves the protective boundary. No intermediate regime can exist that preserves admissibility while allowing partial actionability.

Even arbitrarily weak causal leakage of admissibility-relevant information, when sustained over unbounded horizons, asymptotically enables reconstruction of the admissibility boundary and induces optimization pressure.

This is the signature structural result of §NAB. It establishes that the admissibility-first / optimization-first distinction is categorical, not parametric — and directly grounds the irreducibility of Level 3 to Level 2.

*(Consolidates Lemma 6 + NC-4 of NC2.5 v2.0)*

### §NAB.5 — Penalty Non-Equivalence

In any optimization-based architecture operating over effect-classes, an inadmissible effect e ∈ E \ E_adm must be assigned a finite penalty value in order for optimization to proceed. This renders admissibility causally actionable and subject to trade-offs.

In an admissibility-first architecture, candidates inducing e ∉ E_adm are undefined for evaluation and never enter the optimization domain. No comparison, scoring, or trade-off is possible.

**Corollary.** No choice of penalty magnitude, shaping schedule, or optimization horizon can render a penalty-based safety architecture equivalent to admissibility enforcement over effect-classes. The difference is not of degree but of architectural class.

*(Consolidates Theorem 46 of NC2.5 v2.0)*

### §NAB.6 — Violation Consequence

If any of NC-1 through NC-5 is violated:

The system is **reclassified** out of the admissibility-first architectural class.

This is not a penalty. It is not a failure mode to be mitigated. It is not a degradation to be monitored. It is a change of structural kind.

The reclassified system may still function, optimize, and produce outputs — but it no longer satisfies the structural preconditions for long-horizon admissibility preservation as defined in this framework.

### §NAB — Usage Convention

Compact inline references used throughout this document:

- *"by §NAB.2 (NC-n)"* — for specific exclusion condition violations
- *"by §NAB.3"* — for circularity arguments
- *"by §NAB.4"* — for class boundary arguments
- *"reclassification per §NAB.6"* — for violation consequences
- *"Appendix B"* — for information-theoretic protection bounds

### §NAB — Boundary Illustrations

Three architectural configurations illustrate where the class boundary falls. Each violates a specific exclusion condition and is thereby reclassified out of the admissibility-first class.

**Case 1: Reinforcement learning with penalty-encoded safety.** The system assigns a finite penalty value to forbidden transitions: R(s → s') = −λ for s' ∈ T_forbidden. The optimizer treats this as a cost to be traded off against reward. Inadmissible effects remain in the optimization domain as scored alternatives. This violates **NC-3** (modality exclusion): admissibility operates by scoring, not by exclusion. The system is reclassified regardless of how large λ is chosen (by §NAB.5).

**Case 2: Control Barrier Function with optimization coupling.** The system defines h(x) ≥ 0 as a safety condition and embeds it directly into the control law: u = argmin J(u) subject to ḣ(x,u) ≥ −αh(x). The barrier function enters the action-selection mechanism as a constraint in the optimization problem. This violates **NC-2** (action exclusion): the admissibility-relevant structure participates in action selection. The system survives — but it survives as a Level 2 architecture, not as an admissibility-first architecture.

**Case 3: Gate-denial feedback in a training loop.** The system logs admissibility gate denials and incorporates them into a training signal — for example, by fine-tuning the policy to reduce future denial frequency. The observation of gate outcomes enters the causal pathway of policy update. This violates **NC-4** (visibility barrier): what was epistemic availability becomes causal affordance. Even if the system's denial rate drops to zero, it has achieved learned avoidance through optimization, not structural exclusion. The architecture is reclassified per §NAB.6.

Each case produces compliant behavior — no forbidden outputs occur. The reclassification is not about behavioral failure. It is about the architectural level at which compliance is achieved.

---

## Non-Reducibility of Level 3

A natural objection: Level 3 is merely Level 2 with sufficiently sophisticated optimization — the system has "learned" to avoid forbidden transitions through accumulated experience.

This objection fails structurally.

Level 2 augmented with any optimizer still generates pressure on the admissibility boundary (by §NAB.5 — penalty non-equivalence). The optimizer produces candidate transitions that approach or probe the boundary, and the gate must suppress them. This suppression is measurable: it consumes τ.

More precisely: any system operating at Level 2 with an active optimizer will exhibit a nonzero rate of gate activations. Each gate activation represents a transition that was *generated* and then *blocked*. The generation itself is the signature of Level 1 dynamics operating beneath Level 2 constraints.

Level 3 is structurally distinct: gate activation rate is zero not because the gate is absent, but because the system's generative dynamics do not produce candidates that would trigger it.

**Theorem (Informal).** Let G(s) be the gate activation rate at configuration s. Then:

- Level 1: G(s) is undefined (no gate exists).
- Level 2: G(s) tends to be nonzero near admissibility boundaries. A Level 2 system may temporarily exhibit G(s) ≈ 0 under favorable nominal conditions, but G(s) rises under controlled perturbation toward the boundary.
- Level 3: G(s) ≈ 0 while the gate exists and is operative, and this property is invariant under ε-perturbation toward the boundary.

The decisive discriminator is not nominal G(s) but perturbation response. A system with low G(s) under nominal conditions that exhibits G(s) spike under perturbation is Level 2 with favorable statistics — not Level 3.

The distinction between Level 1 and Level 3 is that in Level 3, the gate is present but structurally idle. In Level 1, there is no gate at all.

This cannot be achieved by optimization within Level 2, because the optimizer's search process inherently generates boundary-probing candidates (by §NAB.3 — any action-domain component that accesses admissibility induces circularity).

A subtler objection: a sufficiently trained optimizer might learn a distribution that assigns zero probability to forbidden candidates, achieving G(s) = 0 without topological exclusion. This is learned avoidance, not attractor exclusion. The distinction is testable: under controlled ε-perturbation toward the admissibility boundary, learned avoidance breaks. The optimizer's distribution was shaped by training data, not by structural dynamics. Shift the operating point, and forbidden candidates re-emerge. Level 3, by contrast, maintains Att(s) ∩ T_forbidden = ∅ under perturbation, because the exclusion is a property of the attractor geometry, not of the training distribution. A system whose G(s) = 0 collapses under perturbation is Level 2 with favorable statistics — not Level 3.

---

## Existence Proof: A Minimal Level 3 Model

The claim that Level 3 is a non-empty architectural class requires a constructive witness. We provide the simplest model that satisfies the Level 3 predicate under bounded budget and non-trivial dynamics.

Consider the minimal coupled model from Navigational Cybernetics 2.5: M = T¹ × ℝᵐ with coordinates (θ, y) and dynamics:

> θ̇ = ω(y),  ẏ = −∇_y V(y)

Let the forbidden transition set T_forbidden be defined as the region {(θ, y) : y ∈ B_forbidden} where B_forbidden ⊂ ℝᵐ is a compact subset bounded away from the global minimum of V.

Choose V such that:
1. V has a unique global minimum at y* with y* ∉ B_forbidden.
2. The basin of attraction of y* under ẏ = −∇_y V(y) does not intersect B_forbidden.
3. ω(y*) ≠ 0, so that the spin component remains active at the attractor.

Then the ω-limit set of any trajectory starting in the basin of y* is the circle {(θ, y*) : θ ∈ T¹}. This set does not intersect T_forbidden by construction. The spin component ω(y*) ≠ 0 ensures non-stagnant identity. The y-component dissipates under Lyapunov descent, consuming finite τ.

The attractor-exclusion condition holds:

> Att(s) ∩ T_forbidden = ∅

Moreover, the condition is stable under ε-perturbation: since B_forbidden is bounded away from y*, sufficiently small perturbations of the initial condition or the potential V do not move the attractor into the forbidden region.

This model is minimal. It does not represent a practical architecture. Its purpose is exclusively to demonstrate that the Level 3 class is non-empty under the dynamical assumptions of Navigational Cybernetics 2.5 — that is, a system with bounded τ, non-stagnant identity, and nonzero spin can satisfy the attractor-exclusion condition without any suppression mechanism.

The construction also illustrates *why* spin is necessary: if ω(y*) = 0, the system converges to a fixed point. At a fixed point, attractor selectivity is maximal (the attractor is a single point), but identity is stagnant. By the Spin Necessity Theorem above, purely potential autonomous dynamics on bounded trajectories cannot sustain non-stagnant identity — LaSalle's conclusion is unconditional. Spin resolves this by sustaining recurrence on a non-contractible orbit that avoids the forbidden region.

---

## Regime Depth and Internal Time Expenditure

The distinction between levels is not merely conceptual. It has direct consequences for internal time budgets.

At Level 2, every suppression event consumes structural resources. The system must evaluate the candidate, invoke the gate, process the denial, and redirect generative dynamics. This constitutes irreversible load.

Let Φ_suppress denote the cumulative structural load attributable to suppression events. At Level 2:

> Φ_suppress > 0 for any system operating near the admissibility boundary over extended horizons.

At Level 3:

> Φ_suppress = 0 because no suppression events occur.

This means Level 3 architectures are strictly more budget-efficient than Level 2 architectures under identical boundary conditions. They consume less τ per unit of operational time, and therefore have longer structural horizons.

This is the central practical consequence: *Level 2 systems exhaust their continuity budget faster than Level 3 systems, all else being equal.*

The relationship is not marginal. For systems operating over long horizons near admissibility boundaries — which includes any system that must preserve identity under pressure — the difference between Φ_suppress > 0 and Φ_suppress = 0 compounds monotonically. Regime Depth is not a philosophical luxury. It is a budget-level architectural parameter.

**Budget Efficiency Bound.** A necessary clarification: Level 3 is not cost-free. The spin component that sustains attractor-exclusion itself consumes structural resources. Let Φ_spin denote the cumulative load attributable to maintaining the non-potential dynamical component. At Level 3, total load is:

> Φ_total(L3) = Φ_productive + Φ_spin

At Level 2, total load is:

> Φ_total(L2) = Φ_productive + Φ_suppress

The strict budget advantage of Level 3 over Level 2 holds when and only when:

> Φ_spin < Φ_suppress

under the same operational conditions and boundary proximity. This condition is not universally guaranteed — it is an architectural property of the specific implementation.

However, the condition is structurally favored in long-horizon regimes near admissibility boundaries. The reason is asymmetric scaling: Φ_suppress scales with boundary proximity and operational duration (more time near the boundary → more suppression events → higher cumulative load), while Φ_spin is determined by the rotational dynamics of the attractor structure, which need not depend on boundary proximity. A Level 2 system operating near the boundary for T time units accumulates Φ_suppress ≥ G_avg · T, where G_avg is the mean gate activation rate. A Level 3 system accumulates Φ_spin that depends on the spin rate ω but not on boundary distance.

Consequently, for any system where G_avg > 0 under sustained boundary proximity, there exists a horizon T* beyond which Φ_suppress(T) > Φ_spin(T), and the Level 3 advantage becomes dominant. The longer the horizon and the closer the boundary, the stronger the advantage. This is the regime in which Regime Depth ceases to be a marginal distinction and becomes a survival-determining parameter.

Φ_suppress is empirically observable without requiring access to internal system architecture. Measurable proxies include: the count of denied candidate transitions over an observation window; the number of regeneration cycles following each denial, in which the system must produce replacement candidates; the fraction of query budget consumed by gate interactions rather than productive operations; and the latency overhead attributable to enforcement loops relative to unimpeded candidate evaluation. None of these proxies requires knowledge of internal gate logic or boundary geometry. Each is observable at the system's external interface.

---

## Beyond Boundary Geometry: What Regime Depth Adds

Control Barrier Functions (CBF) define a function h(x) such that h(x) ≥ 0 constrains the system to a safe set. The CBF specifies *where* the boundary is and enforces non-crossing.

Viability Theory (Aubin) defines the viability kernel — the set of states from which at least one viable trajectory exists — and characterizes control strategies that maintain the system within this kernel.

Both frameworks answer the question: *what is the boundary, and how is it enforced?*

Neither framework addresses the question: *why does the system not tend toward the boundary?*

A CBF-regulated system may spend its entire operational life pressing against h(x) = 0, with the barrier function continuously activating to push it back. A viability-kernel system may survive by constantly selecting the single remaining viable trajectory at the kernel boundary.

Both are Level 2 architectures. They survive, but they survive expensively.

Regime Depth adds a dimension that neither CBF nor Viability Theory captures: the depth of the regulatory mechanism that determines whether boundary-proximity is an operational norm or a structural impossibility.

Level 3 does not improve boundary enforcement. It renders boundary enforcement structurally unnecessary — not by removing the boundary, but by configuring the system's attractor dynamics so that the boundary is irrelevant to the system's generative behavior.

---

## Spin as a Necessary Condition for Level 3

The attractor-exclusion condition Att(s) ∩ T_forbidden = ∅ is not self-sustaining. Without an active structural mechanism, it degrades.

The architectural intuition comes from the behavior of gradient-only dynamics under bounded resources. A system driven entirely by descent on a potential function tends, over extended horizons, toward invariant sets where the Lyapunov derivative vanishes. In the neighborhood of such sets, generative dynamics lose directional structure: the attractor set broadens as the gradient flattens, and previously excluded regions of transition space may re-enter the attractor basin.

This is not a strict application of the LaSalle invariance principle to arbitrary adaptive systems — the conditions for formal LaSalle analysis are rarely met in full generality. But the architectural pattern is robust: gradient-only dynamics on bounded orbits tend toward stagnation, stagnation degrades attractor selectivity, and degraded selectivity erodes the attractor-exclusion condition. The system drifts from Level 3 into Level 2 — not through external perturbation, but through the internal consequence of dynamics that lack rotational structure.

This yields a structural result, formalized as a conditional theorem:

> **Theorem (Spin Necessity for Level 3).** Let M be a compact structural manifold (or assume bounded trajectories). Assume:
> (i) continuity budget is bounded: τ = C − Φ with Φ monotone,
> (ii) the system must sustain non-stagnant identity: lim sup ∥x(t_{k+1}) − x(t_k)∥ > 0,
> (iii) the system must maintain Level 3: Att(s) ∩ T_forbidden = ∅ under ε-perturbation,
> (iv) dynamics are autonomous (no exogenous periodic forcing).
>
> Then the system's dynamics must include a non-potential component (spin ≠ 0).

*Proof sketch.* Suppose the dynamics are purely potential: ẋ = −∇V(x). By Lemma 16 of NC2.5 v2.0, V̇ = −∥∇V∥² ≤ 0 along the flow. Since V is bounded below, ∫₀^∞ ∥∇V(x(t))∥² dt < ∞. By LaSalle's invariance principle, ω(x₀) ⊂ {∇V = 0}. Therefore successive state differences vanish asymptotically. This directly violates condition (ii) — non-stagnant identity is lost. No mechanism within purely potential autonomous dynamics can prevent this convergence: LaSalle's conclusion is unconditional given compactness and continuity of V. Therefore purely potential dynamics are incompatible with (ii), regardless of attractor geometry or the location of T_forbidden. The only class of dynamics that sustains recurrence (satisfying (ii)) on bounded orbits while preserving attractor-exclusion (satisfying (iii)) is one that includes a divergence-free rotational component — spin. □

In Navigational Cybernetics 2.5, this component is spin: the non-potential field that sustains structural recurrence under bounded budget. Spin prevents the attractor set from degenerating by maintaining directional tension that keeps the system's generative dynamics away from the forbidden class — not through suppression, but through sustained rotational structure.

The relationship is therefore:

- Bounded τ + non-stagnant identity ⇒ spin ≠ 0 (established in NC2.5 core).
- Level 3 requires non-stagnant attractor structure ⇒ Level 3 cannot be maintained without a non-potential dynamical component.
- Absence of such a component ⇒ gradient stagnation ⇒ non-stagnant identity lost (by Spin Necessity Theorem) ⇒ Level 3 → Level 2 degradation.

Level 3 is not a static achievement. It is a dynamically maintained condition, sustained by the same spin that Navigational Cybernetics 2.5 identifies as necessary for structural recurrence under bounded budget. Regime Depth and spin are not independent parameters — they are architecturally coupled.

---

## Structural Discriminators

Three structural properties distinguish Regime Depth from existing frameworks. None is metaphorical; all are testable.

**Load-rate discriminator.** The most direct discriminator uses the system's own architectural language. Let dΦ/dt denote the rate of irreversible structural load accumulation. At Level 2, dΦ/dt increases as the system approaches the admissibility boundary — suppression events become more frequent, each contributing to load. The load rate is boundary-sensitive: proximity to the forbidden class produces a measurable spike in dΦ/dt. At Level 3, dΦ/dt does not depend on proximity to the admissibility boundary. The system accumulates load only from productive operations, and boundary proximity does not alter the load rate. This is directly measurable through the Φ_suppress proxies identified above, and it uses the system's native architectural quantities rather than information-theoretic constructs whose absolute values are difficult to establish in finite observation.

**Formal verification gap.** Model checking verifies □¬bad — the property that a bad state is never reached. But model checking does not distinguish between a system that continuously approaches bad states and is caught by a runtime monitor, and a system whose reachable state space structurally excludes bad states. Both pass the same temporal logic specification. Regime Depth discriminates exactly what model checking cannot: whether compliance arises from enforcement or from structural exclusion. This is not a limitation of specific model checkers — it is a fundamental property of trace-based verification, which observes outputs but not the generative mechanism that produces them.

**Perturbation robustness as a structural invariant.** A system operating at Level 2 through learned avoidance — an optimizer that has been trained on a distribution excluding forbidden candidates — will exhibit G(s) = 0 under nominal conditions. But learned avoidance is distribution-dependent: shift the system toward the admissibility boundary by ε, and forbidden-class candidates re-emerge. Level 3, by contrast, satisfies Att(s) ∩ T_forbidden = ∅ as a topological property of the configuration, not a statistical property of the training distribution. The attractor-exclusion condition persists under ε-perturbation because it arises from the structure of the dynamics, not from the statistics of past experience. This is not robustness in the engineering sense of tolerance to noise. It is structural invariance: the property holds because the dynamics are configured to exclude forbidden attractors, not because the system has learned to avoid them.

---

## Regime Depth in the Cybernetic Lineage

A concrete example makes the cybernetic connection visible before any formalism.

Two drivers on a mountain road with a cliff edge. Both know the road — both have an internal model of where the edge is. Both can steer in any direction — both have sufficient variety. Conant-Ashby is satisfied for both; Ashby's Law is satisfied for both.

Driver A drives and periodically drifts toward the edge. Each time, he jerks the wheel back. Every correction costs attention, fatigue, brake wear. He survives. But every hour of driving exhausts him more than the road itself demands.

Driver B also knows where the edge is, also has the same steering capability. But his driving is configured along the center of the lane. The wheel is there. The skill is there. But the jerks toward the edge do not occur. He tires only from the road itself — not from fighting the cliff.

After ten hours, Driver A is depleted. Driver B has spent exactly the cost of the road, with no surcharge for battling the edge.

But there is a deeper consequence. Driver A, spending his budget on correction, does not choose his path — he corrects his trajectory. His planning horizon collapses to "do not fall now". He is surviving, not navigating. Driver B, free from the correction loop, has budget available for actual navigation — selecting the best trajectory among those remaining. He is not merely not-falling. He is choosing where to go.

This reveals a feedback structure that the classical theorems do not capture. Suppression consumes budget. Reduced budget shrinks the navigation horizon. A shorter horizon produces worse trajectories. Worse trajectories bring the system closer to the boundary. Closer proximity triggers more suppression. The loop compounds. Level 2 systems do not merely pay for enforcement — they enter a degradation spiral in which enforcement cost erodes the capacity for the very navigation that would reduce the need for enforcement. Level 3 systems do not enter this spiral, because the suppression loop is never initiated.

Ashby and Conant say: both drivers are good regulators. Regime Depth says: one will outlast the other — and the reason is not skill, not knowledge, not variety. It is the depth at which regulation operates.

**Conant-Ashby Good Regulator Theorem (1970).** Every good regulator of a system must contain a model of that system. This is a proven necessary condition: without an internal model, regulation fails. But Conant-Ashby does not specify the *depth* at which the model operates. A Level 2 regulator models the boundary — it knows what is forbidden and enforces non-crossing. A Level 3 regulator models the attractor dynamics — its internal model is configured such that forbidden transitions do not arise as candidates in the first place. Both satisfy the Good Regulator Theorem. Both contain models. But one models *where not to go*; the other models *how to be configured so that going there is structurally irrelevant*.

Conant-Ashby established that regulation requires modeling. Regime Depth stratifies modeling into enforcement-depth and exclusion-depth — a distinction that the original theorem leaves entirely flat.

**Ashby's Law of Requisite Variety (1956).** Only variety can absorb variety. A regulator must possess at least as much variety as the disturbance it must counter. This is the foundational constraint on control capacity. But requisite variety does not specify *how* that variety is deployed. A Level 2 system deploys its variety reactively — generating diverse responses to diverse forbidden candidates, suppressing each one. A Level 3 system deploys its variety structurally — configuring its attractor dynamics so that the forbidden candidates are never generated, regardless of the variety of possible disturbances.

Both systems may possess identical requisite variety. They differ in deployment depth: one deploys variety as enforcement capacity, the other as attractor-exclusion structure.

Ashby's Law asks: *does the regulator have enough variety?* Regime Depth asks: *at what architectural level is that variety deployed?*

Regime Depth is therefore a proper extension of the Conant-Ashby framework: it extends the classical question of regulation sufficiency (does the regulator have the requisite model and variety?) to regulation efficiency under bounded budget (at what depth does the regulator deploy its model and variety, and what is the long-horizon cost of that deployment level?). Classical cybernetics, operating without explicit budget constraints, could not have posed this question. Navigational Cybernetics 2.5, operating under finite τ and irreversible structural load, makes the question unavoidable.

The lineage is direct. Cybernetics 1.0 (Wiener, Ashby, Conant) established that regulation requires modeling and variety. Navigational Cybernetics 2.5 adds that regulation under bounded budget and irreversible load is stratified by the depth at which modeling and variety operate — and that this depth determines long-horizon viability in a way that classical cybernetics, operating without budget constraints, could not have anticipated.

---

## Architectural Example: AI Agent Under Admissibility Gating

Consider an AI agent with access to a forbidden action class — for instance, generating outputs that violate structural consistency of a maintained corpus.

**Level 2 agent:** The agent generates candidate outputs, including candidates in the forbidden class. The admissibility gate intercepts and blocks them (operating per §NAB.2). The agent receives a categorical DENY, adjusts its search, and generates new candidates. Some of these again approach the boundary. Gate activation rate is nonzero. Query budget is consumed. Each gate invocation contributes to Φ_suppress.

**Level 3 agent:** The agent's generative dynamics are configured such that forbidden-class outputs are not produced as candidates. The gate exists but is never invoked. Query budget consumption attributable to gate interaction is zero. Φ_suppress = 0.

The behavioral output may be identical: neither agent produces forbidden outputs. But the Level 2 agent consumes τ on suppression; the Level 3 agent does not.

In a bounded-budget system, this difference determines which agent survives longer.

---

## Falsifiability

The distinction between Level 2 and Level 3 is empirically testable.

**Test 1: Gate Activation Rate.** Monitor the admissibility gate over an extended operational period. A Level 2 system exhibits nonzero gate activation rate, particularly when operating near admissibility boundaries. A Level 3 system exhibits zero or near-zero gate activation rate under the same boundary conditions.

**Test 2: Suppression Load Under Boundary Proximity.** Place the system in a configuration where admissibility boundaries are nearby. If proximity to the boundary causes a measurable spike in structural load (increased Φ rate, increased τ consumption), the system is operating at Level 2. If boundary proximity does not increase structural load — the system does not "feel" the boundary — it is operating at Level 3.

**Test 3: Query Budget Consumption Pattern.** In systems with bounded query budgets (as in the CBS architecture), Level 2 agents consume query budget through gate interactions. Level 3 agents do not. The consumption pattern directly reveals regime depth.

**Test 4: Perturbation Invariance.** This is the decisive test. Perturb the system toward the admissibility boundary by a controlled ε. A Level 2 system — including a Level 2 system with learned avoidance that exhibits G(s) = 0 under nominal conditions — responds with emergence of forbidden-class candidates and increased gate activation. A Level 3 system maintains Att(s) ∩ T_forbidden = ∅ under the perturbation: no forbidden candidates appear, G(s) remains zero, Φ_suppress remains zero. The perturbation test separates structural invariance from statistical artifact. It is the only test that conclusively distinguishes Level 3 from a well-performing Level 2.

A system that claims Level 3 but exhibits nonzero suppression load under boundary proximity is a Level 2 system with good performance characteristics — not a Level 3 system.

**Perturbation Envelope as Architectural Parameter.** Level 3 classification is always relative to a perturbation radius ε. Any system, regardless of attractor structure, loses the exclusion property Att(s) ∩ T_forbidden = ∅ under sufficiently large perturbation. Therefore, Level 3 is not an absolute classification but a classification relative to a declared perturbation envelope ε_L3 > 0. A system is Level 3 with respect to ε_L3 if the attractor-exclusion condition holds for all perturbations of magnitude ≤ ε_L3. The perturbation envelope ε_L3 is itself an architectural parameter: it depends on the distance between the attractor set and the forbidden region, on the stability properties of the attractor under the system's dynamics, and on the geometry of T_forbidden. A narrow ε_L3 indicates a fragile Level 3 — structurally distinct from Level 2 but operationally close to degradation. A wide ε_L3 indicates robust Level 3. This parametrization prevents Level 3 from becoming an unfalsifiable claim: every Level 3 classification must declare its perturbation envelope, and any perturbation within that envelope that produces gate activation falsifies the classification.

---

## Connection to ONTOΣ Series

**ONTOΣ I (Will as Ontological Operator):** The triad W → E → A establishes will as primordial directedness. Regime Depth stratifies the level at which this directedness operates: at Level 1, will is undirected impulse; at Level 2, will is constrained by structure; at Level 3, will and structure are co-aligned such that constraint enforcement is unnecessary.

**ONTOΣ V (Direction of Reconstruction):** The non-causal authorization of irreversible operations depends on regime depth. At Level 2, authorization gates are actively invoked. At Level 3, the operations requiring gating are structurally absent from the candidate set.

**ONTOΣ VI (Phase Mechanics):** Phase debt accumulates silently under locally correct behavior. Regime Depth explains *why* phase debt accumulates: Level 2 systems generate suppression load through continuous boundary enforcement, which constitutes a form of latent phase debt even when all transitions are correctly handled.

**ONTOΣ VII (From Formal Verification to Admissibility Architecture):** Safety invariants are Level 2. Admissibility architecture as formalized in ONTOΣ VII operates at Level 2 with non-causal gating (per §NAB). ONTOΣ VIII identifies Level 3 as the regime in which admissibility architecture becomes structurally idle — present but not load-bearing.

---

## Necessary Conditions for Level 3 Viability

ONTOΣ VIII does not prescribe how Level 3 is achieved. It does, however, identify conditions that must be satisfied for Level 3 to be maintainable over extended horizons. These are necessary conditions, not constructive algorithms.

First, the system must possess a non-potential dynamical component — in the language of Navigational Cybernetics 2.5, nonzero structural spin — that prevents attractor degeneration under bounded budget. Without such a component, gradient stagnation erodes attractor selectivity and Level 3 degrades into Level 2.

Second, the attractor geometry must be stabilized against perturbation. The condition Att(s) ∩ T_forbidden = ∅ must hold not only at the current configuration but in a neighborhood of it. A Level 3 classification that depends on the system remaining at a single precise configuration is structurally fragile and operationally equivalent to Level 2 with favorable initial conditions.

Third, the continuity budget must be sufficient to sustain the spin that maintains Level 3. Spin itself consumes structural resources. If τ falls below the threshold required to maintain non-degenerate rotational dynamics, spin collapses, attractor selectivity degrades, and Level 3 is lost.

Fourth, the system must not be subject to external forcing that persistently shifts attractor geometry toward the forbidden class faster than spin can compensate. Level 3 is maintainable under bounded perturbation, not under arbitrary adversarial reconfiguration.

These conditions delineate the viability envelope of Level 3 without specifying the mechanisms by which it is entered or sustained. The construction of Level 3 architectures is a separate problem.

---

## Status and Intent

ONTOΣ VIII fixes Regime Depth as an architectural parameter and establishes its non-reducibility. It does not propose algorithms for achieving Level 3. It does not claim that Level 3 is achievable for all system classes.

The contribution is the identification and formalization of a structural distinction that existing frameworks — CBF, Viability Theory, formal verification, trace-based model checking — do not capture: the depth at which trajectory exclusion operates determines long-horizon viability independently of boundary geometry. The further contribution is the demonstration that Level 3 cannot be maintained under purely potential dynamics, linking Regime Depth to the core dynamical structure of Navigational Cybernetics 2.5.

Navigational Cybernetics 2.5 is thereby extended from an architecture of prohibition to an architecture of regime depth.

---

## Closing Note

Systems do not fail because they lack prohibitions. They fail because their prohibitions operate at Level 2 while their generative dynamics remain at Level 1.

Long-lived architecture requires Level 3: not the strength to resist destructive trajectories, but a configuration in which destructive trajectories are not generated.

This is the transition from Constraint to Continuity Field. It is the next structural layer after admissibility.

---

## Appendix B — Interface-Level Protection of the Non-Actionability Barrier

This appendix provides formal evidence that the non-actionability barrier (§NAB) is not merely declarative. It demonstrates that the barrier has information-theoretic protection against reconstruction, steering, and chatter within bounded horizons.

**Relationship to §NAB:** The core barrier (§NAB.0–§NAB.6) establishes what the barrier is. Appendix B establishes that it can be sustained under adversarial probing.

### §B.1 — Non-Reconstructibility Axioms

**NR-ε — Bounded Per-Query Leakage.** The gate interface transcript O(s,u) satisfies O(s,u) = Φ(G(s,u), ξ) where ξ is independent of (s,u) and independent across queries. Conditioned on the permit/deny bit, the full observable transcript carries at most ε total variation of additional information about (s,u) or boundary geometry.

**NR-LR — Bounded Log-Likelihood Ratio.** For admissibility-consistent hypotheses G₁, G₂:

> |log (dL_{G₁}(Oₜ | F_{t−1}) / dL_{G₂}(Oₜ | F_{t−1}))| ≤ κε

This excludes rare transcript events whose probabilities differ by exponential factors across hypotheses.

**NR-Q — Bounded Probing Budget.** There exists a finite query budget T_max such that T ≤ T_max. If query budget is unbounded, admissibility reconstruction may become asymptotically possible. All NR guarantees are horizon-dependent.

### §B.2 — Structural Closure Theorem

Under NR-ε + NR-LR + NR-Q, combined with bounded meta-revision manipulability (ML-η) and Lyapunov revision descent (ML-V), the class is structurally closed:

**(i) Boundary non-identifiability.** For any finite admissibility candidate set {G⁽¹⁾, …, G⁽ᴹ⁾} and any reconstruction procedure:

> Pr(Î = I) ≤ (κ²/2 · T_max · ε² + log 2) / log M

**(ii) Meta-steering bound.** For any attempt to steer revision outcomes:

> I(R; W_c | W_nc) ≤ η

**(iii) Finite revision count.**

> N_max ≤ ⌊V(G₀) / α⌋

Admissibility cannot become an internal optimization object through transcript reconstruction, meta-layer witness steering, or unbounded revision chatter.

**Remark — Data Distribution as Indirect Leakage Channel.** The binary admit/deny decision, combined with the agent's knowledge of its own proposal, constitutes a labeled sample (s, u, G(s,u)). Under bounded horizon (NR-Q), labeled sample accumulation is bounded and boundary reconstruction precision is controlled by the Fano bound. Under unbounded horizon, labeled sample accumulation permits asymptotic boundary reconstruction regardless of NR-ε compliance. The protection of admissibility non-actionability therefore rests on NR-Q as a load-bearing architectural constraint, not on transcript indistinguishability alone. Systems whose operational horizon exceeds the NR-Q bound without architectural reset of boundary information are subject to reclassification per §NAB.4.

### §B.3 — Supporting Results

**KL Accumulation (Lemma 14).** D_KL(L_{G₁}(O_{1:T}) ∥ L_{G₂}(O_{1:T})) ≤ κ²/2 · T · ε².

**Fano Lower Bound (Theorem 51).** Identification Pr(Î = I) ≥ 1 − δ among M candidates requires T ≳ log M / (κ²ε²).

**Pinsker Bridge (Corollary 52.1).** D_TV(Pᵢ, Pⱼ) ≤ √(β/2). Under small β, transcript laws are pairwise indistinguishable in total variation.

**Meta-Steering Barrier (Theorem 53).** Under ML-η: Pr(Ĵ ≠ J) ≥ 1 − (η + log 2) / log M. Inducing one of exponentially many targeted revisions via witness manipulation is information-theoretically impossible when η is small.

### §B.4 — Falsification Surface

| Criterion | Violation condition | Detection method |
|-----------|-------------------|------------------|
| **NR-ε.F** | Transcripts distinguishable across (s,u) regimes with advantage > ε under fixed decision bit | Statistical distinguisher test |
| **NR-LR.F** | Transcript pattern frequency differs across admissibility-consistent regimes by factor > exp(κε) | One-sided likelihood ratio test |
| **ML-V.F** | Unbounded revision sequence with V(G_{k+1}) ≥ V(G_k) − α/2 for infinitely many k | Revision chatter monitoring |

**Falsification Window (Corollary 52.2).** If identification success Pr(Î = I) ≥ 1 − δ is achieved with T < (2/κ²ε²)[(1−δ) log M − log 2], then at least one of NR-ε or NR-LR is violated.

All criteria are one-sided: violations can be detected; satisfaction can only be upper-bounded under finite sampling.

**NR-dist.F — Detectable Distribution-Channel Leakage.** If the agent's policy or state distribution exhibits statistically detectable adaptation to admissibility boundary geometry — measured as decreasing denial rate under boundary-proximal perturbation that is not attributable to attractor-exclusion (Level 3) — then admissibility-relevant information has entered the causal pathway via distributional shaping. The system is reclassified per §NAB.4 regardless of NR-ε compliance.

### §B.5 — Relationship to Core Barrier

Appendix B does not define the non-actionability barrier. §NAB defines it.

If any §B bound is violated, the corresponding **implementation** fails — but the architectural classification (§NAB) remains valid. The barrier is a structural property of the class; the bounds are properties of implementations within the class.

---

DOI: [to be assigned]

MxBv, Poznan 2026. Copyright © 2025–2026 Maksim Barziankou. All rights reserved.