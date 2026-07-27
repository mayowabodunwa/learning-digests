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

- [ ] DDIA — Ch.2 (Part 1 of 2): Relational Model vs. Document Model (digest + carousel)
- [ ] AI Engineering — Ch.2 (Part 1 of 2): Understanding Foundation Models — Training Data & Model Design (digest + carousel)
- [ ] High Performance MySQL — Ch.2: Monitoring in a Reliability Engineering World (digest + carousel)
- [ ] AWS — Topic 2: Transit Gateway & multi-VPC connectivity (digest + carousel)

## Track A: Designing Data-Intensive Applications

| Ch | Title | Pages | Digested | Carousel | Notes |
|---:|-------|-------|----------|----------|-------|
| 1 | Reliable, Scalable, and Maintainable Applications | 25–48 | 2026-07-20 | 2026-07-20 | |
| 2 | Data Models and Query Languages | 49–90 | 2026-07-27 (Part 1 of 2) | 2026-07-27 (Part 1 of 2) | Part 1 = pages 49–63, "Relational Model Versus Document Model" (digest: ddia-ch02-relational-vs-document). Part 2 still due: pages 64–90, "Query Languages for Data" + "Graph-Like Data Models" (starts right at the "Query Languages for Data" heading on p.64). |
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
| 2 | Understanding Foundation Models | 73-136 | 2026-07-27 (Part 1 of 2) | 2026-07-27 (Part 1 of 2) | Part 1 = pages 73–101, "Training Data" + "Modeling" (architecture & size) (digest: ai-eng-ch02-training-data-modeling). Part 2 still due: pages 102–136, "Post-Training" + "Sampling" (starts right at the "Post-Training" heading on p.102). |
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
| 2 | Monitoring in a Reliability Engineering World | 41-62 | 2026-07-27 | 2026-07-27 | Full chapter in one digest (hpmysql-ch02-monitoring). Book's own printed pagination for this chapter is 19–39; 41–62 is the PDF page index (kept for consistency with the cached-range convention). |
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
| 2 | Transit Gateway & multi-VPC connectivity | docs.aws.amazon.com | 2026-07-27 | 2026-07-27 | Sources: what-is-transit-gateway, how-transit-gateways-work, tgw-route-tables (all docs.aws.amazon.com/vpc/latest/tgw/), invalid-peering-configurations (docs.aws.amazon.com/vpc/latest/peering/) |
| 3 | EC2 (instances, AMIs, ASGs, load balancing) | docs.aws.amazon.com | | | |
| 4 | S3 (storage classes, lifecycle, security) | docs.aws.amazon.com | | | |
| 5 | Lambda (event model, cold starts, limits) | docs.aws.amazon.com | | | |
| 6 | Queueing/messaging (SQS, SNS, EventBridge) | docs.aws.amazon.com | | | |
| 7 | CloudWatch (metrics, logs, alarms, dashboards) | docs.aws.amazon.com | | | |
