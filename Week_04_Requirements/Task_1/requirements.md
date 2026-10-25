# Software Requirements Specification

> Generated from the supplied corpus. Review priorities and ambiguities with stakeholders before implementation.

## Priority scale

- **P1 — Critical:** essential to core operation, security, or compliance.
- **P2 — High:** important operational capability with substantial user value.
- **P3 — Medium:** useful standard capability; should be planned after higher priorities.
- **P4 — Low:** optional, lower-impact, or explicitly nice-to-have.

## Requirements

### REQ-001: Material volume report

- **Priority:** P1
- **Type:** reporting
- **Sources:** `conversations/conv_pines014_material_volume.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system shall provide a consolidated report for a user-selected library, counting items whose recorded location is that library. It shall report current holdings and holdings as of a selected historical date, an overall item total, acquisitions, items on shelf or checked in, items checked out or in circulation, and holds; checked-out items remain included in the total. Libraries shall be able to configure or select category breakdowns, including examples such as adult fiction, board books, genre, and format, with holds by category where applicable. The report shall support acquisition summaries for the last 30, 60, and 90 days and recurring monthly and quarterly management reporting.

**Acceptance criteria**

- A user can select a library and receive counts limited to items attributed to that library under the report's location logic.
- The output shows a total and separate acquisition, on-shelf/checked-in, and checked-out/in-circulation counts; checked-out items are included in the total.
- The output shows overall holds and, when enabled, holds by configured category.
- A user can configure or select category dimensions, including genre and format where configured.
- The report can produce current and selected historical-date results and acquisition summaries for 30-, 60-, and 90-day periods.
- The report can be used for monthly and quarterly reporting.

### REQ-002: Branch capacity overview

- **Priority:** P1
- **Type:** functional
- **Sources:** `conversations/conv_pines015_capacity_interface.eml`, `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system shall provide a high-level, system-wide overview of branch capacity metrics, aggregate data across branches, and allow drill-down to an individual branch. The overview shall support filtering and sorting by region, library type, and current load when those fields are available. The design shall address display density for 286 locations; grouping by system or region and filtering are approaches to evaluate, not settled design decisions. The definition and calculation of capacity are unresolved: candidate measures include item count versus shelf space, physical item count versus a configured limit, and circulation volume versus processing capacity, and must be agreed before implementation. Capacity trends and CSV export are required; green/yellow/red status coding is an optional design choice.

**Acceptance criteria**

- The overview displays all branches and key capacity metrics simultaneously, with data aggregated across branches.
- A user can drill down from the overview to an individual branch.
- Users can filter and sort by region, library type, and current load when those dimensions are available.
- The design is evaluated for 286 locations; grouping and filtering alternatives are assessed for usability without presuming a final approach.
- The capacity metric and calculation are documented and approved before implementation.
- The interface shows longitudinal capacity or load trends and can export capacity data as CSV.
- Green/yellow/red capacity coding is evaluated as optional and is not treated as mandatory without confirmation.

### REQ-003: Shelf-space and collection-use comparison

- **Priority:** P1
- **Type:** reporting
- **Sources:** `conversations/conv_pines016_shelf_space.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system shall report, for each material genre and format, the percentage of total circulations, percentage of the collection, and percentage of total shelf space occupied. Reports shall run for an individual library or an entire system, support side-by-side library comparisons and comparison with the system average, and allow date-range analysis, including quarterly comparisons. Because shelf space is not directly tracked, the system shall estimate it from item dimensions when usable dimensions are available or support item count as a proxy when dimensions are unavailable or that approach is selected.

**Acceptance criteria**

- For each reported genre-and-format group, results include circulation share, collection share, and shelf-space share calculated against their applicable totals.
- The report runs for one library and a library system, with grouping by library, genre, and format where applicable.
- A library result can be compared side by side with other libraries and the corresponding system average.
- Users can select a date range and compare periods such as Q1 and Q2.
- Shelf-space estimation uses available item dimensions or an identified item-count proxy when appropriate.
- The report supports quarterly review.

### REQ-004: Batch item transfer workflow

- **Priority:** P1
- **Type:** functional
- **Sources:** `conversations/conv_pines018_item_transfer.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system shall provide an authorized-staff utility for transferring batches of items between branches and temporary locations, including mobile libraries, outreach programs, warehouses, sales, events, and programs. Users shall be able to query candidate items using item attributes and circulation history, save and reuse queries, and manually select items from results. Before execution, the utility shall show a preview including item count and origin and destination locations and require confirmation. Execution shall update selected item locations and generate a printable pull list and printable transit barcode labels. Transfers shall be transaction-safe and processed in appropriately sized batches to avoid excessive database locking, accounting for a collection of approximately 9.6 million items.

**Acceptance criteria**

- Authorized staff can query candidates by item attributes and circulation history, including items in a collection that have not circulated for a specified period.
- A saved query can be reused; users can manually select individual results for transfer.
- The preview shows item count, origin, and destination and requires explicit confirmation.
- Execution updates every selected item location and produces a printable pull list and barcode transit labels.
- A failed transfer does not leave a partially updated, inconsistent batch; large transfers are processed in batches that avoid excessive database locking.
- Branch and temporary destinations include mobile, outreach, warehouse, sale, and event/program locations.

### REQ-005: Transfer authorization, audit, and recovery

- **Priority:** P1
- **Type:** security
- **Sources:** `conversations/conv_pines018_item_transfer.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`, `survey_results_2009.txt`

Only authorized roles shall transfer items between locations; identified eligible roles are managers, administrators, and transfer coordinators. The system shall retain transfer history sufficient to identify affected items and operations and report an item's transfer count over a period, and provide undo for an erroneous completed transfer. It shall support scheduled automatic reversion to the original location based on configured elapsed time or other criteria, including status changes such as sold or returned, event completion, and destination checkout policy. A configured mobile-library rule may keep checked-out items at the destination while returning unused items. The source does not specify a complete rule language or conflict-resolution policy; these details remain to be defined.

**Acceptance criteria**

- Users without transfer authorization cannot execute a transfer; eligible roles can be granted authorization.
- Transfer history identifies operations and affected items and supports transfer counts over a selected period.
- An authorized user can undo a completed transfer and restore the original location.
- Scheduled rules can revert items after a configured duration or configured status/event condition, including sold, returned, and event completion.
- A configured destination-checkout rule can retain checked-out mobile-library items and revert unused items.
- Configured reversion rules and unresolved conflict behavior are inspectable rather than silently assumed.

### REQ-006: Transfer delay notifications

- **Priority:** P3
- **Type:** functional
- **Sources:** `conversations/conv_pines018_item_transfer.eml`

The system shall notify designated users when an item transfer is delayed or encounters a recorded issue.

**Acceptance criteria**

- A recorded transfer delay or issue generates a notification to configured recipients.

### REQ-007: Missing and damaged item reporting

