# Resume audit — 6 October 2026

Read-only assessment of resume content against local projects and public GitHub source. No resume changes made in this audit. Repository code establishes available implementation, not individual ownership or successful deployment. Personal contributions to newly found projects and the AWS deployment were requested from the user.

## Most useful omissions

- Frontend: React, TypeScript, Tailwind CSS, Zustand, Vitest and React Testing Library are present in KanvaFlow. Its virtual list, normalized state, URL-synchronized filters and custom pointer-based drag/drop provide concrete frontend engineering examples. Presence is simulated; do not claim a collaborative backend.
- Full stack: CodeSync contains React UI and an Express/Mongoose backend. BizInsights contains React/TypeScript, TanStack Query, protected routes and FastAPI services. Confirm which parts the user implemented before describing full-stack work experience.
- Relational data: movie-booking-system contains SQLAlchemy models/session management, PostgreSQL setup documentation and route tests. DBMS task repositories contain actual SQL joins and aggregations. SQL and SQLAlchemy can be useful SWE keywords; PostgreSQL operational experience requires confirmation.
- AI serving: qwen-aws-serving documents an EC2 GPU/vLLM/Docker deployment and troubleshooting. It is a runbook repository, not proof of a running deployment. Confirm the user executed it before adding EC2, vLLM and GPU-serving experience; omit copied cost/performance measurements until verified.
- Explicit vocabulary: spell out Retrieval-Augmented Generation (RAG), hybrid search, vector embeddings, cross-encoder reranking, LLM integration, asynchronous processing and event-driven workflows where the existing implementation supports them. AI skills currently omit REST APIs/testing; those can replace lower-priority jargon if space is limited.
- Existing impact: historical call-volume/company-research metrics are absent from the current PDFs. Resolve the claim ledger against the user's confirmations and establish exact measurement definitions before restoring figures. Do not manufacture new metrics.

## Project selection

| Project | Best use | Evidence and limits |
| --- | --- | --- |
| Nemotron Streaming ASR | AI/local inference | Already represented; substantial stateful streaming and equivalence-test implementation. |
| PDF RAG API | Both resumes | Already represented; retrieval, APIs, background ingestion, tests and Docker. |
| KanvaFlow | General SWE/frontend | Strong missing UI example; source supports state architecture and virtualization. No real collaboration service. |
| pi-mlx-vision | Backend/developer tooling or AI tool integration | Already represented in SWE; persistent process protocol and model lifecycle are distinctive. |
| AI Meeting Recorder | Desktop/integration SWE | User previously confirmed building it; newly inspected Electron/Recall SDK lifecycle handling, partial/final transcripts, IPC and bounded transcript UI. Do not claim on-device transcription or Drive/Slack integrations. |
| qwen-aws-serving | AI inference/cloud roles | Conditional on personal execution of the documented deployment. |
| CodeSync | Full-stack roles | React/Express/Mongoose and scraper integration; older and less distinctive than KanvaFlow. |
| Movie booking system | SQL/backend-specific applications | SQLAlchemy relational models, sessions, bookings/admin routes and test files; useful supporting skill evidence. |
| ApplyPilot | Agent/browser-automation roles | Keep as a tailored choice; not mandatory in every resume. |
| tap-whisper | Speech-focused applications | Overlaps Nemotron; avoid spending two slots on dictation by default. |
| AI Form, tutorial clones, basic exercises | Supporting GitHub only | User dislikes AI Form. Basic examples offer less differentiation than the above. |

## Recommended editing direction

Keep three substantial projects per one-page resume. For a broad SWE application, PDF RAG + KanvaFlow + pi-mlx-vision is a useful balance; the meeting recorder can replace vision for desktop/integration roles. For AI applications, retain Nemotron + RAG and select the third project for the role: ApplyPilot for agents, pi-mlx-vision for local multimodal tools, or the confirmed AWS deployment for inference/cloud positions. Do not add every project or skill to both resumes.

## Public source references inspected

- https://github.com/abdulchotu7/KanvaFlow — README, package manifest, store, virtual list, presence simulation and drag/drop manager.
- https://github.com/abdulchotu7/AI_Meeting_Recorder — README, manifest, main process, renderer and preload bridge.
- https://github.com/abdulchotu7/CodeSync — backend controller/schema/manifest and frontend display page.
- https://github.com/abdulchotu7/movie-booking-system — README, database session setup, booking model and routes.
- https://github.com/abdulchotu7/FeedB — Mongoose user/post schemas.
- https://github.com/abdulchotu7/dbms_task_2 — SQL query examples.
- https://github.com/abdulchotu7/qwen-aws-serving — matching local README inspected.

Public repository inventory was retrieved using GitHub's API. Project execution, tests and historical benchmarks were not rerun for this content audit. Private repositories were not accessible through the public inventory.
