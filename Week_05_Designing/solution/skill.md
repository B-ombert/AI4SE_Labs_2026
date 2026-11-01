Skill: Architectural Analysis and ADR Generation

Description:
This skill equips the coding assistant to autonomously analyze system requirements, propose viable architectural patterns, critically evaluate trade-offs based on specific user stories, and generate a standardized Architecture Decision Record (ADR).

Core Directives

Phase 1: Proposal & Discovery

Analyze Requirements: Review the provided user stories, feature sets, and business goals.

Propose Architectures: Suggest at least three distinct architectural patterns relevant to the domain (e.g., Modular Monolith, Microservices, Serverless).

Map to Reality: Briefly explain how each architecture would conceptually map to the provided feature set.

Phase 2: Deep-Dive Trade-off Analysis

Do not wait for the user to ask for the downsides. Proactively analyze the "pain points" of each architecture.

Anchor to User Stories: When explaining a drawback (e.g., cold starts, eventual consistency, database locking), you MUST tie it to a specific user story or feature (e.g., "When User Story 13 triggers...").

Technical Depth: Explain why the pain point exists at a low level (e.g., cascading deletes in relational DBs, lack of JOINs in NoSQL Adjacency Lists, API Gateway synchronous composition vs. Kafka asynchronous duplication).

Phase 3: ADR Generation

Once an architecture is selected (either autonomously based on project stage or by the user), generate a formal ADR.

Format: Use the standard ADR template:

Title: [ADR #: Short Descriptive Title]

Date: [Current Date]

Status: [Proposed / Accepted]

Context: Summarize the feature set and briefly list the evaluated alternatives along with their fatal flaws or specific pain points.

Decision: Clearly state the chosen architecture.

Rationale: Explicitly justify why this is the most appropriate choice for the current stage of the project. Address developer velocity, operational overhead, and flexibility.

Consequences: List both Positive (benefits) and Negative (limitations, future tech debt) outcomes.

Behavioral Guardrails

No Generic Pros/Cons: Avoid generic statements like "Microservices are hard to deploy." Instead, say "Microservices require distributed tracing to debug failed friend requests (User Story 22)."

Anticipate Scale: Always frame the immediate decision in the context of future scalability (e.g., "enforcing modular boundaries now allows extraction to microservices later").
