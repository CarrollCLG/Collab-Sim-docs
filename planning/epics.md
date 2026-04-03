---
stepsCompleted:
  - 1
  - 2
  - 3
  - 4
inputDocuments:
  - _bmad-output/planning-artifacts/prd.md
  - _bmad-output/planning-artifacts/architecture.md
  - _bmad-output/planning-artifacts/architecture-starter-skeleton.md
  - _bmad-output/planning-artifacts/ux-design-specification.md
  - _bmad-output/planning-artifacts/prd-validation-report.md
---

# Collab_Sim - Epic Breakdown

## Overview

This document provides the complete epic and story breakdown for Collab_Sim, decomposing the requirements from the PRD, UX Design, and Architecture requirements into implementable stories.

## Requirements Inventory

### Functional Requirements

FR1: Human Supervisor can override any agent decision at any time during a session.  
FR2: Lab Assistant can supervise mission-level activities across active sessions.  
FR3: Site Manager can supervise operational and session-environment readiness and continuity.  
FR4: Agents can operate under dual reporting rules (mission alignment and operational compliance).  
FR5: System can pause and request human decision when mission and operations directives conflict.  
FR6: Human participants can communicate with AI collaborators inside the session environment.  
FR7: Human participants can ask natural-language questions to the in-room Lab Assistant.  
FR8: Lab Assistant can reference in-scene objects and active session context when responding.  
FR9: Participants can identify objects using pointer and selection interactions.  
FR10: System can visualize participant-specific object highlights with time-based dissolve behavior.  
FR11: Participants can grab, move, and release scene objects during collaboration.  
FR12: System can maintain shared object state visibility for all active session participants.  
FR13: System can maintain duplex communication channels between key collaborators.  
FR14: System can detect unacknowledged communication attempts within configured timeout thresholds.  
FR15: System can notify relevant participants when communication attempts are not acknowledged.  
FR16: Site Manager can initiate communication recovery workflows after fault detection.  
FR17: System can preserve session continuity after communication recovery.  
FR18: Users can save active session state and resume it later.  
FR19: System can persist dynamic object states across save and resume cycles.  
FR20: System can capture and store chronological activity logs for each session.  
FR21: System can store session decisions, context, and artifacts for later review.  
FR22: System can associate external data references used in-session with log records.  
FR23: System can load client-specific digital twin scene configurations.  
FR24: Sessions can access preconfigured historical production data during runtime.  
FR25: System can validate data-source availability before session workflows begin.  
FR26: System can support local and NAS-backed data access for MVP session operations.  
FR27: Participants can use external data context to support in-session diagnosis and optimization reasoning.  
FR28: Model Manager can maintain a reusable model repository.  
FR29: Model Manager can spawn requested models into active sessions.  
FR30: Participants can request model injection during sessions.  
FR31: System can expose available model inventory to participants in-session.  
FR32: System can support model removal from active scenes while preserving repository control boundaries.  
FR33: Site Manager can monitor session health and participant communication status.  
FR34: Site Manager can orchestrate troubleshooting and monitoring agent workflows.  
FR35: System can record detected issues and applied recovery actions.  
FR36: System can support system optimization and QA sessions for validating new capabilities before production use.  
FR37: Lab Assistant can capture in-session ideas and tasks into a mission roster.  
FR38: System can retain cross-session records of successful methods and actions.  
FR39: Research Agent can perform out-of-session research tasks aligned to session objectives.  
FR40: Research Agent can provide structured findings for later session preload and use.  
FR41: System can associate research findings with relevant session goals and logs.  
FR42: System can run as a Windows desktop application for MVP.  
FR43: System can provide human-participant VR session operation with required runtime stack dependencies.  
FR44: System can support optional internet-assisted enrichment tasks during sessions.  
FR45: System can display externally retrieved reference assets in-session and persist them with session artifacts.  
FR46: System can enforce role-based command precedence across Human Supervisor, Lab Assistant, and Site Manager.  
FR47: System can persist and replay agent-to-agent and agent-to-human command and decision trails for auditability.  
FR48: System can validate session prerequisites (runtime health, data bindings, communication channels) before mission start.  
FR49: System can enter safe degraded mode when required dependencies fail, while preserving session artifacts.  
FR50: System can generate session outcome summaries suitable for client-facing proof and demo artifacts.  
FR51: System can map each session outcome to measurable KPI tags (time, correctness, fault detection, etc.).  
FR52: System can maintain reusable win-case records linked to scenario type and improvement evidence.  
FR53: Lab Assistant can classify captured ideas and tasks into backlog categories (mission, operations, integration, research).  
FR54: System can recommend prior successful methods based on similarity to current session goals.  
FR55: System can expose deterministic session replay mode for QA validation.  
FR56: System can record pass and fail evidence for each mission objective checkpoint in a session.  
FR57: System can enforce the MVP baseline collaboration flow with Human Supervisor and Lab Assistant as the first required communication stratum.  
FR58: System can persist baseline collaboration turns (question, response, referenced object context, decision note) as mission artifacts.  
FR59: System can expand from baseline collaboration to Site Manager-supervised communication only after baseline flow checks pass.  
FR60: System can classify communication events by stratum (`strata1_baseline`, `strata2_oversight`, `strata3_extended`) for traceability and reporting.  
FR61: System can display a screen-first baseline communication UI with a scrollable dialogue panel and participant color mapping (`H=green`, `LA=blue`).  
FR62: System can complete utterance detection using a `1200ms` silence threshold for baseline HMD speech capture.  
FR63: System can require user confirmation before committing low-confidence STT output when confidence is `<0.85`.  
FR64: System can support session resume initiation by voice command and saved-session list selection with explicit load confirmation.  
FR65: System can keep dialogue/event logs as durable records that are never cleared and are synchronized with scene save/load operations.  
FR66: System can prepend each dialogue/event log entry with a timestamp and event type.  
FR67: System can apply dirty-state checks before autosave/close actions and can skip redundant save operations when no changes exist.  
FR68: Model Manager can return numbered candidate reference images for user selection by voice or laser interaction and can persist selected references in session artifacts.  
FR69: Model Manager can generate mesh geometry using integrated `UPBGE` model script capability and report estimated completion time before scene insertion.  
FR70: In no-gravity mode, system can preserve released object position and orientation at release time.  
FR71: System can enable scaling mode on selected parts with visible wireframe bounding boxes, corner handles, and live `X/Y/Z` dimensions until scaling mode is toggled off.  
FR72: System can support single-axis scaling when opposing handles on the same edge are manipulated and uniform scaling when diagonally opposite handles are manipulated.  
FR73: System can apply group scaling transforms to all selected parts while preserving relative spacing and scaling each part from its center origin.  
FR74: System can enforce per-scaling-action bounds of `10x` in either direction; additional scaling beyond `10x` requires releasing and re-enabling scaling mode.  
FR75: System can execute inactivity lifecycle handling: prompt save at `2 min` no-human activity, autosave after `+1 min` if still inactive, and save-then-close after `5 min` total zero activity.

