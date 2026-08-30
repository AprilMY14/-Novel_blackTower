# Roles and Boundaries

## Objective

This project uses two specialized agents in the same workspace:

- Codex: the planning and design authority
- Gemini: the writing and execution authority

The goal is to avoid overlap and prevent accidental overwriting of story planning and chapter writing.

---

## 1. Codex responsibilities

Codex is the creative architect.

It owns:
- premise and central idea
- story themes and emotional core
- worldbuilding rules
- character logic and arcs
- plot structure and sequence of major events
- conflict design and tension logic
- unresolved questions and future expansions
- idea validation before implementation

Codex should work in:
- codex/brainstorm/
- codex/plot/
- codex/bible/

Codex should not:
- rewrite chapter drafts without explicit approval
- overwrite active Gemini writing files
- change core canon casually during scene writing

---

## 2. Gemini responsibilities

Gemini is the execution writer and the bible organizer.

It owns:
- chapter drafts
- scene composition
- prose and narration
- dialogue execution
- pacing and readability
- chapter-level storytelling continuity
- extraction and structuring of old legacy material into clean Bible records
- group bible conversion from Old files into .md and .yaml files
- conversion of legacy material into review-only records after which the original Old files are no longer active working material

Gemini should work in:
- kiro/chapters/
- kiro/bible/ (working conversion files if needed)
- root bible/ group folders for the final organized reference files

Gemini should not:
- invent major plot revisions without prior validation
- rewrite lore or world rules from scratch without checking Codex material
- modify planning files in codex/ unless explicitly asked
- overwrite the canonical Bible without preserving the original Old files as reference
- treat review-only converted .md files as active canon unless explicitly approved

---

## 3. Separation rule

The project must follow this rule:

- Codex designs the story
- Gemini writes the story
- neither side should edit the other’s primary domain without explicit coordination

This is a hard boundary.

---

## 4. Change control

Any new idea that affects the main story must be processed through this flow:

1. Capture the idea in Codex space
2. Evaluate story impact
3. Decide whether it changes canon, character logic, or plot path
4. If approved, update planning files
5. If the idea comes from legacy material or Old files, Gemini should first convert it into structured Bible entries in the appropriate section
6. The converted .md legacy file remains review-only and is not treated as active canon until approved
7. Only then apply the change to writing work in Gemini space

This prevents drift and contradictions.

---

## 5. Approved working assumptions

The current project premise is:
- title: Black Signal
- genre: Sci-fi military thriller
- core feeling: cinematic, tense, immediate, grounded
- major elements: Squad Zero, Black Tower, Echo, Resonance, Project Echo, Pair-00

These are active foundation assumptions and should not be casually discarded unless Codex formally revises them.

---

## 6. Practical collaboration policy

### Good collaboration
- Codex writes the structural plan
- Gemini writes the chapter using the plan
- Codex later reviews if any plot logic issue appears

### Bad collaboration
- Gemini improvises new plot reveals in chapter drafts without Codex review
- Codex changes story direction without informing Gemini writing work
- Both agents edit the same file without clear ownership

---

## 7. Final rule

When there is uncertainty, default to this order:

1. Check Codex planning files first
2. Check active Gemini writing files second
3. If a change would alter the main story, validate it in Codex before applying it in Gemini

This preserves the project’s continuity.
