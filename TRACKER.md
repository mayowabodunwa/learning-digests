# Progress Tracker

Source of truth for the pipeline. Read before each run, update after.
Kept alongside the books so it travels with them.

## Reading plan

**Focused scope (set 2026-08-09).** Batches draw ONLY from the topics listed below.
Everything else in these books is **parked**, including chapters that were left part-way
through. Do not resume a parked chapter, and do not "finish" a book sequentially: the
scope below replaces the old cover-to-cover plan.

**Track A: books**
1. *Designing Data-Intensive Applications*: **Ch.4, Ch.5, Ch.6, Ch.7, Ch.10, Ch.11** (in that order)
2. *AI Engineering* (Chip Huyen): **Ch.5 onwards** (5, 6, 7, 8, 9, 10 in order)
3. *High Performance MySQL, 4th ed.*: **Ch.6, Ch.7, Ch.8** (in that order)

**Track B: AWS** — four service areas, covered **concept by concept** and revisited in
**rotation**: `S3 → EC2 → VPC → CloudWatch → S3 → …`. Each batch takes the next unstarted
concept from whichever area is next in the rotation (finish any in-progress concept
first). These four areas are the standing scope; keep circling them until every concept
listed is covered, then go deeper on the same services rather than moving to new ones.

**How AWS digests are labelled.** Each area is its own track in the library: set the
manifest `book` to `AWS S3`, `AWS EC2`, `AWS VPC` or `AWS CloudWatch`, and set `ch` to
`Concept N`, where N is that concept's number in the area table below (so S3 row 4 is
`Concept 4`). Do NOT use a single running `Topic N` across all of AWS: the areas are
produced independently, so a global counter cannot be allocated correctly and ends up
with four different digests all claiming the same number.

**Parked, do not produce:** AI Engineering Ch.2 Part 3, High Performance MySQL Ch.3
Part 2, DDIA Ch.3, and every chapter not named above. They stay published in the library
for reference, they are simply not continued.

## Current batch: tick each when you've studied it

