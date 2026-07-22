# The Double Fibre of Verification

## Hidden Lineage, Hidden Admissibility, and the Contraction of Meaning

**Maksim Barziankou (MxBv)**  
PETRONUS™ · The Urgrund Laboratory · research@petronus.eu  
Poznań · July 2026  
License: CC BY-NC-ND 4.0  
This work DOI: 10.17605/OSF.IO/Z9E5N  
Axiomatic core anchor: **NC2.5 v2.1**, DOI 10.17605/OSF.IO/NHTC5

*Working formal manuscript. Finite, declaration-relative core.*

## Abstract

Verification can fail even when the visible artifact and its dynamic skeleton are both available: the artifact may hide the lineage that produced it, while the skeleton may hide the admissibility selector under which that lineage should be judged. This paper models the two losses as a compatible double fibre over finite declared histories and selector families. A target verdict factors through the visible representation exactly when it is constant on every double fibre, equivalently when its conditional entropy given the visible representation is zero under a full-support prior. The paper defines a double binding functional, separates hidden-pair ambiguity from target ambiguity, proves a conditional confined-access non-absorption result, and gives explicit crossed, compatibility-cancelled, correlated-prior, and partial-visibility finite models. On the constructive side, every finite target admits a least sufficient visible refinement with a universal property and an exact information price — the residual target entropy — and the gap between hidden-pair binding and target ambiguity is characterised exactly. A separate restriction dynamics yields finite contraction of viable meanings only under stated monotonicity and no-repair premises. Finally, a deterministic pre-commit reference monitor is shown sufficient to enforce decidable prefix-closed safety under authoritative visibility and complete mediation; it is maximally permissive among sound pre-commit monitors, and when the admissibility selector itself is hidden and the declared proposal class carries no selector information, the fibrewise intersection of the candidate safety properties yields the maximally permissive sound commitment rule on the declared proposal surface among monitors confined to the visible channel. The resulting architecture separates verification, reconstruction, property detection, enforcement, revision, liveness, and semantic coordination rather than compressing them into one score.

---

## §0. Status and claim ledger

This paper isolates a narrow epistemic structure that recurs across long-horizon verification.

A visible artifact can forget the history that produced it. A visible dynamic skeleton can also forget the admissibility rule under which that history is to be judged. These are different losses. The first is a **lineage fibre**. The second is an **admissibility fibre**. Their compatible pull-together is the **double fibre of verification**.

The paper establishes, in a finite setting, with a full-support prior wherever entropy is scored:

1. an exact factorisation criterion for visible verdicts;
2. a target-fibre witness that refutes exact visible verification;
3. a three-valued maximal sound classifier;
4. a double binding functional and its conditional-entropy decomposition;
5. reconstruction and confined-access non-absorption results;
6. a finite contraction theorem under explicit restriction and no-repair premises;
7. a reference-monitor sufficiency result for decidable prefix-closed safety properties under complete mediation;
8. an exact equality criterion separating hidden-pair binding from target ambiguity;
9. a least-sufficient-refinement theorem: every finite target admits a coarsest visible refinement through which it factors, obtained by adjoining the target's level sets fibrewise, at an exact information price equal to the residual target entropy, with a lattice of sufficient channels above it;
10. maximal permissiveness of the $\mathcal S$-monitor among sound pre-commit monitors, and an intersection-envelope theorem bounding what any monitor confined to the visible channel can soundly enforce on the declared proposal surface when the proposal class carries no selector information — an envelope that is monotone in the compatible selector set, that a genuine selector channel legitimately escapes, and that may widen if the proposal class is itself coupled to the selector;
11. a quantitative floor on approximate visible verdicts — Fano's inequality and the exact fibrewise posterior-mode error — showing that positive target ambiguity bounds every estimator, not only exact ones.

Result 10 carries three declared premises beyond the finite setting: an extension order on histories with downward-closed selectors, each admitting at least one realised history so the intersection keeps the empty run; a realisation map tying event sequences to those histories, the two together making the candidate safety properties derived rather than supplied and their closure conditions consequences rather than assumptions; and a proposal class carrying no selector information, without which the committed prefix is itself a selector channel. Result 7 carries none of these — Theorem 6.2 is stated entirely in terms of one declared property on event sequences, and precedes the enforcement declarations.

The architectural synthesis is new relative to the surrounding corpus in the following limited sense: hidden lineage and hidden admissibility are treated as two typed forgetting operations within one sealed verification problem. The information-theoretic identities, fibre factorisation principle, chain rule, and data-processing inequality are standard; the reference-monitor construction, the safety/liveness boundary, and the maximal-permissiveness pattern are likewise standard, and the References section catalogues the canonical sources.

This paper does **not** claim that verification is generally impossible, that meaning must always contract, that an isolated verifier is literally non-causal, that positive hidden-state entropy always makes a particular verdict ambiguous, or that a cognitive agent is necessary for enforcement.

The functional severance coordinate from *Severance Defect and the Binding Functional* remains independent. The present paper extends the reconstructive side of that programme; it does not replace the severance profile.

---

## §1. The problem

Suppose two completed processes produce the same visible artifact. They may differ in the order of their internal transitions, in the seams crossed, in the updates missed, or in the witness carried through those transitions. A verifier confined to the artifact cannot distinguish those histories unless the target property is constant across the corresponding observation fibre.

Now suppose the dynamic skeleton itself is visible. Even then, the rule that declares histories admissible may be absent. The same states and transitions can support more than one admissibility selector. A verifier that sees the skeleton but not the selector may therefore lack the rule by which the visible or reconstructed history should be judged.

These failures compose:

$$
(D,h,\alpha)\longmapsto (D,O_D(h)).
$$

The map forgets both the hidden history $h$ behind the observation and the admissibility selector $\alpha$ behind the skeleton $D$.

The central question is:

> When does a target verdict factor through the jointly forgotten representation, and what can be stated when it does not?

A second question concerns time. Repeated substitutions, burdens, exclusions, or reinterpretations may contract a set of viable meanings or continuations. That phenomenon is related to hidden lineage and hidden admissibility, but it is not identical to either. It requires a separate update law and separate monotonicity premises.

---

## §2. Typed setup

### 2.1 Dynamic skeletons and histories

Let $\mathcal D$ be a finite declared class of dynamic skeletons. For each $D\in\mathcal D$, let:

- $\mathcal H_D$ be a finite set of typed histories supported by $D$;
- $\mathcal Y_D$ be a finite visible codomain;
- $O_D:\mathcal H_D\to\mathcal Y_D$ be the declared observation map.

A history may encode a transition sequence, a seam sequence, a propagation trace, a retained-memory trajectory, or another typed provenance object. No metaphysical claim is attached to the word history: it is whatever the audit declares and can operationally compare.

An audit **may** additionally declare a partial order $\sqsubseteq$ on $\mathcal H_D$, read as *extends*: $h'\sqsubseteq h$ when $h$ continues $h'$. Every provenance object listed above carries a natural such order, but nothing in §§3–5 uses one, and the models of §5 leave $\mathcal H_D$ unordered. The order is declared only where it is needed, in §6.6.

### 2.2 Admissibility selectors

For each $D$, let $\mathfrak A(D)$ be a finite declared family of admissibility selectors

$$
\alpha:\mathcal H_D\to\{0,1\}.
$$

The family may be restricted by window closure, shift compatibility, burden monotonicity, or another stated axiom system. Those restrictions are part of the declaration. The dynamic skeleton does not determine $\mathfrak A(D)$ uniquely.

One restriction presupposes the order of §2.1 and is used in §6.6. Call $\alpha$ **downward closed** when $\alpha(h)=1$ and $h'\sqsubseteq h$ imply $\alpha(h')=1$: a history cannot be admissible while something it extends is not. This is a restriction on the declared family, not a property of selectors in general — the crossed selectors of §5.1 are not downward closed under any strict order on their two histories, which is exactly why §5 leaves $\mathcal H_D$ unordered.

The structural forgetting map is

$$
U:(D,\alpha)\longmapsto D.
$$

Its fibre over $D$ is

$$
\mathcal F_U(D)=\mathfrak A(D).
$$

The existence of two selectors in $\mathfrak A(D)$ is not yet a disagreement about a particular history. It becomes verdict-relevant only when they evaluate some compatible history differently.

### 2.3 Compatibility

Not every history-selector pair must be admitted as a possible completion. Let

$$
\mathcal C_D\subseteq \mathcal H_D\times\mathfrak A(D)
$$

be the declared compatibility relation. A point $(h,\alpha)\in\mathcal C_D$ means that $h$ and $\alpha$ may jointly occur in the sealed comparison class.

The completed world space is

$$
\Theta=\coprod_{D\in\mathcal D}\{D\}\times\mathcal C_D.
$$

A world is written $\theta=(D,h,\alpha)$.

Compatibility is load-bearing. It may encode typing constraints, construction constraints, empirical exclusions, or coupling rules. It must be fixed before scoring. If it is changed after a target verdict is seen, the audit has changed.

### 2.4 The two component fibres

For $y\in O_D(\mathcal H_D)$, define the lineage fibre

$$
\mathcal F_O(D,y)=\{h\in\mathcal H_D:O_D(h)=y\}.
$$

The admissibility fibre is $\mathcal F_U(D)=\mathfrak A(D)$.

These are independent as **types of forgetting**, not necessarily as random variables. Compatibility can correlate histories and selectors.

### 2.5 The double fibre

Define the visible map

$$
V:\Theta\to\coprod_{D\in\mathcal D}\{D\}\times\mathcal Y_D,
\qquad
V(D,h,\alpha)=(D,O_D(h)).
$$

**Definition 2.1 (Double fibre).** For an attained visible value $v=(D,y)$,

$$
\mathcal F_2(D,y)
=
V^{-1}(D,y)
=
\{(D,h,\alpha):(h,\alpha)\in\mathcal C_D,\ O_D(h)=y\}.
$$

After suppressing the visible $D$,

$$
\mathcal F_2(D,y)
\cong
\{(h,\alpha)\in\mathcal C_D:h\in\mathcal F_O(D,y)\}.
$$

In general,

$$
\mathcal F_2(D,y)\subseteq
\mathcal F_O(D,y)\times\mathfrak A(D).
$$

Equality holds only when the declared compatibility relation contains every pair in that product. Calling the double fibre a Cartesian product without checking compatibility is an overclaim.

### 2.6 Targets

A finite target is a map

$$
Q:\Theta\to\mathcal Q.
$$

Important examples are:

1. **admissibility verdict**
   $$
   J_{\mathrm{Adm}}(D,h,\alpha)=\alpha(h);
   $$

2. **persistence verdict**
   $$
   J_P(D,h,\alpha)=I_P(h),
   $$
   where $I_P$ is a declared seam- or witness-preservation criterion;

3. **identity-witness label**
   $$
   J_W(D,h,\alpha)=W(h);
   $$

