# When Agreement Means Something: Regime Isolation and Evidence-Bound Synthesis in Multi-Interpreter Knowledge Systems

**Maksim Barziankou (MxBv)**
PETRONUS™ — petronus.eu
research@petronus.eu
March 2026

**DOI (parent framework):** 10.17605/OSF.IO/NHTC5
**License:** CC BY-NC-ND 4.0

*Implementation details are patent pending.*

---

## Abstract

This paper presents an architectural framework for answering domain-expert queries against a knowledge corpus using a plurality of computationally independent interpretation agents operating under regime isolation. The architecture is distinguished from existing retrieval-augmented generation (RAG), multi-agent debate, and ensemble methods by three jointly necessary properties: (1) evidence-bound structural synthesis, in which answer confidence is derived from cross-interpreter agreement on shared corpus evidence rather than from model-internal probability scores or text-level similarity; (2) divergence as a first-class output, in which contradictory interpretations of the same corpus passage produce a structural ambiguity report rather than a forced consensus; and (3) regime isolation enforced as an epistemic precondition, not an implementation preference, preventing the collapse of independent structural observation into social convergence. The architecture is a structure-revealing system, not a decision system: it characterizes the epistemic state of a corpus relative to a query without selecting or ranking answers. The paper formally specifies the architectural invariants, the synthesis classification logic, the epistemic class definition, and the relationship to the Navigational Cybernetics 2.5 formal framework.

---

## 1. Introduction

The problem of answering expert-level questions against a domain corpus is typically addressed through retrieval-augmented generation (RAG) [Lewis et al., 2020]: a single language model retrieves relevant passages via vector similarity search, then generates an answer conditioned on the retrieved context. This approach has a fundamental limitation: the answer reflects one model's interpretation, with no mechanism for determining whether that interpretation is structurally consistent with the corpus.

Multi-agent debate systems [Du et al., 2023; Chan et al., 2023] address this by allowing multiple models to interact. However, these systems introduce feedback loops: Agent B sees Agent A's output, adjusts, and converges. This transforms independent structural observation into social convergence. Agreement in such systems is evidence that agents influenced each other — not evidence that the corpus structurally supports a particular reading. Research has shown that multi-agent debate can amplify rather than correct errors when agents share training priors [Xu et al., 2023], and that persuasion dynamics within debate can drive agents toward confident but incorrect consensus [Liang et al., 2023].

Ensemble methods aggregate outputs through voting or averaging [Wang et al., 2022]. They improve statistical robustness but aggregate answers without evidence provenance: they determine which answer is most frequent, not which answer is best supported by specific corpus passages. Multiple models may agree on an incorrect answer when they share training-distribution biases [Turpin et al., 2023].

The present architecture departs from all three paradigms categorically. Prior art systems conflate two functions: the production of an epistemic topology characterizing how a corpus structures available evidence under a query, and the downstream selection of an answer from that topology. The present architecture separates these functions. It produces the topology and terminates. This is not a relocation of the decision — it is a structural decoupling that makes the epistemic basis of any downstream decision auditable, versioned, and independent of any single model's preferences.

---

## 2. Architectural Overview

The system comprises seven layers operating as an integrated mechanism.

**Layer 1 — Corpus Ingestion and Structural Extraction.** The system receives a domain knowledge corpus and produces a structural representation comprising: extracted claims classified by type (definitional, differentiating, mechanistic, independence confirmation, load-bearing assumption, structural consequence), defined terms with canonical identifiers, dependency relationships between claims, and evidence structures linking claims to source passages. This layer generates an immutable Corpus Passport: a SHA-256 fingerprint of the corpus version. The Corpus Passport binds all subsequent operations to this specific corpus state.

**Layer 2 — Query Decomposition.** The system receives a natural-language user query and decomposes it into structural sub-queries aligned with the corpus's claim and term structure. The output is a Retrieval Package: a structured specification of corpus passages, claims, and context to be delivered to each interpretation agent.

**Layer 3 — Regime-Isolated Interpretation.** A minimum of three interpretation agents, drawn from at least two distinct model families, each execute in a mutually isolated runtime environment. No agent receives any other agent's output. Each agent produces an Interpretation Report comprising: a direct answer with corpus evidence citations, a confidence assessment, identified ambiguities, and alternative interpretations where the evidence supports multiple readings.

**Layer 4 — Evidence-Bound Structural Synthesis.** The synthesis engine receives all Interpretation Reports and performs evidence-bound agreement classification. Detailed in Section 3.