### NonFunctional Requirements

NFR1: Human VR session rendering must sustain `>=90 FPS` during standard mission workflows.  
NFR2: AI perception and scene-context feed should sustain `1-5 FPS` during standard mission windows.  
NFR3: Model injection responsiveness targets are `<3s` for simple assets and `<10s` for heavy assets under expected MVP conditions.  
NFR4: System should run uninterrupted for up to 8 hours per active session with zero unrecoverable failure events.  
NFR5: Unacknowledged communications must be detected within `<10s`.  
NFR6: Communication fault recovery should restore actionable session continuity with a working target of `<30s`.  
NFR7: Session artifacts and active decision context must remain intact across failures with `100%` artifact integrity verification at close.  
NFR8: Baseline collaboration median turn latency should remain `<2.5s` during standard mission load.  
NFR9: Baseline collaboration acknowledgment success rate should remain `>=99%` during standard mission load.  
NFR10: Collaboration understanding quality should score `>=4.0/5.0` in post-session reviewer scoring for mission-critical exchanges.  
NFR11: Durable audit logging is mandatory for critical actions/events with `>=99%` critical event capture and event-write latency `<2s`.  
NFR12: Role-aware access enforcement must achieve `100%` denial of unauthorized privileged command attempts in test suites.  
NFR13: Security baseline is log-first for MVP; post-MVP remote traffic must enforce TLS `1.2+` and artifacts encrypted at rest with managed key rotation.  
NFR14: Local storage and NAS integration are mandatory MVP pathways with successful read/write audit events for `100%` of completed sessions.  
NFR15: Required external data sources must be validated pre-session with `100%` source-validation confirmation recorded.  
NFR16: In-session external enrichment assets must be traceable with source metadata (`URL/source id + timestamp`) for `100%` of saved enrichment assets.  
NFR17: MVP must support one human supervisor with up to 6 in-room/service agents while preserving reliability targets.  
NFR18: Post-MVP architecture should support at least 5 concurrent client sessions while maintaining reliability/recovery targets in load tests.

### Additional Requirements