4. **vector verdict**
   $$
   \mathbf J=(J_{\mathrm{Adm}},J_P,J_{\mathrm{Live}}),
   $$
   where $J_{\mathrm{Live}}$ is a declared liveness verdict, typed per audit; this paper treats it as an imported coordinate (§13) and proves nothing liveness-specific about it.

The target must be declared before looking at the desired result. Changing from full completion reconstruction to a coarse property after observing a non-identifiability witness changes the question.

---

## §3. Exact verification through the visible representation

### 3.1 Exact visible verification

**Definition 3.1.** A target $Q$ is exactly verifiable from $V$ on $\Theta$ if there exists

$$
q:\operatorname{im}(V)\to\mathcal Q
$$

such that

$$
Q=q\circ V.
$$

The verifier is then confined to the declared visible representation. A constant map for one preselected target world does not count as uniform verification over $\Theta$.

### 3.2 Factorisation theorem

**Theorem 3.2 (Double-fibre factorisation).** Let $\Theta$ and $\mathcal Q$ be finite, and let $\pi$ be a full-support prior on $\Theta$. The following are equivalent:

1. $Q=q\circ V$ for some $q$;
2. $Q$ is constant on every double fibre $\mathcal F_2(D,y)$;
3. $H_\pi(Q\mid V)=0$.

**Proof.** If $Q=q\circ V$, two worlds with the same visible value have the same target, so $Q$ is fibre-constant. If $Q$ is fibre-constant, define $q(v)$ as the common target value on $V^{-1}(v)$; this is well-defined and gives $Q=q\circ V$. For finite variables, $H(Q\mid V)=0$ exactly when $Q$ is almost surely a function of $V$. Full support converts almost-sure constancy into constancy on every declared fibre. $\square$

The theorem is target-relative. A fibre may contain many hidden completions while a coarse target remains constant.

### 3.3 Target-fibre witness

**Corollary 3.3 (Target-fibre witness).** If there exist **compatible** pairs

$$
(h_0,\alpha_0),\,(h_1,\alpha_1)\in\mathcal C_D,
\qquad
\theta_0=(D,h_0,\alpha_0),\quad
\theta_1=(D,h_1,\alpha_1),
$$

such that

$$
O_D(h_0)=O_D(h_1)
\quad\text{but}\quad
Q(\theta_0)\neq Q(\theta_1),
$$

then no exact $V$-confined verifier for $Q$ exists on the declared class.

*Proof.* Compatibility places $\theta_0$ and $\theta_1$ in $\Theta$, and the common visible value places both in the double fibre $\mathcal F_2\big(D,O_D(h_0)\big)$. They carry different target values, so $Q$ is not fibre-constant; Theorem 3.2 then denies factorisation. $\square$

One pair is sufficient. The witness must preserve all visible coordinates and differ in the declared target. A pair that changes an undeclared side channel is not a witness for the original channel. The compatibility requirement is not decorative: a pair drawn from $\mathcal F_O(D,y)\times\mathfrak A(D)$ but absent from $\mathcal C_D$ is not a world at all, and a refutation built on such a pair asserts exactly the product assumption that F6 forbids.

### 3.4 The maximal sound partial verdict

For binary $Q$ and an attained visible value $(D,y)\in\operatorname{im}(V)$, define

$$
q^\star(D,y)=
\begin{cases}
1,& Q=1\text{ on all of }\mathcal F_2(D,y),\\
0,& Q=0\text{ on all of }\mathcal F_2(D,y),\\
?,& \text{otherwise}.
\end{cases}
$$

**Proposition 3.4 (Fibre trichotomy).** The classifier $q^\star$ is sound: whenever it returns $0$ or $1$, that value equals $Q$ for every compatible hidden completion. It is maximally decisive among all sound $V$-confined classifiers $\operatorname{im}(V)\to\{0,1,?\}$: every heterogeneous target fibre must receive $?$. The restriction to $V$-confined classifiers is what makes the claim non-trivial — a classifier reading $\theta$ directly is sound and never returns $?$, but it is not a verifier in the sense of Definition 3.1.

**Proof.** Homogeneous fibres permit their common value. On a heterogeneous fibre, returning either binary value would be wrong for at least one compatible completion. $\square$

The symbol $?$ means insufficient information under the sealed declaration. It is not a claim that the world itself is indeterminate.

### 3.5 Vector targets

**Proposition 3.5.** A finite vector target

$$
\mathbf Q=(Q_1,\ldots,Q_m)
$$

factors through $V$ if and only if every coordinate $Q_i$ factors through $V$.

*Proof.* If $\mathbf Q=q\circ V$ then $Q_i=\mathrm{pr}_i\circ q\circ V$ for each $i$. Conversely, if $Q_i=q_i\circ V$ for every $i$, then $\mathbf Q=(q_1,\ldots,q_m)\circ V$. $\square$

Exact recovery of the vector therefore requires fibre constancy of every coordinate separately. This does not forbid some scalar summary from factoring through $V$: a collapsed score such as $Q_1\wedge Q_2$ can be fibre-constant while its constituent coordinates are not. The witness is given in §5.5, where the score factors through $V$ and is non-constant on $\Theta$ while **neither** conjunct factors; a model with a constant observation map can only make the point with a globally constant score, which collapses nothing. What is lost is exactly the coordinate structure: a factoring score carries no uniform information about a non-factoring coordinate, and failure of one coordinate does not logically determine the others.

### 3.6 Specialisations

**Corollary 3.6 (Fibrewise agreement test for the admissibility verdict).** $J_{\mathrm{Adm}}$ factors through $V$ if and only if for every attained $(D,y)$ and all pairs $(h,\alpha),(h',\alpha')\in\mathcal F_2(D,y)$,

$$
\alpha(h)=\alpha'(h').
$$

*Proof.* Theorem 3.2 with $Q=J_{\mathrm{Adm}}$; constancy on the double fibre is literally the displayed agreement. $\square$

The test needs no entropy, and it separates the two failure axes: a selector-only witness violates the agreement with $h=h'$, a lineage-only witness violates it with $\alpha=\alpha'$.

**Remark 3.7 (Support-relative version).** For an arbitrary prior $\pi$, $H_\pi(Q\mid V)=0$ holds if and only if $Q$ is constant on the support restriction $\mathcal F_2(D,y)\cap\operatorname{supp}\pi$ of every double fibre of positive mass. Zero-mass completions are invisible to the entropy, so $H_\pi(Q\mid V)=0$ is weaker than constancy on the whole of every fibre over $\Theta$: it ignores every world outside $\operatorname{supp}\pi$. When $\operatorname{supp}\pi\neq\Theta$, a world outside the support can break whole-fibre constancy while leaving the entropy zero — whether it is a zero-mass world inside a scored fibre or a world in a fibre of zero mass. Exact factorisation on all of $\Theta$ is recovered in the full-support case $\operatorname{supp}\pi=\Theta$, the setting of Theorem 3.2. Probabilistic identifiability on a sub-support must not be reported as declaration-wide verification.

### 3.7 The least sufficient refinement

The negative results above say when the declared channel is too coarse. The constructive counterpart says exactly how much must be added.

Observations are compared by the partitions of $\Theta$ they induce. For $O_1:\Theta\to\mathcal Y_1$ and $O_2:\Theta\to\mathcal Y_2$, say that $O_2$ **refines** $O_1$, written $O_2\succeq O_1$, when $O_2(\theta)=O_2(\theta')$ implies $O_1(\theta)=O_1(\theta')$: every $O_2$-fibre lies inside one $O_1$-fibre, equivalently $O_1=g\circ O_2$ for some $g$ on the attained values. These observation channels are typed on $\Theta$, unlike the declared observation map $O_D$ of §2.1, which is typed on $\mathcal H_D$; the letter is shared, the domains are not. Refinement compares information content, not codomain labels. It is an order on observation channels only — unrelated both to the temporal subdivision of a history into finer steps in the companion seam papers and to the specification-refinement question of §12, problem 8.

**Theorem 3.8 (Least sufficient visible refinement).** Let $Q:\Theta\to\mathcal Q$ be a finite target. Define

$$
V_Q(\theta)=\big(V(\theta),\,Q(\theta)\big).
$$

Then:

1. $V_Q\succeq V$, and $Q$ factors through $V_Q$;
2. $V_Q$ is coarsest with these properties: if $O'\succeq V$ and $Q=f\circ O'$ for some $f$, then $O'\succeq V_Q$;
3. the $V_Q$-fibres are exactly the intersections of $V$-fibres with $Q$-level sets, so the information that must be added to $V$ is exactly the target's level-set partition on each mixed double fibre — and nothing on any homogeneous fibre.

*Proof.* (1) is immediate from the definition. (2) Suppose $O'(\theta)=O'(\theta')$. Then $V(\theta)=V(\theta')$ because $O'\succeq V$, and $Q(\theta)=f(O'(\theta))=f(O'(\theta'))=Q(\theta')$; hence $V_Q(\theta)=V_Q(\theta')$, which is $O'\succeq V_Q$. (3) restates the definition of $V_Q$. $\square$

The theorem is the constructive dual of Corollary 3.3. The witness pair says that a mixed fibre defeats every $V$-confined verifier; the refinement theorem says which further distinctions — and no more — restore the verdict. The refinement $V_Q$ is defined through $Q$ itself, so it specifies the informational content of a sufficient channel, not a procedure the confined verifier could execute: the theorem locates the missing information; it does not conjure it. Which physical instrument realises those distinctions is a separate engineering obligation (§12, problem 2).

**Corollary 3.9 (Lattice form).**

1. $Q=q\circ V$ for some $q$ if and only if $V\succeq V_Q$;
2. for a vector target $\mathbf Q=(Q_1,\ldots,Q_m)$, the channel $V_{\mathbf Q}$ is the least upper bound of $V_{Q_1},\ldots,V_{Q_m}$ in the refinement order among observations refining $V$;
3. if $Q_r=r\circ Q$ is a coarsening of the target, then $V_Q\succeq V_{Q_r}$, so exact visibility of $Q$ yields exact visibility of every deterministic summary of $Q$.

*Proof.* (1) If $V\succeq V_Q$, then $V_Q=g\circ V$ and $Q$ is the second coordinate of $g\circ V$; conversely, $Q=q\circ V$ makes $V_Q=(V,q\circ V)$ a function of $V$. (2) $V_{\mathbf Q}$ refines every $V_{Q_i}$; an observation refining $V$ and every $V_{Q_i}$ determines $V$ and every coordinate, hence $V_{\mathbf Q}$. (3) Equal $V_Q$-values force equal $(V,r(Q))$-values. $\square$

Theorem 3.2 is thus the bottom test of a lattice: the declared channel verifies the target exactly when it already sits above the least sufficient refinement, vector targets join componentwise — which makes Proposition 3.5 constructive — and coarser targets sit lower. The sufficient channels do form a lattice, with $V_Q$ at the bottom. They are closed under join because the common refinement of two channels refining $V_Q$ again refines it, and under meet because the finest common coarsening does too — the join of two equivalence relations contained in the $V_Q$-relation is contained in it, that relation being transitive. Both closures are immediate; clause (2) is a sharper statement about the specific channels $V_{Q_1},\ldots,V_{Q_m}$ of a vector target, not the general closure. As with refinement itself, the lattice lives on the induced partitions rather than on the maps.

