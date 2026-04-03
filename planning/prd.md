---
stepsCompleted:
  - step-01-init
  - step-02-discovery
  - step-02b-vision
  - step-02c-executive-summary
  - step-03-success
  - step-04-journeys
  - step-05-domain
  - step-06-innovation
  - step-07-project-type
  - step-08-scoping
  - step-09-functional
  - step-10-nonfunctional
  - step-11-polish
  - step-12-complete
  - step-e-01-discovery
  - step-e-02-review
  - step-e-03-edit
inputDocuments:
  - _bmad-output/planning-artifacts/product-brief-Collab_Sim-2026-03-13.md
documentCounts:
  briefCount: 1
  researchCount: 0
  brainstormingCount: 0
  projectDocsCount: 0
workflowType: prd
workflow: edit
date: 2026-03-16
lastEdited: 2026-03-17
editHistory:
  - date: 2026-03-17
    changes: "Documented phased communication flow: Human <-> Lab Assistant baseline first, then agent-strata expansion with aligned journeys, requirements, NFR metrics, and traceability."
classification:
  projectType: desktop_app
  domain: "scientific + process_control"
  complexity: high
  projectContext: greenfield
  constraints:
    humanVrFpsTarget: ">=90"
    aiPovFpsTarget: "1"
    performanceStack: "SteamVR + UPBGE"
---

# Product Requirements Document - Collab_Sim

**Author:** Dr Carroll
**Date:** 2026-03-13

## Executive Summary

`Collab_Sim` is a high-complexity, greenfield desktop VR platform built on `UPBGE` and `SteamVR` that enables spatially grounded collaboration between human and AI participants. It addresses a core failure mode in technical and operational decision-making: teams currently rely on abstract text and voice exchanges instead of co-witnessed spatial context, which slows decisions, obscures root causes, and increases missed opportunities.

`Collab_Sim` can host a digital twin of a client's business and integrate real-time production-data-coupled analytics to optimize processes and procedures. It enables teams to evaluate proposed improvements virtually, observe operational and financial impact before physical installation, and perform zero-physical-risk pre-deployment validation. Human operators use immersive high-fidelity rendering (target `>=90 FPS`), while AI participants use lower-rate scene perception (`~1 FPS`) for grounded object-level reasoning and interaction.

Digital twin fidelity is engineered through CLG and field-team mesh model creation plus direct telemetry ingestion from client PLC production systems. Latency is treated by use case: highly constrained for real-time adjustment workflows and less restrictive for systemic design and optimization studies.

For communication design, MVP begins with a single baseline channel (`Human Supervisor <-> Lab Assistant`) to prove reliable collaboration and shared understanding before expanding communication responsibilities across additional agent strata.

### What Makes This Special

`Collab_Sim` shifts work from "talking about systems" to "witnessing and improving systems" through shared human-AI co-presence in the same scene. AI can point to concrete assembly or process dependencies, helping teams identify what must change and why.

The product follows a dual-use value arc:
- Phase 1: internal R&D acceleration tool
- Phase 2: client-facing sales and enablement environment demonstrating measurable operational improvement

It also creates a scalable proof-and-sales loop:
- CLG improves internal outcomes using `Collab_Sim`
- CLG clients use their own digital twins as sales tools to win their clients
- CLG uses those client outcomes as proof cases to acquire additional industrial clients

The user value is direct: stakeholders can query where operations "hurt," explore better margin paths, and witness validated improvements without stepping onto the factory floor.

## Project Classification

- **Project Type:** `desktop_app` (VR-first collaborative application)
- **Domain:** `scientific + process_control` (hybrid)
- **Complexity:** `high`
- **Project Context:** `greenfield`
- **Platform/Performance Constraints:**
  - Human VR rendering target: `>=90 FPS`
  - AI POV update rate: `~1 FPS`
  - Runtime stack: `SteamVR + UPBGE`

## Success Criteria

### User Success

1. Users identify at least one root-cause driver and one actionable improvement per completed mission session, as recorded in session outcome artifacts.
2. Human and AI participants reach shared understanding with post-session reviewer score `>=4.0/5.0`, and mission time-to-objective improves by `>=30%` versus the text/voice baseline.
3. Users validate improvement options in zero-physical-risk digital-twin scenarios with `100%` of deployment-impacting recommendations tagged with approval status (`draft`, `reviewed`, or `approved`) before export.

### Business Success

**3-Month Success**
- Complete at least one pilot use-case with a commercial manufacturing client and produce measurable before and after outcomes.

**12-Month Success**
- Convert pilots into paying integrations with at least 3 industrial clients.
- Establish `Collab_Sim` as a repeatable R&D-to-sales enablement offering in CLG's portfolio.

### Technical Success