**Layer 5 — Structural Confidence Scoring.** Answer confidence is derived from the topology of cross-interpreter agreement on specific corpus evidence, not from any model's internal probability estimate. Detailed in Section 4.

**Layer 6 — Divergence Output.** When agents produce contradictory interpretations of the same corpus evidence, the system produces a first-class Divergence Report. Detailed in Section 5.

**Layer 7 — Cryptographic Integrity.** Every output is cryptographically bound to the Corpus Passport. Corpus modification version-locks all prior outputs: they retain process validity for the corpus version against which they were generated, but are not authoritative for any subsequent version.

---

## 3. Evidence-Bound Structural Synthesis

### 3.1 The Problem with Text-Level Agreement

Existing aggregation methods operate on the text of the answer. But textual agreement is not structural agreement. Two models may produce identical text for entirely different reasons: one may have found the relevant passage, while the other hallucinated a plausible-sounding answer [Maynez et al., 2020]. The present architecture addresses this by operating on corpus evidence references, not on answer text.

### 3.2 Three-Category Classification

**Overlap.** Agents are in overlap if and only if their findings cite at least one common corpus passage AND arrive at structurally compatible conclusions about that passage. Overlap is evidence of structural transmission — the corpus passage was independently read by isolated agents and produced consistent interpretation. The synthesis engine performs no aggregation, voting, averaging, or learned combination of agent outputs.

**Unique.** An agent produces a finding with evidence references not cited by any other agent. The finding may be correct but cannot be structurally confirmed from cross-interpreter agreement alone.

**Divergence.** Two or more agents cite the same corpus passage but arrive at contradictory conclusions. Divergence is not an error. It is a structural finding indicating that the corpus passage admits multiple interpretations under the current query conditions.

### 3.3 Formal Specification

Let I = {I₁, ..., Iₙ} be the set of interpretation agents, n ≥ 3 (hard minimum; two-agent sessions are non-conformant because a 1-to-1 divergence produces no topological signal for structural confidence computation).

Let Fᵢ be the set of findings produced by agent Iᵢ. Let E(f) denote the set of corpus evidence references cited by finding f.

Two findings fᵢ and fₖ are in **evidence-overlap** iff E(fᵢ) ∩ E(fₖ) ≠ ∅ and Conclusion(fᵢ) ≅ Conclusion(fₖ), where ≅ denotes structural compatibility.

Two findings are in **evidence-divergence** iff E(fᵢ) ∩ E(fₖ) ≠ ∅ and Conclusion(fᵢ) ⊥ Conclusion(fₖ), where ⊥ denotes structural contradiction.

A finding fᵢ is **unique** iff for all k ≠ i: E(fᵢ) ∩ E(fₖ) = ∅.

This three-way classification constitutes the synthesis output. The system output is not an answer extracted from the agent pool: it is a structural characterization of the corpus's epistemic state relative to the query.

### 3.4 New Signal Category: Corpus-Induced Convergence Under Isolation

The present architecture introduces a signal distinct from existing AI confidence signals (model-internal probability, reward, loss, ensemble uncertainty [Guo et al., 2017]): **corpus-induced convergence under isolation** — the probability that independent agents, operating without knowledge of each other's outputs, cite the same corpus passage and arrive at compatible conclusions about it.

This probability is a property of the corpus structure, not of any agent. It cannot be computed by a single model, cannot be estimated from model logits, and cannot be approximated by ensemble aggregation. The principle is analogous to independent replication in empirical science [Ioannidis, 2005]: a finding is considered robust not when one observer reports it confidently, but when multiple independent observers report it from the same evidence. The present architecture operationalizes this principle at the architectural level.

---

## 4. Structural Confidence from Agreement Topology

Answer confidence is computed from the agreement topology:

**Confidence(claim) = f(N_overlap, N_total, E_specificity, D_divergence)**

Where N_overlap is the number of agents producing overlapping findings; N_total is the total agents; E_specificity is the specificity of shared evidence (passage-level citation > document-level); D_divergence is the divergence penalty.

The Structural Confidence Score is not a standalone output. It is valid only when presented as an atomic unit with the full synthesis topology: the overlap finding set, the unique finding set, the divergence finding set. The score is a property of the corpus epistemic state, not a quality ranking of agents or answers.

A critical property: unanimous overlap with zero unique findings is treated as a potential correlated-bias indicator, not as a maximum-confidence result. In practice, genuine structural transmission from a complex corpus almost always produces some unique findings [consistent with diversity-of-thought findings in collective intelligence literature, cf. Page, 2007]. Full unanimous overlap with zero unique findings may indicate that agents are reproducing a shared prior rather than independently reading the corpus.

