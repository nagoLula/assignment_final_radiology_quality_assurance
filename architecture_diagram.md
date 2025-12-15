# Description of System Components and Data Flow

User[Radiology Staff / QA Team]

    Flask[Flask Web Application
    - Upload CSV
    - View TAT Dashboard]

    Blob[Azure Blob Storage
    - Raw CSV Files]

    Function[Azure Function
    - Data Cleaning
    - TAT Calculation]

    SQL[Azure SQL Database
    - Cleaned Records
    - TAT Metrics]

    ML[Azure ML Notebook
    - Trend Analysis
    - Outlier Detection]

    User --> Flask
    Flask -->|Upload CSV| Blob
    Blob -->|Trigger on Upload| Function
    Function -->|Processed Data| SQL
    SQL -->|Query Metrics| ML
    SQL -->|Summary Metrics| Flask
    