1. **System stability:** each mission session can run up to 8 hours with zero unrecoverable failures during core workflows.
2. **Rapid model injection:** requested models spawn within `<3s` for simple assets and `<10s` for heavy assets under expected MVP conditions.
3. **Improvement-loop capability:** repeated simulate -> evaluate -> optimize cycles are executable and auditable, with complete cycle logs for `100%` of completed loops.
4. **Remote collaboration readiness:** remote client sessions meet communication targets (`<10s` fault detection, `<30s` recovery) while preserving session context and artifacts.

### Measurable Outcomes

- **Time-to-objective:** `>=30%` reduction versus text/manual baseline.
- **Pilot outcomes:** `>=1` documented pilot with quantified operational and financial impact within first 3-6 months.
- **Client adoption:** `>=3` industrial client integrations by month 12.
- **Win-case documentation:** target `>=3` published case studies in year 1.
- **Strategic growth indicators (aspirational):**
  - Government-contract adoption signal in year 1.
  - Enterprise valuation trajectory targeting potential `>$1B` offer within `<3` years.

## Product Scope

### MVP - Minimum Viable Product

- Deliver core collaborative VR workflow with Human Supervisor and Lab Assistant in-scene interaction as the baseline communication pair.
- Demonstrate with at least 2 active client environments.
- Support persistent save/resume and measurable session outcomes.
- Expand communication responsibilities through defined agent strata only after baseline collaboration metrics are met.

### Growth Features (Post-MVP)

- Continuous capability expansion based on pilot and client feedback.
- Enhanced remote collaboration and optimization workflows.
- Broader domain templates and reusable improvement-playbook automation.

### Vision (Future)

- `Collab_Sim` becomes a default industrial problem-solving interface for digital-twin decisioning.
- CLG scales a proof-and-sales ecosystem where clients use `Collab_Sim` to win their own clients.
- Company-level strategic outcome target includes acquisition/offering trajectory `>$1B` within 3 years.

## User Journeys

### Journey 0: Baseline Communication Flow - Human <-> Lab Assistant

**Opening Scene**  
The Human Supervisor (`H`) launches `Collab_Sim` from desktop, the application starts `SteamVR`, and `UPBGE` establishes VR runtime communication with the HMD. `H` enters a `100 ft x 100 ft` virtual lab with practical lighting, object shadows, a floor compass rose, and a `30 ft` north-wall status screen. Lab Assistant (`LA`) appears in-scene facing `H`, slightly left of the status screen.

**Rising Action**  
`H` and `LA` use a screen-first communication loop. Dialogue is shown as a scrollable color-coded conversation feed (`H=green`, `LA=blue`) in the left one-third of the status screen, and session history appears in the lower-left saved-session panel. `H` uses HMD microphone speech with silence detection (`1200ms`) to complete utterances. STT results appear in `1-2s`, and confidence below `0.85` requests confirmation before commit. `LA` starts the session with: "Hello Dr Carroll, I'm Mike your lab assistant. Would you like to begin this session from a previous save point in an existing session, or begin a new session using a freeflow conversation?" `H` can reply by voice and select saved sessions with laser and index-finger click confirmation.

**Climax**  
During active troubleshooting, `H` and `LA` jointly inspect and manipulate a gearbox scene. `LA` can request Model Manager support for candidate references, present numbered image options for verbal/laser selection, and inject generated geometry into the running scene. `H` can reposition parts in no-gravity mode, request dimension/spec edits (for example shaft-length changes), and use scaling mode to transform one or multiple selected parts with visual bounding-box handles and live `X/Y/Z` dimensions.

**Resolution**  
When `H` requests save or exits temporarily, `LA` coordinates with Site Manager to persist scene state exactly as-is, including object transforms, dialogue/event history, and timestamped artifacts. The dialogue/event log is durable (never cleared) and is loaded/saved with each scene file so the current scene always has synchronized historical context. During inactivity, the system follows staged idle handling (prompt, autosave, close) while applying dirty-state checks before save/close actions.

### Journey 1: Primary User (Dr Carroll) - Core Collaboration Success Path

**Opening Scene**  
Dr Carroll enters a live `Collab_Sim` session, loads an active project scene, and initiates collaboration with a designated AI partner (preferred: OpenClaw agent on local Mac mini network; fallback: alternate hosted collaborator AI profile).

**Rising Action**  
Dr Carroll asks targeted questions while jointly inspecting scene objects and context. The system streams low-rate imagery context (target 1-5 FPS for AI collaboration channels) and conversational context to the collaborator AI through configured communication pipelines.

**Climax**  
AI and human converge on a shared spatial understanding of the root issue and candidate improvements, with explicit object and process references visible in-scene.

**Resolution**  
Session outputs include validated insight, next-step decision, and persisted state/log artifacts that can be resumed or presented later.

### Journey 2: Primary User Edge Case - Communication Breakdown and Recovery

