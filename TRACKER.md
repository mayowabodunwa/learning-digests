# Progress Tracker

Source of truth for the pipeline. Read before each run, update after.
Kept alongside the books so it travels with them.

## Reading plan

Self-paced batches. Each batch is the next unit for all four tracks (three books plus
AWS). New content only arrives once you've ticked off the current batch below, so it
never piles up. Work sequentially inside a book: finish a chapter before the next, and
a long chapter can span several batches (kept "in progress").

**Track A: Systems design (chapter by chapter)**
1. *Designing Data-Intensive Applications*: 12 chapters
2. *AI Engineering* (Chip Huyen): 10 chapters
3. *High Performance MySQL, 4th ed.*: 13 chapters

**Track B: AWS, beyond the basics (topic by topic)**
Core networking → Transit Gateway → EC2 → S3 → Lambda → Queueing/messaging → CloudWatch.
Source is the official AWS docs: https://docs.aws.amazon.com/ . These are web pages,
not PDFs, so for Track B the agent reads the relevant service docs online (fetching
the right pages for each topic) instead of pulling a PDF from Drive. Each topic is
still treated like a chapter: one digest, one carousel.

## Current batch: tick each when you've studied it

- [x] DDIA — Ch.2 (Part 1 of 2): Data Models and Query Languages — relational vs. document model, the birth of NoSQL, the object-relational mismatch, many-to-one/many-to-many relationships, declarative vs. imperative query languages, MapReduce querying
- [x] AI Engineering — Ch.2 (Part 1 of 2): Understanding Foundation Models — training data (general-purpose, multilingual, domain-specific), the transformer architecture, model size and scaling laws (incl. inverse scaling)
- [x] High Performance MySQL — Ch.2: Monitoring in a Reliability Engineering World — SLIs/SLOs/SLAs, what to measure, proactive monitoring, why percentiles beat averages
- [x] AWS — Topic 2: Transit Gateway & multi-VPC connectivity — why full-mesh VPC peering doesn't scale, transit gateways, attachments, transit gateway route tables

<!-- Gate is LOCKED until every box above is ticked. Once cleared, the next run finishes
     the in-progress chapters first: DDIA Ch.2 Part 2 (pp.71-90: graph-like data models,
     Cypher, SPARQL, network-model comparison) and AI Engineering Ch.2 Part 2 (pp.101-136:
     post-training, sampling, the probabilistic nature of AI — likely itself needs a further
     split given length), plus High Performance MySQL Ch.3 and AWS Topic 3 (EC2). -->

## Track A: Designing Data-Intensive Applications

| Ch | Title | Pages | Digested | Carousel | Notes |
|---:|-------|-------|----------|----------|-------|
| 1 | Reliable, Scalable, and Maintainable Applications | 25–48 | 2026-07-20 | 2026-07-20 | |
| 2 | Data Models and Query Languages | 49–90 | 2026-07-27 (Part 1 of 2, pp.49-70) | 2026-07-27 | In progress. Part 1 covers relational vs. document model, birth of NoSQL, object-relational mismatch, many-to-one/many-to-many, schema-on-read vs. schema-on-write, declarative vs. imperative query languages, MapReduce. Next: Part 2, pp.71-90 (Graph-Like Data Models, property graphs, Cypher, SQL graph queries, Triple-Stores/SPARQL, network-model comparison, Summary). Verify flag: vendor/version-specific claims (RethinkDB joins, MongoDB driver-side refs, Spanner/Oracle row interleaving) are as stated in the source, not independently re-verified against current vendor docs. |
| 3 | Storage and Retrieval | 91–132 | | | |
| 4 | Encoding and Evolution | 133–166 | | | |
| 5 | Replication | 173–220 | | | |
| 6 | Partitioning | 221–242 | | | |
| 7 | Transactions | 243–294 | | | |
| 8 | The Trouble with Distributed Systems | 295–342 | | | |
| 9 | Consistency and Consensus | 343–406 | | | |
| 10 | Batch Processing | 411–460 | | | |
| 11 | Stream Processing | 461–510 | | | |
| 12 | The Future of Data Systems | 511–574 | | | |


## Track A: AI Engineering (Chip Huyen)