---

## §4. The double binding functional

Let the random world $(D,H,A)$ have full-support law $\pi$ on $\Theta$, where $A$ is the selector-valued coordinate. Following standard information-theoretic usage, $H$ denotes both the entropy functional and the history-valued coordinate, as in $H(H,A\mid V)$; position fixes the reading. Let

$$
Y=O_D(H),\qquad V=(D,Y).
$$

### 4.1 Pointwise and average double binding

**Definition 4.1.** For an attained $v=(D,y)$,

$$
\mathfrak B_2^\pi(v)=H_\pi(H,A\mid V=v).
$$

The average double binding is

$$
\overline{\mathfrak B}_2^\pi=H_\pi(H,A\mid V).
$$

This measures residual uncertainty about the hidden history-selector pair. It does not by itself measure functional damage, computational difficulty, moral quality, or ambiguity of a specific verdict.

Under a uniform posterior on a finite double fibre,

$$
\mathfrak B_2^{\mathrm{unif}}(D,y)
=
\log_2|\mathcal F_2(D,y)|.
$$

### 4.2 Exact decomposition

**Theorem 4.2 (Double binding decomposition).**

$$
\begin{aligned}
H(H,A\mid V)
&=H(H\mid V)+H(A\mid H,V)\\
&=H(H\mid V)+H(A\mid V)-I(H;A\mid V).
\end{aligned}
$$

**Proof.** The first line is the conditional chain rule. The second is immediate from the definition $I(H;A\mid V)=H(A\mid V)-H(A\mid H,V)$. $\square$

The terms have distinct meanings:

- $H(H\mid V)$ is lineage binding;
- $H(A\mid V)$ is visible-selector ambiguity;
- $H(A\mid H,V)$ is selector ambiguity remaining after the history is supplied;
- $I(H;A\mid V)$ is the dependence correction.

No independence assumption is licensed by the phrase two fibres. The correction can be made positive by either of two distinct mechanisms: a restricted compatibility relation that removes pairs from the support (§5.2), or a correlated prior on a full product support (§5.4). Naming the term after compatibility alone would conflate them; Lemma 4.7 in §4.6 separates the two regimes exactly.

### 4.3 Verdict ambiguity

Define the target ambiguity

$$
\mathfrak V_Q^\pi=H_\pi(Q\mid V).
$$

The fraktur $\mathfrak V$ is chosen to avoid collision with the visible map $V$ of §2.5.

**Proposition 4.3.** If $Q$ is a deterministic function of $(D,H,A)$, then

$$
H(Q\mid V)\leq H(H,A\mid V).
$$

**Proof.** Since $D$ is already contained in $V$, conditional data processing for the deterministic map $(D,H,A)\mapsto Q$ yields the inequality. $\square$

Positive double binding is therefore only a capacity for target ambiguity. It does not entail it. The target can be constant on a non-singleton double fibre. Conversely, by the same inequality, positive target ambiguity entails positive double binding: $\mathfrak V_Q^\pi>0$ forces $\overline{\mathfrak B}_2^\pi>0$. Proposition 4.8 in §4.6 characterises exactly when the inequality is tight.

### 4.4 Reconstruction criterion

**Proposition 4.4 (Hidden-pair reconstruction).** Under a full-support prior on finite $\Theta$, the following are equivalent:

1. every double fibre is a singleton in its hidden pair $(H,A)$;
2. there exists $\rho$ such that $\rho(V)=(H,A)$ on all of $\Theta$;
3. $H(H,A\mid V)=0$.

*Proof.* Theorem 3.2 with $Q$ the hidden pair itself. Constancy of that target on a double fibre says the fibre has one hidden pair, which is (1); factorisation through $V$ is the decoder $\rho$ of (2); the entropy clause transfers unchanged. $\square$

This is reconstruction of the declared hidden pair. A coarser lineage label may be reconstructible even when the full history is not. Reconstruction is also the top of the target hierarchy: under full support, $H(H,A\mid V)=0$ if and only if every finite target factors through $V$ — one direction is Proposition 4.3 applied to an arbitrary target, the other takes the target to be the hidden pair itself.

### 4.5 Confined non-absorption

Let $D$ be public side information already included in $V$, and let $Z$ be every datum available to a downstream verifier or upper layer. The symbol $Z$ is used here so that $W$ remains reserved for the identity witness of §8.1.

**Definition 4.5.** Access is confined to $V$, conditionally on $D$, when

$$
(H,A)\longrightarrow V\longrightarrow Z\mid D
$$

is a conditional Markov chain; equivalently,

$$
I((H,A);Z\mid V,D)=0.
$$

Independent randomness and arbitrary post-processing are allowed; undeclared information about $(H,A)$ is not.

**Theorem 4.6 (Confined non-absorption).** Under Definition 4.5,

$$
H(H,A\mid Z,D)
\geq
H(H,A\mid V,D)
=
H(H,A\mid V).
$$

Consequently, if $H(H,A\mid V)>0$, no decoder from $(Z,D)$ can uniformly reconstruct the hidden pair.

If, in addition, $H(Q\mid V)>0$, then

$$
H(Q\mid Z,D)
\geq
H(Q\mid V,D)
=
H(Q\mid V)
>0,
$$

so no exact verifier based on $(Z,D)$ can recover $Q$ uniformly.

**Proof.** Conditional data processing gives

$$
I((H,A);Z\mid D)
\leq
I((H,A);V\mid D),
$$

which is equivalent to the hidden-pair entropy inequality. Because $D$ is already a coordinate of $V$, conditioning on both $V$ and $D$ is the same as conditioning on $V$. The same conditional Markov relation holds for every deterministic target $Q=Q(D,H,A)$, giving the target-level inequality. $\square$

If $D$ is already retained inside $Z$, the conditioning on $D$ may be suppressed. The theorem says nothing when a side channel breaks the conditional Markov relation. It also does not prohibit approximation, property detection, emulation, or independent rediscovery.

### 4.6 Exact regimes

Two exact statements pin down the boundary cases of the decomposition and of Proposition 4.3.

**Lemma 4.7 (Product regime).** If, conditionally on every attained visible value $v$, the posterior factorises,

$$
\pi(h,\alpha\mid v)=\pi(h\mid v)\,\pi(\alpha\mid v),
$$

then $I(H;A\mid V)=0$ and the double binding is additive: $H(H,A\mid V)=H(H\mid V)+H(A\mid V)$. Conversely, $I(H;A\mid V)=0$ forces that factorisation on every attained fibre of positive mass, so the two conditions are equivalent; a law that fails to factorise on some such fibre therefore has $I(H;A\mid V)>0$. A factorised fibre law has product support, so a fibre whose conditional support is not the product of its marginal supports gives $I(H;A\mid V)>0$ as a special case — one detectable from the support alone, without reference to the numerical law.

*Proof.* Conditional mutual information vanishes exactly at conditional independence, which is the displayed factorisation; additivity is then Theorem 4.2. The support of a product law is the product of the marginal supports, so a non-product conditional support excludes factorisation on that fibre; that fibre contributes strictly positive conditional mutual information, and every fibre contributes non-negatively. $\square$

The diagonal relation of §5.2 has a non-product conditional support, so its correction is forced; the correlated prior of §5.4 keeps a full product support and produces its correction through the law alone. Removing pairs does not force dependence when the removal leaves a product — deleting every pair containing one history shrinks the support to a smaller product and permits $I(H;A\mid V)=0$; the non-product condition is the exact trigger.

**Proposition 4.8 (Equality criterion).** Let $\pi$ have full support and let $Q$ be a deterministic function of $(D,H,A)$. Then

$$
H(Q\mid V)=H(H,A\mid V)
$$

if and only if $Q$ is injective on every attained double fibre: for all $(h,\alpha),(h',\alpha')\in\mathcal F_2(D,y)$ with $(h,\alpha)\neq(h',\alpha')$, the target values differ.

*Proof.* Since $D$ is a coordinate of $V$ and $Q$ is a function of $(D,H,A)$, the chain rule gives

$$
H(H,A\mid V)=H(Q\mid V)+H(H,A\mid Q,V).
$$

Equality therefore holds exactly when $H(H,A\mid Q,V)=0$, that is, when the hidden pair is almost surely determined by the pair $(Q,V)$. Under full support this is determination on every attained fibre, which is the displayed injectivity. $\square$

The gap between double binding and target ambiguity is thus not an accident of the examples: it closes exactly when the target separates every pair of hidden completions that share an observation, and it is strict in every other audit.

**Proposition 4.9 (Information budget of repair).** Let $\pi$ have full support.

1. $H(V_Q\mid V)=H(Q\mid V)$: the least sufficient refinement adds exactly the residual target entropy;
2. every observation $O'\succeq V$ through which $Q$ factors satisfies $H(O'\mid V)\ge H(Q\mid V)$;
3. an added side channel $X$ obeys $H(Q\mid V,X)=H(Q\mid V)-I(Q;X\mid V)$, so repair is monotone; and if $X$ is itself an observation on $\Theta$, the verdict becomes exact precisely when the side channel carries the full residual entropy.

*Proof.* (1) $V_Q=(V,Q)$, and the chain rule gives $H(V,Q\mid V)=H(Q\mid V)$. (2) $Q$ is a function of $O'$, so $H(Q\mid V)\le H(O'\mid V)$. The entropy identity in (3) is the definition of conditional mutual information and needs nothing further; exactness at $H(Q\mid V,X)=0$ is Theorem 3.2 applied to the enlarged channel $(V,X)$, which is again a map on $\Theta$ precisely because $X$ is, and it is there that the full-support hypothesis is used. A randomised or externally seeded side channel still satisfies the identity but is not an observation on $\Theta$, so the exactness reading does not transfer to it. $\square$

Target ambiguity is therefore not only an obstruction measure. It is the exact price, in bits, of the channel that verification lacks: no sufficient enlargement can carry less, and the least one carries exactly that. Falsifier F1's recomputation obligation has a closed form.

---

## §5. Minimal finite models

### 5.1 Fully crossed double fibre

Fix one skeleton $D$. Let

$$
\mathcal H_D=\{h_0,h_1\},\qquad
\mathfrak A(D)=\{\alpha_0,\alpha_1\},
$$

with

$$
\alpha_0(h_0)=1,\quad \alpha_0(h_1)=0,
$$
$$
\alpha_1(h_0)=0,\quad \alpha_1(h_1)=1.
$$

Let $O_D(h_0)=O_D(h_1)=y$, let every pair be compatible, and place the uniform prior on the four worlds.

Then

$$
H(H,A\mid V)=2\text{ bits},
$$
$$
H(H\mid V)=1,\qquad H(A\mid V)=1,\qquad I(H;A\mid V)=0.
$$