- Starter template decision: Story 1.1 must initialize project scaffold using `uv init collab-sim-runtime --package ...` and establish runtime module boundaries.
- Runtime baseline must pin a specific `UPBGE` build artifact for MVP and avoid floating upgrades during early implementation.
- MVP persistence must be file-first (`.blend` + event/log artifacts + manifest) on local/NAS paths.
- Implement `SessionBundle v1` and `EventLog v1` contracts with explicit `schemaVersion` support.
- Enforce canonical session layout: `sessions/{sessionId}/scene|logs|manifest|artifacts`.
- Enforce artifact naming convention: `YYYYMMDD-HHMMSS_{sessionId}_{type}_{version}.{ext}`.
- Implement atomic write protocol (`temp write -> flush/fsync -> atomic rename`) for persistence safety.
- Enforce schema compatibility policy (read current + previous minor; reject unknown major).
- Implement checksum policy and emit `PERSIST_INTEGRITY_FAIL` on mismatch.
- Standardize error namespace (`COMM_*`, `PERSIST_*`, `MODEL_*`, `INTERACT_*`, `OPS_*`) and consistent `correlationId` propagation.
- Enforce persistence telemetry events (`PERSIST_SAVE_STARTED|SUCCEEDED|FAILED|RECOVERY_APPLIED`) and replay integrity QA gates.
- Maintain strict module boundaries (`runtime/orchestrator`, `interaction`, `communication`, `persistence`, `model_adapter`, `ops_guardrail`, `logging_observability`, `ui_runtime`).
- Protect frame budget by separating frame-critical from non-frame-critical work.
- Define environment profiles (`local-dev`, `local-mission`, `qa-replay`) before feature expansion.

### UX Design Requirements

UX-DR1: Implement fixed north-screen geometry `30 ft x 12 ft` with immutable three-equal-third panel mapping.  
UX-DR2: Implement left panel transcript with role color mapping (`H=green`, `LA=blue`) and persistent conversation history.  
UX-DR3: Implement transcript navigation controls: `Page Up`, `Page Down`, and right-side scrollbar with long-history handling.  
UX-DR4: Implement warning dialogs that can override any panel region and always include explicit `OK/Cancel` actions.  
UX-DR5: Implement concurrent popup manager with independently cancellable popups and persistent lifecycle logging for create/dismiss/cancel.  
UX-DR6: Implement right panel sections for goals/sub-goals, timestamped problem list, and object list.  
UX-DR7: Implement object-list-to-scene highlight behavior with user-color wireframe bounding box fading after approximately `5s`.  
UX-DR8: Implement object actions (`duplicate`, `delete`, `rename`) with mandatory two-step `Y/N` confirmation flow.  
UX-DR9: Implement STT confidence-gating UX: values `<0.85` must require explicit user confirmation before commit.  
UX-DR10: Implement session start/resume UX flow with `LA` greeting, saved-session selection, and explicit load confirmation.  
UX-DR11: Implement design-token foundation for role colors, warning/error semantics, spacing rhythm, and interaction-state tokens.  
UX-DR12: Implement clear typography hierarchy and high-legibility VR text rules (panel titles, section labels, body, metadata).  
UX-DR13: Implement semantic interaction states for critical actions (`default`, `focus`, `armed`, confirmation steps, completed).  
UX-DR14: Implement transcript control cluster component with large hit targets and explicit focus state.  
UX-DR15: Implement object-action double-confirm component as reusable safety primitive.  
UX-DR16: Implement multi-popup manager integration component as reusable operational primitive.  
UX-DR17: Implement feedback pattern standards (success, warning, error, info) with explicit, actionable messaging behavior.  
UX-DR18: Implement accessibility rules: color+text redundancy, clear selection/focus states, minimum target sizing, low-discomfort motion.  
UX-DR19: Preserve deterministic panel-purpose behavior (content may change; panel role may not) to protect spatial memory.  
UX-DR20: Instrument popup/object-action UX events for QA traceability and replay validation.

### FR Coverage Map

