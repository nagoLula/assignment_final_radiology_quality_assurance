# Prototype – Radiology Quality Assurance Dashboard

## Overview

- This prototype presents a simplified implementation of the Radiology Quality Assurance Dashboard.
- It was developed as an exploratory exercise to assess and reinforce my foundational technical skills while validating core concepts outlined in the system architecture.

### The application enables users to

- Upload a synthetic radiology workflow CSV file  
- Store uploaded files locally, simulating Azure Blob Storage  
- Access a basic dashboard interface that displays uploaded files  

Rather than implementing the full Azure-based pipeline, this prototype focuses on demonstrating the essential upload and dashboard workflow described in the architecture plan using a lightweight local setup.

## Features

- `/` – Home page providing a file upload interface  
- `/upload` – Handles CSV uploads and saves files to a local `uploads/` directory  
- `/dashboard` – Displays a list of uploaded files as a placeholder for future quality metrics  

## Requirements

Install the required dependencies using:

```bash
pip install -r requirements.txt



