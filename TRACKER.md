# Progress Tracker

Source of truth for the pipeline. Read before each run, update after.
Kept alongside the books so it travels with them.

## Reading plan

**Focused scope (set 2026-08-09).** Batches draw ONLY from the topics listed below.
Everything else in these books is **parked**, including chapters that were left part-way
through. Do not resume a parked chapter, and do not "finish" a book sequentially: the
scope below replaces the old cover-to-cover plan.

**Track A: books**
1. *Designing Data-Intensive Applications*: **Ch.4, Ch.10, Ch.11** (in that order)
2. *AI Engineering* (Chip Huyen): **Ch.5 onwards** (5, 6, 7, 8, 9, 10 in order)
3. *High Performance MySQL, 4th ed.*: **Ch.6, Ch.7, Ch.8** (in that order)

**Track B: AWS** — four service areas, covered **concept by concept** and revisited in
**rotation**: `S3 → EC2 → VPC → CloudWatch → S3 → …`. Each batch takes the next unstarted
concept from whichever area is next in the rotation (finish any in-progress concept
first). These four areas are the standing scope; keep circling them until every concept
listed is covered, then go deeper on the same services rather than moving to new ones.

**Parked, do not produce:** AI Engineering Ch.2 Part 3, High Performance MySQL Ch.3
Part 2, DDIA Ch.3, and every chapter not named above. They stay published in the library
for reference, they are simply not continued.

## Current batch: tick each when you've studied it

- [ ] DDIA — Ch.4 (Part 2, final): Modes of Dataflow (`docs/digests/ddia-ch04-part2-modes-of-dataflow.html`)
- [ ] AI Engineering — Ch.5 (Part 2, final): Defensive Prompt Engineering — Attacks, Extraction & Defenses (`docs/digests/ai-eng-ch05-part2-defensive-prompting.html`)
- [ ] High Performance MySQL — Ch.6 (Part 2, final): Schema Management (`docs/digests/hpmysql-ch06-part2-schema-management.html`)
- [ ] AWS — Topic 4: Security Groups and Network ACLs in Depth (`docs/digests/aws-04-security-groups-nacls.html`)

## Track A: Designing Data-Intensive Applications

Focus: Ch.4, Ch.10, Ch.11. Nothing else from this book.

| Ch | Title | Pages | Digested | Carousel | Notes |
|---:|-------|-------|----------|----------|-------|
| 4 | Encoding and Evolution | 133–166 | 2026-08-09 (Pt.1, pp.133–150); 2026-08-18 (Pt.2, final, pp.150–162) | 2026-08-09 (Pt.1); 2026-08-18 (Pt.2, final) | Done. Part 2 = Modes of Dataflow (databases, REST/RPC, message brokers, distributed actor frameworks) through the chapter's own Summary. Chapter 4 is fully covered; PDF pages 162–166 are references/Part II divider, not chapter content. **Next DDIA unit:** Chapter 10, Batch Processing. |
| 10 | Batch Processing | 411–460 | | | |
| 11 | Stream Processing | 461–510 | | | |

*Already published (do not redo):* Ch.1; Ch.2 Parts 1 and 2.
*Parked:* Ch.3, 5, 6, 7, 8, 9, 12.

## Track A: AI Engineering (Chip Huyen)

Focus: Ch.5 onwards, in order. Ch.2 is parked mid-chapter on purpose (Part 3 will not
be produced); Ch.3 and Ch.4 are skipped.

| Ch | Title | Pages | Digested | Carousel | Notes |
|---:|-------|-------|----------|----------|-------|
| 5 | Prompt Engineering | 235-276 | 2026-08-09 (Pt.1, pp.235–258); 2026-08-18 (Pt.2, final, pp.259–276) | 2026-08-09 (Pt.1); 2026-08-18 (Pt.2, final) | Done. Part 2 = Defensive Prompt Engineering (prompt extraction, jailbreaking/injection, information extraction, prompt-level and system-level defenses) through the chapter's own Summary. **Next AI Engineering unit:** Chapter 6, RAG and Agents. |
| 6 | RAG and Agents | 277-330 | | | |
| 7 | Finetuning | 331-386 | | | |
| 8 | Dataset Engineering | 387-428 | | | |
| 9 | Inference Optimization | 429-472 | | | |
| 10 | AI Engineering Architecture and User Feedback | 473-518 | | | |

*Already published (do not redo):* Ch.1; Ch.2 Parts 1 and 2.
*Parked:* Ch.2 Part 3, Ch.3, Ch.4.

## Track A: High Performance MySQL (4th ed.)

Focus: Ch.6, Ch.7, Ch.8. Nothing else from this book.

| Ch | Title | Pages | Digested | Carousel | Notes |
|---:|-------|-------|----------|----------|-------|
| 6 | Schema Design and Management | 147-176 | 2026-08-09 (Pt.1, pp.147–168); 2026-08-18 (Pt.2, final, pp.168–176) | 2026-08-09 (Pt.1); 2026-08-18 (Pt.2, final) | Done. Part 2 = the closing ENUM/NULL gotchas plus Schema Management (source control, Flyway/Liquibase/Skeema/Vitess, native DDL vs. pt-online-schema-change vs. gh-ost, CI/CD pipeline design) through the chapter's own Summary. **Next High Performance MySQL unit:** Chapter 7, Indexing for High Performance. |
| 7 | Indexing for High Performance | 177-212 | | | |
| 8 | Query Performance Optimization | 213-248 | | | |

