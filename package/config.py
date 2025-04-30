import os
from datetime import datetime

class Config:
    def __init__(self, YEAR_OF_ANALYSIS=2029):
        # ---------------------------
        # Network Model Data Collation Configuration
        # ---------------------------
        self.YEAR_OF_ANALYSIS = YEAR_OF_ANALYSIS
        self.FES_SCENARIO = "HT"
        self.CONSIDER_DEMAND_TYPES = ["R", "E", "C", "I", "H", "D", "T", "Z"]
        self.SELECTED_TAGS = {'NGET'}
        self.IGNORE_DER = 1
        self.GEN_CAPACITY_FOR_TRANSMISSION = 100

        # ---------------------------
        # Other Settings
        # ---------------------------
        self.PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
        date_str = datetime.now().strftime("%d-%m-%Y")

        self.ETYSB_FILE_PATH = os.path.join(self.PROJECT_DIR, "package/input_data/etys_appendix_b_2024.xlsx")
        self.COORDINATES_FILE_PATH = os.path.join(self.PROJECT_DIR, "package/input_data/substation_coordinates.csv")
        self.TEC_REGISTER_FILE_PATH = os.path.join(self.PROJECT_DIR, "package/input_data/tec_register_04feb2025.csv")
        self.IC_REGISTER_FILE_PATH = os.path.join(self.PROJECT_DIR, "package/input_data/interconnector_register_04feb2025.csv")
        self.TEC_REGISTER_MAPPING_FILE_PATH = os.path.join(self.PROJECT_DIR, "package/input_data/tec_register_mapping.csv")
        self.IC_REGISTER_MAPPING_FILE_PATH = os.path.join(self.PROJECT_DIR, "package/input_data/ic_register_mapping.csv")
        self.DEMAND_FILE_PATH = os.path.join(self.PROJECT_DIR, "package/input_data/fes_2024_active_power_demand_data.csv")

        self.NETWORK_OUTPUT_FILE_PATH = os.path.join(self.PROJECT_DIR, f"package/output_data/NODE_NETWORK_DATA_{date_str}.xlsx")
        self.PLANT_OUTPUT_FILE_PATH = os.path.join(self.PROJECT_DIR, f"package/output_data/PLANT_DATA_{date_str}.xlsx")
        self.DEMAND_OUTPUT_FILE_PATH = os.path.join(self.PROJECT_DIR, f"package/output_data/DEMAND_DATA_{date_str}.xlsx")
        self.HVDC_OUTPUT_FILE_PATH = os.path.join(self.PROJECT_DIR, f"package/output_data/INTRA_HVDC_{date_str}.xlsx")
        self.FULL_GRID_OUTPUT_FILE_PATH = os.path.join(self.PROJECT_DIR, f"package/output_data/FULL_GRID_{date_str}.xlsx")

        self.SHEET_ASSOCIATIONS = {"a": "SHET", "b": "SPT", "c": "NGET", "d": "OFTO", "1": "All"}
