# Architecture & Implementation Plan

- Radiology Quality Assurance Dashboard

## Overview

- This architecture describes a cloud‑integrated solution that automates the ingestion, processing, and analysis of radiology workflow data to support quality assurance (QA) and turnaround time (TAT) monitoring.
- The system uses Azure services for storage, compute, database management, and optional analytics.
- A Flask web application serves as the user interface for uploading daily modality workflow files and viewing TAT metrics.
- The design fulfills the course requirement to integrate multiple cloud components, including storage, compute, database, and analytics, into a cohesive workflow.

## Service Mapping

| Layer               | Azure Service                                | Role in Solution                                             | Related Assignment/Module     |
|---------------------|-----------------------------------------------|--------------------------------------------------------------|--------------------------------|
| Frontend / Access   | Flask App (local or Azure App Service)        | Upload CSV files, display dashboard                          | Flask module                  |
| Storage             | Azure Blob Storage                            | Stores raw CSV files uploaded daily                          | Cloud Storage module          |
| Compute (ETL)       | Azure Functions (Blob Trigger or Timer)       | Cleans data, calculates TAT, loads processed data into SQL   | Serverless Functions module   |
| Database            | Azure SQL Database                            | Stores cleaned encounter records and computed TAT metrics    | SQL Database module           |
| Analytics (Optional)| Azure ML Notebook or Azure Data Studio        | Runs trend analysis, outlier detection, QA analytics         | Analytics / ML module         |

---

## Data Sources

This project uses a **synthetic radiology dataset** downloaded from Kaggle and stored in data and renamed to `radiology_event_log.csv`

This project focuses on architectural design and implementation planning rather than full cloud deployment, consistent with the scope of a student mini‑capstone.

The dataset includes fields such as:

- Case ID
- Event Name
- Timestamp
- Duration
- Resource
- Outcome
- Age & gender
- Exam Type
- Medical History
- Urgency Level

No real patient data is used

---

## Data Flow

1. Radiology workflow data is exported daily as a CSV file from the imaging system.
2. A user uploads the CSV file through the Flask web application.
3. The uploaded file is stored in Azure Blob Storage to keep the raw data.
4. An Azure Function is triggered when a new file is added.
5. The function processes the data by cleaning timestamps and calculating turnaround times.
6. The processed data is saved into an Azure SQL Database.
7. An analytics notebook queries the database to calculate summary metrics and trends.
8. The Flask dashboard displays turnaround time metrics and flagged cases to users.

## Design Context

The overall structure of this workflow was inspired by similar quality assurance processes observed in a real-world radiology operations environment from personal experience.

The design has been adapted for educational purposes using synthetic data and simplified cloud components to align with the scope of this course.
