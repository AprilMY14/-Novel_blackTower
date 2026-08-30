# Novel Project Workflow

## Version

Current version: 2026-08-30

This file is the active working summary for the project. It replaces the need to read old chat snapshots and archive folders unless a specific historical reference is needed.

This document is one of the core workflow files together with AGENTS.md, agent-guardrails.md, and chapter-preflight-checklist.md.

---

## 1. Project role split

The project now uses two different agent roles in the same workspace, with separate responsibilities:

### Codex
Role: creative architect / planning brain

Purpose:
- generate plot ideas
- test story logic
- shape worldbuilding and themes
- draft premise, arcs, tension, conflict structure
- decide what should exist before writing begins
- act like a novelist/editor before the prose is produced

Typical work:
- story concept
- premise and thesis
- world rules
- character logic
- arc design
- scene planning
- unresolved questions
- note collection and idea development

Files used by Codex should live under:
- codex/brainstorm/
- codex/plot/
- codex/bible/

### Gemini
Role: writing engine / implementation writer / bible extractor

Purpose:
- turn approved ideas into actual files
- organize Old files into structured Bible sources
- convert research and draft material into usable .md and .yaml records
- write chapters and scenes
- build the manuscript in a structured way
- maintain the operational writing draft
- act like the hands that produce the story text

Typical work:
- chapters/
- scene files
- narrative drafting
- chapter-by-chapter story execution
- bible extraction from legacy material
- structured group bible files in .md and .yaml format
- polishing prose after the plot is approved

Files used by Gemini should live under:
- kiro/chapters/
- kiro/bible/ (if used for working conversion files)
- kiro/notes/ (if later added)
- other writing production folders only when explicitly approved

---

## 2. Operating principle

Codex does not write final prose unless specifically asked to do so.
Gemini does not invent major plot direction without prior Codex planning unless the direction is explicitly approved.

The workflow is:
1. Codex explores and defines the idea.
2. Codex shapes the logic, stakes, and structure.
3. Gemini executes the writing from the approved direction.
4. If new ideas appear during writing, they go back to Codex for evaluation before altering the main plan.

This keeps the project from drifting into contradiction.

---

## 3. Core story direction

### Working title
Black Signal

### Genre
Sci-fi military thriller

### Core feeling
The reader should feel as if the story is unfolding in real time, not being narrated from a distance.

### Main identity
The story should feel cinematic, tense, grounded, and immediate.

---

## 4. Story foundation already established

From the earlier work captured in the old files and project bible, the core foundation includes:

- Squad Zero as a special response unit
- Black Tower as the central institutional force or hidden power structure
- Echo / resonance / signal phenomena as the central speculative element
- Project Echo as a significant operation or discovery
- Pair-00 as a high-risk or emotionally critical element
- a hidden historical event or past incident affecting the present story
- military-style tension, secrecy, and operational realism
- character differentiation by ability, role, and psychological profile

These are not random ideas. They are the active world backbone of the project.

---

## 5. Character concept map

### Main cast
- Han Mubai
  - decisive, cold, military discipline
  - short, direct speech
  - acts as the command edge

- Chen Yu
  - observant, precise, strategically minded
  - words carry meaning
  - strong emotional restraint

- Lin Yien
  - quieter, action-heavy, less verbal
  - intensity expressed through behavior rather than explanation

- Gu Yan
  - practical, terse, grounded
  - speaks only when necessary

- Song Yao
  - information-focused, concise, efficient
  - delivers key facts without wasted emotion

These roles and styles should remain stable unless Codex formally revises them.

---

## 6. Writing bible principles

The project already has a valid writing-standard guide:

- show, don't tell
- every scene must do work
- no redundant explanation
- avoid overuse of metaphors
- use sensory detail with purpose
- keep dialogue sharp and character-specific
- action must follow decision and consequence
- clarity is more important than sounding clever
- the story must feel like it is happening, not being explained

This is the standard for all Gemini writing output.

### Gemini continuity-read requirement