- [ ] AI Engineering — Ch.7 (Part 1): Finetuning: When to Do It, and Why Memory Is the Wall (`docs/digests/ai-eng-ch07-part1-when-to-finetune-memory.html`)
- [ ] AI Engineering — Ch.7 (Part 2, final): Finetuning: PEFT, LoRA, Model Merging and Practical Tactics (`docs/digests/ai-eng-ch07-part2-peft-lora-merging.html`)
- [ ] AI Engineering — Ch.8 (Part 1): Dataset Engineering: Curating Data (Quality, Coverage, Quantity) and Getting It (`docs/digests/ai-eng-ch08-part1-data-curation.html`)
- [ ] AI Engineering — Ch.8 (Part 2, final): Dataset Engineering: Synthetic Data, Distillation and Processing (`docs/digests/ai-eng-ch08-part2-synthesis-processing.html`)
- [ ] AI Engineering — Ch.9 (Part 1): Inference Optimization: Bottlenecks, Metrics and AI Hardware (`docs/digests/ai-eng-ch09-part1-inference-metrics-hardware.html`)
- [ ] AI Engineering — Ch.9 (Part 2, final): Inference Optimization: Model-Level and Service-Level Techniques (`docs/digests/ai-eng-ch09-part2-optimization-techniques.html`)
- [ ] AI Engineering — Ch.10 (Part 1): AI Engineering Architecture: From a Single Model Call to a Full System (`docs/digests/ai-eng-ch10-part1-architecture-observability.html`)
- [ ] AI Engineering — Ch.10 (Part 2, final): User Feedback: Extracting, Designing and Handling the Limits of Conversational Feedback (`docs/digests/ai-eng-ch10-part2-user-feedback.html`)
- [ ] AWS CloudWatch — Concept 3: CloudWatch Logs: Log Groups, Streams, Retention, Metric Filters and Subscription Filters (`docs/digests/aws-cloudwatch-03-logs.html`)
- [ ] AWS CloudWatch — Concept 4: CloudWatch Logs Insights: The Query Language for Searching and Analysing Logs (`docs/digests/aws-cloudwatch-04-logs-insights.html`)
- [ ] AWS CloudWatch — Concept 5: CloudWatch Dashboards and Cross-Account, Cross-Region Observability (`docs/digests/aws-cloudwatch-05-dashboards-cross-account.html`)
- [ ] AWS CloudWatch — Concept 6: The CloudWatch Agent and Embedded Metric Format (`docs/digests/aws-cloudwatch-06-agent-emf.html`)
- [ ] AWS CloudWatch — Concept 7: Amazon EventBridge: Rules, Event Patterns, Schedules and Their Link to CloudWatch Events (`docs/digests/aws-cloudwatch-07-eventbridge.html`)
- [ ] AWS CloudWatch — Concept 8: CloudWatch Synthetics Canaries and RUM: Testing Like a User and Watching Real Users (`docs/digests/aws-cloudwatch-08-synthetics-rum.html`)
- [ ] AWS CloudWatch — Concept 9: Container Insights, Lambda Insights, ServiceLens and X-Ray Tracing (`docs/digests/aws-cloudwatch-09-insights-xray.html`)
- [ ] AWS EC2 — Concept 3: EC2 Storage: EBS Volumes, Snapshots and Instance Store (`docs/digests/aws-ec2-03-ebs-snapshots-instance-store.html`)
- [ ] AWS EC2 — Concept 4: Elastic Load Balancing in Depth: ALB vs. NLB vs. GWLB, Target Groups and Health Checks (`docs/digests/aws-ec2-04-elastic-load-balancing.html`)
- [ ] AWS EC2 — Concept 5: Auto Scaling in Depth: Launch Templates, Scaling Policies, Lifecycle Hooks and Warm Pools (`docs/digests/aws-ec2-05-auto-scaling.html`)
- [ ] AWS EC2 — Concept 6: Systems Manager (SSM): Session Manager, Run Command, Patch Manager and Parameter Store (`docs/digests/aws-ec2-06-systems-manager.html`)
- [ ] AWS EC2 — Concept 7: Instance Metadata (IMDSv2), User Data, Instance Profiles and IAM Roles (`docs/digests/aws-ec2-07-metadata-userdata-instance-profiles.html`)
- [ ] AWS EC2 — Concept 8: Placement Groups, the Nitro System, and Dedicated Hosts vs. Dedicated Instances (`docs/digests/aws-ec2-08-placement-nitro-dedicated.html`)
- [ ] AWS EC2 — Concept 9: Security Groups and Key Pairs from the Instance's Point of View (`docs/digests/aws-ec2-09-security-groups-key-pairs.html`)
- [ ] AWS EC2 — Concept 10: Instance Monitoring, Status Checks and Auto Recovery (`docs/digests/aws-ec2-10-monitoring-status-checks-recovery.html`)
- [ ] AWS S3 — Concept 3: S3 Versioning, Delete Markers & MFA Delete: Keeping Every Version and Protecting the Delete Button (`docs/digests/aws-s3-03-versioning-delete-markers-mfa-delete.html`)
- [ ] AWS S3 — Concept 4: S3 Encryption: SSE-S3, SSE-KMS, DSSE-KMS, SSE-C and Bucket Keys (`docs/digests/aws-s3-04-encryption-sse-kms-bucket-keys.html`)
- [ ] AWS S3 — Concept 5: S3 Access Control: Bucket Policies, IAM, ACLs, Block Public Access and Access Points (`docs/digests/aws-s3-05-access-control-policies-bpa-access-points.html`)
- [ ] AWS S3 — Concept 6: S3 Replication: CRR, SRR, Replication Time Control and Batch Replication (`docs/digests/aws-s3-06-replication-crr-srr-rtc-batch.html`)
- [ ] AWS S3 — Concept 7: S3 Presigned URLs, CORS and Static Website Hosting: Sharing S3 Content With Browsers and People (`docs/digests/aws-s3-07-presigned-urls-cors-static-website.html`)
- [ ] AWS S3 — Concept 8: S3 Event Notifications and the EventBridge Integration: Making Uploads Trigger Things (`docs/digests/aws-s3-08-event-notifications-eventbridge.html`)
- [ ] AWS S3 — Concept 9: S3 Multipart Upload, Transfer Acceleration and Byte-Range Fetches: Moving Big Objects Faster (`docs/digests/aws-s3-09-multipart-transfer-acceleration-byte-range.html`)
- [ ] AWS S3 — Concept 10: S3 Object Lock, Retention & Legal Hold, Inventory and Storage Lens: Locking Data Down and Seeing What You Have (`docs/digests/aws-s3-10-object-lock-inventory-storage-lens.html`)
- [ ] AWS VPC — Concept 5: DNS in a VPC: Route 53 Resolver, Private Hosted Zones, DHCP Option Sets (`docs/digests/aws-vpc-05-dns-resolver-phz-dhcp.html`)
- [ ] AWS VPC — Concept 6: VPC Flow Logs and Traffic Mirroring (`docs/digests/aws-vpc-06-flow-logs-traffic-mirroring.html`)
- [ ] AWS VPC — Concept 7: IPv6 in a VPC and the Egress-Only Internet Gateway (`docs/digests/aws-vpc-07-ipv6-egress-only-igw.html`)
- [ ] AWS VPC — Concept 8: VPC Peering in Depth: Limits, CIDR Overlap, Cross-Account and Cross-Region (`docs/digests/aws-vpc-08-vpc-peering-in-depth.html`)
- [ ] AWS VPC — Concept 9: Site-to-Site VPN, Direct Connect, and Hybrid Routing (`docs/digests/aws-vpc-09-site-to-site-vpn-direct-connect.html`)
- [ ] AWS VPC — Concept 10: VPC Sharing with RAM, Managed Prefix Lists, and Route Evaluation Order (`docs/digests/aws-vpc-10-vpc-sharing-prefix-lists-route-order.html`)
- [ ] DDIA — Ch.5 (Part 1): Replication: Leaders, Followers, and Replication Lag (`docs/digests/ddia-ch05-part1-leaders-followers-replication-lag.html`)
- [ ] DDIA — Ch.5 (Part 2, final): Replication: Multi-Leader, Leaderless, and Concurrent Writes (`docs/digests/ddia-ch05-part2-multi-leader-leaderless.html`)
- [ ] DDIA — Ch.6: Partitioning: Splitting Data Across Machines (`docs/digests/ddia-ch06-partitioning.html`)
- [ ] DDIA — Ch.7 (Part 1): Transactions: What They Promise (ACID) and What They Don't (`docs/digests/ddia-ch07-part1-acid-meaning-multi-object.html`)
- [ ] DDIA — Ch.7 (Part 2): Weak Isolation: Read Committed, Snapshots, Lost Updates, and Write Skew (`docs/digests/ddia-ch07-part2-weak-isolation-write-skew.html`)
- [ ] DDIA — Ch.7 (Part 3, final): Serializability: Serial Execution, Two-Phase Locking, and SSI (`docs/digests/ddia-ch07-part3-serializability.html`)
- [ ] DDIA — Ch.10 (Part 3): Joins, Grouping, and What Batch Jobs Produce (`docs/digests/ddia-ch10-part3-joins-grouping-batch-output.html`)
- [ ] DDIA — Ch.10 (Part 4, final): Beyond MapReduce: Dataflow Engines, Graphs, and Declarative Batch (`docs/digests/ddia-ch10-part4-dataflow-engines-graphs-declarative.html`)
- [ ] DDIA — Ch.11 (Part 1): Event Streams, Message Brokers, and Partitioned Logs (`docs/digests/ddia-ch11-part1-event-streams-brokers-logs.html`)
- [ ] DDIA — Ch.11 (Part 2): Databases and Streams: Change Data Capture and Event Sourcing (`docs/digests/ddia-ch11-part2-databases-and-streams.html`)
- [ ] DDIA — Ch.11 (Part 3, final): Processing Streams: Time, Windows, Joins, and Fault Tolerance (`docs/digests/ddia-ch11-part3-processing-streams.html`)
- [ ] High Performance MySQL — Ch.8 (Part 1): Why Queries Are Slow: Asking for Less, Restructuring, and the Client/Server Protocol (`docs/digests/hpmysql-ch08-part1-slow-queries-restructuring-protocol.html`)
- [ ] High Performance MySQL — Ch.8 (Part 2): Inside the Optimizer: Cost, Join Order, Sorting and the Execution Engine (`docs/digests/hpmysql-ch08-part2-optimizer-joins-sorting-execution.html`)
- [ ] High Performance MySQL — Ch.8 (Part 3, final): Where the Optimizer Struggles, and How to Rewrite COUNT, Pagination and UNION Queries (`docs/digests/hpmysql-ch08-part3-optimizer-limits-specific-queries.html`)