For $J_{\mathrm{Adm}}=\alpha(H)$, two worlds are accepted and two rejected, so

$$
H(J_{\mathrm{Adm}}\mid V)=1\text{ bit}.
$$

The pairs $(h_0,\alpha_0)$ and $(h_0,\alpha_1)$ form a selector-only target-fibre witness. The pairs $(h_0,\alpha_0)$ and $(h_1,\alpha_0)$ form a lineage-only witness. The four-world class exhibits both failures at once.

### 5.2 Compatibility cancellation

Keep the same histories and selectors, but declare only

$$
\mathcal C_D=\{(h_0,\alpha_0),(h_1,\alpha_1)\}.
$$

Under the uniform prior,

$$
H(H\mid V)=1,\qquad H(A\mid V)=1,\qquad I(H;A\mid V)=1,
$$

and therefore

$$
H(H,A\mid V)=1\text{ bit}.
$$

Yet $J_{\mathrm{Adm}}=1$ on both worlds, so

$$
H(J_{\mathrm{Adm}}\mid V)=0.
$$

This model proves two points at once: the double fibre need not be a product, and positive double binding need not make the admissibility verdict ambiguous.

### 5.3 Four diagnostic regimes

For a fixed visible value, the following regimes are distinct:

| Lineage multiplicity | Selector multiplicity | Hidden-pair status |
|---:|---:|---|
| $1$ | $1$ | pair reconstructible |
| $>1$ | $1$ | lineage ambiguity only |
| $1$ | $>1$ | selector ambiguity only |
| $>1$ | $>1$ | both axes present, subject to compatibility |

This table classifies hidden completions, not verdicts. The first row is a singleton fibre, so every target is constant on it by construction; each of the remaining rows can still contain either a homogeneous or a heterogeneous target fibre. The minimal models of §5.1, §5.2, §5.4 and §5.5 all realise the last row; the intermediate rows are reached by restricting compatibility so that only one axis retains multiplicity. Restricting §5.1 that way fixes the verdict pattern as well, so the homogeneous sub-cases of rows 2 and 3 need either a coarser target or selectors declared in no model here.

### 5.4 Dependence without restriction

Keep the fully crossed compatibility relation of §5.1 — every pair $(h_i,\alpha_j)$ admitted — but replace the uniform prior by the correlated full-support law

$$
\pi(h_0,\alpha_0)=\pi(h_1,\alpha_1)=\tfrac12-\varepsilon,
\qquad
\pi(h_0,\alpha_1)=\pi(h_1,\alpha_0)=\varepsilon,
$$

for $\varepsilon\in(0,\tfrac12)$ with $\varepsilon\neq\tfrac14$. Both hidden marginals remain uniform, so with $h_2$ the binary entropy function,

$$
H(H\mid V)=H(A\mid V)=1,
\qquad
H(H,A\mid V)=1+h_2(2\varepsilon),
\qquad
I(H;A\mid V)=1-h_2(2\varepsilon)>0,
$$

and the admissibility verdict has $H(J_{\mathrm{Adm}}\mid V)=h_2(2\varepsilon)$. At $\varepsilon=\tfrac18$ the dependence correction is exactly $\tfrac34\log_2 3-1$ bits.

No pair has been excluded: the support is the full product, yet the dependence correction is positive because the fibre law does not factorise (Lemma 4.7). Support restriction (§5.2) and prior correlation are therefore independent mechanisms for coupling the two fibres, and an audit that observes $I(H;A\mid V)>0$ cannot conclude that the compatibility relation was restricted.

### 5.5 Partial visibility

The three models above share a constant observation map, so the visible codomain of each is a single point. That suffices to exhibit binding, cancellation and dependence, but it degenerates three things at once: factorisation through $V$ collapses to global constancy, the least sufficient refinement of Theorem 3.8 is instantiated only where $V$ carries no information, and the detectability regime of §8.3 has no instance, since a constant $V$ forces $I(P;S^\star\mid D)=0$ for every property. The following model separates the visible values.

Fix one skeleton $D$. Histories are written $g_i$ here rather than $h_i$, so that no index collides with the binary entropy $h_2$ of §5.4. Let

$$
\mathcal H_D=\{g_0,g_1,g_2,g_3\},
\qquad
\mathfrak A(D)=\{\alpha_0,\alpha_1\},
$$

with

$$
\alpha_0\text{ admitting }\{g_0,g_2\},
\qquad
\alpha_1\text{ admitting }\{g_1,g_3\},
$$

let every pair be compatible, and let

$$
O_D(g_0)=O_D(g_1)=y_0,
\qquad
O_D(g_2)=O_D(g_3)=y_1 .
$$

Place the uniform prior on the eight worlds. The selector values are declared for typing — a selector must be total on $\mathcal H_D$ — and the quantities below do not depend on them, since the target $P$ is a function of the history alone. Let $P$ be the property taking value $1$ on $g_0,g_1,g_2$ and $0$ on $g_3$, and take the declared statistic $S^\star=V$.

Each double fibre carries four hidden pairs, so

$$
H(H,A\mid V)=2\text{ bits}.
$$

The $y_0$ fibre is $P$-homogeneous and the $y_1$ fibre is mixed, so

$$
H(P\mid V)=\tfrac12,
\qquad
H(P)=h_2\big(\tfrac14\big)=2-\tfrac34\log_2 3,
\qquad
I(P;S^\star\mid D)=\tfrac32-\tfrac34\log_2 3>0 .
$$

Three conditions hold simultaneously: the hidden pair is not reconstructible, the property is not exactly verifiable from $V$, and the property is statistically detectable. This is the regime described in §8.3, and it is the first model here to instantiate it. The leakage is saturated rather than small — $I((H,A);V\mid D)=H(Y\mid D)=1$ bit, the whole capacity of a binary visible channel — so the model witnesses the regime, not the narrow-channel reading of it.

The same model supplies a non-degenerate witness for Proposition 3.5. Let

$$
Q_1=P,
\qquad
Q_2=1\text{ on }\{g_0,g_1,g_3\},\ 0\text{ on }\{g_2\}.
$$

On the $y_1$ fibre $Q_1$ reads $(1,0)$ and $Q_2$ reads $(0,1)$, so **neither coordinate factors through $V$**. Their conjunction is $1$ on $\{g_0,g_1\}$ and $0$ on $\{g_2,g_3\}$, constant on each fibre and non-constant on $\Theta$, so the collapsed score factors while no constituent does. This is the genuine collapse: a score that carries no uniform information about either coordinate it was built from. The crossed model of §5.1 can make the point only with a globally constant score, which collapses nothing.

---

## §6. Verification, enforcement, and revision

### 6.1 Five roles

A verification architecture should distinguish at least five roles:

1. **producer** — emits the artifact or proposes a transition;
2. **observation channel** — exposes the declared $V$;
3. **verifier** — computes a target or partial verdict;
4. **enforcer** — can block or commit the proposed transition;
5. **revision authority** — may change the selector, observation contract, or system version.

These roles may be implemented by one machine, but their authorities remain different. Detection of a violation does not entail authority to block it. Authority to block does not entail authority to revise the rule. Visibility of the boundary does not entail optimizer query, gradient, or write access to that boundary.

### 6.2 Structural and transaction-level admissibility

Let $\mathcal A_h$ be an action set, $\mathcal E_h$ an effect space, and

$$
e_h:\mathcal A_h\to\mathcal E_h
$$

the declared effect map. Let

$$
\mathrm{Adm}^{\mathrm{str}}_h:\mathcal E_h\to\{0,1\}
$$

be a structural predicate over effects.

The exact executable pullback is

$$
G_h^{\mathrm{str}}(a)
=
\mathrm{Adm}^{\mathrm{str}}_h(e_h(a)).
$$

A policy or credential gate $G_h^{\mathrm{txn}}$ is a different object. It may equal the pullback, be stricter, or admit actions whose long-horizon effect is structurally destructive.

Let $R_h\subseteq\mathcal A_h$ be the declared reachable action set: the actions that can actually be executed in the audited run class. (Throughout this subsection the subscript $h$ names the audited context and is fixed.) A run has **clean transaction-level records** when every executed action $a$ satisfies $G_h^{\mathrm{txn}}(a)=1$. Call the run class **rich** when every gate-passing action in $R_h$ is executed by at least one run with clean records — any class closed under single-action runs is rich.

**Proposition 6.1 (Transaction-to-structure correspondence).** For a rich run class, clean transaction-level records entail structural admissibility of every executed effect if and only if

$$
G_h^{\mathrm{txn}}(a)\le \mathrm{Adm}^{\mathrm{str}}_h(e_h(a))
\qquad\text{for every }a\in R_h.
$$

Equality on $R_h$ additionally makes the executed gate an exact implementation of the structural pullback on the reachable support.

*Proof.* If the domination holds, every executed action of a clean-record run passes the gate and therefore has a structurally admissible effect; richness is not needed for this direction. If the domination fails at some $a^\star\in R_h$, then $G_h^{\mathrm{txn}}(a^\star)=1$ while $\mathrm{Adm}^{\mathrm{str}}_h(e_h(a^\star))=0$; richness supplies a clean-record run executing $a^\star$, and that run has a structurally inadmissible effect. $\square$

Without richness the converse can fail vacuously: if every run reaching a gate-passing bad action also executes a gate-failing one, no clean run witnesses the defect, and the entailment holds while the domination does not.

One-sided domination on the reachable support is the whole correspondence obligation; agreement with the pullback outside $R_h$ is not required. The problem is not that a Boolean gate is inherently too shallow. A Boolean gate can implement a rich geometry exactly. The defect is a missing or false domination through the effect map and structural kernel.

### 6.3 Reference-monitor sufficiency

Let $E$ be a finite typed event alphabet and let

$$
\mathcal S\subseteq E^\star
$$

be a decidable prefix-closed safety property with $\epsilon\in\mathcal S$.

A **pre-commit monitor** holds the current committed prefix $p$ and, on a proposed event $e$, either commits it or rejects that event and continues; a rejected event leaves $p$ unchanged and the run is not terminated. This is the disable-a-controllable-event semantics of supervisory control, not truncation: rejecting a proposed step suppresses that step, it does not halt the process. This names a class: the decision rule is not yet fixed. The **$\mathcal S$-monitor** is the member that commits $e$ exactly when $pe\in\mathcal S$.

**Theorem 6.2 (Safety enforcement under complete mediation).** If:

1. every committed event is visible to the monitor;
2. every event is committed only through the monitor — no unmediated commit path exists;
3. the monitor evaluates the authoritative prefix;
4. the decision procedure for membership in $\mathcal S$ is correct;
5. $\epsilon\in\mathcal S$, equivalently $\mathcal S$ is non-empty;

then, at every step, the authoritative committed prefix of the mediated system coincides with the prefix held by the $\mathcal S$-monitor and remains in $\mathcal S$.

