# Radiology Quality Assurance Dashboard Use_Case

## Problem Statement

Radiology departments need to monitor imaging turnaround times (TAT) to improve patient care and operational efficiency. Manual tracking is inefficient and error-prone.

## Project proposal

This project proposes a cloud-integrated dashboard that automates the ingestion, processing, and visualization of imaging workflow data to support quality assurance (QA) and continuous improvement initiatives.

## Primary users

Radiologists and modality technologists

Quality improvement team

Hospital administrators

## Data Sources

- Modality Worklist Export (CSV)
- PACS/RIS Metadata (JSON or CSV)
- Manual QA Flags (optional)

## Workflow

1. Upload daily CSV via web interface
2. Store file in Azure Blob Storage
3. Trigger Azure Function for data processing
4. Load cleaned data into Azure SQL Database
5. Run Azure ML Notebook for TAT metrics
6. Display results on Flask dashboard

## Key Metrics

- Average TAT by modality and shift
- Trend analysis over time
- Outlier detection for QA review

## Notes

- Data is refreshed daily
- Supports compliance and quality improvement