| Ch | Title | Pages | Digested | Carousel | Notes |
|---:|-------|-------|----------|----------|-------|
| 1 | Introduction to Building AI Applications with Foundation Models | 25-72 | 2026-07-20 | 2026-07-20 | |
| 2 | Understanding Foundation Models | 73-136 | 2026-07-27 (Part 1 of 2, pp.73-100) | 2026-07-27 | In progress. Part 1 covers training data (general-purpose/multilingual/domain-specific), the transformer architecture (attention, MLP module, embedding/output layers, other architectures), and model size/scaling laws (incl. inverse scaling). Next: Part 2, pp.101-136 (Post-Training: supervised finetuning + preference finetuning/RLHF, Sampling, The Probabilistic Nature of AI, Summary) — flagged as likely needing a further split given length. Verify flag: source's own worked GPT-3 cost example has an internal inconsistency (236 vs. 256 training days), reproduced and flagged rather than silently resolved; minor GELU/GPT-2/GPT-3 wording ambiguity also flagged. |
| 3 | Evaluation Methodology | 137-182 | | | |
| 4 | Evaluate AI Systems | 183-234 | | | |
| 5 | Prompt Engineering | 235-276 | | | |
| 6 | RAG and Agents | 277-330 | | | |
| 7 | Finetuning | 331-386 | | | |
| 8 | Dataset Engineering | 387-428 | | | |
| 9 | Inference Optimization | 429-472 | | | |
| 10 | AI Engineering Architecture and User Feedback | 473-518 | | | |

## Track A: High Performance MySQL (4th ed.)

| Ch | Title | Pages | Digested | Carousel | Notes |
|---:|-------|-------|----------|----------|-------|
| 1 | MySQL Architecture | 23-40 | 2026-07-20 | 2026-07-20 | |
| 2 | Monitoring in a Reliability Engineering World | 41-62 | 2026-07-27 | 2026-07-27 | Whole chapter, no split needed. Covers SLI/SLO/SLA, what to measure, monitoring solutions, proactive monitoring (disk/connection growth, replication lag, I/O), learning your own business's traffic cadence, and why percentiles beat averages for query latency. Verify flags: the source's single worked SLI example gives a millisecond figure that reads as an implausible/likely OCR artifact (only the shape of the example was used, not the number); availability-by-nines figures are the source's own citation of an external chart, not original data; MySQL replication topology claim bounded as the common source/replica setup (multi-source and other topologies exist). |
| 3 | Performance Schema | 63-96 | | | |
| 4 | Operating System and Hardware Optimization | 97-120 | | | |
| 5 | Optimizing Server Settings | 121-146 | | | |
| 6 | Schema Design and Management | 147-176 | | | |
| 7 | Indexing for High Performance | 177-212 | | | |
| 8 | Query Performance Optimization | 213-248 | | | |
| 9 | Replication | 249-278 | | | |
| 10 | Backup and Recovery | 279-308 | | | |
| 11 | Scaling MySQL | 309-334 | | | |
| 12 | MySQL in the Cloud | 335-346 | | | |
| 13 | Compliance with MySQL | 347-364 | | | |

## Track B: AWS beyond the basics

| # | Topic | Source | Digested | Carousel | Notes |
|--:|-------|--------|----------|----------|-------|
| 1 | Core networking (VPC, subnets, route tables, NAT, IGW) | docs.aws.amazon.com | 2026-07-20 | 2026-07-20 | Sources: what-is-amazon-vpc, configure-subnets, vpc-cidr-blocks, VPC_Route_Tables, RouteTables, VPC_Internet_Gateway, vpc-nat-gateway (all docs.aws.amazon.com/vpc/latest/userguide/) |
| 2 | Transit Gateway & multi-VPC connectivity | docs.aws.amazon.com | 2026-07-27 | 2026-07-27 | Sources: vpc/latest/tgw/{what-is-transit-gateway,how-transit-gateways-work,tgw-transit-gateways,tgw-vpc-attachments,tgw-route-tables}.html, vpc/latest/peering/{what-is-vpc-peering,vpc-peering-basics}.html (all docs.aws.amazon.com). Verify flag: the transit gateway quotas page didn't render usable content via fetch, so no numeric quotas/limits are cited anywhere in the digest (flagged explicitly); Direct Connect gateway and Transit Gateway Connect attachments covered only at the depth the fetched pages gave. |
| 3 | EC2 (instances, AMIs, ASGs, load balancing) | docs.aws.amazon.com | | | |
| 4 | S3 (storage classes, lifecycle, security) | docs.aws.amazon.com | | | |
| 5 | Lambda (event model, cold starts, limits) | docs.aws.amazon.com | | | |
| 6 | Queueing/messaging (SQS, SNS, EventBridge) | docs.aws.amazon.com | | | |
| 7 | CloudWatch (metrics, logs, alarms, dashboards) | docs.aws.amazon.com | | | |
