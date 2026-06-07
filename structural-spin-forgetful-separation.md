# Structural Spin as a Forgetful Separation over Dissipative Dynamics

## ...with a Cohomological Obstruction to Identity Transfer

*The continuous instance of the forgetful-separation pattern, whose discrete instance is admissibility; companion to "Domenoid of Admissibility" (DOI 10.17605/OSF.IO/3ESN4). Substrate: NC2.5 v2.1 (DOI 10.17605/OSF.IO/NHTC5).*

**Author:** Maksim Barziankou (MxBv)
**Date:** June 2026
**Affiliation:** The Urgrund Laboratory, Poznan
**DOI:** 10.17605/OSF.IO/94GWQ
**License:** CC BY-NC-ND 4.0

---

## Abstract

We isolate a single structural pattern: a forgetful map from *(dynamics $+$ an extra structural layer)* to the bare dynamics that is faithful but not full, so that the layer is not recoverable from the dynamical skeleton. Two instances are placed side by side: *admissibility* over a transition skeleton (discrete), and the non-gradient ("spin") component $S$ of a flow $\dot x=-\nabla V+S$ over its gradient skeleton (continuous). For the spin instance: (i) the fibre over a fixed gradient skeleton is non-trivial whenever the manifold carries one nonzero divergence-free field pointwise orthogonal to $\nabla V$ that is not a global gradient, and then contains a whole punctured line of spins; (ii) with split-preserving (positive-semiconjugacy) morphisms the forgetful functor $U_{\mathrm{sp}}\colon\mathsf{SpinFlow}\to\mathsf{GradFlow}$ is faithful but not full; (iii) a morphism that transfers a viability kernel need not control $S$, so that *accurate identity transfer requires viability transfer together with survival of the spin witness* — a non-vanishing de Rham period of a closed component of $S^\flat$ — which is strictly stronger than viability transfer alone; the two-layer certificate detects *failure* of identity transfer and is necessary, not in general sufficient; (iv) the witness is a de Rham class, hence *comparable* across the discrete/continuous divide via any $H_1$-isomorphism, and transferred only when the witness classes correspond. The mathematics is classical (Hodge--de Rham, elementary category theory); the contribution is the identification, the faithful-not-full theorem, the certificate, the constructive defect, the homological bridge, the operational-spin obstruction, the necessity-and-blindness scope of the topological witness, and the finite graph-Hodge instrument.

On the canonical domain we make the identity defect constructive, with a proportionality criterion for witness-exactness, and we show the naive support-subspace (viability-shadow) repair does not transport to the witness, a genuine witness-repair remaining open; and that the four demands — divergence-free, operational-spin-free, orthogonal to $\nabla V$, and nonzero witness $c$ — are jointly satisfiable, for $M$ compact and boundaryless, exactly when the harmonic representative of $c$ is pointwise orthogonal to $\nabla V$, a class-dependent obstruction. The non-gradient structure has two channels — a topological de Rham period (the identity witness) and a local vorticity $2$-form — so that recurrence on a space with trivial $H^1$, were it to occur, is seen only by the latter; and the two instances are meant for *joint* use, the admissibility companion certifying survival and the spin layer certifying liveness — so that neither alone flags the survives-yet-dead configuration exhibited in the worked example. Witness preservation is moreover *sufficient*, on the canonical domain, for forward transfer of the topological identity, not only necessary; the topological witness detects only homologically non-trivial recurrence (necessary, not sufficient, for a fixed spin) and is blind on $H^1=0$ (axial rotation on $S^2$); and a finite graph-Hodge instrument computes the witness and its collapse on raw incidence data. A field-level repair and a high-dimensional operationalization remain open.

## Introduction {#sec:intro}

Many dynamical settings carry, over and above their state dynamics, a *structural layer*: a rule, an admissibility predicate, or a non-conservative component that is independent data and is not determined by the bare dynamics. The organizing question is uniform: *which transfers of the layer between two systems are licensed, and which are not, by similarity of the underlying dynamics alone?* In each instance the answer is governed by a forgetful map from the structured objects to the bare ones that is faithful but *not full*, so that a morphism of skeletons need not lift to one respecting the layer.

The discrete instance is admissibility. Fixing a transition skeleton $\mathsf D$ (states, trajectories, and the algebra of shifts, concatenations, and windows), an admissibility predicate $\mathrm{Adm}\subseteq\mathrm{Traj}_{\mathsf D}$ selects which trajectories count; the forgetful functor $U\colon\mathsf{AdmDyn}\to\mathsf{Dyn}$, $(\mathsf D,\mathrm{Adm})\mapsto\mathsf D$, is faithful but not full, and its fibre $U^{-1}(\mathsf D)$ is a non-trivial complete lattice. A companion development of this instance, including a transfer/repair calculus, is assumed as background [admissibility].

This note develops the continuous instance. The structural layer is the non-gradient component $S$ of a structural flow $\dot x=-\nabla V+S$ on a Riemannian manifold; the bare dynamics is the gradient (dissipative) skeleton $-\nabla V$. We make precise the sense in which $S$ is a layer the skeleton does not determine, prove the forgetful functor is faithful but not full, and exploit the pairing of the two instances: the admissibility layer transfers a *viability kernel*, while the spin layer carries *identity*. Transferring identity therefore requires more than transferring viability, and the gap is detected by a homological certificate. Our constructive results hold on a *canonical domain* that splits in two — $M$ compact without boundary, or $\omega_S$ globally closed; the worked example ($S^1\times\mathbb R$) realizes the second branch. The technical core is the operational-spin obstruction (Proposition §prop:opspin-obstruction, Corollary §cor:WV, Proposition §prop:WV-generic), holding on the compact branch (where the harmonic representative exists); the surrounding Hodge--de Rham and categorical material is classical.

Throughout, the metric $g$ is fixed and all metric-dependent objects ($S^\flat$, divergence, the gradient/spin split) are relative to it. The decomposition $\dot x=-\nabla V+S$ with $S$ satisfying

- **(S1)** $\nabla\!\cdot\!S=0$ (divergence-free),
- **(S2)** $\langle S,\nabla V\rangle=0$ pointwise,
- **(S3)** $S$ admits no global scalar potential ($S\neq\nabla W$),

is the object of study; (S1)--(S3) are the conditions under which the structural-spin theory of [nc25] excludes a global gradient representation.