**Proof.** Hypotheses 1--3 couple the system trace to the monitor state: every system commit is visible to the monitor, no commit can bypass it, and the prefix evaluated by the monitor is the authoritative committed prefix. The base case is hypothesis 5, with both prefixes equal to $\epsilon$. Assume the common current prefix is $p\in\mathcal S$. If the $\mathcal S$-monitor accepts a proposed event $e$, correctness of the decision procedure gives $pe\in\mathcal S$ and complete mediation advances both prefixes to $pe$. If it rejects $e$, complete mediation prevents a system commit and both prefixes remain $p$. Induction proves both coincidence and safety. $\square$

A cognitive agent and model-family heterogeneity are unnecessary for this enforcement result. They may be useful for proposing invariants, interpreting evidence, or auditing a monitor, but they are not premises of the theorem.

The theorem does not guarantee liveness, availability, semantic convergence beyond the predicate, recovery after monitor failure, or safety under incomplete mediation. Prefix-closedness is what makes $\mathcal S$ a safety property in the classical sense of Alpern and Schneider. The induction uses correctness of the decision procedure, $\epsilon\in\mathcal S$, and the exact system-to-monitor coupling supplied by authoritative visibility and complete mediation. Decidability is an implementability condition on the monitor, not a premise of the induction.

**Proposition 6.3 (Maximal permissiveness).** Call a pre-commit monitor sound when every prefix it commits lies in $\mathcal S$. Among sound pre-commit monitors, the $\mathcal S$-monitor is stepwise maximally permissive: at every reachable committed prefix $p\in\mathcal S$ it commits a proposed event $e$ exactly when some sound monitor at $p$ could commit it, namely when $pe\in\mathcal S$.

*Proof.* Soundness forbids committing $e$ at $p$ when $pe\notin\mathcal S$. The $\mathcal S$-monitor commits in every remaining case. $\square$

Safety alone is achievable by the monitor that rejects everything; maximal permissiveness is what makes the construction non-trivial. Because the monitor can veto every event, this is the degenerate all-events-controllable case of the supremal-sublanguage pattern of supervisory control. Whether a committed prefix retains admissible continuations is a liveness question and remains outside the theorem.

### 6.4 Isolation and return channels

Isolation is a channel restriction:

$$
\text{hidden world}\longrightarrow V\longrightarrow \text{verifier}.
$$

It is not literal non-causality. A verifier may return a minimal verdict to an enforcer without exposing the raw provenance or a gradient-bearing boundary to the optimizer.

If detailed findings are used to revise the producer, the result is a new artifact, a new history, and a new audit epoch. Feedback is not forbidden; it changes the object being verified. The safe statement is therefore:

> raw audit information must not silently alter the object inside the same certification claim.

### 6.5 Failure and unknown policies

The fibre trichotomy introduces $?$. An implementation must declare what $?$ does:

- fail closed;
- fail open;
- halt propagation;
- escalate to a privileged audit;
- request a new observation;
- defer until a bounded recovery procedure completes.

The mathematical fibre result does not choose among these policies. Each choice has distinct safety, liveness, and denial-of-service consequences.

### 6.6 Enforcement under hidden admissibility

The $\mathcal S$-monitor of §6.3 presumes one declared safety property. Under the double fibre, the intended property may itself depend on the hidden selector, while the true $\alpha$ stays hidden from the monitor. Making that dependence structural rather than nominal requires one declaration, because selectors are typed on histories (§2.2) and safety properties on event sequences (§6.3); nothing said so far connects $E^\star$ to $\mathcal H_D$.

**Declaration (runs and histories).** Let

$$
\iota:E^\star\longrightarrow\mathcal H_D
$$

be the declared realisation map, sending a run to the history it realises. This subsection declares three things beyond §§2–5: the extension order $\sqsubseteq$ on $\mathcal H_D$ of §2.1; that every $\alpha\in\mathfrak A(D)$ is downward closed in the sense of §2.2; and that $\iota$ is **total**, **computable**, and **order-preserving**,

$$
q\preceq p\ \Longrightarrow\ \iota(q)\sqsubseteq\iota(p),
$$

where $\preceq$ is the prefix order on $E^\star$. Since $\epsilon\preceq p$ for every run, $\iota(\epsilon)$ is $\sqsubseteq$-below every realised history.

Each selector then induces a safety property by pullback,

$$
\mathcal S_\alpha=\{p\in E^\star:\alpha(\iota(p))=1\},
$$

so that $\{\mathcal S_\alpha\}_{\alpha\in\mathfrak A(D)}$ is **determined by** $\mathfrak A(D)$ rather than merely indexed by it. The two conditions Theorem 6.2 needs are now **consequences**, not further declarations.

*Prefix closure.* Let $q\preceq p$ with $p\in\mathcal S_\alpha$. Order-preservation gives $\iota(q)\sqsubseteq\iota(p)$, and downward closure of $\alpha$ turns $\alpha(\iota(p))=1$ into $\alpha(\iota(q))=1$; hence $q\in\mathcal S_\alpha$.

*Initial admissibility.* If $\alpha$ admits any realised history at all, then $\iota(\epsilon)$ lies below it and downward closure gives $\alpha(\iota(\epsilon))=1$, so $\epsilon\in\mathcal S_\alpha$.

*Decidability.* Immediate from computability of $\iota$ and finiteness of $\mathcal H_D$.

These are sufficient conditions, not characterisations: a pullback family can be prefix-closed while some selector fails downward closure, so the converse does not hold and is not claimed. What the declaration buys is that the closure conditions of §6.3 need not be assumed separately for each $\mathcal S_\alpha$ — they follow from the order, the selectors, and $\iota$ together.

For an attained visible value $v=(D,y)$, let

$$
\mathfrak A_v=\{\alpha:\exists h,\ (h,\alpha)\in\mathcal C_D,\ O_D(h)=y\}
$$

be the selectors compatible with $v$. Call a monitor **$V$-confined** when its commit decisions depend only on $v$, the committed prefix, and the proposed event — never on $\alpha$.

Soundness must be stated per world, and it needs one further declaration. Let $\Sigma$ be the declared class of event streams the producer may emit. Call the proposal class **selector-free** when every stream in $\Sigma$ may be emitted in every world of the fibre over $v$, so that the producer's choice carries no information about $\alpha$. Whether $\Sigma$ has this property is part of the declaration, not a consequence of confinement.

Call a monitor **sound in every compatible world** when, for each $\alpha\in\mathfrak A_v$, each stream in $\Sigma$, and each prefix the monitor commits while running in a world with selector $\alpha$, that prefix lies in $\mathcal S_\alpha$. This constrains a monitor only by the property in force in the world it is actually running in; it does not presume the monitor satisfies every member of the family at once.

**Theorem 6.4 (Intersection envelope).** Assume every selector in $\mathfrak A_v$ admits at least one realised history — equivalently $\alpha(\iota(\epsilon))=1$ for each $\alpha\in\mathfrak A_v$, by initial admissibility. Let

$$
\mathcal S_\cap=\bigcap_{\alpha\in\mathfrak A_v}\mathcal S_\alpha.
$$

Then:

1. $\mathcal S_\cap$ is decidable, prefix-closed, and contains $\epsilon$;
2. the $\mathcal S_\cap$-monitor is $V$-confined and sound in every compatible world;
3. under a selector-free proposal class, every $V$-confined monitor that is sound in every compatible world commits only prefixes in $\mathcal S_\cap$, and the $\mathcal S_\cap$-monitor is stepwise maximally permissive at every decision point reached by a monitor in that comparison class on a stream in $\Sigma$.

*Proof.* (1) Each $\mathcal S_\alpha$ contains $\epsilon$ by the admission hypothesis, and a finite intersection of decidable prefix-closed sets each containing $\epsilon$ is decidable, prefix-closed, and contains $\epsilon$. (2) The monitor consults only $v$, the prefix, and the proposed event; every committed prefix lies in $\mathcal S_\cap\subseteq\mathcal S_\alpha$ for each compatible $\alpha$, hence in the property in force in whichever world it runs. (3) Let a $V$-confined monitor commit $p$ while running in a world with selector $\alpha_0\in\mathfrak A_v$, on a stream $\sigma\in\Sigma$. Its decisions read only $v$, the committed prefix, and the proposed event, so the same run on $\sigma$ commits $p$ in every world of the fibre over $v$; a selector-free proposal class makes $\sigma$ available in each of them, so $p$ is committed under every $\alpha\in\mathfrak A_v$. Soundness in each of those worlds gives $p\in\mathcal S_\alpha$ for every compatible $\alpha$, that is $p\in\mathcal S_\cap$. Now consider any decision point $(p,e)$ reached by a monitor in this comparison class on a stream in $\Sigma$. If such a monitor commits $e$, the preceding argument applied to the resulting prefix $pe$ gives $pe\in\mathcal S_\cap$; if $pe\notin\mathcal S_\cap$, no monitor in the class can commit it soundly, while the $\mathcal S_\cap$-monitor commits whenever $pe\in\mathcal S_\cap$. This is the claimed $\Sigma$-relative stepwise maximality. $\square$

Confinement is what carries clause 3: it transports a prefix committed in one world to every other world of the fibre, and the per-world soundness requirements then intersect. Both premises are load-bearing and fail in different ways. Without confinement, claim 3 fails as shown in Remark 6.5. Without a selector-free proposal class it fails for a second and distinct reason: if some streams are unavailable under some compatible selectors, a committed prefix need not be reachable under all of them, and the monitor is bound only by the smaller family
$$
\mathfrak A_{(v,p)}=\{\alpha\in\mathfrak A_v:\ p\text{ is reachable under }\alpha\},
$$
whose intersection $\bigcap_{\alpha\in\mathfrak A_{(v,p)}}\mathcal S_\alpha$ may be strictly larger than $\mathcal S_\cap$. A proposal class coupled to the selector is therefore itself a channel: the committed prefix carries selector information that $v$ does not, and F1 applies at the enforcement layer.

**A worked instance.** Let $E=\{s,a,b\}$, where $s$ is uncontested and $a$, $b$ are each contested by one selector. Let

$$
\mathcal H_D=\{h_\bot,h_a,h_b,h_\top\},
\qquad
h_\bot\sqsubseteq h_a\sqsubseteq h_\top,
\qquad
h_\bot\sqsubseteq h_b\sqsubseteq h_\top,
$$

so a history records which contested events have occurred. Let $\iota(p)$ be $h_\bot$ when $p$ contains neither $a$ nor $b$, $h_a$ when it contains $a$ but not $b$, $h_b$ when it contains $b$ but not $a$, and $h_\top$ when it contains both. A prefix cannot contain a letter its extension lacks, so $\iota$ is order-preserving. Let $\alpha_0$ admit $\{h_\bot,h_a\}$ and $\alpha_1$ admit $\{h_\bot,h_b\}$ — both downward closed — with a constant observation and every pair compatible, so $\mathfrak A_v=\{\alpha_0,\alpha_1\}$.

The pullback then yields, without further declaration,

