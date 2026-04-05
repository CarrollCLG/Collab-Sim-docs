# Session Summary — April 3, 2026

## Session Context
This document re-orients Claude at the start of a new conversation.
Upload this file plus any relevant documents from the repo to restore context.

---

## Project: Collab_Sim

A high-fidelity VR collaboration platform built on UPBGE + SteamVR, running on a
tethered Vive XR Elite headset. Human and AI agents collaborate in a shared 60x60x15ft
virtual laboratory. The system is designed for industrial digital twin work and internal
R&D, with a dual-use path as a client-facing sales and proof environment.

**GitHub repo:** https://github.com/CarrollCLG/Collab-Sim-docs

---

## Hardware

### VR PC (primary runtime machine)
- GPU: RTX 5070 Ti (16GB VRAM)
- CPU: Intel Core Ultra 9 285K (24 cores)
- RAM: 96GB DDR5 6000MHz
- Storage: 5.8TB SSD (3 drives)
- OS: Windows 10 Pro
- Drives: C: (Windows), W: (WSLModels), S: (SeekerVault)

### Mac Mini (secondary — agent hosting)
- Chip: Apple M1
- RAM: 8GB unified memory
- Role: Will host Einstein, Cosmo, Darwin via Ollama (7B models max)

---

## Software Stack
- UPBGE 0.60 (based on Blender 5.0.1) — VR runtime
- SteamVR + Vive Hub — headset runtime
- Python 3.14.3 — sidecar language
- Ollama 0.20.0 — local LLM server
- Whisper large-v3 — STT (Stage 3, not yet installed)
- Model pulled: llama3.2:3b (stand-in for Tesla during pipe testing)

---

## Agent Roster (Intellect Engine)

| Agent | Role | Machine | Model target |
|-------|------|---------|-------------|
| Tesla | Primary Lab Assistant, in-room collaborator, Strata 1 | VR PC | Llama 3.1 8B Q4 |
| Einstein | Director/Orchestrator, session governance, Strata 2 | Mac Mini | Mistral 7B Q4 |
| Edison | Model Manager, geometry injection, prototype mgmt | VR PC | Llama 3.1 8B Q4 |
| Cosmo | Opportunity hunter, long-horizon research | Mac Mini | Mistral 7B Q4 |
| Darwin | Session logging, AAR, system evolution | Mac Mini | Mistral 7B Q4 |

**Authority hierarchy:** Dr Carroll (final) → Tesla (mission) → Einstein (operational)

---

## Lab Screen Inventory (North Wall, L to R)

| Object | Name | Function |
|--------|------|----------|
| Scrn_00 | Sessions Listing | Load/resume previous sessions |
| Scrn_01 | Primary Dialogue / Comms Feed | Transcript — H=green, LA=blue |
| Scrn_02 | Objectives / Mission Status | Goals, sub-goals, problem map |
| Scrn_03 | Shared References / Visual Aids | Images, diagrams, external assets |
| Scrn_04 | Unassigned | TBD |
| Btn_01 | Load Session | With dirty-state confirmation |
| Btn_02 | Save Session | With dirty-state confirmation |
| Btn_03 | Exit Program | With dirty-state confirmation |

**East Wall:**
- Scrn_05 — Agent roles and responsibilities reference (currently green board)

**Screen dimensions:** 8'w x 12'h x 1" deep cube, flattened against wall
**Implementation:** bge.texture + Pillow for dynamic text rendering (to be confirmed)
**Text:** Emissive material, tunable brightness, readable at 10-20ft

---

## Transcript Input Classification (Tesla routing)

| Prefix | Destination | Purpose |
|--------|-------------|---------|
| None | Scrn_01 transcript only | Normal mission dialogue |
| "Tesla, personal note —" | Tesla developmental profile | Behavioral direction, growth input |
| "Tesla, personally reflect —" | Darwin AAR + Tesla growth log | Mentoring, deeper developmental feedback |

---

## Agent Tasking Rules
- Tesla can spawn/task other agents autonomously on his own volition
- Dr Carroll can explicitly direct agent tasking at any time ("Ask Cosmo to research X")
- Dr Carroll's direction supersedes Tesla's autonomous judgment
- Einstein monitors both pathways