**Opening Scene**  
During active collaboration, a message from Dr Carroll or Site Manager AI is transmitted but not acknowledged.

**Rising Action**  
If no response occurs within `<10s`, `Collab_Sim` triggers alternate notification pathways to both collaborators indicating communication failure and active retry attempts.

**Climax**  
Site Manager autonomously detects duplex communication degradation and executes recovery protocol (channel failover, retry routing, status escalation).

**Resolution**  
Both collaborators regain synchronized communication state and continue session without losing task context.

### Journey 3: Admin/Operations Journey - Site Manager Oversight

**Opening Scene**  
Site Manager AI initializes session governance: participant state monitoring, duplex communication link checks, and orchestration readiness.

**Rising Action**  
Site Manager continuously monitors channel health, participant responsiveness, and session signaling integrity.

**Climax**  
On fault detection, Site Manager performs autonomous corrective actions and notifies affected participants with clear status and recovery state.

**Resolution**  
Session governance remains stable; orchestration continuity is preserved across communication interruptions.

### Journey 4: Support/Troubleshooting Journey - Continuous Reliability Assurance

**Opening Scene**  
System enters active operation with Site Manager as orchestrator and monitoring agent-controller.

**Rising Action**  
Site Manager provisions and supervises troubleshooting and monitoring agents responsible for detecting communication degradation and performance anomalies.

**Climax**  
A fault is detected (link instability, missed acknowledgments, channel interruption). Monitoring agents diagnose probable cause and return actionable status to Site Manager.

**Resolution**  
Site Manager applies recovery policy and restores session continuity; issue event is logged for post-session diagnostics and system hardening.

### Journey 5: Integration/API Journey - External Data Enablement

**Opening Scene**  
Before session start, integration operators configure required external data sources (historical production data, telemetry feeds, analytics inputs) for the specific project.

**Rising Action**  
`Collab_Sim` validates data-source connectivity, access permissions, and project binding so external production context is available during runtime.

**Climax**  
During the session, participants query and use historical and operational data to contextualize diagnosis and optimization decisions in-scene.

**Resolution**  
Session completes with traceable data-linked reasoning, and the configured data pathways remain reusable for future sessions.

### Journey 6: Remote Collaboration Readiness - Client Co-Session

**Opening Scene**  
A CLG engineer and remote client stakeholders join a supervised co-session to review a digital twin and run guided troubleshooting.

**Rising Action**  
Site Manager validates remote communication channels, participant status, and session permissions before mission start. The team performs shared object inspection, highlights, and evidence capture while maintaining communication continuity.

**Climax**  
A communication interruption occurs and is detected within `<10s`; Site Manager executes recovery workflow and restores active collaboration without losing mission context.

**Resolution**  
Session continues to objective completion with preserved artifacts, producing a client-ready summary and traceable evidence package.

### Journey Requirements Summary

These journeys reveal required capability areas:

- Baseline communication flow first (`Human Supervisor <-> Lab Assistant`), then staged expansion to Site Manager and supporting agent strata.
- AI collaborator topology management (local Mac mini agent vs alternate AI host profile)
- Real-time communication reliability with `<10s` no-response detection and recovery signaling
- Site Manager autonomy for orchestration, monitoring, and recovery
- Monitoring and troubleshooting agent framework with durable session-health supervision
- Pre-session integration pipeline for external production and historical data access
- Data-linked session traceability across communication, diagnostics, and decision outputs
- Remote collaboration readiness under supervised communication resilience and recovery

## Domain-Specific Requirements

### Compliance & Regulatory
- No formal external compliance framework is required for MVP.
- MVP prioritizes internal traceability through durable session logging.

### Technical Constraints
- Security minimum for MVP is durable logging of key events and interactions.
- Session reliability target is uninterrupted operation for up to 8 hours per session.
- Telemetry and rendering operational dependency is currently assumed to be handled by `SteamVR` and `UPBGE`.

### Integration Requirements
- MVP integration scope is limited to local storage and network-attached storage (NAS).
- No mandatory enterprise platform integrations (SCADA/MES/data lake) in MVP baseline.

### Functional Safety (Process Control Context)
- For MVP, Collab_Sim recommendations are simulation-only and require explicit human approval before any real-world execution.
- All session outputs that could influence plant changes must be tagged with approval status (`draft`, `reviewed`, `approved`) before export.

### OT Security Baseline (MVP)
- Session and command logs must capture authentication events, role changes, and privileged actions with immutable timestamps.
- Communication audit events must include at minimum: `message_sent`, `message_acknowledged`, `message_timeout`, `recovery_started`, and `recovery_restored`.
- Remote-session channels must use encrypted transport (TLS `1.2+`) in post-MVP releases before external-client production use.

### Process Control Operational Requirements
- Historical production data inputs used in-session must pass pre-session source validation checks before mission start.
- Any detected data-staleness or feed-discontinuity event must be surfaced on the session whiteboard and recorded in artifacts.

