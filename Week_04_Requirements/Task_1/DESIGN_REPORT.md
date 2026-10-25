# Agentic Network Design Report

## 1. Purpose

The network refines a directory of mixed software-related text and email documents into a single structured requirements specification. It uses LangGraph to coordinate LLM-based analysis, review, and a deterministic validation step. Input paths are supplied at runtime; no corpus filename is hard-coded.

## 2. Architecture and node responsibilities

1. **Load (deterministic):** recursively discovers `.txt`, `.eml`, `.md`, `.rst`, and `.text` files beneath the supplied directory, reads UTF-8 text, and records relative paths for traceability.
2. **Extract (LLM):** processes each source document independently. It identifies atomic functional, reporting, security, data, and non-functional requirements; preserves source paths and evidence; and ignores unrelated anecdotes.
3. **Merge (LLM):** consolidates semantically duplicate requirements, merges their source lists, standardizes vocabulary, assigns priorities, adds testable acceptance criteria, and records rejected/conflicting candidates in a blacklist.
4. **Review (LLM):** compares the proposed specification with the complete source corpus to find omissions, duplicates, conflicts, vague language, unsupported assumptions, and traceability gaps.
5. **Feedback (deterministic):** feeds reviewer-suggested missing requirements and blacklist additions back into the consolidation stage.
6. **Validate (deterministic):** checks required fields, valid priority labels, source paths, and normalized duplicates; assigns sequential IDs (`REQ-001`, ...).
7. **Finish (deterministic):** writes one Markdown specification with a priority legend, requirements, source traceability, acceptance criteria, blacklist, and quality-control notes.

## 3. Graph and feedback loop

The principal path is `load → extract → merge → review → feedback → validate`. If the reviewer identifies issues, the graph routes from validation back to `merge`. The loop is bounded to two repair rounds to prevent runaway API costs. After the limit, unresolved issues are included in the output's quality-control notes instead of being silently hidden.

## 4. Models

The defaults use three distinct model identifiers from the assignment's provided list:

- Extraction: `gpt-5.6-luna`
- Consolidation: `gpt-6-luna`
- Review: `gpt-5.4-nano`

They can be overridden using `REQ_MODEL_EXTRACT`, `REQ_MODEL_MERGE`, and `REQ_MODEL_REVIEW`. The code loads `OPENAI_API_KEY` from the local `.env` file (using `python-dotenv`) or the process environment and never embeds the key in source code. The `.env` file is excluded by `.gitignore`.

## 5. Output conventions

- **One document:** Markdown, optionally accompanied by machine-readable JSON.
- **Unique IDs:** deterministic sequential IDs are assigned after each validation pass.
- **Deduplication:** semantic consolidation is handled by the merge agent; Python also checks normalized exact duplicates.
- **Traceability:** every requirement retains relative paths of all contributing source documents.
- **Name and description:** each requirement has a concise name and paragraph description.
- **Priority:** P1 critical; P2 high; P3 medium; P4 low/optional. The legend is included in the output.
- **Consistency and conflicts:** the reviewer looks for terminology drift and contradictions; rejected candidates go to a blacklist with reasons.
- **Completeness:** the reviewer sees all source documents and explicitly proposes missing requirements.

## 6. Running the network

Install dependencies:

```bash
python -m venv .venv
# Linux/macOS/WSL:
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Set the API key in the shell, then run with the input directory (not an individual filename):

```bash
export OPENAI_API_KEY="your-key"
python requirements_network.py --input-dir ./corpus -o requirements.md --json-output requirements.json
```

PowerShell equivalent:

```powershell
$env:OPENAI_API_KEY = "your-key"
python requirements_network.py .\corpus -o requirements.md --json-output requirements.json
```

The directory can contain nested folders. The script recursively discovers supported file types.

## 7. Limitations and design decisions

- The API must have access to the model identifiers provided by the course. If a model identifier is unavailable to the account, set the corresponding environment variable to another permitted model.
- LLM semantic deduplication and completeness review are probabilistic. The deterministic node checks structural invariants, not the meaning of every requirement.
- The source corpus may contain conflicting or tentative statements. The network should preserve ambiguity, resolve only when evidence supports a decision, and record discarded candidates rather than silently deleting them.
- A human should review priorities and conflicts before implementation.
- Extraction invokes the model once per source document, improving traceability and reducing the chance that a long corpus is truncated, but it can use more API calls than a single-batch approach.

## 8. Specification coverage

| Spec | Implementation |
|---|---|
| ANS1: at least 3 LLM nodes | Extract, merge, review |
| ANS2: deterministic node | Load, feedback, validate, finish |
| ANS3: feedback loop | Validate conditionally routes back to merge |
| ANS4: at least 3 models | Three configurable model IDs |
| ANS5: LangGraph | `StateGraph` with conditional edges |
| OS1: single document | One Markdown requirements specification |
| OS2: unique identifiers | `REQ-###` IDs |
| OS3: no semantic duplicates | Merge agent plus deterministic duplicate warning |
| OS4: traceability | Relative source paths on each requirement |
| OS5: name and paragraph | Required `name` and `description` fields |
| OS6: priorities | P1–P4 and an in-document legend |
| OS7: consistency | Review agent checks vocabulary and contradictions |
| OS8: completeness | Review agent compares requirements against all source documents |
| OS9: blacklist | Separate discarded-candidates section with reasons and sources |