*Already published (do not redo):* Ch.1; Ch.2; Ch.3 Part 1.
*Parked:* Ch.3 Part 2, Ch.4, Ch.5, Ch.9–13.

## Track B: AWS — four areas, in rotation

Cover the next unstarted concept from the next area in the rotation each batch. Finish an
in-progress concept before starting the next. Source is the official AWS docs
(https://docs.aws.amazon.com/); fetch the relevant service pages for each concept.

### S3 (every concept)
| # | Concept | Digested | Carousel | Notes |
|--:|---------|----------|----------|-------|
| 1 | Buckets, objects, keys, the flat namespace, durability & consistency model | | | |
| 2 | Storage classes & lifecycle policies (incl. Intelligent-Tiering, Glacier tiers) | | | |
| 3 | Versioning, delete markers, MFA delete | | | |
| 4 | Encryption: SSE-S3, SSE-KMS, DSSE-KMS, SSE-C, bucket keys | | | |
| 5 | Access control: bucket policies, IAM, ACLs, Block Public Access, access points | | | |
| 6 | Replication: CRR/SRR, Replication Time Control, batch replication | | | |
| 7 | Presigned URLs, CORS, static website hosting | | | |
| 8 | Event notifications and EventBridge integration | | | |
| 9 | Multipart upload, Transfer Acceleration, byte-range fetches | | | |
| 10 | Object Lock, retention & legal hold, Inventory, Storage Lens | | | |

### EC2 (every concept)
| # | Concept | Digested | Carousel | Notes |
|--:|---------|----------|----------|-------|
| 1 | Instances & AMIs: types/families, lifecycle, custom AMIs, stop vs. terminate | 2026-07-30 (Pt.1); 2026-08-09 (Pt.2, final) | 2026-07-30 (Pt.1); 2026-08-09 (Pt.2, final) | Done. Part 1 = Instances & AMIs (2026-07-30). Part 2 = Auto Scaling Groups & Elastic Load Balancing at an intro/pairing level (2026-08-09); deeper ASG/ELB detail is reserved for concepts 4 and 5 below. |
| 2 | Purchasing options: on-demand, reserved, savings plans, spot | | | |
| 3 | EBS volumes, snapshots, instance store | | | |
| 4 | Elastic Load Balancing in depth: ALB vs. NLB vs. GWLB, target groups, health checks | | | |
| 5 | Auto Scaling in depth: launch templates, scaling policies, lifecycle hooks, warm pools | | | |
| 6 | Systems Manager (SSM): Session Manager, Run Command, Patch Manager, Parameter Store | | | |
| 7 | Instance metadata (IMDSv2), user data, instance profiles & IAM roles | | | |
| 8 | Placement groups, Nitro, dedicated hosts vs. dedicated instances | | | |
| 9 | Security groups & key pairs from the instance's point of view | | | |
| 10 | Instance monitoring, status checks, auto recovery | | | |

### VPC (every concept)
| # | Concept | Digested | Carousel | Notes |
|--:|---------|----------|----------|-------|
| 1 | Core networking: VPC, subnets, route tables, IGW, NAT gateway | 2026-07-20 | 2026-07-20 | Done. |
| 2 | Transit Gateway & multi-VPC connectivity | 2026-07-27 | 2026-07-27 | Done. |
| 3 | Security groups and network ACLs in depth | 2026-08-18 | 2026-08-18 | Done. Stateful security groups (instance/ENI level, allow-only) vs. stateless network ACLs (subnet level, allow+deny, ordered rules), ephemeral return-traffic ports, and default vs. custom rule sets, grounded in the live AWS VPC User Guide. |
| 4 | VPC endpoints: gateway vs. interface, and PrivateLink | | | |
| 5 | DNS in a VPC: Route 53 Resolver, private hosted zones, DHCP option sets | | | |
| 6 | Flow Logs and traffic mirroring | | | |
| 7 | IPv6 in a VPC, egress-only internet gateway | | | |
| 8 | VPC peering in depth: limits, CIDR overlap, cross-account/region | | | |
| 9 | Site-to-Site VPN, Direct Connect, hybrid routing | | | |
| 10 | VPC sharing with RAM, prefix lists, route evaluation order | | | |

### CloudWatch (every concept)
| # | Concept | Digested | Carousel | Notes |
|--:|---------|----------|----------|-------|
| 1 | Metrics: namespaces, dimensions, resolution, custom metrics | | | |
| 2 | Alarms: static, anomaly detection, composite, and alarm actions | | | |
| 3 | Logs: log groups/streams, retention, metric filters, subscription filters | | | |
| 4 | Logs Insights query language | | | |
| 5 | Dashboards and cross-account / cross-region observability | | | |
| 6 | The CloudWatch agent and Embedded Metric Format | | | |
| 7 | EventBridge: rules, patterns, schedules, and its relation to CloudWatch Events | | | |
| 8 | Synthetics canaries and RUM | | | |
| 9 | Container/Lambda Insights, ServiceLens, X-Ray tracing | | | |