### Engineering Authority & Sign-Off
- Human Supervisor is the final authority for decisions and sign-off on any recommendation produced in session.
- Engineering sign-off records must include decision rationale, approving actor, and timestamp in session artifacts.

### Risk Mitigations
1. **Communication channel instability**
   - Mitigation: link-heartbeat monitoring, timeout detection, automatic retries, and fallback alert paths to participants.
2. **Model drift / model-reality divergence**
   - Mitigation: scheduled model validation checkpoints and controlled re-baseline before critical sessions.
3. **Telemetry dependency assumptions**
   - Mitigation: explicit telemetry validation tests at session start (data freshness, channel health, expected signal availability) before operational decisions.

## Innovation & Novel Patterns

### Detected Innovation Areas

- **Embodied AI collaboration in industrial digital twins:** Human and AI participants co-reason in shared spatial context rather than text-only interaction.
- **Duplex AI orchestration model:** Site Manager AI supervises communication resilience, monitoring, and autonomous recovery behavior.
- **R&D-to-sales conversion architecture:** The same operational environment used for internal optimization is reused as a client-facing proof and sales instrument.
- **Multi-rate cognition architecture:** Human immersive rendering (`>=90 FPS`) coexists with lower-rate AI scene perception (`~1 FPS`) while preserving collaborative utility.

### Market Context & Competitive Landscape

- Most existing industrial tools separate simulation, collaboration, and sales demonstration into different systems.
- `Collab_Sim`'s differentiation is integrated workflow continuity: diagnose -> optimize -> demonstrate -> sell inside one coherent environment.
- Competitive advantage is reinforced by customer-specific digital twins and direct telemetry-linked contextual reasoning.

### Validation Approach

- Validate collaboration efficacy via benchmark scenarios (time-to-objective, first-pass correctness, missed-fault reduction).
- Validate commercial value via pilot outcomes and documented win-cases tied to measurable operational and financial improvements.
- Validate communications resilience with timeout detection (`<10s`) and recovery success-rate metrics.
- Validate digital-twin trust through model and telemetry integrity checks before decision sessions.

### Risk Mitigation

- **Innovation adoption risk:** Start with constrained pilot scenarios and visible win-case documentation.
- **Technical trust risk:** Enforce pre-session model and telemetry validation checkpoints.
- **Over-automation risk:** Keep human supervisory control explicit while progressively expanding autonomous functions.
- **Scope inflation risk:** Maintain MVP boundaries and phase advanced capabilities into growth roadmap.

## Desktop App Specific Requirements

### Project-Type Overview

`Collab_Sim` is a Windows-first desktop VR application designed for high-fidelity simulation scenes with higher poly-count meshes and complex object density. MVP prioritizes hardware and runtime realism over cross-platform breadth.

### Technical Architecture Considerations

- **Platform Support (MVP):**
  - Windows-only for MVP due to GPU and performance requirements in high-fidelity VR scenarios.
- **VR Runtime Requirements:**
  - Fully operational VR capability for the human participant is mandatory in MVP.
  - Runtime dependency stack remains `SteamVR + UPBGE`.
- **3D authoring (offline):** **Blender `4.5.8` LTS** is the **standard** for modeling and editing Collab_Sim `.blend` / mesh content **before** or **between** sessions (see `architecture.md` toolchain notes). **UPBGE** remains the **in-session** runtime; exact **UPBGE** build is pinned separately from the **Blender** authoring version.
- **VR PC vs LLM hosting (MVP planning):**
  - The **VR PC** is the **designated host** for **headset rendering** and **in-session runtime / session management** tied to the immersive experience.
  - **LLM inference** may run **on the VR PC** or on a **separate computer or service**; **final standard topology is undecided** pending **initial performance testing** (VR frame rate + AI latency under realistic workloads).
  - Rationale: **VR and large local models** often **compete for GPU**; split hosting is a **first-class option**, not an afterthought.
- **Offline/Network Operation:**
  - Core sessions can operate without internet when AI agents are local on the same network.
  - Internet is optional for in-session augmentation tasks (for example, live web lookup of external references and images).
- **In-Session External Content:**
  - Internet-fetched assets should be displayable in-scene and persisted into session logs and artifacts.

### System Integration & Operational Workflow

- **Local Integration Baseline:**
  - Local storage and NAS access for project and session data.
  - Local-network AI agent interoperability (including collaborator and orchestration roles).
- **Systems Engineer Agent Loop:**
  - A dedicated systems-engineer AI ingests session logs (or listens in-session), captures enhancement requests, and prepares new capability increments.
  - New capability increments are validated in explicit system optimization and QA sessions before production promotion.

### Implementation Considerations