## Track A: Designing Data-Intensive Applications

Focus: Ch.4, Ch.5, Ch.6, Ch.7, Ch.10, Ch.11, in that order. Nothing else from this book.

| Ch | Title | Pages | Digested | Carousel | Notes |
|---:|-------|-------|----------|----------|-------|
| 4 | Encoding and Evolution | 133–166 | 2026-08-09 (Pt.1, pp.133–150); 2026-08-18 (Pt.2, final, pp.150–162) | 2026-08-09 (Pt.1); 2026-08-18 (Pt.2, final) | Done. Part 2 = Modes of Dataflow (databases, REST/RPC, message brokers, distributed actor frameworks) through the chapter's own Summary. Chapter 4 is fully covered; PDF pages 162–166 are references/Part II divider, not chapter content. |
| 5 | Replication | | 2026-10-25 (Pt.1, printed pp.151–167 / PDF 173–189); 2026-10-25 (Pt.2, final, printed pp.168–193 / PDF 190–215) | | Done. Part 1 = leader-based replication (sync vs. async, adding followers, node failure and failover, replication log implementations) and replication lag (read-your-writes, monotonic reads, consistent prefix reads). Part 2 = multi-leader replication and write conflicts, leaderless/Dynamo-style replication (quorums, sloppy quorums, hinted handoff), and detecting concurrent writes. |
| 6 | Partitioning | | 2026-10-25 (printed pp.199–218 / PDF 221–240) | | Done. Single digest: partitioning by key range vs. hash, skew and hot spots, secondary indexes (local vs. global), rebalancing strategies and request routing. |
| 7 | Transactions | | 2026-10-25 (Pt.1, printed pp.221–232 / PDF 243–254); 2026-10-25 (Pt.2, printed pp.233–251 / PDF 255–273); 2026-10-25 (Pt.3, final, printed pp.251–267 / PDF 273–289) | | Done. Part 1 = what transactions promise (ACID) and single- vs. multi-object operations. Part 2 = weak isolation: read committed, snapshot isolation, lost updates and write skew. Part 3 = serializability via actual serial execution, two-phase locking and serializable snapshot isolation. |
| 10 | Batch Processing | 411–460 | 2026-09-07 (Pt.1, pp.411–419); 2026-10-11 (Pt.2, printed pp.397–403 / PDF 419–425); 2026-10-25 (Pt.3, printed pp.403–418 / PDF 425–440); 2026-10-25 (Pt.4, final, printed pp.419–431 / PDF 441–452) | 2026-09-07 (Pt.1); 2026-10-11 (Pt.2) | Done. Part 1 = chapter framing (services vs. batch vs. stream systems) plus "Batch Processing with Unix Tools" in full (log analysis pipeline, sort vs. in-memory aggregation, the Unix Philosophy: uniform interface, separation of logic/wiring, transparency/experimentation). Stops at the boundary before "MapReduce and Distributed Filesystems". Part 2 = HDFS and shared-nothing storage, the four MapReduce steps (mapper/reducer), distributed execution (partitioning, shuffle) and workflows; stops before "Reduce-Side Joins and Grouping" (mid printed p.403). Part 3 = reduce-side joins and grouping, map-side joins, and the output of batch workflows. Part 4 = dataflow engines, graph processing and declarative high-level APIs. **Next DDIA unit:** none; the focused scope (Ch.4, 5, 6, 7, 10, 11) is now fully published. |
| 11 | Stream Processing | 461–510 | 2026-10-25 (Pt.1, printed pp.439–451 / PDF 461–473); 2026-10-25 (Pt.2, printed pp.451–464 / PDF 473–486); 2026-10-25 (Pt.3, final, printed pp.464–481 / PDF 486–503) | | Done. Part 1 = event streams, message brokers vs. log-based brokers and partitioned logs. Part 2 = databases and streams: change data capture, event sourcing, state vs. streams. Part 3 = processing streams: event time vs. processing time, windows, stream joins and fault tolerance. |

