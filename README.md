# assignment_final_radiology_quality_assurance_dashboard for imaging Turnaround Times

## Overview

This project proposes a cloud-integrated dashboard to monitor radiology imaging turnaround times (TAT) for quality assurance and operational improvement.

## Contents

- `use_case.md` – Detailed description of the radiology TAT use case  
- `architecture_plan.md` – Cloud architecture, service mapping, and implementation plan  
- `architecture_diagram.md` – Visual diagram of the system architecture  
- `reflection.md` – Reflection on design decisions and alternatives  
- `prototype/` – Optional Flask prototype for file upload and dashboard demo  
- `data/` – Synthetic radiology dataset used for testing

## Sample Data

This project uses a **synthetic radiology dataset** from Kaggle.

The file is stored in the repository under:

- `data/radiology_event_log.csv`  
  (original filename: `hospital_radiology_data.csv`)
  This dataset contains simulated radiology encounters with fields such as modality, provider, timestamps, and workflow status.  
**No real patient data is included.**

## Original Data set source

The synthetic dataset was obtained from Kaggle:

- [Synthetic Radiology Data – Predictive Process Mining][radiologyDataSource]

[radiologyDataSource]: https://www.kaggle.com/datasets/clemsadand/synthetic-radiology-data-predictive-process-mining?resource=download

## Prototype Demonstration

Screenshots demonstrating the running prototype and computed QA metrics are provided in the `screenshots/` directory.


## Sources and Acknowledgments

- The project was created using course materials, publicly available documentation, and synthetic datasets from Kaggle. 
- AI-based tools for brainstorming and clarity supported architectural design, documentation structure, and reflection writing.

### AI tools used for assistance

- Microsoft Copilot – Assisted with architectural reasoning, documentation structure, and clarity of explanations.
- Grok (xAI) – Used for general conceptual exploration and comparison of cloud architecture ideas.