- **Update Model (MVP):**
  - No mandatory autonomous application auto-update requirement for MVP.
  - Improvement cadence is driven by the systems-engineer agent's log-informed enhancement pipeline plus human-in-the-loop QA validation.
- **Performance Positioning:**
  - Architecture decisions should preserve high-fidelity scene performance for human VR interaction while supporting auxiliary AI workflows and optional internet-assisted enrichment.

## Project Scoping & Phased Development

### MVP Strategy & Philosophy

**MVP Approach:** Problem-solving MVP focused on proving the core collaborative diagnosis and optimization loop.  
**Resource Requirements:** Lean, high-skill team centered on VR runtime engineering, AI orchestration, data integration, and QA operations.

### Governance Model (Critical)

- **Final Authority:** Human supervisor voice (Dr Carroll) is final in all matters.
- **Mission Authority:** Lab Assistant supervises objective execution and goal-based activities across sessions.
- **Operational Authority:** Site Manager supervises environment readiness, communication health, model/stage support, and operational continuity.
- **Dual Reporting Rule:** All agents align to mission goals under Lab Assistant while maintaining operational compliance under Site Manager.

### MVP Feature Set (Phase 1)

**Core User Journeys Supported:**
- Baseline Human Supervisor and Lab Assistant communication flow (`Journey 0`) for mission collaboration.
- In-room human and AI collaboration with mission-focused session execution.
- Communication failure detection and recovery (`<10s` no-response awareness).
- Persistent session save/resume and traceable decision logs.

**Must-Have Capabilities:**
- Windows-first VR runtime (`SteamVR + UPBGE`) with human VR performance target (`>=90 FPS`).
- In-scene AI collaborator using Lab Assistant peer model.
- Site Manager operational orchestration and duplex communication resilience.
- Local/NAS-backed data access and session artifacts.
- Basic digital twin loading and historical production context support.
- Mission task roster capture across sessions (secretary-of-work function).

**Communication Strata Rollout:**
- **Strata 1 (MVP baseline):** Human Supervisor <-> Lab Assistant
- **Strata 2 (MVP hardening):** Site Manager oversight and recovery workflows around baseline collaboration
- **Strata 3 (Post-MVP):** Monitoring/Troubleshooting and domain-specialist agent collaboration pathways

### Post-MVP Features

**Phase 2 (Growth):**
- Research Agent for long-horizon out-of-session investigation and evidence packets.
- Expanded remote client session operations and richer integrations.
- Systems-engineer agent improvement loop with structured QA promotion workflows.

**Phase 3 (Expansion):**
- Broader domain scaling and enterprise/government hardening.
- Advanced autonomy under explicit human final-authority safeguards.
- Scalable proof-to-sales flywheel across multi-client ecosystems.

### Risk Mitigation Strategy

**Technical Risks:**  
Communication instability, model drift, and telemetry assumptions are addressed with heartbeat monitoring, validation gates, and controlled re-baselining.

**Market Risks:**  
Adoption risk is reduced through pilot-first proof with measurable outcomes and reusable win cases.

**Resource Risks:**  
Scope overload is mitigated through strict MVP boundary enforcement, phased capability release, and human-prioritized decision authority.

## Agent Operating Model

### Authority Hierarchy

- **Human Supervisor (Dr Carroll):** final authority in all matters.
- **Lab Assistant:** mission authority (session objectives and goal execution).
- **Site Manager:** operational authority (environment readiness, communication health, continuity).
- **Dual reporting:** all agents align to mission direction from Lab Assistant and operational constraints from Site Manager.

### Communication Flow Strata (Execution Order)

1. **Strata 1 - Baseline Collaboration**
   - Active pair: Human Supervisor <-> Lab Assistant
   - Purpose: prove mission collaboration speed and understanding quality before adding orchestration complexity.
2. **Strata 2 - Operational Oversight**
   - Active roles: Human Supervisor <-> Lab Assistant, supervised by Site Manager
   - Purpose: add reliability controls and recovery management around baseline exchanges.
3. **Strata 3 - Extended Agent Ecosystem**
   - Active roles: add Monitoring/Troubleshooting, Domain Assistant, and other support agents as needed
   - Purpose: scale collaboration depth while preserving baseline flow guarantees.

### Communication State Ownership

- **Baseline exchange state ownership:** Lab Assistant maintains conversational continuity and mission context.
- **Fault and recovery state ownership:** Site Manager owns timeout detection, recovery initiation, and recovery status reporting.
- **Final decision state ownership:** Human Supervisor retains final authority on acceptance and follow-on actions.

### Telemetry Model

- **Spatial telemetry:** VR scene and interaction state.
- **Process telemetry:** progress signals for reasoning and problem-solving workflow.
- **Temporal telemetry:** timing and continuity signals (timeouts, stalls, dropped responses).
- **Industrial telemetry:** external production system signals.

