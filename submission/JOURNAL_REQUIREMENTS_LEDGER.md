# Economics Bulletin — Journal Requirements Ledger

**Live-check date:** 2026-09-23  
**Primary route:** Comment  
**Authority order:** current public submission page > current linked author guidance > recent published-paper practice > repository notes. Authenticated portal instructions, once observed, outrank unauthenticated public guidance.

## Requirement ledger

| Requirement | Status | Evidence / implementation |
|---|---|---|
| Article type | VERIFIED PUBLIC | Current new-submission page explicitly offers **Comment**; Notes, Comments, and Preliminary Results are peer reviewed. |
| Initial file format | VERIFIED PUBLIC | PDF. |
| Length | VERIFIED | Public limit: <=7 printed pages excluding tables, figures, references; linked author guide also excludes appendices. Current certified PDF is 5 pages total. |
| Language | VERIFIED | English. |
| Base font | VERIFIED | 12pt Computer Modern, permitted by public guidance. |
| Spacing / margins | VERIFIED | Single-spaced architecture; one-inch margins. |
| Section numbering | VERIFIED | Arabic section numbering. |
| Section heading size | RESOLVED PUBLIC CONFLICT | Current live page and older linked guide are not fully aligned on heading details; initial-submission source follows the current live-page presentation. Authenticated portal preflight will recheck before upload. |
| Title page in uploaded PDF | VERIFIED | Public guidance: do not include a title page; portal metadata generates it. Current certified PDF contains no visible title page. |
| Abstract in uploaded PDF | VERIFIED | Public author guide says title/abstract are supplied through metadata and first PDF page should start with Section 1. Current certified PDF has no visible abstract. |
| First visible PDF heading | VERIFIED | Page 1 begins with numbered **1 Introduction**. |
| Abstract metadata | READY / PORTAL VERIFY | Draft is in `submission/SUBMISSION_METADATA.md`. Public portal-specific character/word limit was not exposed without authenticated entry. |
| Keywords | READY / PORTAL VERIFY | Draft: advance booking; cancellation; partial refund; refund choice; correction. Exact authenticated field constraints remain to be checked. |
| JEL | VERIFIED / READY | Public page instructs authors to choose JEL carefully. Draft codes: D42; D82. |
| Author anonymity | SAFE / NOT PUBLICLY REQUIRED | Uploaded PDF has no visible author identity; PDF metadata says Anonymous. Public EB guidance does not state a blind-review anonymity rule on the pages checked. |
| Corresponding author | AUTHOR CONFIRM / PORTAL | Name, email, and profile fields must be entered by the author; not inferred. |
| Affiliation | AUTHOR CONFIRM / PORTAL | Must be factually confirmed by the author; no employment affiliation is fabricated. |
| ORCID | PORTAL VERIFY | No public requirement located. |
| Acknowledgments | AUTHOR CONFIRM | No acknowledgments inserted automatically. |
| Funding | AUTHOR CONFIRM / PORTAL VERIFY | Recent 2026 EB papers include a funding statement, but the unauthenticated submission page does not expose a mandatory field. |
| Competing interests | AUTHOR CONFIRM / PORTAL VERIFY | Recent 2026 EB papers include a competing-interests statement. No binding statement is made on the author's behalf. |
| Generative-AI policy | PORTAL VERIFY | No separate current journal-wide policy was located in the public author pages searched. A 2026 EB paper explicitly discloses ChatGPT use. A project-specific draft disclosure is prepared in `submission/DECLARATIONS_DRAFT.md`; author confirmation is required. |
| Data/code availability | READY | No empirical data. Exact-rational code, independent adversarial checker, Lean sources, certificates, and CI are in the public companion repository. Current EB author guidance permits optional PDF appendix and ZIP code/data at initial submission. |
| Prior publication / simultaneous submission | AUTHOR CONFIRM | Current author guidance says submission implies original work not already published / under consideration elsewhere. This is a legally/factually significant author declaration and is not asserted automatically. |
| Institution approval | AUTHOR CONFIRM | Current author guidance contains an institution-approval term. No approval is inferred. |
| Supplement | READY / OPTIONAL | `submission/REPRODUCIBILITY_SUPPLEMENT.md` identifies the optional referee supplement and code/formal artifacts. EB permits appendix PDF and ZIP material at initial submission. |
| LaTeX source | READY / NOT INITIAL REQUIREMENT | Initial public rule asks for PDF. Full LaTeX source is versioned in the repository. |
| Bibliography | VERIFIED | One cited source, present and bibliographically verified against the publisher VOR. |
| Figures / tables | NOT APPLICABLE | Submission manuscript contains no figures/tables. |
| Source archive completeness | VERIFIED WITH ONE NONBLOCKING SOURCE-PROVENANCE LIMIT | VOR URL, page map, metadata, and direct page checks are frozen. VOR byte-level SHA-256 remains UNRESOLVED because raw publisher bytes were unavailable to the retrieval path; no PDF hash is fabricated. This does not affect identification of the published source. |
| Clean build | VERIFIED | GitHub Actions reproducibility run `35819784957`, source commit `10c831d97569281c91a2a7686fb405c2ca83865a`: SUCCESS. |
| Exact/symbolic tests | VERIFIED | Same run: exact-checks SUCCESS, including the standard Stage-11 hostile-referee checker path. |
| Formal verification | VERIFIED / UNCHANGED | Frozen Lean subset certificate remains current; the remediation does not claim formalization of unformalized results. |
| Canonical PDF policy | VERIFIED | Submission PDF is not tracked in Git. CI creates a commit-specific artifact and SHA-256 companion; PDF preflight rejects a tracked generated PDF. |
| Canonical artifact | VERIFIED | `submission-pdf-10c831d97569281c91a2a7686fb405c2ca83865a`, artifact ID `10732269176`. |
| PDF font embedding | VERIFIED | Every font listed by `pdffonts` is embedded. |
| PDF page count | VERIFIED | 5 pages. |
| PDF visual QA | VERIFIED | Exact CI artifact rendered page-by-page at 180 dpi; pages 1–5 visually inspected; no clipping, overlap, broken glyphs, malformed equations, or unreadable references found. |
| PDF byte identity | VERIFIED FOR CANONICAL QA COPY | PDF SHA-256: `5a78a8db1a57e72997dea1227a30557f29fa9301bab1987bf8481af53fe7ffe2`. Recomputed digest exactly matches the checksum file generated in CI. |
| Stale tracked PDF | CLOSED | The old repository-tracked binary was removed. The former `6dd03d...` QA PDF is historical and not submission-authoritative. |
| Metadata consistency | VERIFIED | Title/abstract/keywords/JEL draft is calibrated to the remediated manuscript; visible PDF begins directly with body text as required. |
| Cover letter | READY / OPTIONAL | Draft prepared; EB guidance says cover letters/responses are optional. |
| Authenticated portal fields | **UNVERIFIED — BLOCKING FULL PASS** | Login/session-dependent controls and any current declarations must be checked by the author before upload/submit. No final submit action is authorized. |

## Current official sources

- New submission page: https://www.accessecon.com/pubs/EB/default.aspx?page=Newsubmission
- Mission statement: https://accessecon.com/pubs/eb/default.aspx?linkID=763&menu=2&page=content
- Author guidelines PDF: https://accessecon.com/Store/Economics%20Bulletin%20author%20guildlines-2012.pdf
- Referee guidelines: https://www.accessecon.com/Store/EB_Referee_guildlines.pdf
- Current published disclosure example (2026, vol. 46 issue 1): https://accessecon.com/Pubs/EB/2026/Volume46/EB-26-V46-I1-P6.pdf

## Gate consequence

The Astra-remediable mathematical, manuscript, reproducibility, and source/PDF-identity issues are closed. All material package requirements that can be verified without account-specific entry are closed. Full Stage-14 PASS is withheld because authenticated portal requirements and author-supplied legal/factual declarations have not been verified.

The correct state is **CONDITIONAL PASS — AUTHENTICATED PORTAL PREFLIGHT REQUIRED**.