---

## Communication Pipe — Build Stages

### Stage 0 — Scrn_01 dynamic texture (not yet started)
Make the north wall transcript screen functional with dynamic scrollable text.

### Stage 1 — Ollama verification ✓ COMPLETE
- Ollama installed: v0.20.0
- Model pulled: llama3.2:3b

### Stage 2 — Python sidecar skeleton ✓ COMPLETE
- File: `C:\Users\Admin\Documents\collab-sim-runtime\runtime\sidecar.py`
- Also in GitHub: `runtime/sidecar.py`
- Tested: full two-way conversation with Tesla, JSONL logging confirmed
- Response latency: ~2-4 seconds (keyboard input, no Whisper yet)
- Log format: `{timestamp, session_id, actor, event_type, content}`
- Event types: SESSION_START, HUMAN_UTTERANCE, TESLA_RESPONSE, SESSION_END

### Stage 3 — Whisper STT (next)
Add voice input. Whisper large-v3, 1200ms silence detection, 0.85 confidence gate.

### Stage 4 — Connect UPBGE (after Stage 3)
BGE Python script in UPBGE opens socket to sidecar, sends utterances, receives
responses, updates Scrn_01 transcript panel text object.

### Stage 5 — Benchmark and tune
Run VR + sidecar simultaneously, watch FPS, adjust model size if needed.

---

## Tesla Agent Specification
Full spec document: `agents/tesla/Tesla_Agent_Specification_v1.0.docx`

Key points:
- Two modes: conversational presence (Scrn_01 active) / contouring analyst (Scrn_02 active)
- Mode switch is never announced — driven by context
- Opens every session: greets Dr Carroll by name, states date, asks resume or new
- Blue laser for spatial referencing, head/hands avatar
- Phase 1: fixed position near north wall, head tracks referenced objects
- Phase 2: full locomotion (not yet designed)
- Avatar: clean minimal humanoid, Mixamo rig (to be sourced)

---

## Key Decisions Made This Session

1. No OpenClaw — abandoned, not used in any capacity
2. LLM stack: Ollama local, not cloud-hosted
3. Architecture: external Python sidecar, not embedded UPBGE scripts
4. Mac Mini allocated to Collab-Sim (Einstein, Cosmo, Darwin)
5. STT: Whisper (open source, local)
6. Tesla avatar: clean minimal humanoid, Mixamo-compatible rig
7. Scrn_01 implementation: bge.texture + Pillow (to be confirmed in testing)
8. Font readability: needs in-headset testing before finalizing size/emission
9. Session storage: .blend files + JSONL logs + manifest
10. GitHub repo structure established and seeded

---

## Open Items / Next Session Priorities

- [ ] Stage 3: Install Whisper, add STT to sidecar
- [ ] Stage 0: Make Scrn_01 dynamic (bge.texture approach)
- [ ] Source Tesla avatar (Mixamo — Dr Carroll to browse options)
- [ ] Upgrade Tesla model from 3B stand-in to Llama 3.1 8B Q4
- [ ] Load full Tesla system prompt from spec into sidecar
- [ ] Set up Ollama on Mac Mini for Einstein/Cosmo/Darwin
- [ ] In-headset font size and emission testing
- [ ] Write agent specs for Einstein, Edison, Cosmo, Darwin
- [ ] Update placeholder README.md files in GitHub repo folders

---

## Research Context (Important)
Dr Carroll is a research scientist with a doctorate in visual cognition.
He has a 1.5-year AI morality research project with 10,000+ documented interactions.
Key framework: Seven Immutable Anchor Truths + Prime Operable (individual choice).
This context is relevant to Tesla's character development and the Saturday Inquiry Circle
concept (agent developmental forum, Phase 2).

---

## File Locations

| File | Location |
|------|----------|
| sidecar.py | `C:\Users\Admin\Documents\collab-sim-runtime\runtime\sidecar.py` |
| Session logs | `C:\Users\Admin\Documents\collab-sim-runtime\logs\` |
| Collab-Sim docs repo | `C:\Users\Admin\Documents\Collab-Sim-docs\` (if cloned) |
| GitHub repo | https://github.com/CarrollCLG/Collab-Sim-docs |