---

## 5. Divergence as a First-Class Output

### 5.1 Divergence Taxonomy

Divergence findings are classified into four types:

**Corpus Ambiguity.** Agents cite the same passage and arrive at contradictory conclusions because the passage admits multiple valid readings. Primary diagnostic use case. Recommended downstream action: human expert review.

**Logical Contradiction.** One agent's conclusion directly negates the other's on the same factual claim. Signals internal inconsistency in the corpus. Recommended action: corpus correction.

**Scope Mismatch.** Agents cite the same passage but answer different implicit sub-questions. Signals that query decomposition may need refinement.

**Temporal Conflict.** Agents cite different versions of the same passage because the corpus contains superseded and current versions. Recommended action: corpus versioning.

Each Divergence Report declares the divergence type as a structured field. Downstream applications must not treat all divergence types equivalently.

### 5.2 Epistemic Value of Divergence

The Divergence Report is information the user cannot obtain from any single-model system (which always produces one answer) or multi-agent debate system (which drives agents toward consensus even when the corpus is genuinely ambiguous [Du et al., 2023]). The present architecture is a distinct architectural class in which the design goal is to surface disagreement rather than to suppress it. This is not an incremental improvement over prior art — it is an inversion of the design objective.

---

## 6. Regime Isolation: Formal Basis

### 6.1 Isolation Contract

Each interpretation agent operates under the following prohibitions:

- (i) No agent receives any other agent's output, intermediate or final.
- (ii) No agent receives feedback from the synthesis engine or any downstream component.
- (iii) No agent receives information about the number, identity, or model type of other agents.
- (iv) No agent's output is fed back to any agent, used to modify the corpus, or exposed to any other agent.
- (v) Violation of any isolation condition invalidates the consultation session.

### 6.2 Why Isolation is Necessary — and What It Does Not Guarantee

The epistemic argument: under isolation, P(B agrees with A | corpus) reflects the corpus's structural properties. Without isolation, P(B agrees with A | corpus, A's output) reflects both the corpus and A's influence. These are different probability measures. Only the first supports structural confidence claims about the corpus.

The independence guaranteed here is defined at the level of **generation paths**, not at the level of input data. Shared input data does not violate this independence condition — two agents reading the same corpus passage are analogous to two scientists reading the same paper [Collins, 1985]. What destroys independence is causal coupling of the generative processes. The Isolation Contract prohibits this causal coupling.

Isolation does not eliminate shared training bias [Bommasani et al., 2021]. Models trained on overlapping corpora may produce correlated errors independent of inter-agent communication. The architecture mitigates this through heterogeneous model family selection (Section 13.1), but does not claim to eliminate this risk entirely.

### 6.3 Relationship to NC2.5 Formal Framework

The isolation protocol derives from the Navigational Cybernetics 2.5 (NC2.5) formal framework [Barziankou, 2025–2026], specifically:

- **Axiom 15** (Causal Observation Distorts): The moment an observation enters causal pathways, it ceases to function as observation and becomes control.
- **Axiom 22** (Non-Causal Observational Dimension Required): Any long-horizon adaptive system requires an architecturally independent observation function that does not participate in the action domain.
- **Theorems 36–37** (Non-Causal Witnessing): Gate architecture produces non-causal witnessing of structurally relevant information independent of the optimization loop.
- **Theorem 67** (Coordination Enforcement): Runtime enforcement of multi-agent coordination requires a non-participant, architecturally independent function.

---

## 7. Architectural Invariants

**Invariant 1 — Interpreter Regime Isolation.** Each interpretation agent operates in a mutually isolated runtime environment. Violation invalidates the session. Agents must be drawn from at least two distinct model families with different training distributions and architectural lineages.

**Invariant 2 — Evidence-Bound Synthesis.** Agreement classification occurs only when evidence references overlap. The synthesis engine performs no aggregation, voting, or learned combination. It does not perform output selection.

**Invariant 3 — Divergence as Signal.** Contradictory findings on the same corpus evidence produce a typed Divergence Report, not a selected interpretation.

**Invariant 4 — Corpus Passport Binding.** All outputs are cryptographically bound to a specific corpus version. Corpus modification version-locks prior outputs.

**Invariant 5 — Model-Agnostic Intelligence.** System intelligence resides in the architecture, not in any specific interpretation model. Models are interchangeable without loss of system intelligence.

---

## 8. Epistemic Class Definition

### 8.1 Structure-Revealing vs. Decision System