**MVP constraint:** historical industrial data only (no live industrial telemetry analysis in MVP).

### Core Agents and Duties

1. **Human Supervisor**
   - Final decision authority; can override any agent behavior/output.
   - Can change/fork session objectives and approve critical transitions.

2. **Lab Assistant (in-room collaborator)**
   - Persistent peer collaborator and mission supervisor.
   - Maintains objective focus; captures task roster and forked objectives.
   - Recommends prior successful methods from cross-session memory.

3. **Site Manager**
   - Supervises operational session readiness and communication stability.
   - Detects communication failures and coordinates recovery actions.
   - Reports communication inadequacy statistics to human supervisor.

4. **Model Manager**
   - Maintains model repository and scene injection pipeline.
   - Controls model lifecycle authority boundaries (scene usage vs repository operations).

5. **Systems Manager**
   - Maintains platform integrity, revisions, and operational integration pathways.
   - Supports long-term system evolution and environment-level service operations.

6. **Research Agent (asynchronous)**
   - Performs long-horizon research tasks between sessions.
   - Produces objective-aligned evidence packets for future session preload.
   - Works under Human + Lab Assistant mission direction.

7. **Domain Assistant(s)**
   - Provides on-demand specialist support for active scenario domains.
   - Performs domain-specific data preparation/cleaning when required.
   - Works under Human + Lab Assistant mission direction.

### Supporting Agents

8. **Monitoring/Troubleshooting Agent(s)**
   - Operate under Site Manager for health monitoring and fault diagnostics.
   - Feed actionable recovery data to Site Manager.

9. **Systems Engineer Agent**
   - Converts session-derived improvement requests into candidate increments.
   - Stages increments for optimization/QA sessions before release approval.

### Optional Agents (Context-Dependent)

10. **Data Steward Agent**
   - Data lineage, provenance, trust labels, and retention governance.

11. **Knowledge Librarian Agent**
   - Curates win-cases, playbooks, and reusable methods across sessions.

12. **Experiment Designer Agent** (rare-use)
   - Designs controlled what-if experiments and reproducibility structure.

### Session Rules of Engagement

- Collab-Sim rules apply to VR sessions.
- Real-world follow-on actions are at Human Supervisor discretion.
- If key collaborator communication fails, Site Manager coordinates recovery and notifies participants.
- If key agent outage persists, Human chooses to continue solo or save session state for recovery follow-on.

### Handoff Rules

- **Mission changes/forks:** Human -> Lab Assistant -> relevant agents.
- **Operational incidents:** Site Manager leads recovery; Lab Assistant maintains mission continuity.
- **Specialized technical escalation:** Lab Assistant -> Domain Assistant and/or Research Agent.
- **Model operations:** Human/Lab Assistant -> Model Manager.
- **Platform improvement requests:** Lab Assistant/Systems Engineer -> optimization + QA -> Human approval.

## Functional Requirements

### Session Governance & Agent Authority

- FR1: Human Supervisor can override any agent decision at any time during a session.
- FR2: Lab Assistant can supervise mission-level activities across active sessions.
- FR3: Site Manager can supervise operational and session-environment readiness and continuity.
- FR4: Agents can operate under dual reporting rules (mission alignment and operational compliance).
- FR5: System can pause and request human decision when mission and operations directives conflict.
- FR46: System can enforce role-based command precedence across Human Supervisor, Lab Assistant, and Site Manager.
- FR47: System can persist and replay agent-to-agent and agent-to-human command and decision trails for auditability.
- FR48: System can validate session prerequisites (runtime health, data bindings, communication channels) before mission start.
- FR49: System can enter safe degraded mode when required dependencies fail, while preserving session artifacts.

### In-Scene Collaboration

- FR6: Human participants can communicate with AI collaborators inside the session environment.
- FR7: Human participants can ask natural-language questions to the in-room Lab Assistant.
- FR8: Lab Assistant can reference in-scene objects and active session context when responding.
- FR9: Participants can identify objects using pointer and selection interactions.
- FR10: System can visualize participant-specific object highlights with time-based dissolve behavior.
- FR11: Participants can grab, move, and release scene objects during collaboration.
- FR12: System can maintain shared object state visibility for all active session participants.

### Communication Reliability