- **Priority:** P2
- **Type:** reporting
- **Sources:** `conversations/conv_pines019_020_missing_intransit.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system shall provide inventory-audit reports of items identified as missing, lost, or damaged, organized or filterable by branch and supporting selectable date ranges. Results shall include condition notes when available and item and location information useful for investigating branch patterns, repeated losses, and collection-management actions. This report is separate from the in-transit report.

**Acceptance criteria**

- The report returns items in supported missing, lost, or damaged statuses and can be run or filtered by branch.
- Users can select date ranges, including the last 30 days and last quarter.
- Available condition notes are included; absent notes are not fabricated.
- Results provide item and location detail suitable for counts, branch audits, pattern investigation, and collection-management review.
- The report can be run independently of in-transit reporting.

### REQ-008: Aging in-transit report

- **Priority:** P1
- **Type:** reporting
- **Sources:** `conversations/conv_pines019_020_missing_intransit.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system shall provide one report combining transit-to and transit-from items that exceed a configurable transit-age threshold. Seven days is a probable default, not a fixed requirement. An item qualifies when its arrival date is null and its departure date is more than the configured threshold in the past. Results shall be available by branch and library system and sortable by due date.

**Acceptance criteria**

- Transit-to and transit-from items appear in one combined result set.
- Users can configure the age threshold; seven days can be used as the proposed default.
- An item qualifies when arrival date is null and departure date is more than the configured threshold in the past.
- Results can be viewed by branch and system and sorted by due date.
- The report remains separate from missing/damaged item reporting.

### REQ-009: Configurable purge candidate identification

- **Priority:** P1
- **Type:** functional
- **Sources:** `conversations/conv_pines021_item_purging.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system shall provide read-only reports and utilities to identify item records eligible for purge or weeding using configurable criteria. Criteria shall include item status, including missing, discard/weed, and damaged; duration in a status; time since last circulation; and combined conditions using AND. Thresholds shall support days, months, or years. Identifying candidates shall not alter or delete records; actual deletion requires separate explicit confirmation and an audit trail of who purged what and when. Automatic scheduling, such as annual execution, is an optional enhancement rather than a mandatory behavior.

**Acceptance criteria**

- Users can configure status, status-duration, and time-since-last-circulation criteria with thresholds in days, months, or years.
- Candidate searches support AND combinations, including missing-status duration plus circulation inactivity.
- Candidate reports do not change item records.
- A separate explicit confirmation is required before purge or deletion.
- Each completed purge records the actor, affected records, and time.
- Automatic scheduling is not required for candidate identification.

### REQ-010: Batch item status conversion

- **Priority:** P2
- **Type:** functional
- **Sources:** `conversations/conv_pines021_item_purging.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system shall provide a report or workflow to identify items for status conversion and convert selected items in a batch, including conversions such as 100 items from missing to discard/weed.

**Acceptance criteria**

- Users can identify candidate items by current status and select a target status.
- Users can convert multiple selected items in one operation, including a 100-item batch.
- Every selected item receives the target status and unselected items remain unchanged.

### REQ-011: Last-copy identification by scope

- **Priority:** P1
- **Type:** reporting
- **Sources:** `conversations/conv_pines021_item_purging.eml`, `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `interview_cataloging_2009-05-08.txt`

The system shall provide a last-copy report that flags item or bibliographic records that are the only copy within a selected scope: an individual library or branch, or the entire library system or consortium. The report shall support cataloger review before deletion or external WorldCat updates and, where deletion history permits, identify deleted items that were last copies.

**Acceptance criteria**

- For each qualifying record, the report identifies whether it is the sole copy in the selected library/branch or system-wide scope.
- Users can select library/branch or system/consortium scope.
- Current last copies can be reviewed before deletion or WorldCat updates.
- Where deletion history is retained, users can report deleted items that were last copies.

### REQ-012: Catalog cleanup utilities

- **Priority:** P2
- **Type:** functional
- **Sources:** `conversations/conv_pines021_item_purging.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system shall provide efficient utilities to delete volume entries together with associated copy entries and to identify and remove bibliographic or other catalog records with no attached items, including orphaned records. Destructive cleanup actions shall be separately confirmed and covered by applicable deletion auditing.

**Acceptance criteria**

- A cleanup operation can remove a volume entry together with its associated copy entries.
- A cleanup operation can identify records with no attached items and remove selected records.
- Cleanup is available as a utility rather than requiring exclusively manual record-by-record processing.
- Destructive cleanup requires confirmation and is covered by deletion audit logging.

### REQ-013: Deletion audit capture

- **Priority:** P1
- **Type:** security
- **Sources:** `conversations/conv_pines022_deletions.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`, `survey_results_2009.txt`

The system shall persist an automatically captured audit record for each completed deletion, including at least item and patron records and supporting bibliographic and other record types where available. Each record shall identify record type, deleted-record identifier, timestamp, deleting user, and the user's location or branch, and shall remain queryable after the source record is removed. Pre-deletion status and deletion reason shall be captured when available; reason capture is requested for troubleshooting and director review.

**Acceptance criteria**

- A successful deletion automatically creates a persistent, queryable audit-table record that remains after the source record is deleted.
- The record identifies deleted-record type and identifier, deletion date/time, deleting user, and user location/branch.
- Item and patron records are supported; bibliographic and other record types are supported where available.
- Pre-deletion status and deletion reason are recorded when available.
- Audit records are not silently lost when source records are removed.

### REQ-014: Deletion audit queries and reports