*Already published (do not redo):* Ch.1; Ch.2 Parts 1 and 2.
*Parked:* Ch.3, 8, 9, 12.

## Track A: AI Engineering (Chip Huyen)

Focus: Ch.5 onwards, in order. Ch.2 is parked mid-chapter on purpose (Part 3 will not
be produced); Ch.3 and Ch.4 are skipped.

| Ch | Title | Pages | Digested | Carousel | Notes |
|---:|-------|-------|----------|----------|-------|
| 5 | Prompt Engineering | 235-276 | 2026-08-09 (Pt.1, pp.235–258); 2026-08-18 (Pt.2, final, pp.259–276) | 2026-08-09 (Pt.1); 2026-08-18 (Pt.2, final) | Done. Part 2 = Defensive Prompt Engineering (prompt extraction, jailbreaking/injection, information extraction, prompt-level and system-level defenses) through the chapter's own Summary. |
| 6 | RAG and Agents | 277-330 | 2026-09-07 (Pt.1, pp.277–298); 2026-10-11 (Pt.2, final, printed pp.275–306 / PDF 299–330) | 2026-09-07 (Pt.1); 2026-10-11 (Pt.2, final) | Done. Part 1 = the RAG half of the chapter in full (what RAG is, RAG architecture, term-based vs. embedding-based retrieval, hybrid search/RRF, retrieval optimization, evaluating retrieval, RAG beyond text). Stops at the boundary before "Agents" begins. Part 2 = Agents (tools, planning, reflection, tool selection, failure modes and evaluation), Memory, and the chapter's own Summary. **Next AI Engineering unit:** none; the focused scope (Ch.5 onwards, through Ch.10) is now fully published. |
| 7 | Finetuning | 331-386 | 2026-10-25 (Pt.1, printed pp.307–332 / PDF 331–356); 2026-10-25 (Pt.2, final, printed pp.332–362 / PDF 356–386) | | Done. Part 1 = when to finetune (vs. RAG) and why memory is the bottleneck. Part 2 = PEFT, LoRA and quantized variants, model merging, and practical finetuning tactics. |
| 8 | Dataset Engineering | 387-428 | 2026-10-25 (Pt.1, printed pp.363–380 / PDF 387–404); 2026-10-25 (Pt.2, final, printed pp.380–404 / PDF 404–428) | | Done. Part 1 = data curation (quality, coverage, quantity) and acquiring data. Part 2 = data augmentation and synthesis, distillation, and data processing (inspect, dedupe, clean, format). |
| 9 | Inference Optimization | 429-472 | 2026-10-25 (Pt.1, printed pp.405–425 / PDF 429–449); 2026-10-25 (Pt.2, final, printed pp.426–448 / PDF 450–472) | | Done. Part 1 = compute- vs. memory-bound bottlenecks, latency/throughput/utilization metrics and AI hardware. Part 2 = model-level and service-level optimization techniques. |
| 10 | AI Engineering Architecture and User Feedback | 473-518 | 2026-10-25 (Pt.1, printed pp.449–474 / PDF 473–498); 2026-10-25 (Pt.2, final, printed pp.474–493 / PDF 498–517) | | Done. Part 1 = building up an AI application architecture (context, guardrails, routers, gateways, caches, agents, monitoring, orchestration). Part 2 = user feedback: extracting, designing and the limits of conversational feedback. |