- FR13: System can maintain duplex communication channels between key collaborators.
- FR14: System can detect unacknowledged communication attempts within configured timeout thresholds.
- FR15: System can notify relevant participants when communication attempts are not acknowledged.
- FR16: Site Manager can initiate communication recovery workflows after fault detection.
- FR17: System can preserve session continuity after communication recovery.
- FR57: System can enforce the MVP baseline collaboration flow with Human Supervisor and Lab Assistant as the first required communication stratum.
- FR58: System can persist baseline collaboration turns (question, response, referenced object context, decision note) as mission artifacts.
- FR59: System can expand from baseline collaboration to Site Manager-supervised communication only after baseline flow checks pass.
- FR60: System can classify communication events by stratum (`strata1_baseline`, `strata2_oversight`, `strata3_extended`) for traceability and reporting.
- FR61: System can display a screen-first baseline communication UI with a scrollable dialogue panel and participant color mapping (`H=green`, `LA=blue`).
- FR62: System can complete utterance detection using a `1200ms` silence threshold for baseline HMD speech capture.
- FR63: System can require user confirmation before committing low-confidence STT output when confidence is `<0.85`.
- FR64: System can support session resume initiation by voice command and saved-session list selection with explicit load confirmation.

### Session Persistence & Traceability

- FR18: Users can save active session state and resume it later.
- FR19: System can persist dynamic object states across save and resume cycles.
- FR20: System can capture and store chronological activity logs for each session.
- FR21: System can store session decisions, context, and artifacts for later review.
- FR22: System can associate external data references used in-session with log records.
- FR65: System can keep dialogue/event logs as durable records that are never cleared and are synchronized with scene save/load operations.
- FR66: System can prepend each dialogue/event log entry with a timestamp and event type.
- FR67: System can apply dirty-state checks before autosave/close actions and can skip redundant save operations when no changes exist.

### Digital Twin & Data Context

- FR23: System can load client-specific digital twin scene configurations.
- FR24: Sessions can access preconfigured historical production data during runtime.
- FR25: System can validate data-source availability before session workflows begin.
- FR26: System can support local and NAS-backed data access for MVP session operations.
- FR27: Participants can use external data context to support in-session diagnosis and optimization reasoning.

### Model Lifecycle & Injection

- FR28: Model Manager can maintain a reusable model repository.
- FR29: Model Manager can spawn requested models into active sessions.
- FR30: Participants can request model injection during sessions.
- FR31: System can expose available model inventory to participants in-session.
- FR32: System can support model removal from active scenes while preserving repository control boundaries.
- FR68: Model Manager can return numbered candidate reference images for user selection by voice or laser interaction and can persist selected references in session artifacts.
- FR69: Model Manager can generate mesh geometry using integrated `UPBGE` model script capability and report estimated completion time before scene insertion.

### Operations Monitoring & Support

- FR33: Site Manager can monitor session health and participant communication status.
- FR34: Site Manager can orchestrate troubleshooting and monitoring agent workflows.
- FR35: System can record detected issues and applied recovery actions.
- FR36: System can support system optimization and QA sessions for validating new capabilities before production use.

### Research & Knowledge Loop

- FR37: Lab Assistant can capture in-session ideas and tasks into a mission roster.
- FR38: System can retain cross-session records of successful methods and actions.
- FR39: Research Agent can perform out-of-session research tasks aligned to session objectives.
- FR40: Research Agent can provide structured findings for later session preload and use.
- FR41: System can associate research findings with relevant session goals and logs.
- FR53: Lab Assistant can classify captured ideas and tasks into backlog categories (mission, operations, integration, research).
- FR54: System can recommend prior successful methods based on similarity to current session goals.

### Environment & Runtime Capabilities

- FR42: System can run as a Windows desktop application for MVP.
- FR43: System can provide human-participant VR session operation with required runtime stack dependencies.
- FR44: System can support optional internet-assisted enrichment tasks during sessions.
- FR45: System can display externally retrieved reference assets in-session and persist them with session artifacts.
- FR70: In no-gravity mode, system can preserve released object position and orientation at release time.
- FR71: System can enable scaling mode on selected parts with visible wireframe bounding boxes, corner handles, and live `X/Y/Z` dimensions until scaling mode is toggled off.
- FR72: System can support single-axis scaling when opposing handles on the same edge are manipulated and uniform scaling when diagonally opposite handles are manipulated.
- FR73: System can apply group scaling transforms to all selected parts while preserving relative spacing and scaling each part from its center origin.
- FR74: System can enforce per-scaling-action bounds of `10x` in either direction; additional scaling beyond `10x` requires releasing and re-enabling scaling mode.
- FR75: System can execute inactivity lifecycle handling: prompt save at `2 min` no-human activity, autosave after `+1 min` if still inactive, and save-then-close after `5 min` total zero activity.

### Sales Proof & Outcome Intelligence

- FR50: System can generate session outcome summaries suitable for client-facing proof and demo artifacts.
- FR51: System can map each session outcome to measurable KPI tags (time, correctness, fault detection, etc.).
- FR52: System can maintain reusable win-case records linked to scenario type and improvement evidence.

### QA & Verification Support

- FR55: System can expose deterministic session replay mode for QA validation.
- FR56: System can record pass and fail evidence for each mission objective checkpoint in a session.

## Non-Functional Requirements

### Performance