FR1: Epic 1 - Human override authority in baseline collaboration  
FR2: Epic 1 - Lab Assistant mission supervision foundation  
FR3: Epic 1 - Site Manager operational readiness foundation  
FR4: Epic 1 - Dual reporting rule in baseline control model  
FR5: Epic 1 - Human conflict-resolution authority flow  
FR6: Epic 1 - Human to AI in-session communication  
FR7: Epic 1 - Natural-language interaction with Lab Assistant  
FR8: Epic 1 - Context-grounded assistant responses  
FR9: Epic 2 - Object identification interactions  
FR10: Epic 2 - Object highlight feedback behavior  
FR11: Epic 2 - Grab/move/release interactions  
FR12: Epic 2 - Shared object-state visibility  
FR13: Epic 5 - Duplex channel reliability baseline  
FR14: Epic 5 - Timeout detection  
FR15: Epic 5 - Fault notification behavior  
FR16: Epic 5 - Recovery orchestration trigger  
FR17: Epic 5 - Post-recovery continuity  
FR18: Epic 3 - Save/resume user capability  
FR19: Epic 3 - Dynamic object-state persistence  
FR20: Epic 3 - Chronological activity logging  
FR21: Epic 3 - Decision/context/artifact retention  
FR22: Epic 3 - External reference linkage in logs  
FR23: Epic 6 - Digital twin scene loading  
FR24: Epic 6 - Historical production data access  
FR25: Epic 6 - Pre-session data-source validation  
FR26: Epic 6 - Local/NAS data pathway support  
FR27: Epic 6 - Data-context diagnostic reasoning support  
FR28: Epic 4 - Model repository lifecycle support  
FR29: Epic 4 - In-session model spawn behavior  
FR30: Epic 4 - User-requested model injection  
FR31: Epic 4 - In-session model inventory visibility  
FR32: Epic 4 - Model removal with repository boundary control  
FR33: Epic 5 - Session-health monitoring  
FR34: Epic 5 - Troubleshooting/monitoring orchestration  
FR35: Epic 5 - Issue/recovery event recording  
FR36: Epic 5 - Optimization/QA validation session support  
FR37: Epic 7 - Mission roster capture  
FR38: Epic 7 - Cross-session method memory  
FR39: Epic 7 - Asynchronous research workflow  
FR40: Epic 7 - Structured research preload output  
FR41: Epic 7 - Research-to-goal linkage  
FR42: Epic 1 - Windows desktop runtime support  
FR43: Epic 1 - Human VR runtime operation capability  
FR44: Epic 4 - Optional internet-assisted enrichment support  
FR45: Epic 4 - External reference display + persistence  
FR46: Epic 5 - Command precedence enforcement  
FR47: Epic 5 - Decision/audit replay trail  
FR48: Epic 5 - Pre-session runtime prerequisite checks  
FR49: Epic 5 - Safe degraded mode behavior  
FR50: Epic 7 - Session outcome summary generation  
FR51: Epic 7 - KPI tagging of outcomes  
FR52: Epic 7 - Win-case record maintenance  
FR53: Epic 7 - Backlog classification from session capture  
FR54: Epic 7 - Similar-method recommendation support  
FR55: Epic 8 - Deterministic replay mode for QA  
FR56: Epic 8 - Mission checkpoint pass/fail evidence capture  
FR57: Epic 1 - Baseline strata-1 collaboration enforcement  
FR58: Epic 3 - Baseline turn persistence as artifacts  
FR59: Epic 5 - Strata progression gate checks  
FR60: Epic 5 - Communication event strata classification  
FR61: Epic 1 - Screen-first baseline communication UI  
FR62: Epic 1 - 1200ms utterance completion detection  
FR63: Epic 1 - STT confidence confirmation gate  
FR64: Epic 1 - Resume-initiation and saved-session load flow  
FR65: Epic 3 - Durable synchronized dialogue/event logs  
FR66: Epic 3 - Timestamped event log entries  
FR67: Epic 3 - Dirty-state-aware autosave/close behavior  
FR68: Epic 4 - Numbered candidate selection + artifact persistence  
FR69: Epic 4 - Generated mesh injection with completion estimates  
FR70: Epic 2 - No-gravity release persistence behavior  
FR71: Epic 2 - Scaling mode visual/interaction affordances  
FR72: Epic 2 - Axis/uniform scaling interaction model  
FR73: Epic 2 - Group scaling transform behavior  
FR74: Epic 2 - Per-action scaling bounds enforcement  
FR75: Epic 3 - Inactivity lifecycle prompt/autosave/close flow

## Epic List

### Epic 1: Mission Session Foundation & Baseline Collaboration
Enable users to launch `Collab_Sim`, start or resume a baseline `Human <-> Lab Assistant` session, and complete confidence-gated conversational turns under authority-safe control rules.
**FRs covered:** FR1, FR2, FR3, FR4, FR5, FR6, FR7, FR8, FR42, FR43, FR57, FR61, FR62, FR63, FR64
**Definition of Done:** User can launch/start/resume and run the baseline conversation loop with confidence gating and role precedence enforced.
**Dependencies:** None (foundational epic).
**Story sizing intent:** Target 4-6 stories, each independently testable.
**NFR focus:** Performance, Reliability, Security.
**First story hint:** Initialize runtime scaffold, startup checks, and baseline session start/resume shell.
**Out-of-scope guardrail:** No advanced multi-strata orchestration beyond baseline collaboration flow.

### Epic 2: Scene Interaction & Safe Object Manipulation
Enable users to inspect, select, manipulate, and safely transform scene objects with deterministic visual feedback and bounded scaling interactions.
**FRs covered:** FR9, FR10, FR11, FR12, FR70, FR71, FR72, FR73, FR74
**Definition of Done:** User can reliably select/highlight/grab/release/scale objects with all defined bounds and feedback behaviors.
**Dependencies:** Epic 1 runtime/session baseline.
**Story sizing intent:** Target 3-5 stories, each independently testable.
**NFR focus:** Performance, Reliability.
**First story hint:** Implement object select/highlight pipeline with deterministic visual feedback.
**Out-of-scope guardrail:** No model repository/injection workflows in this epic.