- **Priority:** P1
- **Type:** reporting
- **Sources:** `conversations/conv_pines022_deletions.eml`, `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

Authorized users shall be able to query and report deletion activity by date range, user, record type, location or branch, and system. Reports shall show totals by month, quarter, or year; breakdowns by type, location, and system; and users with the highest deletion counts. Audit data shall support tracing a deletion and demonstrating retention-schedule compliance. Denied deletion attempts should also be recordable with operation, user, time, location, and record details when available.

**Acceptance criteria**

- Authorized users can query deletion events by date range, user, record type, location, and system.
- Reports show totals by month, quarter, and year and breakdowns by type, location, and system.
- A report identifies users with the highest deletion counts and their counts.
- An authorized user can trace a deleted record to its deletion time, user, and location.
- Reports support retention reviews, including patron-record deletion counts and dates.
- Where enabled, denied deletion attempts record the attempted operation and available user, time, location, and record details.

### REQ-015: Patron-characteristic query and reporting

- **Priority:** P2
- **Type:** reporting
- **Sources:** `conversations/conv_pines023_patron_characteristics.eml`, `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`

Queries and reports shall filter and group patron and related activity data by age range, ZIP/postal code, county of residence, home branch, patron type, and preferred language. Reports shall provide patron counts and circulation or checkout counts by selected dimensions. Age brackets shall be configurable per report and calculated at query time from birth date. Multiple filters shall support both AND and OR logic, including activity criteria such as no checkout during a specified period. Records with missing optional demographic fields shall remain in results with null values. Queries shall use the corresponding patron-table fields.

**Acceptance criteria**

- Users can filter and group by age range, ZIP/postal code, county, home branch, patron type, and preferred language.
- Reports can show patron and circulation/checkout counts by selected dimensions.
- Users can define age brackets per report; age is calculated from birth date when the query runs.
- Queries can combine demographic and activity filters using AND and OR, including a specified no-checkout period.
- Qualifying records with null or blank optional demographic values remain represented with those values.
- Demographic queries use the corresponding patron-table fields.

### REQ-016: Inactive-patron reporting

- **Priority:** P1
- **Type:** reporting
- **Sources:** `conversations/conv_pines024_inactive_patrons.eml`, `early_draft_srs_galecia.txt`

The system shall identify patrons with no physical circulation and no qualifying electronic activity during a configurable number of preceding days. The threshold shall accept day values, with 365 days as the commonly used default and 30, 90, and 180 days among anticipated values. Qualifying electronic activity includes OPAC/account logins, online holds, online renewals, and logged access to integrated digital resources where available. The report shall combine activity sources, including separate tables, and support System, Home Library, County, and additional configured aggregation levels. Results shall support system-level identification of branches with the most inactive patrons and assignment of cleanup work by home library. The report shall include current mailing addresses, distinguish inactive patrons with outstanding fines, allow configurable exclusions such as do-not-disturb, VIP, staff, and communication opt-out records, and export to CSV.

**Acceptance criteria**

- The report identifies patrons with no circulation or qualifying electronic activity within the configured number of days.
- The threshold is configurable in days and supports 30, 90, 180, and 365; 365 days can be selected as the default.
- Activity calculation includes circulation, OPAC login, online holds, online renewals, and logged integrated digital-resource access where available.
- The report uses the latest activity across applicable sources and tables.
- Results can be grouped by System, Home Library, County, and configured additional levels; system results expose branch counts.
- Results include current mailing addresses and distinguish patrons with outstanding fines.
- Users can configure exclusions including do-not-disturb, VIP, staff, and communication opt-out categories.
- The report can be exported as CSV for an external outreach system.

### REQ-017: Reporting architecture and operational performance

- **Priority:** P1
- **Type:** non-functional
- **Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `interview_sysadmin_2009-05-10.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The reporting solution shall support approximately 286 locations, 3.5 million patrons, 9.6 million collection items, 17 million annual circulations, and more than 900,000 items purchased or processed annually. Reports and searches shall be usable during library open hours without disrupting circulation, OPAC, or other production functions. Long-running reports shall support background execution and queuing; an appropriate isolation mechanism, such as a read-only replica or other design, shall prevent resource-intensive reports from blocking operational workloads. The system shall work with the existing relational database and complex joins. A separate denormalized reporting warehouse is not mandated: historical reporting may require retained history or a warehouse, but synchronization risks and architecture options must be evaluated rather than presumed resolved.

**Acceptance criteria**

- Architecture documentation and tests address the stated scale: 286 locations, 3.5 million patrons, 9.6 million items, 17 million annual circulations, and more than 900,000 items processed or purchased annually.
- Long-running reports can run in the background while operational functions remain usable.
- Performance tests show report execution does not make circulation or OPAC unusable during open hours.
- The implementation works with a relational database and supports required relational joins.
- The architecture documents historical-data access and evaluates isolation options without mandating an unapproved denormalized warehouse.

### REQ-018: Historical and current-state reporting