- Human VR session rendering must sustain `>=90 FPS` during standard mission workflows.
- AI perception and scene-context feed should sustain approximately `1-5 FPS` without breaking mission collaboration flow, measured from session telemetry logs across `>=30` minute mission windows.
- Model injection responsiveness must preserve collaboration flow, with practical targets of `<3s` for simple assets and `<10s` for heavy assets under expected MVP conditions.

### Reliability

- The system should operate uninterrupted for up to 8 hours per active session, measured by mission runtime telemetry with zero unrecoverable failure events per 8-hour run.
- Unacknowledged communications must be detected within `<10s`.
- Communication fault recovery should restore actionable session continuity within a practical short recovery window, with a working target of `<30s`.
- Session artifacts and active decision context must remain intact across communication failures and recovery events, with `100%` artifact integrity verification at session close.
- Baseline collaboration median turn latency (Human Supervisor <-> Lab Assistant) should remain `<2.5s` during standard mission load.
- Baseline collaboration acknowledgment success rate should remain `>=99%` during standard mission load.
- Collaboration understanding quality should score `>=4.0/5.0` in post-session reviewer scoring for mission-critical exchanges.

### Security

- Durable audit logging is mandatory for all critical actions, role decisions, and mission events, with `>=99%` critical event capture and event-write latency `<2s` during normal session operation.
- Role-aware access enforcement must protect mission and operational command surfaces, with `100%` denial of unauthorized privileged command attempts in access-control test suites.
- Security baseline is log-first for MVP; by the first post-MVP release, remote-session traffic must enforce TLS `1.2+` and session artifacts must be encrypted at rest with managed key rotation.

### Integration

- Local storage and NAS integration are mandatory MVP data pathways, verified by pre-session path accessibility checks and successful read/write audit events for `100%` of completed sessions.
- External data sources required for a mission must be validated pre-session before mission start, with `100%` source-validation pass confirmation recorded in session metadata.
- In-session external enrichment (for example internet-sourced references/images) must be explicitly traceable and attached to session artifacts, measured by source metadata presence (`URL or source id + timestamp`) for `100%` of saved enrichment assets.

### Scalability

- MVP must support one human supervisor with up to 6 in-room/service agents in a single mission session while preserving all reliability targets.
- Post-MVP architecture should support at least 5 concurrent client sessions while maintaining session reliability and communication recovery targets, measured by quarterly load tests of 5 parallel sessions where `>=95%` of session intervals meet the same reliability and recovery SLAs.

## Traceability Map (Journeys -> Requirements)

### Communication Flow Strata Mapping

- **Strata 1 (Human Supervisor <-> Lab Assistant baseline):** Journey 0 -> FR6-FR8, FR57-FR75, Reliability (turn latency, ack success, understanding quality, inactivity lifecycle)
- **Strata 2 (Site Manager oversight and recovery):** Journeys 2-3 -> FR13-FR17, FR33-FR35, FR59-FR60, Reliability (fault detection and recovery targets)
- **Strata 3 (extended supporting agents):** Journeys 4-6 -> FR34-FR41, FR60, Scalability and Security requirements

### Journey 1: Primary User Success Path

- **Functional alignment:** FR6-FR12, FR18-FR22, FR37-FR41
- **Non-functional alignment:** Performance, Reliability

### Journey 2: Communication Breakdown and Recovery

- **Functional alignment:** FR13-FR17, FR33-FR35, FR46-FR49
- **Non-functional alignment:** Reliability, Security

### Journey 3: Site Manager Operations Oversight

- **Functional alignment:** FR3-FR5, FR13-FR17, FR33-FR36, FR46-FR49
- **Non-functional alignment:** Reliability, Integration

### Journey 4: Monitoring and Troubleshooting Assurance

- **Functional alignment:** FR33-FR36, FR47-FR49, FR55-FR56
- **Non-functional alignment:** Reliability, Security, Scalability

### Journey 5: External Data Enablement

- **Functional alignment:** FR23-FR27, FR50-FR52
- **Non-functional alignment:** Integration, Security

### Journey 6: Remote Collaboration Readiness

- **Functional alignment:** FR13-FR17, FR33-FR36, FR43-FR44, FR50-FR52
- **Non-functional alignment:** Reliability, Security, Scalability

## Approval Snapshot

- **PRD status:** Complete (Step 12 finalized)
- **Document version date:** 2026-03-13
- **MVP scope lock:** Approved
- **Communication baseline scope:** Approved for phased rollout beginning with Human Supervisor <-> Lab Assistant, then advancing through agent strata.
- **Authority model lock:** Approved (Human final authority; Lab Assistant mission authority; Site Manager operational authority)
- **Key accepted risks:** communication instability, model drift, telemetry dependency assumptions, and phased security hardening
- **Primary readiness outcome:** PRD baseline is ready for validation, architecture, and epic/story decomposition