Before writing, revising, or converting any story content, Gemini must read the active canonical Bible records for every element it will touch. The required reading is determined by content, not merely by the target file:

- character mention, memory, action, dialogue, or introduction: matching character record and applicable relationship record;
- plot event, reveal, cause, consequence, objective, or sequence: timeline and approved plot record;
- faction, operation, institution, command structure, or loyalty: faction record;
- setting, facility, travel, or location constraint: location record;
- technology, power/capability, Echo/resonance/signal rule, or world constraint: world record.

If the work reveals information about the past, moves or changes a character capability/power, or recontextualizes an earlier event, Gemini must read the relevant older chapter(s). At minimum, this includes the chapter where the fact or capability was established and every chapter whose continuity is affected; checking only the previous chapter is insufficient.

Gemini must use the active canonical Bible and approved planning, never memory or review-only legacy conversions, as the source of truth. Missing or contradictory records require a stop for Codex/human review before prose or Bible changes proceed.

---

## 7. Folder structure and ownership

The project should now follow this rule:

### Root
- README.md
- PROJECT_WORKFLOW.md
- bible/
- plot/
- chapters/
- codex/
- kiro/
- notes/

### Codex owns
- codex/brainstorm/
- codex/plot/
- codex/bible/

### Gemini owns
- kiro/chapters/
- kiro/bible/ (working conversion of historical material into organized files)

### Shared world materials
The main project-level story bible is stored in the root-level directories under bible/ and is treated as the canonical reference set for the story world. Gemini is responsible for converting Old files into that organized structure.

### Legacy material policy
- Old files are archival reference only.
- Once converted into .md working records, those files are review-only artifacts.
- They are not treated as active canon unless explicitly re-approved.
- The active canonical source is the approved Bible and approved planning documents.

Important rule:
- Codex should generate concept and authority.
- Gemini should create writing artifacts, chapter drafts, and structured Bible files.
- Neither side should overwrite the other’s main planning folder without a clear reason.

---

## 8. Safe collaboration rules

To avoid cross-writing conflicts:

1. Codex owns planning and logic.
2. Gemini owns the draft manuscript and legacy conversion work.
3. Gemini should not rewrite Codex plot documents unless asked.
4. Codex should not overwrite chapter files unless the project is intentionally being restructured.
5. If a new idea affects the main plot, it must first be recorded in codex/ and then approved before being applied in the manuscript.
6. Old files are historical; they are not the active source of truth unless the latest version is absent.
7. Converted legacy .md files are review-only and should not drive active development unless explicitly approved.
8. Any canon-affecting change must be tracked in the change log before implementation.

---

## 9. Change log and approval states

Every major update must be tracked with:
- what changed
- why it changed
- which files were affected
- who approved it
- current state

Approval states:
- draft
- in review
- approved
- rejected
- archived

This keeps the project transparent and prevents undocumented canon drift.

---

## 10. Current active rule

The active truth of the project is:
- Codex = planning and design authority
- Gemini = execution and writing authority
- This summary file = current source of workflow understanding

When in doubt, read this file before reading old archive folders.

---

## 11. Recommended next step

The next practical move is:

1. review the legacy material in Old files and extract useful canonical content
2. convert the extracted content into group Bible files under bible/ in .md and .yaml format
3. treat the converted .md output as review-only material and do not use it as the active source unless it is approved
4. create a short planning doc under codex/plot/ with: premise, arc list, and chapter roadmap
5. create a chapter folder under kiro/chapters/ for actual draft writing
6. keep all new ideas in codex/brainstorm/ until they are approved
7. write only after the plot logic is stable
8. store all canonical and approval records in approved project files, not in legacy conversion artifacts

This keeps the project clean and prevents the two agents from stepping on each other’s work.

---

## Core workflow set

For daily work, the project relies on four files only:
- AGENTS.md
- PROJECT_WORKFLOW.md
- agent-guardrails.md
- chapter-preflight-checklist.md

These are the active operational files. Everything else is auxiliary and should be treated as optional unless specifically required.