- **Priority:** P1
- **Type:** reporting
- **Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`, `email_report_features.eml`, `evergreen_reference_2009.txt`, `meeting_tech_subcommittee_2009-06-30.txt`, `survey_results_2009.txt`

The system shall support reporting against current operational data and historical values or states as of a specified date or date range, including historical item or shelving locations and prior bills. Historical reporting shall retain or access the data needed to reproduce prior states. Detailed transaction-history retention shall be configurable, while monthly and annual transaction aggregates shall be retained indefinitely. Applicable legal and audit retention periods are not fully specified and must be configurable or resolved against governing requirements.

**Acceptance criteria**

- Users can run reports against current data and for a selected historical date or range.
- Historical reports can reproduce prior item locations/shelving values and bill amounts when those data are retained.
- A bills report can retrieve a prior-date snapshot rather than only the current state.
- Detailed transaction-history retention is configurable and monthly and annual aggregates remain available indefinitely.
- Unspecified statutory retention periods are not hard-coded as universal values.

### REQ-019: Report query and data model capabilities

- **Priority:** P1
- **Type:** functional
- **Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `evergreen_reference_2009.txt`, `meeting_tech_subcommittee_2009-06-30.txt`, `survey_results_2009.txt`

The system shall provide a user-friendly query interface for supported reporting record types, including bibliographic, item, patron, circulation, hold, financial, transaction, and staff/actor records. Users shall select query and display fields, choose values from picklists, use Boolean operators, and use regular-expression criteria where supported. Administrators shall control access to tables and fields. The reportable model shall expose relevant fields and relationships, including bibliographic-to-item, item-to-circulation, patron-to-circulation, patron-to-financial, and staff-to-circulation relationships, and provide complete data specifications. Results shall retain records with null or blank values when they meet other criteria.

**Acceptance criteria**

- The query interface supports the stated record types and documented relationships.
- Users can select fields and picklist values, combine criteria with Boolean operators, and use regular expressions where enabled.
- Administrators can restrict access to queryable tables and fields.
- The reportable field set includes relevant bibliographic, item, patron, circulation, hold, financial, and staff data; specifications document field names, types, and relationships.
- Qualifying records with null or blank fields are not silently excluded.

### REQ-020: Report templates and controlled customization

- **Priority:** P1
- **Type:** functional
- **Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `evergreen_reference_2009.txt`, `survey_results_2009.txt`

Administrators shall be able to create, publish, edit, and manage shared report templates that staff can run unchanged or customize within administrator-approved limits. Administrators shall control which filters and display fields users may change so permitted customization preserves intended accuracy and does not expose prohibited data. Authorized users may clone a template as a separate variant without changing the source. Templates shall support reuse, shared folders, and consistent baseline criteria; permitted examples include setting a call-number range or selecting display fields from an approved list.

**Acceptance criteria**

- An administrator can create and publish a template that authorized staff can run as-is.
- Administrators can specify which filters and display fields users may change.
- Users cannot make unapproved changes that expose prohibited data or invalidate intended results.
- An authorized user can clone a template into a distinct variant without changing the original.
- Templates can be reused and organized in shared folders with consistent baseline criteria for a named report.
- Approved customization can include call-number ranges and approved display-field selections.

### REQ-021: Report permissions and role administration

- **Priority:** P1
- **Type:** security
- **Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `email_staff_login.eml`, `interview_sysadmin_2009-05-10.txt`, `meeting_tech_subcommittee_2009-06-30.txt`, `survey_results_2009.txt`

The system shall provide fine-grained, role-based permissions for report creation, editing, cloning, running, scheduling, cancellation, prioritization, sharing, template modification, and ad hoc access to specified data sets. Permissions shall control access to reports, folders, filters, and data sets. Changing a user's role shall update effective permissions without individual permission edits. The model shall support individuals, workgroups, and arbitrary staff groups and accommodate Patron, Staff, Local Admin, Global Admin, front-desk staff, department heads, and library managers with configured capabilities. Global Admin shall have full system access; Local Admin shall have branch-level reporting and configuration; other roles shall be permission-limited.

**Acceptance criteria**

- Administrators can separately control report creation, editing, cloning, running, scheduling, cancellation, prioritization, sharing, and ad hoc data access.
- Permissions can be scoped by role to reports, folders, filters, and data sets.
- Changing a user's role changes that user's effective permissions.
- The model supports individuals, workgroups, and arbitrary staff groups.
- Global Admin has full system access; Local Admin can access branch-level reporting and configuration; limited roles cannot exceed assigned permissions.
- Front-desk users can be configured for basic reports with limited filters and department heads for approved template creation or modification.

### REQ-022: Report types, templates, and scheduling

- **Priority:** P2
- **Type:** functional
- **Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `evergreen_reference_2009.txt`, `survey_results_2009.txt`

The system shall provide canned, on-demand, and open-template reporting interfaces, including prewritten generic reports and permitted combined runs of multiple canned reports. Reports shall support ASAP, hourly, daily, weekly, monthly, and yearly execution, including recurring schedules; users shall be able to edit or cancel schedules. Users shall save and reuse report definitions, use preselected maintenance or collection-development criteria, and find reports through an organized interface with descriptions for report titles.

**Acceptance criteria**

- The system offers distinct canned, on-demand, and open-template reporting capabilities.
- Authorized users can run prewritten reports, edit permitted on-demand criteria, and build reports from open templates.
- Users can select multiple canned reports to run together and view outputs in one document.
- Reports support ASAP, hourly, daily, weekly, monthly, and yearly schedules; recurring schedules can be edited and cancelled.
- Users can save and reuse report definitions and access on-demand reports with preselected maintenance or collection-development criteria.
- The interface organizes reports for discovery and provides descriptions for report titles.

### REQ-023: Report queue, status, priority, and cancellation

- **Priority:** P2
- **Type:** functional
- **Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `evergreen_reference_2009.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`, `survey_results_2009.txt`

Users shall be able to see submitted reports' queue position, number of reports ahead, submission time, and status, including waiting, running, completed, and failed. Authorized users or configured report types shall receive higher execution priority where configured, including a board report ahead of an ad hoc query. Authorized users shall be able to cancel scheduled or running reports, and running processing shall check cancellation signals and stop accordingly.

**Acceptance criteria**

- A report submitter can view queue position, number of reports ahead, submission time, and waiting/running/completed/failed status.
- Authorized users or configured report types can be prioritized ahead of lower-priority work, including a director's board report ahead of an ad hoc query.
- Authorized users can cancel scheduled and running reports.
- Running reports check for cancellation and stop after receiving a cancellation signal.

### REQ-024: Report output, metadata, and data quality

- **Priority:** P1
- **Type:** reporting
- **Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `evergreen_reference_2009.txt`, `meeting_tech_subcommittee_2009-06-30.txt`, `survey_results_2009.txt`

Reports shall be rendered or exported in CSV, HTML, and Excel-compatible formats and support pivot-table output. Outputs shall display report name, selected date range, and selection criteria. Exports shall avoid unintended duplicate rows and preserve one logical result per intended record. Users shall be able to upload file-based filter values such as barcodes or TCNs. Authorized users may customize canned-report display options. Output accuracy shall be validated before reports are treated as dependable.

**Acceptance criteria**

- Reports can be rendered or exported as CSV, HTML, and Excel-compatible output.
- The reporting interface supports pivot-table-style output.
- Each result displays the report name, date range, and query selections or criteria.
- Known-data export tests produce no unintended duplicate rows and one logical result per intended record.
- Users can upload text files of values such as barcodes or TCNs as report filters.
- Authorized users can customize canned-report display options.
- Report accuracy is verified against known test data before output is certified as dependable.

### REQ-025: Report delivery by email

- **Priority:** P3
- **Type:** functional
- **Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `survey_results_2009.txt`

Users shall be able to specify email addresses for report delivery, with an optional address book for recurring recipients. Generated reports shall be deliverable by email rather than requiring download from the web interface.

**Acceptance criteria**

- A user can enter email recipients and receive a generated report by email.
- An address book can be provided for frequently used recipients.
- Recurring report settings retain delivery addresses and allow them to be updated.

### REQ-026: Report use and activity statistics

- **Priority:** P2
- **Type:** reporting
- **Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `survey_results_2009.txt`

The system shall report operational activity including check-ins, checkouts, holds placed, holds filled, renewals, fines collected, and patron registrations. Activity shall be cross-tabulated by terminal, branch, system, hour, patron age range, patron type, and patron location. Reports shall distinguish check-in methods; staff and self-service checkouts and renewals, including online/OPAC renewals; and hold placement methods, including staff desk, public computer, and remote placement. Transaction totals shall be available per patron, library, selected library group, system, and county, with active, frozen, and frozen-until hold subtotals where applicable.

**Acceptance criteria**

- Activity reports include check-ins, checkouts, holds placed, holds filled, renewals, fines collected, and patron registrations.
- Users can group or cross-tabulate activity by terminal, branch, system, hour, age range, patron type, and patron location.
- Check-in methods and checkout/renewal methods are separately reported for specified staff, self-service, book-drop, online, and OPAC cases.
- Hold reports identify placement method and support placed, filled, and stale holds; patron totals include applicable active, frozen, and frozen-until subtotals.
- Transaction totals can be viewed per patron, library, library group, system, and county.

### REQ-027: Circulation and item analytics

- **Priority:** P2
- **Type:** reporting
- **Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `interview_cataloging_2009-05-08.txt`, `survey_results_2009.txt`

The reporting system shall support circulation and item reports covering check-ins, checkouts, renewals, noncataloged circulation, total circulation by type, configurable overdue thresholds, circulation modifiers, material categories, shelving location, Dewey/call number, MARC fields, circulation location by patron county or home library, and patron age. Item reports shall cover additions, edits, deletions, totals, creation-date ranges, fines-stopped reasons, status, sending/destination library, checked-out, overdue, long-overdue, claims-returned, usage counts, collection age and value, last circulation, last edit, and weeding. Check-in timestamps shall be distinct from renewals; last-edit date shall not include or be replaced by last-circulation time. Where requested, MARC fields shall be extractable onto one report row, including fields stored across multiple rows.

**Acceptance criteria**

- Reports support the specified circulation and item measures, status lists, date ranges, usage counts, and grouping dimensions.
- A report can select circulation by modifier, Dewey/call number, MARC field, circulation location and patron geography, and age demographic.
- Check-in date/time is distinct from renewal date/time, and last circulation is separately available.
- Last-edit date reflects edits and is not updated or replaced by circulation activity.
- Weeding reports can include last circulation; overdue reports support a configurable day threshold and, where requested, patron contact information.
- MARC fields can be selected and returned on one logical row, including fields stored across multiple rows.

### REQ-028: Bibliographic, patron, hold, and data-quality reports

- **Priority:** P2
- **Type:** reporting
- **Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `interview_cataloging_2009-05-08.txt`

The system shall support bibliographic reports for record counts, edits, additions by user and library, records without items, and records missing specified MARC fields. Patron reports shall support counts and additions by period and demographic dimensions, survey answers and responses, expiration dates, barred or inactive status, staff-account password-change dates, and patron-note searches. Hold reports shall support purchase alerts, items sent or received, intra-system and intra-facility loans, unfilled and stale holds, annual counts, and holds remaining on a hold shelf too long. Data-quality reports shall identify invalid item types, excessively long call numbers, bibliographic records without items, and patrons with invalid home libraries.

**Acceptance criteria**

- Bibliographic reports support counts, edits, additions by user and library, missing item links, and selectable missing MARC fields.
- Patron reports support demographic counts, additions by month, survey reports, expiration/barred/inactive lists, staff password-change dates, and patron-note searches.
- Hold reports support purchase alerts, sent/received items, loans, unfilled holds, stale holds, annual counts, and aged hold-shelf records.
- Data-quality reports identify invalid item types, long call numbers, bibliographic records without items, and patrons with invalid home libraries.
- A staff password-change report returns each staff account and its last password-change date.

### REQ-029: Financial reporting and account queries

- **Priority:** P1
- **Type:** reporting
- **Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`

