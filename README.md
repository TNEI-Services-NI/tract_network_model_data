GB Power System Model Data
========================

Welcome to the repository for ETYS network data collation, processing and sorting ready for feeding into a power system model for analysis.

Getting started 
=============================


- [Installation](#Installation)
- [Running ...repo_name...](#Running...repo_name...)
- [Directory](#Directory)
- [Email](#Email)

----------------------------------

# Installation
`1. Run "make.bat"`\
`2. Once all packages have been installed ("press any key, to continue" will appear), close command prompt.`\
`3. Open base directory as new project in PyCharm.`\
`4. Once PyCharm"s init. processes complete (updating skeletons, indexing etc.), set virtual environment path. Either:`\
`4.1 Select suggested directory in amber banner above code editor;`\
`Or `\
`4.1 File -> Settings -> Search "venv" -> Click configure icon -> Click "Add"`\
`4.2 Select "Existing Directory" -> Select venv engine "...repor_base_dir...\venv\Scripts\python.exe"`\
`4.3 Click "Apply" -> Click "Ok"`

----------------------------------

# Running...repo_name...

----------------------------------

### File Tree

```
tract_network_model_data/
├── docs/                            # Documentation (empty or not expanded)
├── package/
│   ├── data_processing/             # Core data processing logic
│   │   ├── __init__.py
│   │   ├── intra_hvdc.py
│   │   ├── load_data.py
│   │   ├── network_data.py
│   │   └── plant_data.py
│   ├── input_data/                 # Input datasets
│   │   ├── etys_appendix_b_2024.xlsx
│   │   ├── fes_2024_active_power_demand_data.csv
│   │   ├── ic_register_mapping.csv
│   │   ├── interconnector_register_04feb2025.csv
│   │   ├── internal_hvdc_etysappb2024.csv
│   │   ├── substation_coordinates.csv
│   │   ├── tec_register_04feb2025.csv
│   │   └── tec_register_mapping.csv
│   └── output_data/               # Output data following scripts
│       ├── __init__.py
│       ├── config.py
│       └── main.py
├── tests/                           # Unit tests and validation
│   ├── __init__.py
│   ├── context.py
│   ├── isolated_nodes_network_data.py
│   ├── test_advanced.py
│   └── test_basic.py
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
```

# Directory
TBC

# Email
Nathanael Sims - Principal Consultant\
<nathanael.sims@tneigroup.com>