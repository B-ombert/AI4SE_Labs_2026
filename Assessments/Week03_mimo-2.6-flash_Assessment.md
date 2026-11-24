# Assessment by mimo-2.6-flash

# Week 03 Prompting
- Awarded: 2b out of 5b
- Commentary: Tasks 1 and 2 are largely delivered: three well-formed non-ROSES, non-zero-shot prompts (ICIO, PAR, RTF), three prediction CSVs with metadata, a comparison report with a chart, and honest limitations reporting. However, explicit requirements are missed: model inference times were never measured (left blank), Task 3's report is a single sentence with no numeric per-prompt results or metric defence, and Task 4 has no deliverable at all beyond the assignment description. Note: accuracy_comparison.png could not be viewed by this model (no image input), so the visualization was judged from the report text that references it.

## Task 1
- Awarded: 1b   (max 1b)
- Commentary: Three frameworks are chosen (ICIO, PAR, RTF), correctly avoiding ROSES and zero-shot, all sourced from https://frompting.com/frameworks as required. The prompts in prompts/icio.txt, par.txt and rtf.txt are detailed, follow their respective structures faithfully, and are purpose-built for the Task 2 text-to-SQL problem (schema handling, CSV format, validation steps, anti-hardcoding rules). The report explains why each framework suits the task (e.g., ICIO's separation of instructions/context/input/output for SQL generation) and states where they were found, satisfying both required outputs.

## Task 2
- Awarded: 0.5b   (max 1b)
- Commentary: Strengths: predictions for all three prompts over the full 155 questions (predictions_icio/par/rtf.csv), metadata-rich experiment_results.csv (technique, prompt file, model identifier field, accuracy, timing columns), fresh session per prompt, prompt integrity verified by SHA-256, and a clear comparison report with accuracy figures (ICIO 27.74%, RTF 27.74%, PAR 24.52%), 0 SQL execution errors, plus an embedded chart. Weakness: the explicit requirement "measure inference times" was not fulfilled — generation_time_seconds and total_elapsed_seconds are empty for all three runs, and only local evaluator/pipeline times (~0.15–0.9 s) are reported, which the report itself admits are not model latency. The honest explanation (Copilot session tooling exposed neither model ID nor timing) mitigates but does not recover the missing measurement, hence half credit.

## Task 3
- Awarded: 0.5b   (max 1b)
- Commentary: The metric implementation exists (Task_2/data/evaluate_retrieval_predictions_f1.py): a result-set F1 over row multisets (precision/recall harmonic mean), a sensible partial-credit refinement of the original exact-multiset-match accuracy, with a self-test in __main__. However, the argumentation and defence required by the task is reduced to a single Slovak sentence (report.txt): essentially "it gives values between 0 and 1 instead of only 0 or 1, but all files came out the same." There is no discussion of whether F1 complements or replaces the original metric, no recorded numeric F1 values for any of the three prediction files, and no comparison table/report across prompts — the required report output is effectively absent beyond that one-line conclusion.

## Task 4
- Awarded: 0b   (max 2b)
- Commentary: No deliverable was submitted. The Task_4 folder contains only the assignment description Task_4.md; there is no detailed report, no tables or graphs of metric values, no statistical significance testing (e.g., McNemar/chi-square/bootstrap over the 155 paired questions), and no analysis treating prompt, model, and coding agent as factors. Nothing to assess beyond the unfulfilled specification.