*Already published (do not redo):* Ch.1; Ch.2 Parts 1 and 2.
*Parked:* Ch.2 Part 3, Ch.3, Ch.4.

## Track A: High Performance MySQL (4th ed.)

Focus: Ch.6, Ch.7, Ch.8. Nothing else from this book.

| Ch | Title | Pages | Digested | Carousel | Notes |
|---:|-------|-------|----------|----------|-------|
| 6 | Schema Design and Management | 147-176 | 2026-08-09 (Pt.1, pp.147–168); 2026-08-18 (Pt.2, final, pp.168–176) | 2026-08-09 (Pt.1); 2026-08-18 (Pt.2, final) | Done. Part 2 = the closing ENUM/NULL gotchas plus Schema Management (source control, Flyway/Liquibase/Skeema/Vitess, native DDL vs. pt-online-schema-change vs. gh-ost, CI/CD pipeline design) through the chapter's own Summary. |
| 7 | Indexing for High Performance | 177-212 | 2026-09-07 (Pt.1, pp.177–184); 2026-10-11 (Pt.2, printed pp.162–178 / PDF 184–200); 2026-10-25 (Pt.3, final, printed pp.178–190 / PDF 200–212) | 2026-09-07 (Pt.1); 2026-10-11 (Pt.2) | Done. Part 1 = chapter opener, "If I Use an ORM, Do I Need to Care?" sidebar, and all of "Indexing Basics" (B-tree indexes incl. adaptive hash index and leftmost-prefix behavior, full-text indexes, benefits of indexes). Stops before "Indexing Strategies for High Performance" begins. Part 2 = Indexing Strategies for High Performance from its start through "When Primary Key Order Is Worse" (prefix indexes, multicolumn/column order, clustered indexes); stops before "Covering Indexes". Part 3 = covering indexes, index scans for sorts, redundant/duplicate/unused indexes, index and table maintenance, and the chapter's own Summary. **Next High Performance MySQL unit:** none; the focused scope (Ch.6, 7, 8) is now fully published. |
| 8 | Query Performance Optimization | 213-248 | 2026-10-25 (Pt.1, printed pp.191–204 / PDF 213–226); 2026-10-25 (Pt.2, printed pp.205–218 / PDF 227–240); 2026-10-25 (Pt.3, final, printed pp.219–226 / PDF 241–248) | | Done. Part 1 = why queries are slow, restructuring queries and the client/server protocol. Part 2 = the optimizer: cost, join order, sorting and the execution engine. Part 3 = optimizer limitations and rewrites for COUNT, pagination and UNION queries. |