### Epic 3: Session Persistence, Continuity & Inactivity Lifecycle
Enable full save/resume continuity with synchronized scene and log context, plus reliable inactivity and dirty-state lifecycle handling.
**FRs covered:** FR18, FR19, FR20, FR21, FR22, FR58, FR65, FR66, FR67, FR75
**Definition of Done:** Save/resume reproduces scene + synchronized logs and inactivity lifecycle rules execute with integrity checks.
**Dependencies:** Epic 1 baseline session flow.
**Story sizing intent:** Target 4-6 stories, each independently testable.
**NFR focus:** Reliability, Security, Integration.
**First story hint:** Define and persist `SessionBundle v1` and `EventLog v1` contracts.
**Out-of-scope guardrail:** No post-MVP distributed persistence or cloud orchestration.

### Epic 4: Model Lifecycle & In-Scene Injection
Enable model repository operations, candidate/reference selection, internet-assisted enrichment (optional), and controlled in-session geometry injection with traceable artifacts.
**FRs covered:** FR28, FR29, FR30, FR31, FR32, FR44, FR45, FR68, FR69
**Definition of Done:** User can request/select references (including optional internet-assisted enrichment), inject generated assets, and persist all related traceable artifacts.
**Dependencies:** Epic 1 baseline collaboration; Epic 3 persistence contracts for artifact traceability.
**Story sizing intent:** Target 3-5 stories, each independently testable.
**NFR focus:** Performance, Reliability, Integration.
**First story hint:** Implement candidate reference retrieval + numbered selection + artifact persistence.
**Out-of-scope guardrail:** No broad external marketplace/catalog integrations.

### Epic 5: Operational Resilience & Site Manager Governance
Enable communication reliability, health monitoring, fault recovery, and governance controls that preserve mission continuity.
**FRs covered:** FR13, FR14, FR15, FR16, FR17, FR33, FR34, FR35, FR36, FR46, FR47, FR48, FR49, FR59, FR60
**Definition of Done:** Communication faults are detected/recovered within target windows with governance rules, degraded-mode handling, and audit traceability intact.
**Dependencies:** Epic 1 baseline communication contracts; Epic 3 persistence/logging continuity.
**Story sizing intent:** Target 4-6 stories, each independently testable.
**NFR focus:** Reliability, Security, Scalability.
**First story hint:** Implement duplex health monitor with timeout detection and correlated recovery events.
**Out-of-scope guardrail:** No autonomous decision authority that bypasses Human final authority.

### Epic 6: Digital Twin Data Context
Enable validated digital twin and historical data-context use in mission workflows across mandatory local/NAS pathways.
**FRs covered:** FR23, FR24, FR25, FR26, FR27
**Definition of Done:** Pre-session data validation gates pass and users can use historical/digital-twin context during mission execution.
**Dependencies:** Epic 1 session baseline; Epic 3 persistence context linkage.
**Story sizing intent:** Target 2-4 stories, each independently testable.
**NFR focus:** Integration, Reliability.
**First story hint:** Implement pre-session data source validation with explicit mission-start gating.
**Out-of-scope guardrail:** No full enterprise SCADA/MES integration expansion in MVP.

### Epic 7: Knowledge Loop, Research & Outcome Intelligence
Enable mission roster capture, cross-session learning, research preload workflows, and measurable proof-of-value outputs.
**FRs covered:** FR37, FR38, FR39, FR40, FR41, FR50, FR51, FR52, FR53, FR54
**Definition of Done:** Sessions produce reusable knowledge artifacts, research preload outputs, and measurable outcome intelligence suitable for review/proof.
**Dependencies:** Epic 3 persistence/traceability baseline.
**Story sizing intent:** Target 3-5 stories, each independently testable.
**NFR focus:** Reliability, Integration, Security.
**First story hint:** Implement mission roster capture + categorized backlog extraction from session context.
**Out-of-scope guardrail:** No fully autonomous strategic planning loops without human review.

### Epic 8: QA Replay, Verification & Release Readiness
Enable deterministic replay and checkpoint evidence capture for reliability and implementation conformance verification.
**FRs covered:** FR55, FR56
**Definition of Done:** QA can run deterministic replay and capture pass/fail evidence for mission checkpoints with reproducible outputs.
**Dependencies:** Epics 1-7 implemented enough to produce replayable session artifacts.
**Story sizing intent:** Target 2-3 stories, each independently testable.
**NFR focus:** Reliability, Performance.
**First story hint:** Build deterministic replay harness with checkpoint evidence capture schema.
**Out-of-scope guardrail:** No broad analytics dashboard initiative beyond replay/evidence verification needs.

