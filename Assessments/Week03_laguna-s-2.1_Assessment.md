# Assessment by laguna-s-2.1

# Week 03 Prompting
- Awarded: 2.5b out of 5b
- Commentary: Task 1 is well executed: three distinct, non-excluded prompting frameworks (ICIO, PAR, RTF) are chosen from frompting.com/frameworks, with one concise prompt file per framework and a report explaining the rationale and source. Task 2 is strong: all three prediction CSVs (155 rows each, with question/prompt/model metadata) and a structured report with a results table, accuracy visualization, and timing are present; inference time could not be measured due to Copilot session limitations, which is documented honestly. Task 3 is incomplete: the only artifact is a one-sentence report stating F1 was used and results matched accuracy, with no implementation file, no calculated/comparison values, and no justification; Task 4 has no student output at all (only the assignment brief remains).

## Task 1
- Awarded: 1b   (max 1b)
- Commentary: Three prompting frameworks were selected (ICIO, PAR, RTF), none of which are ROSES or zero-shot, each formulated into a dedicated prompt file (prompts/icio.txt, prompts/par.txt, prompts/rtf.txt) tailored to the SQL-generation problem. The accompanying report.txt (in Slovak) briefly explains why each framework was chosen and its expected benefit (ICIO: clear instruction/context/input/output split; PAR: problem-action-result structure; RTF: role-task-format for consistent SQL output), and states all were sourced from https://frompting.com/frameworks. The deliverables (prompt files + report, including source) match the task requirements.

## Task 2
- Awarded: 1b   (max 1b)
- Commentary: The problem is solved using the Task 1 prompts: three prediction files (predictions_icio.csv, predictions_par.csv, predictions_rtf.csv) each contain 155 predictions in the required question,predicted_sql format with preserved order. experiment_results.csv records per-technique metadata (prompt file, model identifier marked as unavailable, question/prediction counts, accuracy, execution errors). The report.md compares the three techniques with a results table (ICIO 27.74%, PAR 24.52%, RTF 27.74%, 0 SQL execution errors) and includes a visualization. A note on the image: the accuracy_comparison.png could not be viewed as an image by this text-based grader; the conclusion was therefore judged from the report text and the experiment_results.csv table. Inference/model-generation time was not measurable because the Copilot session tooling did not expose model duration or session timestamps; the student documented this limitation and instead reported evaluator and local-pipeline timings, which is a reasonable and honest effort given the constraint.

## Task 3
- Awarded: 0.5b   (max 1b)
- Commentary: The only Task 3 artifact is a one-sentence report.txt stating that an F1 score metric was used (result-set similarity yielding values between 0 and 1), but that the resulting accuracies came out the same. There is no source-code file implementing the metric, no argument for why F1 is applicable, no discussion of complementing/replacing the original accuracy metric, no calculated metric values for the Task 2 predictions, and no comparison report/tables for different prompts. The conceptual mention of F1 (a reasonable choice for SQL result-set similarity, for which a reference implementation exists in the data folder) earns partial credit only, as the implementation, calculation, and comparison requirements are not met.

## Task 4
- Awarded: 0b   (max 2b)
- Commentary: No Task 4 output was produced. The Task_4 directory contains only the assignment brief (Task_4.md); there is no analysis report, no tables/graphs, and no statistical-significance determination comparing the prompts. The task therefore has no deliverable to assess.
