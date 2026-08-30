# AGENTS

This file is the mandatory entry point for all agent work in this project.

Every agent must read this file before beginning any task.

---

## 1. Project roles

### Codex
Role: Story architect and planner

Primary responsibilities:
- generate premise and ideas
- define story logic and structure
- build plot arcs, character logic, and tension design
- maintain worldbuilding decisions
- validate whether an idea belongs in the main canon

Should read before work:
- AGENTS.md
- PROJECT_WORKFLOW.md
- codex/plot/
- codex/bible/
- codex/brainstorm/

### Gemini
Role: Writer and Bible organizer

Primary responsibilities:
- convert legacy notes and Old files into structured Bible records
- write chapters and scenes
- maintain story draft continuity
- transform approved planning into readable manuscript work
- keep the working Bible organized in .md and .yaml files
- convert legacy material into review-only .md records after which the original Old files are no longer treated as active source material

Should read before work:
- AGENTS.md
- PROJECT_WORKFLOW.md
- kiro/bible/README.md
- kiro/chapters/
- bible/

---

## 2. Mandatory workflow sequence

Before any new work, each agent must follow this sequence:

1. Read AGENTS.md
2. Read PROJECT_WORKFLOW.md
3. Read roles-and-boundaries.md
4. Read the relevant folder or file for the task
5. Only then begin execution

This prevents drift and avoids duplicate work.

---

## 3. Task routing rules

### If the task is plot/idea/worldbuilding
Read:
- AGENTS.md
- PROJECT_WORKFLOW.md
- codex/plot/
- codex/bible/

Then act as Codex.

### If the task is chapter writing or manuscript drafting
Read:
- AGENTS.md
- PROJECT_WORKFLOW.md
- kiro/bible/README.md
- kiro/chapters/
- every relevant Bible section, using the Gemini context-read protocol below
- earlier chapter(s) required by the same protocol

Then act as Gemini.

### If the task is cleaning or converting Old files
Read:
- AGENTS.md
- PROJECT_WORKFLOW.md
- kiro/bible/README.md
- .kiro/steering/Old files/
- relevant root bible section

Then act as Gemini and convert materials into structured records.

Important rule:
- Once a legacy file has been converted into a .md working record, it becomes review-only reference material.
- It is not treated as the active working source for the current canon unless explicitly re-approved.
- The active canonical source is the approved Bible and project plan, not the Old files or their converted copies.

### Gemini context-read protocol (mandatory)

Before Gemini writes, revises, converts, or otherwise touches story content, Gemini must identify every story element in scope and read the matching active canonical source. Reading a generic or nearby Bible file is not sufficient.

- A named, present, recalled, or newly introduced character requires the relevant `bible/characters/` record and any relationship record that affects the interaction.
- Plot events, objectives, reveals, causes, consequences, or chronology require the relevant `bible/timeline/` and plot/approved-plan records.
- Factions, organizations, authority, operations, or allegiance require the relevant `bible/factions/` record.
- Locations, travel, facility details, or geographic constraints require the relevant `bible/locations/` record.
- Technology, Echo/resonance/signal phenomena, capabilities, limitations, or other setting rules require the relevant `bible/world/` record.
- When information from the past is revealed, a character's power/capability changes or is moved, or an earlier event is reinterpreted, Gemini must also read the affected earlier chapter(s), not only the immediately preceding chapter. This includes the chapter where the fact, capability, or event was first established and any chapter whose continuity the new disclosure changes.

Gemini must not rely on memory, summaries, or legacy/review-only material in place of these reads. If the needed canonical record is absent or conflicts with the draft, Gemini must stop and request Codex/human review before introducing or changing the material.

---

## 4. Ownership boundaries

### Codex owns
- plot
- premise
- conflict design
- story architecture
- idea validation
- canon decisions

### Gemini owns
- chapter writing
- scene drafting
- prose execution
- Bible extraction and conversion
- structured archival cleanup

The two domains must not overwrite each other without clear review.

---

## 5. Decision gate

If a task changes any of the following, it must be recorded and approved before implementation:
- plot direction
- major character arc
- world rules
- story canon
- faction or timeline logic
- major event consequences

For such tasks:
- Codex should review first
- Gemini should implement only after the update is approved

---

## 6. Default working rule

When there is ambiguity:
- prefer Codex for story decisions
- prefer Gemini for writing and organization
- read the workflow files before making a change
- never act from memory alone when the project structure is involved

---

## 7. Required file map

- AGENTS.md — required entry file
- PROJECT_WORKFLOW.md — project operating model
- agent-guardrails.md — protection rules
- chapter-preflight-checklist.md — chapter gate
- codex/ — planning and concept space
- kiro/ — writing and conversion space
- bible/ — canonical world reference
- chapters/ — manuscript work
- .kiro/steering/Old files/ — archived legacy material

---

## 8. Final rule

This project is run as a split workflow:
- Codex creates the map
- Gemini executes the journey
- both must start by reading the workflow files

No work begins without that read sequence.