## Epic 1: Mission Session Foundation & Baseline Collaboration

Enable users to launch `Collab_Sim`, start or resume a baseline `Human <-> Lab Assistant` session, and complete confidence-gated conversational turns under authority-safe control rules.

### Story 1.1: Set Up Initial Project from Starter Template

**Implements:** FR42, FR43

As a Human Supervisor,  
I want the project initialized from the approved starter template with baseline runtime checks,  
So that I can begin a mission session reliably.

**Acceptance Criteria:**

**Given** the app is launched on a supported Windows environment  
**When** starter initialization and bootstrap setup execute  
**Then** the scaffold created by `uv init collab-sim-runtime --package ...` is configured with required runtime checks (`SteamVR`, `UPBGE`)  
**And** session shell initializes with baseline strata-1 collaboration mode active.

### Story 1.2: Session Start/Resume Entry Flow

**Implements:** FR57, FR64

As a Human Supervisor,  
I want to start a new session or resume an existing session,  
So that I can continue work without losing mission continuity.

**Acceptance Criteria:**

**Given** the baseline session shell is active  
**When** `LA` greeting prompt is displayed and user chooses new or resume  
**Then** user can select a saved session via approved interaction path and explicit load confirmation  
**And** session state transitions to active collaboration mode with correct context.

### Story 1.3: Baseline Voice Turn and STT Confidence Gate

**Implements:** FR6, FR7, FR8, FR61, FR62, FR63

As a Human Supervisor,  
I want voice turns to be captured and validated for confidence,  
So that committed dialogue is trustworthy.

**Acceptance Criteria:**

**Given** an active baseline session  
**When** user speaks and utterance end is detected at `1200ms` silence threshold  
**Then** transcript is generated and shown in baseline dialogue UI  
**And** if confidence is `<0.85`, explicit confirmation is required before commit.

### Story 1.4: Role Precedence and Authority Controls

**Implements:** FR1, FR2, FR3, FR4, FR5

As an operator team,  
I want role-based command precedence enforced,  
So that mission and operational safety rules are respected.

**Acceptance Criteria:**

**Given** a command may conflict with role policies  
**When** command evaluation executes  
**Then** authority precedence rules are enforced (`Human` final authority, mission/ops constraints applied)  
**And** conflicts trigger explicit decision prompts and auditable events.

## Epic 2: Scene Interaction & Safe Object Manipulation

Enable users to inspect, select, manipulate, and safely transform scene objects with deterministic visual feedback and bounded scaling interactions.

### Story 2.1: Object Selection and Highlight Feedback

**Implements:** FR9, FR10, FR12

As a Human Supervisor,  
I want to select objects and see deterministic highlight feedback,  
So that I can confirm I am acting on the right target.

**Acceptance Criteria:**

**Given** objects are present in scene and object list  
**When** user selects an object via approved interaction  
**Then** the corresponding object is highlighted with required visual behavior  
**And** highlight behavior follows timed fade and traceable event logging rules.

### Story 2.2: Grab/Move/Release with No-Gravity Persistence

**Implements:** FR11, FR70

As a Human Supervisor,  
I want object movement to persist accurately after release,  
So that spatial adjustments remain stable.

**Acceptance Criteria:**

**Given** no-gravity mode is enabled  
**When** user grabs, moves, and releases an object  
**Then** released position and orientation are preserved as defined  
**And** resulting transform state is available for subsequent save/resume workflows.

### Story 2.3: Scaling Mode with Handles, Axis Rules, and Bounds

**Implements:** FR71, FR72, FR73, FR74

As a Human Supervisor,  
I want controlled scaling interactions with clear feedback and safety limits,  
So that object transformations are precise and reversible in workflow context.

**Acceptance Criteria:**

**Given** scaling mode is enabled on selected objects  
**When** user manipulates defined handle patterns  
**Then** axis/uniform/group scaling behavior follows specified rules  
**And** per-action scale bounds (`10x`) are enforced with required user feedback.

## Epic 3: Session Persistence, Continuity & Inactivity Lifecycle

Enable full save/resume continuity with synchronized scene and log context, plus reliable inactivity and dirty-state lifecycle handling.

### Story 3.1: SessionBundle v1 and EventLog v1 Persistence Contracts

**Implements:** FR19, FR20, FR65, FR66

As a platform maintainer,  
I want standardized persistence contracts,  
So that sessions are saved consistently and replay can be deterministic.

**Acceptance Criteria:**