The system shall report item value by aggregating item-record purchase prices for the entire collection or a selected portion, with filters such as item status, material format, collection designation, and call number. Financial reports shall cover patron balances by patron, home library, and system; fines and charges by period and charge type; waived fines by period and branch; and payments by period, payment method, collection channel, and collecting branch. Authorized staff shall be able to query balances above a specified amount. Financial records shall associate fines, charges, waivers, payments, and ecommerce transactions with patron and item records as applicable, support joins across those sources, and reflect payments promptly, including front-desk payments.

**Acceptance criteria**

- Item value equals the aggregate purchase-price fields for the selected scope and supports filters such as long-overdue status, children's DVDs, and call number.
- Balances can be reported by patron, home library, and system; authorized users can query balances greater than a specified amount.
- Fines and charges can be reported by period and charge type; waived fines can be reported by period and branch.
- Payments can be reported by period, payment method, collection channel, and collecting branch.
- Financial records can be joined across patron and item data as applicable and associated with relevant records.
- A completed payment, including a front-desk payment, is reflected promptly.

### REQ-030: Financial audit ledger and compliance

- **Priority:** P1
- **Type:** compliance
- **Sources:** `early_draft_srs_galecia.txt`, `email_financial_reports.eml`, `meeting_minutes/meeting_2009-03-15_minutes.txt`

The system shall maintain an auditable payment ledger identifying each payment and the charge or charges to which it was applied, with transaction details needed for reconciliation. Financial reports and archived data shall comply with applicable accounting practices and state, county, and municipal audit requirements. Retention shall be configurable to governing policies, including seven years where required; no single duration is presumed where applicable law is unspecified.

**Acceptance criteria**

- Each payment can be traced through a persistent ledger to the charge or charges to which it was applied.
- Ledger records support reconciliation and identify payment details required by applicable audit rules.
- Retention settings can enforce the applicable period, including seven years when required.
- Financial reports and archives can be reviewed against applicable accounting and state/local audit requirements.

### REQ-031: Patron privacy and demographic statistics

- **Priority:** P1
- **Type:** security
- **Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `survey_results_2009.txt`

Transaction history and demographic reporting shall protect patron privacy while preserving useful aggregate statistics. Data used for demographic statistics shall not retain personally identifiable patron information. Detailed transaction history shall be retained only for its configured retention period, with aggregate statistics retained according to transaction-retention policy.

**Acceptance criteria**

- Demographic outputs do not expose personally identifiable patron information.
- Data used for demographic statistics excludes or removes identifying information while preserving required non-identifying dimensions such as geography and age range.
- Detailed transaction and aggregate data follow their configured retention policies.

### REQ-032: Demographic, behavior, and custom management analytics

- **Priority:** P2
- **Type:** reporting
- **Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-03-15_minutes.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `survey_results_2009.txt`

The system shall support management analysis of patron demographics and interests, collection use, branch comparisons, staff productivity and workflow, and library program planning. Analytics shall include transactions by geographic region, ZIP code where available, and age range, and material-use measures such as average return speed, renewal likelihood, and the percentage of checkouts that are renewals. Custom or local reports shall support collection development, program attendance, and staff time per transaction.

**Acceptance criteria**

- Users can analyze patron demographics and interests, collection use, program planning, and staff productivity/workflow.
- Demographic transaction statistics can be grouped by geographic region, ZIP code where available, and age range.
- Material-use statistics include average return speed, renewal likelihood, and the percentage of checkouts that are renewals.
- Authorized users can create or run local reports for collection development, program attendance, and time per transaction.

### REQ-033: Uncataloged material inventory and use

- **Priority:** P2
- **Type:** functional
- **Sources:** `early_draft_srs_galecia.txt`, `interview_cataloging_2009-05-08.txt`

The system shall support tracking uncataloged materials, including paperback books and children's board books, as inventory before full cataloging. The workflow shall enable rapid distribution with minimal branch labor and provide a way to identify use. Transactions involving tracked uncataloged materials shall be counted in circulation statistics and reports.

**Acceptance criteria**

- Uncataloged materials can be tracked as inventory before individual catalog records are complete.
- The distribution workflow enables quick availability without substantial per-item branch processing.
- The system can report use of tracked uncataloged materials.
- Transactions involving tracked uncataloged materials are included in circulation statistics and reports.

### REQ-034: Executive and predefined report catalog