$$
\mathcal S_{\alpha_0}=\{p:\text{$p$ has no }b\},
\qquad
\mathcal S_{\alpha_1}=\{p:\text{$p$ has no }a\},
\qquad
\mathcal S_\cap=\{s\}^\star,
$$

each prefix-closed and each containing $\epsilon$ by the derivation above. The intersection is not the trivial $\{\epsilon\}$: on the stream $s\,s\,a\,b\,s$ the $\mathcal S_\cap$-monitor commits $sss$, rejecting only the contested events, while the monitor that rejects everything commits $\epsilon$. Both are sound; only the first is permissive, which is the content of Proposition 6.3 made visible.

**Remark 6.5 (Confinement is load-bearing, and the price is monotone).** Claim 3 fails for selector-aware monitors. In the worked instance, a monitor with a channel to the true selector may commit $a$ exactly under $\alpha_0$ and $b$ exactly under $\alpha_1$ — sound in every world, since $a\in\mathcal S_{\alpha_0}$ and $b\in\mathcal S_{\alpha_1}$, while committing outside $\mathcal S_\cap$ in each. The envelope is the price of hiddenness, not of soundness. That price is monotone: if $\mathfrak A_v\subseteq\mathfrak A'_v$, then $\bigcap_{\alpha\in\mathfrak A'_v}\mathcal S_\alpha\subseteq\bigcap_{\alpha\in\mathfrak A_v}\mathcal S_\alpha$ — each additional compatible selector weakly shrinks what a confined monitor may commit, and any refinement of the visible channel that shrinks $\mathfrak A_v$ weakly enlarges it. The fibre trichotomy dualises at the enforcement layer: a prefix in $\mathcal S_\cap$ is admissible under every compatible selector, a prefix outside $\bigcup_{\alpha\in\mathfrak A_v}\mathcal S_\alpha$ under none, and the region between is the enforcement-side $?$.

Enforcement under hidden admissibility therefore pays an exact price: with a selector-free proposal class and no channel to $\alpha$, no committed prefix reached on a stream in $\Sigma$ can lie outside the compatible intersection for a sound confined monitor, and the intersection rule is stepwise maximally permissive on that declared proposal surface. A monitor that, while the selector is hidden, commits prefixes outside $\mathcal S_\cap$ under the banner of enforcing some particular $\mathcal S_{\alpha_0}\supsetneq\mathcal S_\cap$ is in at least one of three positions: it is unsound for another compatible selector; or it is silently using an undeclared selector channel; or the declared proposal class is coupled to the selector, so that the committed prefix is itself such a channel and the operative envelope is the one over $\mathfrak A_{(v,p)}$. The three are not exclusive — a monitor may read the selector and be unsound as well.

**What the envelope is not.** It is tempting to read $\mathcal S_\cap$ as the enforcement-side image of target ambiguity, so that the verifier's mixed fibre becomes the enforcer's intersection. That reading is wrong in both directions, and this paper's own models refute it. The envelope is a function of the compatible selector family $\mathfrak A_v$ — its members and their induced safety properties, not its cardinality alone — whereas target ambiguity $H(Q\mid V)$ measures how a declared target varies across the whole double fibre.

*A mixed fibre need not contract the envelope.* Reuse the worked instance's downward-closed $\alpha_0$, admitting $\{h_\bot,h_a\}$, as the only compatible selector, over runs that realise $h_b$ and $h_\top$ as well. The admissibility verdict $\alpha_0(\iota(\cdot))$ is then mixed across the realised histories — a lineage-only witness in the sense of §3.6. But $\mathfrak A_v=\{\alpha_0\}$, so $\mathcal S_\cap=\mathcal S_{\alpha_0}$ and nothing is given up at all.

*A homogeneous fibre may contract it.* Keep both downward-closed selectors $\alpha_0,\alpha_1$ of the worked instance, but restrict compatibility to the worlds each one admits — $(h_\bot,\alpha_0),(h_a,\alpha_0),(h_\bot,\alpha_1),(h_b,\alpha_1)$. Every compatible world is then admissible, so $H(J_{\mathrm{Adm}}\mid V)=0$ and the verifier's fibre is homogeneous. Yet both selectors occur, so $\mathfrak A_v=\{\alpha_0,\alpha_1\}$ and $\mathcal S_\cap=\{s\}^\star$ is strictly smaller than either $\mathcal S_{\alpha_0}$ or $\mathcal S_{\alpha_1}$, which differ on the realised histories $h_a$ and $h_b$.

Identifying the two would be precisely the conflation F5 names. What survives is exact and weaker: hidden lineage prices verification, hidden admissibility prices enforcement, and the two prices are charged on different quantities. The role of $\iota$ is to make the enforcement price computable from the declared selectors at all — without it, $\{\mathcal S_\alpha\}$ is a family the audit must supply by hand, and the closure conditions of §6.3 must be assumed rather than derived.

---

## §7. Contraction of meaning

### 7.1 A separate dynamic object

Let $\Omega_M$ be a finite declared universe of meanings, interpretations, continuations, or generators. Let

$$
M_t\subseteq\Omega_M
$$

be the set remaining viable at time $t$.

The word meaning is operational here: membership in $M_t$ must be determined by a declared compatibility or viability criterion. The theorem below does not identify semantic meaning with Shannon entropy.

### 7.2 Restriction dynamics

Assume a sequence of declared restrictions $R_t\subseteq\Omega_M$ and the update

$$
M_{t+1}=M_t\cap R_t.
$$

**Theorem 7.1 (Finite monotone contraction).** Under this update:

1. $M_{t+1}\subseteq M_t$ for every $t$;
2. the set can change strictly at most $|M_0|$ times;
3. if non-emptiness is required, it can change strictly at most $|M_0|-1$ times;
4. the sequence eventually stabilises.

**Proof.** Intersection gives nesting. Every strict inclusion of finite sets removes at least one element. There are only $|M_0|$ elements to remove, or $|M_0|-1$ if one must remain. Therefore only finitely many strict changes can occur, after which the nested sequence is constant. $\square$

For $M_{t+1}\neq\varnothing$, define the contraction increment

$$
\kappa_t
=
\log_2\frac{|M_t|}{|M_{t+1}|}
\geq 0.
$$

For $s<t$ with every intermediate set non-empty,

$$
\sum_{k=s}^{t-1}\kappa_k
=
\log_2\frac{|M_s|}{|M_t|}.
$$

If $M_{t+1}=\varnothing$, the logarithmic score is not finite; collapse must be reported separately.

### 7.3 What the theorem does not say

Contraction is not inevitable. If $R_t\supseteq M_t$, then $M_{t+1}=M_t$. A repair, capacity increase, reinterpretation, or expansion operator can also violate the intersection update.

Therefore a claim of unavoidable contraction needs, at minimum:

1. a fixed comparison type $\Omega_M$;
2. a declared update law;
3. monotone restriction or burden-to-viability correspondence;
4. no unmodelled repair or capacity growth;
5. at least one strict restriction if strict contraction is claimed.

A non-zero burden variable alone does not prove that $|M_t|$ decreases.

### 7.4 Epistemic and ontic contraction

A consistent-generator set

$$
\mathrm{Cons}_{t+1}
=
\mathrm{Cons}_t\cap
\{\gamma:\gamma\text{ fits evidence }e_{t+1}\}
$$

may contract because knowledge improves. This is **epistemic contraction**.

A viable-continuation set $M_t$ may contract because possible futures are actually removed. This is **ontic or operational contraction**.

The first does not entail the second. Learning which generator produced a trace can reduce uncertainty while enlarging the set of actions the observer knows to be safe. Those are different objects: the intersection update of §7.2 governs $M_t$ and can only shrink it, whereas knowing an action to be safe is a fact about the observer's information rather than membership in the declared universe $\Omega_M$. Reporting epistemic gain as ontic expansion is exactly the conflation this subsection separates. Conversely, viable futures can disappear while the observer remains uncertain about why.

### 7.5 Relation to the double fibre

For each hidden completion $(D,h,\alpha)$, a declared rule may assign a continuation set

$$
M_t=M_t(D,h,\alpha).
$$

**Corollary 7.2 (Visible identifiability of contraction).** Fix the declared assignment and a contraction statistic $Q_t$ — for instance $Q_t=|M_t|$, or $Q_t=\kappa_t$ on steps with $M_{t+1}\neq\varnothing$. Then $Q_t$ is exactly verifiable from $V$ if and only if $Q_t$ is constant on every double fibre.

*Proof.* Theorem 3.2 applied to the target $Q_t$. $\square$

The condition genuinely fails in small models: in the crossed model of §5.1, declare $M_0=\{m_1,m_2\}$ for every world and the rule $M_1(D,h,\alpha)=M_0$ if $\alpha(h)=1$ and $M_1(D,h,\alpha)=\{m_1\}$ otherwise. Then $\kappa_0=0$ on the accepted worlds and $\kappa_0=1$ on the rejected ones, while all four worlds share one visible value: two hidden completions carry the same artifact and different remaining meanings.

Contraction therefore lives **inside** the hidden completion and can be queried through the factorisation theorem. It is not a third fibre unless a third, independently typed forgetting map is introduced.

---

## §8. Witness, liveness, and weaker property detection

### 8.1 Retained memory and witness factorisation

Let

$$
\mathrm{Ret}:\mathcal H_D\to\mathcal R_D
$$

be a retention map from full history to retained state, and let

$$
W:\mathcal H_D\to\mathcal W
$$

be an identity-relevant witness.

**Proposition 8.1.** There exists $\widetilde W$ with

$$
W=\widetilde W\circ\mathrm{Ret}
$$

if and only if $W$ is constant on every retention fibre.

*Proof.* The factorisation argument of Theorem 3.2 with $\mathrm{Ret}$ in place of $V$: if $W=\widetilde W\circ\mathrm{Ret}$, two histories with equal retained state carry equal witnesses; conversely, fibre constancy makes $\widetilde W(r)$ the common value on $\mathrm{Ret}^{-1}(r)$ well defined. $\square$

Stored records are therefore not automatically identity-preserving. A copy, fork, or replay may retain the same record without selecting one numerical continuation. The witness and the equivalence relation must be declared.

### 8.2 Persistence and admissibility

A transported witness can remain intact while the resulting history is inadmissible under the current selector. Conversely, an admissible transition can lose a chosen witness. These are different target coordinates.

A vector such as

$$
(J_{\mathrm{Adm}},J_W,J_{\mathrm{Live}})
$$

must be audited coordinate by coordinate. Exact recovery of any declared vector requires fibre constancy of every coordinate.

### 8.3 Property detection without reconstruction

Let $P=P(D,H,A)$ be a finite property and let $S^\star=s(V)$ be a declared statistic of the visible channel. Work at fixed $D$, or condition throughout on $D$.

Assume:

$$
I(P;S^\star\mid D)>0
$$

as an explicit detectability premise, and suppose the hidden-pair leakage obeys