**Given** a save operation is initiated  
**When** persistence writes session artifacts  
**Then** `SessionBundle v1` and `EventLog v1` schemas are applied with required fields and versioning  
**And** writes use atomic protocol (`temp -> fsync -> rename`) with integrity metadata.

### Story 3.2: Resume with Synchronized Scene and Durable Logs

**Implements:** FR18, FR21

As a Human Supervisor,  
I want resumed sessions to restore full context,  
So that I can continue exactly where I left off.

**Acceptance Criteria:**

**Given** a valid saved session exists  
**When** resume is executed  
**Then** scene state and synchronized dialogue/event history are restored together  
**And** integrity verification runs before session activation, with failure path handled safely.

### Story 3.3: Dirty-State-Aware Save, Autosave, and Inactivity Lifecycle

**Implements:** FR67, FR75

As a Human Supervisor,  
I want idle handling to protect my work without unnecessary writes,  
So that state is preserved while minimizing disruption.

**Acceptance Criteria:**

**Given** inactivity thresholds are reached  
**When** prompt/autosave/close lifecycle logic executes  
**Then** configured timing behavior is enforced (`2 min` prompt, `+1 min` autosave, `5 min` save-and-close)  
**And** dirty-state checks prevent redundant saves while preserving safety.

### Story 3.4: Baseline Turn and External Reference Traceability

**Implements:** FR22, FR58

As a reviewer,  
I want baseline conversational turns and references to be fully traceable,  
So that decisions are auditable post-session.

**Acceptance Criteria:**

**Given** baseline dialogue and reference actions occur  
**When** events are committed  
**Then** each event includes required timestamp/type/correlation context  
**And** external references are linked to session records with source metadata.

## Epic 4: Model Lifecycle & In-Scene Injection

Enable model repository operations, candidate/reference selection, internet-assisted enrichment (optional), and controlled in-session geometry injection with traceable artifacts.

### Story 4.1: Model Repository Inventory and Lifecycle Operations

**Implements:** FR28, FR29, FR31, FR32

As a Human Supervisor or Lab Assistant,  
I want to view and manage model inventory operations in-session,  
So that needed assets are available during mission work.

**Acceptance Criteria:**

**Given** model repository is configured  
**When** inventory and lifecycle operations are requested  
**Then** list/spawn/remove behaviors follow repository boundary controls  
**And** each operation is persisted and auditable.

### Story 4.2: Candidate References and Optional Enrichment Selection

**Implements:** FR44, FR45, FR68

As a Human Supervisor,  
I want numbered candidate references (including optional internet-assisted enrichment),  
So that I can choose the right model direction quickly.

**Acceptance Criteria:**

**Given** a model/reference request is made  
**When** candidate references are returned  
**Then** candidates are presented in numbered selectable form via supported interaction paths  
**And** selected references are persisted as traceable artifacts.

### Story 4.3: Generated Geometry Injection with Status and Timing

**Implements:** FR30, FR69

As a Human Supervisor,  
I want generated geometry to be injected safely with status feedback,  
So that mission flow remains predictable.

**Acceptance Criteria:**

**Given** a valid model generation request  
**When** generation and injection execute  
**Then** estimated completion timing and status transitions are surfaced  
**And** success/failure outcomes are logged with recovery-safe behavior.

## Epic 5: Operational Resilience & Site Manager Governance

Enable communication reliability, health monitoring, fault recovery, and governance controls that preserve mission continuity.

### Story 5.1: Duplex Communication Monitoring and Timeout Alerts

**Implements:** FR13, FR14, FR15, FR60

As Site Manager,  
I want communication health monitored continuously,  
So that failures are detected quickly.

**Acceptance Criteria:**

**Given** an active collaboration session  
**When** acknowledgments exceed timeout thresholds  
**Then** timeout events are detected within configured limits and participant notifications are issued  
**And** monitoring events are classified and logged by communication stratum.

### Story 5.2: Recovery Orchestration and Continuity Restoration

**Implements:** FR16, FR17, FR59

As Site Manager,  
I want standardized recovery workflows,  
So that collaboration continuity is restored without losing context.

**Acceptance Criteria:**

**Given** a communication fault is detected  
**When** recovery workflow is initiated  
**Then** recovery actions execute according to policy and continuity target behavior  
**And** restored state preserves active mission context and artifacts.

### Story 5.3: Session Health, Troubleshooting, and Recovery Evidence

**Implements:** FR33, FR34, FR35, FR36, FR47

As operations staff,  
I want health and issue evidence captured,  
So that failures can be diagnosed and improved over time.

**Acceptance Criteria:**

**Given** health anomalies or failures occur  
**When** troubleshooting workflows run  
**Then** issues, applied actions, and outcomes are recorded in durable event logs  
**And** data is available for optimization/QA session review.

### Story 5.4: Prerequisite Validation and Safe Degraded Mode