The present architecture is a **structure-revealing system**, not a decision system. A decision system computes or selects an answer. The present architecture characterizes the epistemic state of a corpus with respect to a query: which claims the corpus structurally supports under independent interpretation, which claims it leaves unconfirmed, and which passages it leaves ambiguous.

System validity is a property of the process — whether isolation was maintained, whether evidence provenance was correctly classified, whether divergence was surfaced — not a property of any answer derived from the output.

The present architecture does not improve answer quality. It alters the epistemic structure of the output space. Systems that improve answer quality operate on a shared output space in which a correct answer exists and the goal is to approach it. The present architecture operates on a different space: one in which the output is the topology of agreement and disagreement under independence constraints, and in which no single correct answer is defined or targeted.

### 8.2 Process Validity vs. Factual Truth

The architecture guarantees **process validity**, not factual truth. Process validity is the property that isolation was maintained and evidence-bound synthesis was executed correctly. Factual truth is the property that the claims in the corpus are objectively correct in the world. These are independent properties.

A corpus containing a factual error may produce high structural confidence if all independent agents consistently extract the same error from the same passage. The system is a structural transmission verifier, not a fact-checking system [consistent with the distinction between formal verification and empirical validation in software engineering, cf. Clarke et al., 1999].

### 8.3 Architectural Class Boundaries

The architecture defines a class characterized by three jointly necessary properties: (1) constraint on information flow between agents as an epistemic precondition; (2) measurement of corpus-induced convergence rather than answer-level consensus; (3) process validity as the primary output. Prior art systems we are aware of do not simultaneously satisfy all three properties.

An ensemble system without communication satisfies property (1) but not (2) or (3): it aggregates outputs rather than measuring evidence provenance, and produces a selected answer. A self-consistency system [Wang et al., 2022] satisfies property (1) but not (2) or (3): it measures text-level agreement rather than shared evidence provenance. A RAG system [Lewis et al., 2020] satisfies none of the three.

---

## 9. Dual-Mode Architecture

**Mode 1 — Verification.** The user uploads their own corpus. Interpretation agents assess structural coherence, claim consistency, and dependency integrity. Output: a coherence map.

**Mode 2 — Expert Consultation.** The user submits a query against an expert corpus. Interpretation agents consult the corpus to answer the question. Output: a structural topology with confidence scores, evidence citations, and typed divergence reports.

Both modes use the same regime isolation protocol, synthesis engine, and corpus passport mechanism. They maintain strict state isolation and do not share session state or cached synthesis outputs.

---

## 10. Comparison with Prior Art

| Feature | RAG | Multi-Agent Debate | Ensemble / Self-Consistency | Present Architecture |
|---|---|---|---|---|
| Interpreter isolation | N/A (single model) | No (feedback loops) | Partial | Yes (epistemic precondition) |
| Evidence-bound synthesis | No | No | No | Yes |
| Divergence as output | No | No (forces consensus) | No (majority vote) | Yes (first-class, typed) |
| Answer selection | Yes | Yes (consensus) | Yes (vote) | No (topology only) |
| Corpus passport binding | No | No | No | Yes |
| Model-agnostic intelligence | No | Partial | Partial | Yes |
| Structural confidence | No (probability) | No (consensus score) | No (vote count) | Yes (agreement topology) |
| Process validity guarantee | No | No | No | Yes |

---

## 11. Falsifiability and Empirical Surface

The architecture makes four testable predictions:

1. **Structural confidence vs. model probability.** For queries where the corpus is genuinely ambiguous, the architecture should produce divergence reports while single-model systems produce high-confidence single answers. Testable by constructing corpora with known ambiguities [cf. methodology in Min et al., 2023].

2. **Isolation effect on agreement quality.** Agreement under regime isolation should correlate more strongly with corpus structural properties than agreement under debate conditions. Testable by running identical query/corpus pairs under isolated and non-isolated conditions.

3. **Model substitution invariance.** Replacing interpretation models while holding corpus and query constant should produce structurally similar synthesis topologies. Significant sensitivity to model identity would indicate that system intelligence is not fully architecture-resident.

4. **Correlated bias detection.** For queries where homogeneous-family agents produce unanimous overlap but heterogeneous-family agents produce divergence, the architecture should flag the homogeneous result as a potential correlated-bias indicator.

---

## 12. Limitations and Open Questions

### 12.1 Correlated Interpretation Bias

Regime isolation eliminates inter-agent influence. It does not eliminate shared training bias [Bommasani et al., 2021; Bender et al., 2021]. Models trained on overlapping corpora may independently produce the same incorrect reading of a correctly-cited passage.