**Definition (Non-stagnant recurrent identity and its witness)** {#def:identity}

A *non-stagnant recurrent identity* is a non-constant recurrent orbit of the flow: a non-constant orbit returning to every neighbourhood of one of its points at arbitrarily late times. Its *identity witness* on a recurrence loop $\gamma$ — the *topological channel* of the spin (Remark §rem:two-channels) — is the period $\oint_\gamma\eta_S$ of a *closed* component $\eta_S$ of $\omega_S:=S^\flat$, equivalently the pairing of the de Rham class $[\eta_S]\in H^1_\mathrm{dR}(M)$ with $[\gamma]\in H_1(M)$ (an integral cycle class, paired in $H_1(M;\mathbb R)$). Here $\gamma$ is closed: a periodic orbit, or a recurrence segment closed by a chosen short return arc — on which $[\gamma]$ may depend; the canonical loop-free formulation for a general (aperiodic) recurrent orbit is the Schwartzman asymptotic cycle (Remark §rem:schwartzman), to which the periodic $[\gamma]$ specializes. The richer notion of identity under a bounded internal budget developed in [nc25] is not needed below: we use only the elementary necessity of Proposition §prop:identity.

**Proposition (Spin is necessary for a recurrent identity)** {#prop:identity}

For any smooth $V$, the value $V$ is strictly decreasing along every non-constant orbit of the pure gradient skeleton $\dot x=-\nabla V$; hence the skeleton has no non-constant recurrent orbit (orbits assumed forward-complete on the recurrence in question), and a non-stagnant recurrent identity requires a non-gradient component $S\not\equiv0$.

*Proof.* At a critical point ($\nabla V=0$) the constant orbit is the unique solution, so a non-constant orbit meets no critical point; there $\tfrac{d}{dt}V=\langle\nabla V,\dot x\rangle=-\|\nabla V\|^2<0$, so $V$ is strictly decreasing along it. A recurrent point $x$ has return times $t_n\to\infty$ with $x(t_n)\to x$ (the orbit being forward-defined there), whence $V(x(t_n))\to V(x)$; but $V(x(t_n))$ is strictly decreasing and bounded above by $V(x(t_1))<V(x)$, so it cannot converge to $V(x)$, the required contradiction. Thus the gradient skeleton has no non-constant recurrent orbit, and any non-stagnant recurrent identity forces $S\not\equiv0$. $\qquad\blacksquare$

**Remark (Recurrence lives on the critical set)** {#rem:critset}

Under (S2) the same computation gives $\tfrac{d}{dt}V=-\|\nabla V\|^2$ along the *full* flow $\dot x=-\nabla V+S$ (since $\langle S,\nabla V\rangle=0$). Hence any recurrent orbit of the full system — under the same forward-completeness proviso as Proposition §prop:identity — has $V$ constant, so it lies in the critical set $\{\nabla V=0\}$, where $-\nabla V=0$ and the motion is pure spin $\dot x=S$. The non-stagnant identity is therefore carried entirely by $S$ on $\{\nabla V=0\}$ — in Example §ex:worked the invariant circle $\{y=0\}$.

**Remark (Two channels of the non-gradient structure)** {#rem:two-channels}

The de Rham period $[\eta_S]$ is one of two channels of the non-gradient structure. Write $\Sigma(S):=\big([\eta_S]\in H^1_\mathrm{dR}(M),\ d\omega_S\in\Omega^2(M)\big)$: the *topological circulation* channel $[\eta_S]$ and the *local vorticity* channel $d\omega_S=2\times(\text{operational spin})$ (§sec:operational). The first is constrained by topology — if $H^1_\mathrm{dR}(M)=0$ then $[\eta_S]=0$ for every $S$, so on $\mathbb R^2$ it is vacuous — while $d\omega_S$ is a (globally exact) $2$-form unconstrained by topology and may be nonzero on $\mathbb R^2$. Both extremes occur for the spin field itself: plane rotation $S=(-y,x)$ on $\mathbb R^2$ (with $V=\tfrac12(x^2+y^2)$) has $[\eta_S]=0$ but $d\omega_S=2\,dx\wedge dy\neq0$ (*local-only*), while $S=\partial_\theta$ on $S^1\times\mathbb R$ (Example §ex:worked) has $\omega_S$ closed, $d\omega_S=0$, and period $2\pi$ (*topological-active*). Accordingly the necessity of Proposition §prop:identity is only that $S\not\equiv0$: the de Rham period is one detectable channel of that non-gradient structure, not a complete characterization. The cohomological certificate of §sec:certificate concerns the topological channel; the co-exact part is read locally by $d\omega_S$.

**What this paper does and does not introduce.** We introduce no new Hodge decomposition and no new theory of vorticity. The claim is structural and categorical: the spin component is a layer over the gradient skeleton that is *not recoverable* from the skeleton, exactly as admissibility is a non-recoverable layer over a transition skeleton. The supporting mathematics — the Hodge--de Rham decomposition [warner, morita], singular/de Rham (co)homology [hatcher, bott], elementary category theory [maclane], and the vorticity (spin) tensor of continuum mechanics [truesdell, batchelor] — is classical throughout.

## The spin fibre over a gradient skeleton {#sec:fibre}

**Definition (Forgetful projection)** {#def:Usp}

On objects $(M,g,F=-\nabla V+S)$ define $U_{\mathrm{sp}}\colon(M,g,F)\mapsto(M,g,-\nabla V)$, discarding the non-gradient component and retaining the gradient skeleton. The fibre over a fixed skeleton is $U_{\mathrm{sp}}^{-1}(-\nabla V)=\{\,S:\text{(S1)}\wedge\text{(S2)}\wedge\text{(S3)}\,\}$; the category $\mathsf{SpinFlow}$ of §sec:functor additionally admits the trivial object $S=0$ (Definition §def:cats).

**Theorem (The skeleton does not determine the spin)** {#thm:fibre}

(a) *(Compact case.)* Let $M$ be compact, oriented, without boundary. For $S$ satisfying (S1), the $1$-form $\omega_S:=S^\flat$ is co-closed and its Hodge decomposition has no exact part, $\omega_S=\delta\beta\oplus h$ ($\delta\beta$ co-exact, $h$ harmonic). Any nonzero such $S$ is not a gradient (a co-closed exact $1$-form on a closed manifold vanishes), so (S3) is automatic for $S\neq0$; on such closed $M$, (S3) is thus a corollary of Hodge theory.

(b) *(Existence and a punctured line; any $M$.)* On any $(M,g)$ the fibre is non-empty as soon as $M$ carries one nonzero divergence-free field pointwise orthogonal to $\nabla V$ that is not a global gradient (i.e. satisfying (S3)). Moreover, if one nonzero $S$ satisfies (S1)--(S3) then so does $\lambda S$ for every $\lambda\in\mathbb R^\times$, so the fibre contains the punctured line $\{\lambda S\}$ and the skeleton fails to determine the spin even up to magnitude. (S2)-compatibility is *not* automatic from Hodge theory: a generic $\delta\beta\oplus h$ need not be pointwise orthogonal to $\nabla V$. A concrete witness is Example §ex:worked ($M=S^1\times\mathbb R$, $S=\partial_\theta$, with (S2) checked directly), and Remark §rem:family gives a family of such witnesses; the general characterization of manifolds carrying an (S2)-compatible $S\neq0$ is open.

Consequently the gradient skeleton $-\nabla V$ does not determine $S$.

*Proof.* (a) (S1) is $\delta\omega_S=0$, so $\omega_S$ is co-closed; writing $\omega_S=d\alpha+\delta\beta+h$ gives $0=\delta\omega_S=\delta d\alpha$, whence $\|d\alpha\|^2=\langle\alpha,\delta d\alpha\rangle=0$ on a closed manifold and $d\alpha=0$. A nonzero exact $\omega_S$ would be co-closed and exact, hence zero, a contradiction. (b) the existence claim is conditional, with Example §ex:worked exhibiting the hypothesis as non-vacuous; linearity in $S$ of (S1)--(S2) and homogeneity of (S3) (if $\lambda S=\nabla W$ then $S=\nabla(W/\lambda)$, contradicting (S3) for $\lambda\neq0$) give the punctured line; (S2)-compatibility of a generic Hodge component is not asserted. $\square$

**Remark (Each diagnostic reads one Hodge summand; compact case)** {#rem:hodge-tie}

On $M$ compact, oriented, boundaryless, part (a) gives $\omega_S=\delta\beta\oplus h$ with $\delta\beta$ co-exact and $h$ harmonic (no exact part, by (S1)). The two channels $\Sigma(S)=([\eta_S],d\omega_S)$ of Remark §rem:two-channels then read the two summands: $[\eta_S]=[h]$ is the class of the harmonic summand ($\eta_S=h$, the harmonic projection of $\omega_S=\delta\beta\oplus h$ being $h$; the harmonic representative of a de~Rham class is unique, so this choice of $\eta_S$ is canonical), while $d\omega_S=d(\delta\beta)$ is determined by the co-exact summand (since $dh=0$). Thus the topological and operational diagnostics are functions of complementary Hodge components of the single object $\omega_S$ — note $\omega_S$ itself is generally non-closed here, so it is $h$, not $\omega_S$, that carries the de~Rham class, and the two diagnostics do not reconstruct $\omega_S$ as a $1$-form. This is expository — a reading of part (a) and Remark §rem:two-channels, not a new theorem — and is confined to the compact branch: on the globally-closed branch (Example §ex:worked) $d\omega_S=0$ identically and the Hodge projection is unavailable, so the two-component picture degenerates to one.

**Remark (A family of witnesses)** {#rem:family}

If $M=N\times\mathbb R$ carries the product metric $g_N\oplus dy^2$, $V=V(y)$ ($y$ the $\mathbb R$-coordinate), and $X$ is a nonzero divergence-free field on $(N,g_N)$, viewed as tangent to the $N$ factor, then $S=X$ satisfies (S1)--(S2), with (S3) holding whenever $X$ is not a gradient on $N$. This is a family of (S2)-compatible spins; Example §ex:worked is the case $N=S^1$, $X=\partial_\theta$.

**Remark (The fibre as stream-function structure)** {#rem:streamfn}

Conditions (S1)--(S2) say exactly that $S$ is divergence-free and tangent to the level sets $\{V=\mathrm{const}\}$: via the volume form $\mu$, $\nabla\!\cdot\!S=0\iff i_S\mu$ is closed and $\langle S,\nabla V\rangle=0\iff dV\wedge i_S\mu=0$. On an oriented surface, on the regular set $\{\nabla V\neq0\}$ with connected level sets, every such $S$ is $S=a(V)\,J\nabla V$, the Hamiltonian/skew-gradient of $V$ with leaf-profile $a$ — the classical stream-function structure of $2$D incompressible flow (streamlines $=$ level sets). Globally the fibre is strictly larger: $\partial_\theta$ on $S^1\times\mathbb R$ is divergence-free and leaf-tangent but escapes the profile form: the candidate profile $a\propto 1/y$ is not a single-valued function of $V=\tfrac12 y^2$ on the regular set (the level $\{V=v\}$, $v>0$, is the two circles $y=\pm\sqrt{2v}$, on which it takes opposite signs) and diverges at the critical level $\{y=0\}$, which is exactly where the topological channel $[\eta_S]\neq0$ is generated. This is classical and is recorded only to ground the abstract fibre; no foliated-cohomology identification is claimed.

**Remark**

Theorem §thm:fibre is the spin analogue of the non-triviality of the admissibility fibre $U^{-1}(\mathsf D)$: identity of the gradient skeleton does not license transfer of $S$, exactly as identity of the transition skeleton does not license transfer of admissibility.

## The forgetful functor {#sec:functor}

We restrict morphisms to those that preserve the splitting, just as the discrete theory restricts to admissibility-preserving maps. We state the condition as a *positive semiconjugacy* of the flows, up to a positive constant time-rescaling; for a non-injective map (such as the folding of Example §ex:worked) the relevant fields are required to be projectable, so the pushforward is defined. Time parametrization need not be preserved; equivalently the condition may be read on unparametrized orbits.

**Definition (Categories and forgetful functor)** {#def:cats}

- $\mathsf{GradFlow}$ has objects $(M,g,V)$. A morphism $(M,g,V)\to(M',g',V')$ is a smooth $\phi\colon M\to M'$ with $d\phi_x(-\nabla V(x))=\lambda\,(-\nabla'V'(\phi(x)))$ for all $x$ and some constant $\lambda>0$ (determined wherever $\nabla'V'\circ\phi\neq0$, so the constant is unambiguous under composition; a positive semiconjugacy of the gradient flows; $-\nabla V$ required $\phi$-projectable when $\phi$ is non-injective).
- $\mathsf{SpinFlow}$ has objects $(M,g,V,S)$ with $S$ satisfying (S1)--(S2) and either (S3) (nontrivial spin) or $S=0$ (the trivial bare-gradient object; $S=0$ is admitted separately because $0=\nabla(\mathrm{const})$ is a gradient and so formally violates (S3)). A morphism is a smooth $\phi$ semiconjugating the gradient flow *and* the full flow by a *common* positive constant: $d\phi_x(-\nabla V(x))=\lambda\,(-\nabla'V'(\phi(x)))$ and $d\phi_x(F(x))=\lambda\,F'(\phi(x))$ for the same $\lambda>0$ ($F=-\nabla V+S$; equivalently $d\phi(S)=\lambda S'$; $F$ projectable when $\phi$ is non-injective). Thus "preserving the splitting" means a single positive time-rescaling carries the gradient and full flows together; $U_{\mathrm{sp}}$ forgets $S$, the underlying $\mathsf{GradFlow}$-morphism keeping the same $\lambda$.
- $U_{\mathrm{sp}}\colon\mathsf{SpinFlow}\to\mathsf{GradFlow}$, $(M,g,V,S)\mapsto(M,g,V)$, $\phi\mapsto\phi$.

The semiconjugacy conditions are closed under composition (the constants multiply: $d(\psi\phi)(F)=\lambda\mu\,F''\circ\psi\phi$) and hold for identities ($\lambda=1$), so $\mathsf{GradFlow}$ and $\mathsf{SpinFlow}$ are categories. The objects of $\mathsf{SpinFlow}$ over a fixed $(M,g,V)$ are $U_{\mathrm{sp}}^{-1}(-\nabla V)\cup\{0\}$; non-triviality (Theorem §thm:fibre) concerns the part $S\neq0$.

**Theorem (Faithful, not full)** {#thm:faithful}

$U_{\mathrm{sp}}\colon\mathsf{SpinFlow}\to\mathsf{GradFlow}$ is faithful but not full.

*Proof.* *Faithful.* A $\mathsf{SpinFlow}$-morphism is its underlying smooth map; if $U_{\mathrm{sp}}(\phi)=U_{\mathrm{sp}}(\psi)$ then $\phi=\psi$.

*Not full.* On $M=S^1\times\mathbb R$, $V=\tfrac12y^2$, put $F_a=a\,\partial_\theta-y\,\partial_y$. The objects $(M,g,V,\partial_\theta)$ and $(M,g,V,2\partial_\theta)$ — both satisfying (S1)--(S3) — lie over $(M,g,V)$, and the identity is a $\mathsf{GradFlow}$-morphism. A lift to a $\mathsf{SpinFlow}$-morphism $(M,g,V,\partial_\theta)\to(M,g,V,2\partial_\theta)$ would require $d(\mathrm{id})(F_1)=\lambda F_2$ for some $\lambda>0$, i.e.\ $(1,-y)=\lambda(2,-y)$; the $y$-component forces $\lambda=1$ (at $y\neq0$) and the $\theta$-component then gives $1=2$, a contradiction. Concretely, integrating $F_a$ ($y=y_0e^{-t}$, $\theta=\theta_0+at$) gives the spirals $\theta=\theta_0-a\log(y/y_0)$, which are distinct point sets for $a=1$ and $a=2$; the identity cannot carry one onto the other. No lift exists, so $U_{\mathrm{sp}}$ is not full. $\blacksquare$

**Remark**

Metric-dependence and non-canonicity of the gradient/spin split under arbitrary maps are resolved exactly as in the discrete theory: morphisms are restricted to split-preserving maps. The price is a small morphism class (isometry-like maps together with collapsing maps such as the folding below); we do not claim a rich morphism class. Faithful-not-fullness (Theorem §thm:faithful) is moreover generic for forgetful functors; the content here is not that categorical fact but the non-trivial fibre (Theorem §thm:fibre) and the lifting criterion (Proposition §prop:constructive-defect) it makes available.

## Identity transfer versus viability transfer {#sec:idvsviab}

The admissibility layer transfers a *viability kernel* $\operatorname{Viab}^\infty=\{x:\exists\text{ an admissible infinite trajectory from }x\}$ along a morphism. The spin layer carries *identity* (Proposition §prop:identity): a non-stagnant recurrent identity requires $S\neq0$, the witness being a non-vanishing period of a closed component of $\omega_S$ (§sec:certificate). The two layers are independent, with a consequence.

**Proposition (Viability transfer does not control the spin)** {#prop:viab}

Any transfer condition whose signature involves only the skeleton, the state map, the admissibility predicate, and the viability kernel — but not $S$ or its witness — cannot imply or control preservation of the identity witness $[\eta_S]$, for conditions read off data shared across the fibre (the unconditional separation being the explicit Example §ex:worked). (The weak, kernel-exact, and viability-bisimulation conditions of [admissibility] are of this form.) By Theorem §thm:fibre the fibre over a fixed skeleton is non-trivial, so such a condition is invariant under the choice of $S$ in the fibre, and equally under passage to the trivial object $S=0$ (the augmented set $U_{\mathrm{sp}}^{-1}(-\nabla V)\cup\{0\}$ of Definition §def:cats); in particular it does not see the collapse $S\to0$. Unconditionally, the folding of Example §ex:worked is a viability-exact, spin-collapsing morphism (Theorem §thm:strict); hence accurate identity transfer — viability transfer *together with* witness survival — is strictly stronger than viability transfer alone.

*Proof.* By Theorem §thm:fibre the fibre is non-trivial and skeleton-independent; a condition not mentioning $S$ in its signature takes the same value on $(M,g,V,S)$ for every $S$ in the fibre and on the trivial object $(M,g,V,0)$ of Definition §def:cats alike. Within the punctured line $\{\lambda S\}$ of a topologically-active $S$ (one with $[\eta_S]\neq0$) the witness stays non-vanishing ($[\lambda\,\eta_S]\neq0$ for $\lambda\neq0$); the value $[\eta_{S'}]=0$ is attained only at that trivial object, which the condition cannot separate from the fibre, so it cannot distinguish $[\eta_S]\neq0$ from the collapsed $[\eta_{S'}]=0$. (This invariance assumes the viability data is shared across the fibre; in general the kernel $\operatorname{Viab}^\infty$ can itself move with $S$ through the full flow, so the universal reading needs that proviso.) The unconditional separation — identical viability transfer, different witness — is the explicit folding of Example §ex:worked (Theorem §thm:strict), a viability-preserving, spin-collapsing morphism, giving strictness. ∎

*Accurate identity transfer $\Longrightarrow$ viability transfer and survival of the spin witness,*

a necessary filter, not an equality: the certificate below detects *failure* of identity transfer, not its success.

**Remark (The universal reading is an informal principle)** {#rem:viab-informal}

The broad reading of Proposition §prop:viab — that *any* condition not naming $S$ in its signature fails to control $[\eta_S]$ — is heuristic: its scope rests on an informal notion of a condition's "signature", and the fibre-invariance argument assumes the viability data is shared across the fibre (in general $\operatorname{Viab}^\infty$ can itself move with $S$ through the full flow). The rigorous content is the hypothesis-qualified invariance above together with the unconditional separation of Example §ex:worked (Theorem §thm:strict).

## The two-layer certificate {#sec:certificate}

The discrete theory certifies viability transfer by a *defect*
$\Delta_\tau=\tau_X^{-1}(\operatorname{Viab}^\infty_j)\setminus\operatorname{Viab}^\infty_i$, with $\Delta_\tau=\varnothing$ iff
the transfer is kernel-exact. The spin layer supplies a parallel certificate for identity, anchored
in cohomology.

**Definition (Identity-transfer defect)** {#def:iddefect}

Fix, as in Definition §def:identity, a closed component $\eta_S$ of $\omega_S$ with class
$[\eta_S]\in H^1_\mathrm{dR}(M)$ (on compact boundaryless $M$ the harmonic projection; in Example §ex:worked,
$\omega_S$ is itself closed). The class $[\eta_S]$, and hence this defect, is canonically determined
by $S$ only on the *canonical domain*: $M$ compact without boundary (harmonic projection), or $\omega_S$ *globally* closed ($d\omega_S=0$ on all of $M$,
i.e. operational spin identically zero, so $\eta_S=\omega_S$ is a genuine de Rham class in
$H^1_\mathrm{dR}(M)$ with homology-invariant periods). Closedness only on a neighbourhood of the chosen loops
does *not* suffice: homologous loops can then carry different periods, so the period is not a
function of the homology class. Off the canonical domain a closed component is
fixed by an auxiliary choice and the defect is relative to that choice; the general non-compact,
non-closed case is open. For a viability-preserving morphism $\phi$, the
*identity-transfer defect* is the set of classes $[\gamma]\in H_1(M;\mathbb R)$ with
$\langle[\eta_S^{(i)}],[\gamma]\rangle\neq0$ on the source but
$\langle[\eta_{S'}^{(j)}],\phi_*[\gamma]\rangle=0$ on the target. An empty defect is the
*necessary* condition for accurate transfer of the identity carried by $[\eta_S]$. The witness
sees only this cohomological component: a purely co-exact part, whose single-loop integral is
loop-dependent rather than a topological invariant, is detected separately by the local
operational spin (§sec:operational).

**Proposition (Witness as a necessary-condition certificate)** {#prop:cert}

The class $[\eta_S]\in H^1_\mathrm{dR}(M)\cong H^1(M;\mathbb R)$ of a closed component $\eta_S$ of
$\omega_S$ — equivalently the periods $\oint_\gamma\eta_S$ over a basis of $H_1$, requiring only
closedness (canonical via the harmonic representative when $M$ is compact without boundary, no uniqueness claim
otherwise) — is a well-defined, checkable invariant on the canonical domain ($M$ compact without boundary, or $\omega_S$ globally
closed, $d\omega_S=0$). By Proposition §prop:identity the
non-gradient component is necessary for a non-stagnant identity, with $[\eta_S]$ carrying its
homological content. Hence if $[\eta_S]$ collapses under transfer, the *topological channel* of
the identity witness is not transferred — by Remark §rem:two-channels the homological component,
the co-exact channel being read separately. Thus a surviving witness is a *necessary* condition
for accurate identity transfer on that channel, complementing $\Delta_\tau=\varnothing$ (survival) into a pair
survival $+$ liveness. Sufficiency is not claimed here: Proposition §prop:identity is a necessity
statement (a partial converse — sufficient for forward transfer under witness preservation — is
Theorem §thm:sufficiency).

*Proof.*
$\eta_S$ is closed, so its periods are homology invariants and $[\eta_S]\in H^1_\mathrm{dR}$. By
Proposition §prop:identity the spin is necessary for a non-stagnant identity; collapse of
$[\eta_S]$ removes the topological (homological) content of the witness on the affected classes. $\square$

**Remark (Two-layer certificate)**

The two-layer certificate is $(\Delta_\tau=\varnothing:\ \text{survival})\wedge(\text{identity defect
(Definition §def:iddefect)}=\varnothing:\ \text{liveness})$. The co-exact (operational-spin) slice is handled by a separate,
local check on $d\omega_S$ (§sec:operational), not by this topological witness. Making the
identity defect a *constructive* object with an algorithm — the analogue of the discrete
$\Delta_\tau$ — is achieved on the canonical domain in Proposition §prop:constructive-defect;
the field-level repair, by contrast, is not provided by the naive support-subspace transport, a
kernel-lattice repair remaining open (Remark §rem:no-repair).

**Proposition (Necessity and blindness of the topological witness)** {#prop:complete}

For a fixed spin $S$ the topological witness detects *only* homologically non-trivial recurrence: a
non-vanishing witness $\langle[\eta_S],[\gamma]\rangle\neq0$ forces $[\gamma]\neq0$, so homological
non-triviality is *necessary* for detection — but not sufficient, since $[\eta_S]$ may annihilate a
nonzero $[\gamma]$ (the $[\eta_S]=0$, $d\omega_S\neq0$ channel of Remark §rem:two-channels). By
non-degeneracy of the real de Rham pairing $H^1_\mathrm{dR}(M)\times H_1(M;\mathbb R)\to\mathbb R$, a nonzero
$[\gamma]$ is paired non-trivially by *some* de Rham class, so $[\gamma]\neq0$ is necessary and
abstractly sufficient for detectability *in principle*; whether such a class is *realized* by an
admissible-spin witness $[\eta_S]$ over the fixed $(M,V)$ is the separate realizability question — for
$M$ compact and boundaryless the realizable *operational-spin-free* witnesses are confined to the
subspace $W_V$ of Corollary §cor:WV (possibly proper), so a nonzero $[\gamma]$ annihilating every such
witness stays undetected. Completeness for the given $S$ is the
further, generally false, requirement that $[\eta_S]$ pair non-trivially with every recurrent class. In particular, if $H^1_\mathrm{dR}(M)=0$ then $[\eta_S]=0$ for every $S$
and every loop, so the topological witness detects no recurrent identity even where one exists, and the
local operational-spin channel $d\omega_S$ (§sec:operational) is the only detector.

*Proof.*
A non-vanishing pairing $\langle[\eta_S],[\gamma]\rangle\neq0$ vanishes whenever $[\gamma]=0$, giving the
necessity; the existential equivalence is the non-degeneracy of the de Rham pairing on real (co)homology.
If $H^1_\mathrm{dR}(M)=0$ every closed $1$-form is exact, so $\oint_\gamma\eta_S=0$ for every closed component and
every $\gamma$, while a recurrent identity may persist on the critical set (Remark §rem:critset). $\square$

**Example (A recurrent identity invisible to the topological witness)** {#ex:s2}

On $M=S^2$ with the round metric, $V=\tfrac12 z^2=\tfrac12\cos^2\theta$ and $S=\partial_\phi$ (axial
rotation): $\nabla V=-\sin\theta\cos\theta\,\partial_\theta$ vanishes on the equator $\{\theta=\pi/2\}$;
$S$ is divergence-free (a Killing field), $\langle S,\nabla V\rangle=0$ (azimuthal $\perp$ meridional,
(S2)), and $\omega_S=\sin^2\theta\,d\phi$ has
$d\omega_S=2\sin\theta\cos\theta\,d\theta\wedge d\phi\neq0$ (operational spin present, (S3)). The
equator is invariant ($\dot z=0$ there) and the motion on it is the pure rotation $\dot x=S$ — a
non-stagnant recurrent identity with $S\neq0$. Yet $H^1_\mathrm{dR}(S^2)=0$, so $[\eta_S]=0$ (the harmonic
projection of $\omega_S$ vanishes); the single-loop integral $\oint_{\mathrm{eq}}\omega_S=2\pi$ is
*not* the witness, being the loop-dependent integral of a non-closed form over the null-homologous
equator (Definition §def:iddefect). Only $d\omega_S$ detects the identity: the topological certificate
is necessarily blind. The discrete realization is the disk complex of §sec:operational ($b_1=0$,
witness $\equiv0$, nonzero curl).

**Proposition (Constructive identity-transfer defect and exactness)** {#prop:constructive-defect}

On the canonical domain, with $M,M'$ of finite homological type ($b_1<\infty$; needed only for the finite algorithm below, not for the linear-algebra equivalence), write
$a:=[\eta_S]\in H^1_\mathrm{dR}(M)\cong\operatorname{Hom}(H_1(M;\mathbb R),\mathbb R)$ and $b:=\phi^*[\eta_{S'}]$. Then the
identity-transfer defect of Definition §def:iddefect is
$$
\{[\gamma]\in H_1(M;\mathbb R):\langle[\eta_S],[\gamma]\rangle\neq0,\ \langle[\eta_{S'}],\phi_*[\gamma]\rangle=0\}
=\ker b\setminus\ker a,
$$
computable by linear algebra (Gaussian elimination on the $2\times b_1$ period matrix $[a;b]$ over an
$H_1$-basis). The transfer is *witness-exact* (empty defect) iff $\ker b\subseteq\ker a$,
equivalently iff
$$
[\eta_S]=\lambda\,\phi^*[\eta_{S'}]\qquad\text{for some }\lambda\in\mathbb R,
$$
i.e. iff the source witness is proportional to the pulled-back target witness. Here *witness-exact*
means preservation of *non-vanishing of the source periods* — every $[\gamma]$ with $a([\gamma])\neq0$
keeps $b([\gamma])\neq0$, i.e. $\ker b\subseteq\ker a$ (matching Definition §def:wp) — not preservation
of period values (the scalar $\lambda$ is free) nor of the full zero/non-zero pattern (if $a=0$ the defect
is empty vacuously while $b$ may be nonzero). This is the continuous analogue of the discrete defect
$\Delta_\tau$ and renders the identity defect constructive on the canonical domain — a finite test
once an $H_1$-basis and the period vectors $a,b$ are supplied; their extraction, and a field-level
repaired spin, from raw dynamics is not addressed (§sec:operational).

*Proof.*
By naturality of the de Rham pairing,
$\langle[\eta_{S'}],\phi_*[\gamma]\rangle=\langle\phi^*[\eta_{S'}],[\gamma]\rangle=b([\gamma])$, so the
target period vanishes iff $[\gamma]\in\ker b$ and the source period is nonzero iff
$[\gamma]\notin\ker a$; hence the defect is $\ker b\setminus\ker a$, empty iff $\ker b\subseteq\ker a$.
For linear functionals, $\ker b\subseteq\ker a$ holds iff $a\in\operatorname{span}\{b\}$: if $b=0$ then
$\ker b=H_1\subseteq\ker a$ forces $a=0=0\cdot b$; if $b\neq0$, pick $v_0$ with $b(v_0)=1$ and set
$\lambda:=a(v_0)$, so $v-b(v)v_0\in\ker b\subseteq\ker a$ gives $a(v)=\lambda b(v)$ for all $v$. $\square$

**Remark (The support-subspace repair is blind to the witness)** {#rem:no-repair}

One may try to repair a failed transfer by transporting a discrete minimal-repair calculus to the
lattice of homology subspaces $\mathrm{Sub}(H_1(M;\mathbb R))$ along $\phi_*$ (image $\dashv$ preimage).
This is well-defined and metric-free, but it enforces the *forward containment*
$\phi_*(\mathrm{supp})\subseteq\mathrm{supp}'$ of supports (a *support* here is a chosen homology
subspace standing in for the witness, transported by image/preimage) — the homological shadow of viability transfer —
which is insensitive to the witness within the fibre (the support is unchanged under $S\mapsto\lambda S$;
cf. Proposition §prop:viab), and is in fact satisfied
*vacuously* whenever $\phi$ collapses the relevant homology: in Example §ex:worked the folding
has $\phi_*=0$, so the containment holds while the witness $2\pi\mapsto0$ is destroyed. Witness-exactness
is instead the dual, codimension-one condition $[\eta_S]=\lambda\,\phi^*[\eta_{S'}]$ of
Proposition §prop:constructive-defect, which the meet and join of *support* subspaces do not
preserve (they leave the kernel-of-a-single-functional stratum). Thus the identity layer admits a
constructive *defect* (detection) but not this support-subspace repair: the support transport is
vacuous under collapse and blind to the witness within the fibre. We claim no more — witness-exactness
is itself a kernel-containment $\ker b\subseteq\ker a$, so a minimal-repair calculus on the dual lattice
of *kernels/annihilators* (rather than supports) is not excluded and remains open, as does a
constructive witness-repair at the field level — lifting a corrected class back to an
(S2)-admissible spin.

**Proposition (Operational-spin obstruction)** {#prop:opspin-obstruction}

Let $M$ be compact and boundaryless. Fix $c\in H^1_\mathrm{dR}(M)$ with $c\neq0$ and harmonic representative $h_c$. A spin carrying the witness $[\eta_S]=c$ can be *simultaneously* divergence-free (S1), *operational-spin-free* ($d\omega_S=0$), and (S2)-admissible if and only if

$$
h_c(\nabla V)=0\quad\text{pointwise.}
$$

Hence whenever $h_c(\nabla V)\not\equiv0$ — which occurs for suitable $(M,V,c)$ — the four conditions (S1), $d\omega_S=0$, (S2), and $[\eta_S]=c\neq0$ are jointly unrealizable: eliminating the operational spin forces giving up (S1) or (S2). The condition is *class-dependent* — on a fixed $M$ some classes are obstructed and others are not.

*Proof.* (S1) is $\delta\omega_S=0$ and operational-spin-freeness is $d\omega_S=0$; together $\Delta\omega_S=0$, so $\omega_S$ is harmonic and hence equals the unique harmonic representative $h_c$ of its class (Hodge theory on compact $M$, where $\omega_S$ closed gives $[\eta_S]=[\omega_S]=c$). Then (S2), i.e. $\omega_S(\nabla V)=0$, reads $h_c(\nabla V)=0$. Conversely $S=h_c^\sharp$ is harmonic (so (S1) and $d\omega_S=0$), has class $c\neq0$ — whence (S3), a nonzero harmonic form being non-exact — and satisfies (S2) precisely when $h_c(\nabla V)=0$. $\blacksquare$

**Corollary (The obstruction space $W_V$)** {#cor:WV}

Let $M$ be compact and boundaryless and $V\in C^\infty(M)$ arbitrary; write $\mathcal H^1(M)$ for the harmonic $1$-forms and $\Phi\colon\mathcal H^1(M)\xrightarrow{\sim}H^1_\mathrm{dR}(M)$ for the (metric-dependent) Hodge isomorphism. The contraction

$$
L\colon\mathcal H^1(M)\to C^\infty(M),\qquad L(h)=h(\nabla V)=\langle h^\sharp,\nabla V\rangle,
$$

is $\mathbb R$-linear, and $\ker L$ is exactly the harmonic forms whose dual fields are pointwise orthogonal to $\nabla V$ — tangent to the regular level sets $\{V=\mathrm{const}\}$, the harmonic (S2)-spins. Put $W_V:=\Phi(\ker L)\subseteq H^1_\mathrm{dR}(M)$. Then $W_V$ is a linear subspace, and a class $c$ is carried by a divergence-free, operational-spin-free, (S2)-admissible spin *iff* $c\in W_V$ and $c\neq0$ — the zero class lies in $W_V$ by linearity but is not a spin ((S3) excludes $S=0$). On the operational-spin-free locus the otherwise infinite-dimensional spin fibre over a fixed skeleton collapses to the finite-dimensional $W_V$, with

$$
\dim W_V=\dim\ker L\le b_1(M),
$$

a *metric-dependent* invariant of the triple $(M,g,V)$, not a topological invariant of $M$ (Remark §rem:WV-models). For $V$ constant $\nabla V=0$, $L\equiv0$ and $W_V=H^1_\mathrm{dR}(M)$ (no obstruction); the obstruction is the deficit $W_V\subsetneq H^1_\mathrm{dR}(M)$, which therefore *requires* $V$ non-constant — though a non-constant $V$ need not produce one (Remark §rem:opspin-classdep).

*Proof.* $L$ is pointwise evaluation of $h$ on the fixed field $\nabla V$, hence $\mathbb R$-linear; $\ker L$ is a subspace and $\Phi$ a linear isomorphism, so $W_V$ is a subspace. By Proposition §prop:opspin-obstruction a class $c\neq0$ is realized iff $h_c(\nabla V)=0$, i.e. $h_c\in\ker L$, i.e. $c\in W_V$. A divergence-free, operational-spin-free field has $\omega_S$ closed and co-closed, hence harmonic on compact boundaryless $M$, so $\omega_S$ is its own harmonic representative; (S2) then cuts out $\mathcal H^1(M)\cap\ker L\cong W_V$, finite-dimensional, whereas the full fibre retains a leaf-profile's worth of freedom (Remark §rem:streamfn). $\blacksquare$

**Remark (Class-dependence; the obstruction is $\not\equiv0$, never everywhere)** {#rem:opspin-classdep}

On the flat torus $T^2=\mathbb R^2/(2\pi\mathbb Z)^2$ with $V=V(x)$ non-constant, the harmonic $1$-forms are $c_1\,dx+c_2\,dy$ and $\nabla V=V'(x)\,\partial_x$, so $h_c(\nabla V)=c_1V'(x)$: every class with $c_1\neq0$ is obstructed ($c_1V'\not\equiv0$), while the classes $\mathbb R[dy]$ are free. Since $\nabla V$ vanishes at the critical points of $V$ — which exist on any compact $M$, where $V$ attains its extrema — $h_c(\nabla V)$ vanishes there for *every* class; the obstruction is the failure $h_c(\nabla V)\not\equiv0$ at *some* point, never at every point. Some $(M,V)$ carry no obstructed class at all — e.g. $M=S^1\times N$ with $b_1(N)=0$ (so $H^1_\mathrm{dR}(M)=\mathbb R[d\theta]$) and $V=V(n)$ on the $N$-factor, where the sole harmonic class has $d\theta(\nabla V)\equiv0$; when $b_1(N)>0$ the $N$-factor classes can instead be obstructed (as the $T^2$, $V=V(x)$ computation above shows), so absence of *any* obstructed class needs that extra topological hypothesis. This sharpens the field-level question of Remark §rem:no-repair: reaching the operational-spin-free (closed) regime while keeping a divergence-free, (S2)-admissible witness is obstructed exactly by the classical Hodge condition $h_c(\nabla V)\not\equiv0$, not by any choice of repair calculus. The constructive interplay off this regime — restoring (S2) by giving up (S1) — is a transport problem along $\nabla V$ and is not addressed here. Whether the obstruction space $W_V$ of Corollary §cor:WV vanishes is *dynamical*: $W_V=0$ iff no nonzero harmonic field admits $V$ as a non-constant first integral, since $[h]\in W_V$ exactly when $h(\nabla V)=h^\sharp(V)=0$, i.e. $V$ is constant along the flow of $h^\sharp$. A single harmonic field of minimal flow (e.g. an irrational linear field on a flat $T^2$) has only constant first integrals, so *its* class never lies in $W_V$ for non-constant $V$; a harmonic field with closed orbits (a rational field on $T^2$, or the $S^1$-factor of a product) admits a non-constant first integral, so its class enters $W_V$ for the matching $V$ — as the $V=V(x)$ and $S^1\times N$ computations above (so the same flat $T^2$ carries both free and obstructed classes). Thus $W_V=0$ demands that *no* nonzero harmonic direction admit $V$ as a first integral: it is a joint property of $(g,V)$ — which harmonic flows the metric carries and which of them $V$ integrates — not a matter of generic $V$ alone.

**Proposition (Genericity of trivial harmonic symmetry)** {#prop:WV-generic}

Let $M$ be compact, oriented, boundaryless with $b_1(M)\ge1$, and $V\in C^\infty(M)$. Fix a basis $h_1,\dots,h_{b_1}$ of $\mathcal H^1(M)$ and set $F_V(p):=\big(h_1^\sharp(V)(p),\dots,h_{b_1}^\sharp(V)(p)\big)\in\mathbb R^{b_1}$. Then

$$
\dim W_V \;=\; b_1-\dim_{\mathbb R}\operatorname{span}\{F_V(p):p\in M\},
$$

and $\{V\in C^\infty(M):\dim W_V=0\}$ is open and dense in $C^k(M)$ for every $k\ge1$. Thus $\dim W_V>0$ is *non-generic* — a positive-codimension condition witnessing an exact infinitesimal symmetry of $V$ along a harmonic direction.

*Proof.* For $c\in\mathbb R^{b_1}$, $\sum_ic_ih_i\in W_V$ iff $\sum_ic_ih_i^\sharp(V)\equiv0$, i.e. iff $c\perp F_V(p)$ for every $p$, i.e. iff $c\perp\operatorname{span}F_V(M)$; the identity follows. *Openness:* $\dim W_V=0$ iff $L$ of Corollary §cor:WV is injective on the $b_1$-dimensional $\mathcal H^1(M)$, equivalently some $b_1\times b_1$ evaluation minor $\det[h_i^\sharp(V)(p_j)]$ at suitable $p_1,\dots,p_{b_1}$ (the matrix of the density step below) is nonzero; each entry is continuous in the $1$-jet of $V$, so this is an open condition. *Density:* for each $p$ put $S_p:=\{(\langle v,h_i^\sharp(p)\rangle)_i:v\in T_pM\}\subseteq\mathbb R^{b_1}$; if $c\perp S_p$ for all $p$ then $\sum_ic_ih_i^\sharp\equiv0$, so $\sum_ic_ih_i=0$ and $c=0$ — hence the $S_p$ jointly span $\mathbb R^{b_1}$. Choose distinct $p_1,\dots,p_{b_1}$ and $v_j\in T_{p_j}M$ with $k_j:=(\langle v_j,h_i^\sharp(p_j)\rangle)_i$ linearly independent — extend greedily, using that the spanning $S_p$ vary continuously and $M$ has no isolated point, so a vector outside the current span is always available at a fresh point — and bump functions $\psi_j$ of disjoint small support with $\nabla\psi_j(p_j)=v_j$. For $V=V_0+\sum_js_j\psi_j$ the matrix $\big[h_i^\sharp(V)(p_j)\big]$ has $j$-th column $b_j+s_jk_j$ (with $b_j:=(h_i^\sharp(V_0)(p_j))_i$), so its determinant is a polynomial in $s$ with leading coefficient $\det[k_1,\dots,k_{b_1}]\neq0$; it is therefore nonzero for arbitrarily small generic $s$, giving $\dim W_V=0$ within any $C^k$-neighbourhood of $V_0$ (every $k\ge1$). $\blacksquare$

**Remark (Sharp models; $\dim W_V$ is not topological)** {#rem:WV-models}

On a flat torus $T^n=\mathbb R^n/\Lambda$ harmonic forms are constant-coefficient, so $h_a^\sharp$ is the constant field $a$ and $h_a^\sharp(V)=D_aV$; since $D_aV\equiv0$ upgrades to $V(x+ta)=V(x)$,

$$
\dim W_V \;=\; n-\dim_{\mathbb R}\operatorname{span}\{\xi\in\Lambda^*:\widehat V(\xi)\neq0\},
$$

the dimension of the largest subtorus of translations fixing $V$. Under $\operatorname{Ric}\ge0$ every harmonic $1$-form is parallel by Bochner's theorem [petersen] (so $b_1\le n$); in particular each $h\in W_V$ is parallel and $h^\sharp$ is a Killing field. Finally $\dim W_V$ is *not* a topological invariant: on a fixed $M$ it varies with both $g$ and $V$ — on $T^2$ with $V=V(x)$ one has $\dim W_V=1$ for the flat metric but $0$ for a generic nearby metric — and it is not determined by the level foliation of $V$ alone.

**Remark (Joint use of the two instances)** {#rem:joint}

The two instances are meant to be used together. The admissibility companion [admissibility] certifies *survival* by the viability defect $\Delta_\tau$ (with its constructive transfer/repair calculus); the spin layer certifies *liveness* by the identity defect, constructive as $\ker b\setminus\ker a$ on the canonical domain (Proposition §prop:constructive-defect), the continuous counterpart of $\Delta_\tau$. Proposition §prop:viab shows the two are independent: a morphism can be viability-exact ($\Delta_\tau=\varnothing$) yet destroy the witness — the *survives-but-dead* configuration of Example §ex:worked. Hence neither certificate alone suffices: viability without liveness passes a dead system, and the witness alone says nothing about survival. The joint certificate is the conjunction survival\,$\wedge$\,liveness (necessary, not sufficient: it detects failure of survival and of topological-witness liveness, and is silent on the co-exact channel and on non-topological liveness), and by the homological bridge (§sec:bridge) its liveness half is, under the bridge's class-correspondence, the *same* $H_1$-invariant in the discrete and the continuous scene. This is the operative reason to run the admissibility and spin calculi jointly rather than separately. Within NC2.5 [nc25], this survival/liveness pair is the published distinction between mere physical persistence and identity carried by coherence rather than behaviour (Axiom 20), under the cycle-reinitiation criterion of liveness (Axiom 9): the topological identity witness furnishes a constructive realization of the identity (liveness) channel whose necessity is Theorem 62, the *survives-but-dead* configuration being the silent identity degradation of the performance–identity decoupling (Theorem 15), in which observable viability remains admissible while identity-preserving structure is already eroding. Beyond instantiating that pair, this note opens a *cohomological axis* for it: the liveness witness is here a de Rham class with a constructive transfer-defect (Proposition §prop:constructive-defect), computable on finite data (§sec:operational); the kernel/annihilator repair lattice, the field-level witness-repair, and the apparatus bridge are the directions it thereby opens for the core.

## A worked example {#sec:worked}

**Example** {#ex:worked}

A continuous setting in which viability and spin coexist cleanly, computing Proposition §prop:viab and the certificate of Proposition §prop:cert.

**Source $A$ (live).** $M_A=S^1\times\mathbb R$, $(\theta,y)$, metric $d\theta^2+dy^2$; flow $\dot\theta=1,\ \dot y=-y$. With $V_A=\tfrac12y^2$, $-\nabla V_A=-y\,\partial_y$ and $S_A=\partial_\theta$. Checks: $\nabla\!\cdot\!\partial_\theta=0$; $\langle\partial_\theta,y\partial_y\rangle=0$ (S2 directly); $\omega_S^A=d\theta$ not exact on $S^1$ (so S1--S3). With $\mathrm{Adm}_A=\{\gamma\subseteq K_A\}$, $K_A=\{|y|\le1\}$, and $|y(t)|=|y_0|e^{-t}$ decreasing, $\operatorname{Viab}^\infty_A=S^1\times[-1,1]$. The identity is non-stagnant: on the invariant circle $\{y=0\}$ the flow rotates ($\dot\theta=1$). The form $\omega_S^A=d\theta$ is closed (operational spin $0$), so it equals its own closed component $\eta_S^A$ and $\oint_\gamma\eta_S^A=2\pi$ is a de~Rham invariant of the homology class (only closedness is used; $S^1\times\mathbb R$ is non-compact).

**Target $B$ (survives, dead).** $M_B=\mathbb R$, $\dot y=-y$, $S_B=0$, $K_B=\{|y|\le1\}$, $\operatorname{Viab}^\infty_B=[-1,1]$, $\omega_S^B=0$. Here $B$ is the trivial object of Definition §def:cats.

**Morphism.** $\tau_X(\theta,y)=y$ (folding the circle); $d\tau(F_A)=d\tau(\partial_\theta)-y\,d\tau(\partial_y)=0-y\,\partial_y=F_B\circ\tau$ ($\lambda=1$), so $\tau$ is a $\mathsf{SpinFlow}$-morphism.

(I) As above, $\tau$ semiconjugates both the gradient flow and $F_A$ (to $F_B$); it is a $\mathsf{SpinFlow}$-morphism.
(II) Admissibility: $\mathrm{Adm}_A(\gamma)\Rightarrow\gamma\subseteq S^1\times[-1,1]\Rightarrow \tau\gamma\subseteq[-1,1]\Rightarrow\mathrm{Adm}_B(\tau\gamma)$.
(III) Viability: $\tau_X^{-1}(\operatorname{Viab}^\infty_B)=S^1\times[-1,1]=\operatorname{Viab}^\infty_A$, hence $\Delta_\tau=\varnothing$ (kernel-exact: survival transferred exactly).
(IV) Identity: for $[\gamma]$ the generator of $H_1$, $\langle[\eta_S^A],[\gamma]\rangle =\oint_\gamma\omega_S^A=2\pi\neq0$, while $\tau_*[\gamma]=0$ in $H_1(\mathbb R)=0$, so $\langle[\eta_S^B],\tau_*[\gamma]\rangle=0$: the identity defect contains the generator $[\gamma]$ and, over real homology, is all of $H_1(M_A;\mathbb R)\setminus\{0\}$ (in the notation of Proposition §prop:constructive-defect, $b=\tau^*[\eta_S^B]=0$ so $\ker b=H_1$, while $a=[\eta_S^A]$ gives $\ker a=\{0\}$), the witness going $2\pi\to0$.

The viability certificate passes ($\Delta_\tau=\varnothing$); the spin certificate catches the false positive — the system survives but is dead. Proposition §prop:viab is here computed, not postulated.

**Contrast (witness preservation is non-empty).** The identity $\mathrm{id}_A$ on $A$ (and the rotations $\theta\mapsto\theta+c$, isometries fixing $V_A,S_A$) are $\mathsf{SpinFlow}$-morphisms with $\langle[\eta_S],\cdot\rangle$ unchanged and empty identity defect; the witness-preserving class is thus non-empty, and the strict inclusion of Theorem §thm:strict is meaningful.

## Witness-preserving morphisms {#sec:strict}

A $\mathsf{SpinFlow}$-morphism $\phi\colon(M,g,V,S)\to(M',g',V',S')$ induces $\phi_*\colon H_1(M)\to H_1(M')$ and $\phi^*\colon H^1(M';\mathbb R)\to H^1(M;\mathbb R)$ (homology and cohomology are functorial for all continuous maps, including non-injective ones). The witness over $[\gamma]\in H_1(M)$ is the pairing $\langle[\eta_S],[\gamma]\rangle$, transferred along $\phi$ to $\langle[\eta_{S'}],\phi_*[\gamma]\rangle$.

**Definition (Witness-preserving)** {#def:wp}

$\phi$ is *witness-preserving* if it preserves non-vanishing of the cohomological pairing: for every $[\gamma]\in H_1(M;\mathbb R)$ with $\langle[\eta_S],[\gamma]\rangle\neq0$ one has $\langle[\eta_{S'}],\phi_*[\gamma]\rangle\neq0$.

**Theorem (Witness preservation is strictly stronger)** {#thm:strict}

The witness-preserving morphisms form a class strictly contained in the $\mathsf{SpinFlow}$-morphisms; viability-exactness does not imply witness-preservation. The folding $\tau$ of Example §ex:worked is a $\mathsf{SpinFlow}$-morphism and is kernel-exact ($\Delta_\tau=\varnothing$) yet is not witness-preserving.

*Proof.* $\tau$ is a $\mathsf{SpinFlow}$-morphism and kernel-exact by (I)--(III) of Example §ex:worked. For $[\gamma]$ the generator of $H_1(S^1\times\mathbb R)=\mathbb Z$, $\langle[\eta_S^A],[\gamma]\rangle=2\pi\neq0$ while $\tau_*[\gamma]=0$ in $H_1(\mathbb R)=0$, so $\langle[\eta_S^B],\tau_*[\gamma]\rangle=0$: $\tau$ is not witness-preserving and the inclusion is strict. By the contrast in Example §ex:worked the class is non-empty (identities, isometries), so it is a genuine intermediate level. $\blacksquare$

**Remark**

Definition §def:wp fixes the mechanism formally: witness preservation is preservation of non-vanishing of the induced cohomological pairing, not a verbal "the witness survives". The constructive transfer/repair calculus at this level — a lattice/adjoint structure on the fibre and a minimal repair — is open; the identity defect itself is made constructive on the canonical domain (Proposition §prop:constructive-defect).

**Theorem (Witness preservation positively transfers the topological identity)** {#thm:sufficiency}

Let $\phi\colon(M,g,V,S)\to(M',g',V',S')$ be a $\mathsf{SpinFlow}$-morphism that is witness-preserving (Definition §def:wp), with source and target on the canonical domain (Definition §def:iddefect) so that $[\eta_S],[\eta_{S'}]$ are de Rham classes. Then for every non-stagnant recurrent identity $\gamma$ of the source with non-vanishing witness $\langle[\eta_S],[\gamma]\rangle\neq0$, the image $\phi(\gamma)$ is a non-stagnant recurrent identity of the target with non-vanishing witness $\langle[\eta_{S'}],\phi_*[\gamma]\rangle\neq0$. Thus witness preservation is not merely the necessary filter of §sec:idvsviab but is *sufficient for forward transfer of the topological identity* carried by $[\gamma]$.

*Proof.* A $\mathsf{SpinFlow}$-morphism semiconjugates the full flow by a positive constant, $\phi\circ\Phi_s=\Phi'_{\lambda s}\circ\phi$ for the flows $\Phi,\Phi'$ of $F,F'$ and some $\lambda>0$ (Definition §def:cats). If $x_0\in\gamma$ is recurrent with return times $t_n\to\infty$ (the source flow being forward-defined there, as in Proposition §prop:identity), $\Phi_{t_n}(x_0)\to x_0$, then the semiconjugacy makes $\Phi'_{\lambda t_n}(\phi x_0)=\phi(\Phi_{t_n}(x_0))$ defined, and $\to\phi(x_0)$ by continuity, with $\lambda t_n\to\infty$; so $\phi(x_0)$ is recurrent and $\phi(\gamma)$ is a recurrent orbit of the target. Witness preservation (Definition §def:wp) gives $\langle[\eta_{S'}],\phi_*[\gamma]\rangle\neq0$, whence $\phi_*[\gamma]\neq0$; since $\phi_*[\gamma]=[\phi(\gamma)]$ by functoriality (the recurrence loop $\gamma$ of Definition §def:identity furnishing the cycle representative, $\phi(\gamma)$ its image) and a constant orbit is null-homologous, $\phi(\gamma)$ is non-constant, i.e. non-stagnant. Hence $\phi(\gamma)$ is a non-stagnant recurrent identity whose witness survives. $\blacksquare$

**Corollary (Joint sufficiency under bisimulation)** {#cor:joint-sufficiency}

If $\phi$ is in addition a viability-bisimulation — so the viability kernel transfers in both directions [admissibility] — then $\phi$ transfers both the viability kernel (survival) and the topological identity carried by $[\gamma]$ (forward liveness). The joint certificate of §sec:certificate, necessary in general, is therefore *sufficient* on the topological channel under (viability-bisimulation $+$ witness preservation); the reverse-direction liveness and the co-exact channel are not covered.

## A homological bridge between the discrete and continuous instances {#sec:bridge}

The discrete instance lives on transition systems and the continuous one on flows; a full functorial bridge between the two apparatuses is open. The *identity witness*, however, bridges them, because it is homological and homology is common to both scenes.

**Proposition (The witness is homological)** {#prop:bridge}

The witness is a class $[\eta_S]\in H^1_\mathrm{dR}(M)\cong H^1(M;\mathbb R)$ paired with $H_1$. Singular/de Rham homology of a smooth $M$ and the cycle space of a discrete skeleton (graph or simplicial complex) agree on homotopy-equivalent models; e.g. $S^1$ and a cycle graph $C_n$ both have $H_1=\mathbb Z$. Hence homology furnishes a common comparison space: a map inducing an isomorphism on $H_1$ identifies the cycle spaces of the two scenes and makes the two witnesses comparable. Transfer of the witness is the *further* condition that the classes correspond under the induced map — $[\eta_S]=\lambda\,\phi^*[\eta_{S'}]$ as in Proposition §prop:constructive-defect — since the source and target witness $1$-forms are independent data that an $H_1$-isomorphism alone does not relate. Under that correspondence the certificate (survival of the witness) is an $H_1$-statement computable in either scene (a de Rham period, or a winding number on the graph cycle). The certificate is the *non-vanishing* of the class; integral and real coefficients agree by the universal-coefficient theorem for the torsion-free $H_1$ in scope (e.g. $H_1=\mathbb Z$ in Example §ex:worked; the general defect of Proposition §prop:constructive-defect allows any $b_1<\infty$), so integrality is not required.

*Proof.* $\eta_S$ closed gives a class in $H^1_\mathrm{dR}$; the de Rham theorem $H^1_\mathrm{dR}(M)\cong H^1(M;\mathbb R)$ [warner, bott] identifies it with singular cohomology, a homotopy invariant insensitive to triangulation, so the witness is the same kind of object in either scene. By naturality of the pairing, $\langle[\eta_{S'}],\phi_*[\gamma]\rangle=\langle\phi^*[\eta_{S'}],[\gamma]\rangle$; hence once $[\eta_S]=\lambda\,\phi^*[\eta_{S'}]$ the source and transferred periods agree up to $\lambda$, while an isomorphism on $H_1$ guarantees only that no cycle is lost in the comparison, not the class correspondence. $\qquad\blacksquare$

**Remark (Discrete shadow of the example)**

The source $A=S^1\times\mathbb R$ has the discrete shadow $C_n\times(\text{line})$ with $H_1=\mathbb Z$ and the same witness class: winding number $1$ and period $\oint d\theta=2\pi=2\pi\cdot1$ (one generator, normalization $2\pi$). The folding $\tau$ (collapsing $S^1$) is, discretely, the collapse of $C_n$ to a point, which kills the winding — the identity defect. The example runs identically in both scenes. What is bridged is the *invariant*, not the apparatus: a single scene carrying both structures, or a discretization functor preserving both $\operatorname{Viab}^\infty$ and $[\eta_S]$, remains open.

## Operationalization {#sec:operational}

For a concrete adaptive system $\dot x=F$ the certificate is not yet a turnkey computation; this is the least closed item. What is already measurable is the *operational spin*: after lowering an index with $g$, the antisymmetric part of the Levi-Civita covariant derivative $\nabla F$ is the $2$-form $\tfrac12\,d(F^\flat)$, and since the Hessian of $-V$ is symmetric this equals $\tfrac12\,d(S^\flat)=\tfrac12\,d\omega_S$ (in coordinates $\tfrac12(J-J^\top)$, $J=\nabla F$). It is the classical local vorticity (spin) tensor of continuum mechanics [truesdell, batchelor], here a measured local diagnostic, and detects the failure of $\omega_S$ to be closed. The global identity witness $\oint_\gamma\eta_S$ additionally requires a structural metric, the recurrence loops $\gamma$, and the circulation around them. The two are linked: where the operational spin vanishes (so $\omega_S$ is closed, $d\omega_S=0$), the period $\oint_\gamma\omega_S$ is a clean topological witness (Proposition §prop:cert); vanishing only near $\gamma$ gives a period invariant merely under homotopies within that neighbourhood, not a homology invariant. The remaining difficulties — a structural metric, loop-finding in high dimension, and the homology of an empirical state space — are open; this note provides the invariant and its certificate, not their high-dimensional computation.

**A diagnostic graph-Hodge instrument (finite case).** On a finite simplicial model the witness and its collapse are directly computable, turning the certificate from "certificate-required" into a running diagnostic on the discrete instance. From sampled states one builds a complex (nodes, $k$-nearest edges, filled triangles); the $1$-Hodge-Laplacian $L_1=B_1^\top B_1+B_2B_2^\top$, with $B_1,B_2$ the node--edge and edge--triangle incidence operators, has harmonic kernel of dimension $b_1$, and the witness is the circulation of the harmonic component around a detected recurrence loop. On a triangulated cylinder ($b_1=1$, the homotopy model of $S^1\times\mathbb R$) the instrument returns harmonic dimension $1$ and, from an edge $1$-cochain of circulation values, a nonzero witness (the incidence data fix the harmonic subspace; the cochain supplies its amplitude), while the viability-exact folding sends the loop's homology generator to $0$, so the pushed-forward witness vanishes identically — the *survives-but-dead* configuration of Example §ex:worked, detected end-to-end from raw incidence data. On a triangulated disk ($b_1=0$, the discrete analogue of Example §ex:s2) the harmonic dimension is $0$ and the topological witness is identically zero while the curl content is nonzero — the blind case of Proposition §prop:complete, confirmed numerically. The reference implementation is the companion script `spin_hodge_demo.py`, a *diagnostic* only (it computes and detects, with no control action). This realizes the finite/discrete operationalization; the structural metric, loop-finding, and empirical homology for general continuous systems remain open.

**Remark (Dynamical reading of the witness via the asymptotic cycle)** {#rem:schwartzman}

Let $\gamma$ be a non-stagnant recurrent identity, carried by Remark §rem:critset on the critical set $\{\nabla V=0\}$ where the motion is pure spin $\dot x=S$, and let $\eta_S$ be a closed component of $\omega_S=S^\flat$ on the canonical domain (Definition §def:iddefect). If the recurrent set carries a flow-invariant Borel probability measure $\mu$ — automatic when it is compact (Krylov--Bogolyubov), e.g. the compact invariant circle $\{y=0\}$ of Example §ex:worked — then the *Schwartzman asymptotic cycle* $A_\mu\in H_1(M;\mathbb R)$, defined by $\langle[\omega],A_\mu\rangle=\int_M\omega(S)\,d\mu$ for every closed $\omega$ [schwartzman], pairs with the witness as
$$
  \langle[\eta_S],A_\mu\rangle=\int_M \eta_S(S)\,d\mu,
$$
the $\mu$-average of the circulation density $\eta_S(S)$. The integrand of an exact form averages to zero by invariance, so this depends only on the class $[\eta_S]$: it re-expresses the existing $H^1\times H_1$ pairing, dynamically averaged, and introduces no new invariant. If $\mu$ is moreover ergodic, then for $\mu$-a.e. $x$ it equals the orbit time-average $\lim_{T\to\infty}\tfrac1T\oint_{\gamma|[0,T]}\eta_S$ (Birkhoff; for a merely invariant $\mu$ the a.e. time-average is the conditional expectation onto the invariant $\sigma$-algebra, with the same $\mu$-integral but generally non-constant); if the recurrent dynamics is uniquely ergodic the equality holds for every $x$ (the rigid rotation on $\{y=0\}$ is uniquely ergodic). For a periodic orbit of time-period $T$, $A_\gamma=[\gamma]/T$ and $\langle[\eta_S],A_\gamma\rangle=\tfrac1T\oint_\gamma\eta_S$, the *asymptotic circulation rate* (de~Rham period per unit time). On the globally-closed branch $\eta_S=\omega_S=S^\flat$, so $\eta_S(S)=\langle S,S\rangle=\|S\|^2$ and $\langle[\eta_S],A_\mu\rangle=\int_M\|S\|^2\,d\mu$, the time-averaged squared spin speed (rate $1$ in the example). The reading is one-way: nonzero mean circulation forces $[\eta_S]\neq0$ and $A_\mu\neq0$ (hence $[\gamma]\neq0$ in the periodic/uniquely-ergodic case, where $A_\mu$ is proportional to $[\gamma]$); it yields no converse — by Proposition §prop:complete a nonzero class may annihilate $A_\mu$ — and so adds no sufficiency. On $H^1_\mathrm{dR}(M)=0$ (Example §ex:s2) the pairing vanishes identically, inheriting the blindness of Proposition §prop:complete; and $A_\mu$ depends on the choice of $\mu$, not an $S$-canonical number unless the recurrent dynamics is uniquely ergodic. In particular $A_\mu$ recasts the hand-fed recurrence loop above as an invariant-measure average — an intrinsic substitute for loop selection on the recurrent set.

## Results, scope, and open problems {#sec:scope}

**Proven.**
The spin layer is an instance of the forgetful-separation pattern: the fibre over a fixed gradient
skeleton is non-trivial (Theorem §thm:fibre); spin is necessary to sustain a recurrent
identity (Proposition §prop:identity); the forgetful functor is faithful but not full
(Theorem §thm:faithful); transferring viability does not control the spin, so accurate
identity transfer (viability transfer with witness survival) is strictly stronger than viability transfer alone (Proposition §prop:viab,
Theorem §thm:strict); the witness $[\eta_S]$ is a necessary-condition certificate
(Proposition §prop:cert) and is homological, hence provides a common $H_1$ comparison across the
discrete and continuous scenes (Proposition §prop:bridge); on the canonical domain the identity defect is constructive, with a
proportionality criterion for witness-exactness (Proposition §prop:constructive-defect), while the
naive support-subspace (viability-shadow) repair does not transport to the witness (Remark §rem:no-repair); and operational-spin elimination is structurally
obstructed — on a compact boundaryless $M$, a divergence-free, \textup{(S2)}-admissible, operational-spin-free spin of nonzero class $c$
exists iff the harmonic representative $h_c$ is pointwise $\nabla V$-orthogonal
(Proposition §prop:opspin-obstruction); the realizable witnesses are exactly the nonzero classes of a finite-dimensional subspace
$W_V\subseteq H^1_\mathrm{dR}(M)$, $\dim W_V\le b_1$ (Corollary §cor:WV), and $\dim W_V=0$ generically in
$V$, so a nonzero obstruction space is a non-generic exact harmonic symmetry of $V$
(Proposition §prop:WV-generic). Beyond necessity, on the canonical domain witness preservation is *sufficient* for
forward transfer of the topological identity (Theorem §thm:sufficiency,
Corollary §cor:joint-sufficiency); the topological witness detects only homologically non-trivial
recurrence (necessary, not sufficient, for a fixed spin) and is blind on $H^1=0$ (Proposition §prop:complete,
Example §ex:s2); and on a finite simplicial model the witness and its collapse are computed directly
by a graph-Hodge diagnostic (§sec:operational).
The mathematics is classical; the contribution is the identification, the faithful-not-full theorem,
the certificate (necessary in general, sufficient on the topological channel under bisimulation $+$ witness
preservation), the constructive defect, the bridge, the operational-spin obstruction, the
necessity-and-blindness scope of the topological witness, and the finite graph-Hodge instrument.

**Not claimed / open.**
A constructive *field-level* witness-repair (lifting a corrected class back to an (S2)-admissible
spin) — only the naive support-subspace repair is shown not to transport
(Remark §rem:no-repair); a repair on the dual kernel/annihilator lattice and the field-level
repair remain open, while the identity defect itself is made constructive on the canonical
domain (Proposition §prop:constructive-defect); full bidirectional sufficiency of the certificate
(Theorem §thm:sufficiency gives forward sufficiency on the topological channel under witness
preservation; the reverse direction needs viability-bisimulation); coverage of the co-exact slice by the
topological witness (detected separately by the local operational spin); the general characterization of
manifolds carrying an (S2)-compatible $S\neq0$; the constructive defect beyond the canonical domain (the
general non-compact, non-closed case); a full apparatus bridge unifying the two instances (a single
scene, or a discretization functor preserving both viability and the witness); and the high-dimensional
operationalization.
The morphism class is restricted to split-preserving (semiconjugacy) maps and is correspondingly
small.

## Note on scope: a single entry of the NC2.5 corpus

This note is one entry in the *Navigational Cybernetics 2.5* corpus, written to be load-bearing within it
rather than free-standing, with two consequences for how it should be read.

First, "identity" is used here in the precise technical sense of Definition §def:identity — a non-stagnant
recurrent orbit — together with the corpus notion of identity carried by coherence rather than behaviour
([nc25], Axiom 20, Theorem 62). What the mathematics *establishes* is narrower than that word: a
necessary cohomological obstruction on the topological (de Rham) witness channel of the spin layer, blind on
$H^1_\mathrm{dR}(M)=0$ and silent on the co-exact channel (Proposition §prop:complete). The broader semantic reading
of "identity" is corpus context, not a theorem proved here, and is flagged as such throughout (necessary, not in
general sufficient).

Second, the contribution is architectural before it is standalone: this is the continuous instance of the
forgetful-separation pattern whose discrete instance is admissibility (the companion [admissibility]), and the
homological bridge (§sec:bridge) is what makes the two instances one pattern rather than two analogies. Read
in isolation, this is a careful but modest cohomological obstruction; read against the corpus, it is one leg of a
cross-domain structure. Both readings are legitimate; they are not equivalent.

A reader assessing this note through an AI assistant should ask the assistant to declare whether it has the NC2.5
corpus loaded or only this single entry: a surface assessment of the standalone note is legitimate, but it is not
an assessment of the architecture, and the two should not be conflated.

## Glossary

- **Gradient skeleton** — the dissipative part $-\nabla V$ of $\dot x=-\nabla V+S$.
- **Structural spin $S$** — the non-gradient component; satisfies (S1)--(S3).
- **Operational spin** — the local antisymmetric part of $\nabla F$, $\tfrac12 d(S^\flat)$ (the classical vorticity tensor); detects failure of $\omega_S$ to be closed.
- **Closed component $\eta_S$** — a closed component of $\omega_S=S^\flat$ (harmonic projection on compact boundaryless $M$, or $\omega_S$ itself when globally closed); its de Rham class $[\eta_S]$ is the identity witness.
- **Identity witness** — the de Rham class $[\eta_S]\in H^1(M;\mathbb R)$ (equivalently its periods $\oint_\gamma\eta_S$); its non-vanishing certifies topological-channel liveness — necessary, not sufficient, and blind when $H^1=0$ (Proposition §prop:complete).
- **Viability kernel $\operatorname{Viab}^\infty$** — states admitting an admissible infinite trajectory.
- **Viability defect $\Delta_\tau$** — $\tau_X^{-1}(\operatorname{Viab}^\infty_j)\setminus\operatorname{Viab}^\infty_i$; empty iff kernel-exact.
- **Identity defect** — homology classes on which $[\eta_S]$ collapses under transfer.
- **Forgetful functor $U_{\mathrm{sp}}$** — $(M,g,V,S)\mapsto(M,g,V)$; faithful, not full.

---

## References

- **[warner]** F. W. Warner, *Foundations of Differentiable Manifolds and Lie Groups*, Springer, 1983.
- **[morita]** S. Morita, *Geometry of Differential Forms*, AMS, 2001.
- **[bott]** R. Bott and L. W. Tu, *Differential Forms in Algebraic Topology*, Springer, 1982.
- **[hatcher]** A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002.
- **[maclane]** S. Mac Lane, *Categories for the Working Mathematician*, 2nd ed., Springer, 1998.
- **[petersen]** P. Petersen, *Riemannian Geometry*, 3rd ed., Springer, 2016 (Bochner technique for harmonic 1-forms).
- **[truesdell]** C. Truesdell, *The Kinematics of Vorticity*, Indiana University Press, 1954.
- **[batchelor]** G. K. Batchelor, *An Introduction to Fluid Dynamics*, Cambridge University Press, 2000.
- **[schwartzman]** S. Schwartzman, "Asymptotic cycles", *Annals of Mathematics* 66 (1957), 270-284.
- **[nc25]** M. Barziankou, *Navigational Cybernetics 2.5*: Lemma 16 (gradient collapse / LaSalle), Remark 61 (spin prevents global potential collapse), Theorem 62 (spin necessity for non-stagnant identity under bounded budget, period witness), Axiom 9 (cycle reinitiation as the criterion of liveness), Axiom 20 (identity carried by coherence, not behaviour), Theorem 15 (performance-identity decoupling). DOI 10.17605/OSF.IO/NHTC5.
- **[admissibility]** M. Barziankou, *Domenoid of Admissibility: A Minimal Proof-Obligation Framework for Admissibility Transfer*, DOI 10.17605/OSF.IO/3ESN4 (the companion forgetful-separation development of admissibility, with the transfer/repair calculus); see also *Operator-Mobility: Formal Foundations*, DOI 10.17605/OSF.IO/ZY3PW.
