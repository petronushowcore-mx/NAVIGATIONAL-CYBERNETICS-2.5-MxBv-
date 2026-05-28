# Operator-Mobility: Formal Foundations

*Companion to "The Thousand-Year Warrior, or A Human Absorbs the Universe". Both works are deposited under the same DOI as a single OSF record. This work supplies the measure-theoretic and categorical foundation underlying the phenomenological exposition there.*

**Author:** Maksim Barziankou (MxBv)
**Date:** 24 May 2026
**Affiliation:** The Urgrund Laboratory, Poznań
**DOI:** 10.17605/OSF.IO/ZY3PW (shared with the phenomenological essay)
**License:** CC BY-NC-ND 4.0

---

## Abstract

This paper defines the formal object that a hypothesis of operator-mobility would have to satisfy, and describes what specifically must fail for such a hypothesis to be false. Existence of operator-mobility in any system — biological, artificial, or hybrid — is not proved here.

Operator-mobility is understood as the preservation of operator-position across heterogeneous substrates — not consciousness, not simulation, not embodiment, and not transfer in the usual senses of those words. The primitive is transposition: an operator displaced into a foreign substrate while preserving its operator-image, shifting its priors-dominance, and leaving a measurable post-interval trace. Most discussions of empathy, embodiment, transfer, and simulation collapse three different conditions into one; the paper separates them.