- **Priority:** P2
- **Type:** reporting
- **Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `evergreen_reference_2009.txt`, `meeting_minutes/meeting_2009-03-15_minutes.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system shall provide predefined reports for boards, executives, and external reporting, including basic statistics required for the Georgia Annual Report and Application for State Aid. It shall support the specified canned and detailed reporting coverage for circulation, item, bibliographic, patron, holds, transit, bills, in-house use, and operational reporting. An Executive Reports Interface shall expose reports selected for PINES executive and board use, and report definitions shall be available across PINES libraries.

**Acceptance criteria**

- Predefined board and executive reports include basic statistics required for the Georgia Annual Report and Application for State Aid.
- The report catalog covers the specified circulation, item, bibliographic, patron, holds, transit, bills, and in-house-use reporting.
- Operational reports include bibliographic records with holds, configurable inactivity thresholds, item-level holds, invalid item types, in-transit items with outstanding holds, long transit duration, last copies, long call numbers, missing items, records without items, and patrons with invalid home libraries.
- An Executive Reports Interface can expose reports selected for PINES executive and board use.
- Report definitions can be made available across PINES libraries.

### REQ-035: Report correctness and selection criteria

- **Priority:** P1
- **Type:** data
- **Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

Report selection criteria shall be clearly defined and shown with results. Records with null or blank values shall remain in results when they meet other selection criteria. Report results shall be tested against known data to establish accuracy. Survey filters shall accept a survey name and resolve it to the corresponding internal identifier. File-based filtering shall accept values such as barcodes and TCNs.

**Acceptance criteria**

- Selection criteria are defined and displayed with report results.
- A record matching other criteria is retained when fields are null or blank.
- Report results match independently calculated results for representative known-data tests.
- Users can select a survey by name and the system resolves it to the correct internal identifier.
- Users can use uploaded barcode or TCN values as report filters.

### REQ-036: Reporting environments, configuration migration, and testing

- **Priority:** P2
- **Type:** constraint
- **Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `interview_sysadmin_2009-05-10.txt`, `meeting_minutes/meeting_2009-03-15_minutes.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system shall provide separate development, training, and production environments. Training shall permit experimentation without modifying production data, and development shall permit report testing without production impact. Templates, permissions, saved queries, and related configuration shall be exportable from development or training and importable into production. The Reports Working Group shall act as a testing gate through which new report development is reviewed before release or adoption.

**Acceptance criteria**

- Distinct development, training, and production environments are available.
- Development and training activities do not modify production data.
- Templates, permissions, saved queries, and related configuration can be exported from a nonproduction environment and imported into production.
- New report development is reviewed through the Reports Working Group testing process before release or adoption.

### REQ-037: Platform and client compatibility

- **Priority:** P1
- **Type:** constraint
- **Sources:** `early_draft_srs_galecia.txt`, `interview_sysadmin_2009-05-10.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The management-process system shall operate on Linux or Solaris server environments, including the identified Red Hat Enterprise Linux 5 primary and Solaris 10 on SPARC secondary environments where applicable. Users shall access the system through a web browser or Windows-compatible client. Browser-based access shall support Internet Explorer 6.0 or later and Firefox 2.0 or later, as specified in the source requirements; these legacy requirements do not establish a broader modern-browser policy.

**Acceptance criteria**

- The system operates in the supported Linux and Solaris environments, including identified RHEL 5 and Solaris 10/SPARC deployments where applicable.
- The system is accessible through a web browser or Windows-compatible client.
- Browser access is tested with Internet Explorer 6.0 or later and Firefox 2.0 or later.

### REQ-038: Accessibility and standards-compliant web output

- **Priority:** P1
- **Type:** accessibility
- **Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `interview_sysadmin_2009-05-10.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system, including reports and help, shall meet Section 508 accessibility requirements and work with screen readers, screen magnification software, and other assistive technologies, including JAWS, NVDA, and ZoomText. HTML output shall be standards-compliant and properly structured for accessibility, including semantic elements, appropriate alternative text, and ARIA labels where applicable.

**Acceptance criteria**

- The reporting interface and online help pass applicable Section 508 accessibility checks.
- Representative workflows are usable with JAWS or NVDA and screen magnification such as ZoomText.
- HTML output validates against applicable standards and uses semantic structure, appropriate alternative text, and applicable ARIA labels.
- Reports and help remain accessible when rendered as HTML.

### REQ-039: Staff authentication and identity

- **Priority:** P1
- **Type:** security
- **Sources:** `early_draft_srs_galecia.txt`, `email_staff_login.eml`, `meeting_minutes/meeting_2009-07-20_minutes.txt`

The system shall support optional streamlined staff login, such as employee-card or RFID-badge login, while retaining individual username-and-password authentication as a fallback. Streamlined login shall not be mandatory for branches without supporting infrastructure. Card-based login shall identify and authenticate the individual rather than provide shared or anonymous access, and the system shall record logged-in staff identity for auditing regardless of authentication method.

**Acceptance criteria**

- Staff can authenticate with individual username and password when card infrastructure is unavailable.
- Card or badge login is optional and not required to use the system.
- Card-based login identifies an individual and does not create anonymous or shared authentication.
- The authenticated staff identity is recorded for auditing for both login methods.

### REQ-040: Enterprise integration and management-process scope

- **Priority:** P1
- **Type:** constraint
- **Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-03-15_minutes.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

Management Processes shall operate as part of the enterprise library automation system, rely on its relational data structures and functionality, and integrate with Acquisitions, Cataloging, and OPAC-generated data. Reporting shall query OPAC-created patron, hold, and circulation data without managing Acquisitions or Cataloging functions or modifying OPAC transaction data. Services shall be centrally consolidated while accepting input from and serving multiple locations. Vendor integration shall use published APIs and/or automated standard-format transfers such as USMARC21 and EDIFACT; EDI ordering data shall be handled when available but shall not be required from every vendor or library. These requirements address management reporting and do not constrain OPAC functionality or replace separate Acquisitions and Cataloging specifications.

**Acceptance criteria**

- Reporting uses enterprise ILS data structures and integrates with Acquisitions and Cataloging data as needed.
- Reports query OPAC-generated patron, hold, and circulation data without modifying those transactions.
- Reporting does not manage acquisitions or cataloging operations and does not constrain OPAC functionality.
- Management services accept input from and serve multiple locations through centralized operation.
- Vendor integration supports published APIs or automated standard-format file transfer, including USMARC21 and EDIFACT where applicable.
- The system handles EDI data when provided and continues functioning when it is absent.

### REQ-041: Data specifications and process documentation

- **Priority:** P2
- **Type:** documentation
- **Sources:** `early_draft_srs_galecia.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The developer shall provide complete data specifications and data dictionaries for authority, bibliographic, order, item, hold/request, and other records maintained or accessed by Management Processes, including field names, data types, and relationships. The developer shall also provide high-level documentation of major processes, including bibliographic import/export, validation against internal and external authority sources, and standard reports.

**Acceptance criteria**

- Documentation covers authority, bibliographic, order, item, hold/request, and other relevant records.
- Data specifications identify field names, data types, and relationships.
- Process documentation describes bibliographic import/export, authority validation, and standard reporting.

### REQ-042: Online help and operational feedback

- **Priority:** P1
- **Type:** functional
- **Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `interview_sysadmin_2009-05-10.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The system shall provide searchable, navigable, hierarchical, cross-linked HTML help describing and illustrating system functions, with context-sensitive access where applicable. It shall provide meaningful high-level error messages when operations fail and low-level query-specific diagnostics for Local and Global System Administrators, including relevant table, field, or error details when available. Help and error output shall be accessible and standards-compliant.