Three architectural mitigations are required:

**Mitigation 1 — Heterogeneous Model Families (Required).** Agents must be drawn from at least two distinct model families with different training distributions and architectural lineages. Overlap across heterogeneous families is stronger evidence of structural transmission than overlap within one family. A session using multiple instances of the same model provides no meaningful structural confidence regardless of isolation. This follows from the general principle that independence of observers is a precondition for evidential strength of agreement [Pearl, 2009].

**Mitigation 2 — Retrieval Diversity.** Enhanced configurations provide independent retrieval paths per agent, reducing shared retrieval blind spots. Recommended for high-stakes consultation.

**Mitigation 3 — Correlated-Bias Detection via Unique Findings Topology.** Full unanimous overlap with zero unique findings is flagged as a potential correlated-bias indicator rather than maximum confidence. Genuine structural transmission from complex corpora almost always produces some unique findings.

### 12.2 General Limitations

(a) Corpus quality — the system faithfully reports what the corpus says, including errors; (b) query-corpus mismatch — the system can detect evidence insufficiency but cannot generate knowledge absent from the corpus; (c) computational cost — running multiple isolated agents per query is more expensive than a single RAG call [cf. cost analysis in Yoran et al., 2023]; (d) structural extraction quality — utility depends on the quality of corpus ingestion and structural representation.

### 12.3 Open Questions

The relationship between interpreter count and synthesis topology reliability is an open empirical question. The minimum conformant count is n ≥ 3; optimal configurations likely depend on corpus complexity and query type. The quantitative effect of model family heterogeneity on correlated-bias reduction requires systematic empirical study.

---

## References

Barziankou, M. (2025–2026). Navigational Cybernetics 2.5: An architectural theory in which drift, rather than equilibrium, is the primary medium of existence, v2.1. DOI: 10.17605/OSF.IO/NHTC5.

Barziankou, M. (2026). ECR-VP: Epistemic Coherence Review and Verification Protocol, v1.0. PETRONUS.

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? In *Proceedings of FAccT 2021*.

Bommasani, R., et al. (2021). On the opportunities and risks of foundation models. *arXiv:2108.07258*.

Chan, C. M., et al. (2023). ChatEval: Towards better LLM-based evaluators through multi-agent debate. *arXiv:2308.07201*.

Clarke, E. M., Grumberg, O., & Peled, D. A. (1999). *Model Checking*. MIT Press.

Collins, H. M. (1985). *Changing Order: Replication and Induction in Scientific Practice*. University of Chicago Press.

Du, Y., Li, S., Torralba, A., Tenenbaum, J. B., & Mordatch, I. (2023). Improving factuality and reasoning in language models through multiagent debate. *arXiv:2305.14325*.

Guo, C., Pleiss, G., Sun, Y., & Weinberger, K. Q. (2017). On calibration of modern neural networks. In *Proceedings of ICML 2017*.

Ioannidis, J. P. A. (2005). Why most published research findings are false. *PLoS Medicine, 2*(8), e124.

Lewis, P., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. In *Advances in Neural Information Processing Systems (NeurIPS 2020)*.

Liang, T., et al. (2023). Encouraging divergent thinking in large language models through multi-agent debate. *arXiv:2305.19118*.

Maynez, J., Narayan, S., Bohnet, B., & McDonald, R. (2020). On faithfulness and factuality in abstractive summarization. In *Proceedings of ACL 2020*.

Min, S., et al. (2023). FActScore: Fine-grained atomic evaluation of factual precision in long form text generation. *arXiv:2305.14251*.

Page, S. E. (2007). *The Difference: How the Power of Diversity Creates Better Groups, Firms, Schools, and Societies*. Princeton University Press.

Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.

Turpin, M., Michael, J., Perez, E., & Bowman, S. R. (2023). Language models don't always say what they think: Unfaithful explanations in chain-of-thought prompting. *arXiv:2305.04388*.

Wang, X., et al. (2022). Self-consistency improves chain of thought reasoning in language models. *arXiv:2203.11171*.

Xu, Z., et al. (2023). Critical evaluation of multi-agent debate as a solution for LLM hallucination. *arXiv:2311.08163*.

Yoran, O., Wolfson, T., Ram, O., & Berant, J. (2023). Making retrieval-augmented language models robust to irrelevant context. *arXiv:2310.01558*.

---

*© 2025–2026 Maksim Barziankou. All rights reserved.*
*CC BY-NC-ND 4.0*
*PETRONUS™ — petronus.eu*