*Already published (do not redo):* Ch.1; Ch.2; Ch.3 Part 1.
*Parked:* Ch.3 Part 2, Ch.4, Ch.5, Ch.9–13.

## Track B: AWS — four areas, in rotation

Cover the next unstarted concept from the next area in the rotation each batch. Finish an
in-progress concept before starting the next. Source is the official AWS docs
(https://docs.aws.amazon.com/); fetch the relevant service pages for each concept.

### S3 (every concept)
| # | Concept | Digested | Carousel | Notes |
|--:|---------|----------|----------|-------|
| 1 | Buckets, objects, keys, the flat namespace, durability & consistency model | 2026-10-11 | 2026-10-11 | Done. General purpose buckets (naming, global namespace), objects, keys and the flat namespace, durability design target and 3+ AZs, strong read-after-write consistency, conditional writes. CLI micro-projects checked against the CLI reference but not run against a live account. |
| 2 | Storage classes & lifecycle policies (incl. Intelligent-Tiering, Glacier tiers) | 2026-10-25 | | Done. Storage classes as a price-vs-access trade (access speed, AZ count, retrieval fees, minimum duration and size), Intelligent-Tiering, Glacier tiers, and lifecycle rules for automatic transitions and expiry; no prices quoted. |
| 3 | Versioning, delete markers, MFA delete | 2026-10-25 | | Done. Versioning (multiple versions per key), delete markers, and MFA delete. |
| 4 | Encryption: SSE-S3, SSE-KMS, DSSE-KMS, SSE-C, bucket keys | 2026-10-25 | | Done. The four server-side encryption options (SSE-S3, SSE-KMS, DSSE-KMS, SSE-C) and S3 Bucket Keys for cutting KMS cost. |
| 5 | Access control: bucket policies, IAM, ACLs, Block Public Access, access points | 2026-10-25 | | Done. How S3 evaluates requests: IAM and bucket/access point policies, ACLs, Block Public Access, explicit deny beats allow. |
| 6 | Replication: CRR/SRR, Replication Time Control, batch replication | 2026-10-25 | | Done. CRR vs. SRR, Replication Time Control, and Batch Replication for objects live replication skips. |
| 7 | Presigned URLs, CORS, static website hosting | 2026-10-25 | | Done. Presigned URLs, CORS, and static website hosting. |
| 8 | Event notifications and EventBridge integration | 2026-10-25 | | Done. Event Notifications to SNS/SQS/Lambda vs. the EventBridge integration. |
| 9 | Multipart upload, Transfer Acceleration, byte-range fetches | 2026-10-25 | | Done. Multipart upload, Transfer Acceleration, and byte-range fetches. |
| 10 | Object Lock, retention & legal hold, Inventory, Storage Lens | 2026-10-25 | | Done. Object Lock (governance/compliance retention, legal hold), S3 Inventory, and Storage Lens. |

### EC2 (every concept)
| # | Concept | Digested | Carousel | Notes |
|--:|---------|----------|----------|-------|
| 1 | Instances & AMIs: types/families, lifecycle, custom AMIs, stop vs. terminate | 2026-07-30 (Pt.1); 2026-08-09 (Pt.2, final) | 2026-07-30 (Pt.1); 2026-08-09 (Pt.2, final) | Done. Part 1 = Instances & AMIs (2026-07-30). Part 2 = Auto Scaling Groups & Elastic Load Balancing at an intro/pairing level (2026-08-09); deeper ASG/ELB detail is reserved for concepts 4 and 5 below. |
| 2 | Purchasing options: on-demand, reserved, savings plans, spot | 2026-10-25 | | Done. The seven ways to pay for EC2 (On-Demand, Savings Plans, Reserved Instances, Spot, and capacity/dedicated-hardware options) framed as trade-offs of commitment, flexibility and certainty; no dollar prices quoted. |
| 3 | EBS volumes, snapshots, instance store | 2026-10-25 | | Done. EBS volumes, incremental snapshots, and instance store. |
| 4 | Elastic Load Balancing in depth: ALB vs. NLB vs. GWLB, target groups, health checks | 2026-10-25 | | Done. ALB vs. NLB vs. GWLB, target groups and health checks. |
| 5 | Auto Scaling in depth: launch templates, scaling policies, lifecycle hooks, warm pools | 2026-10-25 | | Done. Launch templates, scaling policies, lifecycle hooks and warm pools. |
| 6 | Systems Manager (SSM): Session Manager, Run Command, Patch Manager, Parameter Store | 2026-10-25 | | Done. Session Manager, Run Command, Patch Manager and Parameter Store. |
| 7 | Instance metadata (IMDSv2), user data, instance profiles & IAM roles | 2026-10-25 | | Done. IMDSv2, user data, and instance profiles / IAM roles. |
| 8 | Placement groups, Nitro, dedicated hosts vs. dedicated instances | 2026-10-25 | | Done. Placement groups, the Nitro System, and Dedicated Hosts vs. Dedicated Instances. |
| 9 | Security groups & key pairs from the instance's point of view | 2026-10-25 | | Done. Security groups and key pairs from the instance's point of view. |
| 10 | Instance monitoring, status checks, auto recovery | 2026-10-25 | | Done. Status checks, monitoring metrics and auto recovery. |

### VPC (every concept)
| # | Concept | Digested | Carousel | Notes |
|--:|---------|----------|----------|-------|
| 1 | Core networking: VPC, subnets, route tables, IGW, NAT gateway | 2026-07-20 | 2026-07-20 | Done. |
| 2 | Transit Gateway & multi-VPC connectivity | 2026-07-27 | 2026-07-27 | Done. |
| 3 | Security groups and network ACLs in depth | 2026-08-18 | 2026-08-18 | Done. Stateful security groups (instance/ENI level, allow-only) vs. stateless network ACLs (subnet level, allow+deny, ordered rules), ephemeral return-traffic ports, and default vs. custom rule sets, grounded in the live AWS VPC User Guide. |
| 4 | VPC endpoints: gateway vs. interface, and PrivateLink | 2026-10-25 | | Done. Gateway endpoints (route-table entry, S3 and DynamoDB only) vs. interface endpoints (network interfaces in your subnets via PrivateLink), and endpoint services. |
| 5 | DNS in a VPC: Route 53 Resolver, private hosted zones, DHCP option sets | 2026-10-25 | | Done. The built-in VPC DNS resolver, DHCP option sets, private hosted zones, and Resolver endpoints/rules for hybrid DNS. |
| 6 | Flow Logs and traffic mirroring | 2026-10-25 | | Done. Flow Logs (metadata to CloudWatch Logs, S3 or Firehose) and Traffic Mirroring (packet copies). |
| 7 | IPv6 in a VPC, egress-only internet gateway | 2026-10-25 | | Done. Dual-stack IPv6 and the egress-only internet gateway. |
| 8 | VPC peering in depth: limits, CIDR overlap, cross-account/region | 2026-10-25 | | Done. Peering limits (no overlapping CIDRs, no transitive routing), cross-account/region peering, and route setup. |
| 9 | Site-to-Site VPN, Direct Connect, hybrid routing | 2026-10-25 | | Done. Site-to-Site VPN, Direct Connect, and hybrid routing. |
| 10 | VPC sharing with RAM, prefix lists, route evaluation order | 2026-10-25 | | Done. Subnet sharing with RAM, managed prefix lists, and route evaluation order. |

### CloudWatch (every concept)
| # | Concept | Digested | Carousel | Notes |
|--:|---------|----------|----------|-------|
| 1 | Metrics: namespaces, dimensions, resolution, custom metrics | 2026-09-07 | 2026-09-07 | Done. Namespaces, dimensions (up to identifying a metric uniquely), standard vs. high-resolution, and publishing custom metrics via PutMetricData, grounded in the live CloudWatch User Guide and API reference. |
| 2 | Alarms: static, anomaly detection, composite, and alarm actions | 2026-10-25 | | Done. How an alarm evaluates (OK / ALARM / INSUFFICIENT_DATA), static threshold vs. anomaly detection vs. composite alarms, and actions on state changes. **Next AWS unit:** none; every listed concept across S3, EC2, VPC and CloudWatch is now published. |
| 3 | Logs: log groups/streams, retention, metric filters, subscription filters | 2026-10-25 | | Done. Log groups and streams, retention, metric filters and subscription filters. |
| 4 | Logs Insights query language | 2026-10-25 | | Done. The Logs Insights query language. |
| 5 | Dashboards and cross-account / cross-region observability | 2026-10-25 | | Done. Dashboards and cross-account, cross-region observability. |
| 6 | The CloudWatch agent and Embedded Metric Format | 2026-10-25 | | Done. The CloudWatch agent and Embedded Metric Format. |
| 7 | EventBridge: rules, patterns, schedules, and its relation to CloudWatch Events | 2026-10-25 | | Done. EventBridge rules, event patterns and schedules, and the link to CloudWatch Events. |
| 8 | Synthetics canaries and RUM | 2026-10-25 | | Done. Synthetics canaries and RUM. |
| 9 | Container/Lambda Insights, ServiceLens, X-Ray tracing | 2026-10-25 | | Done. Container Insights, Lambda Insights, ServiceLens and X-Ray tracing. |