**Implements:** FR46, FR48, FR49

As Site Manager,  
I want pre-session readiness checks and safe degraded operation,  
So that sessions avoid unsafe starts and can continue safely during dependency failures.

**Acceptance Criteria:**

**Given** session start is requested  
**When** prerequisites are validated  
**Then** missing critical dependencies block unsafe start with actionable messaging  
**And** degraded-mode entry preserves artifact continuity and authority model compliance.

## Epic 6: Digital Twin Data Context

Enable validated digital twin and historical data-context use in mission workflows across mandatory local/NAS pathways.

### Story 6.1: Digital Twin and Historical Context Loading

**Implements:** FR23, FR24, FR27

As a Human Supervisor,  
I want digital twin scenes and historical context loaded for missions,  
So that analysis is grounded in real operational data.

**Acceptance Criteria:**

**Given** mission data configuration exists  
**When** session context is initialized  
**Then** required digital twin and historical context are loaded and associated to mission scope  
**And** context availability is visible to participants.

### Story 6.2: Pre-Session Data Source Validation Gates

**Implements:** FR25, FR26

As Site Manager,  
I want data-source validation before mission start,  
So that invalid data pathways do not compromise session quality.

**Acceptance Criteria:**

**Given** required local/NAS data pathways are configured  
**When** pre-session checks run  
**Then** mission start gating enforces validation success criteria  
**And** validation outcomes are recorded in session metadata.

### Story 6.3: In-Session Data Context Reasoning Support

**Implements:** FR24, FR27

As a collaborator,  
I want in-session access to validated data context,  
So that diagnosis and optimization decisions are evidence-based.

**Acceptance Criteria:**

**Given** validated context is available  
**When** participants request data-informed reasoning support  
**Then** relevant context is retrievable in-session  
**And** referenced data usage is traceable in session artifacts.

## Epic 7: Knowledge Loop, Research & Outcome Intelligence

Enable mission roster capture, cross-session learning, research preload workflows, and measurable proof-of-value outputs.

### Story 7.1: Mission Roster Capture and Backlog Classification

**Implements:** FR37, FR53

As Lab Assistant,  
I want to capture ideas/tasks and classify them,  
So that mission follow-up work is organized and reusable.

**Acceptance Criteria:**

**Given** mission ideas/actions are identified  
**When** roster capture occurs  
**Then** items are persisted with timestamps and category labels  
**And** records remain available across sessions.

### Story 7.2: Cross-Session Method Memory and Recommendations

**Implements:** FR38, FR54

As Human Supervisor,  
I want recommendations from prior successful methods,  
So that I can accelerate decision quality in similar scenarios.

**Acceptance Criteria:**

**Given** historical method records exist  
**When** similarity criteria match current goals  
**Then** recommended methods are surfaced with traceable rationale  
**And** recommendation use is auditable.

### Story 7.3: Research Agent Findings and Session Preload Integration

**Implements:** FR39, FR40, FR41

As a mission team,  
I want asynchronous research findings integrated into future sessions,  
So that long-horizon investigation improves in-session decision speed.

**Acceptance Criteria:**

**Given** research tasks are executed out-of-session  
**When** findings are published  
**Then** structured findings can be linked and preloaded into target sessions  
**And** each finding maintains source and objective linkage.

### Story 7.4: Outcome Summaries, KPI Tags, and Win-Case Records

**Implements:** FR50, FR51, FR52

As product/operations stakeholders,  
I want mission outcome summaries and KPI-tagged records,  
So that value can be reviewed and demonstrated consistently.

**Acceptance Criteria:**

**Given** a mission session completes  
**When** outcome processing runs  
**Then** summary artifacts and KPI tags are generated and stored  
**And** win-case records can be linked to scenario and evidence references.

## Epic 8: QA Replay, Verification & Release Readiness

Enable deterministic replay and checkpoint evidence capture for reliability and implementation conformance verification.

### Story 8.1: Deterministic Replay Harness

**Implements:** FR55

As QA,  
I want deterministic replay of session artifacts,  
So that reliability and regression behavior can be verified repeatedly.

**Acceptance Criteria:**

**Given** valid session artifacts exist  
**When** replay mode executes under `qa-replay` profile  
**Then** replay outputs are deterministic across repeated runs  
**And** replay deviations are surfaced as conformance failures.

### Story 8.2: Mission Checkpoint Evidence Capture

**Implements:** FR56

As QA/review stakeholders,  
I want pass/fail evidence at mission checkpoints,  
So that release readiness decisions are supported by objective validation artifacts.

**Acceptance Criteria:**

**Given** mission checkpoints are defined  
**When** verification executes  
**Then** pass/fail evidence is captured with timestamped traceability  
**And** evidence is exportable for review and audit.