$$
I((H,A);V\mid D)\leq\varepsilon.
$$

Then data processing gives

$$
0<I(P;S^\star\mid D)
\leq
I((H,A);V\mid D)
\leq\varepsilon.
$$

This is compatible with positive residual entropy

$$
H(H,A\mid V,D)>0.
$$

Detectability is therefore **compatible** with non-reconstructibility, and the displayed chain bounds it from above rather than establishing it: $I(P;S^\star\mid D)>0$ is an assumed premise, not a conclusion, and what the chain adds is that no more property information can be present than the visible channel leaks about the hidden pair. The model of §5.5 instantiates the regime — there $H(H,A\mid V)=2$ while $I(P;S^\star\mid D)=\tfrac32-\tfrac34\log_2 3>0$ — and no model with a constant observation map can, since a constant $V$ forces $I(P;S^\star\mid D)=0$. Positive property information does not yield an exact target verdict, a pointwise witness for every fibre, or identification of the full architecture.

The leakage bound is less general than it looks. Since $V$ is a deterministic function of $(D,H)$, the quantity $I((H,A);V\mid D)$ equals $H(Y\mid D)$: the ceiling on detectability is the visible channel's own entropy, so a narrow channel bounds every property statistic at once. The detectability premise is in addition conditional on the declared property, statistic, ensemble, and calibration discipline. It is not derived from non-reconstructibility alone.

**Remark 8.2 (Quantitative bridge).** Positive target ambiguity is not only an obstruction to exact verification but a floor on approximate visible verdicts. For a finite target $Q$ with $|\mathcal Q|=n_Q$ and any estimator $\widehat Q=g(V)$, Fano's inequality gives

$$
h_2\big(\Pr[\widehat Q\neq Q]\big)+\Pr[\widehat Q\neq Q]\log_2(n_Q-1)\ \ge\ H(Q\mid V),
$$

so for binary $Q$ the error obeys $h_2(\Pr[\widehat Q\neq Q])\ge H(Q\mid V)$. Fano holds for every estimator without further structure, though its value $H(Q\mid V)$ is itself prior-dependent; for any declared prior the exact optimum is

$$
\Pr[\widehat Q\neq Q]_{\min}
=
1-\sum_{v}\pi(v)\,\max_{u\in\mathcal Q}\pi(u\mid v),
$$

attained by the fibrewise posterior mode. In the crossed model of §5.1 both readings give exactly $\tfrac12$ — no better than ignoring the artifact altogether.

---

## §9. Coordination as an implementation condition

Let $S_k$ be an authoritative committed state at version $k$. Agent $i$ has applied frontier $v_i\leq k$, typed projection $P_i(S_{v_i})$, and operational context $C_i$.

Define version lag

$$
L_i=k-v_i.
$$

A finite lag bound limits one kind of lineage divergence: the number of authoritative commits omitted from the agent's local history. It does not by itself bound semantic or behavioural divergence. That requires:

1. a projection-conformance condition;
2. a declared observable metric;
3. a stability modulus linking context error to verdict or action error;
4. a recovery protocol for cold start and partial propagation.

Two agents may hold byte-identical logs and still apply different interpreters or selector versions. Conversely, agents may hold different typed projections yet remain behaviourally equivalent on a sealed probe class.

Within the present framework:

- missed or reordered updates are hidden lineage;
- different local predicate versions are hidden admissibility;
- the coordination protocol controls how large those fibres can become in operation;
- a reference monitor that takes no part in the agents' semantic protocol can enforce a declared safety invariant without claiming semantic identity among them; it is not thereby a passive observer, since Theorem 6.2 requires it to mediate the commit path in full.

Propagation halt is an authority, not a proof. It is useful only if the halt surface is completely mediated, scoped, recoverable, and paired with an explicit fail policy.

---

## §10. Sealed finite reference audit

The minimal reference audit is fully enumerable.

### 10.1 Declaration

The audit runs the models of §5 and the enforcement layer of §§6–7. The core information-theoretic declaration is:

- one skeleton $D$;
- histories $\{h_0,h_1\}$;
- selectors $\{\alpha_0,\alpha_1\}$;
- a constant observation $O_D(h_0)=O_D(h_1)=y$;
- one of the two compatibility relations of §5.1 or §5.2;
- a full-support prior, uniform or the correlated prior of §5.4;
- targets $J_{\mathrm{Adm}}$, $H$, $A$, and any chosen persistence target.

Two further declarations, needed by outputs that the constant-observation core cannot express, are run alongside it:

- the **partial-visibility** declaration of §5.5 — four histories $\{g_0,\ldots,g_3\}$, the two-valued observation $O_D$, the property $P$, the selectors $\alpha_0,\alpha_1$ admitting $\{g_0,g_2\}$ and $\{g_1,g_3\}$, and $S^\star=V$ — which is the only model instantiating the detectability regime of §8.3 and the only non-degenerate witness for Proposition 3.5;
- the **enforcement** declaration of §6.6 — the event alphabet $E=\{s,a,b\}$, the ordered histories $h_\bot\sqsubseteq h_a,h_b\sqsubseteq h_\top$, the realisation map $\iota$, downward-closed selectors, and the induced family $\{\mathcal S_\alpha\}$ — together with the contraction universe $\Omega_M$ and restriction sequence $\{R_t\}$ of §7.2.

These are distinct sealed declarations; a companion must keep them apart and never carry a label from one into another.

### 10.2 Required outputs

A companion verifier should:

1. enumerate $\Theta$;
2. group worlds by $V$;
3. list each double fibre;
4. test target constancy on every fibre;
5. emit an explicit target-fibre witness when constancy fails;
6. compute $H(H,A\mid V)$;
7. compute $H(H\mid V)$, $H(A\mid V)$, and $I(H;A\mid V)$;
8. verify the chain-rule identity exactly up to a declared numerical tolerance;
9. compute $H(Q\mid V)$;
10. verify the maximal three-valued classifier;
11. rerun after replacing the crossed compatibility relation by the diagonal relation;
12. verify the fibrewise agreement test of Corollary 3.6 on both compatibility relations;
13. construct the least sufficient refinement of Theorem 3.8 on the partial-visibility model and verify both halves of its universal property by enumerating every partition of the eight-world class, confirming the quantifier is non-vacuous;
14. verify the equality criterion of Proposition 4.8 in both directions;
15. verify the product regime of Lemma 4.7 and the correlated-prior model of §5.4, including the closed form $I(H;A\mid V)=1-h_2(2\varepsilon)$;
16. run the $\mathcal S$-monitor of Theorem 6.2, the maximal-permissiveness comparison of Proposition 6.3, the transaction-to-structure domination of Proposition 6.1 with a positive and a negative instance, the contraction ledger of Theorem 7.1 with the Corollary 7.2 witness, and the Fano floor of Remark 8.2;
17. verify the lattice form of Corollary 3.9, the reconstruction-top equivalence of §4.4, the information budget of Proposition 4.9, the confined non-absorption inequality of Theorem 4.6, the exact fibrewise posterior-mode floor of Remark 8.2, and the target-level data-processing bound of Proposition 4.3;
18. on the partial-visibility declaration of §5.5: confirm $H(H,A\mid V)=2$, $H(P\mid V)=\tfrac12$, and $I(P;S^\star\mid D)=\tfrac32-\tfrac34\log_2 3$; check that $P$ does not factor through $V$; verify the Proposition 3.5 witness in which the conjunction factors while neither conjunct does; and confirm the §5.5 selector declaration admits one history per visible fibre;
19. on the enforcement declaration of §6.6: derive $\{\mathcal S_\alpha\}$ from $\iota$ and the downward-closed selectors, confirm each is prefix-closed and contains $\epsilon$, run the $\mathcal S_\cap$-monitor to a non-trivial committed prefix, exhibit the selector-aware escape of Remark 6.5, and verify the monotone envelope; then confirm both coupled witnesses that the envelope tracks the compatible selector family and not target ambiguity — a single-selector model whose mixed verdict leaves $\mathcal S_\cap=\mathcal S_{\alpha_0}$ uncontracted, and a two-selector model whose homogeneous verdict still contracts $\mathcal S_\cap$ strictly below each member.

### 10.3 Expected checks

For the crossed model:

$$
\overline{\mathfrak B}_2=2,\qquad
H(J_{\mathrm{Adm}}\mid V)=1.
$$

For the diagonal model:

$$
\overline{\mathfrak B}_2=1,\qquad
H(J_{\mathrm{Adm}}\mid V)=0,
$$

and the dependence correction is one bit.

For the correlated-prior model of §5.4 at $\varepsilon=\tfrac18$:

$$
\overline{\mathfrak B}_2=1+h_2\big(\tfrac14\big)=3-\tfrac34\log_2 3,
\qquad
I(H;A\mid V)=\tfrac34\log_2 3-1,
\qquad
H(J_{\mathrm{Adm}}\mid V)=2-\tfrac34\log_2 3.
$$

The code should use only the sealed declaration. It must not infer hidden labels from filenames, enumeration order, or metadata outside $V$.

### 10.4 Extension tests

The executable companion of §10.5 provides finite executable witnesses and checks for items 1–19: the four information-theoretic models, a coarse target that factors through the two-valued observation of §5.5, the finite contraction sequence with telescoping $\kappa_t$, and the enforcement layer. A later harness can still add:

- a side-channel variable and demonstrate the change from $V$ to $V'=(V,X)$;
- a propagation trace with bounded version lag but divergent local selector copies.

These are separate tests. Passing one must not be reported as passing the others. The list above is a coverage map, not a claim that every clause has an independent failure marker. Some identities are structural consequences of the declared constructors, and some named checks are deliberately shadowed by an upstream biting invariant; the audit labels those cases explicitly.

### 10.5 Executable companion

The standard-library bundle is

```text
harness/double_fibre_audit.py
harness/check_bundle.py
harness/double_fibre_certificate.json
harness/README.md
```

The audit executes finite witnesses and checks for the sealed declarations of §10.1, the required-output map of §10.2, the expected values of §10.3, and the covered extension tests, in ordinary and optimised Python, without bare `assert` statements, and emits a deterministic certificate. Its named checks include independently biting teeth and explicitly classified derived or shadowed coverage markers; the latter do not count as independent failure modes. The bundle gate checks inventory, hygiene, certificate equality, its own advertised counts, and scratch mutations that must be rejected by named markers.

Expected audit output:

```text
double fibre audit passed: 64 checks
```

Expected bundle output:

```text
bundle checks passed: 13 gates, 42 mutations
```

The executable audit establishes only the declared finite models. It does not certify any real verification pipeline, monitor deployment, or coordination system.

---

## §11. Falsification surface

The framework is invalidated or its conclusion narrowed when any of the following occurs.

**F1 — undeclared side channel.** The verifier receives information not included in $V$. The relevant fibre and conditional entropy must be recomputed for the enlarged channel.

**F2 — post-hoc comparison class.** Histories, selectors, compatibility, prior, or target are changed after the verdict is known.