**Acceptance criteria**

- Help is online, searchable, hierarchical, cross-linked, and describes and illustrates system functions.
- Users can access context-relevant help without leaving the system where context-sensitive help is provided.
- Failed operations produce meaningful feedback rather than only a generic failure message.
- Local and Global System Administrators can access query-specific diagnostics, including table, field, or error details when available.
- Help and error views use accessible, standards-compliant HTML.

### REQ-043: Management reporting scope and stakeholder support

- **Priority:** P1
- **Type:** constraint
- **Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`, `meeting_minutes/meeting_2009-07-20_minutes.txt`, `meeting_tech_subcommittee_2009-06-30.txt`

The Reports solution shall support managers, administrators, staff, directors, boards, and consortium administrators in planning, evaluation, oversight, and service design. It shall focus on management processes and reporting rather than day-to-day patron-facing functions handled by the OPAC or circulation client; report information may be displayed indirectly to patrons at library screens without making patrons direct users of the administrative reporting system. Requirements shall relate to management activities, assume the general foundations of a full-fledged ILS, and coordinate with separate Acquisitions and Cataloging specifications.

**Acceptance criteria**

- Reporting supports planning, evaluation, oversight, and service-design activities for the identified staff and management stakeholders.
- Direct patron-facing OPAC and circulation functions remain outside the management-reporting scope.
- Report information may be displayed indirectly to patrons without granting administrative reporting access.
- Requirements do not redefine general ILS foundations or duplicate Acquisitions/Cataloging specifications except where reporting integration is required.
- The Global System Administrator can generate consortium-wide statistical reports and manage consortium-level reporting configuration.

### REQ-044: Requirements development and validation process

- **Priority:** P2
- **Type:** process
- **Sources:** `meeting_minutes/meeting_2009-03-15_minutes.txt`

The requirements effort shall use the King County Library System and Galecia Group SRS as a foundation adapted to PINES needs, gather report needs through at least one staff interview per working-group member, and use collaborative iterative review with end users. The initial requirements phase shall prioritize functional behavior; detailed UI and data-structure requirements shall be developed later through iterative, prototype-oriented work. Documentation shall be readable to nontechnical library stakeholders while sufficiently precise for implementation. Source-recorded milestones include interviews by April 15, 2009, architecture discussion in late June 2009, and findings review on July 20, 2009; these dates are historical planning constraints, not runtime product behavior.

**Acceptance criteria**

- The King County/Galecia SRS is used as a foundation and adapted to PINES needs.
- Each working-group member conducts at least one staff interview to gather report needs.
- End users have multiple opportunities to review prototypes through an iterative process.
- Initial requirements focus on functional behavior; detailed UI and data-structure requirements are scheduled for later iterative specification.
- Requirements are readable to nontechnical stakeholders and sufficiently precise for developers.
- The recorded interview, technical-subcommittee, and findings-review milestones are documented as historical project milestones.

### REQ-045: Operational report usability and accuracy

- **Priority:** P2
- **Type:** non-functional
- **Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `meeting_tech_subcommittee_2009-06-30.txt`, `survey_results_2009.txt`

The reporting interface shall organize reports so users can find them, allow selection of relevant data and fields, clearly define criteria, and provide dependable results. Reports shall support real-time or near-real-time queries for current operational questions, such as items overdue today, while historical reporting remains available through retained history. Performance during busy periods shall remain operationally acceptable; large reports shall not require a synchronous interactive request.

**Acceptance criteria**

- Users can find reports through an organized interface and select relevant data and fields within their permissions.
- Current-data reports can answer time-sensitive questions such as items overdue today.
- Large reports can run asynchronously or in the background rather than requiring a long synchronous request.
- Busy-period performance tests demonstrate that the reporting interface remains usable.
- Report criteria and output accuracy are validated against known data.

### REQ-046: Missing key: Report queue cancellation and cancellation requirements coverage

- **Priority:** P2
- **Type:** functional
- **Sources:** `early_draft_srs_galecia.txt`, `evergreen_reference_2009.txt`, `meeting_tech_subcommittee_2009-06-30.txt`, `survey_results_2009.txt`

The system shall provide the ability to cancel a scheduled report or a running report, and ensure cancellation status is reflected in the queue and that processing stops when cancellation is received.

**Acceptance criteria**

- A user can cancel a scheduled report before it starts.
- A user can cancel a running report; the system indicates cancellation status in the report queue.
- Report processing stops after cancellation is received (no further results generation beyond safe point).
- Canceled reports are not marked as completed successfully.

### REQ-047: Missing key: Pivot table output capability

- **Priority:** P3
- **Type:** reporting
- **Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `meeting_tech_subcommittee_2009-06-30.txt`, `survey_results_2009.txt`

Report output shall support pivot-table-style output (or equivalent) so that business users can analyze results across dimensions in a summarized way.

**Acceptance criteria**

- The reporting system can generate an output format suitable for pivot-table analysis (e.g., spreadsheet output with structure that supports pivoting).
- Pivot output is available in at least one supported export format.
- Pivot output preserves key row/column dimensions derived from report selections.

### REQ-048: Missing key: Transaction-data retention for X days and indefinite monthly/annual aggregates

- **Priority:** P1
- **Type:** non-functional
- **Sources:** `early_draft_srs_galecia.txt`, `survey_results_2009.txt`

Transaction history shall be retained for a configurable number of days, while monthly and annual aggregate information is retained indefinitely to enable historical trend reporting with privacy protection.

**Acceptance criteria**

- The system supports configuration of X days for detailed transaction retention.
- Monthly and annual aggregates remain available indefinitely even when detailed transactions expire.
- Historical aggregate reports use the retained aggregates after detailed transactions expire.

### REQ-049: Missing key: Reporting interface includes query selections displayed alongside results

- **Priority:** P2
- **Type:** reporting
- **Sources:** `early_draft_srs_galecia.txt`, `email_report_features.eml`, `evergreen_reference_2009.txt`

The reporting output shall display the query selections/criteria used to generate results, so users can understand what filters were applied.

**Acceptance criteria**

- Each report run shows the criteria/selections that were applied (including date ranges and filter criteria).
- This selection metadata is visible with the results in the UI and/or in exported output.

### REQ-050: Missing key: Null/blank handling requirement consistency across all reports

- **Priority:** P1
- **Type:** data
- **Sources:** `early_draft_srs_galecia.txt`, `email_staff_login.eml`, `evergreen_reference_2009.txt`, `survey_results_2009.txt`

The system must include null and blank fields in results whenever they meet other selection criteria (i.e., do not silently filter out records due to nulls in optional fields).

**Acceptance criteria**

- For optional demographic fields (e.g., ZIP, county, preferred language), records with null values appear in results when they match other filters.
- For other datasets with optional fields, null/blank values are included unless explicitly filtered out by a user-selected criterion.

## Blacklist: discarded or rejected candidates

### BL-001: Assume denormalized reporting warehouse with ongoing synchronization is acceptable without evaluation

**Reason:** The sources explicitly warn against denormalization and sync issues (“strongly recommend against denormalization… maintaining sync between a reporting warehouse and the live database creates more problems than it solves”). If a future change requests it, it should be treated as a deviation requiring explicit approval and architecture evaluation.

**Sources:** `meeting_tech_subcommittee_2009-06-30.txt`, `evergreen_reference_2009.txt`

### BL-002: Hard-code statutory retention periods (e.g., seven years) as universal without configuration

**Reason:** The corpus states compliance and retention periods must be configurable/resolved against governing requirements; seven years is mentioned as an example/requirement in one area, not universally across all data types.

**Sources:** `email_financial_reports.eml`, `early_draft_srs_galecia.txt`

## Quality-control notes

- Source documents read: 20.
- Requirements emitted: 50.
- Review rounds: 2.

Remaining review issues:

- **duplicate:** Two requirements overlap heavily around query/templates/permissions and reporting correctness. Specifically, “Report query and data model capabilities”, “Report correctness and selection criteria”, and “Report templates and controlled customization” plus “Report templates and controlled customization” and “Report permissions and role administration” together largely restate the same themes already captured in the Galecia/early draft and feature threads (query tool, templates, permissions, null handling, selection criteria display, upload filters). Suggested fix: Consolidate: keep one requirement for “Query tool + null handling + selection-criteria display” and one for “Template management (run/clone/controlled customization)” and one for “Permissions/roles (including shared folders/fine-grained controls)”. Demote the duplicated parts (e.g., null handling, selection criteria display, file-based filters) into acceptance criteria of the consolidated query/correctness requirement.
- **clarity:** Material volume report acceptance criteria mention “holds by category where applicable” but the description does not clearly define the conditions for category breakdown of holds (e.g., whether holds are grouped by the item’s category, bibliographic category, or other mapping). The corpus supports “holds count per category” but does not define mapping rules. Suggested fix: Add an acceptance criterion requiring that category mappings for holds use the same category dimension as item/bibliographic categories used for volume (or explicitly state the mapping source). If mapping is unresolved, mark it as a decision to be documented before implementation.
- **unsupported:** Batch item transfer workflow requires “printable transit barcode labels” and “pull list”, but the corpus mentions transit labels (printable barcodes) and pull list generation; however, the current requirement also states “Transfers shall be transaction-safe and processed in appropriately sized batches … avoid excessive database locking” and “A failed transfer does not leave a partially updated, inconsistent batch”. The corpus supports batching and transaction safety in general, but does not explicitly guarantee rollback/inconsistency handling semantics for partially failed transfers. Suggested fix: Adjust acceptance criteria to match evidence: require transaction safety (use transactions) and batch processing to reduce locking, but remove/soften the stronger guarantee “failed transfer does not leave a partially updated, inconsistent batch” unless the sources explicitly state rollback behavior.
- **traceability:** “Transfer authorization, audit, and recovery” claims “provide undo for an erroneous completed transfer” and “transfer history sufficient to identify affected items and operations” and “scheduled automatic reversion … status changes such as sold or returned”. The corpus supports undo, transfer history tracking, and both time-based and event/status-based auto-revert. However, the requirement also includes “other criteria” and “source does not specify a complete rule language or conflict-resolution policy; these details remain to be defined.” That last clause is reasonable, but the requirement does not propose what is needed to resolve it (e.g., explicit blacklist of unspecified scope language). Suggested fix: Add a missing item/acceptance criterion that the revert-rule model (time-based + event-based + optional destination-checkout keep rule) is explicitly documented as limited to those rule types unless expanded later.
- **clarity:** The “Aging in-transit report” acceptance criteria require “An item qualifies when arrival date is null and departure date is more than the configured threshold in the past.” The corpus states “arrival date is null and the departure date is more than X days ago” but also discusses sorting by due date and merging transit-to/from and keeping report separate from missing/damaged. Due-date wording is not clearly defined in the sources; “due date” appears only as a sorting request for the in-transit report, not a qualification field. Suggested fix: Change “sorted by due date” acceptance criterion to “sorted by the computed oldest/longest-in-transit based on relevant transit date” or “sortable by the transit-age/due-chase field as used by the system”.
- **unsupported:** “Inactive-patron reporting” requires inclusion of integrated digital-resource access “where available” and activity calculation “uses the latest activity across applicable sources”. The corpus supports digital resource access “if integrated” but does not define “latest across sources” behavior. It also does not explicitly say the report uses the latest activity vs. separate “no activity in last X days across all sources” logic. Suggested fix: Replace the “latest across sources” criterion with an evidence-aligned one: “A patron is inactive only if no qualifying activity occurred in any supported activity source within the last X days (or equivalent combined query semantics).”
- **missing:** No explicit requirement for “Report delivery by email” priority is P3, but the SRS also includes ability to cancel scheduled/running reports, pivot table output, cancellation/queue status, and cancel priority behavior. Some exist (report queue, cancellation) but “pivot table output” is only in “Report output, metadata, and data quality” and may not be sufficiently specific/traceable to the sources’ ‘Pivot table output would be great’ request. Suggested fix: Ensure “pivot table output” is explicitly present and traceable as an interface/output capability in the correct requirement, and add a cancellation acceptance criterion tied to the same sources (Evergreen gaps list includes no cancel; Galecia fine-grained includes ability to cancel scheduled/running reports).
- **clarity:** “Reporting architecture and operational performance” says “A separate denormalized reporting warehouse is not mandated: historical reporting may require retained history or a warehouse, but synchronization risks and architecture options must be evaluated rather than presumed resolved.” The technical subcommittee notes include “Modern SQL databases can handle complex analytical queries… strongly recommend against denormalization…”. The current requirement mixes “warehouse” and “denormalization” but does not align terms: a “warehouse” could be denormalized; sources discuss warehouse options for historical data and replica/queue/background as alternatives. This leads to ambiguous interpretation of what is allowed. Suggested fix: Refine wording: distinguish “denormalized warehouse synced with production” (discouraged) from “reporting replica or historical snapshot/warehouse” (optional). Add an acceptance criterion that denormalization/sync issues are explicitly evaluated and that the default approach avoids denormalized sync.
- **other:** Some priorities appear potentially inconsistent with evidence-based severity. For example, “Transfer delay notifications” is P3 though the transfer thread requests alerts. Evergreen SRS does not emphasize transfer delay alerts as high priority; this is not necessarily wrong, but there is no mapping rationale across P1/P2/P3. Suggested fix: Either justify with source evidence (explicitly marked as key/critical by stakeholders) or adjust priority to match similar features (preview/undo/permission appear P1; alerts could be P2 unless evidence supports lower). If unsure, mark as P2 and keep notification scope narrow.
