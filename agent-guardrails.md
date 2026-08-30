# Agent Guardrails

This file is the protection layer for workflow safety.

## Purpose

These rules prevent:
- wrong-agent execution
- accidental edits to workflow configuration files
- edits to protected project files by the wrong agent
- silent drift between Codex planning and Gemini writing

---

## 1. Mandatory route check

Before any work begins, the agent must classify the request.

### Route to Codex
Use Codex for:
- plot ideas
- premise development
- arcs and tension design
- worldbuilding
- story logic
- canon decisions

### Route to Gemini
Use Gemini for:
- chapter writing
- scene drafting
- prose execution
- Bible conversion from legacy material
- review-only conversion work

### Route to human maintainer
Use human maintainer for:
- workflow configuration changes
- protected file edits
- review approval decisions
- any change to canon rules or workflow policy

---

## 2. Protected files

These files are protected and must not be edited by Codex or Gemini without direct approval:
- AGENTS.md
- PROJECT_WORKFLOW.md
- agent-guardrails.md
- chapter-preflight-checklist.md

If an agent is asked to modify one of these files, it must stop and request manual confirmation.

---

## 3. Ownership boundaries

### Codex may edit
- codex/
- plot/
- bible/
- notes/ideas/
- notes/unresolved/

### Gemini may edit
- kiro/
- chapters/
- kiro/bible/
- notes/research/

### Neither agent may edit the other's root planning or workflow files without approval.

---

## 4. Warning behavior

If a user request or instruction is mismatched,
 the agent must stop and warn with a short, firm message such as:

- This task belongs to Codex, not Gemini.
- This task belongs to Gemini, not Codex.
- This file is protected workflow metadata.
- Please confirm before continuing.

---

## 5. Approval gate

Any task that affects:
- plot direction
- character arc
- world rules
- canon
- faction logic
- timeline logic
- workflow rules

must be reviewed by the human maintainer or by Codex before implementation.

---

## 6. Final rule

No agent may silently reconfigure the workflow or rewrite protected project configuration files.
The workflow is not a free-edit zone.
The process must be explicit, reviewable, and traceable.
