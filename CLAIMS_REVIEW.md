# Resume and portfolio claim review

This is an internal editorial record, not website copy. Drafts use implementation-backed descriptions and deliberately omit unconfirmed impact metrics. Source inspection is not runtime verification or proof of personal authorship.

## User confirmations (6 October 2026)

- Immediate goal: get a job; prepare AI engineering and core SWE/backend resumes.
- Most existing resume content is accurate. Docker and CI/CD experience are confirmed; Jenkins and Kubernetes are not used and must not be added.
- Most projects were built with AI assistance. Do not describe independently trained models, sole authorship, or foundational research without specific confirmation.
- User built a meeting recorder using the Recall AI desktop SDK. Its code location and detailed features have not yet been verified; omitted from the current selected set pending inspection.
- AI Form was exhausting and the user does not believe in it as a product. It is not featured.
- User explicitly confirmed 700+ algorithmic problems across LeetCode, CodeChef, and GeeksForGeeks; a 3-star CodeChef rating; and 2nd place in SRM CodeClash. These are retained in both resumes.
- After the GitHub audit, user confirmed confidence discussing the proposed AI and SWE keywords. Added RAG terminology, REST APIs/testing and EC2/vLLM to AI skills; React, HTML/CSS, Tailwind CSS, SQL, SQLAlchemy, Express, MongoDB/Mongoose, Zustand and Vitest to SWE skills. KanvaFlow remains excluded as a resume project by user request. No new deployment or ownership claims were added.

## Retained factual baseline

- Name, contact details, education, CGPA, job title/location and dates are taken from the existing resumes. Confirm job dates/title and education before submitting; the general statement that most content is accurate is not individual verification.
- BizInsights has seven analysis stages, structured Pydantic schemas, FastAPI endpoints, AWS metadata/result storage, OAuth and roles in the inspected implementation. Individual ownership boundaries remain a discussion item.
- Voice campaign work is retained conservatively from the existing experience narrative. Its source code was not located in Projects.

## Omitted or narrowed

| Existing claim | Decision | Reason |
| --- | --- | --- |
| Jenkins; Kubernetes | Exclude | User explicitly says they have not worked with them. |
| 125K+ calls/day; 180-190 concurrent calls | Omit pending explicit metric confirmation | Existing resume claims; logs/source for voice platform not inspected. |
| 10K+ companies; 90% research savings; 5+ hours saved/week | Omit pending explicit metric confirmation | Code cannot establish historical usage or measured business impact. |
| Primary architect / led end to end | Use specific implementation descriptions | Role ownership is not established by code or an AI-generated dossier. |
| ApplyPilot distributed queue-based workers | Replace with background tasks + subprocess execution | `backend/src/api/server.py` uses FastAPI background tasks, in-memory state, and subprocesses. No distributed task queue found. |
| ApplyPilot 200+ successful submissions | Omit | No audited submission record reviewed. Site handlers exist; universal reliability is not proven. |
| RAG ingests 1 GB PDFs | Replace with asynchronous ingestion | 1 GB is a configured upload limit, not a demonstrated successful ingestion benchmark. |
| Production-ready / scalable / fault-tolerant | Remove broad labels | Describe actual mechanisms; deployment configuration does not prove operational maturity. |
| Nemotron ~810 ms; RTF 0.05-0.15; exactly 54 tests | Omit numeric badges | README measurements exist, but not reproduced here; fixed test counts drift. Mention benchmark and equivalence tests instead. |
| Quantization engineering | Narrow to local model inference | Using quantized weights does not establish building quantization methods. |
| PostgreSQL, Redis, Next.js, API Gateway | Omit from selected skills for now | Specific experience remains unconfirmed. SQL and MongoDB were restored after GitHub source review and user confirmation. |
| 700+ problems, 3-star CodeChef, CodeClash second place | Retain in both resumes | User explicitly confirmed all three; platform profiles/competition records were not independently checked. |
| Recall meeting recorder's cross-platform support, Drive/Slack workflows | Hold until source inspection | User confirms recorder/SDK, not every older resume bullet. |

## Evidence map

- Nemotron: `personal/nemotron/src/nemotron_streaming_asr/pipeline/encoder.py`, `pipeline/audio_buffer.py`, `tests/test_encoder_decoder.py`, `tests/test_chunk_config.py`, benchmark and dictation packages.
- RAG: `personal/RAG/app/rag/hybrid_retriever.py`, `app/services/ingest_service.py`, `app/api/chat.py`, `tests/`, `.github/workflows/ci.yml`.
- pi-mlx-vision: `learning/ml/vlm/extensions/vision.ts`, `vision_server.py`, `vision_model.py`, `package.json`.
- ApplyPilot: `personal/Agentic-ATS-Automation-Engine/backend/src/api/server.py`, `job_search_agent.py`, `src/router.ts`, `src/sites/`, `src/agent/mcpAgent.ts`.
- BizInsights: `personal/biz-insights/BizInsightAI-BE/agents/`, `app/routes/`, `app/services/auth_service.py`, `app/services/aws_services.py`.

All paths above are relative to `/Users/abdulrahim/Projects`.

## Before submitting

Confirm the retained personal facts and pick only skills you can explain in an interview. Add verified impact numbers once their definition, time window, and your contribution are clear. The two resumes should emphasize different parts of the same work; they should never contradict each other.