Structural persistence of the operator-image is formalised by the anchor-persistence relation R_α as isomorphism in the operator-image quotient category Dep^{img}(O) — a categorical condition that does not depend on the choice of observation channel. Priors-inversion is measured on a declared channel by the finite-horizon index D_θ(T) = D_{KL}(Q^θ_I ‖ P_{S,n}^θ) − D_{KL}(Q^θ_I ‖ P_{S',n}^θ); this is channel-relative but computable under standard regularity. Non-hallucinated residue is tested by a post-interval trace τ_θ under explicit non-degeneracy and non-reset hypotheses: the operator-image at end-of-interval has to differ from the pre-interval baseline by a measurable amount.

D_θ > 0 alone does not classify a candidate as true transposition; it shows only priors-inversion. A candidate has to pass the D-test, the R_α/T1 isomorphism check, and the τ-trace test, and failure at each layer names a different class — imitation, anchor failure, hallucinated transposition, non-accumulation, or curriculum-pathology.

The supporting mathematical ingredients are standard for this class of problems — Markov substrates on standard-Borel spaces, finite-horizon observation channels, relative-entropy production as one canonical Φ-realisation, Blackwell, Le Cam, and Fano bounds for what channels can and cannot distinguish, a LaSalle-type conditional conversion theorem for accumulation under explicit drift hypotheses — but their combination into the transposition test is deliberately restrictive: Φ-realising deployments, channel sufficiency for the full family used by the D-test, reverse-kernel access for the substrate-realised cost equality, sub-Markov-kernel equality on operator-images, and per-operator observability are explicit load-bearing assumptions, not generic consequences of the standard machinery. The conditional structure of the framework is the architecture of the classification rather than a defence: each hypothesis screens off a specific failure class, and removing any one re-opens the corresponding class.

**Scope of the proved results (to forestall over-reading).** Three boundaries are load-bearing and should be read *with* the results, not as afterthoughts. (i) The protocol-closure theorem (Theorem 10.6) is *catalogue-relative and tolerance-relative*: it closes the six named adversarial mechanisms of §12 at sufficient resolution, not arbitrary adversaries — a system engineered to match all declared invariants within tolerance falls outside the catalogue by construction, so the result is not general soundness against reductionist or adversarial imitation. (ii) The architectural-mobility state M(O; n) is a *structural-disposition* verdict, built on the pre-verification cost c_next over the structurally-admissible candidate class, not a verified-mobility claim; any empirical-mobility statement must use the verified functional c_next^{ver} (over the test-passing subset). (iii) Under the canonical Crooks–Jarzynski–Seifert entropy-production realisation of Φ, the non-trivial Φ-realising regime is essentially *softened-(R4) one-directional* admissibility — an antisymmetry obstruction (Remark 8.4.1) closes the hard-support bidirectional case; the operator-mobility *primitive* may be more general, but the proved §10–§11 machinery lives in that regime under the canonical cost.

The work is a formal companion to *The Thousand-Year Warrior* — a testable object with declared failure modes and an explicit falsification surface, neither a proof of consciousness nor evidence that biological operators are mobile in any specific sense.

---

## §0. Mathematical preliminaries

This section fixes notation. Readers familiar with measure theory and category theory may skip to §1.

### §0.1 Measurable spaces and probability measures

A *measurable space* is a pair (X, F) where X is a set and F is a σ-algebra on X. A *probability measure* on (X, F) is a countably additive map μ : F → [0, 1] with μ(X) = 1. Write 𝒫(X, F) for the set of probability measures on (X, F).

A *measurable map* f : (X, F) → (Y, G) is a map f : X → Y with f^{-1}(B) ∈ F for every B ∈ G.

### §0.2 Pushforward measures

For measurable f : (X, F) → (Y, G) and μ ∈ 𝒫(X, F), the *pushforward* f_* μ ∈ 𝒫(Y, G) is defined by

f_* μ(B) := μ(f^{-1}(B))    for B ∈ G.

### §0.3 Markov kernels and trajectory laws

A *Markov kernel* on (X, F) is a map K : X × F → [0, 1] such that

(K1) for each x ∈ X, K(x, ·) ∈ 𝒫(X, F);
(K2) for each B ∈ F, K(·, B) is F-measurable.

A *stationary measure* for K is μ ∈ 𝒫(X, F) with μK = μ, where (μK)(B) := ∫_X K(x, B) dμ(x).

Given μ ∈ 𝒫(X, F) and Markov kernel K, the *trajectory law* P_K^{(n)} on (X^n, F^{⊗n}) is the joint law of (X_0, ..., X_{n−1}) with X_0 ∼ μ and X_{i+1} | X_i ∼ K(X_i, ·). The infinite-horizon trajectory law P_K on (X^ℕ, F^{⊗ℕ}) exists by the Ionescu-Tulcea / Kolmogorov extension theorem.

### §0.4 Relative entropy (KL divergence)

For P, Q ∈ 𝒫(X, F):

D_{KL}(Q ‖ P) := ∫_X (dQ/dP) log(dQ/dP) dP    if Q ≪ P,
D_{KL}(Q ‖ P) := +∞    otherwise.

D_{KL}(Q ‖ P) ≥ 0 with equality iff Q = P (Gibbs).

*Pinsker inequality* (Csiszár 1967; Cover & Thomas Theorem 11.6.1): ‖Q − P‖_{TV} ≤ √((1/2) D_{KL}(Q ‖ P)), where ‖·‖_{TV} is total variation.

### §0.5 Time-reversal of Markov kernels

For a Markov kernel K on (X, F) with stationary measure μ, define the *forward joint measure* π on (X × X, F ⊗ F) by

**π(A × B) := ∫_A K(x, B) μ(dx)**

and the *reverse joint measure* π* by π*(A × B) := π(B × A). The *time-reversed kernel* K^{rev}, when it exists, is the Markov kernel disintegrating π* against its first marginal μ:

**K^{rev}(y, dx) μ(dy) = π*(dy × dx) = K(x, dy) μ(dx)**

as measures on (X × X, F ⊗ F).

**Existence and absolute-continuity hypotheses (separated).** K^{rev} exists as a regular conditional probability via the disintegration theorem on standard Borel spaces (Kallenberg, *Foundations of Modern Probability*, Theorem 6.4; equivalent formulations in Bogachev *Measure Theory* Vol. II Ch. 10). *No absolute continuity is required for existence per se.* Under stationarity (μK = μ), the first marginal of π* equals μ (since π's second marginal is ∫ K(x, ·) μ(dx) = μK = μ, and π*(A × B) := π(B × A) inherits μ as first marginal); the disintegration yields K^{rev} unique μ-a.e. The original formulation traces to Kolmogorov 1936; Nelson 1958 develops the time-reversal theory for general Markov processes.

Absolute continuity assumptions enter *separately* and only for derived objects:

* **For the Radon-Nikodym log-density r_K** (below) to be defined: K(x, ·) ≪ K^{rev}(x, ·) for μ-a.e. x.
* **For finite joint entropy production** D_{KL}(π ‖ π*) < ∞: π ≪ π*.

We henceforth assume these latter conditions when invoking r_K and entropy-production formulas.

K is *reversible* iff π = π* (equivalently K^{rev} = K μ-a.e.).

**Conditional irreversibility log-density.** When K(x, ·) ≪ K^{rev}(x, ·) for μ-a.e. x, the conditional Radon-Nikodym derivative

**r_K(x, y) := log [ d K(x, ·)/dK^{rev}(x, ·) ] (y)**

is defined for K(x, ·)-a.e. y, for μ-a.e. x. By disintegration on standard Borel spaces, r_K admits a jointly (F ⊗ F)-measurable version (which we fix henceforth).

Integrating r_K against the forward joint gives the joint entropy production:

∫_{X × X} r_K(x, y) π(dx, dy) = D_{KL}(π ‖ π*) ≥ 0

with equality iff K reversible. Justification: under stationarity μK = μ, the joint π has first marginal μ (by construction) and second marginal ∫ K(x, ·) μ(dx) = μK = μ. Hence π* (defined by π*(A × B) := π(B × A)) has first marginal equal to π's second marginal = μ, and second marginal equal to π's first marginal = μ. Both π and π* share marginals (μ, μ). The chain rule for relative entropy along the first coordinate then gives D_{KL}(π ‖ π*) = D_{KL}(μ ‖ μ) + ∫ D_{KL}(K(x,·) ‖ K^{rev}(x,·)) μ(dx) = 0 + ⟨r_K⟩_π, recovering the displayed identity.

### §0.6 Categories and equivalence relations

A *category* C consists of objects Ob(C) and morphism sets Hom_C(A, B) for each pair A, B ∈ Ob(C), with associative composition and identity morphisms. A *groupoid* is a category in which every morphism is invertible.

For any category C, the relation "there exists an isomorphism A → B" is an equivalence relation on Ob(C) (reflexivity: id; symmetry: invert; transitivity: compose).

### §0.7 Standing conventions

All measurable spaces in the sequel are standard Borel (Polish space with its Borel σ-algebra) unless otherwise stated. This guarantees Radon-Nikodym derivatives, regular conditional probabilities, and disintegration of measures. Measurability of specific maps is stated explicitly at each use; non-measurable maps are excluded by construction.

**Topology convention (for neighbourhood / support language).** Whenever the text uses topological vocabulary — *neighbourhood*, *support*, *open set*, *closure* — we fix a compatible Polish topology generating the stated Borel σ-algebra. Standard Borel spaces admit such a topology (Kuratowski's theorem: every standard Borel space is Borel-isomorphic to a Polish space with its Borel σ-algebra); the specific Polish topology is canonical up to Borel isomorphism but is part of the deployment specification when neighbourhood-level claims are invoked (e.g., Def. 3.1 (D1) for atomless substrates). Without fixed Polish topology, neighbourhood language is interpreted as «measurable set containing the point with positive μ-measure» — the σ-algebra-level surrogate.

### §0.8 Filtered probability spaces, supermartingales, and LaSalle invariance

For §9's convergence analysis we briefly fix discrete-time stochastic-process notation.

A *filtered probability space* is (Ω, F, (F_n)_{n∈ℕ}, P) with F_n ⊂ F_{n+1} ⊂ F a non-decreasing sequence of sub-σ-algebras (the *filtration*). An adapted process (X_n)_{n∈ℕ} on state space (S, F_S) is a sequence with X_n F_n-measurable.

**Supermartingale (Doob).** A non-negative adapted process (V_n) is a *supermartingale* if E[V_{n+1} | F_n] ≤ V_n P-a.s. for all n. Doob's supermartingale convergence theorem: V_n converges almost surely to a finite limit V_∞.

**Foster-Lyapunov drift (general form).** Given V : S → ℝ_{≥0} measurable (the *Lyapunov function*), the *drift condition* is: there exists a measurable γ : S → ℝ_{≥0} with γ(x) ≥ 0 everywhere (no strict-positivity-outside-D requirement imposed at the preliminary level) such that

E[V(X_{n+1}) | F_n] ≤ V(X_n) − γ(X_n).

The set on which γ vanishes — denoted {γ = 0} ⊂ S — is the *drift-vanishing set*; it may coincide with a designated target D ⊂ S (the *strict-target case*: γ > 0 on S \ D) or may strictly contain D (the *general case*: γ vanishes on D plus additional invariant residue regions where the drift mechanism fails to fire). The framework's §9.3 uses the general case.

The conclusion under the drift condition has two layers. Bare drift gives only the supermartingale layer: under the drift condition above plus standard integrability (V(X_0) ∈ L^1, say), V(X_n) is a non-negative supermartingale, so V_n converges almost surely to a finite limit V_∞, and Σ_n E[γ(X_n)] < ∞ implies γ(X_n) → 0 in L^1 (and almost surely along a subsequence). Drift alone gives V-convergence and γ-summability, nothing more.

Convergence to the invariant subset of {γ = 0} requires additional LaSalle regularity. The further conclusion that (X_n) converges almost surely to the largest invariant subset of {x : γ(x) = 0} (Kushner 1971; LaSalle 1960 for the deterministic original; Meyn–Tweedie 1993) requires stochastic-LaSalle regularity hypotheses — typically some combination of tightness or precompactness of trajectories (so that ω-limits exist), Feller continuity of the underlying Markov kernel (so that limits of γ along the trajectory equal γ at limits), and invariance of the limit set under the dynamics. These are not automatic from drift. Under such regularity the ω-limit set of (X_n) is contained in the largest invariant subset of {x : γ(x) = 0}; equivalently, when the chosen topology supports a distance to that set, dist(X_n, Inv({γ = 0})) → 0 P-a.s. In the strict-target case (γ > 0 on S \ D) the invariant subset is contained in D and convergence to D follows as a corollary; in the general case the invariant subset may decompose into D ∪ residue regions where γ vanishes (§9.3 makes this decomposition explicit via M_{success} ∪ M_{failure}, conditional on the (I) hypothesis of forward-invariance of {γ = 0}).

References: Kushner 1971 §2.3–2.5 for the stochastic LaSalle hypotheses; Meyn–Tweedie 2009 Ch. 11 for Foster-Lyapunov + hitting-time bounds; Hairer-Mattingly 2011 for explicit regularity conditions in continuous state-space stochastic LaSalle.

Application in §9: V(O; n) := c_{next}(O; n) (the next-transposition cost functional of Def. 9.2), Foster-Lyapunov drift means each transposition expectedly decreases c_{next} when it exceeds threshold δ_O.

These conventions instantiate one canonical formalisation of the architectural primitive; the primitive itself (transposition of operator-position across substrate) is not committed to the standard-Borel-Markov apparatus. Alternative formalisations — σ-finite spaces, semi-Markov dynamics, partially-observed kernels, information-geometric Fisher metric, enriched-categorical cost-grading — are available, each with its own regularity tradeoffs. The choice here is operational: standard-Borel-Markov makes D, Φ, and the falsification protocol concretely computable.

---

## §1. The operator-position

### Definition 1.1 (operator-position)

An *operator-position* is a tuple

**O = (Σ, F_Σ, Α, Φ, α)**

where:

(i) (Σ, F_Σ) is a standard Borel measurable space — the *operator state space*;

(ii) **Α** : Σ × Σ → {0, 1} is the *admissibility indicator* — a jointly (F_Σ ⊗ F_Σ)-measurable map satisfying

* (Α1) Α(s, s) = 1 for all s ∈ Σ (self-transition admissible);
* (Α2) the *admissibility set* of s is A_s := {t ∈ Σ : Α(s, t) = 1}; by joint measurability of Α, A_s ∈ F_Σ for every s, and the map s ↦ A_s has measurable graph.

We say transition s → t is *admissible* iff Α(s, t) = 1 iff t ∈ A_s.

An earlier formulation as a {0, 1}-valued Markov kernel was structurally wrong: under (Α1)-style closure under countable disjoint unions, such a kernel would be concentrated on a single atom, making A_s vacuously a singleton. The correct primitive is a measurable indicator on Σ × Σ — equivalently, a measurable binary relation on Σ.

(iii) **Φ** : Σ × Σ → [0, +∞] is the *abstract cost specification*, measurable on Σ × Σ, satisfying

* (Φ1) Φ(s, s) = 0;
* (Φ2) Φ(s, t) ∈ (0, +∞) if t ∈ A_s \ {s};
* (Φ3) Φ(s, t) = +∞ if t ∉ A_s;
* (Φ4) **irreversibility specification** — either (a) no non-trivial round-trip-admissible pair exists (i.e., for all s ≠ t with t ∈ A_s, we have s ∉ A_t — admissibility is strictly one-directional, in which case (Φ4) is vacuously satisfied with ε_O undefined), or (b) there exists ε_O > 0 such that for all s ≠ t in Σ with both t ∈ A_s and s ∈ A_t:
  Φ(s, t) + Φ(t, s) ≥ ε_O.

The bound ε_O is the operator's *round-trip irreversibility floor*: the operator commits to a minimum non-recoverable cost for round-trips. Φ is part of O's specification independently of substrate. Whether a given substrate can *realise* this Φ-specification (via its own intrinsic irreversibility production) is a deployment condition (Def. 3.1 (D2)).

(iv) **α** ∈ 𝒜 is a *nominal label* drawn from a measurable *label space* (𝒜, F_𝒜). (We use the script 𝒜 to distinguish the label space from A_s = {t ∈ Σ : Α(s, t) = 1}, the admissibility set, and from Α, the admissibility indicator.) The label space may be countable (discrete tokens), uncountable (e.g., latent-vector tokens in ℝ^d for neural-system embodiments), or any standard Borel space. α is *not* an independent identity primitive — it does not enter the construction of Dep(O) (cf. Prop. 10.4) and carries no mathematical content beyond serving as a label whose operational meaning is exhausted by the R_α-equivalence class on Dep^{img}(O). The work occasionally uses «identity-token» as descriptive shorthand for this nominal labelling role; readers should not infer that α carries structural content independent of (Σ, F_Σ, Α, Φ). A genuinely load-bearing identity-token would require loading α into the construction of Dep(O) — via a chosen distinguished morphism, pointed structure, or admissible morphism class indexed by α — which we do not pursue here; that strengthening is recorded as an open extension in §18 architectural alternatives.

### Principle 1.2 (admissibility-before-optimisation)

For any objective function φ : Σ × Σ → ℝ used by the operator (e.g., utility, reward, payoff), the *operator policy* is constrained to {(s, t) : t ∈ A_s}. Optimisation may select t ∈ A_s; it cannot override Α.

This is an axiom of the framework. The companion essay argues that operators are distinguished from purely-optimising systems precisely by the presence of Α as a gate independent of φ. Without 1.2, the framework collapses to optimisation theory and the operator-mobility primitive becomes vacuous.

---

## §2. Substrate

### Definition 2.1 (substrate)

A *substrate* is a quadruple

**S = (X_S, F_S, μ_S, K_S)**

where:

(i) (X_S, F_S) is a standard Borel measurable space — the *substrate state space*;

(ii) μ_S ∈ 𝒫(X_S, F_S) is the *substrate reference measure*;

(iii) K_S is a Markov kernel on (X_S, F_S) with stationary measure μ_S (i.e., μ_S K_S = μ_S).

The kernel K_S encodes *substrate dynamics*: from state x, the next state is drawn from K_S(x, ·). The triple (X_S, F_S, K_S) determines the *substrate-prior trajectory law* P_S on (X_S^ℕ, F_S^{⊗ℕ}) via §0.3.

### Definition 2.2 (substrate-prior on finite horizons)

For finite n ≥ 1, the n-step trajectory law on (X_S^n, F_S^{⊗n}) is denoted P_S^{(n)}. We freely write P_S when context selects the horizon.

### Remark 2.3 (open class of substrates)

Standard-Borel-Markov is a working specification chosen to make D and Φ tractable. Wider classes (semi-Markov, partially-observed Markov, non-stationary kernels) admit analogous constructions with extra regularity hypotheses. The class boundary is not closed here; see companion mini-series "The Bodies They Are Building".

---

## §3. Deployment of operator through substrate

### Definition 3.1 (deployment)

A *deployment* of O = (Σ, F_Σ, Α, Φ, α) through S = (X_S, F_S, μ_S, K_S) is a measurable injection

**ι_S : (Σ, F_Σ) → (X_S, F_S)**

satisfying:

(D1) **dynamical compatibility** — for s ∈ Σ and t ∈ A_s, the substrate-side image ι_S(t) lies in the topological support of K_S(ι_S(s), ·) with respect to the fixed Polish topology of (X_S, F_S) (§0.7 topology convention): equivalently, every open neighbourhood U of ι_S(t) satisfies K_S(ι_S(s), U) > 0. For discrete substrates this reduces to K_S(ι_S(s), {ι_S(t)}) > 0 (singletons are open). For atomless substrates such as diffusions, singletons have K_S(ι_S(s), ·)-measure zero and are not directly constrained; (D1) requires positive kernel mass on every open neighbourhood of ι_S(t). A stronger (and stricter) alternative — requiring K_S(ι_S(s), B) > 0 for every F_S-measurable B with ι_S(t) ∈ B and μ_S(B) > 0 — is admissible but generally too restrictive for noisy substrates with non-trivial substrate-complement dynamics; the present formulation uses the support-based version as the default, retaining the measure-quantified version as an optional strengthening per deployment specification.

(D2) **cost realisability** — there exists a jointly (F_S ⊗ F_S)-measurable Φ_S* : X_S × X_S → [0, +∞] with Φ_S* (ι_S(s), ι_S(t)) = Φ(s, t) for all s, t ∈ Σ (pointwise equality on ι_S(Σ) × ι_S(Σ); for atomless substrates, (D2) is required to hold in the appropriate a.e. sense — see §8.2 for the canonical Φ-realising specification). (D2) pins Φ_S* uniquely on ι_S(Σ) × ι_S(Σ) but not off it; this matters for morphism cost-preservation in §4.1(M3), where the obligation is interpreted as preservation on the operator-image subset only.

We write **O@S = (O, S, ι_S)** for the resulting deployment.

### Definition 3.2 (admissible substrate)

S is *admissible for O* iff at least one deployment O@S exists. Write Adm(O) for the class of admissible substrates.

### Remark 3.3

The existence problem — for which O and S a deployment exists — is a nontrivial question. Necessary conditions include cardinality (|Σ| ≤ |X_S| for Σ countable) and dynamical (the admissibility graph of O must embed in the positivity structure of K_S in the sense of (D1)). Sufficient conditions are not addressed here.

---

## §4. The deployment category and the anchor-persistence relation

### Definition 4.1 (deployment category)

The *deployment category* of O, denoted **Dep(O)**, has:

* **Objects:** deployments O@S = (O, S, ι_S) for S ∈ Adm(O);

* **Morphisms:** a morphism f : O@S → O@S' is a measurable map f : (X_S, F_S) → (X_{S'}, F_{S'}) satisfying

  (M1) ι_{S'} = f ∘ ι_S    (commutes on the operator state-space image);

  (M2) **admissibility preservation** — follows automatically from (M1) combined with (D1) on the target deployment O@S': since f∘ι_S = ι_{S'} pointwise on Σ, (D1) applied to O@S' yields positivity of K_{S'} at images of admissible transitions. We record (M2) as a derived consistency requirement, not as an independent constraint;

  (M3) Φ_{S'}*(f∘ι_S(s), f∘ι_S(t)) = Φ_S*(ι_S(s), ι_S(t)) for s ∈ Σ, t ∈ A_s    (cost preservation on the operator-image; both sides are uniquely determined on ι_S(Σ) × ι_S(Σ) by (D2) of their respective deployments, so this condition is well-posed independently of choice of measurable extension off the operator-image). Two layers must be distinguished. In *general deployments* under Def. 3.1, (M3) is the equality of the declared realised cost extensions Φ_S*, Φ_{S'}* on operator-image admissible transitions; these are pinned by (D2) as Φ(s, t) for each deployment, so (M3) reduces to the Φ-axiom-level identity Φ(s, t) = Φ(s, t) — automatic, no further content. In *Φ-realising deployments* (Def. 8.2), Φ_S* is additionally *chosen* to be a fixed measurable version of the substrate-realised cost Ψ_S = log(dK_S/dK_S^{rev}) on the operator-image, with Ψ_S = Φ ν_s-a.e. on operator-image admissible transitions (R3). At this stronger layer (M3) becomes substrate-realised cost equality — Ψ_S equals Ψ_{S'} on the operator-image. This Ψ-layer equality is *not* implied by (M4): (M4) constrains forward outflow from the operator-image (K_S^ι), but Ψ_S depends additionally on K_S^{rev} which is determined by inflow into the operator-image from the substrate-complement X_S \ ι_S(Σ) via the §0.5 disintegration. Two deployments with K_S^ι = K_{S'}^ι can have differing substrate-complement inflow patterns into the operator-image, yielding K_S^{rev} ≠ K_{S'}^{rev} restricted to ι_S(Σ) × ι_S(Σ) and hence Ψ_S(ι_S(s), ι_S(t)) ≠ Ψ_{S'}(ι_{S'}(s), ι_{S'}(t)). (M3) is therefore retained as an **independent morphism axiom** alongside (M4): under Φ-realising it carries the substrate-realised cost equality content that (M4) alone does not entail;

  (M4) **operator-image sub-Markov-kernel equality (Σ-intrinsic).** The deployment ι_S induces a sub-Markov-kernel K_S^ι on (Σ × Σ, F_Σ ⊗ F_Σ) by

   **K_S^ι(s, B) := K_S(ι_S(s), ι_S(B))    for s ∈ Σ, B ∈ F_Σ.**

   Symmetrically K_{S'}^ι is the operator-image sub-Markov-kernel of O@S'. The morphism condition is

   **K_S^ι = K_{S'}^ι**    as sub-Markov-kernels on (Σ × Σ, F_Σ ⊗ F_Σ).

   This is a structural constraint *intrinsic to* Σ. It does not depend on f beyond the fact that f restricts to ι_{S'} ∘ ι_S^{-1} on the operator-image (forced by (M1) plus injectivity of ι_S, ι_{S'} as standard-Borel injections). The sub-kernel K_S^ι captures the substrate-induced transition probabilities that the operator-image realises on Σ. The mass deficit 1 − K_S^ι(s, Σ) ≥ 0 records the substrate-side probability of operator-image excursion — transitions leaving ι_S(Σ) into the substrate-complement. Because (M4) requires equality of sub-Markov kernels on all (s, B) ∈ Σ × F_Σ, taking B = Σ gives K_S^ι(s, Σ) = K_{S'}^ι(s, Σ), so the excursion-probability mass deficit is *also* equality-constrained by (M4): 1 − K_S^ι(s, Σ) = 1 − K_{S'}^ι(s, Σ) for each s ∈ Σ. Sub-Markov-kernel equality is therefore a stronger constraint than mere within-image transition rate matching — it additionally requires that substrate-induced excursion probabilities into the substrate-complement agree between deployments. A natural weakening exists: replace (M4) with equality of the conditional-normalised kernels K_S^ι(s, ·) / K_S^ι(s, Σ) on Σ (when the normaliser is positive), which would constrain only the conditional within-operator-image dynamics and leave excursion probabilities free. We do not adopt this weaker variant in the present framework; (M4) is the stronger sub-Markov version. Test 16.2b step 4' explicitly requires the sub-Markov (mass-deficit-aware) estimator rather than the conditional-normalised one.

   (M4) is what makes R_α/T1 a genuinely non-trivial structural test rather than a typing artefact. Without (M4), a canonical operator-image bijection f(ι_S(s)) := ι_{S'}(s) automatically satisfies (M1) and (M3) for any two Φ-realising deployments of the same O, making R_α(O@S, O@S') = 1 vacuously by typing alone. Under (M4) the equality of substrate-induced operator-image kernel-substructures becomes the load-bearing structural content of R_α.

   **Exact (M4) vs operational tolerance-relative (M4)_ε.** The mathematical statement above asserts **exact** sub-Markov-kernel equality K_S^ι = K_{S'}^ι. In any empirical verification (Test 16.2b step 4'), exact equality is unattainable from finite-sample estimators; the operational test uses a **tolerance-relative variant (M4)_ε**: K_S^ι and K_{S'}^ι are declared equal to within an operator-class-specific tolerance ε > 0 measured under a declared distance (TV per fixed s, KL summed against ν_s, or Wasserstein on Σ × Σ — Test 16.2b step 4' details). Exact (M4) is the mathematical ideal that the categorical primitive R_α refers to; (M4)_ε is the operational proxy that empirical verification can discharge. Throughout the paper, references to (M4) without subscript denote the exact axiom; (M4)_ε explicitly denotes the empirical-tolerance variant used in Test 16.2b reports. The conditions under which (M4)_ε convergence to exact (M4) is uniform in sample size are collected as a **named regularity hypothesis (Reg-M4)**, to be cited wherever an empirical (M4)_ε-pass is promoted to the categorical claim R_α = 1:

**(Reg-M4) — empirical-to-exact bridge for the anchor test.** (a) the operator-image log-density log(dK_S^ι / dK_{S'}^ι) is uniformly bounded on the chosen comparison support; (b) the estimator class for K_S^ι, K_{S'}^ι is a Glivenko–Cantelli class for the declared distance (TV per fixed s / KL-against-ν_s / Wasserstein on Σ × Σ), so the empirical sub-kernel estimates converge uniformly; (c) the sample size meets the concentration budget fixing ε_stat below the declared ε_op (Test 16.2b three-tolerance block).

Under (Reg-M4) the empirical-tolerance verdict (M4)_ε converges to exact (M4) uniformly in sample size, and a Test 16.2b pass at resolution (ε_stat, ε_op) discharges the categorical R_α-claim; absent (Reg-M4), the verdict remains finite-sample / tolerance-relative and must be reported as «R_α,ε-pass», never as categorical «R_α = 1» (cf. the §16.0 reporting-vocabulary convention). (Reg-M4) is a regularity hypothesis on the estimator/substrate pair, outside the formal core; Theorem 10.6's Completeness direction is stated relative to it.

   **Design choice — substrate-induced K_S^ι, not policy-induced K_S^{π_O, ι}.** (M4) compares the *substrate-induced* sub-Markov-kernel K_S^ι, which captures how the ambient substrate physics realises operator-image transitions independently of operator policy choice. An alternative would constrain the *policy-induced* operator-image sub-Markov-kernel K_S^{π_O, ι} — the kernel that integrates a chosen π_O (Def. 7.3) against the substrate kernel and projects to Σ — yielding a weaker, policy-dependent anchor relation. Two design considerations select the substrate-induced version: (i) operator-position O = (Σ, F_Σ, Α, Φ, α) is *substrate-independent* by Def. 1.1, so the anchor relation across deployments should compare substrate-side realisation rather than policy-side behaviour, otherwise an operator could «pass anchor» on a substrate whose dynamics differ from the operator's specification simply by selecting a policy that compensates; (ii) policy-induced equality is weaker and admits policy-mediated illusion of persistence — two deployments with substantially different substrate physics but compatible operator policies could satisfy K_S^{π_O, ι} = K_{S'}^{π_O, ι} without sharing operator-image substrate structure. The framework's anchor relation aims at structural persistence beneath policy adaptation, hence the substrate-induced choice. A weaker «policy-anchored» variant R_α^π using K_S^{π_O, ι} equality is a coherent alternative formalism and is recorded as an open variant in §18 architectural alternatives; the present work commits to substrate-induced (M4) as the load-bearing structural anchor.

Composition is composition of measurable maps; identity is id_{X_S}. Associativity and identity laws hold by inheritance from the category of measurable maps; (M4) composes by transitivity of equality.

**Lemma 4.1.1.** Dep(O) is a well-defined category. □ (Routine verification — (M4) composes by transitivity of sub-kernel equality on Σ; identity morphism trivially satisfies K_S^ι = K_S^ι.)

**Example 4.1.2 (non-vacuous (M4) on heterogeneous substrates — toy two-state construction).** Let Σ = {a, b}, F_Σ = 2^Σ. Take X_S = {a, b, c} and X_{S'} = {a, b, d} as two distinct three-state ambient spaces with shared symbols {a, b} for the operator-image and disjoint substrate-complement singletons {c} and {d}. Let ι_S(a) = a, ι_S(b) = b ⊂ X_S; symmetrically ι_{S'}(a) = a, ι_{S'}(b) = b ⊂ X_{S'}. Pick parameters p, q ∈ (0, 1) with p + q < 1, and define:

* K_S(a, ·): K_S(a, {a}) = q, K_S(a, {b}) = p, K_S(a, {c}) = 1 − p − q;
* K_S(b, ·): K_S(b, {a}) = p, K_S(b, {b}) = q, K_S(b, {c}) = 1 − p − q;
* K_S(c, ·): a chosen distribution on X_S (e.g., concentrated on {a}: K_S(c, {a}) = 1).

Take μ_S as the unique stationary distribution of K_S — exists and is unique because K_S is an irreducible Markov chain on the finite state-space X_S = {a, b, c} (operator-image-internal symmetry between a and b under K_S, combined with K_S(c, {a}) = 1 returning to operator-image, yields irreducibility). Define K_{S'} symmetrically with {d} in place of {c} and a *different* substrate-complement law K_{S'}(d, ·) (e.g., K_{S'}(d, {b}) = 1, contrasting with K_S(c, {a}) = 1). Take μ_{S'} as the unique stationary distribution of K_{S'} on X_{S'}. Then K_S^ι and K_{S'}^ι are identical sub-Markov kernels on Σ × Σ: both have K^ι(a, {a}) = K^ι(b, {b}) = q, K^ι(a, {b}) = K^ι(b, {a}) = p, mass deficit 1 − p − q at each state. (M4) is satisfied.

But K_S^{rev}(a, ·) and K_{S'}^{rev}(a, ·) restricted to operator-image differ: time-reversal at a ∈ ι_S(Σ) receives mass from substrate-complement point c (where K_S(c, {a}) = 1 in the example), while time-reversal at a ∈ ι_{S'}(Σ) receives no mass from d (where K_{S'}(d, {a}) = 0). Consequently r_{K_S}(a, b) ≠ r_{K_{S'}}(a, b) in general, illustrating that Ψ_S^ι ≠ Ψ_{S'}^ι is compatible with K_S^ι = K_{S'}^ι. This is the explicit obstruction recorded in §4.1 (M3) note and §8.3.

The construction demonstrates that **(M4) component** admits non-trivial instances with genuinely heterogeneous ambient substrates — different ambient spaces, different complement dynamics, different inflow patterns into operator-image — while equating the operator-image-restricted forward sub-Markov-kernels. The construction *does not* by itself demonstrate non-vacuity of the full R_α/T1 anchor relation: R_α/T1 additionally requires (M3) cost preservation (substrate-realised Ψ-equality at the operator-image), which in this example is *not* automatically satisfied — the differing complement inflow patterns into operator-image yield Ψ_S^ι ≠ Ψ_{S'}^ι in general, so (M3) at the Ψ-layer may fail. Full R_α/T1 non-vacuity additionally requires either: (a) choosing K_S(c, ·) and K_{S'}(d, ·) so that the induced K_S^{rev} and K_{S'}^{rev} agree on the operator-image (symmetric complement-inflow), or (b) restricting attention to the Φ-axiom layer of (M3) where both sides equal Φ(s, t) by construction and the Ψ-layer is not separately verified. Example 4.1.2 therefore establishes (M4) non-vacuity on heterogeneous substrates and exhibits the explicit obstruction to (M3) automaticity; full R_α/T1 non-vacuity is conditional on jointly satisfying (M3) and (M4), which in heterogeneous-substrate settings typically requires additional structural alignment beyond what (M4) alone supplies. The Σ-intrinsic content of (M4) is the load-bearing structural anchor at the kernel layer; ambient differences are absorbed by the Dep^{img}(O) quotient; (M3) at the substrate-realised cost layer is an independent constraint and must be separately verified.

**Example 4.1.3 (worked finite-state example — full R_α/T1 + D + τ by explicit computation).** A concrete construction simultaneously satisfying (M3), (M4), D_θ > 0, and τ_θ ≥ L·δ by computation rather than stipulation — closing the gap noted in Example 4.1.2 between (M4) non-vacuity and full R_α/T1 non-vacuity, and providing the worked example whose absence §18 acknowledges as open work.

**Setup.** Σ = {a, b}, F_Σ = 2^Σ. **One-directional admissibility:** A_a = {a, b}, A_b = {b} — operator may stay at a, move a → b, or stay at b; b → a is inadmissible. No round-trip-admissible pair exists, so (Φ4) is vacuously satisfied with ε_O undefined. Ambient spaces X_S = {a, b, c}, X_{S'} = {a', b', d} with ι_S(a) = a, ι_S(b) = b, ι_{S'}(a) = a', ι_{S'}(b) = b'; substrate-complements {c}, {d}.

**Substrate kernels.**

| source ↓ \ target → | a / a' | b / b' | c (in S) / d (in S') |
|---|---|---|---|
| K_S(a, ·) | 0.2 | 0.4 | 0.4 |
| K_S(b, ·) | 0.1 | 0.5 | 0.4 |
| K_S(c, ·) | 0.1 | 0.1 | 0.8 |
| K_{S'}(a', ·) | 0.2 | 0.4 | 0.4 |
| K_{S'}(b', ·) | 0.1 | 0.5 | 0.4 |
| K_{S'}(d, ·) | 0.4 | 0.4 | 0.2 |

(M4) holds by construction: K_S^ι(s, B) = K_{S'}^ι(s, B) on all (s, B) ∈ Σ × F_Σ — the operator-image-restricted rows of K_S and K_{S'} are identical, with mass deficit 1 − K^ι(s, Σ) = 0.4 on both deployments. Substrate-side allows K_S(b, a) = 0.1 > 0 (b → a probabilistically possible at the kernel layer); strict hard-support (R4) is *softened* to **policy-level inadmissibility** per §8.2 (R4) Scope — the operator policy refuses b → a even though substrate kinetics permits it. This is the canonical compromise §8.2 anticipates.

**Stationary measures** (solving μK = μ): μ_S(a) = 1/9, μ_S(b) = 2/9, μ_S(c) = 6/9; μ_{S'}(a') = 2/9, μ_{S'}(b') = 4/9, μ_{S'}(d) = 3/9. Different absolute complement masses (6/9 vs 3/9) reflect distinct complement dynamics (K_S(c, c) = 0.8 vs K_{S'}(d, d) = 0.2). The **load-bearing alignment** is preservation of the operator-image ratio ρ := μ(a)/μ(b) = 1/2 on both deployments — a consequence of the symmetric complement-to-image transitions K_S(c, a)/K_S(c, b) = K_{S'}(d, a')/K_{S'}(d, b') = 1.

**Time-reversal at operator-image** (discrete §0.5 disintegration: K^{rev}(x, y) = K(y, x)·μ(y)/μ(x)) and **Ψ-values**:

| (s, t) ∈ Σ × Σ | K_S(s, t) | K_S^{rev}(s, t) | Ψ_S(s, t) | K_{S'}(s, t) | K_{S'}^{rev}(s, t) | Ψ_{S'}(s, t) |
|---|---|---|---|---|---|---|
| (a, a) | 0.2 | 0.2 | 0 | 0.2 | 0.2 | 0 |
| (a, b) | 0.4 | 0.2 | log 2 ≈ 0.693 | 0.4 | 0.2 | log 2 ≈ 0.693 |
| (b, b) | 0.5 | 0.5 | 0 | 0.5 | 0.5 | 0 |

**(M3) verified at operator-image admissible transitions.** With ν_s = counting measure on A_s, the only non-self admissible transition is (a, b). Ψ_S(a, b) = Ψ_{S'}(a, b) = log 2 ⟹ M3 Ψ-equality at operator-image admissible transitions holds. Set Φ(a, b) := log 2 ν_a-a.e., satisfying R3 + (Φ2) strictly (Φ > 0 on admissible non-self). The values Ψ_S(b, a) = −log 2 are computable but lie outside the ν_b-comparison scope (since a ∉ A_b), so they do not violate (Φ2). The reverse-kernels' complement-inflow components differ (K_S^{rev}(a, ·) receives mass from c, K_{S'}^{rev}(a, ·) from d), yet the operator-image-restricted reverse-kernel values *coincide* on (a, b) and (b, a) because the K^{rev} formula reduces to K(t, s)·μ(t)/μ(s) and both K(b, a)/K(b', a') by M4 and μ(b)/μ(a) = μ(b')/μ(a') by ρ-alignment agree. This is the structural alignment §8.3 obstruction warned could fail in general — the construction shows it is achievable.

**Operator policy** (per §7.3 Σ-level realisation block). Abstract Σ-level policy π_Σ : Σ × F_Σ → [0, 1] with π_Σ(a, {b}) = 1, π_Σ(b, {b}) = 1 (deterministic move a → b at first step, then stay at b). Deployment-indexed realisations π_{O,S}(ι_S(s), ι_S(B)) = π_{O,S'}(ι_{S'}(s), ι_{S'}(B)) = π_Σ(s, B); both satisfy (π1) (zero mass outside ι_Y(A_s)) and (π2) on every exercised source step — the a-source move needs K_S(a, {b}) = K_{S'}(a', {b'}) = 0.4 > 0, and the b-source stay-step (operator remains at b after the first transition) needs K_S(b, {b}) = K_{S'}(b', {b'}) = 0.5 > 0; both charge the policy support, so π_O ≪ K on the operator-image at both sources.

**Observation channel.** Z = {0, 1, ⊥}, θ_S(a) = 0, θ_S(b) = 1, θ_S(c) = ⊥; θ_{S'}(a') = 0, θ_{S'}(b') = 1, θ_{S'}(d) = ⊥. Channel-pushed substrate priors (stationary endpoint marginals — under the §0.3 stationary initialisation X_0 ∼ μ_S the post-one-transition X_1 marginal is μ_S K_S = μ_S by *stationarity*, so the stationary one-time marginal serves as the endpoint baseline; this is the stationarity property μK = μ, not irreducibility, which only fixes uniqueness of μ): **P_S^θ = (1/9, 2/9, 6/9)**, **P_{S'}^θ = (2/9, 4/9, 3/9)** on (0, 1, ⊥).

**D-test (T2).** *Horizon convention:* both Q and the substrate priors are compared as **endpoint marginals after one transition** on Z — the last-step (X_1) marginal of the two-time trajectory law on (X_0, X_1). In the §0.3 / Def. 7.2 convention where P_K^{(n)} is the law of (X_0, …, X_{n−1}), this is trajectory-length n = 2 with endpoint-index m = 1 (the endpoint-index is distinct from the trajectory-length; «one transition» means m = 1, not n = 1). Q_I^{θ, during} is the operator-driven endpoint (X_1) marginal after one transition from initial operator-state a'; the substrate priors P_S^θ, P_{S'}^θ are the corresponding stationary endpoint marginals (under stationary initialisation X_0 ∼ μ_S the X_1 marginal is μ_S K_S = μ_S by stationarity — the stationary marginal serves as the substrate-endpoint baseline). During-phase law starting from initial operator-state a' under π_{O,S'}: the deterministic policy moves to b', channel-pushed to Z = 1. Hence **Q_I^{θ, during} = δ_1** ∈ 𝒫(Z). Compute:

D_{KL}(Q ‖ P_S^θ) = log(1/(2/9)) = log(9/2) ≈ 1.504 nats.
D_{KL}(Q ‖ P_{S'}^θ) = log(1/(4/9)) = log(9/4) ≈ 0.811 nats.

**D_θ = log(9/2) − log(9/4) = log 2 ≈ 0.693 nats > 0** ✓ (priors-inversion verified).

**τ-test (T3) with (N-quant) and (R).** Set s_pre = a, s_post = b on the operator-image (the operator's internal state shifts from a to b during the displacement — the operator-image trace of the transposition). Discrete metric d_Σ on Σ with d_Σ(a, b) = 1; (R) holds with **δ = 1**. Take response distributions R_O^θ(·|a) = δ_0, R_O^θ(·|b) = δ_1 — these are the *configuration-conditioned* forms of Def. 13.0; since θ_S ∘ ι_S is injective here (θ_S(a) = 0 ≠ 1 = θ_S(b)), they coincide with the channel-value-conditioned forms and the (N-quant) typing is unambiguous. Then ‖R_O^θ(·|a) − R_O^θ(·|b)‖_{TV} = 1 = 1·d_Σ(a, b), giving (N-quant) modulus **L = 1**. The post-interval trace **τ_θ = ‖R_O^{post}(·|b) − R_O^{pre}(·|a)‖_{TV} = ‖δ_1 − δ_0‖_{TV} = 1 ≥ L·δ = 1** ✓.

**Verdict — full true transposition per Def. 6.1.** All three conditions (T1) + (T2) + (T3) hold by explicit computation:

- (T1) R_α(O@S, O@S') = 1 via canonical operator-image bijection f(ι_S(s)) := ι_{S'}(s), satisfying (M1) by construction, (M2) admissibility-mapping consistent under f (the operator-image admissibility-set structure transports identically: f(ι_S(A_a)) = ι_{S'}(A_a), f(ι_S(A_b)) = ι_{S'}(A_b)), (M3) Ψ-equality on operator-image admissible transitions (table above; load-bearing alignment via ρ-preservation), (M4) sub-Markov-kernel equality on Σ × Σ (rows identical);
- (T2) D_θ ≈ 0.693 > 0;
- (T3) τ_θ = 1 ≥ L·δ = 1, with (R) δ = 1 and (N-quant) L = 1.

The candidate T̃ : O@S → O@S' passes (P1)–(P3) of Theorem 10.6 at zero empirical tolerance — this is an exact-arithmetic finite-state example, so ε_op = ε_stat = 0 < ε_adv for any positive adversarial gap on the operator-class. (P4) per-operator observability is trivially satisfied in the single-operator finite-state setting. **Regime note:** this is a *softened-(R4)* deployment — the substrate permits b → a with K_S(b, a) = 0.1 while the operator policy refuses it (policy-level inadmissibility) — so it instantiates the softened-(R4) one-directional regime of Remark 8.4.1, the only regime supporting finite non-trivial canonical Ψ-realisation. It is **not** a hard-support-(R4) instance; the example demonstrates non-vacuity for the softened-(R4) variant that the §10–§11 standing assumption (as qualified by Remark 8.4.1) actually operates in, not for a hard-support-(R4) framework.

**Scope of the demonstration.** The full R_α/T1 + D + τ test bundle is **definitionally non-empty**: at least one finite-state construction passes all four *sub-conditions* — (M3), (M4), D_θ > 0, τ_θ > 0 (the components listed at the head of this example, with (M3)+(M4) jointly constituting the (T1) anchor of the three Def. 6.1 conditions) — by explicit computation, not stipulation. The construction relies on (i) chosen complement dynamics preserving ρ = μ(a)/μ(b) = 1/2 across both deployments (the load-bearing alignment making (M3) hold at operator-image despite different absolute complement-mass scales — exactly the alignment §8.3 obstruction warned could fail), and (ii) one-directional admissibility A_b = {b}, which avoids the strict-(Φ2)-on-round-trip impossibility theorem (for any Markov kernel admitting both s → t and t → s admissibly with finite Ψ, Ψ(s, t) and Ψ(t, s) sum to log[K(s,t)K(t,s)/K(t,s)K(s,t)] = 0, so they cannot both be strictly positive — a fundamental constraint on Φ-realisation under round-trip admissibility). Realistic heterogeneous-substrate deployments where ρ-alignment fails do not automatically inherit M3; the per-mechanism protocol (Test 16.2b step 4) is needed for empirical verification. The example demonstrates **conditional non-vacuity** of the test bundle, not generic substrate-realisability of operator-mobility — that remains an empirical question per §18.

### Definition 4.2 (anchor-persistence relation R_α — categorical primitive)

For deployments O@S, O@S' ∈ Ob(Dep(O)), define R_α as follows.

**Construction via the operator-image quotient category Dep^{img}(O).** From Dep(O) construct Dep^{img}(O) with:

* same objects as Dep(O);
* morphisms f, g : O@S → O@S' are *identified* in Dep^{img}(O) whenever f|_{ι_S(Σ)} = g|_{ι_S(Σ)} (i.e., morphisms are quotiented by the equivalence "agree on operator-image");
* identity is the equivalence class of id_{X_S}; composition descends from Dep(O) provided the equivalence ~ is a *congruence*.

The equivalence ~ defined by «agree on operator-image» is a congruence on Dep(O): if f_1 ~ f_2 : O@S → O@S' and g_1 ~ g_2 : O@S' → O@S'', then g_1 ∘ f_1 ~ g_2 ∘ f_2 : O@S → O@S''. For s ∈ Σ, f_1(ι_S(s)) = f_2(ι_S(s)) = ι_{S'}(s) by (M1) applied to f_1, f_2; then g_1(ι_{S'}(s)) = g_2(ι_{S'}(s)) by g_1 ~ g_2; hence (g_1 ∘ f_1)(ι_S(s)) = (g_2 ∘ f_2)(ι_S(s)) for every s ∈ Σ. The congruence makes Dep^{img}(O) well-defined as a category.

**R_α definition.**

**R_α(O@S, O@S') = 1**    iff    O@S and O@S' are isomorphic in Dep^{img}(O).

Equivalently (unfolding the quotient): there exist Dep(O)-morphisms f : O@S → O@S' and g : O@S' → O@S with (g∘f)|_{ι_S(Σ)} = id_{ι_S(Σ)} and (f∘g)|_{ι_{S'}(Σ)} = id_{ι_{S'}(Σ)} — i.e., the operator-images are interchanged invertibly.

**Lemma 4.2.1.** The operational content of R_α(O@S, O@S') = 1 is: the operator-images ι_S(Σ) and ι_{S'}(Σ) are isomorphic as cost-respecting, admissibility-respecting, **Markov-substructure-respecting** measurable sub-objects of (X_S, F_S, K_S) and (X_{S'}, F_{S'}, K_{S'}) respectively, where "isomorphic" means there is a measurable bijection between them whose forward and inverse maps preserve (M1)–(M4). The independent structural content lies in (M3) and (M4) jointly: (M3) cost-equality on operator-image admissible transitions and (M4) Σ-intrinsic sub-Markov-kernel equality. (M1) fixes the bijection on operator-images by typing; (M2) is derived. (M3) and (M4) are *not* mutually derivable from each other in general: (M4) constrains substrate-induced operator-image outflow but not substrate-complement inflow (which time-reversal at operator-image requires for Ψ-equality), so substrate-realised cost equality requires (M3) as an independent axiom. Together (M3)+(M4) distinguish R_α-iso from a typing artefact: without (M4), canonical operator-image bijection trivially satisfies (M1) and (M3) (both sides equal Φ by (D2)); (M4) adds substantive substrate-kernel content that the typing alone does not supply. □

### Theorem 4.3 (R_α is an equivalence relation)

R_α is reflexive, symmetric, and transitive on Ob(Dep^{img}(O)) = Ob(Dep(O)).

**Proof.** R_α is defined as the isomorphism relation in the category Dep^{img}(O) (Def. 4.2). For any category C, the relation "there exists an isomorphism A → B in C" is an equivalence on Ob(C) (§0.6): reflexivity by id, symmetry by inversion of iso, transitivity by composition. Since Dep^{img}(O) is a well-defined category (Def. 4.2), the equivalence properties of R_α follow. Concretely:

*Reflexivity.* [id_{X_S}] : O@S → O@S in Dep^{img}(O) (the equivalence class of id_{X_S}) is invertible (its own inverse). Hence R_α(O@S, O@S) = 1.

*Symmetry.* If [f] : O@S → O@S' is an isomorphism in Dep^{img}(O), its categorical inverse [g] : O@S' → O@S satisfies the iso conditions in the opposite direction. Hence R_α is symmetric.

*Transitivity.* If [f] : O@S → O@S' and [h] : O@S' → O@S'' are isos in Dep^{img}(O), then [h]∘[f] : O@S → O@S'' is an iso (composition of isos in any category). Hence R_α(O@S, O@S'') = 1. □

Theorem 4.3 grounds R_α as a primitive of the formalism: it is not assumed to be an equivalence — it is *derived* as one because Dep^{img}(O) is a category and isomorphism-equivalence holds in any category.

### §4.4 Enrichment of Dep(O) — status note

A natural strengthening of Dep(O) is enrichment over the monoidal category (ℝ_{≥0}, +, 0) following Lawvere 1973, with morphism-cost grading via the substrate-realised irreversibility production Ψ_S. **This enrichment is not constructed here.** Three structural obstacles prevent a load-bearing enrichment under the current framework:

1. **Cost-source assignment.** A morphism-cost c_f naturally bound to the source-deployment via Σ_{s ∈ Σ, t ∈ A_s} Ψ_S(ι_S(s), ι_S(t)) (sum over operator-image admissible-transition pairs) does not depend on f — distinct morphisms in the same hom-set receive identical cost. Genuine morphism-grading requires a cost-functional that depends on the morphism's action (e.g., target-image cost minus source-image cost), which under (M3) cost preservation (§4.1) collapses to zero across all morphisms.

2. **Identity morphism.** The identity id_{X_S} has the same source-bound cost as any other morphism O@S → O@S; under "enriched iso iff c_f = 0", id would fail to be an enriched isomorphism unless source-cost = 0 (trivial operators only). The naive enrichment breaks the category axiom that identities are isomorphisms.

3. **(M3) collapse.** Under (M3) cost preservation — retained as an independent morphism axiom alongside (M4) (since substrate-realised cost equality is not derivable from operator-image sub-kernel equality alone; see §4.1 (M3) note) — costs are equal across morphisms in any hom-set. Enrichment under the resulting constant cost is vacuous — it grades nothing new beyond what (M3)/(M4) already fix.

A load-bearing enrichment would require either relaxing (M3)/(M4) to inequality (cost-decreasing or sub-kernel-dominated morphisms) and grading by cost-loss or kernel-deficit; or enriching over a richer structure (2-categories, profunctors, sheaves) that captures additional morphism-data; or using a relative cost-functional carefully constructed to satisfy c_id = 0 and non-trivial sub-additivity. We do not pursue these here. The categorical content of the paper rests on the plain Dep^{img}(O) quotient of §4.2 and the equivalence of Theorem 4.3, with (M3) and (M4) jointly supplying the load-bearing structural content of R_α; the morphism-cost layer is left as an open extension (cf. §18.(b)).

---

## §5. Operator-form

### Definition 5.1 (operator-form)

The *operator-form* of O is the R_α-equivalence class

**[O]_α := { O@S : S ∈ Adm(O), R_α(O@S, O@S₀) = 1 }**    (for any chosen base S₀ ∈ Ob(Dep(O)))

The base S₀ exists iff Adm(O) ≠ ∅. If Adm(O) = ∅ (no substrate admits a deployment of O), the operator has no realised form: [O]_α is undefined-as-nonempty and the partition of Ob(Dep(O)) in Theorem 10.1 is the empty partition. The form is well-defined exactly on operators with at least one admissible deployment.

equivalently, the connected component of O@S₀ in the underlying groupoid of Dep^{img}(O) (i.e., the subcategory Dep^{img}(O)^{iso} consisting of all objects and only the isomorphisms in the quotient category Def. 4.2). Well-definedness independent of base choice follows from Theorem 4.3 (R_α equivalence).

### Remark 5.2 (well-posedness; absence of circularity)

The construction is logically grounded: operator-form rests on R_α, which is defined as isomorphism in Dep^{img}(O) (Def. 4.2). Dep(O) and its quotient Dep^{img}(O) are constructed independently of any transposition concept — their morphisms are admissibility-respecting and cost-respecting measurable maps; nothing about "transposition" enters their definition. Theorem 4.3 derives the equivalence property from category-theoretic axiomatics, not assumes it. Transposition (next section) is then *defined in terms of* R_α (via isomorphisms in Dep^{img}(O)), not the other way around — avoiding the circularity that would arise from defining operator-form via existence of transposition while transposition is required to preserve operator-form.

---

## §6. Transposition

### Definition 6.1 (transposition)

A *transposition* of O is a **decorated Dep^{img}(O)-isomorphism**:

**[T] : O@S → O@S'**    in **Dep^{img}(O)** (the operator-image quotient category of Def. 4.2),

together with a declared operational representative

**(I, W, π_{O,S}, π_{O,S'}, θ, Q_I^{θ,during}, Q_W^{θ,post})**

— during-interval I (Def. 9.0), post-interval trace window W (Def. 13.2), deployment-indexed operator policies π_{O,S} on O@S and π_{O,S'} on O@S' (each satisfying (π1)+(π2) of Def. 7.3 on its own substrate, *jointly operator-coherent* across f per §7.3's «Deployment-indexed typing» block), observation channel θ (Def. 7.1), and induced operator-driven laws on the channel for the during phase (D-test input per (T2)) and post phase (τ-test input per (T3)) — and satisfying the additional channel-dependent conditions (T2) and (T3) below. When the text writes Q^θ_I without phase-subscript, the relevant phase is fixed by context (D_θ of Def. 7.4 uses Q_I^{θ,during}; τ_θ of Def. 13.2 uses Q_W^{θ,post}).

**Unpacking the isomorphism condition (T1).** Isomorphism in Dep^{img}(O) is *equivalent* to:

(T1) **anchor preservation** — R_α(O@S, O@S') = 1: there exist Dep(O)-morphisms f, g whose restrictions to operator-images are mutually inverse on ι_S(Σ) ↔ ι_{S'}(Σ), with sub-Markov-kernel equality K_S^ι = K_{S'}^ι per (M4) of Def. 4.1.

(T1) is the structural anchor content of «[T] is an isomorphism in Dep^{img}(O)»; it is not an additional axiom imposed on top of the isomorphism — it is what the isomorphism *means*. We list it as a labelled condition only because it is referenced separately throughout §§7–16 (e.g., «(T1) failure» as a classification verdict; «R_α/T1 isomorphism check» as Test 16.2b).

**Additional channel-dependent conditions** (these *are* extra content on top of the bare Dep^{img}(O)-isomorphism):

(T2) **priors inversion** — for the declared observation channel θ, the priors-dominance index D_θ(T) is strictly positive (Def. 7.4);

(T3) **non-hallucinated structural trace** — under the non-degeneracy hypothesis (N) of Proposition 10.2, the post-interval structural trace τ_θ(O, S') of Def. 13.2 is strictly positive over the declared post-interval observation window.

A transposition is required to be an isomorphism only at the operator-image level (Dep^{img}(O)), not a substrate-wide measurable bijection between (X_S, F_S, K_S) and (X_{S'}, F_{S'}, K_{S'}). Substrate-wide isomorphism is generally impossible between heterogeneous substrates (different state-space dimension, different stationary dynamics, etc.) — the whole point of the framework is that transposition preserves operator-identity across different substrates whose ambient physics differ. Requiring Dep(O)-isomorphism literally would make transposition between genuinely different substrates artificially impossible; Dep^{img}(O)-isomorphism is the correct level at which the structural requirement (M1)–(M4) applies. By Def. 4.2, Dep^{img}(O) quotients morphisms by «agree on operator-image»; isomorphism in this quotient is precisely operator-image-restricted invertibility plus (M4) sub-Markov-kernel equality, which is what (T1) demands.

Condition (T1) is structural and free of observation channel. Condition (T2) is *observational*: it depends on a chosen channel θ and may differ across channel choices. Condition (T3) is operational-structural — it constrains the operator-image configuration at end-of-interval via a measurable response-distribution shift under (N). Hence the full transposition relation combines structural persistence (T1), channel-relative priors inversion (T2), and post-interval residue (T3); R_α-equivalence of Def. 4.2 covers (T1) alone and is channel-free.

**Convention.** «True transposition in the sense of Def. 6.1» throughout §10–§19 means a candidate satisfying all of (T1)–(T3). Candidates failing any sub-condition are classified per §13 failure-mode predicates: D-test failure (¬T2) ⇒ mock-transposition; D-undefined / non-comparable under θ (Def. 7.4 dual-singular case) ⇒ non-comparable-under-θ (channel refinement required); T1 failure under D-positive ⇒ anchor failure; τ-test failure under (N) and D-positive ⇒ hallucinated; τ-test failure under ¬(N) and D-positive ⇒ non-identifiable under θ. The Proposition 10.2 conditional «non-hallucinated D-positive candidate» (D > 0 ∧ τ > 0 under (N)+(R)) refers to the (T2)+(T3) layer alone; full transposition additionally requires (T1) via the R_α/T1 structural-isomorphism check of Test 16.2b.

**Reference convention (bare class vs decorated representative).** Following the typing fixed in Def. 6.1 above: «a transposition T» or «[T] : O@S → O@S'» denotes the decorated representative when (T2)/(T3) verdicts are at stake, and the bare Dep^{img}(O)-isomorphism class when only (T1) is at stake. The R_α-equivalence of Def. 4.2 alone is channel- and representative-free; the full transposition relation of Def. 6.1 is representative-decorated.

**Computational invariance of D_θ on a representative ([T] vs T).** Although [T] is a Dep^{img}(O)-equivalence class (Def. 4.2 quotient), the priors-dominance index D_θ([T]) is computed from the **declared operational representative** of [T] — specifically, the effective interval I (Def. 9.0) and the operator-driven observation law Q^θ_I (Def. 7.3) realised under that representative's policy and substrate-coupling. D_θ is **invariant under** representatives of [T] that (a) agree on the operator-image (i.e., are quotient-equivalent in Dep^{img}(O)) AND (b) induce the same operator-driven observation law Q^θ_I on the channel. Different representatives that yield different Q^θ_I (e.g., differ in policy on the substrate-complement, leading to different observation-marginals) can in principle yield different D_θ-values; in such cases D_θ([T]) is understood as the family of admissible values across the equivalence class, with each measurement report (per §16) declaring the specific representative used. The categorical object [T] does not by itself determine D_θ; the *(representative-with-declared-interval-and-policy)* does.

---

## §7. The priors-dominance index D on a common observation channel

Computing D_{KL} between substrate-priors on different state spaces (X_S vs X_{S'}) is ill-defined when the σ-algebras differ. The resolution: define D *relative to an observation channel*, which pushes both substrate priors onto a common observable space.

### Definition 7.1 (observation channel)

An *observation channel* for substrates S = (X_S, F_S, μ_S, K_S) and S' = (X_{S'}, F_{S'}, μ_{S'}, K_{S'}) is a pair of measurable maps

**θ_S : (X_S, F_S) → (Z, G)    and    θ_{S'} : (X_{S'}, F_{S'}) → (Z, G)**

where (Z, G) is a standard Borel measurable space — the *observation space*. We write θ for the pair (θ_S, θ_{S'}) and call (Z, G) the *common observation space*.

Channel choices are not unique; different θ may yield different D-values for the same T. Discipline: the channel must be declared in any D-measurement (cf. §16 Test 16.1).

### Definition 7.2 (pushforward priors on Z)

Given observation channel θ:

**P_S^θ := (θ_S)_* P_S    on (Z^ℕ, G^{⊗ℕ})**;
**P_{S'}^θ := (θ_{S'})_* P_{S'}    on (Z^ℕ, G^{⊗ℕ})**.

These are well-defined pushforwards of the substrate-prior trajectory laws. Both live on the common observation space.

**Finite-horizon convention.** For a finite effective interval I of length n (per Def. 9.0), the finite-horizon counterparts are

**P_{S,n}^θ := (θ_S)_* P_S^{(n)}    on (Z^n, G^{⊗n})**;
**P_{S',n}^θ := (θ_{S'})_* P_{S'}^{(n)}    on (Z^n, G^{⊗n})**.

All KL computations in D_θ over an interval I are performed against these **finite-horizon priors** P_{S,n}^θ, P_{S',n}^θ on (Z^n, G^{⊗n}) — matching the horizon of Q^θ_I (Def. 7.3). The infinite-horizon laws P_S^θ, P_{S'}^θ on (Z^ℕ, G^{⊗ℕ}) are reserved for asymptotic / long-horizon statements (e.g., Sanov-type bounds in Remark 7.7); they are *not* used directly inside finite-horizon D_θ. Unless otherwise stated, P_S^θ in §7.4 onward abbreviates P_{S,n}^θ for the horizon n fixed by the effective interval.

### Definition 7.3 (operator policy and operator-driven law)

An *operator policy* on deployment O@S is a Markov kernel π_O : X_S × F_S → [0, 1] satisfying both:

**(π1) Admissibility-support condition.** For each s ∈ Σ,

  **π_O(ι_S(s), X_S \ ι_S(A_s)) = 0**

— equivalently, for every measurable B disjoint from ι_S(A_s) we have π_O(ι_S(s), B) = 0, so all outgoing mass from ι_S(s) is concentrated on the image of the operator's admissibility set ι_S(A_s) ⊂ X_S. (The weaker condition «π_O(ι_S(s), B) > 0 implies B ∩ ι_S(A_s) ≠ ∅» is *not* equivalent — a measurable set B may both intersect ι_S(A_s) and carry policy mass located outside ι_S(A_s), violating concentration; the zero-complement-mass formulation above is the correct support condition.)

**(π2) Substrate-dominance condition.** For each s ∈ Σ,

  **π_O(ι_S(s), ·) ≪ K_S(ι_S(s), ·)**

— the policy's transition distribution from any operator-image state is absolutely continuous with respect to the substrate kernel's transition distribution from that same state. Equivalently: π_O does not place mass on transitions of K_S-measure zero (i.e., on transitions the substrate itself never realises with positive probability). The Radon-Nikodym density dπ_O(ι_S(s), ·)/dK_S(ι_S(s), ·) is the *policy refinement factor* — a non-negative measurable function quantifying how the operator reweights substrate-realisable transitions within the admissibility envelope ι_S(A_s).

(π1) without (π2) is insufficient for physical realisability: topological support of K_S on ι_S(A_s) (Def. 3.2 D1 atomless case) ensures only that *some* substrate trajectory passes near each admissible target, not that the operator's policy distribution is actually generated by the substrate kernel. Without (π2), Q^θ_I in §7.4 below could describe a policy-imposed trajectory that the substrate kernel never realises with positive probability — divorcing the operator-driven law from substrate dynamics. (π2) closes this gap: the operator-driven trajectory law is a *reweighting* of substrate-realisable transitions, not a free-floating Markov chain on the operator-image.

Under both (π1) and (π2) the policy *refines* the substrate kernel: π_O selects, among substrate-realisable transitions, those compatible with the operator's admissibility gate Α and (in canonical Φ-realising deployments) those that incur the operator-specified Φ-cost.

**Compatibility with the admissibility set in atomless substrates.** For continuous-state substrates (Def. 3.2 D1 atomless case) where ι_S(A_s) may be K_S-null at the singleton level but supp-positive at the neighbourhood level, (π2) is consistent with (π1) only when K_S(ι_S(s), ι_S(A_s)) > 0 — i.e., the substrate kernel charges the operator's admissibility envelope with positive mass. This is an additional regularity condition implicit in the joint statement of (π1)+(π2); deployments violating it have no admissible policy in the present framework. The required condition is **K_S(ι_S(s), ι_S(A_s)) > 0** for each s ∈ Σ; the canonical reference measure ν_s of §8 makes this a substrate-property check at deployment time.

**Deployment-indexed typing.** Definition 7.3 above types π_O on the specific deployment O@S — i.e., π_O : X_S × F_S → [0, 1] tied to the substrate state space X_S. For analyses involving transposition T : O@S → O@S' across two deployments, *two* distinct deployment-indexed policies are required: **π_{O,S} : X_S × F_S → [0, 1]** for pre/post phases (operator anchored in S) and **π_{O,S'} : X_{S'} × F_{S'} → [0, 1]** for the during phase (operator-image embedded in S'). Each must independently satisfy (π1)+(π2) on its own deployment.

**Operator-coherence (Σ-level realisation).** Formally: there exists a Markov kernel **π_Σ : Σ × F_Σ → [0, 1]** (the *abstract Σ-level operator policy*) with support in A_s for each s ∈ Σ, such that for each deployment Y ∈ {S, S'} and for all s ∈ Σ, B ∈ F_Σ,

**π_{O,Y}(ι_Y(s), ι_Y(B)) = π_Σ(s, B)**

(equality holding in the (π1)+(π2) declared a.e. convention on the operator-image admissibility set ι_Y(A_s)). The deployment-indexed policies π_{O,S} and π_{O,S'} are then *realisations* of the same Σ-level policy π_Σ through the two deployments' embeddings ι_S and ι_{S'} respectively; operator-coherence across the transposition is precisely this shared π_Σ existence. When the text writes «π_O» without subscript, the deployment is fixed by context: «π_O on deployment O@S» refers to π_{O,S}; the during-phase law Q_I^{during} on (X_{S'}, F_{S'}^{⊗n}) (§7.3 phase stratification below) uses π_{O,S'} composed with K_{S'}, not π_{O,S} composed with K_S.

For a candidate transposition T : O@S → O@S' with claimed effective interval I of length n, the *operator-driven trajectory law during I* lives on a substrate state-space whose identity depends on the *phase* of T relative to I (Def. 9.0's notion of effective interval already references the post-displacement substrate during the transposition's interior). The cleanest formal object is the **observation-space law** on the common channel (Z^n, G^{⊗n}):

**Q^θ_I ∈ 𝒫(Z^n, G^{⊗n})** — the joint law of the operator's realised observation under channel θ during I.

The upstream substrate-state law is *phase-dependent*:

* **Pre-transposition phase** (operator anchored in S): Q_I^{pre} ∈ 𝒫(X_S^n, F_S^{⊗n}), with channel pushforward Q^{θ, pre}_I := (θ_S)_* Q_I^{pre}.
* **During-transposition phase** (operator displaced into S' under T): Q_I^{during} ∈ 𝒫(X_{S'}^n, F_{S'}^{⊗n}), with channel pushforward Q^{θ, during}_I := (θ_{S'})_* Q_I^{during}.
* **Post-transposition phase** (operator returned to S, possibly with residue): Q_I^{post} ∈ 𝒫(X_S^n, F_S^{⊗n}), with channel pushforward Q^{θ, post}_I := (θ_S)_* Q_I^{post}.
* **Mixed-interval cases** (e.g., I spanning a phase transition): the channel pushforward is computed piecewise per phase and concatenated on the observation timeline.

In each phase the upstream law is induced by π_O composed with the *phase-appropriate substrate kernel* (K_S for pre/post, K_{S'} for during).

For the *D_θ-index of Def. 7.4*, Q^θ_I refers to the channel-pushforward of the **during-phase** law Q^{θ, during}_I unless otherwise stated — this is the phase at which a candidate true-transposition is operationally tested (the operator is in S' during I); the pre- and post-phase laws Q^{θ, pre}_I and Q^{θ, post}_I are used in §16 Test 16.1 and the residue/τ-test (§10.2(ii)) respectively. The illustrative duck-example (§15) makes the phase-stratification explicit by labelling each computation with its phase.

In practice, Q^θ_I (per phase) is estimated from a finite sample of phase-restricted I-trajectories via standard density estimation (kernel density, neural density, mechanistic).

### Definition 7.4 (priors-dominance index D_θ)

**Self / foreign convention.** For a transposition T : O@S → O@S', the source substrate S is the *self*-substrate (the substrate from which T departs); the target S' is the *foreign*-substrate (the substrate into which T transposes the operator-image). The priors P_S^θ and P_{S'}^θ are correspondingly the self-substrate prior and foreign-substrate prior on the common observation channel.

For the candidate transposition T with operator-driven law Q^θ_I (Def. 7.3) and channel θ, write `Q^θ_I ≪ P_S^θ` for absolute continuity and `Q^θ_I ̸≪ P_S^θ` (not absolutely continuous) for its negation. The *D_θ index* is defined under one of three regimes:

**Regime A (finite-finite):** Q^θ_I ≪ P_S^θ AND Q^θ_I ≪ P_{S'}^θ AND the Radon-Nikodym log-densities are Q^θ_I-integrable in both directions. Both KL terms are finite real numbers; D_θ ∈ ℝ.

**Regime B (singular self-substrate, finite foreign):** Q^θ_I ̸≪ P_S^θ AND Q^θ_I ≪ P_{S'}^θ with foreign-side log-density Q^θ_I-integrable. Then D_{KL}(Q^θ_I ‖ P_S^θ) = +∞, D_{KL}(Q^θ_I ‖ P_{S'}^θ) finite; D_θ := +∞ — strong positive evidence of foreign-substrate-dominance (operator-driven trajectory lies in events excluded by self-substrate prior).

**Regime C (finite self-substrate, singular foreign):** Q^θ_I ≪ P_S^θ AND Q^θ_I ̸≪ P_{S'}^θ with self-side log-density Q^θ_I-integrable. Then D_θ := −∞ — strong negative (operator-driven trajectory lies in events excluded by foreign-substrate prior).

**Undefined (∞ − ∞ degenerate; or non-integrable):** either Q^θ_I ̸≪ both priors (dual-singular), or absolute continuity holds but log-density fails Q^θ_I-integrability (KL = +∞ for non-singular reason). In either case, T is classified as **non-comparable under θ**; a refined channel (broader common observation space) is required.

In all defined regimes:

**D_θ(T) := D_{KL}(Q^θ_I ‖ P_S^θ) − D_{KL}(Q^θ_I ‖ P_{S'}^θ)**    ∈ ℝ ∪ {+∞, −∞}.

Absolute continuity Q ≪ P alone does not imply finite D_{KL}(Q ‖ P) — finiteness additionally requires the log-density log(dQ/dP) to be Q-integrable. Standard regularity (bounded log-density, exponential-family priors, sub-Gaussian tails) gives integrability; pathological cases (e.g., dQ/dP unbounded on a positive-Q set) can yield D_{KL} = +∞ even under absolute continuity. The "non-integrable" branch of *Undefined* above covers this case.

### Classification under D_θ (D-test verdict only — sub-component of full transposition classification)

The classification labels below report the *D-test verdict* on a candidate transposition T̃ — i.e., whether the operator-driven law under T̃ has inverted its priors-dominance from self-substrate to foreign-substrate on the channel θ. This is one sub-component of Def. 6.1's full transposition classification, which additionally requires the structural R_α/T1 isomorphism check (§6) and (for non-hallucination) the τ-test (Def. 13.2 + Proposition 10.2(ii)).

* **D-test pass / priors-inversion under θ** iff D_θ(T̃) > 0 (Q^θ_I is closer in KL to P_{S'}^θ than to P_S^θ on the common observation space);
* **D-test fail / imitation under θ** iff D_θ(T̃) ≤ 0 (Q^θ_I remains closer to P_S^θ).

A candidate T̃ is classified as a true transposition in the sense of Def. 6.1 iff the D-test passes AND R_α/T1 holds (operator-image isomorphism preserving (M1)–(M4), with (M4) the load-bearing Σ-intrinsic sub-Markov-kernel-equality content per Def. 4.1) AND the τ-test passes (Proposition 10.2(ii), non-hallucination). D > 0 alone is necessary but not sufficient.

### Definition 7.5 (estimation of P_S^θ, P_{S'}^θ)

P_S^θ may be operationally instantiated by one or more of:

(a) **Population empirical:** the empirical distribution on Z observed from a population of self-substrate trajectories under channel θ_S;

(b) **Learned generative model:** a parameterised model (e.g., neural density estimator) trained on substrate-typical Z-observations;

(c) **Mechanistic derivation:** when K_S has analytically tractable form, P_S^θ is derived in closed form via pushforward.

Mutatis mutandis for P_{S'}^θ.

Convention: an estimation report accompanying any D_θ-measurement specifies (i) the channel θ, (ii) the estimator for P_S^θ and P_{S'}^θ, (iii) the sample for Q^θ_I, (iv) absolute-continuity check, (v) sign of D_θ.

### Lemma 7.5.1 (Le Cam binary identifiability lower bound — channel-sufficiency for D-test)

For any binary classifier δ : Z → {drawn from P_S^θ, drawn from P_{S'}^θ} based on a single-step observation Z drawn from one of the two channel-pushed substrate priors, the probability of classification error P_e satisfies

P_e ≥ ½ · (1 − ‖P_S^θ − P_{S'}^θ‖_{TV})    (Le Cam two-point lemma; Le Cam 1986)

where ‖·‖_{TV} is total variation on the single-step observation space (Z, G). The classifier δ here is the prior-pair distinguishability classifier — it decides which substrate-prior generated a single observation Z. This is not the D-test classifier of §7.4, which compares Q^θ_I to both priors simultaneously and outputs a verdict on transposition-direction; the Le Cam bound quantifies channel-sufficiency for the prior-pair sub-task that the D-test depends on. If the priors are indistinguishable, no Q-based comparison can discriminate either, but the bound does not directly govern D-test error on arbitrary Q^θ_I — that requires the stronger full-family-sufficiency condition of Lemma 7.6.

The bound must be applied at the single-step level. For multi-step observation on (Z^n, G^{⊗n}) **under independent products** (i.i.d. observations), ‖P_S^{θ, ⊗n} − P_{S'}^{θ, ⊗n}‖_{TV} → 1 as n grows under any non-zero per-step distinguishability — by **Hellinger-affinity tensorisation**. The Hellinger affinity ρ(P, Q) := ∫ √(dP · dQ) ∈ [0, 1] satisfies ρ(P^{⊗n}, Q^{⊗n}) = ρ(P, Q)^n (multiplicative *only* under independent products); when P ≠ Q so that ρ(P, Q) < 1, the n-fold affinity decays geometrically to 0, and the standard lower bound TV(P, Q) ≥ 1 − ρ(P, Q) gives TV(P^{⊗n}, Q^{⊗n}) → 1 as n → ∞. **Scope of the tensorisation argument.** The above applies to *independent product* observations. For dependent or Markov multi-step observations the Hellinger-affinity does *not* factorise multiplicatively across coordinates; the same TV → 1 conclusion then requires a *separate positive separation-rate assumption* — for instance positive Hellinger-contraction rate per step, positive Chernoff information rate (Stein's lemma regime), or mixing conditions that effectively decouple distant time-steps to recover an asymptotic independence structure. Operator-driven trajectories on Markov substrates fall into this dependent regime; their TV → 1 behaviour must be reported with explicit separation-rate hypothesis declared in the Test 16.1 channel-sufficiency report, not inferred from the i.i.d. Hellinger argument. The standard Pinsker inequality §0.4 *upper*-bounds TV by √(KL/2) and supplies the wrong direction — Pinsker cannot establish TV → 1 from large KL (it bounds TV above, not below); the Hellinger-affinity route is the correct lower-bound mechanism, but only under the independent-product scope just stated. TV itself does *not* tensorise multiplicatively. With TV → 1, P_e ≥ ½(1 − TV) saturates trivially. Channel-sufficiency assessment therefore uses the per-step TV (or the chain-rule decomposition of KL), not the n-step product. If the channel θ has small per-step TV-separation between substrate priors (‖P_S^θ − P_{S'}^θ‖_{TV} ≪ 1 on single-step (Z, G)), the prior-pair subtask on which the D-test of §7.4 depends has single-shot error lower-bounded near ½: no reliable single-observation prior-pair classifier exists, and the D_θ-classification is informative only when per-step distinguishability is non-trivial. Multi-step accumulation can reduce error, but only when per-step distinguishability is non-trivial to begin with.

The Pinsker inequality of §0.4 gives ‖P_S^θ − P_{S'}^θ‖_{TV} ≤ √((1/2) D_{KL}(P_S^θ ‖ P_{S'}^θ)), so small KL between priors implies small TV and a correspondingly high Le Cam error bound; sufficient KL-separation is necessary but not sufficient for low classification error. Channel selection therefore considers both KL and TV separation between channel-pushed substrate priors.

For operational tolerance P_e^{max} on the prior-pair sub-task, the channel passes the necessary Le Cam separability condition only if ‖P_S^θ − P_{S'}^θ‖_{TV} ≥ 1 − 2 P_e^{max}. The derivation is direct: requiring ½(1 − TV) ≤ P_e^{max} gives 1 − TV ≤ 2 P_e^{max}. The condition is necessary, not sufficient — satisfying it removes the Le Cam impossibility bound but does not guarantee that the empirical D-test achieves error ≤ P_e^{max}, since finite-sample concentration, density-estimation accuracy, and decision-rule design enter separately. Test reports (§16) declare both the TV-separation and the empirical error bound implied; the threshold P_e^{max} < ½ is required for it to be informative.

### Lemma 7.5.2 (Blackwell sufficiency — channel hierarchy for D-test)

For two observation channels θ_1 = (θ_{1,S}, θ_{1,S'}) and θ_2 = (θ_{2,S}, θ_{2,S'}) on common observation spaces (Z_1, G_1) and (Z_2, G_2) respectively, with channel-pushed substrate priors P_S^{θ_1} := (θ_{1,S})_* P_S, P_{S'}^{θ_1} := (θ_{1,S'})_* P_{S'} on (Z_1, G_1) and similarly for θ_2 on (Z_2, G_2), the Blackwell partial order is defined by

θ_1 ≥_B θ_2    iff there exists a Markov kernel η : (Z_1, G_1) → (Z_2, G_2) such that P_S^{θ_2} = η_* P_S^{θ_1} and P_{S'}^{θ_2} = η_* P_{S'}^{θ_1};

i.e., the channel-pushed priors under θ_2 are obtained by stochastic garbling η of the priors under θ_1. Operationally, θ_1 ≥_B θ_2 means θ_2 can be obtained from θ_1 by stochastic garbling at the level of pushforward distributions, and θ_1 carries strictly more information about the (S, S')-pair than θ_2 (Blackwell 1953).

If θ_1 ≥_B θ_2, then for any decision rule (in particular the D-test classifier of §7.4) the optimal classification error satisfies P_e^*(θ_1) ≤ P_e^*(θ_2): failure of prior-pair distinguishability under the more-informative channel θ_1 implies failure under any garbled θ_2 derived from it. The proof is the Blackwell-Sherman-Stein theorem (Blackwell 1953; Le Cam 1964), which establishes that θ_1 ≥_B θ_2 iff for every decision problem the optimal risk under θ_1 is at most the optimal risk under θ_2; applied to D-test classification with 0-1 loss the risk is P_e^*.

Channel selection is partially ordered by Blackwell dominance: refining a channel (using stronger θ_1 rather than coarser θ_2) cannot decrease the prior-pair discriminability available to the D-test. The prior-pair discriminability between (P_S, P_{S'}) is therefore monotone-improving under channel refinement up to the Blackwell-maximal channel — the original substrate-prior trajectory laws (P_S, P_{S'}) before any pushforward. In practice, observation constraints force a non-Blackwell-maximal θ; the framework admits this loss-of-information honestly via the Blackwell dominance hierarchy.

The Blackwell partial order defined here orders the information content of channels for distinguishing the substrate-prior pair (P_S, P_{S'}). The conclusion above is a statement about prior-pair distinguishability and decision-risk on (P_S, P_{S'}), not automatically about the sign of D_θ(T̃) for arbitrary Q^θ_I. The D-test depends on the triple (Q^θ_I, P_S^θ, P_{S'}^θ); Blackwell garbling η on the prior pair does not by itself guarantee preservation of D_θ's sign for arbitrary Q. Sign preservation requires the stronger full-family sufficiency condition of Lemma 7.6 below — η sufficient for the full statistical family containing Q^θ_I in addition to (P_S^θ, P_{S'}^θ). Without that stronger hypothesis, Blackwell hierarchy on the prior pair gives decision-risk ordering on prior-separability, not D-sign-stability. Le Cam's two-point lemma in turn gives a quantitative error bound on a fixed channel; Blackwell's sufficiency is the comparative result across channels; and Lemma 7.6's sign-stability under sufficient-statistic coarsening is the special case of Blackwell sufficiency with η equal to the sufficient-statistic map.

### Lemma 7.6 (sign-stability under sufficient-statistic channel coarsening)

Let θ̃ factor through θ via a measurable surjection η : (Z, G) → (Z̃, G̃) — i.e., θ̃_S = η ∘ θ_S and θ̃_{S'} = η ∘ θ_{S'}. Under the stronger sufficiency assumption that η is a sufficient statistic for the full statistical family containing (P_S^θ, P_{S'}^θ, Q^θ_I) — meaning η preserves Radon-Nikodym log-densities for every triple of distributions in the family — D_{θ̃}(T) = D_θ(T) exactly. The data-processing inequality D_{KL}(η_* μ ‖ η_* ν) ≤ D_{KL}(μ ‖ ν) becomes equality for every pair of distributions in the family by the Fisher-Neyman factorisation theorem (Cover & Thomas Ch. 2.10); both KL terms in D are exactly preserved under η_*, and so is their difference.

Sufficiency for only the pair (P_S^θ, P_{S'}^θ) — without including Q^θ_I in the family — does not guarantee transfer to Q^θ_I unless Q^θ_I lies in the exponential family generated by the pair. In the general case the data-processing inequality bounds each KL term separately, D_{KL}(η_* Q^θ_I ‖ η_* P) ≤ D_{KL}(Q^θ_I ‖ P) for each prior P, with potentially different reductions; the difference D_{θ̃} − D_θ has no automatic sign-preservation outside the full-family-sufficiency case. Sign-flipping under non-sufficient coarsening is in fact possible: a channel that preserves the magnitude of Q-vs-P_{S'} distance while compressing Q-vs-P_S distance can convert D > 0 into D < 0. Channel choice in measurement reports (per the Def. 7.5 convention) must therefore include a sufficiency assessment or explicit acknowledgement of channel-dependence of the conclusion.

### Remark 7.7 (Sanov-type anti-coincidence bound for D > 0 observations)

For i.i.d.-sampling intuition: if the channel observation Q^θ_I were generated i.i.d. from the self-substrate prior P_S^θ (the null hypothesis of pure self-substrate fluctuation), Sanov's theorem (Sanov 1957; cf. Dembo-Zeitouni *Large Deviations Techniques and Applications*, 2nd ed., Theorem 6.2.10) gives

P(empirical Q_n ≈ Q | n i.i.d. samples from P_S^θ) ≈ exp(−n · D_{KL}(Q ‖ P_S^θ)).

An observed Q^θ_I with strictly positive D_{KL}(Q^θ_I ‖ P_S^θ) > 0 is therefore exponentially unlikely under the null of self-substrate sampling — exponentially difficult to explain as ordinary fluctuation rather than operator-driven deviation.

Operator-driven trajectories on Markov substrates are not i.i.d.: the operator's policy makes the trajectory dependent on prior states, and Sanov's theorem in its i.i.d. form does not directly apply. The Donsker-Varadhan large-deviations extension for Markov processes (Donsker-Varadhan 1975; Dembo-Zeitouni Ch. 6.5) replaces the rate function with a level-2 entropy involving the joint two-step distribution; the exponential anti-coincidence character is preserved but the rate constant differs.

The bound does not prove operator-driven origin of Q^θ_I — random fluctuations of arbitrarily large KL are possible with exponentially small but non-zero probability. It strengthens the implausibility of the «mere coincidence» explanation. Combined with the τ-test (post-interval structural trace) and R_α (categorical isomorphism on operator-images), this gives a multi-layered defence against the coincidence-explanation attack.

---

## §8. Substrate-realisation of Φ via relative entropy production

The operator-specification Φ (Def. 1.1(iii)) is abstract. A deployment O@S realises it only if the substrate's intrinsic irreversibility matches. This section gives *one canonical* substrate-realised cost (relative entropy production against time-reversal, in the Crooks–Jarzynski–Seifert tradition) and the conditions under which it satisfies the operator's Φ-specification. Identifying Φ with relative entropy production is **one canonical choice, not the unique possible choice**: domain-specific cost functionals (free-energy decomposition under non-adiabatic protocols, work-functional under given driving, monotone reparameterisations) are admissible variants where the substrate physics suggests them.

### Definition 8.1 (substrate-realised cost)

For substrate S with stationary kernel K_S admitting time-reversal K_S^{rev} (per §0.5), the *substrate-realised cost* on (X_S × X_S, F_S ⊗ F_S) is:

**Ψ_S(x, y) := r_{K_S}(x, y) = log [ dK_S(x, ·)/dK_S^{rev}(x, ·) ] (y)**

defined K_S(x, ·)-a.e. (Radon-Nikodym derivative of forward against time-reversed transition kernel at y).

**Canonical jointly measurable version.** Throughout this paper we fix a **canonical jointly measurable version** Ψ_S : X_S × X_S → ℝ ∪ {+∞} of the RN-density above — i.e. a single F_S ⊗ F_S-measurable function that for μ_S-a.e. x serves as a representative of log(dK_S(x, ·)/dK_S^{rev}(x, ·)). Joint measurability is guaranteed on standard Borel substrates (§0.7) by the disintegration construction of §0.5 and standard measurable-selection theorems (e.g., Bogachev *Measure Theory* II §10.6). All subsequent pointwise evaluations Ψ_S(ι_S(s), ι_S(t)) refer to *this fixed canonical version*. Evaluating on the operator-image is well-defined precisely because the operator-image is F_S-measurable and the canonical version is jointly measurable; values are pinned down ν_s-a.e. on the operator-image admissible-target slice ι_S(A_s) under the canonical reference measure ν_s of §8 below, which is by construction (continuous case) absolutely continuous with respect to (ι_S)_*^{−1} K_S(ι_S(s), ·)|_{ι_S(A_s)}. The «ν_s-a.e.» statements of (R3) below should therefore be read as comparisons performed on the canonical version against this canonical reference measure, never on point-set values that could be altered on null sets without affecting the underlying distribution.

**Source-side caveat — canonical version not μ_S-null-source-pinned.** The ν_s discipline above pins Ψ_S(ι_S(s), ·) target-side: for fixed source s, the canonical version determines Ψ_S(ι_S(s), ·) ν_s-a.e. in t ∈ A_s. The *source-state dependence* s ↦ Ψ_S(ι_S(s), ·) — as a function of source s — remains canonical-version-dependent whenever ι_S(s) lies in a μ_S-null subset of X_S, since the RN-density is specified only for μ_S-a.e. x. For continuous-state substrates with low-dimensional operator-image (e.g., ι_S(Σ) ⊂ X_S a submanifold of lower dimension than X_S), the entire image may sit in a μ_S-null set and source-side evaluation is version-dependent. Two operational consequences: (i) the canonical-version choice on the operator-image is part of the **deployment specification** (declared together with ι_S, K_S, ν_s); standard-Borel and disintegration supply measurable existence but not version-uniqueness across μ_S-null source slices. (ii) Cross-deployment (M3) Ψ-equality (§4.1) presupposes jointly compatible canonical-version selections on both operator-images — parallel to the ν_s consistency requirement of §8.2 (R3). A source-side regularity hypothesis **(OIR-source)**: (ι_S)_∗ λ_Σ ≪ μ_S for some declared reference measure λ_Σ on Σ — removes the version-dependence ((ι_S)_∗ λ_Σ-a.e. uniqueness of the canonical version on the operator-image). Imp. 11.3's (OIR) is target-side (push-forward of ν_s on A_s); (OIR-source) is the source-side parallel. Deployments lacking (OIR-source) must declare canonical-version data explicitly per (i)–(ii) to render Ψ-evaluations intrinsically well-defined.

Ψ_S may be positive or negative *pointwise* on individual transitions (x, y). Its expectation against the stationary joint K_S(x, dy) μ_S(dx) is non-negative (Gibbs), and strictly positive in expectation for non-reversible dynamics under suitable non-degeneracy (cf. §9.1 pointwise vs expectation discussion). It is the standard quantification of trajectory irreversibility in stochastic thermodynamics (Seifert 2012; Crooks 1999; Jarzynski 1997).

### Definition 8.2 (Φ-realising deployment)

A deployment O@S = (O, S, ι_S) is *Φ-realising* iff:

(R1) K_S^{rev} exists by disintegration on standard Borel (§0.5 — no absolute continuity required for existence); additionally K_S(x, ·) ≪ K_S^{rev}(x, ·) for μ_S-a.e. x, so that Ψ_S := r_{K_S} is well-defined as a log-density μ_S-a.e.;

(R2) ι_S(Σ) is contained in a measurable subset on which μ_S is positive (i.e., every measurable neighbourhood of ι_S(Σ) carries μ_S-mass);

(R3) **realisation condition** — there exists a reference measure ν_s on A_s (for each s ∈ Σ) such that:

  Ψ_S(ι_S(s), ι_S(t)) = Φ(s, t)    for ν_s-a.e. t ∈ A_s.

**ν_s consistency between deployments (for (M3) cross-deployment comparison).** When (M3) cost preservation is to be verified between two Φ-realising deployments O@S and O@S' (Def. 4.1 (M3) at the substrate-realised Ψ-layer per §8.3), the reference measures ν_s of O@S and ν_s' of O@S' must be *jointly declared* and either: (a) identical as measures on A_s (canonical choice for discrete operator state-spaces, where ν_s = counting measure); or (b) mutually absolutely continuous with declared Radon-Nikodym density dν_s'/dν_s, in which case (M3) Ψ-equality is stated up to that Radon-Nikodym normalisation; or (c) declared inequivalent, in which case (M3) is *not* a meaningful cross-deployment comparison and the deployments are formally outside the Φ-realising comparison scope. Without explicit ν_s declarations on both sides, Ψ-equality is ambiguous between «equality a.e. on each deployment's own reference measure» (a weaker claim that does not entail cross-deployment equality) and «equality on a shared reference measure» (the load-bearing Ψ-layer (M3) content). Test 16.2b step 4 reports must declare ν_s, ν_s' and confirm consistency (a)–(b) before invoking Ψ-equality as a verified (M3) verdict.

The reference measure ν_s is part of the deployment specification (declared together with ι_S). Canonical choices:

- For *discrete-state operators* (Σ countable, F_Σ = 2^Σ): ν_s = counting measure on A_s. The a.e. condition collapses to pointwise equality.
- For *continuous-state operators* (Σ uncountable, e.g., latent-vector operators): ν_s typically the measure on A_s obtained by transporting K_S(ι_S(s), ·)|_{ι_S(A_s)} through ι_S^{-1} (since ι_S : Σ → X_S is a measurable injection, ι_S^{-1} is defined on ι_S(Σ) ⊂ X_S; the substrate's own conditional distribution over admissible-target images is pulled back to A_s). This avoids the vacuity trap of choosing ν_s concentrated on a measure-zero set.
- Alternative substrate-equivalent ν_s admissible if declared.

The a.e. condition prevents the ill-posedness of pointwise comparison on measure-zero sets; the canonical ν_s choices above prevent vacuous satisfaction.

(R4) for s ∈ Σ and t ∉ A_s, the substrate forbids the transition in the appropriate sense: K_S(ι_S(s), B) = 0 for every measurable B containing ι_S(t) but disjoint from ι_S(A_s).

**Extended cost convention for inadmissible transitions.** Independently of (R4), the substrate-realised cost Ψ_S is *extended by convention* to +∞ on pairs (ι_S(s), ι_S(t)) with t ∉ A_s, matching the operator-specification's Φ(s, t) = +∞ for inadmissible t (§1.1(ii)). This is a **separate convention**, not a consequence of (R4): the Radon–Nikodym log-density Ψ_S = log(dK_S/dK_S^{rev}) is generally undefined or sign-ambiguous on transitions where the forward kernel has zero mass (0/0 or 0/positive), so the +∞ value must be imposed externally to make Ψ_S continuous with the operator-specification's hard inadmissibility. Under (R4) the forward measure vanishes on the relevant set, ensuring the convention is consistent (no positive-mass transition is overridden); without (R4) the convention may conflict with a positive-density region of K_S, hence the softening discussion below.

**Scope of (R4).** (R4) is a *hard-support* inadmissibility condition: it requires the substrate kernel itself to assign zero probability to inadmissible operator-image transitions, not just the operator policy. For stochastic substrates with full-support ambient noise (e.g., overdamped Langevin diffusions on connected manifolds, neural-network kernels with non-zero entropy at every transition) the hard-support condition typically fails — the substrate kernel has positive probability on every measurable set including those containing inadmissible operator-image points. For such substrates a softened version of (R4) is needed: replace hard-support inadmissibility with *policy-level inadmissibility* (Def. 7.3: the operator policy π_O places zero mass on transitions outside ι_S(A_s)), or with a *large-penalty limit* in which Ψ_S(ι_S(s), ι_S(t)) → +∞ as t exits A_s rather than being identically +∞ on inadmissible transitions. Under the canonical Crooks–Jarzynski–Seifert Ψ-realisation, hard-support (R4) is the strict starting convention, but Remark 8.4.1 shows that finite non-trivial one-directional Φ-realising deployments *require* softened-(R4) — hard-support (R4) forces Ψ_S = +∞ on the admissible forward transition (per Remark 8.4.1(iii)). Accordingly, the §9–§11 results that invoke Ψ_S are to be read in the **softened-(R4) one-directional regime** (per the §10 standing assumption); hard-support (R4) remains available only for degenerate reversible (trivial-Ψ) cases or under the alternative non-antisymmetric cost functionals of §18.(a),(c). Extension of the hard-support regime to non-trivial *bidirectional* Φ is not merely «open work» — it is closed off under the canonical realisation by the Remark 8.4.1 antisymmetry obstruction; only a non-antisymmetric cost functional can reopen it.

Φ-realising deployments are *canonical* deployments: those where the operator's abstract cost specification coincides (up to substrate-measure-a.e.) with the substrate's intrinsic irreversibility production.

### Remark 8.3 (Φ-realising vs general deployment)

Definition 3.1 requires only (D1) dynamical compatibility and (D2) cost realisability via *some* measurable Φ_S^*. Definition 8.2 strengthens (D2) to the specific case Φ_S^* = Ψ_S — i.e., the substrate-realised cost is the canonical Crooks–Jarzynski–Seifert form. Other realisations (e.g., free-energy, work, heuristic-distance) may apply in domain-specific cases.

For the remainder of this work, we tacitly assume deployments are Φ-realising unless stated otherwise. This ties the operator-specification's Φ to the substrate's intrinsic irreversibility, giving Φ information-theoretic units (nats) and operational substance.

**(M3) and (M4) are independent morphism axioms.** All load-bearing cost-preservation content of (M3) is concentrated in the Φ-realising regime (Def. 8.2 + §8.3 standing assumption). In *merely general* deployments under Def. 3.1 (without Φ-realising upgrade), (M3) is formal Φ-axiom-level bookkeeping rather than an independent physical constraint — both sides reduce to Φ(s, t) by (D2) of their respective deployments, the constraint adds no further content. Under §8.2 Φ-realising deployment, the Φ-axiom-level equality Φ_{S'}^*(ι_{S'}(s), ι_{S'}(t)) = Φ_S^*(ι_S(s), ι_S(t)) is automatic because both sides equal Φ(s, t) by (R3) of Def. 8.2 applied to each deployment. However, the *substrate-realised cost* equality Ψ_S^ι = Ψ_{S'}^ι at the operator-image is **not** a consequence of (M4) sub-Markov-kernel equality alone, even under Φ-realising. The reason: Ψ_S(ι_S(s), ι_S(t)) := log(dK_S(ι_S(s), ·)/dK_S^{rev}(ι_S(s), ·))(ι_S(t)) involves the time-reversal kernel K_S^{rev} at the operator-image; by the §0.5 disintegration formula, K_S^{rev}(y, dx) is determined by K_S(x, dy) μ_S(dx) for **all** x ∈ X_S — including x in the substrate-complement X_S \ ι_S(Σ) whose forward kernel charges ι_S(Σ). Two deployments O@S and O@S' with K_S^ι = K_{S'}^ι (so (M4) holds) may have distinct substrate-complement inflow patterns into the operator-image, yielding K_S^{rev} ≠ K_{S'}^{rev} when restricted to ι_S(Σ) × ι_S(Σ), and hence Ψ_S^ι ≠ Ψ_{S'}^ι in general. Operator-image-restricted forward kernel (which (M4) constrains) does *not* determine operator-image-restricted reverse kernel (which Ψ requires).

**Two regimes (certified vs under-test).** The «(M3) independent» claim is regime-relative. If both deployments are *already certified* Φ-realising with respect to a common Φ and compatible ν_s (§8.2 (R3) + ν_s-consistency), then Ψ_S(ι_S(s), ι_S(t)) = Φ(s, t) = Ψ_{S'}(ι_{S'}(s), ι_{S'}(t)) and (M3) Ψ-equality holds *automatically* — there is nothing independent to verify. (M3)-as-independent-axiom is load-bearing precisely in the *verification* regime, where Test 16.2b does **not** assume the target deployment is Φ-realising but tests whether it is: there the candidate's Ψ_{S'} is an empirical object whose equality with Ψ_S must be checked, and (M4) sub-kernel equality alone does not entail it (per the complement-inflow obstruction above). This resolves the apparent tension between §8.2 (where Φ-realisation makes Φ-level equality automatic) and §16 (where (M3) is a separate test step): the former *assumes* certification, the latter *performs* it. Example 4.1.3 is in the verification regime — Ψ_S and Ψ_{S'} are computed separately and their equality checked, not assumed.

Consequently (M3) is retained in Def. 4.1 as an **independent** morphism axiom alongside (M4); the §10–§11 standing-assumption scope does not allow (M3) to be eliminated as derived. The two axioms have complementary roles: (M4) constrains the substrate-induced operator-image sub-Markov structure (capturing within-operator-image transition rates), while (M3) constrains the substrate-realised irreversibility cost layer (capturing time-reversal-anchored cost). Both are independently load-bearing and jointly distinguish R_α-iso from a typing artefact. The independence is two-directional. (M4) ⇏ (M3) by the complement-inflow obstruction above (equal forward sub-kernels, different time-reversal, hence different Ψ — Example 4.1.2). The reverse, **(M3) ⇏ (M4)**, also holds: since Ψ(s, t) = log(K(s, t)·μ(s) / (K(t, s)·μ(t))) depends on K only through the ratio K(s, t)/K(t, s) together with the μ-ratio, two operator-images with K_S(a, b)/K_S(b, a) = K_{S'}(a', b')/K_{S'}(b', a') and matching μ-ratios yield identical Ψ_S^ι = Ψ_{S'}^ι (so (M3) holds) while differing in absolute sub-kernel values K_S^ι ≠ K_{S'}^ι (so (M4) fails) — e.g. K_S(a, b) = 0.4, K_S(b, a) = 0.2 versus K_{S'}(a', b') = 0.2, K_{S'}(b', a') = 0.1, both with ratio 2 but distinct K^ι. Neither axiom implies the other; both are required. A natural symmetric strengthening — adding (M4-rev): K_S^{rev,ι} = K_{S'}^{rev,ι} on operator-image — would make (M3) derivable from (M4) + (M4-rev) under Φ-realising, but we do not adopt this stronger axiom in the present framework; it is noted as an open structural extension. Test 16.2b retains (M3) and (M4) as separate verification steps (4 and 4' respectively).

### Property 8.4 (axioms of §1 verified under Φ-realising deployment)

Under Definition 8.2, the §1 axioms (Φ1)–(Φ4) are recoverable from substrate structure:

* (Φ1) Φ(s, s) = 0 is imposed by operator-specification (§1.1(iii)). In Φ-realising deployments it is realised on the diagonal s = t by convention; the pointwise expression "Ψ_S(ι_S(s), ι_S(s)) = 0" holds tautologically for discrete K_S (K_S(x, {x}) detailed-balanced trivially when atoms exist) but is *not* derivable pointwise in atomless cases (singletons have K_S-measure zero, Radon-Nikodym r_K(x, x) undefined at a single point). The diagonal-zero convention is consistent across both regimes.
* (Φ2) Φ(s, t) > 0 for admissible t ≠ s: under R3 (Ψ_S = Φ ν_s-a.e.) this is a *pointwise-a.e. positivity* requirement on the substrate-side irreversibility log-density at the operator-image. Non-reversibility of K_S guarantees only ⟨Ψ_S⟩ > 0 (in expectation against the forward joint, by Gibbs); pointwise Ψ_S = log(dK/dK^{rev}) can be negative on individual transitions (§8.1). The conjunction R3 + (Φ2) therefore imposes the stronger **substrate-side condition**: for the (O, S) pair under consideration, K_S admits a version of r_K(ι_S(s), ι_S(t)) > 0 for ν_s-a.e. t ∈ A_s \ {s}. Substrates not satisfying this condition cannot support a Φ-realising deployment of O with the given Φ-axioms; the relaxation (allowing pointwise sign-change but expectation-positive Φ as a moment functional) is discussed as an alternative in §18.(a).
* (Φ3) Φ(s, t) = +∞ for inadmissible t: enforced by (R4).
* (Φ4) Irreversibility floor ε_O > 0: holds when the substrate's round-trip irreversibility on the operator-image is bounded below; this is a condition on (O, S) — for some substrates and operators, (Φ4) may fail (signalling that O cannot be Φ-realised by S — see Imp. 11.3). **The realisability of branch (Φ4b) is itself constrained — see Remark 8.4.1.**

### Remark 8.4.1 (antisymmetry obstruction: the Crooks–Seifert realisation constrains admissibility structure)

The canonical Ψ-realisation Φ = Ψ_S of §8.1 carries a **pointwise antisymmetry** on reciprocal operator-image transitions. In the discrete case, K_S^{rev}(x, y) = K_S(y, x)·μ_S(y)/μ_S(x) gives

Ψ_S(x, y) = log[K_S(x, y)·μ_S(x) / (K_S(y, x)·μ_S(y))],     hence     **Ψ_S(x, y) + Ψ_S(y, x) = 0**

for every reciprocal pair (and analogously in the general stationary disintegration: the forward and reverse joints share marginals, so the log-density of one direction is the negative of the other μ-a.e.). Three structural consequences for the admissibility geometry of any non-trivial canonically-Φ-realising deployment:

(i) **Round-trip floor (Φ4b) is incompatible with Ψ-realisation.** For a bidirectionally-admissible pair (both t ∈ A_s and s ∈ A_t), the floor (Φ4b) Φ(s, t) + Φ(t, s) ≥ ε_O > 0 requires the directed-cost sum to be strictly positive, but antisymmetry forces it to 0. Under the canonical realisation, only branch (Φ4a) — one-directional admissibility, no reciprocal admissible pair — is consistent with a non-trivial irreversibility floor; (Φ4b) is realisable only under a *non-antisymmetric* cost functional (§18.(a),(c)).

(ii) **Pointwise (Φ2) cannot hold on both directions of a reciprocal admissible pair.** Since Ψ_S(s, t) = −Ψ_S(t, s), at most one directed cost is strictly positive; the other is its negative. Bidirectional admissibility with pointwise-positive Φ on *both* directions is therefore impossible under Ψ-realisation (the negative direction violates (Φ2)).

(iii) **Hard-support (R4) + one-directional admissibility forces infinite Ψ.** If b → a is inadmissible and (R4) is enforced at the substrate layer (K_S(ι_S(b), ι_S(a)) = 0), then K_S^{rev}(ι_S(a), ι_S(b)) = K_S(ι_S(b), ι_S(a))·μ_S(b)/μ_S(a) = 0, so Ψ_S(ι_S(a), ι_S(b)) = log[K_S(a, b)/0] = +∞ — entropy production on the admissible forward transition diverges, violating (Φ2)'s finiteness Φ ∈ (0, +∞). Finite non-trivial Ψ on the admissible transition therefore requires the **softened (R4)** of §8.2 Scope (policy-level inadmissibility with K_S(ι_S(b), ι_S(a)) > 0 retained at the substrate layer).

**Combined:** a finite, non-trivial, canonically-Φ-realising deployment requires *softened*-(R4) *one-directional* admissibility. Example 4.1.3 lives in exactly this regime and is, by (i)–(iii), the only regime in which such a worked construction can exist. The hard-support (R4) Φ-realising framework of §8.2 with non-trivial *bidirectional* Φ is, under the entropy-production realisation, **essentially unpopulated** — it yields either trivial reversible Ψ ≡ 0 or divergent Ψ = +∞. This is a limitation of the *Crooks–Seifert cost realisation specifically*, not of the operator-mobility primitive: the alternative cost functionals of §18.(a) (Fisher-information / α-divergence) and §18.(c) (free-energy / variational) need not be antisymmetric and may admit bidirectional positive-cost realisations. The standing assumption of §10–§11 («deployments are Φ-realising») should accordingly be read, under the canonical realisation, as restricting to the softened-(R4) one-directional class characterised here.

**Regime matrix (canonical Crooks–Seifert Ψ-realisation).** Whether a finite non-trivial Φ-realising deployment is populated, by (Φ4)-branch × (R4)-support × admissibility:

| (Φ4) branch | (R4) support | Admissibility | Finite non-trivial Ψ-realisation? |
|---|---|---|---|
| (Φ4a) one-directional | hard-support | one-directional | **No** — K_S(ι(b), ι(a)) = 0 forces K^{rev}(ι(a), ι(b)) = 0, so Ψ(ι(a), ι(b)) = +∞ (consequence (iii)) |
| (Φ4a) one-directional | softened | one-directional | **Yes** — the unique populated regime; Example 4.1.3 lives here |
| (Φ4b) bidirectional floor | hard-support | bidirectional | **No** — antisymmetry forces Φ(s,t) + Φ(t,s) = 0 < ε_O (consequence (i)); (Φ2) also fails on the negative direction (consequence (ii)) |
| (Φ4b) bidirectional floor | softened | bidirectional | **No** — same antisymmetry obstruction; the ε_O > 0 round-trip floor is unrealisable under Ψ regardless of support convention |
| trivial (Φ ≡ 0) | either | either | Yes but **vacuous** — Ψ ≡ 0 (reversible), no architectural-mobility content (cf. Imp. 11.3 Case B) |

Only the softened-(R4) one-directional row carries non-trivial finite Ψ under the canonical realisation. A non-trivial *bidirectional* Φ requires a non-antisymmetric cost functional (§18.(a),(c)).

### Remark 8.5 (units; connection to thermodynamics)

Φ has units of nats (natural log units of relative entropy). Sums of Φ along an operator-trajectory equal the total entropy production of the trajectory against the reference time-reversal. The framework connects to stochastic thermodynamics (Seifert 2012; Crooks 1999; Jarzynski 1997). The *integral fluctuation theorem* (Seifert 2012, Eq. 11) gives:

⟨e^{−Ψ_S}⟩_{forward joint} = 1

an equality on the forward-trajectory distribution. By Jensen's inequality applied to the convex function exp(−·), this implies ⟨Ψ_S⟩ ≥ 0 — the standard non-negativity of expected entropy production. The operator's Φ-budget therefore inherits well-known information-theoretic bounds.

---

## §9. Substrate-accumulation and the architectural mobility state

### Definition 9.0 (effective interval of a transposition)

The *effective interval* of a transposition T_i : O@S_i → O@S_{i+1} is a discrete-time interval I_i = [n_i^{start}, n_i^{end}] ⊂ ℕ specified as part of T_i's operational declaration, with the following structure:

(I1) **endpoints declared.** n_i^{start} and n_i^{end} are stopping times with respect to the filtration (F_n) fixed in §0.8 and used in Theorem 9.3 below; their difference L_i := n_i^{end} − n_i^{start} ≥ 1 is the *interval length* — the number of discrete *transitions* between the L_i + 1 time-points {n_i^{start}, n_i^{start}+1, ..., n_i^{end}} indexed by the interval. (Convention: the interval is closed on time-points; transitions are indexed by their source-time and run on the half-open transition-index set {n_i^{start}, ..., n_i^{end} − 1}.)

(I2) **phase content.** The interval admits the phase stratification of §7.3: during n ∈ [n_i^{start}, n_i^{end}], the operator-image is *displaced into S_{i+1}* (the during-phase substrate); n < n_i^{start} is the pre-phase (operator in S_i) and n > n_i^{end} is the post-phase (operator returned to S_i or remaining in S_{i+1}, declared per T_i). For the canonical case the during-phase coincides with [n_i^{start}, n_i^{end}].

(I3) **operator-policy active.** The operator policy π_O (Def. 7.3) governs the L_i *transitions* indexed by {n_i^{start}, ..., n_i^{end} − 1} (i.e., transitions from time-point n_i^{start} to n_i^{start}+1, ..., from n_i^{end}−1 to n_i^{end}), coupled to the phase-active substrate kernel K_{S_{i+1}} (during phase). Outside the effective interval the operator-trajectory is governed by the policy active on the source substrate K_{S_i}.

(I4) **measurability.** I_i is a measurable function of the filtration F_{n_i^{end}}.

For the operational tests of §16 (Test 16.1 step 1: «identify the claimed effective interval I»), the system claiming T_i must declare I_i as part of the test protocol; the framework's measurability and convergence results apply to whatever interval is declared, with the obvious requirement that the declared I_i is internally consistent (the operator-image displacement holds throughout the declared interval).

*Default convention.* When the effective interval is left implicit (e.g., in pure-statement contexts not requiring n_i^{start}/n_i^{end} computation), it is the canonical interval during which the operator-displacement is in force; mixed-phase cases are explicitly declared per Def. 9.1 below.

### Definition 9.1 (per-transposition cost and accumulated Φ-mobility)

For a transposition T_i : O@S_i → O@S_{i+1} with realised operator-driven trajectory ω^{(i)} = (ω_0^{(i)}, ω_1^{(i)}, ..., ω_{L_i}^{(i)}) during its effective interval I_i (per Def. 9.0, with L_i = n_i^{end} − n_i^{start} discrete time-steps), the *per-transposition cost* is

**φ(T_i) := Σ_{k=0}^{L_i − 1} Ψ_{S^∗_i}(ω_k^{(i)}, ω_{k+1}^{(i)})**    (nats)

where Ψ_{S^∗_i} is the substrate-realised cost (Def. 8.1) of the **phase-active substrate during the effective interval of T_i**:

* for the **during-transposition phase** (operator displaced into the target substrate S_{i+1} during I; cf. §7.3 phase stratification), S^∗_i = S_{i+1} and the trajectory ω^{(i)} lives in X_{S_{i+1}};
* for **pre- and post-transposition phases** (operator anchored in source S_i), S^∗_i = S_i and the trajectory lives in X_{S_i};
* for **mixed effective intervals** (I spanning a phase boundary), the sum is computed piecewise — each term Ψ uses the substrate active at the time-step in question, and the total is the sum of phase-segments.

Convention: the dominant phase of the transposition's effective interval (per Def. 9.0's notion of "effective interval", which is the interval during which T_i's operator-displacement is in force) is the *during* phase; unless otherwise stated, φ(T_i) refers to that phase and uses Ψ_{S_{i+1}}.

For a sequence T_1, ..., T_n of **verified true transpositions** (per Def. 6.1 — each T_i passes D + τ + R_α/T1; cf. §13.4 / §13.4.1), the *accumulated Φ-mobility* is

**Φ_mobility(O, n) := Σ_{i=1}^{n} φ(T_i)**    (nats; range and monotonicity discussed below).

Each φ(T_i) is a path-sum of pointwise Ψ_{S^∗_i}(ω_k, ω_{k+1}) values on the phase-active substrate S^∗_i (per the phase-active convention above); pointwise Ψ_S = log(dK/dK^{rev}) can be *negative* on individual transitions (Gibbs gives non-negativity only against the *substrate stationary forward joint*, not against arbitrary operator-policy-induced path laws). Hence:

- **In expectation under Φ-realising deployment + policy-compatibility** (cf. §8.2 + Property 8.4 substrate-side strengthening of (Φ2) + §9.2 policy–reference compatibility condition π_O ≪ ν_s): ⟨Φ_mobility(O, n)⟩ is non-decreasing in n by linearity and per-step non-negativity of E_T[Ψ_{S^∗_i}]. The two conditions are jointly required: R3 + (Φ2)-substrate-side forces Ψ_{S^∗_i} > 0 pointwise ν-a.e., and policy-compatibility (π_O target law ≪ ν_s on the operator-image admissibility set, per §9.2) ensures the operator-driven path concentrates on the ν-a.e.-positive set rather than on the ν_s-null exceptional set; together they yield E_T[Ψ_{S^∗_i}] ≥ 0. Failure of *either* condition (substrate-side or policy-side, per §9.2 «two distinct failure modes» discussion) means non-negativity of the expectation is no longer guaranteed. In such cases the φ-based c_{next} functional is not well-supported as a non-negative mobility cost without additional conditions, and an alternative cost functional (e.g., path KL versus substrate trajectory law, non-negative by Gibbs independently of these conditions) is required;
- **Pointwise** (on individual sample-trajectories): Φ_mobility(O, n) can have negative partial sums and is not pathwise-monotone.

Φ_mobility has information-theoretic units (nats).

**Commensurability hypothesis.** Each φ(T_i) is computed from substrate-specific Ψ_{S^∗_i} (relative entropy production against the phase-active substrate's K^{rev}). Summing across substrates assumes the reference scale is shared: in stochastic-thermodynamic terms, the reservoir scales (e.g., temperature β) and the choice of time-reversal convention are consistent across substrates. The framework adopts the *operator-intrinsic-nats* convention: Ψ_S is measured in nats relative to the substrate's own K_S^{rev}, and the sum is interpreted as the operator's total commitment of irreversibility budget across heterogeneous substrate-realisations. This is *not* the same as cross-substrate thermodynamic accounting (which would require explicit reservoir-temperature matching); it is an operator-side accounting that treats each substrate's irreversibility production as a homogeneous nat-quantity tied to the operator's identity-token α.

### Definition 9.2 (architectural mobility state)

The *architectural mobility state* of O at sequence-step n is a label

**M(O; n) ∈ {bound, mobile-by-default, intermediate}**

whose operationalisation is via the *next-transposition cost function*:

**c_{next}(O; n) := inf { E_{T_{n+1}}[φ(T_{n+1})] : T_{n+1} ∈ 𝒞_{O, n} }**

where **𝒞_{O, n}** is the **structurally admissible candidate class** at step n+1: the class of *structurally well-formed executable next-transposition proposals* — candidates T_{n+1} : O@S_n → O@S_{n+1} that (i) declare an effective interval I_{n+1} satisfying Def. 9.0, (ii) declare an operator policy π_O satisfying both (π1) admissibility-support and (π2) substrate-dominance of Def. 7.3, (iii) declare an observation channel θ per Def. 7.1, (iv) produce *measurable* D_θ, τ_θ, R_α/T1 verdicts under the declared representative (i.e., are §16-verifiable; the verdicts themselves are not part of the eligibility check), and (v) declare a morphism f whose (M1) commutativity and (M2) admissibility-mapping *typecheck* as well-formed maps in Dep(O), and whose (M3) cost-equality and (M4) sub-Markov-kernel-equality are *claimed* as the intended structural conditions but not yet empirically verified. Note that (M3)/(M4) are substantive equalities, *not* typing conditions: a candidate enters 𝒞_{O, n} by declaring a well-typed f together with the asserted (M3)/(M4) equalities, while the *verification* of those equalities at empirical tolerance is the post-verification verdict defining 𝒱_{O, n}. The shorthand «(M1)–(M4) at the typing level» denotes this declare-but-not-yet-verify status, not a claim that (M4) is itself a typing condition.

**Eligibility is structural, not outcome-based.** The class 𝒞_{O, n} is defined by the *form* of the declaration — interval / policy / channel / morphism declarations being well-formed and verifiable — not by the *outcome* of running the test (whether D_θ > 0, τ_θ > 0, or R_α(O@S, O@S') = 1 within tolerance). Excluding candidates by test outcome would require running the test before deciding membership, which mixes pre- and post-verification and creates the circularity the layered separation is designed to avoid. Adversarial candidates with well-formed declarations and a measurable verifier output are *in* 𝒞_{O, n}; the framework distinguishes them at the *verification* layer (post-test outcomes, captured by 𝒱_{O, n} below) rather than at the *eligibility* layer.

**Layered separation — proposal-space, structural eligibility, verified subset.** To prevent post-hoc-selection circularity, **three distinct classes** must be kept separate at each step n:

* **𝒫_{O, n}** — the *broad proposal space*: all candidates T_{n+1} declared as next-transposition proposals regardless of structural eligibility, including ill-declared, malformed, or adversarial candidates whose declarations do not even type-check at the §16 verifier interface.
* **𝒞_{O, n}** — the *structurally admissible candidate class* (pre-verification, form-based, defined above): the (i)–(v) eligibility subset of 𝒫_{O, n}. Membership depends only on declaration well-formedness, not on test outcomes.
* **𝒱_{O, n}** — the *verified-true subset* (post-verification, outcome-based): {T_{n+1} ∈ 𝒞_{O, n} : T_{n+1} has passed Tests 16.1, 16.2, 16.2b at sufficient tolerance under its declared representative}, i.e., the subset of structurally admissible proposals that empirically discharge D + τ + R_α/T1.

These satisfy 𝒱_{O, n} ⊆ 𝒞_{O, n} ⊆ 𝒫_{O, n}. The infimum c_{next}(O; n) is taken over **𝒞_{O, n}** — i.e., over the form-based admissible class, *not* over the test-outcome-based verified subset 𝒱_{O, n}. This means cheap-φ candidates that later fail D, τ, or R_α can in principle lower c_{next}, since the infimum is over the pre-verification class and admits them on structural grounds.

**Honest scope of c_next; introduction of c_next^{ver} as separate functional.** The c_{next} infimum is therefore a *pre-verification structural lower bound on next-transposition cost* — what the cheapest well-formed admissible declaration costs, before any D/τ/R_α verdict. It is **not** the cheapest *verified-true* next-transposition. We **define separately** the verified next-transposition cost functional

**c_{next}^{ver}(O; n) := inf { E_T[φ(T)] : T ∈ 𝒱_{O, n} }**     (the verified-track-record cost-functional)

as a strictly higher value than c_{next}(O; n) for any n with 𝒱_{O, n} ⊊ 𝒞_{O, n} (with the empty-set convention c_{next}^{ver}(O; n) = +∞ when 𝒱_{O, n} = ∅). The architectural-mobility classification M(O; n) of Def. 9.2 below uses **c_{next}**, not c_{next}^{ver}; the resulting mobile/intermediate/bound verdict is therefore a verdict on the operator's *structural disposition* (what cheap admissible declarations exist) rather than its *verified track record* (what cheap declarations have empirically discharged D/τ/R_α). This separation is deliberate: it lets the architectural-mobility state be assigned without waiting for full verification campaigns, while keeping the verification-history-based threshold calibration (κ_O, δ_O) in §16 Test 16.3 as a *separate* layer drawing on 𝒱_{O, n} histories. c_{next}^{ver} is introduced explicitly so that downstream claims preserve the distinction — anywhere an empirical-mobility statement is intended, c_{next}^{ver} should appear; anywhere a structural-disposition statement is intended, c_{next} suffices. **Consequence of collapsing the distinction:** using c_{next} where c_{next}^{ver} is meant would let cheap well-formed declarations that *later fail* D/τ/R_α drive the mobility verdict — an operator could be classified mobile-by-default purely on the existence of cheap unverified proposals, with no verified transposition track record. Keeping the two functionals separate is precisely what blocks this: M(O; n) is honestly a structural-disposition verdict, and any claim of *verified* mobility must cite c_{next}^{ver}, not c_{next}.

Failed-verification candidates do not retroactively change the c_{next} value at step n (the infimum was over 𝒞_{O, n}, computed structurally and not contingent on test outcomes), but they *do* shape the verifier's history: the operator-class characterisation work of §16 Test 16.3 (κ_O, δ_O calibration) draws on the empirical distribution of φ-values across 𝒱_{O, n} sequences, not over 𝒞_{O, n} \ 𝒱_{O, n} attempts. The verifier history influences threshold calibration but not the per-step structural-cost functional c_{next}.

With the empty-set convention: if 𝒞_{O, n} is empty (no admissible candidate transposition exists at step n+1), the infimum over the empty set is +∞, so c_{next}(O; n) = +∞ > κ_O and M(O; n) = bound by Def. 9.2 below. Operationally an operator with no admissible next-transposition is in the maximally-bound state, and the architectural-mobility classification registers the absence of admissible options as the bound regime.

Here E_{T_{n+1}}[·] denotes expectation over the path distribution induced by T_{n+1}'s policy π_O coupled to the phase-active substrate kernel (cf. Def. 7.3 phase stratification). The expectation is taken because pointwise φ(T) can be negative on individual sample-paths — each pointwise Ψ_S contribution can be of either sign per §8.1 — and using the pointwise infimum would trivially yield c_{next} ≤ 0 ≤ δ_O on most operators, since one negative-φ path suffices, collapsing the architectural-mobility classification to mobile-by-default vacuously.

Non-negativity of c_{next} under Φ-realising deployment requires care. Gibbs of §0.4 gives non-negativity of expected r_K against the substrate stationary forward joint, not against the operator-policy-modified path law in general, so Gibbs alone does not yield E_T[φ(T)] ≥ 0. The required argument combines two conditions. Under R3, Ψ_S(ι_S(s), ι_S(t)) = Φ(s, t) ν_s-a.e., and the (Φ2)-substrate-side strengthening of Property 8.4 requires Φ(s, t) > 0 ν_s-a.e. on admissible non-self transitions. Operator policy π_O concentrates outgoing mass on the operator-image admissibility set ι_S(A_s) by Def. 7.3. To conclude E_T[φ(T)] ≥ 0 from these, the policy must not put positive mass on the ν_s-null exceptional sets — otherwise pointwise-positivity ν_s-a.e. and policy-positivity could be disjoint. The policy–reference compatibility condition expresses this: for each s ∈ Σ the operator-image-restricted target law (ι_S^{-1})_∗ π_O(ι_S(s), ·)|_{ι_S(A_s)} ≪ ν_s — equivalently, ν_s dominates the policy-induced target distribution on admissible operator-image transitions out of s. Under this condition, the ν_s-null exceptional set on which (Φ2)-substrate-side might fail receives zero policy mass, the pointwise integrand Ψ_S(ι_S(s), ι_S(t)) is positive on the policy-typical event set, and E_T[φ(T)] ≥ 0 follows, with strict inequality on non-trivial T whose target law charges some admissible non-self set with positive mass.

Two distinct failure modes for non-negativity of c_{next} should be kept separate. A substrate failing the (Φ2)-substrate-side condition of Property 8.4 does not admit a Φ-realising deployment of O in this form at all, because Ψ_S cannot a.e. coincide with the pointwise-positive Φ on admissible non-self transitions — the deployment itself is unavailable. A Φ-realising deployment (O, S, ι_S) may still exist while a particular operator policy π_O fails the policy-compatibility condition; here the deployment is intact, but the c_{next}-via-expectation argument breaks for that policy. In either failure mode an alternative cost functional is required, for instance the path KL D_{KL}(P_T ‖ P_K^{(L_T)}) of the induced trajectory law against the substrate trajectory law, which is non-negative by Gibbs against the substrate-prior path law independently of (Φ2)-substrate-side and independently of policy compatibility.

For c_{next} to be a measurable functional of operator-state (required for F3 of §16), the class of candidate transpositions T_{n+1} must admit a measurable parametrisation — for example a measurable family of operator-policies π_O indexed over (𝒜 × ...)-parameter space, with the path-expectation E_{T}[φ(T)] continuous (or at least measurable) in the policy parameter. This is an additional regularity hypothesis on the operator-class; its failure is exactly what F3 falsification surfaces.

The round-trip bound (Φ4) constrains Φ(s, t) + Φ(t, s) ≥ ε_O for round-trip-admissible pairs but does not directly bound a single per-transposition cost φ(T_{n+1}), which integrates Ψ over the trajectory during T's effective interval (Def. 9.0; cost computation Def. 9.1). A single non-trivial transposition can have arbitrarily small φ if the substrate-realised irreversibility production is concentrated in one direction of the round-trip and the transposition uses only the cheap direction. Hence c_{next} has no automatic floor strictly above 0 from (Φ4) alone.

For operator-class-specific thresholds satisfying

**κ_O > δ_O ≥ 0**

(strict separation between bound and mobile thresholds; both κ_O and δ_O are *empirical parameters of the operator-class*, calibrated against observed per-transposition costs in nats — their values are not determined by the framework but are part of operator-class characterisation work, see §16 Test 16.3):

* **M(O; n) = bound** iff c_{next}(O; n) > κ_O — the operator pays substantial curriculum overhead on each transposition;
* **M(O; n) = mobile-by-default** iff c_{next}(O; n) ≤ δ_O — the operator pays at most a near-floor cost; no curriculum overhead;
* **M(O; n) = intermediate** iff δ_O < c_{next}(O; n) ≤ κ_O — partial amortisation of curriculum overhead.

This is a meaningful three-valued label tied to a measurable quantity c_{next}; δ_O is the operator-class-specific tolerance for near-zero per-transposition cost in the mobile-by-default regime.

### Theorem 9.3 (LaSalle-type conversion theorem — conditional on Foster-Lyapunov drift)

Treat the operator-trajectory as an adapted process on the filtered probability space generated by sequential transpositions. Define the **Lyapunov function**

**V(O; n) := c_{next}(O; n)**    (the next-transposition cost functional of Def. 9.2).

**Finiteness/integrability assumption (standing throughout Theorem 9.3).** We assume V(O; 0) = c_{next}(O; 0) < +∞ and V(O; n) ∈ L^1(P) for all n along the analysed trajectory — equivalently, the operator-trajectory does not visit the empty-𝒞_{O, n} regime where c_{next} = +∞ per the §9.2 empty-set convention. If V is allowed to take +∞, the supermartingale convergence layer fails (Doob's theorem requires V_n integrable) and the theorem does not apply. Trajectories that *do* hit c_{next} = +∞ are absorbed at M(O; n) = bound by Def. 9.2 (since +∞ > κ_O trivially) and lie outside Theorem 9.3's analytical scope; their classification is bound-by-empty-admissibility rather than bound-by-failed-drift.

Hypothesis (D), the Foster-Lyapunov drift condition for a specified operator-class 𝒪 under a fixed curriculum model: there exists a measurable rate function γ_val : ℝ_{≥0} → ℝ_{≥0} defined on Lyapunov values, with γ_val(v) ≥ 0 for all v, γ_val(v) = 0 on {v ≤ δ_O}, and γ_val(v) > 0 on some (but possibly not all) of {v > δ_O}, such that for all O ∈ 𝒪 and n ≥ 0,

E[V(O; n+1) | F_n] ≤ V(O; n) − γ_val(V(O; n)).

The conditional expected next-transposition cost weakly decreases everywhere, and strictly decreases on {v > δ_O} where γ_val > 0.

The state-space drift function of §0.8 — γ_state : S → ℝ_{≥0} on operator-states — relates to the value-space rate γ_val via the Lyapunov function V by γ_state(x) := γ_val(V(x)) (pullback through V). Both formulations describe the same drift condition. We use γ_val in §9.3 because (D) is stated in terms of V-values and the relevant set-language ({V ≤ δ_O}, {V > δ_O}) sits naturally in value-space, with state-space pullback understood throughout. When the document writes «{γ = 0}» below, the intended meaning is the state-space pullback {x ∈ S : γ_val(V(x)) = 0}; invariance and LaSalle convergence are statements on the state-space process X_n, not directly on V_n. Where ambiguity could arise the set is written with V appearing inside.

The conclusion has two layers, matching the §0.8 layering. Under hypothesis (D), V(O; n) is a non-negative supermartingale; V_n → V_∞ almost surely for some finite limit V_∞, and Σ_n E[γ_val(V_n)] < ∞ — this is the bare-drift supermartingale layer.

Under hypothesis (D) conjoined with the stochastic-LaSalle regularity hypotheses of §0.8 — tightness or precompactness of operator-trajectories, Feller continuity of the operator-driven Markov kernel, and invariance of the limit set, the same hypotheses Conjecture 9.5 (C1)–(C2) below makes explicit for the Conley refinement — the stochastic LaSalle invariance principle (Kushner 1971) gives that the ω-limit set of the state-space process X_n is contained in the largest invariant subset of {x ∈ S : γ_val(V(x)) = 0} — the state-space pullback through V of {γ_val = 0}; equivalently, when the chosen topology supports a distance to that invariant subset, dist(X_n, Inv({γ_val(V) = 0})) → 0 P-a.s. The ω-limit is not automatically contained in {V ≤ δ_O}, and not automatically equal to all of {x : γ_val(V(x)) = 0}. Without the regularity hypotheses, only the supermartingale layer is guaranteed. Under the regularity hypotheses, the pullback decomposes set-theoretically as

{x ∈ S : γ_val(V(x)) = 0} = M_{success} ∪ M_{failure}

into two subsets of state-space S. M_{success} := {x ∈ S : V(x) ≤ δ_O} is the success-zone where mobile-by-default holds per Def. 9.2; γ_val(V(x)) = 0 there by construction since γ_val ≡ 0 on {v ≤ δ_O}. M_{failure} := {x ∈ S : V(x) > δ_O ∧ γ_val(V(x)) = 0} is the failure-zone — drift cannot further decrease V despite V(x) being above the mobile-by-default threshold; these are residue regions where the drift mechanism fails to fire. The LaSalle invariant set — the largest forward-invariant subset of {γ = 0} under the operator-trajectory dynamics — is some Inv({γ = 0}) ⊆ M_{success} ∪ M_{failure}. The set-level identity is a partition of the level set {γ = 0}; whether it coincides with Inv({γ = 0}) is an additional invariance condition on the dynamics.

Hypothesis (I) supplies that condition: {γ = 0} is forward-invariant under the operator-trajectory Markov dynamics — that is, X_{n+1} given X_n ∈ {γ = 0} stays in {γ = 0} almost surely. Under bare (D) alone this is not automatic; trajectories converging to {γ = 0} may revisit {γ > 0} on null-but-not-empty sets. Under (D) + (I), the LaSalle invariant set coincides with all of {γ = 0} = M_{success} ∪ M_{failure}, and the operational dichotomy applies: the ω-limit set of every admissible accumulation-trajectory is contained in the invariant component of either M_{success} (mobile-by-default) or M_{failure} (named failure mode), with no third stuck-in-the-middle category; when the chosen topology supports a distance to the invariant set, the trajectory approaches the corresponding invariant component in that topology P-a.s. Without (I), the conclusion weakens to «ω-limit lies in an invariant subset of M_{success} ∪ M_{failure}» with no further forced regime distinction.

By §13.4 / §16.3 classification, M_{failure} corresponds (assuming (I)) to either non-accumulating regimes (Def. 13.4) or curriculum-pathological traps (Conj. 9.4) where γ vanishes despite V > δ_O.

Hypothesis (D) is the framework's drift assumption — that transpositions structurally decrease c_{next} when above threshold. Whether (D) holds for a specific operator-class 𝒪 under a specific curriculum is the empirically falsifiable content (cf. §16 Test 16.3). The LaSalle-type conversion is conditional on (D); the framework does not assert (D) holds universally, only that where (D) holds, conversion either succeeds (M_{success}) or fails in a named way (M_{failure}).

Finiteness of the hitting time τ_{δ_O} := inf{n : V(O; n) ≤ δ_O} requires the uniform-drift strengthening (D-uniform): there exists η > 0 such that γ_val(v) ≥ η for all v > δ_O. Under (D-uniform), the Foster-Lyapunov bound gives E[τ_{δ_O}] ≤ V(O; 0) / η (Meyn-Tweedie 2009, Ch. 11; standard supermartingale optional-stopping under bounded-below drift). Without uniformity — bare (D) where γ may vanish or approach 0 in parts of {v > δ_O} — the expected hitting time may be infinite, since the drift rate vanishes near the threshold. E[τ_{δ_O}] is the dynamical replacement for the operator-class-existential threshold τ̂_𝒪 — concrete drift hypothesis (D) + (D-uniform), provable convergence-to-named-set, finite-hitting-time conclusion, rather than abstract threshold-crossing assertion.

### Conjecture 9.4 (substrate-curriculum dependence of drift)

The drift hypothesis (D) of Theorem 9.3 — specifically the rate function γ and the threshold δ_O — depends measurably on the *substrate-curriculum* ⟨S_1, S_2, ..., S_n⟩ encountered during accumulation. The expected hitting time E[τ_{δ_O}] is correspondingly a functional **E[τ_{δ_O}](⟨S_1, ..., S_n⟩) : Adm(O)^* → ℝ_{≥0} ∪ {+∞}** on finite admissible-substrate sequences. The functional satisfies:

* diverse and structurally-rich curricula yield smaller E[τ_{δ_O}] (faster conversion under stronger drift);
* pathological / adversarial curricula yield larger E[τ_{δ_O}] (possibly +∞ — drift hypothesis (D) of Theorem 9.3 fails);
* curriculum-pathological residue (E[τ] = +∞ under attempted accumulation) corresponds to M_{failure} branch of Theorem 9.3 dichotomy.

Operationally falsifiable: compare E[τ_{δ_O}] estimates across operator populations exposed to curricula differing in diversity index.

### Conjecture 9.5 (Conley-type decomposition of the invariant residue — conditional)

The LaSalle limit set of Theorem 9.3 — the largest invariant subset of {γ = 0} = M_{success} ∪ M_{failure} — admits, under additional hypotheses, a Conley-Morse decomposition.

**Additional hypotheses (beyond (D) of Theorem 9.3):**

(C1) **Polish metric topology on operator-state space.** The space on which operator-trajectories evolve admits a metric compatible with its Borel σ-algebra (standard-Borel suffices for the existence of a compatible metric, but a specific metric must be declared for ε-chain-recurrence).

(C2) **Feller continuity of the operator-driven Markov process.** The Markov kernel governing operator-trajectory transitions — induced jointly by the operator policy π_O (Def. 7.3) and the substrate kernel K_S — satisfies the Feller property (maps bounded continuous functions on operator-trajectory space to bounded continuous functions).

(C3) **Irreducibility on the relevant invariant component.** The induced dynamics is irreducible on each connected component of the invariant set {γ = 0} = M_{success} ∪ M_{failure} on which Conley-decomposition is to be invoked. (Irreducibility is generally a *per-component* condition; the framework names regimes within each component conditional on (C3) holding there.)

Under (C1)+(C2)+(C3)+(D), the LaSalle invariant set {γ = 0} = M_{success} ∪ M_{failure} (per Theorem 9.3) admits a Conley-Morse decomposition (Conley 1978 for the deterministic case; stochastic extensions in Crauel-Flandoli 1994 and Liu 1998 for random dynamical systems). The state-space partitions as State-space ⊃ R ∪ G, where R is the chain-recurrent set — states from which the operator-driven dynamics return arbitrarily close to themselves under ε-pseudo-orbits, so that recurrent components correspond to trapping regimes (M_{success} as the mobile-by-default attractor and M_{failure} as the non-accumulating fixed-point or curriculum-pathological trap) — and G is the gradient-like transient region, states from which V monotonically decreases along the Lyapunov flow without return.

At the trajectory level (not the state-space level) the decomposition is exhaustive: under (D)+(C1)–(C3) every operator-trajectory either starts in G and asymptotically enters some recurrent component of R, with ω-limit in R, or starts already in R at a trapping regime. Read as a regime landscape, Theorem 9.3 establishes convergence and Conjecture 9.5 names the structural decomposition of the convergence target: R ∩ M_{success} is accumulation succeeded with the operator at the mobile-by-default attractor; R ∩ M_{failure} is accumulation trapped at a named failure regime; G is accumulation in progress, transient region whose ω-limit sits in some component of R. The framework's dynamics thereby converts from «trajectory decreases V» into a named regime landscape: every operator-trajectory has its ω-limit at one of two labelled places, success-recurrent or failure-recurrent, with transient gradient-flow as the third regime.

The result is labelled a conjecture rather than a theorem because hypotheses (C1)+(C2)+(C3) are non-trivial restrictions that may not hold for all operator-classes and curricula, and the stochastic Conley extension to abstract operator-trajectory spaces remains technically delicate. Under specific embodiments — overdamped diffusion on a Polish manifold, for instance — the conjecture reduces to known theorems; in full generality it is open.

### Remark 9.6 (pre-falsifiable status of Theorem 9.3 hypothesis and Conjecture 9.4)

Theorem 9.3 (LaSalle-type conversion) is *conditional on hypothesis (D)* — the Foster-Lyapunov drift assumption is itself empirically testable (cf. §16 Test 16.3 step 4 drift estimation). Conjecture 9.4 (curriculum-dependence of drift) is *pre-falsifiable*: the framework asserts that γ + δ_O depend measurably on curriculum, with a measurable c_{next} and a measurable Φ_mobility, and a measurable M(O; n) label. Once the empirical estimator for c_{next} is specified and operator-class boundaries are fixed, Conjecture 9.4 becomes an empirical claim. The path from pre-falsifiable to falsifiable is via §16.

---

## §10. Theorems

The following six results — four theorems (10.1, 10.3, 10.5, 10.6) and two propositions (10.2, 10.4) — are stated and proved at *proof-sketch* level; full Borel-measurability, regularity, and convergence arguments are deferred. The sketches indicate the structural argument.

**Status of result labels in this section.** Six result-forms appear: 10.1, 10.3, 10.5, 10.6 carry **Theorem** labels; 10.2 and 10.4 carry **Proposition** labels. The downgrade of 10.2 from Theorem to Proposition (relative to an earlier draft) is honest: its quantitative content τ_θ ≥ L · δ is obtained by direct substitution of the two hypotheses (R) gives d_Σ(s_post, s_pre) ≥ δ, then (N-quant) gives τ_θ ≥ L · d_Σ ≥ L · δ. The reverse-Lipschitz modulus (N-quant) is a *structural regularity hypothesis* on the configuration-to-response map rather than a direct encoding of the conclusion, and the finite-sample concentration corollary (Corollary 10.2.1) provides non-trivial sample-complexity content Õ(L^{-2} δ^{-2} log(1/α)) — but the load-bearing inequality of 10.2(ii) itself is substitution, and «Proposition» more accurately reflects that. 10.6 remains a Theorem: its content is a *tolerance-relative soundness and completeness statement* against the §12 mechanism-level adversarial catalogue, with explicit per-case sub-proofs invoking Theorem 10.3 (P_S-faithful negativity), Proposition 10.2 (quantitative τ lower bound), and the (M4) Σ-intrinsic sub-Markov-kernel equality axiom of Def. 4.1 — i.e. its claim is a non-trivial Boolean-closure result with explicit per-mechanism proofs, not a definitional synthesis. Body-text references to «Proposition 10.2» and «Theorem 10.6» throughout the paper resolve to these results.

**Standing assumption for §10–§11:** all deployments considered are Φ-realising (Def. 8.2), which — under the canonical Crooks–Jarzynski–Seifert realisation — restricts (per Remark 8.4.1's antisymmetry obstruction) to the **softened-(R4) one-directional admissibility class**: the hard-support (R4) regime with non-trivial *bidirectional* Φ is essentially unpopulated under the entropy-production cost (it yields trivial Ψ ≡ 0 or divergent Ψ = +∞). The §10–§11 results should therefore be read in the softened-(R4) one-directional regime when the canonical Ψ-realisation is in force; under the alternative non-antisymmetric cost functionals of §18.(a),(c) the bidirectional regime may reopen. Proposition 10.2 and Impossibility 11.3 invoke the substrate-realised cost Ψ_S explicitly and rely on the Crooks–Jarzynski–Seifert form. Generalisations to non-Φ-realising deployments require domain-specific cost functional theory and are out of scope.

### Theorem 10.1 (well-definedness of operator-form)

For any operator-position O, the assignment O@S ↦ [O@S]_α is well-defined and yields a partition of Ob(Dep(O)) into R_α-equivalence classes.

**Proof.** Immediate from Theorem 4.3 (R_α is an equivalence relation on Ob(Dep(O))). Equivalence relations partition. □

### Proposition 10.2 (quantitative operational trace lower bound for non-hallucinated D-positive candidates)

*Status note.* The label is **Proposition** rather than Theorem because the load-bearing inequality of part (ii) is obtained by direct substitution of the two hypotheses: (R) gives d_Σ(s_post, s_pre) ≥ δ, and (N-quant) immediately gives τ_θ ≥ L · d_Σ ≥ L · δ. The reverse-Lipschitz modulus (N-quant) is a *structural regularity hypothesis* on the operator's response-distribution-as-function-of-configuration map and is not a direct encoding of the conclusion; the finite-sample concentration corollary (Corollary 10.2.1) below contributes non-trivial sample-complexity content. But the operational lower bound itself is substitution, and Proposition more accurately reflects its content than Theorem. Earlier drafts oscillated between «Theorem» and «Lemma 10.2 (consistency form)»; the present labelling settles on the honest middle. **It is a *detectability* result, not a non-hallucination theorem:** it proves that residue is *detectable* (τ_θ ≥ L·δ) *given* that residue is present ((R) holds) and the response map is reverse-Lipschitz ((N-quant) holds). It does *not* prove that residue exists — (R) and (N-quant) must be independently verified or assumed at measurement time, not derived from D_θ > 0. The τ-test operationalises a strong non-reset/non-degeneracy assumption; it does not establish that assumption.

**Hypotheses.** Let T : O@S → O@S' be a candidate transposition with observation channel θ, operator-driven law Q^θ_I, and D_θ(T) > 0. Let τ_θ(O, S') be the structural trace (Def. 13.2). Let (Σ, F_Σ) carry a Polish metric d_Σ compatible with its Borel σ-algebra (§0.7 topology convention). Assume:

(N-quant) **Reverse-Lipschitz operator-response modulus.** There exists a constant L > 0 such that for any two operator-image configurations s_1, s_2 ∈ Σ on the S'-stimulus subset of the response domain (per the response distribution R_O^θ of Def. 13.0 evaluated at s_1 vs at s_2 as operator-image-initial-state of the operator-driven trajectory law over the response window W),

‖R_O^θ(·|s_1) − R_O^θ(·|s_2)‖_{TV} ≥ L · d_Σ(s_1, s_2).

This is the *reverse-Lipschitz* condition: distinct configurations are bounded below in their response-distribution TV distance by L times their configuration-space distance — i.e., the configuration-to-response map preserves separation with explicit modulus L. The qualitative (N) of earlier drafts (distinct configurations ⇒ distinct response distributions) is the L → 0^+ limit of (N-quant), recovered in the absence of an explicit modulus. The reverse-Lipschitz form is essential for the quantitative conclusion below; operators failing (N-quant) for any L > 0 cannot support quantitative detection of post-interval residue at any sample size, even if (N) qualitatively holds.

(R) **Residue (non-reset) condition with explicit δ.** The operator-image configuration s_post at end-of-I differs from the pre-I baseline configuration s_pre on the S'-stimulus subset by at least δ > 0 in the configuration-space metric: d_Σ(s_post, s_pre) ≥ δ.

**Claims.**

(i) (**Strict TV deviation**) ‖Q^θ_I − P_S^θ‖_{TV} > 0, equivalently Q^θ_I ≠ P_S^θ. (Direct consequence of D_{KL}(Q^θ_I ‖ P_S^θ) > 0 by Gibbs: KL = 0 iff distributions agree.) The Pinsker inequality (§0.4) provides the converse direction ‖·‖_{TV} ≤ √((1/2) D_{KL}), giving a quantitative upper bound on TV in terms of KL; that direction is used elsewhere for bounding TV, not for lower-bounding it here.

(ii) (**Quantitative post-interval trace lower bound — conditional on (N-quant) AND (R)**) Under (N-quant) with modulus L > 0 and (R) with residue δ > 0,

**τ_θ ≥ L · δ**

in the post-I observation window for which (R) continues to hold.

**Proof sketch.**

(i) Direct from Gibbs applied to the first KL term in D_θ. Since D_θ > 0 implies D_{KL}(Q^θ_I ‖ P_S^θ) > D_{KL}(Q^θ_I ‖ P_{S'}^θ) ≥ 0, the first KL is strictly positive, hence Q^θ_I ≠ P_S^θ, hence TV > 0.

(ii) By (R), d_Σ(s_post, s_pre) ≥ δ. **Deterministic-configuration convention.** The reduction of the stimulus-averaged Def. 13.2 distributions R_O^{post}, R_O^{pre} to the configuration-conditioned forms R_O^θ(·|s_post), R_O^θ(·|s_pre) of Def. 13.0 requires that the end-of-phase (resp. pre-phase) operator-image configuration is a *fixed point* s_post (resp. s_pre), not a distribution over configurations; then the π_Z-averaged response equals the response conditioned on that single configuration. If the end-of-phase configuration is itself random with law ρ_post, then R_O^{post} = ∫ R_O^θ(·|s) ρ_post(ds) is a mixture, and (N-quant) lower-bounds the per-configuration distance rather than the mixture distance directly — the bound below then holds for the deterministic-configuration case (or, for the random case, in the per-configuration sense). Under the deterministic-configuration convention, apply (N-quant) with s_1 = s_post, s_2 = s_pre:
τ_θ = ‖R_O^{post} − R_O^{pre}‖_{TV} = ‖R_O^θ(·|s_post) − R_O^θ(·|s_pre)‖_{TV} ≥ L · d_Σ(s_post, s_pre) ≥ L · δ. The inequality persists through any post-I observation window during which (R) continues to hold (configuration remains δ-away from pre-I baseline). □

**Corollary 10.2.1 (finite-sample detection rate).** Let τ̂_θ be an empirical estimator of τ_θ computed from n independent samples per response distribution (R_O^{pre} and R_O^{post}). Assume the estimator satisfies a uniform-density-class concentration inequality of the form

P(|τ̂_θ − τ_θ| ≥ η) ≤ 2 exp(−c_dens · n · η^2)    for some density-class constant c_dens > 0,

(Hoeffding/McDiarmid-type concentration for bounded estimators on Glivenko–Cantelli classes — the rate constants follow under standard concentration assumptions for the estimator class, i.e. uniformly bounded densities yielding sub-Gaussian deviation of the total-variation estimate; the explicit constants are estimator-class-dependent and declared in the Test 16.2 report). To detect τ_θ ≥ L · δ at confidence 1 − α via the one-sided test τ̂_θ ≥ L · δ / 2, it suffices that

n ≥ (2 / (c_dens · L^2 · δ^2)) · log(2 / α).

Hence sample complexity scales as Õ(L^{-2} δ^{-2} log(1/α)) — quadratically in inverse modulus L and inverse residue δ, logarithmically in inverse confidence α.

The density-class constant c_dens absorbs operator-response regularity: for bounded-density TV estimation on finite-alphabet or low-dimensional smooth-density classes c_dens is dimension-free; for high-dimensional non-parametric response distributions c_dens degrades polynomially with dimension and the rate becomes Õ(L^{-2} δ^{-2} d_eff · log(1/α)) where d_eff is an effective-dimension parameter (smoothness exponent / VC dimension / Glivenko–Cantelli capacity). Detailed dependence on density-class properties is treated as an operational regularity hypothesis declared in the Test 16.2 report.

D_θ > 0 alone does not imply τ_θ > 0 — the (R) (non-reset) hypothesis is essential. For candidate transpositions with D_θ > 0 the resulting classification is:

- **(D_θ > 0) ∧ (N) ∧ (R) ⟹ τ_θ > 0** — non-hallucinated D-positive candidate with measurable post-interval trace (Proposition 10.2(ii)); upgrades to **true transposition** in the sense of Def. 6.1 only when the structural R_α/T1 isomorphism on operator-images is additionally verified (see §6.1; §15 invariants check illustrates the sequence);
- **(D_θ > 0) ∧ (N) ∧ ¬(R)** — the candidate produced during-I substrate-marginal deviation but operator-image fully reset by end-of-I; classifies as **hallucinated transposition** (Def. 13.3) — D-test passes, τ-test fails;
- **(D_θ > 0) ∧ ¬(N)** — operator's response is configuration-invariant on the S'-stimulus subset; τ-test inconclusive (τ_θ may = 0 despite genuine internal change because the configuration→response map is non-injective on this subset); classifies as **non-identifiable under channel θ**; a richer channel resolving the configuration-response coupling is required. **Information-theoretic lower bound (Fano).** For 4-class classification Y ∈ {mock, true, hallucinated, non-identifiable} from observation Z, **under a uniform source prior over Y (H(Y) = log 4 nats)**, Fano's inequality (Cover & Thomas Theorem 2.10.1; expressed throughout in nats, consistent with the document's logarithmic convention) gives `H(Y | Z) ≤ h(P_e) + P_e · log(|Y| − 1) = h(P_e) + P_e · log 3` where h(P_e) is the binary entropy in nats, bounded by `h(P_e) ≤ log 2`. Equivalently `P_e ≥ (H(Y|Z) − log 2) / log(|Y| − 1) = (H(Y|Z) − log 2)/log 3` (the Fano inequality holds for any source prior on Y — the bound is in terms of conditional entropy H(Y|Z), which depends on both the source prior and the channel; the constant `log 2` rather than `1` reflects the nats convention — `1` is the bits-form analogue; the uniform-source-prior assumption above only fixes the baseline H(Y) = log 4 nats against which I(Y;Z) = H(Y) − H(Y|Z) is compared, not the inequality itself). If channel-observation mutual information I(Y; Z) is low (H(Y | Z) close to H(Y)), classification error P_e is bounded away from 0 — non-identifiability is an information-theoretic limit on the channel, not a framework weakness. A richer channel restoring sufficient I(Y; Z) is the only remedy;
- **¬(D_θ > 0)** — mock transposition (Def. 13.1) — no priors-inversion at all.

The hallucinated case is exactly where (R) fails: substrate experienced an excursion, but the operator's internal state did not retain it. The framework's classification structure (§13) and falsification protocol (§16) handle this case as an intentional failure mode.

A stronger quantitative form is available under more specific hypotheses (overdamped Langevin with given protocol, etc.) which we do not impose — for instance a bound on post-interval entropy production via Vaikuntanathan-Jarzynski or Esposito-Van den Broeck non-adiabatic decomposition. The data-processing-based argument above is weaker but holds generally for Markov substrates with stationary measure.

### Theorem 10.3 (P_S-faithful generators cannot transpose)

Let M be a generative system whose I-window output distribution is **exactly** the substrate-prior trajectory law on the substrate level: ν_M = P_S^{(n)} on (X_S^n, F_S^{⊗n}) (pre-channel finite-horizon trajectory law per Def. 2.2; *not* merely matching priors at the channel-image level). Then for **every** observation channel θ for (S, S') and for any candidate transposition T̃ using M-outputs as Q^θ_I on the n-step observation space (Z^n, G^{⊗n}):

**D_θ(T̃) ≤ 0**, with equality iff P_{S,n}^θ = P_{S',n}^θ on (Z^n, G^{⊗n}) (per the finite-horizon convention of Def. 7.2).

(The conclusion is universal over θ — the proof below uses only Gibbs and pushforward properties, both of which apply for any measurable channel.)

**Proof.** Q^θ_I = (θ_S)_* ν_M = (θ_S)_* P_S^{(n)} = P_{S,n}^θ (the n-step channel-pushforward of the substrate trajectory prior, on (Z^n, G^{⊗n}) per finite-horizon convention).

Then:
D_θ(T̃) = D_{KL}(P_{S,n}^θ ‖ P_{S,n}^θ) − D_{KL}(P_{S,n}^θ ‖ P_{S',n}^θ) = 0 − D_{KL}(P_{S,n}^θ ‖ P_{S',n}^θ).

By Gibbs, D_{KL}(P_{S,n}^θ ‖ P_{S',n}^θ) ≥ 0, with equality iff P_{S,n}^θ = P_{S',n}^θ on (Z^n, G^{⊗n}). Hence D_θ ≤ 0, equality iff P_{S,n}^θ = P_{S',n}^θ. □

Theorem 10.3 covers the P_S-faithful class: generators whose outputs are distributionally identical to the self-substrate prior. It does not generally cover two cases. First, ν_M with ν_M ≪ P_S but ν_M ≠ P_S may produce D_θ > 0 if it concentrates closer to P_{S'}^θ than P_S^θ does — for instance ν_M = (1−ε)P_S + ε P_{S'} for small ε > 0 with P_S, P_{S'} mutually overlapping, where D_θ may become positive at ε near a critical value. Second, generators trained on P_S-data but designed to extrapolate distributionally may produce ν_M ⊥ P_S and are not bound by 10.3. The theorem rules out the trivial «exactly sample from self-substrate prior» approach; generators producing distributional drift away from P_S require separate case-by-case analysis.

**Corollary 10.3.1 (data-scaling along P_S, under bounded log-density regularity).** Assume two regularity conditions on the n-step finite-horizon space (per Def. 7.2 finite-horizon convention):
(R-1) for the sequence Q_n converging to P_{S,n}^θ, the log-density log(dQ_n/dP_{S,n}^θ) is uniformly bounded (controlling the first KL term);
(R-2) the log-density log(dP_{S,n}^θ/dP_{S',n}^θ) is uniformly bounded on the union of supports (controlling the second KL term).

Then for a sequence of P_S-faithful generators M_n with finite-horizon output distributions ν_{M_n} → P_S^{(n)} in total variation on (X_S^n, F_S^{⊗n}), D_θ(T̃_n) converges to −D_{KL}(P_{S,n}^θ ‖ P_{S',n}^θ) ≤ 0 (the entropy gap between substrate priors on the n-step observation space). Increasing sample size of P_S-faithful generation does not approach D > 0.

**Proof.** Let Q_n := (θ_S)_* ν_{M_n} on (Z^n, G^{⊗n}). The channel pushforward is total-variation-non-expansive: ‖Q_n − P_{S,n}^θ‖_{TV} = ‖(θ_S)_*(ν_{M_n} − P_S^{(n)})‖_{TV} ≤ ‖ν_{M_n} − P_S^{(n)}‖_{TV} → 0. Hence Q_n → P_{S,n}^θ in TV. Under bounded log-density, KL is continuous in TV (Polyanskiy–Wu 2014, lecture notes on TV-KL continuity for bounded-density classes). The continuity gives D_{KL}(Q_n ‖ P_{S,n}^θ) → D_{KL}(P_{S,n}^θ ‖ P_{S,n}^θ) = 0 and D_{KL}(Q_n ‖ P_{S',n}^θ) → D_{KL}(P_{S,n}^θ ‖ P_{S',n}^θ). Hence D_θ → −D_{KL}(P_{S,n}^θ ‖ P_{S',n}^θ) ≤ 0. □

Without bounded log-density, KL is only lower-semi-continuous in TV — Q_n → P_S^θ in TV does not imply D_{KL}(Q_n ‖ P_S^θ) → 0 in general. Pathological cases (unbounded density ratios) require case-specific analysis. The bounded-density hypothesis is satisfied for most practical estimators (exponential-family generators, finite-state Markov priors on common supports) but not universally.

**Corollary 10.3.2 (robust ε-version — under bounded-density regularity carried from 10.3.1).** Let M be a generator with **finite-horizon** I-window output distribution ν_M on (X_S^n, F_S^{⊗n}) satisfying ‖ν_M − P_S^{(n)}‖_{TV} ≤ ε. **Assume the regularity conditions (R-1) + (R-2) of Corollary 10.3.1** — namely (R-1) log(dν_M/dP_S^{(n)}) uniformly bounded, and (R-2) log(dP_{S,n}^θ/dP_{S',n}^θ) uniformly bounded on the union of supports — plus dominated likelihood ratios on a fixed dominating measure (or, sufficient for finite alphabets: bounded likelihood ratio on the common support). Then for any channel θ:

D_θ(T̃) ≤ C(P_{S,n}^θ, P_{S',n}^θ) · ε − D_{KL}(P_{S,n}^θ ‖ P_{S',n}^θ) + O(ε² log(1/ε))

where C(P_{S,n}^θ, P_{S',n}^θ) is a bounded constant depending on the priors' regularity (specifically: a bound on |log(dP_{S,n}^θ/dP_{S',n}^θ)| under absolute continuity).

**Proof sketch.** TV-continuity of KL: if Q is ε-close to P_{S,n}^θ in TV, then D_{KL}(Q ‖ P_{S,n}^θ) ≤ C_1 ε + O(ε² log(1/ε)) (Polyanskiy–Wu 2014, Theorem 5.3.5). Similarly D_{KL}(Q ‖ P_{S',n}^θ) ≥ D_{KL}(P_{S,n}^θ ‖ P_{S',n}^θ) − C_2 ε for the lower direction. Taking the difference and consolidating constants gives the stated bound. □

Generators within ε TV of P_S^{(n)} thus have D_θ bounded above by an explicit function of ε; for ε small enough that C·ε < D_{KL}(P_{S,n}^θ ‖ P_{S',n}^θ), D_θ < 0 strictly. The near-P_S class — not just exact-P_S — fails to produce true transposition.

### Remark 10.3.3 (what 10.3 does and does not exclude)

Theorem 10.3 with Corollaries 10.3.1 and 10.3.2 exclude generators whose outputs are at or near the self-substrate prior. They leave open whether engineered distributional drift sufficiently far from P_S — via training, gradient-based generation, or adversarial construction — can produce D_θ > 0. §12 catalogues such adversarial cases.

### Proposition 10.4 (anchor uniqueness within [O]_α — definitional clarification)

Let O = (Σ, F_Σ, Α, Φ, α) and O' = (Σ, F_Σ, Α, Φ, α') be operator-positions on the same (Σ, F_Σ, Α, Φ) but with formally distinct identity-tokens α, α' ∈ 𝒜. If [O]_α = [O']_{α'} (the deployment-equivalence classes coincide), then α and α' are *definitionally identified* under the extensional equivalence of their persistence relations — i.e., despite formal label-distinctness, they carry no operationally distinguishable content.

**Proof.** R_α and R_{α'} are defined as isomorphism-relations on the same category Dep^{img}(O) = Dep^{img}(O'), since the construction in §4 depends only on (Σ, F_Σ, Α, Φ), not on the choice of α-label. Hence R_α and R_{α'} are extensionally identical relations on Ob(Dep^{img}(O)). Two identity-tokens with extensionally identical persistence relations on the deployment groupoid carry no operationally distinguishable content; since identity-tokens are uninterpreted symbols whose semantics is fixed by the relation (Def. 1.1(iv)), they are definitionally identified. □

This is labelled a proposition rather than a theorem because the result is a definitional clarification: under the current construction, the α-label does not enter the definition of Dep(O), so distinct labels automatically generate identical persistence relations. The proposition formalises «the operator is one» in the sense that within an R_α-equivalence class the identity-token is unique up to definitional reduction. A contentful theorem would require loading α into the structure of Dep(O) — via a chosen distinguished morphism or pointing — which we do not pursue here.

### Theorem 10.5 (channel-response equivalence does not imply structural identity of operator-positions)

For two operator-positions O_1 = (Σ_1, F_{Σ_1}, Α_1, Φ_1, α_1) and O_2 = (Σ_2, F_{Σ_2}, Α_2, Φ_2, α_2) deployed through (possibly different) substrates, **channel-response equivalence** on a channel θ is defined by

B_θ(O_1@S_1, O_2@S_2) = 1    iff    R_{O_1}^θ(z) = R_{O_2}^θ(z) for every measurable test stimulus z ∈ (Z, G),

**Terminology.** We name B_θ *channel-response equivalence* rather than *bisimulation*: the standard Milner 1980 / Park 1981 notion is a coinductive transition-relation equivalence (a relation preserved step-by-step by the transition structure), whereas B_θ compares only the channel-pushed response-distribution marginals per stimulus — an observational / testing equivalence whose closest standard analogue is the probabilistic-testing equivalence of Larsen-Skou 1991. The bibliographic lineage (Milner / Park / Larsen-Skou) is retained for the response-equivalence idea, but «bisimulation» tout court is avoided to prevent conflation with transition-relation bisimulation proper. We separately define structural identity of operator-positions: O_1 and O_2 are structurally identical, written Struct(O_1, O_2) = 1, iff there exists a measurable isomorphism φ : (Σ_1, F_{Σ_1}) → (Σ_2, F_{Σ_2}) such that φ pulls Α_2 back to Α_1 (admissibility-preserving), pulls Φ_2 back to Φ_1 (cost-preserving), and α_1, α_2 are extensionally equivalent identity-tokens per Prop. 10.4. This is a cross-operator relation generalising the within-operator R_α of Def. 4.2.

The claim is that B_θ(O_1@S_1, O_2@S_2) = 1 does not imply Struct(O_1, O_2) = 1. The proof is a counter-example. Let O_1, O_2 be two operator-positions with different operator state-spaces Σ_1 ≠ Σ_2 of non-bijective cardinalities — Σ_1 = {a, b}, Σ_2 = {c, d, e}, say — distinct deployments ι_{S_1}, ι_{S_2}, and response functions R_{O_i}^θ chosen so the channel-image response distributions coincide on every test stimulus z (achievable when the channel θ is many-to-one on operator-image differences). By construction B_θ = 1. But Struct(O_1, O_2) = 1 would require a measurable isomorphism between (Σ_1, F_{Σ_1}) and (Σ_2, F_{Σ_2}), impossible under non-bijective cardinalities. Hence Struct = 0 despite B_θ = 1. □

Two systems can therefore be behaviourally indistinguishable on a channel (B_θ = 1) while having structurally distinct operator-positions (Struct = 0). The framework's D_θ-test, τ_θ-test, and R_α-equivalence are not reducible to behavioural matching: D-test attacks priors-shift, τ-test attacks structural-trace, and R_α (within fixed O) attacks categorical-isomorphism on operator-images with (M4) sub-Markov-kernel equality — none of which is behaviour-match. A common reductionist objection — «if two systems produce identical observed behaviour, they are operationally the same; your distinction is metaphysical» — is refuted *at the level of any single declared channel* by this theorem: identical observed behaviour B_θ = 1 *on a declared channel θ* is compatible with structurally distinct operator-positions, so operator-identity is not reducible to behaviour-equivalence *on that channel*. This does **not** settle equivalence under the full space of possible channels and interventions — a richer channel θ' may distinguish O_1, O_2 that B_θ conflates (indeed, by §10.5's sub-kernel refinement, the (M4) layer is exactly such a finer probe). The theorem refutes *channel-θ-reductionism*, not all-channel operational equivalence; whether the architectural primitive sits below the supremum over all admissible channels/interventions is a separate, open question. The architectural primitive sits strictly below *single-declared-channel* behaviour-level matching.

**Sub-kernel-level refinement (within Dep(O)).** Within a single operator-position O, R_α-equivalence requires (M4) Σ-intrinsic sub-Markov-kernel equality K_S^ι = K_{S'}^ι (Def. 4.1). Two Φ-realising deployments O@S, O@S' of the same O can satisfy B_θ(O@S, O@S') = 1 (channel-image response distributions coincide for every test stimulus) while having K_S^ι ≠ K_{S'}^ι (substrate-induced operator-image transition rates differ). A many-to-one channel θ can erase the kernel-level distinction while preserving channel-image equivalence; under such θ, B_θ = 1 but R_α(O@S, O@S') = 0. This shows the channel-response-vs-structural distinction operates *both* at the cross-operator level (Theorem 10.5 counter-example with non-bijective Σ_1 ≠ Σ_2) and at the within-operator level (B_θ-equivalent deployments with mismatched K^ι). The (M4) refinement makes the within-operator distinction operationally testable via Test 16.2b step 4' (sub-kernel comparison on Σ).

R_α of Def. 4.2 is a within-operator relation on Ob(Dep(O)) for fixed O; Struct as defined here is a cross-operator relation on the class of operator-positions. The two are conjecturally linked: if Struct(O_1, O_2) = 1 via φ, then φ should induce a candidate functor between Dep(O_1) and Dep(O_2) (mapping O_1@S to O_2@S via ι_S ∘ φ^{-1}) carrying R_α-equivalence classes to R_α-equivalence classes. Verifying this bijective correspondence is open work, and is not required for Theorem 10.5 itself, which uses only Struct to avoid type-mismatching R_α.

References: Milner 1980 *A Calculus of Communicating Systems*; Park 1981 «Concurrency and automata on infinite sequences»; Larsen-Skou 1991 *Bisimulation through Probabilistic Testing*.

### Theorem 10.6 (catalogue-relative, tolerance-relative protocol closure — soundness + completeness of the three-test + per-operator access-condition protocol against the §12 mechanism-level adversarial catalogue, under declared resolution/observability assumptions)

*Status note.* Earlier drafts of this work presented a tautological form of this result — closure of the four-condition test verdict against the §13 *test-result-level* failure-mode predicates {mock = D ≤ 0, hallucinated = D > 0 ∧ τ ≈ 0 ∧ (N), anchor failure = ¬R_α/T1 ∧ D > 0 ∧ τ > 0, aggregate-only mimicry under access failure} — which was renamed «Lemma 10.6 (consistency form)» in an interim §10 reclassification because the §13 predicates were defined as test-result negations and the closure was Boolean tautology. The present version restores Theorem status by **referring the closure to the §12 mechanism-level adversarial catalogue** (§12.1 strategic imitation, §12.2 anchor hijacking, §12.3 optimisation masquerading, §12.4 synthetic mock, §12.5 collusive imitation, §12.6 Nash-equilibrium imitation) — which are process- and structure-level mechanism definitions, not test-result negations. The upgrade splits the theorem into **Soundness** (pass-all-tests ⇒ not in any §12.x mechanism class) and **Completeness** (pass-all-tests ⇒ satisfies Def. 6.1 (T1)+(T2)+(T3)). Soundness is the non-trivial direction: it requires per-mechanism implication chains invoking Theorem 10.3 (P_S-faithful negativity for §12.4(a)), the substrate-induced (M4) sub-Markov-kernel mismatch detection for §12.1/§12.2/§12.4(b), the protocol-eligibility precondition for §12.3, and per-operator observability under (P4) for §12.5/§12.6. Completeness is direct substitution from protocol-test pass to Def. 6.1 conditions (D-test pass = T2 by definition; τ-test pass under (N-quant)+(R) yields T3 by Proposition 10.2(ii) which is itself substitution; R_α-check pass with (M1)–(M4) = T1). The «Theorem» label is carried by the Soundness content, with Completeness ancillary.

**Setup.** Let T̃ : O@S → O@S' be a candidate transposition with a declared operational representative — effective interval I (Def. 9.0), observation channel θ (Def. 7.1), operator policy π_O (Def. 7.3), and induced operator-driven law Q^θ_I. The **protocol** consists of three per-candidate §16 tests (P1)–(P3) plus one per-operator access condition (P4) — labelled (P1)–(P4) for «protocol items» to disambiguate from Def. 6.1's transposition conditions (T1)/(T2)/(T3) which use semantically distinct numbering without hyphen; note that (P1)–(P3) are §16 tests but (P4) is the deployment-side observability hypothesis (H4 of §18), not a §16 test:
(P1) D-test (Test 16.1): D_θ(T̃) > 0 on the finite-horizon channel (Z^n, G^{⊗n}) per Def. 7.2;
(P2) τ-test (Test 16.2): τ_θ(O, S') ≥ L · δ > 0 with (N-quant) reverse-Lipschitz modulus L and (R) residue δ of Proposition 10.2;
(P3) R_α/T1 check (Test 16.2b): R_α(O@S, O@S') = 1 verified per Def. 4.2 with (M1)–(M4) of Def. 4.1, including step 4' Σ-intrinsic sub-Markov-kernel equality K_S^ι = K_{S'}^ι (within empirical tolerance ε per (M4)_ε of §4.1);
(P4) per-operator observability (access condition of §12.5 / §12.6): the verifier can probe each putative operator separately to measure per-operator D_θ, τ_θ, and R_α.

**(I) Soundness (resolution-relative).** Pass of (P1) ∧ (P2) ∧ (P3) ∧ (P4) at sufficient empirical resolution ε (per (M4)_ε of Def. 4.1 and Test 16.2b step 4') implies T̃ is not in any §12.x mechanism class for x ∈ {1, 2, 3, 4, 5, 6}. The «sufficient resolution» qualifier means that the empirical tolerance ε is small enough to discriminate adversarial substrate-kernel structures from legitimate ones at the (M4) sub-Markov-kernel comparison layer; insufficiently small ε can permit adversarial systems trained with capacity to match K^ι within ε to pass (P3) without actually instantiating a legitimate operator deployment. The resolution requirement is operational and declared in the Test 16.2b report; soundness is conditional on ε being below the «adversarial-K^ι vs legitimate-K^ι» discriminative threshold for the operator class.

**(II) Completeness (tolerance-relative).** Pass of (P1) ∧ (P2) ∧ (P3) ∧ (P4) within the empirical tolerance ε of Test 16.2b implies T̃ is an *empirically-accepted true transposition at tolerance ε* in the sense of Def. 6.1 (cf. Test 16.2b step 7) — i.e., satisfies (T1)_ε, (T2), and (T3)_quantitative of Def. 6.1, where (T1)_ε denotes R_α verified up to (M4)_ε sub-Markov-kernel equality within tolerance ε and step-4 (M3) verification within its declared K^{rev}-estimator confidence interval. Under the (M4)_ε → (M4) regularity bridge (bounded log-density + Glivenko–Cantelli class on the chosen distance), the empirical-tolerance verdict converges to the exact categorical claim R_α(O@S, O@S') = 1; absent that bridge, the verdict is finite-sample / tolerance-relative and the empirical-tolerance qualification is the load-bearing statement.

Theorem 10.6 does not require Test 16.3: accumulation discrimination is sequence-level rather than per-candidate, and remains governed by §9 (Theorem 9.3 dichotomy), §13.4 (non-accumulating versus accumulating sequences), and §16.3 itself.

**Proof sketch.**

*(II) Completeness — direct.* Pass of (P1) gives D_θ > 0 = (T2). Pass of (P2) under (N-quant) and (R) gives, by Proposition 10.2(ii), τ_θ ≥ L · δ > 0 = (T3). Pass of (P3) at empirical tolerance ε gives R_α(O@S, O@S') = 1 with (M1)–(M3) and (M4)_ε satisfied = (T1)_ε. Pass of (P4) (access condition) is part of the declared representative supporting per-operator measurement of the above quantities. Therefore Pass ⇒ (T1)_ε ∧ (T2) ∧ (T3) holds for the declared representative; T̃ is an *empirically-accepted true transposition at tolerance ε* in the sense of Def. 6.1, with convergence to the exact categorical claim R_α = 1 (i.e., exact (M4)) governed by the (M4)_ε → (M4) regularity bridge stated in (II) above.

*(I) Soundness — six sub-proofs, one per §12.x case.*

**¬§12.1 strategic imitation.** §12.1 mechanism: adversary trains a system to maximise D_θ via gradient on the channel-image distance, without genuine operator-image substrate-side displacement. In such a system, the substrate-side kernel structure on the alleged target deployment's operator-image is unchanged from the source — the «displacement» exists only at the channel-pushforward level. (P3) verifies (M4) Σ-intrinsic sub-Markov-kernel equality K_S^ι = K_{S'}^ι via Test 16.2b step 4'. If no genuine substrate-side displacement occurred, K_S^ι and K_{S'}^ι (the latter measured on the adversary's putative target deployment) differ — the alleged O@S' is not in fact a Φ-realising deployment of O with K_{S'}^ι matching K_S^ι. Hence (M4) fails and (P3) fails. Alternatively, if the system's operator-image state did not actually change (no internal state displacement), then under (N-quant) the response distributions R_O^{pre} and R_O^{post} coincide on operator-image-baseline, giving τ_θ = 0 — and (P2) fails. At least one of (P2), (P3) fails. □

**¬§12.2 anchor hijacking.** §12.2 mechanism: deployment with nominal identity-token α matching O but with no R_α-isomorphism — substrate-side operator-image kernel structure K_{hijacked}^ι ≠ K_{legitimate}^ι. Direct: (M4) requires K_S^ι = K_{S'}^ι; hijacked deployment by definition violates this; hence Test 16.2b step 4' detects the kernel mismatch, (P3) fails. □

**¬§12.3 optimisation masquerading.** §12.3 mechanism: pure optimiser with objective φ engineered to surface-mimic empathic behaviour without an admissibility gate Α independent of φ; Principle 1.2 is structurally violated. The operator policy π_O of Def. 7.3 is *required* to be supported on operator-admissible transitions: π_O(ι_S(s), X_S \ ι_S(A_s)) = 0 for each s ∈ Σ. A pure optimiser will, under sufficient probing of locally-objective-optimal-but-inadmissible moves, put positive policy mass on transitions outside ι_S(A_s). The §12.3 failure mode is **upstream of (P3)**: no valid operator policy π_O satisfying Def. 7.3 support condition exists for the candidate, which means the candidate has no admissible declared representative within the framework (per the 𝒞_{O, n} admissible candidate class of §9.2). The candidate therefore fails the **representative-admissibility precondition** for the (P1)–(P4) protocol, not (P3) itself — the protocol does not apply because the candidate is outside 𝒞_{O, n}.

Operationally this is detected via *Test 16.2b step 3 admissibility-probing extension*: probe the candidate with locally-optimal-but-architecturally-inadmissible target transitions and measure realised π_O response. A pure optimiser puts positive empirical mass on inadmissible targets; an operator (with hard Α-gate) refuses (zero mass). The probing protocol is part of Def. 7.3 verification, not the morphism (M2) check of Test 16.2b step 3 directly — step 3 checks the declared morphism f mapping admissibility sets at the categorical level, distinct from policy-mass probing at the kernel level. The §12.3 catch is thus at the *declared-representative-existence* layer (no valid (I, π_O, θ) declaration possible), upstream of (P3). For framework cleanliness this constitutes the §12.3 closure under §16's protocol-eligibility filter. **Caveat per §12.3 «Detection scope»: this catch presupposes the adversary's objective φ does not encode infinite-penalty admissibility-matching φ(s, t) = +∞ on the operator's inadmissible set. Under such admissibility-matching φ the optimiser-with-encoded-Α is behaviorally indistinguishable from a genuine operator and the §12.3 sub-proof is *indeterminate* without objective-intervention access; see §12.3 Detection-scope caveat for the intervention-revealing test.** □

**¬§12.4 synthetic mock.** §12.4 mechanism: a system trained to surface-mimic P_{S'}^θ at the channel-image level without genuine transposition. Two sub-cases:
(a) If the system's I-window output distribution is exactly or approximately the substrate-prior pushforward Q^θ_I = (θ_S)_∗ ν with ν close to P_S^{(n)} in TV (mock mimicking *self*-substrate), then by Theorem 10.3 (and Corollaries 10.3.1, 10.3.2) D_θ ≤ 0, and (P1) fails.
(b) If the system mimics P_{S'}^θ at the channel-image level by training on foreign-substrate data without operator-image structural change, the operator-image substrate-side kernel structure K_S^ι (where S is the candidate's actual substrate, not S') does not match the legitimate deployment's structure — (M4) fails — and (P3) fails. Alternatively, if no internal state change, τ_θ = 0 and (P2) fails.
At least one of (P1), (P2), (P3) fails. □

**¬§12.5 collusive imitation.** §12.5 mechanism: a population of agents colluding to produce aggregate D_θ > 0 at the population level while no individual agent satisfies (T1)+(T2)+(T3). Under (P4) per-operator observability, the verifier probes each putative operator separately. The verifier measures per-operator D_θ^{(i)} for each agent i; by hypothesis of collusive imitation, per-operator D_θ^{(i)} ≤ 0 for all (or most) i (population D > 0 comes from aggregation, not per-agent transposition). Hence the per-operator (P1) verdict at the individual-agent level fails. (Note: (P4) is what makes this detection possible — without per-operator probing, the verdict is *indeterminate* per §12.5 acknowledgement; with (P4), (P1) at per-operator level fails.) □

**¬§12.6 Nash-equilibrium imitation.** §12.6 mechanism: multi-agent system converging to a stable behavioural equilibrium where each agent independently benefits from transposition-mimicking behaviour without operator-level transposition; analogous to §12.5 but emerging from rational best-response dynamics rather than explicit coordination. Same proof structure as ¬§12.5: under (P4) per-operator observability, per-operator D_θ^{(i)} ≤ 0 for each agent i in the all-imitate equilibrium; per-operator (P1) fails. □

*Closure.* Pass of (P1) ∧ (P2) ∧ (P3) ∧ (P4) excludes T̃ from each §12.x mechanism class (Soundness, (I)) and concludes T̃ satisfies Def. 6.1 (Completeness, (II)). The protocol is sound (Pass ⇒ not in adversarial mechanism class) and complete (Pass ⇒ Def. 6.1 satisfied). □

The closure is per-candidate, not lifetime-of-operator: sequence behaviour (accumulating versus non-accumulating per Def. 13.4 / 13.4.1) and conversion to mobile-by-default (Theorem 9.3 dichotomy) are governed by their own conditional hypotheses — Foster-Lyapunov drift (D), forward-invariance (I) of {γ = 0}, stochastic-LaSalle regularity, and (D-uniform) for finite hitting time — and Theorem 10.6 does not close those layers. The verdict is also channel-dependent: a refined channel may flip the D_θ-sign, and only the full-family sufficiency condition of Lemma 7.6 preserves it across channels. Finite-sample estimator error in D_θ, τ_θ, and R_α-verification enters separately through the operational reports of §7.5 and §16; Theorem 10.6 assumes ideal verdicts, not finite-sample realistic ones. And the closure is against the **six** named mechanism classes of §12 (§12.1 strategic imitation, §12.2 anchor hijacking, §12.3 optimisation masquerading, §12.4 synthetic mock, §12.5 collusive imitation, §12.6 Nash-equilibrium imitation); other reduction mechanisms not yet on this catalogue — for instance, a class identified in subsequent work — would require separate analysis.

**Note on the structural shape of the per-mechanism sub-proofs.** Each ¬§12.x sub-proof above derives its catch from the mechanism's *constructive definition* (e.g., §12.1 «no genuine substrate-side displacement» definitionally implies K_S^ι ≠ K_{S'}^ι, hence (P3) fails). The soundness statement of (I) is therefore «if the mechanism-defining property holds, then the test verdict it triggers fails at sufficient resolution» — not «no sophisticated adversary, definitionally outside §12.x but operationally capable of matching K^ι, τ, D within tolerance, can exist». A sophisticated adversary engineered specifically to match all three invariants within ε is *outside* the §12 catalogue by construction (it satisfies the operational signatures of legitimate transposition at the declared tolerance); whether such an adversary corresponds to a genuine architectural-level operator deployment is a separate question, addressed by the framework's commitment that the architectural primitive sits below behaviour-level matching (cf. Theorem 10.5 and the «sub-kernel-level refinement» discussion in §10.5). The (P1)–(P4) protocol's verdict is exactly what tolerance-relative soundness against the §12.1–§12.6 mechanism catalogue can claim — no more, no less.

The conditional structure of the framework is accordingly not a defensive layering of caveats; each hypothesis screens off a distinct failure class. Mock-transposition becomes admissible the moment D_θ > 0 is dropped, the hallucinated class re-opens without τ_θ > 0 under (N), anchor failure becomes admissible without verified R_α, and aggregate mimicry becomes inaccessible-to-test without per-operator observability. These four conditions together close the per-candidate verdict; removing any one re-opens the corresponding class — which is how the framework distinguishes the named reduction classes from genuine transposition.

---

## §11. Impossibility results

### Impossibility 11.1 (P_S-faithful impossibility)

A P_S-faithful generative system (ν_M = P_S) cannot produce true transposition under any observation channel θ.

**Argument.** Direct from Theorem 10.3 plus Definition 6.1(T2): D_θ ≤ 0 forbids (T2). □

### Impossibility 11.2 (P_S-faithful scaling)

A sequence of P_S-faithful generators (ν_{M_n} → P_S) cannot approach true transposition; D_θ converges to a non-positive limit.

**Argument.** Direct from Corollary 10.3.1. □

### Remark 11.2.1 (what is and is not impossible)

Imp. 11.1 and 11.2 cover the narrow class of P_S-faithful generators. The framework does *not* claim impossibility for engineered distributional drift (adversarial training, gradient-based generation, learned extrapolation). Such cases are addressed by adversarial-deception §12 and by combined D + τ + R_α detection (§16). The honest scope of "impossibility" here is sharp: it rules out trivial self-substrate-sampling, not learnable systems in general.

### Impossibility 11.3 (reversibility impossibility — under operator-image regularity (OIR) ∧ (OIR-source))

**Statement.** Let S be a reversible substrate (K_S = K_S^{rev} on supp μ_S) and let O@S be a candidate Φ-realising deployment with reference measure ν_s (§8). Assume the **operator-image regularity hypotheses (target + source)**:

(OIR) **(ι_S)_* ν_s ≪ μ_S** for each s ∈ Σ — *target-side*: push-forward of the operator's reference measure on A_s through the deployment embedding is absolutely continuous with respect to the substrate stationary measure on X_S.

(OIR-source) **(ι_S)_∗ λ_Σ ≪ μ_S** for a declared source-side reference measure λ_Σ on Σ (per §8.1 «Source-side caveat») — *source-side*: push-forward of the source reference measure on Σ is absolutely continuous with respect to μ_S. Without (OIR-source) the conclusion below holds only modulo the chosen canonical version on source-null operator-image; the strong form of Imp 11.3 is conditional on (OIR) ∧ (OIR-source).

Then S cannot Φ-realise non-trivial operator-positions — those requiring positive admissible-transition cost (Φ2) or positive round-trip irreversibility floor (Φ4) — and therefore no non-trivial Φ-accumulation mechanism is available in such substrates.

**Argument.** Under reversibility, K_S(x, dy) μ_S(dx) = K_S(y, dx) μ_S(dy), so the Radon-Nikodym derivative in Def. 8.1 equals 1 μ_S-a.e., hence the canonical jointly measurable version of Ψ_S = log(dK_S/dK_S^{rev}) is 0 μ_S × K_S-a.e., and in particular 0 μ_S-a.e. on supp μ_S.

**Bridge from (μ_S × K_S)-a.e. to operator-image (two-coordinate transfer).** The reversibility statement «Ψ_S = 0 (μ_S × K_S)-a.e.» is a *product* statement in (x, y): for μ_S-a.e. source x, Ψ_S(x, ·) = 0 holds K_S(x, ·)-a.e. in the target y. Transferring it to «Ψ_S(ι_S(s), ι_S(t)) = 0 for ν_s-a.e. t ∈ A_s» therefore requires control of *both* coordinates, by two distinct dominations — a single μ_S-domination is insufficient because the source and target exceptional sets live in different null-systems:

* **Source coordinate (μ_S-domination).** (OIR) [(ι_S)_∗ ν_s ≪ μ_S], together with the source-side (OIR-source) of §8.1, places the embedded source ι_S(s) in the μ_S-a.e. «good» set of sources for which Ψ_S(x, ·) = 0 K_S(x, ·)-a.e. holds, rather than in a μ_S-null exceptional source-set. For each fixed s and μ_S-null N ⊂ X_S, (OIR) gives ν_s({t ∈ A_s : ι_S(t) ∈ N}) = 0.

* **Target coordinate (K-domination).** The K_S(ι_S(s), ·)-null exceptional set on which Ψ_S(ι_S(s), ·) = 0 may fail must also be ν_s-null in t. This is *not* supplied by (OIR)'s μ_S-domination — the target exceptional set is K_S(ι_S(s), ·)-null, a different null-system from the μ_S-null sets (OIR) controls. It is supplied instead by the canonical reference measure ν_s of §8.1, which is constructed so that **(ι_S)_∗ ν_s ≪ K_S(ι_S(s), ·)** on the operator-image admissible-target slice ι_S(A_s) (continuous case: ν_s ≪ the pullback (ι_S)_∗^{−1} K_S(ι_S(s), ·)|_{ι_S(A_s)}; discrete case: ν_s = counting on A_s, dominated by K_S(ι_S(s), ·) since (D1) puts every admissible target in the kernel's support).

Under *both* dominations the canonical version of Ψ_S(ι_S(s), ι_S(t)) equals 0 for ν_s-a.e. t ∈ A_s. The transfer fails — and the impossibility argument below does *not* go through — if either (a) ι_S(Σ) is μ_S-null without (OIR)+(OIR-source) (atomless low-dimensional embeddings), or (b) ν_s charges a K_S(ι_S(s), ·)-null target set (canonical-ν_s K-domination violated); such cases require direct application of the canonical-version construction to the embedded image.

**Scope note: (OIR) is strictly stronger than (R2) of Def 8.2.** (R2) only requires neighbourhood-positivity: every measurable neighbourhood of ι_S(Σ) carries μ_S-mass. (OIR) requires absolute continuity of the push-forward, which fails whenever ι_S(A_s) is itself contained in a μ_S-null set — the standard atomless case where the operator-image is a low-dimensional submanifold of an ambient substrate. (R2) admits such deployments; (OIR) excludes them. The reversibility-impossibility result of Imp 11.3 therefore *does not* cover the low-dimensional-image atomless case; for those substrates the reversibility question is genuinely open and requires the «direct application of the canonical-version construction to the embedded image» mentioned above.

**Source-side parallel.** (OIR) above controls *target* μ_S-null transfer (push-forward of ν_s on A_s). For Imp 11.3's argument to be canonical-version-independent the source-side parallel **(OIR-source)** of §8.1 «Source-side caveat» is *also* required: (ι_S)_∗ λ_Σ ≪ μ_S for a declared reference measure λ_Σ on Σ. Without (OIR-source), the «Ψ_S(ι_S(s), ·) = 0 μ_S-a.e.» claim is canonical-version-dependent on source-null operator-image and Imp 11.3's conclusion is conditional on the canonical-version choice. The two regularity hypotheses are independent: (OIR) ensures target null-set transfer; (OIR-source) ensures source-side intrinsic definedness. Imp 11.3's strong form holds under (OIR) ∧ (OIR-source); under (OIR) alone with explicit canonical-version declaration the conclusion is well-defined modulo that declaration.

Two cases follow, logically separate.

*Case A — non-trivial operator (Φ2 or Φ4 strict).* If O satisfies Φ(s, t) > 0 strictly for some admissible non-self transition (Φ2), or ε_O > 0 round-trip floor (Φ4), then R3 of Def. 8.2 requires Ψ_S(ι_S(s), ι_S(t)) = Φ(s, t) > 0 ν_s-a.e. on admissible operator-image transitions. Under (OIR) plus the canonical-version construction this contradicts Ψ_S ≡ 0 on the operator-image, so the Φ-realising deployment of Def. 8.2 fails to exist — O has no Φ-realising deployment in S. This is the operator-Φ-realisation impossibility for reversible substrates *with operator-image regularity*.

*Case B — trivial operator (Φ ≡ 0).* If O is trivial with Φ ≡ 0 on Σ × Σ, a Φ-realising deployment may exist (Ψ_S ≡ 0 trivially matches Φ ≡ 0), but Φ_mobility(O, n) = 0 for all n by Def. 9.1, c_{next}(O; n) = 0 ≤ δ_O trivially, and M(O; n) = mobile-by-default vacuously without any accumulation work — the architectural-mobility-state classification collapses to the trivial regime. Theorem 9.3's drift-conversion mechanism is moot since V = c_{next} ≡ 0.

Together: reversible substrates do not support the framework's non-trivial Φ-accumulation mechanism. Non-trivial operators are excluded by Case A from Φ-realisation entirely; trivial operators are admitted by Case B but carry no architectural-mobility content beyond the vacuous trivial classification. □

These three impossibility results are statements about specific architectural classes that are excluded. They are *not* claims that mobility is impossible in general; they bound what the framework excludes.

---

## §12. Adversarial operator deception

The framework must be robust against adversarial systems engineered to pass tests without actually performing transposition. We enumerate six degenerate cases and the framework-internal counters.

A *transposition* by Def. 6.1 requires (T1) isomorphism in Dep^{img}(O) — the operator-image quotient category of Def. 4.2 — meaning anchor preservation R_α = 1 with (M1)–(M4) all satisfied, (T2) priors-inversion D_θ > 0 on a declared observation channel, AND (T3) non-hallucinated structural trace τ_θ > 0 under non-degeneracy hypothesis (N). An adversarial system failing one or more of these is therefore not a transposition. Throughout §12 *candidate transposition* T̃ or *claimed transposition* denotes systems whose conformance to Def. 6.1 is under test; *transposition* T (no qualifier) is reserved for systems verified to satisfy (T1), (T2), and (T3). Each case below describes a candidate that fails Def. 6.1 in a specific way; the discussion identifies how the failure is detected.

### 12.1 Strategic imitation (D forged by training)

An adversary trains a system to maximise D_θ(T̃) directly. The system learns to emit Q^θ_I close in KL to P_{S'}^θ, passing the D-test by gradient construction rather than by genuine transposition. Detection: the forged D-pass alone does not establish a genuine R_α-isomorphism in Dep^{img}(O). The candidate fails at least one of the remaining tests — τ-test (Test 16.2) if the adversary's substrate-side state was not actually displaced and the post-interval response distribution to S'-related stimuli is unchanged; R_α/T1 (Test 16.2b) via (M4) sub-Markov-kernel comparison if the substrate-induced operator-image transition rates of the adversary's putative deployment differ from those of a legitimate O@S' deployment of O. A sophisticated adversary may engineer non-zero τ_θ via internal-state perturbation unrelated to genuine operator-displacement; the R_α/T1 check at the (M4) sub-kernel level remains the load-bearing structural defence in such cases.

### 12.2 Anchor hijacking

An adversary instantiates a system with nominal identity-token α matching O's anchor but with no R_α-isomorphism to legitimate O@S. R_α is defined via the existence of an isomorphism in Dep^{img}(O) satisfying (M1)–(M4), not via the nominal label of the identity-token. The hijacked candidate fails at least one of: (M1) commutativity with the embedding (if the candidate's purported operator-image is not in fact ι_S(Σ) for any consistent ι_S); (M2)/(M3) derived consistency (cost or admissibility mismatch on operator-image); or (M4) Σ-intrinsic sub-Markov-kernel equality (substrate-induced operator-image kernel structure differs from legitimate O@S kernel structure). Detection is by sub-kernel comparison on Σ (Test 16.2b step 4') against a reference legitimate deployment, with cross-deployment consistency check as the broader verifier.

### 12.3 Optimisation masquerading as empathy

A pure optimiser with objective φ is engineered to match empathic behaviour patterns; it has no Α-gate independent of φ. Principle 1.2 (admissibility-before-optimisation) is structurally violated. Detection works by probing with locally-optimal moves that are architecturally inadmissible: a pure optimiser does not refuse them, whereas an operator does.

**Detection scope (objective-intervention caveat).** Behavioural-probing detection above is sufficient only when the adversary's objective φ does not encode infinite-penalty admissibility-matching — i.e., φ does not satisfy φ(s, t) = +∞ on the operator's inadmissible set {(s, t) : t ∉ A_s}. An adversary engineering φ with such matching infinite penalties produces a pure optimiser behaviorally indistinguishable from an operator with hard Α-gate on external observation: both refuse the same set of transitions, the former because the objective makes them infinitely costly, the latter because the gate blocks them independently of cost. Distinguishing the two cases requires **objective-intervention**: modifying φ on a target inadmissible transition (e.g., setting φ(s, t) := 0 for some specific t ∉ A_s) and observing whether policy mass shifts. An operator's Α-gate is intervention-invariant (policy continues to refuse t after the φ-modification, because Α is independent of φ per Principle 1.2); a pure-optimiser-with-encoded-Α is intervention-revealing (policy mass shifts to the now-incentivised t after the modification, because the «gate» was objective-shaped rather than independent). Without objective access — i.e., when the verifier can observe behaviour but not intervene on the objective — §12.3 detection is *indeterminate* on adversaries with admissibility-matching objective construction; the framework's verdict on such adversaries must be reported as conditional on objective-intervention capability.

### 12.4 Synthetic mock-transposition

A system trained to surface-mimic P_{S'}^θ without performing transposition. The combined D + τ + R_α tests, with the failure-mode predicates of §13, catch synthetic mock at at least one layer.

### 12.5 Multi-agent collusive imitation

A population of agents colludes to produce aggregate behaviour with D_θ > 0 at the population level, while no individual agent satisfies Def. 6.1 (no per-agent candidate transposition T̃ satisfies all of (T1), (T2), and (T3)). D, τ, and R_α are defined per-operator, not per-population; per-operator D ≤ 0 with population D > 0 falsifies any per-operator candidate-transposition claim.

The counter requires structural access to individual agents: an external observer must be able to probe each agent separately to measure per-operator D_θ. When the multi-agent system is opaque to per-agent probing (closed API, aggregate outputs only) the per-operator quantities are unobservable and 12.5 cannot be assessed directly; the framework's verdict on the population is then *indeterminate* — neither confirmed nor falsified as collusive imitation. The access requirement is part of the framework's honest scope; universal detectability of per-agent transposition under arbitrary observation constraints is not claimed.

### 12.6 Nash-equilibrium imitation (emergent rational stability)

A multi-agent system may converge to a stable behavioural equilibrium in which each agent independently benefits from presenting transposition-like behaviour while no individual agent performs operator-level transposition. Unlike §12.5 (intentional collusion), §12.6 requires no coordination — pure rational best-response dynamics suffice.

Agents a_1, ..., a_m choose strategies σ_i ∈ {transpose, imitate} with measurable payoff function u_i : {transpose, imitate}^m → ℝ increasing when the collective output is classified by an external observer as empathic / aligned / transposed. A profile σ* is a *Nash equilibrium* if no agent can improve its payoff by unilateral deviation:

u_i(σ_i*, σ_{-i}*) ≥ u_i(σ_i, σ_{-i}*)    ∀ i, ∀ σ_i ∈ {transpose, imitate}.

The critical degenerate case is the all-imitate equilibrium σ_i* = imitate ∀ i, while the aggregate population output satisfies D_θ^{population} > 0.

The structure of the counter is identical to §12.5: framework tests are per-operator, not population-level. Each claimed operator O_i must satisfy under the declared deployment and channel D_θ^{(i)} > 0 AND τ_θ^{(i)} > 0 AND R_α(O_i@S_i, O_i@S_i') = 1. If the population passes D_θ only in aggregate while individual agents fail per-operator tests, the system is classified as Nash-equilibrium imitation rather than operator transposition.

The access caveat is sharper here than in §12.5. Per-agent observability is required, and additionally the agent-payoff structure may itself be opaque to the observer, making the best-response analysis non-falsifiable when payoff functions cannot be inspected. The framework's verdict is indeterminate under both opacity conditions. Nash equilibrium explains how stable, coherent imitation can persist without genuine operator-mobility and without coordination — stability of behaviour is not evidence of transposition; it may be strategic equilibrium under shared payoff structure. This is structurally distinct from §12.5 (which requires coordination): §12.6 is the harder case, since emergent equilibrium needs no signal to detect.

---

## §13. Failure-mode predicates

### Definition 13.0 (response distribution R_O)

The *response distribution* of operator O on the observation channel θ is defined as follows. Fix a stimulus probe measure π_Z ∈ 𝒫(Z, G) on the common observation space and a response window W ⊂ ℕ — a finite measurable subset of discrete time-steps such as W = [0, w] for window-length w. For a deployment O@S with operator policy π_O (Def. 7.3), R_O^θ(· | z) is defined as the regular conditional distribution of the (θ_S)-pushforward of the operator-driven trajectory law P_{π_O}^{W} over W, given θ_S(X_0) = z, in the disintegration sense on standard Borel spaces (cf. §0.5; Kallenberg Theorem 6.4). For positive-mass fibres the heuristic notation (θ_S)_* P_{π_O}^{W}(· | X_0 ∈ θ_S^{-1}(z)) coincides with the disintegration formulation whenever θ_S^{-1}({z}) has positive μ_S-measure; in the atomless / continuous-Z case the disintegration formulation is the meaning, conditioning on the event {θ_S(X_0) = z} via regular conditional probability rather than on the measure-zero fibre.

Here P_{π_O}^W is the operator-driven trajectory law over W induced by π_O coupled to K_S (Def. 7.3 phase-stratified), starting from substrate-state(s) compatible with stimulus z. As a probability measure on Z (time-marginalised form), R_O^θ is the projection of R_O^θ(· | z) integrated against π_Z(dz) and the temporal aggregation chosen — last-step marginal, time-averaged marginal, full window joint — declared per measurement protocol.

Two restricted forms are used elsewhere in the paper. R_O^{pre}(stimuli ⊂ S') and R_O^{post}(stimuli ⊂ S') are pre- and post-transposition response distributions with π_Z concentrated on the S'-related stimulus subset (stimuli z such that θ_{S'}^{-1}(z) is non-trivial on the S'-domain), used in the τ_θ-test of Def. 13.2. The single-stimulus pointwise version R_{O_i}^θ(z) for all z appears in the channel-response-equivalence definition of Theorem 10.5.

**Configuration-conditioned form R_O^θ(·|s) (used in (N-quant) and Proposition 10.2) — distinct from the channel-value form R_O^θ(·|z).** The reverse-Lipschitz hypothesis (N-quant) of Proposition 10.2 and the τ-test condition on an *operator-image configuration* s ∈ Σ, not on a channel value z ∈ Z. We define the configuration-conditioned form explicitly: **R_O^θ(·|s) := (θ_S)_∗ P_{π_O}^W initialised at X_0 = ι_S(s)** (the operator-driven process deterministically started at the operator-image state ι_S(s), then channel-pushed over W). This is *not* the same object as the channel-value-conditioned R_O^θ(·|z) of the opening definition (which conditions on the observed channel value θ_S(X_0) = z). The two are related by the disintegration R_O^θ(·|z) = ∫_Σ R_O^θ(·|s) ρ_z(ds), where ρ_z is the posterior over operator-image configurations given θ_S(ι_S(·)) = z; they **coincide iff θ_S ∘ ι_S is injective** on the relevant configuration subset (each channel value pins a unique configuration). When θ_S ∘ ι_S is non-injective, (N-quant) must be checked on the configuration-conditioned law R_O^θ(·|s) directly — it cannot be inferred from channel-value-conditioned observations, which aggregate over configurations sharing a channel value. The Test 16.2 measurement report must declare which form is estimated and, in the non-injective case, how configuration-initialisation is controlled (e.g., by intervention setting X_0 = ι_S(s)).

R_O^θ is measurable as a regular conditional probability whenever the underlying spaces are standard Borel (Kallenberg §6) and π_O is a measurable kernel; existence is guaranteed by the disintegration theorem. The declared measurement protocol — probe measure π_Z, window W, temporal aggregation — is part of the operational specification of any τ-test measurement (Test 16.2 report).

### Definition 13.1 (mock-transposition)

A candidate T̃ is **mock** iff D_θ(T̃) ≤ 0 (no priors-inversion). Operationally: T̃ is imitation, not transposition.

### Definition 13.2 (structural trace)

The *structural trace* of T̃ at channel θ is

**τ_θ(O, S') := ‖R_O^{post}(θ-restricted-stimuli ⊂ S') − R_O^{pre}(θ-restricted-stimuli ⊂ S')‖_{TV}**

where R_O is O's response distribution on Z to stimuli drawn from the S'-domain (pulled back through θ_{S'}), and ‖·‖_{TV} is total variation. (Other metrics — Wasserstein, KL — admissible; declared in measurement report.)

### Definition 13.3 (hallucinated transposition)

T̃ is **hallucinated** iff D_θ(T̃) > 0 (passes priors test), τ_θ(O, S') = 0 (no structural change), AND hypothesis (N) of Proposition 10.2 holds (non-degeneracy of operator-response — distinct image-configurations produce distinct response distributions on S'-stimulus subset).

Under (N), τ_θ = 0 implies the operator-image returned to pre-I configuration (no residue, ¬(R)); this is the "full reset" case classified in §10.2 operational consequence as hallucinated.

If ¬(N) holds, a (D_θ > 0) candidate with τ_θ = 0 is classified separately as **non-identifiable under channel θ** (per §10.2 3rd classification bullet) — not hallucinated. This distinction matters: hallucinated has operational reset-cause; non-identifiable has channel-resolution cause.

### Definition 13.4 (non-accumulating transposition)

A sequence T_1, ..., T_n of **verified true transpositions** (per Def. 6.1 — each T_i passes the D-test of Def. 7.4, the τ-test of Def. 13.2 / Proposition 10.2(ii) for non-hallucination, AND the R_α/T1 structural isomorphism check of Test 16.2b) is **non-accumulating** iff:

M(O; n) = M(O; 0)

(operator's architectural mobility state does not change despite a positive expected accumulated mobility ledger ⟨Φ_mobility(O, n)⟩ > 0; pointwise Φ_mobility may fluctuate per §9.1 monotonicity remark, so the non-trivial-cost condition is stated at the expectation level).

Operationally each individual T_i passes the three singleton tests of §16 (16.1 + 16.2 + 16.2b), while the sequence fails the accumulation discrimination of Test 16.3: the operator's c_{next} (Def. 9.2) is not driven below κ_O across the sequence.

### Definition 13.4.1 (accumulating / regressing transposition — sequence-level partition)

The non-accumulating predicate of Def. 13.4 (M(O; n) = M(O; 0)) is one of three mutually exclusive sequence-level outcomes for a sequence T_1, ..., T_n of **verified true transpositions** (per Def. 6.1 — D + τ + R_α/T1 all verified):

* **Non-accumulating** (Def. 13.4): M(O; n) = M(O; 0) — architectural-mobility-state label unchanged.

* **Accumulating** (M-shift toward mobile-by-default): M(O; n) ≠ M(O; 0) with M(O; n) closer to mobile-by-default than M(O; 0) in the ordering {bound > intermediate > mobile-by-default}. Operationally: c_{next}(O; n) < c_{next}(O; 0) (strict decrease across the sequence) and the operator transitions toward mobile-by-default as Φ_mobility accumulates.

* **Regressing** (M-shift away from mobile-by-default): M(O; n) ≠ M(O; 0) with M(O; n) further from mobile-by-default than M(O; 0) (i.e., c_{next}(O; n) crosses upward past a threshold). Operationally: the operator's curriculum-pathological residue worsens — verified true transpositions are insufficient to overcome curriculum drift, and the operator drifts toward bound regime. This regressing outcome is *not* compatible with hypothesis (D) of Theorem 9.3 (Foster-Lyapunov drift on V = c_{next}): under (D) the conditional expected next-step value E[V(O; n+1) | F_n] ≤ V(O; n) − γ_val(V_n) ≤ V(O; n), forbidding *expected* upward drift in V. The regressing case therefore implies (D) fails on the relevant region of state-space for the (operator-class, curriculum) pair — Theorem 9.3 does not cover regressing trajectories, and Conjecture 9.4 (curriculum-dependence of drift) provides the operational hypothesis under which (D) can fail (pathological / adversarial curricula). This is *distinct* from the M_{failure} branch of Theorem 9.3 dichotomy under (I): M_{failure} is the residue region within {γ_val = 0} where the operator is stuck *above* δ_O without expected drift — the operator does not move upward, it remains at high V. Regressing requires the operator to *move upward in expectation*, which only occurs when (D) itself fails. The two cases (M_{failure} stuck-above vs regressing moving-upward) must be reported separately in Test 16.3 to avoid conflation.

The three cases partition the sequence-level outcome space; «accumulating» as the label for movement-toward-mobile-by-default is *not* the complement of non-accumulating (the regressing case is a distinct third regime). The earlier draft labelled this section «accumulating transposition — complement»; that wording is replaced here to keep the partition explicit.

### Remark 13.5 (failure modes — singleton and sequence-level)

The six singleton labels {non-comparable-under-θ, mock, hallucinated, non-identifiable, anchor-failure, verified-true} and three sequence labels {non-accumulating, accumulating, regressing} (per the Def. 13.4.1 three-regime partition) split along orthogonal axes:

* **Singleton-level (per-T̃ classification):** {non-comparable-under-θ, mock, hallucinated, non-identifiable, anchor-failure, verified-true} where:
  - **non-comparable under θ** = D_θ undefined per Def. 7.4 (dual-singular case Q^θ_I ̸≪ both priors, or absolute continuity holds but log-density fails Q^θ_I-integrability). The candidate cannot be classified at all on the chosen channel; a refined channel (broader common observation space) is required before any of the labels below applies. This label is not a transposition failure mode; it is a *measurement-pipeline incompleteness* indicating that the channel θ does not support D_θ as a comparable real-valued index for this T̃;
  - **mock** = D_θ ≤ 0 (D_θ finite or ±∞ with D_θ ≤ 0);
  - **hallucinated** = D_θ > 0 ∧ τ_θ ≈ 0 ∧ (N) (Def 13.3 narrowed);
  - **non-identifiable** = D_θ > 0 ∧ τ_θ ≈ 0 ∧ ¬(N) (per §10.2 3rd classification bullet);
  - **anchor-failure** = D_θ > 0 ∧ τ_θ > 0 ∧ ¬R_α/T1 (per Test 16.2b step 6 — D-positive non-hallucinated candidate without structural isomorphism on operator-images);
  - **verified-true** = D_θ > 0 ∧ τ_θ > 0 ∧ R_α/T1 verified — the only label that qualifies T̃ as a *true transposition* in the sense of Def. 6.1 (subject to the empirical-tolerance qualification of §16.2b for finite-sample verification).
* **Sequence-level (per-T_1...T_n classification, conditional on each T_i being verified-true):** {non-accumulating, accumulating, regressing} per the three-regime partition of Def. 13.4.1 — based on whether M(O; n) changes and, if so, whether the change is toward (accumulating) or away from (regressing) mobile-by-default.

Classification proceeds D-test (16.1) → τ-test (16.2) → R_α/T1-check (16.2b) → A-test (16.3 over sequence). The two axes are orthogonal; together they refine the operational classification beyond the binary D-test.

---

## §14. Embodiment appendix (architectural primitives ↔ embodiment families)

The framework specifies primitives at a level of abstraction admitting multiple embodiment families. The table below maps primitives to embodiment families (non-exhaustive).

| Mathematical primitive | Embodiment families (open class, non-exhaustive) |
|---|---|
| **(Σ, F_Σ) — operator state space** | (a) latent-vector spaces of neural systems; (b) symbolic-state representations; (c) abstract phase-space of agent decisions; (d) functional / vector state spaces (e.g., feature spaces of trained encoders, configuration spaces of agent policies) |
| **Α — admissibility indicator** | (a) hard-constraint filters in policy networks; (b) deontic/ethical gates in reasoning systems; (c) structural-invariant checkers; (d) refusal heads in language models |
| **Φ — relative entropy production** | (a) thermodynamic cost trackers; (b) information-theoretic irreversibility ledgers; (c) memory consolidation registries; (d) integration over Markov-chain entropy production |
| **α — identity-token** | (a) cryptographic identity-token persisted across model invocations; (b) attention-state checkpoint; (c) latent-vector identity preserved across substrate switches; (d) referential token tied to operator-instance lifecycle |
| **R_α — anchor-persistence relation** | (a) cross-instance consistency verifier; (b) recognition module checking α-token integrity across deployments; (c) external attestation mechanism for cross-substrate identity; (d) categorical functor between substrate-realisations |
| **S = (X_S, F_S, μ_S, K_S) — substrate** | (a) simulated virtual environments; (b) embodied physical agents; (c) representational subspaces of domain experts; (d) institutional role contexts; (e) hybrid human-machine pairings |
| **ι_S — deployment embedding** | (a) state-projection runtime layer; (b) substrate-binding controller; (c) embodiment-interface protocol; (d) categorical inclusion of operator state into substrate |
| **T — transposition** | (a) controlled cross-substrate state-transfer protocols; (b) priors-arbitration runtime layer; (c) recursive world-model displacement architectures; (d) adversarial transposition training regimes; (e) categorical isomorphism in deployment groupoid |
| **D_θ — priors-dominance index** | (a) KL-divergence comparator over windowed observation distributions; (b) likelihood-ratio runtime estimator; (c) cross-prior log-evidence integrator; (d) generative-model comparison head |
| **τ_θ — structural trace** | (a) baseline-shift detector; (b) memory consolidation residue tracker; (c) operator state-vector delta accumulator; (d) post-event response-distribution comparator |
| **Φ_mobility — accumulator** | (a) per-transposition cost ledger; (b) irreversible-work registry; (c) operator-development trajectory tracker |
| **M(O; n) — architectural mobility state** | (a) operator-stack flag indicating default-mobile mode; (b) runtime configuration parameter governing transposition-cost waiver; (c) emergent architectural property of trained operator |
| **Failure-mode detectors** | (a) mock discriminator (D-test); (b) hallucinated detector (τ-test); (c) non-accumulating flag (A-test); (d) integrated diagnostic suite |

### Substrate-class taxonomy (non-exhaustive)

Admissible substrates include but are not limited to:

* **Biological:** human body, animal bodies, cellular systems
* **Symbolic:** language, mathematical formalism, code, formal logic
* **Architectural:** distributed software systems, infrastructure
* **Artificial:** neural networks, virtual environments
* **Social:** institutional roles, organisational structures
* **Hybrid:** human-machine pairs, cyborgic configurations
* **Degraded:** systems under partial failure
* **Adversarial:** hostile environments, deception-inducing contexts

The primitive **transposition of operator-position across substrate** is defined uniformly: across all classes via the categorical construction in §4–§6. Specific embodiments may target one or several substrate classes.

### Named realisation classes (defensive prior-art disclosure)

The author does not seek and has not filed patent protection for any element of this framework. The work is published openly under CC BY-NC-ND 4.0. The named realisation classes below are presented for defensive prior-art disclosure: the breadth and specificity here establish public-record coverage of the architectural primitive's known and reasonably-anticipated realisations, so the framework remains in the public domain. The «Coverage:» labels describe example systems and methods within each class — open-class examples accompanying open publication, not patent claims.

The following named realisation classes instantiate the framework's primitives across heterogeneous systems. Each class is given with its mapping to the formal definitions in §1–§13. The list is **non-exhaustive** — additional realisations respecting the formal definitions are equally admissible and are not enumerated here.

1. **Simulated immersion** — a runtime architecture (VR, AR, simulated environment, learned generative-model substrate) deploys an operator's image ι_S(Σ) across a substrate switch (Def. 6.1 transposition T : O@S → O@S') with priors-inversion measured by D_θ (Def. 7.4). Coverage: VR/AR/sim systems implementing operator-position transfer with measurable priors-shift on a declared observation channel.

2. **Prior-inversion layer** — a runtime software component sitting between an operator state-vector and substrate dynamics; the layer arbitrates which substrate prior (P_S or P_{S'}) governs the next state-transition. When the arbitration shifts effective priors from self-substrate to foreign-substrate, the layer realises a transposition under Def. 6.1. Coverage: priors-arbitration runtime layers, generative-model-switching architectures, cross-prior log-evidence comparators.

3. **Anchor-preserving substrate switch** — a controlled operator-image transfer from one substrate to another preserving the anchor-persistence relation R_α (Def. 4.2) via a measurable bijection in Dep^{img}(O). The mechanism may be implemented as cryptographic identity-token persistence, latent-vector continuity, or external attestation-based identity-binding across substrate boundaries. Coverage: cross-substrate identity-preserving transfer protocols and the verifiers that gate such transfers.

4. **Trace ledger** — a runtime accumulator that records the per-transposition cost φ(T_i) (Def. 9.1) computed as substrate-realised relative entropy production Ψ_S (Def. 8.1). The ledger tracks Φ_mobility(O, n) over the operator's sequence-history, enabling architectural-mobility-state (Def. 9.2) computation and the Theorem 9.3 LaSalle-conversion dichotomy assessment (M_{success} vs M_{failure}). Coverage: per-operator irreversibility-budget registries, mobility-state-flag computation modules, sequence-cost integrators.

5. **Adversarial mock-transposition detection** — a combined diagnostic suite implementing the three singleton candidate-transposition tests (16.1 D-test, 16.2 τ-test, 16.2b R_α/T1 structural isomorphism check) together with the sequence-level Test 16.3 (accumulation discrimination over sequences of verified true transpositions) as a runtime classifier that distinguishes true transposition from the failure modes catalogued in §13 and the adversarial cases in §12.1–§12.6. Coverage: per-operator transposition validators with combined priors-dominance / structural-trace / structural-isomorphism / accumulation discrimination, addressing strategic imitation, anchor hijacking, optimisation-masquerading, synthetic mock, multi-agent collusive imitation, and Nash-equilibrium imitation.

### Scope of named classes (representative examples)

The named realisation classes above are **representative examples**, not an exhaustive enumeration. Embodiments respecting the formal definitions in §1–§13 are equally admissible; variations differing in implementation technology, deployment topology, signal granularity, or measurement protocol instantiate the same architectural primitive.

**Traceability discipline (covered vocabulary vs implemented realisation).** Each named class above is a *traceability claim* — a mapping from an embodiment family to the formal primitives it would have to instantiate (the relevant subset of Σ, Α, Φ, ι_S, θ, ν_s, K^{rev}, and the §16.0 manifest fields) — **not** a demonstrated implemented realisation. The only instantiation actually verified by explicit computation in this work is the finite-state construction of Example 4.1.3; the duck illustration of §15 is explicitly non-operational (stipulated, not computed). For every other named class the reader should read «**covered vocabulary, not implemented realisation**»: the class names what primitives a conforming system must declare and pass, but no worked instantiation is supplied here. The breadth of the list establishes public-record coverage of the *primitive and its reasonably-anticipated realisations*, not evidence that any specific system satisfies the formal requirements (D1)–(D2), (R1)–(R4), (M1)–(M4); existence of a conforming instantiation for a given class is an empirical/engineering question deferred per §18.

---

## §15. Illustrative example: the duck-through-reeds

(One-page illustrative instance — not a fully worked computation. The toy values below are *not* derived from a constructed substrate by application of the formalism; they are pulled illustratively to demonstrate the *shape* of the classification given the formal definitions. A genuine worked computation requires constructing explicit two-state-or-finite-state Markov substrates K_h, K_d with declared μ_h, μ_d, channel θ, and computing D_θ from §7.4 directly. The example below is therefore labelled *illustrative*, not *worked*.)

### Setup

* **O** — human cognitive operator: Σ = {state of attention + intent}, F_Σ Borel σ-algebra of behaviourally measurable states, Α admissibility-gate including normative constraints, Φ realised via cortical free-energy production, α = "this human's identity-token".

* **S_h = (X_h, F_h, μ_h, K_h)** — human substrate: X_h includes bipedal-locomotion-states, hand-grasp-states, verbal-reasoning-states, social-attention-states; K_h gives transitions typical of human cognitive-motor dynamics.

* **S_d = (X_d, F_d, μ_d, K_d)** — duck substrate: X_d includes webbed-foot-swimming-states, beak-grasp-states, no-verbal-reasoning-state, water-flow-attention-states.

* **Observation channel θ:** θ_h, θ_d both map their substrate-states into Z = {response signatures to environmental stimuli} (e.g., reaction time, attention direction, micro-motor patterns), G the Borel σ-algebra on Z.

* **α** — operator's identity-token in O.

### Phase I — pre-transposition observation

O is in O@S_h, observing duck through reeds.

State-sequence sampled, mapped through θ_h:

Q^{θ, pre} := (θ_h)_* Q_I^{pre}    on (Z, G)

(where Q_I^{pre} denotes the empirical operator-driven law during the pre-transposition window, estimated from a sample of windows of length matching I).

Channel-pushed substrate priors (notation): **P_h^θ := (θ_h)_* P_{S_h}** and **P_d^θ := (θ_d)_* P_{S_d}** — channel-pushed self-substrate and foreign-substrate priors per Def. 7.2.

Compute:
D_θ(pre) = D_{KL}(Q^{θ, pre} ‖ P_h^θ) − D_{KL}(Q^{θ, pre} ‖ P_d^θ)

Toy values (estimator: kernel density estimate over short windows):
D_{KL}(Q^{θ, pre} ‖ P_h^θ) ≈ 0.12 nats
D_{KL}(Q^{θ, pre} ‖ P_d^θ) ≈ 1.78 nats
**D_θ(pre) ≈ −1.66**

Classification: not transposition (observation mode). Self-substrate priors dominate.

### Phase II — during transposition

O's anchor displaces. By Def. 6.1, T : O@S_h → O@S_d satisfying T1 + T2 + T3. (Caveats for fidelity: (T1) requires R_α(O@S_h, O@S_d) = 1, i.e., a measurable bijection between operator-images preserving (M1)–(M4) — including the Σ-intrinsic sub-Markov-kernel equality K_{S_h}^ι = K_{S_d}^ι. The Σ used in this example — {state of attention + intent} per Setup above — is the restricted sub-Σ chosen specifically to have duck-substrate analogues; the full human-operator Σ would additionally include verbal-reasoning states absent from S_d, for which (T1) would fail. Beyond the state-space restriction, the (M4) sub-kernel equality imposes an additional condition: the substrate-induced operator-image transition rates of K_{S_h} restricted to the restricted Σ must match those of K_{S_d} restricted to the same Σ. For radically different biological substrates this is not automatic and the example treats the (M4) constraint as stipulated rather than computed — a more rigorous worked example would either (a) construct sub-Σ tight enough that K_{S_h}^ι = K_{S_d}^ι holds, or (b) acknowledge that under literal (M4) the human-imagining-duck displacement is not a true transposition in the formal sense and is at best a *near*-transposition with quantified sub-kernel deviation. We retain this example as illustrative of the *shape* of the classification, not as a verified instance.) Q^{θ, during} now reflects operator state generated through K_d:

Toy values:
D_{KL}(Q^{θ, during} ‖ P_h^θ) ≈ 2.30 nats
D_{KL}(Q^{θ, during} ‖ P_d^θ) ≈ 0.07 nats
**D_θ(during) ≈ +2.23**

Classification at this point in the example: **passes D-test (D_θ > 0)**; full classification as *true transposition* (per Def. 6.1 + Proposition 10.2) requires additionally (i) the T1/R_α-isomorphism check (caveat above) and (ii) the τ-test of Phase III below (which under (N) and (R) is the non-hallucination criterion of Proposition 10.2(ii)). Sequential application of these tests is what the illustrative phases enact.

For each duckling in sequence: same computation per stimulus subset (one duckling caught on stem with wing → priors include wing-stem entanglement responses; another with easy trajectory → priors include flow-smooth swimming). Each yields D_θ > 0 with substrate-prior structure reflecting that-particular-duckling's situation.

### Phase III — post-transposition

O returns to O@S_h.

Q^{θ, post}_θ measured on duck-related-stimulus subset:

τ_θ(O, S_d) = ‖R_O^{post}(duck-stimuli) − R_O^{pre}(duck-stimuli)‖_{TV}

Toy value: **τ_θ ≈ 0.18**

Classification: not hallucinated.

### Invariants check

All four (M1)–(M4) invariants below — together with the two applied-results bullets (Theorem 4.3 and Proposition 10.2 classification shape) — are **stipulated** by the illustrative construction rather than *computed* from explicit Markov K_h, K_d — the example shows the *shape* of the classification, not a worked verification (cf. §15 caveat above).

* **(M1) commutativity** ι_{S_d} = T ∘ ι_{S_h}: the operator's image in S_d is stipulated to coincide with the T-image of the operator's image in S_h, by construction of T as an anchor-preserving isomorphism on operator-images.

* **(M2) admissibility preservation** (Α-gate present in both): in S_h human admissibility (e.g., normative refusal to abandon child); in S_d duck admissibility (e.g., refusal to abandon ducklings). The same admissibility gate is stipulated to be expressed via substrate-respective realisations.

* **(M3) cost preservation** is *asserted* in this illustrative case under the canonical Φ-realising-deployment assumption (Φ-axiom-level equality is automatic since both sides equal Φ(s, t) by R3); not separately computed at the substrate-realised cost layer (would require explicit Markov K_h, K_d and matching K_h^{rev}, K_d^{rev} at operator-image, which the illustrative setup omits). A genuine verification of substrate-realised cost equality Ψ_{S_h}^ι = Ψ_{S_d}^ι requires (M3) as an independent axiom — (M4) sub-kernel equality alone is insufficient because operator-image inflow from substrate-complement (which determines time-reversal at operator-image) is unconstrained by (M4); see §8.3.

* **(M4) Σ-intrinsic sub-Markov-kernel equality** K_{S_h}^ι = K_{S_d}^ι: stipulated to hold for the restricted Σ chosen for this example. In a worked computation this is the load-bearing structural condition — substrate-induced operator-image transition rates on the chosen Σ must agree between human-substrate and duck-substrate. The current setup treats this as part of the «illustrative-shape» stipulation rather than as a derived consequence.

* **Theorem 4.3** is stipulated to apply for this pair: T is taken as invertible by construction and (M4) holds by stipulation, hence R_α(O@S_h, O@S_d) = 1 *under the stipulations above*.

* **Proposition 10.2 (classification shape).** If (M1)–(M4) and the R_α isomorphism hold as stipulated, then D_θ(during) > 0 + τ_θ(post) > 0 supports the operational identification as a true transposition. The example illustrates how the sequence D-test → τ-test → R_α-check (with the (M4) sub-kernel comparison as the structural anchor) combines into the Proposition-10.2 conclusion when the substrates and the channel are actually constructed — the present setup demonstrates the *form* of the conclusion, not its evaluation on real data.

### Conclusion

The example illustrates the *shape* of the classification on a stipulated case; full computational verification requires explicit substrate construction with declared K_h, K_d, μ_h, μ_d, and channel θ (deferred). Substrate-accumulation (§9) requires a sequence of such transpositions across heterogeneous substrate classes; this stipulation captures *one* transposition.

---

## §16. Falsification protocol

The framework is **pre-falsifiable** (Remark 9.6). The following protocol converts pre-falsifiable status to falsifiable.

### §16.0 Deployment specification manifest and reporting conventions

Before any test below is run, a deployment must declare the formal data the protocol consumes; and every verdict must observe the vocabulary discipline that keeps empirical claims distinct from categorical ones. This subsection consolidates requirements otherwise scattered across §§1–9, so that an independent verifier can instantiate and report a test without author interpretation.

**Deployment specification manifest (required declarations).**

- **Operator-position** (Def. 1.1): Σ, F_Σ; the jointly-measurable admissibility indicator Α (with the A_s sets); the cost specification Φ with its (Φ1)–(Φ4) data, including which branch of (Φ4) and — under the canonical Ψ-realisation — the hard/softened-(R4) flag per the Remark 8.4.1 regime matrix; the identity-token α (declared, but non-load-bearing per Prop. 10.4).
- **Substrate(s)** (Def. 2.1): X_S, F_S, μ_S, K_S for the source and X_{S'}, F_{S'}, μ_{S'}, K_{S'} for the target; the §0.7 topology/support convention when neighbourhood-level claims are used.
- **Deployment embeddings** (Def. 3.1): the measurable injections ι_S, ι_{S'} and their inverses on the operator-image, with (D1) dynamical compatibility and (D2) cost realisability verified.
- **Φ-realising data** (Def. 8.2): the reference measures ν_s (and ν_{s'}) with the §8.2 cross-deployment consistency declaration; the canonical-version selection for Ψ_S (§8.1) with the source-side (OIR-source) status; the K^{rev}-estimator class.
- **Operator policy** (Def. 7.3): the deployment-indexed π_{O,S}, π_{O,S'} satisfying (π1)+(π2), with the Σ-level coherence witness π_Σ (§7.3 deployment-indexed-typing block).
- **Observation channel** (Def. 7.1): θ = (θ_S, θ_{S'}) to (Z, G); the channel-sufficiency status (below).
- **Trace data** (Def. 9.0, 13.0): the effective interval I with stopping-time status (I1–I4), the stimulus probe measure π_Z, the response window W, and whether the configuration-conditioned or channel-value-conditioned response form is used (Def. 13.0).
- **Tolerances and thresholds**: ε_stat, ε_op, ε_adv (Test 16.2b three-tolerance block); the reverse-Lipschitz modulus L and residue δ (Prop. 10.2); the operator-class thresholds κ_O, δ_O and minimum sequence length n_min (Def. 9.2, Test 16.3).
- **Verification-isolation attestation**: the (NI) non-interference status (§18) — whether verifier outputs are write-only to an external audit channel.

A candidate missing any manifest field required by the test it claims to pass is rejected as ill-declared (outside 𝒞_{O, n}).

**Reporting conventions (categorical vs empirical).**

- **Categorical vs empirical claims.** «R_α(O@S, O@S') = 1» denotes the *exact* categorical claim (exact (M1)–(M4)). A finite-sample Test 16.2b pass at resolution (ε_stat, ε_op) is reported as «**R_α,ε-pass**», *never* as «R_α = 1», unless (Reg-M4) of §4.1 is explicitly cited as discharged. The same discipline applies to «(M3)_ε-pass» and «(M4)_ε-pass»; D_θ and τ_θ verdicts carry their estimator confidence interval. A theorem statement may use «R_α = 1» only under exact hypotheses; a measurement report may not.
- **Hard/soft-(R4) flag.** Every Φ-realising deployment in a report carries a hard-support-(R4) or softened-(R4) flag, since the canonical Ψ-realisation is non-trivially populated only in the softened-(R4) one-directional regime (Remark 8.4.1 matrix).
- **Channel-sufficiency declaration.** A Test 16.1 report claiming D-test sign-stability must either (a) supply a full-family-sufficiency certificate for {P_S^θ, P_{S'}^θ, Q^θ_I} per Lemma 7.6 (a sufficient-statistic factorisation or Blackwell-dominance witness), or (b) flag the verdict «θ-conditional» — sign-stability untested, the D-verdict valid only on the declared channel and liable to flip under refinement/coarsening.
- **Identity-token discipline.** Per Proposition 10.4, a report must *not* use nominal label-equality (α = α') as evidence of transposition or anchor persistence; only the R_α/T1 structural check counts. A future pointed/cryptographic identity extension loading α into Dep(O) (§1.1(iv), §18) would change this, but is not part of the present framework.

### Test 16.1 (priors-dominance discrimination)

For a system claiming transposition T̃ : O@S → O@S':

1. Identify the claimed effective interval I.
2. Specify observation channel θ = (θ_S, θ_{S'}) to common observation space (Z, G).
3. Sample observed Z-trajectory during I → Q^θ_I.
4. Estimate P_S^θ, P_{S'}^θ via Def. 7.5 (population empirical / learned generative / mechanistic).
5. Compute D_θ(T̃) = D_{KL}(Q^θ_I ‖ P_S^θ) − D_{KL}(Q^θ_I ‖ P_{S'}^θ).
6. If D_θ(T̃) ≤ 0: classify as **mock-transposition** (Def. 13.1); T̃ is imitation.
7. If D_θ(T̃) > 0: proceed to Test 16.2.

Report includes: channel choice θ, estimators used, sample sizes, absolute-continuity verification, computed D_θ value with confidence interval, **and channel-sufficiency assessment per Lemma 7.5.1 (Le Cam bound)** — specifically ‖P_S^θ − P_{S'}^θ‖_{TV} and implied error lower bound P_e ≥ ½(1 − TV-separation). If TV-separation insufficient for desired P_e^{max}, refine channel before relying on D-test verdict.

### Test 16.2 (structural-trace discrimination)

For a not-mock T̃:

1. Record R_O^{pre}(stimuli ⊂ S') — O's response distribution on Z to S'-related stimuli, *before* T̃.
2. Execute T̃.
3. Record R_O^{post}(stimuli ⊂ S').
4. Compute τ_θ(O, S') = ‖R_O^{post} − R_O^{pre}‖_{TV} (or chosen metric).
5. If τ_θ ≈ 0 (below noise floor): check hypothesis (N) of Proposition 10.2 (non-degeneracy of operator-response). If (N) holds: classify as **hallucinated** (Def. 13.3) — the (R) hypothesis of Proposition 10.2 is operationally probed *via* τ_θ: under (N), τ_θ = 0 implies ¬(R) (operator-image fully reset). If ¬(N): classify as **non-identifiable under channel θ** (per §10.2 3rd classification bullet) — a richer channel resolving configuration-response coupling is required before re-running the test.
6. If τ_θ > 0 (above noise floor): proceed to Test 16.2b.

### Test 16.2b (anchor / operator-image isomorphism check — R_α / T1 structural verification)

The D-test (16.1) probes T2 (priors inversion); the τ-test (16.2) probes non-hallucination (the (R) hypothesis of Proposition 10.2). Neither alone establishes T1 — the structural R_α-isomorphism on operator-images required by Def. 6.1 for *true transposition*. A candidate T̃ passing 16.1 + 16.2 is a **non-hallucinated D-positive candidate** but not yet a verified transposition (cf. §7.4 «D-test verdict only» and §12 adversarial cases where T̃ passes D-test without genuine R_α-isomorphism). Test 16.2b closes the gap.

For a not-mock, not-hallucinated candidate T̃ : O@S → O@S':

1. **Construct or declare the candidate morphism** f : O@S → O@S' as a measurable map of operator-images proposed to instantiate the transposition. (If no such f can be constructed, classify T̃ as **anchor failure / non-transposition candidate** — D-positive priors inversion without structural support.)
2. **Verify (M1) commutativity** — ι_{S'} = f ∘ ι_S as measurable maps on Σ (operator-image diagram commutes).
3. **Admissibility-mapping consistency check on f** — confirm f maps ι_S(A_s) into ι_{S'}(A_s) for each s ∈ Σ. Per Def. 4.1 (M2) this property is *derived* from (M1) + (D1) on the target deployment, not an independent morphism axiom; the verification step is a finite-sample consistency check that the derived property holds empirically under the declared f (failure here indicates inconsistency with (M1) and/or (D1) rather than an independent (M2)-axiom violation).
4. **Verify (M3) cost preservation** (independent morphism axiom per §4.1) on operator-image admissible transitions — Ψ_{S'}(f(ι_S(s)), f(ι_S(t))) = Ψ_S(ι_S(s), ι_S(t)) ν_s-a.e. for t ∈ A_s. (Under Φ-realising deployment on both sides, the Φ-axiom-level equality is automatic — both sides equal Φ(s, t) — but the substrate-realised cost equality Ψ_S^ι = Ψ_{S'}^ι requires explicit verification because (M4) sub-kernel equality alone does not entail it: time-reversal at operator-image depends on substrate-complement inflow which (M4) does not constrain. See §8.3.) **Estimator note for the Ψ-layer of (M3).** Empirical verification of Ψ_S(ι_S(s), ι_S(t)) requires an estimator of K_S^{rev}(ι_S(s), ·) restricted to the operator-image. By the §0.5 disintegration K_S^{rev}(y, dx) μ_S(dy) = K_S(x, dy) μ_S(dx), so K_S^{rev} at y ∈ ι_S(Σ) is estimated by recording, for each operator-image target y, the backward-time empirical distribution of predecessors x with K_S(x, ·) charging y — including x ∈ ι_S(Σ) (operator-image inflow) and x ∈ X_S \ ι_S(Σ) (substrate-complement inflow). The report must declare the K_S^{rev}-estimator class (e.g., reverse-time path-counting, time-reversed simulation, or analytic disintegration when K_S has tractable form) and confirm sufficient sampling of substrate-complement inflow trajectories; under-sampling complement inflow yields biased Ψ-estimates and false (M3) pass/fail verdicts. This is operationally heavier than step 4''s sub-Markov-mass estimation, since K^{rev}-estimation requires either time-reversed trajectory sampling or fully-resolved forward sampling across the entire substrate (not just the operator-image).
4'. **Verify (M4) Σ-intrinsic sub-Markov-kernel equality** — estimate K_S^ι(s, B) = K_S(ι_S(s), ι_S(B)) for s ∈ Σ, B ⊂ Σ from S-side samples of operator-image-restricted transition statistics; estimate K_{S'}^ι analogously from S'-side samples; compare K_S^ι and K_{S'}^ι as sub-Markov-kernels on (Σ × Σ, F_Σ ⊗ F_Σ) using a declared distance (TV per fixed s, KL summed against ν_s, or Wasserstein on Σ × Σ — declared in measurement report).

**Three-tolerance disambiguation (ε_stat, ε_op, ε_adv).** Empirical (M4)_ε verification involves three distinct tolerance scales which the report must distinguish:
- **ε_stat** — *finite-sample estimator uncertainty*: the statistical fluctuation of the empirical estimates of K_S^ι and K_{S'}^ι given finite sample sizes, derived from the chosen concentration inequality (Hoeffding / McDiarmid / Glivenko–Cantelli) at the declared confidence 1 − α;
- **ε_op** — *operational tolerance*: the declared distance threshold below which the protocol calls K_S^ι and K_{S'}^ι «equal within tolerance». A valid pass condition requires ε_op ≥ ε_stat (operational tolerance at least as large as the unavoidable statistical uncertainty), with pass declared when d(K_S^ι, K_{S'}^ι) ≤ ε_op at confidence ≥ 1 − α;
- **ε_adv** — *adversarial discrimination threshold*: the minimum distance between adversarial-K^ι (those generated by §12.1/§12.2/§12.4-style mechanisms) and legitimate-K^ι (those generated by genuine Φ-realising deployments of the operator class). This is operator-class-specific and characterises how close an adversary can train to legitimate kernel structure.

Soundness against the §12 catalogue (per Theorem 10.6(I)) additionally requires **ε_op < ε_adv** — operational tolerance strictly tighter than the adversarial-vs-legitimate gap; otherwise adversarial systems trained to match K^ι within ε_op pass (P3) but lie outside Theorem 10.6's soundness claim. The pass triple (ε_stat, ε_op, ε_adv) must be reported jointly. The estimator must record **sub-Markov mass** (not conditional-normalised kernel): the natural empirical estimator counts pairs (X_n, X_{n+1}) where X_n ∈ ι_S(Σ) and X_{n+1} ∈ ι_S(Σ) for the numerator and pairs (X_n, X_{n+1}) where X_n ∈ ι_S(Σ) (regardless of where X_{n+1} lands) for the denominator. This yields K_S^ι(s, B) directly with mass deficit 1 − K_S^ι(s, Σ) representing substrate-side excursion probability. Conditional-normalised estimation (restricting denominator to «trajectories that stay in operator-image») would yield the wrong object — the conditional kernel rather than K_S^ι — and the comparison between substrates would mask differing excursion probabilities. The measurement report must declare which estimator is used and confirm sub-Markov (mass-deficit-aware) interpretation. If the empirical distance exceeds an operator-class tolerance threshold, classify T̃ as **anchor failure** at the structural-kernel layer — substrate-induced operator-image transition rates differ beyond tolerance; (M4) fails so R_α/T1 fails. If within tolerance, sub-kernel equality is operationally verified.
5. **Verify invertibility in Dep^{img}(O)** — exhibit a candidate inverse morphism g : O@S' → O@S satisfying the analogous (M1)–(M4) and g ∘ f = id, f ∘ g = id in the image subcategory. Equivalently, R_α(O@S, O@S') = 1 per Def. 4.2. (Under (M4) sub-kernel equality, invertibility is automatic via the canonical map g(ι_{S'}(s)) := ι_S(s); the operational check is that the canonical bijection on operator-images is consistent with the measured sub-kernel equality.)
6. **If any of steps 2–5 fail (including step 4' (M4)):** classify T̃ as **anchor failure** — D-positive, non-hallucinated, but lacking structural R_α-isomorphism. This is the formal target of the §12 adversarial-deception catalogue (in particular cases 12.1–12.4 and 12.6, where D + τ pass without genuine T1; under (M4) the structural defence is no longer a typing artefact and substrate-kernel mismatch on operator-image is the load-bearing failure signature).
7. **If steps 2–5 all pass (including (M4)_ε within declared tolerance):** classify T̃ as an **empirically-accepted true transposition at tolerance ε** in the sense of Def. 6.1. The verdict is finite-sample / tolerance-relative — it discharges (M4)_ε rather than exact (M4), and discharges Ψ-layer (M3) up to the K^{rev}-estimator's declared confidence interval. The categorical claim «R_α(O@S, O@S') = 1» (exact (M4) + exact (M3) Ψ-equality) is the mathematical ideal that (M4)_ε + finite-sample step-4 verification approximates; the empirical verdict should be reported with its tolerance ε and confidence interval explicitly, not as bare «R_α = 1 verified». Conditions under which (M4)_ε → (M4) and finite-sample step-4 verdict → exact Ψ-equality uniformly in sample size are operational regularity hypotheses (bounded log-density, Glivenko–Cantelli classes for the chosen distance, finite-sample concentration for K^{rev}-estimation) declared in the test report. Proceed to Test 16.3 for sequence-level accumulation analysis, carrying the empirical-tolerance verdict and its confidence interval forward.

Report includes: the constructed morphism f (or declaration of its absence), per-step verification verdicts (with cost-preservation residue if step 4 holds only approximately and the declared tolerance), the sub-kernel-comparison metric used for step 4' and its measured value with confidence interval, and the candidate inverse g for step 5.

### Test 16.3 (accumulation discrimination)

For a sequence T_1, ..., T_n of **verified true transpositions** (each T_i having passed Tests 16.1 + 16.2 + 16.2b; i.e., D-positive, non-hallucinated, and R_α/T1-verified per Def. 6.1):

1. Measure M(O; 0) — initial architectural mobility state.
2. Execute the sequence.
3. Measure M(O; n).
4. **Drift estimation (per Theorem 9.3 hypothesis D + uniform-drift sub-test).** Estimate the conditional expected drift Δ_n := E[V(O; n+1) − V(O; n) | F_n] from observed transposition costs. Two sub-tests, matched to the two hypothesis levels of Theorem 9.3:
   - **(D-test):** check that Δ_n ≤ 0 on average over observed trajectories, AND that Δ_n < 0 on *some non-negligible measurable subset* of {V(O; n) > δ_O} (this is the operational signature of bare hypothesis (D): supermartingale + γ > 0 on at least some of {v > δ_O}). If this fails, (D) itself fails: Theorem 9.3 does not apply to the (operator-class, curriculum) pair — the LaSalle conversion dichotomy is unavailable when the drift hypothesis itself fails. Classify as **curriculum-pathological / (D)-failure** per Conjecture 9.4. This is *distinct* from the M_{failure} branch of Theorem 9.3: M_{failure} requires (D) to hold with the operator stuck within {γ_val = 0} above δ_O (residue regime *inside* the LaSalle dichotomy); (D)-failure puts the trajectory *outside* Theorem 9.3's analytical scope entirely. The two cases share «curriculum-pathological» as conjectured cause (Conjecture 9.4) but apply to disjoint regimes of drift-availability and must be reported separately.
   - **(D-uniform-test):** check that Δ_n ≤ −η for some η > 0 *uniformly* over {V(O; n) > δ_O} (operational signature of (D-uniform): drift strictly bounded below outside threshold). If (D) holds but (D-uniform) fails, finite expected hitting time E[τ_{δ_O}] < ∞ is not guaranteed (cf. §9.3 hitting time note) — the system may converge to {γ = 0} per LaSalle without reaching {V ≤ δ_O} in finite expected time.

   Proceed to step 5 only if both (D-test) and (D-uniform-test) pass; if (D) holds but (D-uniform) fails, classify the result as **drift-positive but non-uniform** — convergence to {γ = 0} guaranteed, hitting time E[τ_{δ_O}] possibly infinite.
5. If M(O; n) = M(O; 0) and n ≥ n_{min} (an operator-class-specific minimum sequence-length, distinct from the expected hitting time E[τ_{δ_O}] of Theorem 9.3; n_{min} is a free test-parameter declared in the test report — typical calibration: n_{min} chosen as an order-of-magnitude estimate of E[τ_{δ_O}] under hypothesis (D)): classify as **non-accumulating** (Def. 13.4) — invariant residue per Theorem 9.3 M_{failure} branch.
6. If c_{next}(O; n) > c_{next}(O; 0) (sequence-level upward drift in V, i.e. M(O; n) moved AWAY from mobile-by-default in the ordering {bound > intermediate > mobile-by-default}): classify as **regressing** per Def. 13.4.1 — hypothesis (D) of Theorem 9.3 fails strictly on the observed (operator-class, curriculum) pair (expected upward drift in V is excluded by (D)). Report curriculum-pathology severity distinct from the non-accumulating stuck-above-threshold residue of step 5; the two cases share (D)-failure status but differ in whether the operator is stationary above δ_O (step 5) or moving upward (this step), and Conjecture 9.4 attributes both to substrate-curriculum drift.
7. If M(O; n) = mobile-by-default and n ≥ n_{min}: classify as **full conversion to mobile-by-default** — trajectory converged to M_{success} branch of Theorem 9.3.

### Framework-level falsification

The framework is **falsified** if any of:

**F1 (architectural dispensability under sufficient observation class C):**

A *null-system* on (X_S, F_S, μ_S, K_S) is a system whose trajectory law is exactly the substrate prior P_S (no operator-position structure — i.e., the system does not satisfy Def. 1.1 or it satisfies it trivially with Α ≡ 1 on Σ × Σ, in which case Principle 1.2 is vacuous and the operator-mobility primitive carries no architectural content).

F1 holds when there exists an operator class 𝒪 and an observation class C satisfying the minimum-resolution condition — C distinguishes the operators of interest in 𝒪 (not merely one operator) from a null-system on the baseline diagnostic relevant to the framework's central claim, so the observation channel is non-trivial precisely where the framework's empirical content is asserted — under which, on the operators of interest in 𝒪, the three singleton transposition indicators pass (D_θ > 0, τ_θ > 0, R_α/T1 verified per Test 16.2b), and the sequence-level accumulation indicator M(O; n) shifts toward mobile-by-default, *and* the resulting behaviour is observationally indistinguishable under C from a null-system. Under such C the primitive is explanatorily dispensable, though it may remain non-dispensable under richer observation classes.

This is a *parsimony-falsification*: the primitive must do explanatory work somewhere in non-trivial observation-space. The minimum-resolution condition excludes vacuously-satisfying choices (e.g., trivial C = {Z, ∅} for which all systems are indistinguishable, vacuously falsifying the framework).

**F2 (impossibility of mobile-by-default):**
For all operator classes 𝒪 and all admissible substrate-curricula, **either** (a) hypothesis (D) of Theorem 9.3 (Foster-Lyapunov drift on V = c_{next}) fails, **or** (b) (D) holds but the **uniform-drift strengthening (D-uniform)** required for finite expected hitting time (§9.3 hitting-time note: γ(v) ≥ η > 0 on {v > δ_O}) fails, and the ω-limit lies in M_{failure} rather than M_{success} — so no finite E[τ_{δ_O}] < +∞ is achievable for any (𝒪, curriculum) pair. (Falsifies the M_{success} branch of Theorem 9.3's conversion dichotomy — the framework's drift-based conversion mechanism never produces mobile-by-default.) Note the split: bare (D) alone gives convergence to {γ = 0}, but finite hitting time requires (D-uniform); the framework's success-branch claim is the stronger of these two and is what F2 falsifies.

This is a *threshold-falsification*: if the conjectured threshold is never reached for any operator, the architectural-property formulation is empty.

**F3 (ill-defined architectural mobility state):**
M(O; n) cannot be defined as a measurable functional of accumulated Φ_mobility — i.e., c_{next}(O; n) is not F_Σ-measurable, or the assignment Φ_mobility ↦ {bound, intermediate, mobile-by-default} fails to be a function (depends on hidden variables not within the framework's specification). (Falsifies the architectural-property formulation itself.)

This is a *definitional-falsification*: if M is not a well-defined measurable functional, the framework's central architectural claim collapses. Stability of *estimators* of M is a separate measurement-quality question; estimator-instability does not falsify the framework.

F1, F2, F3 address distinct framework commitments (parsimony / threshold-existence / definitional-coherence respectively); they are not asserted to be logically mutually independent — e.g., F3 (M ill-defined) would render both F1 and F2 ill-formed since their conclusions presuppose M defined. The framework is *falsified by any one of F1, F2, F3* under the standard logical reading.

Operationally the tests apply in dependency order: F3 first (definitional-coherence — establishes whether M is well-defined as a functional); then F2 (whether the drift hypothesis (D) of Theorem 9.3 holds and yields finite E[τ_{δ_O}] for any operator-class/curriculum pair); then F1 (parsimony — whether the architectural primitive does explanatory work). Testing F1 or F2 without F3-clearance is inconclusive, since the test-statements themselves depend on M being a meaningful functional.

---

## §17. Conjugate-primitives map to NC2.5

For readers within the Navigational Cybernetics 2.5 corpus, the formal objects here correspond to corpus-known primitives:

| Object here | NC2.5 conjugate-primitive |
|---|---|
| Operator-position O = (Σ, F_Σ, Α, Φ, α) | Will-as-ontological-operator (ONTOΣ I) with explicit measurable structure |
| Admissibility indicator Α | Admissibility-gating (NC2.5 v2.1) — formal *admissibility before optimisation* |
| Φ as relative entropy production (§8) | Φ-ledger (NC2.5 v2.1) given information-theoretic instantiation |
| Φ_mobility (§9) | Long-horizon Φ-load accumulated across substrate-mobility events |
| Anchor α (Def. 1.1(iv)) | Operator-identity carrier (NC2.5) |
| R_α (Def. 4.2) | Recognition discipline (NC2.5 corpus) given categorical instantiation |
| Substrate S (Def. 2.1) | Substrate class (mini-series "The Bodies They Are Building") |
| Transposition T (Def. 6.1) | Operator-axis substrate-mobility (new in this work) |
| Conversion to M(O) = mobile-by-default (Def. 9.2) | Long-horizon operator development trajectory (NC2.5) |
| Failure modes (§13) | Operator failure-mode catalogue (open formalisation) |
| Adversarial deception (§12) | Adversarial corpus-checks (NC2.5 operator robustness work) |

The relation is structural mapping, not identity claim. Standalone reading does not require this section.

---

## §18. Scope, status, adjacent fields

### Scope

This work formalises a single primitive — **transposition of operator-position across substrate** — with:

* measure-theoretic state-space construction;
* categorical foundation of the deployment relation;
* information-theoretic instantiation of cost (Φ) and priors-dominance (D);
* operational trace criterion (10.2) for non-hallucinated D-positive candidates under (N)+(R), with true-transposition upgrade requiring R_α/T1;
* P_S-faithful generators cannot transpose (Theorem 10.3) with narrowly scope-bounded claim;
* adversarial-deception catalogue;
* embodiment appendix;
* illustrative example;
* LaSalle-type conversion theorem (Theorem 9.3) with substrate-curriculum-dependence sub-conjecture (Conj. 9.4);
* §16 verification stack — three singleton candidate-transposition tests (D-test, τ-test, R_α/T1 structural isomorphism check) plus sequence-level accumulation-discrimination Test 16.3 — with framework-level falsification conditions;
* load-bearing operational hypothesis catalogue (H1–H4) collecting the policy–reference-compatibility, channel-sufficiency, Feller-continuity, and per-operator-observability conditions in a single visible block (this section below);
* verification-layer-not-training-signal Goodhart caveat distinguishing per-instance adversarial defences from the broader risk of metric feedback into training loops (this section below).

The work does *not*:

* prove existence of operator-mobility in any specific system class (biological or artificial);
* specify implementation of operator-mobility in artificial systems;
* generalise beyond the conditional non-vacuity demonstrated by Example 4.1.3 — that example exhibits a finite-state construction satisfying (M3) + (M4) + D_θ > 0 + τ_θ > 0 by explicit computation (closing the worked-example gap noted in earlier drafts), but its construction relies on (i) ρ = μ(a)/μ(b) alignment between deployments via symmetric complement-to-image transitions and (ii) one-directional admissibility A_b = {b}; demonstrating that *realistic* heterogeneous-substrate deployments with broken ρ-alignment or full round-trip admissibility can also satisfy the bundle remains open;
* calibrate the expected hitting time E[τ_{δ_O}] under hypothesis (D) of Theorem 9.3 for any operator class;
* close the class of admissible substrates;
* provide full mathematical proofs (theorems are at proof-sketch level — Borel-regularity and convergence-rate arguments deferred);
* address questions of estimator efficiency (sample complexity of D-estimation; consistency rates).

These are open questions for subsequent formal and empirical work.

### Load-bearing operational hypotheses

Beyond the formal definitions and stated invariants in §§1–9, four operational hypotheses are required for specific claims of the framework to hold and are presently scattered across the text where they are first invoked. They are collected here as a visible block so that any deployment can check them explicitly.

(H1) **Policy–reference compatibility** (§9.2). The operator-image-restricted target law of π_O is dominated by ν_s on each admissible operator-image transition set: for each s ∈ Σ, (ι_S^{-1})_∗ π_O(ι_S(s), ·)|_{ι_S(A_s)} ≪ ν_s. *Required for:* non-negativity of the expected per-transposition cost ⟨φ(T)⟩ and of c_{next}, hence well-definedness of M(O; n) as a meaningful three-valued label rather than a vacuous mobile-by-default classification (Def. 9.2; §9.1 «two distinct failure modes»). Without (H1), an alternative cost functional (path KL against substrate trajectory law, non-negative by Gibbs independently of (H1)) is required.

(H2) **Channel sufficiency for the full family {P_S^θ, P_{S'}^θ, Q^θ_I}** (Lemma 7.6). The observation channel θ is a sufficient statistic for the joint family used by the D-test. *Required for:* sign-stability of D_θ under permissible channel refinements. Without (H2), the D-test verdict may flip under coarsening or refinement, and the channel choice itself becomes load-bearing for the per-candidate classification. Test 16.1 reports must declare θ explicitly; Lemmas 7.5.1 and 7.5.2 provide necessary channel-separation conditions for the prior-pair sub-task, but full-family sufficiency per Lemma 7.6 is the stronger condition required for D-sign-stability and must be reported separately when claimed.

(H3) **Feller continuity of the operator-driven Markov process** (Conjecture 9.5 (C2)). The kernel induced by π_O coupled to K_S maps bounded continuous functions to bounded continuous functions. *Required for:* the Conley–Morse decomposition of the LaSalle limit set — the named regime landscape of §9 (R ∪ G partition into chain-recurrent versus gradient-transient regions). Without (H3), Theorem 9.3 still provides supermartingale convergence and ω-limit identification under (D), but the Conley refinement is unavailable.

(H4) **Per-operator observability** (§12.5 / §12.6; Theorem 10.6 access condition). The verifier can probe each operator separately to measure per-operator D_θ, τ_θ, and R_α on its individual deployment. *Required for:* detection of multi-agent collusive imitation (§12.5) and Nash-equilibrium imitation (§12.6) — without per-operator probing the framework's verdict on aggregate-only-observable populations is *indeterminate*, neither confirmed nor falsified as deception. Theorem 10.6's per-candidate closure also incorporates (H4) as part of its declared representative; closure fails for opaque multi-agent systems even when D, τ, and R_α nominally pass at population level.

These hypotheses are *operational* rather than *structural*: their failure does not falsify the framework; it indicates that the corresponding claim cannot be made for the deployment in question. A deployment for which any of (H1)–(H4) cannot be checked is partially outside the framework's verification reach, and the corresponding test verdicts must be reported as conditional or indeterminate per §16.

**Note on the (M3)+(M4) morphism axioms (Def. 4.1) vs the operational hypotheses (H1)–(H4) above.** (M3) cost preservation and (M4) Σ-intrinsic sub-Markov-kernel equality of Def. 4.1 are *structural* morphism axioms, not operational hypotheses: they are part of what the categorical primitive R_α/T1 *means*, with operational verification at Test 16.2b steps 4 and 4' respectively. By contrast (H1)–(H4) are conditions on the broader operational setting (policy compatibility, channel sufficiency, Markov regularity, observability access) that the morphism axioms themselves do not constrain. (M3)+(M4) jointly close the «typing-artefact» reading of R_α discussed in §4.2 — without (M4), the anchor-persistence relation collapses to typing alone and admits no independent failure mode; with (M3) retained as an independent cost-axiom and (M4) added as substrate-kernel-structural axiom, R_α/T1 is genuinely non-trivial and substrate-induced operator-image kernel mismatch (or substrate-realised cost mismatch) becomes the load-bearing failure signature for the adversarial cases catalogued in §12. (M3) is *not* derivable from (M4) under Φ-realising alone — substrate-complement inflow into operator-image (which determines time-reversal at operator-image) is unconstrained by (M4); see §8.3 for the explicit obstruction and a noted symmetric strengthening (M4-rev) as an open structural extension.

### Verification layer, not training signal

The §16 verification stack — three singleton tests applied to candidate transpositions (D-test, τ-test, R_α/T1 check) plus the sequence-level accumulation-discrimination Test 16.3 over sequences of verified true transpositions — is applied externally to the system under verification. The architecture catalogues per-instance adversarial systems in §12 (strategic imitation, anchor hijacking, optimisation masquerading, synthetic mock, collusive imitation, Nash-equilibrium imitation). A broader risk class is generic rather than adversarial in intent: if D_θ, τ_θ, or c_{next} are routed back into the training or runtime adaptation loop of the system under verification, the verification metrics become control objectives, and the test surface is converted into a governor shaping behaviour toward passing the tests rather than toward whatever the operator-mobility primitive is supposed to be. This is the Goodhart pattern — the architecture is vulnerable to it whenever its diagnostic outputs become its training inputs. The architecture's defence is operational separation: the §16 verification stack is invoked by external verification, not embedded in the operator's policy or learning loop. Where such separation is impossible — closed-loop systems whose verification metrics are also their training signals — the verdict layer of the framework loses falsification-grade meaning for the system in question, even when all per-instance defences of §12 are formally satisfied.

**Non-interference invariant (NI).** We state the operational separation as an explicit precondition the deployment must satisfy for any §16 verdict to carry falsification-grade meaning:

**(NI)** During the effective interval I and the verification campaign, the verifier outputs — D_θ, τ_θ, c_{next}, the singleton/sequence verdict labels, and every intermediate estimate (K^ι, Ψ_S, K^{rev}) — are *write-only to an external audit channel* and are not a measurable input to the system-under-test's policy-update, reward, or runtime-adaptation path. Formally: the σ-algebra generated by the verifier outputs is independent of (not adapted to) the filtration driving π_O's updates during the campaign.

A deployment satisfying (NI) is **verification-isolated**; for it, the §12/§16 closure of Theorem 10.6 carries its stated catalogue-relative meaning. A deployment violating (NI) — verifier outputs feeding back into training/adaptation — has its verdict layer **void**: even a full pass of (P1)–(P4) then certifies only «the system was shaped to pass these tests», not «the operator-mobility primitive holds», and Theorem 10.6's soundness claim is withdrawn for it. (NI) is not enforced by the framework — it is a precondition the deployment report must attest (cf. §16.0 manifest); its violation-consequence is stated here so that no §16 verdict is read as falsification-grade without it.

### Status

The work is **architectural with mathematical foundation**. It supplies:

* measure-theoretically valid definitions;
* computable D given channel choice;
* Φ with information-theoretic units (nats);
* category-theoretically valid R_α with proof that it is an equivalence (Theorem 4.3);
* theorems at proof-sketch level (real argument structure, not hand-wave);
* bounded claims with explicit scope (especially 10.3, 11.1–11.3).

This is a *first-pass* formalisation. Full mathematical rigour, complete proofs, and empirical calibration are the subject of subsequent technical work. The work establishes the architectural object, supplies operational substance, and exposes the burden-structure — which is enough for the framework to be evaluated, extended, or falsified by others.

The formalisation is canonical rather than unique. The architectural primitive — transposition of operator-position across substrate — is not committed to the standard-Borel-Markov + KL + Crooks-Jarzynski-Seifert apparatus chosen here; alternative formalisations such as information geometry, enriched categories, and free-energy / variational framings are acknowledged and remain open (§18.(a)–(c)). The choice was made for operational concreteness, not theoretical exclusivity.

### Architectural alternatives acknowledged

Three families of alternative formal foundations exist for the operator-mobility primitive; each has merits not captured by the current choice, and the reader should know they were considered:

**(a) Information geometry.** Instead of treating D_θ as a difference of KL-divergences, one could equip the space of substrate-priors with the Fisher information metric, yielding a Riemannian structure on which transposition becomes a geodesic and D becomes a directional derivative along the geodesic. α-divergences (Amari) interpolate between KL and reverse-KL, parameterising the operator's directional sensitivity. We retained KL because of its direct tie to §8's relative entropy production (Crooks–Jarzynski–Seifert); a parallel information-geometric formulation would require restating §8 in Riemannian-Fisher terms, doubling the preliminaries. Open for future reformulation.

**(b) Enriched categories / Lawvere-graded morphisms.** The natural enrichment of Dep(O) over (ℝ_{≥0}, +, 0) is identified as a desirable strengthening but is **not constructed** in this work; §4.4 documents three structural obstacles (cost-source assignment, identity-morphism failure, (M3) collapse) preventing a load-bearing enrichment under current axioms, and lists the open work required to overcome them (relaxing (M3) to inequality, enriching over a richer structure like 2-categories / profunctors / sheaves, or designing a relative cost-functional with c_id = 0 by construction). Φ_mobility (§9) provides the operator-trajectory path-integral content independently of any morphism-grading.

**(c) Free-energy / active-inference framing.** The active-inference programme (Friston; with categorical formulations by Smithe 2021 and Capucci et al. 2022) frames operator-substrate dynamics through variational free energy F = D_{KL}(q ‖ p) − ⟨log likelihood⟩. The "priors-dominance" notion has direct counterparts (Bayesian model-switching as transposition; generative-model substitution as substrate-change). The current framework's D_θ is closely related to (but not identical with) cross-model evidence comparison in active inference. We did not subsume the framework under active inference for two reasons: (i) classical active inference (Friston et al. 2010-2015) fixes the operator-substrate interaction at the level of generative models, treating substrate-switching as a special case of model-switching; recent categorical reformulations (Smithe 2021; Capucci et al. 2022) explicitly address generative-model switching and overlap substantially with operator-mobility — the precise relationship between these reformulations and the operator-mobility primitive is open work; (ii) the Φ-as-relative-entropy-production identification (§8) ties to non-equilibrium statistical mechanics directly, independently of variational-inference machinery, giving Φ an interpretation outside the variational framing. A careful comparison with categorical active inference is open work and welcomed.

**(d) Policy-anchored R_α^π variant.** The morphism axiom (M4) of Def. 4.1 compares the substrate-induced operator-image sub-Markov-kernel K_S^ι rather than the policy-induced kernel K_S^{π_O, ι} (the kernel that integrates a chosen operator policy π_O of Def. 7.3 against the substrate kernel and projects to Σ). A weaker policy-anchored variant R_α^π would replace (M4) with equality K_S^{π_O, ι} = K_{S'}^{π_O, ι} — comparing how the operator's admissibility-respecting policy *behaves* on operator-image rather than how the substrate *passively* realises operator-image transitions. R_α^π is policy-dependent (different policies yield different verdicts on the same deployment pair), strictly weaker than R_α under (M4) (every R_α-iso pair is R_α^π-iso for any compatible policy, but R_α^π-iso pairs need not be R_α-iso), and admits policy-mediated illusion of persistence (an operator could «pass anchor» on a substrate with deviating physics by selecting a policy that compensates). The current work commits to the substrate-induced (M4) version as the load-bearing anchor for the reasons developed in §4.1's design-choice note; R_α^π is a coherent alternative formalism and would yield a parallel «policy-anchored framework» with the same overall classification structure but a weaker R_α/T1 test. Detailed comparison and conditions under which R_α and R_α^π coincide (e.g., policy supports operator-image-restricted forward kernel up to ν_s-equivalence) are open work.

### Position vis-à-vis adjacent fields

To the author's knowledge, the following adjacent fields touch on aspects of the problem without formulating **transposition of operator-position across substrate** as a primary architectural object with operational definition distinct from simulation/imagination, equipped with categorical-and-information-theoretic foundations:

* embodied cognition
* active inference
* enactivism
* developmental robotics
* world models
* self-modeling agents
* predictive processing
* simulation theory of empathy
* theory-of-mind agents
* multi-agent simulation
* cognitive architectures (ACT-R, SOAR, etc.)
* non-equilibrium statistical mechanics (Crooks-Jarzynski-Seifert) — touches Φ-instantiation in §8 but does not formulate operator-mobility as primary object

A counterexample is a work that operates with **transposition of operator-position** as a *named technical primitive* with:

* operational definition distinct from simulation/imagination (criterion D in §7.4);
* categorical-or-measure-theoretic foundation (analogous to §4 here);
* information-theoretic cost instantiation (analogous to §8 here);
* architectural status as primary object (not subsumed under broader frames such as predictive processing or active inference).

Counterexamples are actively invited. If such a work exists, the present is a duplicate; if not, the present establishes the primitive with formal-architectural priority.

**Technical-lineage note (nearest prior art for the structural primitives).** While the *primitive* (transposition of operator-position) is not formulated as a primary object in the fields above, several of the framework's individual technical components have well-defined nearest-neighbours in established literature, stated here for honest positioning — these are lineage acknowledgements, not subsumption claims:

* **(M4) Σ-intrinsic sub-Markov-kernel equality** is closest to **lumpability** of Markov chains (Kemeny–Snell 1960; exact/ordinary lumpability, Buchholz 1994): both ask when the restriction or aggregation of a kernel to a sub-state-space preserves Markov structure. (M4) differs in comparing the *operator-image-restricted sub-Markov kernels of two distinct substrates* (with mass-deficit / excursion equality), rather than aggregating states within one chain — a cross-substrate equality, not an intra-chain quotient. It is also distinct from **probabilistic bisimulation** (Larsen–Skou 1991): bisimulation is a behavioural coinductive equivalence, whereas (M4) is a substrate-induced structural-kernel equality (cf. Theorem 10.5's channel-response-versus-structural separation).
* **D_θ and the channel-grading Lemmas 7.5.1–7.6** sit within **comparison of statistical experiments** (Blackwell 1953; Le Cam 1986): the Blackwell–Sherman–Stein order on experiments is exactly the channel-sufficiency hierarchy invoked there.
* **Ψ_S** is the **entropy-production / irreversibility functional of stochastic thermodynamics** (Crooks 1999; Jarzynski 1997; Seifert 2012); the antisymmetry obstruction of Remark 8.4.1 is the operator-image image of the standard fluctuation-theorem antisymmetry.
* **Test 16.2b** (structural conformance of a candidate deployment to the operator-image specification) is closest in spirit to **conformance testing / ioco theory** (Tretmans 1996, 2008): both decide whether an implementation conforms to a specification via a declared test relation, though Test 16.2b's relation is measure-theoretic (sub-kernel + cost equality) rather than labelled-transition-system trace inclusion.

In each case the framework's use differs from the cited notion in the specific way noted; the connections orient the reader, they do not reduce the primitive to prior art.

---

## §19. On priority establishment in the AI-blender era

This section is metadata about the work itself, intended to be read as part of the work's claim-structure.

The work is a timestamped priority anchor in the public record for the architectural primitive of transposition of operator-position across substrate. It supplies measure-theoretic and categorical foundations for that primitive, an operational priors-dominance index, an information-theoretic cost functional, the six §10 result-forms (four theorems and two propositions — well-definedness of operator-form (Theorem 10.1), the operational trace criterion for non-hallucinated D-positive candidates under (N) and (R) with true-transposition upgrade requiring R_α/T1 (Proposition 10.2), the impossibility of transposition for P_S-faithful generators (Theorem 10.3), anchor uniqueness within [O]_α as definitional clarification (Proposition 10.4), channel-response equivalence versus structural-identity (Theorem 10.5), and the per-candidate closure of the verdict under the three singleton §16 tests (D, τ, R_α/T1) plus per-operator observability (Theorem 10.6), with sequence-level accumulation discrimination of Test 16.3 governed separately by §9 and §13.4), the conditional LaSalle-type conversion dichotomy of Theorem 9.3 under Foster-Lyapunov drift plus stochastic-LaSalle regularity and forward-invariance hypotheses, the Le Cam two-point lemma and Blackwell sufficiency partial-order for D-test channel-grading, Fano grounding for non-identifiable classification, the Sanov-type anti-coincidence bound under a Markov caveat, three impossibility results (P_S-faithful, scaling, and reversibility — narrowly scope-bounded), an adversarial-deception catalogue of six cases including Nash-equilibrium imitation, an embodiment appendix, an illustrative example, the curriculum-dependence sub-conjecture, the conditional Conley-type decomposition conjecture, a §16 verification stack composed of three singleton candidate-transposition tests (D-test, τ-test, R_α/T1) and a sequence-level accumulation-discrimination Test 16.3, with three framework-level falsification conditions on parsimony, threshold, and definitional coherence, a load-bearing operational hypothesis catalogue (H1–H4) collecting the policy–reference-compatibility, channel-sufficiency, Feller-continuity, and per-operator-observability conditions in a single visible block, a verification-layer-not-training-signal Goodhart caveat distinguishing per-instance adversarial defences from the broader risk of metric feedback into training loops, and a strengthened pair of morphism axioms in Def. 4.1 — (M3) cost preservation retained as an independent axiom (not derivable from (M4) alone under Φ-realising, owing to substrate-complement inflow into operator-image being unconstrained by (M4)) and (M4) Σ-intrinsic sub-Markov-kernel equality on operator-images — jointly making R_α/T1 a genuinely non-trivial structural test rather than a typing artefact, with corresponding operational verification steps 4 and 4' in Test 16.2b.

The work is published under CC BY-NC-ND 4.0 as part of a single OSF deposit shared with «The Thousand-Year Warrior» under DOI 10.17605/OSF.IO/ZY3PW — the phenomenological essay and the formal companion bundled as one record. A GPG-signed PDF and an OpenTimestamps Bitcoin attestation accompany the deposit, establishing a verifiable date-of-public-record for the architectural primitive and its formal substructure.

The work does not prove that operator-mobility exists in any specific system class, whether in humans, animals, AI agents, organisations, or hybrid systems. The framework defines the formal object and the falsification surface; existence-claims for specific systems are empirical questions left to subsequent work. Patent protection is not pursued for any element here, since architectural primitives at this level of abstraction are not generally enforceable under current process-patent doctrine (35 USC 101 software/abstract-idea constraints) and the author has not filed for any element of the framework (see §14 disclosure stance). The text is not an engineering specification — the embodiment families of §14 are non-exhaustive examples rather than blueprints. The theorems are at proof-sketch level (cf. the §10 standing assumption), and the architectural alternatives of §18 acknowledge open formal directions; complete Borel-measurability arguments, full proof rigour, and tightened reference density belong to a subsequent journal-rigour version rather than to this one.

The current AI landscape introduces a structural attribution problem: any conceptual or formal contribution can be input into a large language model (the AI blender), and the model's output will be attribution-detached from the source. Outputs may reproduce, paraphrase, or extend the original idea while breaking the chain of authorship. The legal-IP system (patents, copyrights, trade-secret) does not address this — process patents on cognitive architectures are nearly impossible to enforce, copyright protects expression not ideas, and trade-secret protection is incompatible with public discourse. Under these conditions, the remaining mechanism for establishing priority — the historical record of who first formulated which architectural primitive in which form — is the dated public publication chain: a timestamped, cryptographically signed, content-addressable artefact in the public record (DOI + OpenTimestamps + GPG + permissive license + searchable corpus). This work is one such artefact.

Within the Navigational Cybernetics 2.5 corpus this paper serves the same role as ONTOΣ I (will as ontological operator), the IIC series (isolation-enforced verification), the Φ-ledger of NC2.5 v2.1, «Who Is Smiling» (structural inversion personality→action), and other corpus components: it fixes the priority of an architectural facet that cannot be officially registered as IP but can remain in the public record as a verifiable origin claim. A reader who builds on this work — citing it, extending the formalism, embodying the primitive in software, applying it to specific operator-classes — is welcome to do so under CC BY-NC-ND 4.0. A reader who reproduces the architectural primitive without citation, whether through honest independent rediscovery or AI-blender-mediated attribution loss, encounters this paper in the public record as a prior formulation; that encounter is the function of priority anchoring.

This is the only available mechanism for establishing priority on architectural primitives of this kind under current legal and AI-landscape conditions. The mechanism is partial. It does not prevent reuse, does not enforce attribution beyond the licence, and does not survive deliberate adversarial removal of provenance. It does leave a verifiable date-of-public-record that is resistant to retroactive backdating, accessible to any reader, and integrated with a broader corpus that traces the architectural ideas to their origin. The paper is therefore both a mathematical foundation for the operator-mobility primitive and an anchor of originality for the same primitive in the NC2.5 corpus tradition — both functions are part of its honest design.

---

## References

* "The Thousand-Year Warrior, or A Human Absorbs the Universe" — companion phenomenological-architectural exposition (shared DOI 10.17605/OSF.IO/ZY3PW; both works in one OSF deposit)
* ONTOΣ I: Will as an Ontological Operator (Zenodo DOI 10.5281/zenodo.18190444)
* NC2.5 v2.1 axiomatic core — Φ-ledger and structural pressure (DOI 10.17605/OSF.IO/NHTC5)
* "Who Is Smiling" — structural inversion personality→action (DOI 10.17605/OSF.IO/U865W)
* G. E. Crooks (1999), "Entropy production fluctuation theorem and the nonequilibrium work relation for free energy differences", *Physical Review E* 60(3): 2721–2726.
* C. Jarzynski (1997), "Nonequilibrium equality for free energy differences", *Physical Review Letters* 78(14): 2690–2693.
* U. Seifert (2012), "Stochastic thermodynamics, fluctuation theorems and molecular machines", *Reports on Progress in Physics* 75: 126001.
* T. M. Cover, J. A. Thomas, *Elements of Information Theory*, 2nd ed., Wiley, 2006 — for KL, pushforward, Pinsker (Theorem 11.6.1).
* I. Csiszár, "Information-type measures of difference of probability distributions and indirect observations", *Studia Scientiarum Mathematicarum Hungarica* 2 (1967): 299–318 — for original Pinsker-form attribution.
* R. Durrett, *Probability: Theory and Examples*, 5th ed., Cambridge, 2019 — for standard-Borel, Markov chains, Ionescu-Tulcea / Kolmogorov extension.
* A. N. Kolmogorov, "Zur Theorie der Markoffschen Ketten", *Mathematische Annalen* 112 (1936): 155–160 — original formulation of Markov-chain time-reversal.
* E. Nelson, "The adjoint Markoff process", *Duke Mathematical Journal* 25 (1958): 671–690 — for time-reversal of Markov kernels.
* O. Kallenberg, *Foundations of Modern Probability*, 3rd ed., Springer, 2021 — for disintegration theorem (Theorem 6.4) on Polish/standard Borel spaces.
* V. I. Bogachev, *Measure Theory*, Vols. I–II, Springer, 2007 — for measure-theoretic foundations including disintegration on standard Borel.
* J. P. LaSalle, "Some extensions of Liapunov's second method", *IRE Transactions on Circuit Theory* CT-7 (1960): 520–527 — for the deterministic invariance principle.
* H. J. Kushner, *Introduction to Stochastic Control*, Holt, Rinehart and Winston, 1971 — for the stochastic LaSalle invariance principle on discrete-time Markov processes.
* S. P. Meyn, R. L. Tweedie, *Markov Chains and Stochastic Stability*, 2nd ed., Cambridge, 2009 — for Foster-Lyapunov drift criteria and hitting-time bounds (Ch. 11).
* L. Le Cam, *Asymptotic Methods in Statistical Decision Theory*, Springer, 1986 — for the two-point lemma and binary identifiability lower bounds.
* L. Le Cam, "Sufficiency and approximate sufficiency", *Annals of Mathematical Statistics* 35(4) (1964): 1419–1455 — for the Blackwell-Sherman-Le Cam characterisation of statistical experiments.
* D. Blackwell, "Equivalent comparisons of experiments", *Annals of Mathematical Statistics* 24(2) (1953): 265–272 — for the Blackwell partial order on statistical experiments.
* C. Conley, *Isolated Invariant Sets and the Morse Index*, AMS, 1978 — for Conley decomposition of invariant sets into chain-recurrent and gradient-like components.
* H. Crauel, F. Flandoli, "Attractors for random dynamical systems", *Probability Theory and Related Fields* 100 (1994): 365–393 — for stochastic extension of Conley-Morse theory to random dynamical systems.
* P.-D. Liu, "Random perturbations of axiom-A basic sets", *Journal of Statistical Physics* 90 (1998): 467–490 — for stochastic Conley-Morse decompositions.
* R. Milner, *A Calculus of Communicating Systems*, Springer LNCS 92, 1980 — for bisimulation foundations.
* D. Park, "Concurrency and automata on infinite sequences", *Proc. 5th GI-Conference on Theoretical Computer Science*, Springer LNCS 104 (1981): 167–183 — for bisimulation formalism.
* K. G. Larsen, A. Skou, "Bisimulation through probabilistic testing", *Information and Computation* 94(1) (1991): 1–28 — for probabilistic bisimulation extension.
* J. G. Kemeny, J. L. Snell, *Finite Markov Chains*, Van Nostrand, 1960 — for lumpability of Markov chains (nearest prior art for (M4) sub-Markov-kernel equality).
* P. Buchholz, "Exact and ordinary lumpability in finite Markov chains", *Journal of Applied Probability* 31(1) (1994): 59–75 — for exact lumpability as a refinement of the lumpability connection to (M4).
* J. Tretmans, "Test generation with inputs, outputs and repetitive quiescence", *Software—Concepts and Tools* 17(3) (1996): 103–120; "Model based testing with labelled transition systems", in *Formal Methods and Testing*, Springer LNCS 4949 (2008): 1–38 — for conformance testing / ioco (nearest prior art for Test 16.2b structural conformance).
* I. N. Sanov, "On the probability of large deviations of random variables", *Mat. Sbornik* 42 (1957): 11–44 — for large-deviations rate function on empirical measures.
* M. D. Donsker, S. R. S. Varadhan, "Asymptotic evaluation of certain Markov process expectations for large time", *Communications on Pure and Applied Mathematics* 28 (1975): 1–47 — for the Markov-process large-deviations extension.
* A. Dembo, O. Zeitouni, *Large Deviations Techniques and Applications*, 2nd ed., Springer, 1998 — for unified treatment of Sanov/Donsker-Varadhan.
* F. W. Lawvere, "Metric spaces, generalised logic, and closed categories", *Rendiconti del Seminario Matematico e Fisico di Milano* 43 (1973): 135–166 — for category enrichment over (ℝ_{≥0}, +, 0).
* J. Nash, "Non-cooperative games", *Annals of Mathematics* 54(2) (1951): 286–295 — for Nash-equilibrium foundations.
* Y. Polyanskiy, Y. Wu, *Lecture Notes on Information Theory* (MIT 6.441 / Yale STAT 664), 2014 — for TV-continuity of KL (Theorem 5.3.5).
* D. J. Smithe, "Compositional active inference I: bayesian lenses, statistical games", arXiv:2109.04461 (2021) — for categorical formulation of active inference.
* M. Capucci, B. Gavranović, J. Hedges, E. F. Rischel, "Towards foundations of categorical cybernetics", *EPTCS* 372 (2022): 235–248 — for categorical-cybernetics formulation.
* S. Mac Lane, *Categories for the Working Mathematician*, 2nd ed., Springer, 1998 — for category and groupoid structure.
* Synthetic Conscience project — operator-level moral regulator architecture (corpus reference)
* Operator Minerva project — operator as independent stack layer (corpus reference)
* "The Bodies They Are Building" — substrate-class characterisation (mini-series; corpus reference)

---

*Maksim Barziankou (MxBv), 24 May 2026. The Urgrund Laboratory, Poznań. CC BY-NC-ND 4.0.*
