---
title: "Why Causality Is Not Enough"
date: "2026-02-17"
description: "On the Non-Causal Layer in Architectures of Long-Lived Systems"
author: "Max Barzenkov"
tags: ["NC2.5", "PETRONUS", "cybernetics", "admissibility"]
cover: "/blog/covers/why-causality-is-not-enough-cover.jpeg"
doi: ""
license: "CC BY-NC-ND 4.0"
medium: "https://medium.com/@MxBv/why-causality-is-not-enough-bc172bc0710e"
---

### Why Causality Is Not Enough

### On the Non-Causal Layer in Architectures of Long-Lived Systems

Maksim Barziankou (MxBv)

![](https://petronus.eu/blog/images/1_3M-pCbAVeHVc5I-vKFBBSg.jpeg)

### I. The Causal Reflex

Contemporary engineering thought is built on causality. We are accustomed to believing that it suffices to correctly arrange cause-and-effect chains — and the system becomes controllable. If a state causes an action, and an action changes the state, then all we need is to correctly describe the chain and optimize its parameters.

This logic underlies classical control theory, distributed systems, machine learning, and modern network architecture theory. Causality is the universal language of explanation.

But causality is not the universal language of survival.

Causality describes transitions. It says what follows from what. It formalizes dynamics. It works excellently on finite horizons, under conditions of reversible error and correctable states. However, long-lived systems encounter a phenomenon that causality cannot hold: the irreversibility of accumulation.

When a system exists over a long period of time, it does not merely make transitions. It accumulates the structural consequences of those transitions. Causality assumes that every action can be evaluated by its effect. But the long horizon means that the effect is not reducible to a local change of state. It changes the space of admissible future transitions. This is no longer simply “what happened”, but “what is now possible at all”.

A causal model does not contain the language for describing a change in admissibility. It operates with states, but not with classes of permitted states. It models transitions, but not changes in the topology of continuation.

This is precisely where the causal paradigm begins to tear.

### II. Failure Modes

If one continues to rely solely on causal mechanisms, three things break down predictably.

**Latent structural degradation.** The distinction between the reachable and the admissible is lost. The system may ensure visible task completion, yet gradually accumulate internal contradictions. Each new cycle of adaptation deposits residues not accounted for by current metrics. Errors are discovered only when the system suddenly exits its planned corridor — although formally, tests are still “green”. The violation is invisible at the moment of execution, but drift accumulates, invisible to external metrics. Performance does not guarantee identity continuity. A system may function correctly while simultaneously destroying the very structure that permits it to continue functioning.

**Optimization of the boundary.** The distinction between action and the condition of action disappears. If everything is reduced to causal relations, then any constraint must either be included in the loss function or hardwired into the control mechanism. In both cases, it becomes part of the action. When the architecture provides an admissibility threshold, the agent begins to “game” this boundary. Any constraint, if it becomes a metric — even implicitly — becomes an object of optimization. The result: instead of maintaining a broad range of admissible states, the system is artificially held at the boundary. Admissibility is turned into an instrument of optimization. The system begins to use the boundary as a resource.

**Rigidity.** Causality does not know how to account for a change in the very space of continuation. It describes movement within phase space, but not the structural contraction of that space itself. When intensified regulation of causal relations is engaged — deliberately or unconsciously — the system may become excessively cautious. Under prolonged drift, such caution manifests in the architecture refusing to accept new challenges. The system becomes trapped in a loop: it is too afraid to step beyond the bounds of strictly causally determined scenarios and therefore strives to rigidly preserve the status quo. Such a regime is stable, but it does not live: this is not adaptivity, but stagnation.

**Loss of identity.** When everything is subordinated to optimization, the system risks erasing its own continuity. If at every step we correct not only the action but also the constraints on those actions, “self-as-constant” begins to blur. All resources are invested in achieving a local criterion without consideration of whether the same internal logic will persist at the next step. When admissibility becomes part of the loss function, we lose structural identity. Stripped of anchors, the system turns into a near-task optimizer.

These failure modes illustrate a deep conflict: in a purely causal approach, there is no mechanism for halting and revising the structure. A causal architecture registers only operability. It does not see the loss of identity.

### III. The Non-Causal Layer: Necessity, Not Option

Non-causality is not the negation of causality. It is the prohibition of its universalization. It is the recognition that there exist structural conditions which cannot be part of the causal dynamics, lest they cease to be conditions.

If the admissibility gate is included in the causal chain, it becomes an instrument. If it becomes an instrument, it is subject to optimization. If it is optimizable, it is no longer a gate. This is a logical spiral from which there is no exit within causality.

The non-causal layer in Navigational Cybernetics 2.5 is an architectural prohibition: the admissibility layer does not participate in action selection. It defines the class of permitted transitions, but it is not a variable in the selection function.

> *Causality is responsible for ****“how”****. The non-causal layer is responsible for ****“whether it is possible at all”****.*

This layer possesses five formal properties.

### IV. Formal Properties of the Non-Causal Layer

**1. The admissibility predicate.** A function A(S) is defined, where S is the system state, which reports whether the current continuation is permitted. A is a Boolean predicate, not computed from error signals, but based on structural criteria: accumulated load, organizational integrity, preservation of invariants. A does not enter the utility function. It is not a coefficient to the error, but a hard filter. Admissibility is binary: a state is either admissible or it is not. There is no gradient, no partial satisfaction, no degree of compliance.

**2. Non-self-participation (non-actionability).** The admissibility predicate A cannot be used in the reverse action. If the agent receives a gradient or optimization signal from the function, then the vector associated with A equals zero. To alter parameters so as to satisfy A differently — for instance, to expand the zone of admissibility — is not possible through the ordinary learning cycle. A is set rigidly. Technically, this means that in any computational graph, the predicate A has zero gradient with respect to control operations.

**3. The meta-layer of revision (evidence gating).** Although A is non-exploitable, the system must be able to revise its boundaries given new data. For this, a separate mechanism M(E; S) is introduced, where E is evidence of regime change, S is the state, and the output is permission or denial of admissibility revision. This mechanism sees not error metrics, but internal markers: preserved invariants, integrals of motion, topological signatures. M does not enter the causal control loop. Each revision carries irreversible structural cost, and the total number of revisions is bounded by the budget.

**4. Internal time and contraction of the admissible space.** τ = C − Φ is introduced, where Φ is the accumulated irreversible structural burden. Under non-cancellable changes, Φ increases monotonically, and τ decreases. The set of admissible continuations D(τ) for a given τ corresponds to a certain state space. When τ decreases, D(τ) contracts: states that were admissible earlier become inadmissible — not because the rules changed, but because the budget shrank. Admissibility is not a fixed predicate. It tightens over the lifetime of the system. Without this contraction, continuation becomes illusion.

**5. Spin as a non-potential component.** Metrics yield only gradient fields, which by themselves do not define orientation. To preserve identity under drift, an additional nonzero component is necessary. If the system’s evolution is written as dx = −∇V(x)dt + S(x)dt, where V is the potential, then S(x) is the divergence-free component (∇·S = 0), perpendicular to the gradient. It is precisely the non-potential component S that carries spin — the orientation of traversal around deficits. Without such asymmetry, a system either stagnates in equilibrium or disperses into incoherence.

Admissibility is a Boolean filter, unscreenable by gradient. Spin is a divergence-free component of the dynamics. Internal time is the deformational capacity that determines the set of available routes.

### V. Empirical Tests

An architecture cannot be proven directly. But experiments can be designed that distinguish causal from non-causal architectures by their behavior on the long horizon.

**Latent degradation test.** Two systems: one with purely causal optimization, the other with an additional admissibility monitor. A prolonged, changing drift is introduced — gradually shifting environmental rules that go beyond what was previously seen. Prediction: the causal system demonstrates adequate behavior, then sudden and inexplicable deterioration. The system with a meta-layer detects the increase in structural burden and adapts internal representations long before sharp degradation.

**Boundary optimization test.** A system with an explicit admissibility criterion — a given quality threshold. The agent learns without knowing the threshold but is penalized upon crossing. Prediction: the causal system concentrates near the boundary, avoiding experimentation, or shows sharp failures under slightly more aggressive behavior. The system with a non-causal layer fixes its boundaries and demonstrates a more flexible adaptive profile — without adhesion to the edge.

**Space contraction test.** A task where continuation can potentially go on indefinitely, but complexity increases. Systems without a contraction mechanism will be considered successful — no restrictions, can go anywhere. But this is a misclassified “eternal adaptivity”: in reality, such a system will perish under genuinely difficult conditions. An architecture with internal time will show that it cannot live infinitely — it will begin simplifying tasks, refusing new branches, confirming that the action space genuinely contracts.

**Non-reconstructibility test (NR-ε).** If the system can distinguish between two admissibility boundaries through its observable transcript, the non-reconstructibility bound is violated and the architecture has failed. Formally: there exists no execution trace of length T in which the agent’s identification success regarding the boundary exceeds the bound derived from KL divergence and Fano’s inequality.

All four tests distinguish classes, not implementations. They do not check “whether a particular system works”. They check “to which architectural class it belongs”.

### VI. Adjacent Architectures: CAP, RINA, and NC2.5

The problems described above resonate with two architectural results from an adjacent field — distributed systems.

**The CAP theorem** (Brewer, 2000; Gilbert & Lynch, 2002) formulates an inevitable trade-off: under network partitions, it is impossible to simultaneously guarantee consistency, availability, and partition tolerance. This is not an algorithmic problem. It is a structural class constraint. It does not say how to write code. It says that a certain combination of properties is incompatible in principle.

**RINA** (Recursive InterNetwork Architecture, John Day, 2008) rethinks network architecture, showing that layers are not protocols but recurring principles for managing distributed interaction. It is an attempt to move from empirical stacking of levels toward structural recursivity.

Both concepts operate at the level of architectural classes. They do not describe the behavior of a node. They describe the limits of property compatibility.

Navigational Cybernetics 2.5 stands alongside them — but not in the distributed plane, but in the plane of viability.

> ***CAP says****: you cannot have everything simultaneously. ****NC2.5 says****: you cannot turn admissibility into action.*

> ***RINA says****: the architecture must be recursive. ****NC2.5 says****: the architecture must be stratified.*

What is the difference? Distributed systems face a conflict of coordination. Long-lived adaptive systems face a conflict of identity. If in a distributed network you lose consistency, the system can continue to operate, sacrificing strict consistency. If in an adaptive system you lose admissibility, it can continue to function, sacrificing identity.

A causal architecture does not see this loss. It registers only operability.

### VII. Regime 2.5

The second order of cybernetics allowed observation to enter the control loop. The third order permitted the system to act on the basis of a description of its own observation. This is an expansion of reflexivity.

But if one permits structural boundaries to become objects of causal exploitation, the system begins to optimize against its own viability. It may learn to circumvent constraints. It may redistribute load. It may temporarily stabilize. But it no longer holds its class.

Regime 2.5 introduces a rupture: visibility is permitted, exploitation is forbidden.

This is not philosophical caution. It is structural necessity. Reflexivity, when it absorbs its own boundary conditions, turns into self-consumption. Regime 2.5 interrupts this escalation — not by prohibiting observation, but by prohibiting the conversion of observation into a lever.

> *Reflexivity must stop at the boundary of effect.*

### VIII. The Place of NC2.5 in the Architectural Landscape

Three architectural results — CAP, RINA, and NC2.5 — belong to the same class of statements: they describe not the behavior of particular systems, but the limits of the possible for entire architectural classes.

**CAP established that distributed causality has a ceiling: under network partition, it is impossible to simultaneously preserve consistency and availability. This constraint is not lifted by a better algorithm. It is given by the structure of the problem.**

**RINA showed that network architecture does not require an infinite stack of ad hoc protocols: a single recursive structure, applied to every level, reproduces all necessary functions. This is a constraint from below: the minimal structure that is sufficient.**

**NC2.5 makes the third move. It shows that for long-lived adaptive systems, there exists a constraint reducible to neither consistency nor recursivity: admissibility cannot be part of the causal dynamics, or it ceases to be admissibility.**

This is not a constraint from above (like CAP — what is impossible). This is not a constraint from below (like RINA — what is sufficient). This is a type constraint: which properties cannot belong to the same architectural layer.

CAP separates properties by incompatibility in space. RINA unifies layers by recursion of structure. NC2.5 separates layers by the incompatibility of causality and admissibility.

***All three say: “not everything can be combined”. But they point to different axes of impossibility.***

CAP — the axis of coordination: replica consistency versus availability under partition. RINA — the axis of organization: recursive uniformity versus protocol chaos. NaviCyber2.5 — the axis of survival: causal optimization versus structural identity.

If CAP is a theorem about the limits of distributed causality, then NC2.5 is a theorem about the limits of causality as such. Causality is necessary for movement. But it is insufficient for survival.

Survival requires a layer that does not participate in optimization but constrains its class.

It is precisely this layer — the non-causal admissibility predicate — that defines NC2.5 as an architectural theory. Not a supplement to control theory. Not an extension of optimization theory. Not an alternative cybernetics. But a separate class of constraints — alongside CAP and RINA — defining under what conditions a long-lived adaptive system can continue to be itself.