**F3 — type mismatch.** Compared selectors do not act on the same declared history type, or compared histories do not belong to the same visible skeleton class.

**F4 — unsupported entropy claim.** A pointwise conclusion is inferred from an average entropy bound without a target-fibre witness or pointwise premise.

**F5 — hidden-pair/target conflation.** Positive $H(H,A\mid V)$ is reported as positive $H(Q\mid V)$ without checking target constancy.

**F6 — product assumption.** The double fibre is counted as $\mathcal F_O\times\mathfrak A(D)$ without verifying compatibility.

**F7 — inevitable contraction.** Nested contraction is claimed without a fixed universe, restriction update, no-repair condition, and strictness witness.

**F8 — enforcement by observation.** A detector is said to enforce a property without complete mediation and pre-commit authority.

**F9 — semantic overreach.** A metadata monitor is said to certify semantic convergence beyond its declared predicate or probe contract.

**F10 — agent necessity.** A cognitive or heterogeneous agent is claimed necessary for enforcing a decidable prefix-closed safety invariant despite an available deterministic reference-monitor construction.

**F11 — transaction/structure collapse.** A transaction gate is treated as a structural viability predicate without an effect map and correspondence proof.

**F12 — property-detection overclaim.** Non-zero mutual information about a property is treated as full reconstruction, exact classification, or causal identification.

**F13 — same-cycle feedback.** Raw audit findings modify the producer while the original certification claim is kept unchanged. The revised object requires a new audit epoch.

**F14 — envelope violation.** A monitor **claimed** to be $V$-confined and sound in every compatible world commits prefixes outside the intersection $\mathcal S_\cap$ of Theorem 6.4 while the admissibility selector remains hidden. Then at least one of three holds: the soundness claim fails for some compatible selector; or the confinement claim fails, an undeclared selector channel being present — Remark 6.5 shows that a genuine selector channel legitimately escapes the envelope; or the declared proposal class is not selector-free, so the committed prefix carries selector information and the operative envelope is the one over $\mathfrak A_{(v,p)}$. The three are not exclusive. F1 applies to the enforcement layer in the second and third cases. Confinement must be stated as a claim under test rather than as a hypothesis: a monitor assumed $V$-confined cannot, by definition, be using a selector channel, and the second case would be unreachable.

---

## §12. Open problems

1. Extend the finite theory to standard Borel spaces with regular conditional distributions and measurable selector families.
2. Extend the least-sufficient-refinement theorem (Theorem 3.8) beyond the finite case, and characterise when the abstract refinement $V_Q$ is realisable by a physically implementable channel rather than a partition on paper.
3. Separate information-theoretic binding from computational hardness and query-limited boundary reconstruction.
4. Define sequential double binding under adaptive observations and changing selector families $\mathfrak A_t(D)$.
5. Derive composition laws for coupled double fibres without assuming product compatibility.
6. Relate irreversible burden and capacity to continuation-set contraction under explicit repair and capacity-growth models.
7. Define intervention protocols that distinguish ranking, downstream veto, and generative-support exclusion.
8. Give a refinement theorem from abstract structural admissibility to an executable reference monitor.
9. Add liveness and recovery guarantees without weakening complete mediation.
10. Determine when bounded propagation lag plus projection conformance yields a quantitative bound on observable verdict divergence.
11. Formalise epoch semantics for audit feedback, selector revision, and re-certification.
12. Extend the sealed reference audit — now executable in the companion harness of §10.5 — with the side-channel and propagation-lag models of §10.4.

---

## §13. Relation to the surrounding corpus

This paper composes, but does not collapse, several earlier lines.

- *Domenoid of Admissibility* supplies the non-trivial fibre of admissibility structures over one dynamic skeleton.
- *The Physics of Abstraction* supplies histories, seam-relative persistence, observation fibres, target factorisation, and lineage binding.
- *Severance Defect and the Binding Functional* supplies the distinction between functional severance and reconstructive binding, together with the confined-access non-absorption pattern.
- *Identity Does Not Drift* supplies the separation between budget wear and witness transport.
- *Identifiability Bridge* supplies the conditional distinction between property detection and full reconstruction.
- *IIC v2.1* supplies a separate liveness coordinate.
- *Subtle Substitution* motivates the temporal contraction question.
- *Verification Is Not Causal* motivates channel isolation, corrected here to a precise confined-access statement.
- *Transaction-Level Admissibility Stops Bad Actions. Structural Admissibility Stops Good-Looking Systems From Dying Slowly.* supplies the action/effect pullback distinction.
- *Continuity-Bounded Coordination: Why Multi-Agent Systems Still Drift* supplies the propagation and cold-start implementation problem.
- *The Structural Navigation Agent: Enforcement Architecture and Structural Analysis for Multi-Agent Coordination* supplies the separation between detection and transition authority, corrected here to a deterministic reference-monitor core.
- *Will as a Prior Constraint: Why the Prefrontal Cortex Exists at All* supplies the motivation for constraining before a transition rather than correcting after it, which is the pre-commit discipline of §6.3. Its clinical case — consequences understood while the transition is no longer withheld — is an instance of detection without commit authority, the pattern F8 names. Its distinction between holding an impulse and extinguishing it corresponds, at the formal layer, to the gap between the $\mathcal S$-monitor and the monitor that rejects everything: both are sound, and only the first leaves anything admissible.

The double fibre is the epistemic skeleton connecting these works. It is not a universal decomposition of engineered vitality. Directedness, phase, burden, memory, liveness, returnability, and coordination enter only through typed targets, hidden histories, selector families, or additional dynamics. They should not be promoted to new fibres without new forgetting maps.

---

## Conclusion

Verification can fail in two structurally different ways before any algorithmic weakness appears.

The artifact may forget how it was produced. The skeleton may forget the rule under which that production should be judged. Their compatible joint inverse image is the double fibre.

A visible exact verdict exists precisely when the target is constant on that fibre. A single same-visible/different-target pair refutes exact verification. Conditional entropy measures how much of the hidden pair remains, but hidden-pair ambiguity must not be confused with ambiguity of the selected target. Post-processing cannot repair target ambiguity under confined access, while weaker property detection can remain possible under separate premises.

Meaning contraction is not smuggled into this theorem. It follows only from a declared restriction dynamics and can be absent, repaired, or reversed outside that class.

Finally, observation is not enforcement. A deterministic reference monitor can enforce a decidable prefix-closed safety property under complete mediation, while cognitive interpretation, semantic auditing, revision, liveness, and recovery remain separate obligations.

The resulting architecture is deliberately conservative:

$$
\text{declare the hidden completion}
\;\to\;
\text{declare the visible channel}
\;\to\;
\text{inspect the double fibres}
\;\to\;
\text{test the target}
\;\to\;
\text{separate verification from enforcement}.
$$

Anything stronger requires another premise, another witness, or another theorem.

---

## References

### Corpus

Barziankou, M. (2026). *Navigational Cybernetics 2.5 — Axiomatic Core, Version 2.1.* The Urgrund Laboratory, PETRONUS. DOI: [10.17605/OSF.IO/NHTC5](https://doi.org/10.17605/OSF.IO/NHTC5).

Barziankou, M. (2026). *Severance Defect and the Binding Functional: Observation-Relative Non-Reconstructibility and the Impossibility of Uniform Exact Absorption under Confined Markov Access.* Publication pair DOI: [10.17605/OSF.IO/5VJMR](https://doi.org/10.17605/OSF.IO/5VJMR).

Barziankou, M. (2026). *Operator over Dynamics — A Traceable Structural Program (2025–2026) — and Its Formal Core — the Domenoid of Admissibility.* DOI: [10.17605/OSF.IO/3ESN4](https://doi.org/10.17605/OSF.IO/3ESN4).

Barziankou, M. (2026). *Identifiability Bridge — Conditional Admissibility Theorems for Property Detection under Non-Reconstructibility within Navigational Cybernetics 2.5.* DOI: [10.17605/OSF.IO/3F6UJ](https://doi.org/10.17605/OSF.IO/3F6UJ).

Barziankou, M. (2026). *IIC v2.1 — A Class-Relative Structural Law of Adaptive Behaviour as a Conditional Theorem over Navigational Cybernetics 2.5.* DOI: [10.17605/OSF.IO/NYT45](https://doi.org/10.17605/OSF.IO/NYT45).

Barziankou, M. (2026). *ONTOΣ XIV — Nested Substrates and the Frame-Relative Derivative*, with *Cross-Layer Forgetful Separation: A Categorical Foundation.* Bundle DOI: [10.17605/OSF.IO/KAGMH](https://doi.org/10.17605/OSF.IO/KAGMH).

Barziankou, M. (2026). *ONTOΣ XV — Spin-Channel and Nestability*, with its formal companion. Bundle DOI: [10.17605/OSF.IO/EAUD5](https://doi.org/10.17605/OSF.IO/EAUD5).

Barziankou, M. (2026). *The Physics of Abstraction: Identity at the Seam.* DOI: [10.17605/OSF.IO/QJ5BR](https://doi.org/10.17605/OSF.IO/QJ5BR).

Barziankou, M. (2026). *Identity Does Not Drift: Channel Switching, the Two Ledgers, and the Parallel Tunnel.* DOI: [10.17605/OSF.IO/4NMTW](https://doi.org/10.17605/OSF.IO/4NMTW).

Barziankou, M. (2026). *Will as a Prior Constraint: Why the Prefrontal Cortex Exists at All.* DOI: [10.6084/m9.figshare.31288699](https://doi.org/10.6084/m9.figshare.31288699).

Barziankou, M. (2025–2026). *Verification Is Not Causal* · *Subtle Substitution* · *Transaction-Level Admissibility Stops Bad Actions. Structural Admissibility Stops Good-Looking Systems From Dying Slowly.* · *Continuity-Bounded Coordination: Why Multi-Agent Systems Still Drift* · *The Structural Navigation Agent.* Local corpus editions; cited in §13 for architectural lineage.

### General

Alpern, B., and Schneider, F. B. (1985). *Defining Liveness.* Information Processing Letters 21(4), 181–185. (Safety/liveness boundary used in §6.3.)

Anderson, J. P. (1972). *Computer Security Technology Planning Study.* ESD-TR-73-51, U.S. Air Force Electronic Systems Division. (The reference-monitor concept behind Theorem 6.2.)

Cover, T. M., and Thomas, J. A. (2006). *Elements of Information Theory*, 2nd ed. Wiley. (Conditional entropy, chain rule, data-processing inequality, Fano's inequality — §§3, 4, 8.)

Ramadge, P. J., and Wonham, W. M. (1987). *Supervisory Control of a Class of Discrete Event Processes.* SIAM Journal on Control and Optimization 25(1), 206–230. (The maximal-permissiveness pattern of Proposition 6.3.)

Schneider, F. B. (2000). *Enforceable Security Policies.* ACM Transactions on Information and System Security 3(1), 30–50. (Execution-monitoring enforceability of prefix-closed safety — §6.3.)
