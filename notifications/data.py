"""
Static notification data.
--------------------------
Replace `get_all_notifications()` return value with an API call when the
backend is ready.  Every notification type keeps:
  - columns : list[str]   – table headers
  - data    : list[dict]  – rows (keys match column names)
"""

NOTIFICATION_SCHEMA = {
    "Others Notification": ["HRMS", "EBS"],
    "EHS Notification": ["Code", "Details", "Cost Center", "Type", "For Date", "Create Date"],
    "Global Approval Forwarded by Me": ["SL", "Code", "Priority", "Subject", "Insert By", "Department", "Create Date", "Forwarded To", "Forward Duration"],
    "Global Approval Notification": ["SL", "Code", "Priority", "Subject", "Insert By", "Department", "Approval Deadline", "Waiting Duration"],
    "Heavy Vehicle Notification": ["SL", "Code", "Details", "Name(ID)", "Section", "Department", "Required Date"],
    "Utility and Plumbing Notification": ["Code", "Details", "Product", "Department", "Section", "Create Date"],
    "Global Approval Forward Notification": ["SL", "Code", "Priority", "Subject", "Insert By", "Department", "Forward By", "Approval Deadline", "Waiting Duration"],
    "Workshop Notification": ["Code", "Details", "Product", "Department", "Section", "For Date", "Create Date"],
    "Electrical Notification": ["Code", "Details", "Cost Center", "Location", "Description", "Create Date"],
    "HVAC Notification": ["Code", "Details", "Cost Center", "Location", "Description", "Create Date"],
    "Paint Notification": ["Code", "Details", "Cost Center", "Description", "For Department", "Create Date"],
    "Wastage Notification": ["Code", "Details", "Wastage Type", "Wastage Category", "Insert by", "Department", "Create Date"],
    "Wastage Forward Notification": ["Code", "Details", "Wastage Type", "Wastage Category", "Insert by", "Department", "Create Date"],
    "Comp & PCB Notification": ["Code", "Details", "Cost Center", "Description", "Create Date"],
    "Carpenter Notification": ["Code", "Details", "Cost Center", "Description", "For Department", "Create Date"],
    "Permit to Work Notification": ["Code", "Details", "Work Title", "Work Place", "Insert By", "Create Date"],
    "Carpenter Forward Notification": ["Code", "Details", "Cost Center", "Description", "For Department", "Create Date"],
    "Gift Notification": ["Code", "Details", "Receiver Name", "Reference By", "Create Date"],
    "Software Req. Notification": ["SL", "Code", "Details", "Development Team", "Request Type", "Task Title", "For Department", "Create Date"],
    "Policy Approval Notification": ["SL", "Code", "Details", "Doc. Title", "Insert By", "Department", "Create Date"],
    "ESM Automation Notification": ["Code", "Details", "Cost Center", "Description", "For Department", "Create Date"],
    "Machine Making Req. Notification": ["Code", "Details", "Legal Entity", "Product", "Cost Center", "Create Date", "Approval For"],
    "Service Center Forward Notification": ["SL", "Code", "Details", "Name(ID)", "Department", "Section", "Date"],
    "Service Center Notification": ["SL", "Code", "Details", "Name(ID)", "Department", "Section", "Date"],
}

# ---------------------------------------------------------------------------
# Sample static rows – one entry per notification type
# ---------------------------------------------------------------------------
_STATIC_ROWS = {
    "Others Notification": [
        {"HRMS": "HRMS-2024-001", "EBS": "EBS-4401"},
        {"HRMS": "HRMS-2024-002", "EBS": "EBS-4402"},
        {"HRMS": "HRMS-2024-003", "EBS": "EBS-4403"},
    ],
    "EHS Notification": [
        {"Code": "EHS-001", "Details": "Safety Inspection Required", "Cost Center": "CC-101", "Type": "Routine", "For Date": "2024-02-10", "Create Date": "2024-01-28"},
        {"Code": "EHS-002", "Details": "Fire Drill Scheduled", "Cost Center": "CC-102", "Type": "Drill", "For Date": "2024-02-15", "Create Date": "2024-01-30"},
        {"Code": "EHS-003", "Details": "Chemical Spill Report", "Cost Center": "CC-103", "Type": "Incident", "For Date": "2024-02-01", "Create Date": "2024-02-01"},
    ],
    "Global Approval Forwarded by Me": [
        {"SL": 1, "Code": "GAF-001", "Priority": "High", "Subject": "Budget Revision Q1", "Insert By": "Ahmed R.", "Department": "Finance", "Create Date": "2024-01-20", "Forwarded To": "MD Office", "Forward Duration": "3 Days"},
        {"SL": 2, "Code": "GAF-002", "Priority": "Medium", "Subject": "Vendor Onboarding", "Insert By": "Rina S.", "Department": "Procurement", "Create Date": "2024-01-22", "Forwarded To": "CFO", "Forward Duration": "5 Days"},
    ],
    "Global Approval Notification": [
        {"SL": 1, "Code": "GAN-001", "Priority": "Critical", "Subject": "Annual Audit Sign-off", "Insert By": "Zara M.", "Department": "Accounts", "Approval Deadline": "2024-02-05", "Waiting Duration": "2 Days"},
        {"SL": 2, "Code": "GAN-002", "Priority": "High", "Subject": "HR Policy Update", "Insert By": "Kamrul H.", "Department": "HR", "Approval Deadline": "2024-02-08", "Waiting Duration": "4 Days"},
    ],
    "Heavy Vehicle Notification": [
        {"SL": 1, "Code": "HVN-001", "Details": "Forklift Service Due", "Name(ID)": "Truck-07 (VH007)", "Section": "Logistics", "Department": "Operations", "Required Date": "2024-02-12"},
        {"SL": 2, "Code": "HVN-002", "Details": "Crane Inspection", "Name(ID)": "Crane-02 (VH002)", "Section": "Construction", "Department": "Civil", "Required Date": "2024-02-18"},
    ],
    "Utility and Plumbing Notification": [
        {"Code": "UPN-001", "Details": "Pipe Leak – Floor 3", "Product": "PVC Pipe 2in", "Department": "Facility", "Section": "Block-B", "Create Date": "2024-01-29"},
        {"Code": "UPN-002", "Details": "Water Pump Failure", "Product": "Submersible Pump", "Department": "Admin", "Section": "Basement", "Create Date": "2024-01-31"},
    ],
    "Global Approval Forward Notification": [
        {"SL": 1, "Code": "GAFN-001", "Priority": "High", "Subject": "Capex Request", "Insert By": "Tariq U.", "Department": "Projects", "Forward By": "Sonia B.", "Approval Deadline": "2024-02-06", "Waiting Duration": "1 Day"},
    ],
    "Workshop Notification": [
        {"Code": "WKN-001", "Details": "Machine Calibration", "Product": "CNC Machine", "Department": "Production", "Section": "Unit-1", "For Date": "2024-02-14", "Create Date": "2024-01-28"},
        {"Code": "WKN-002", "Details": "Welding Equipment Check", "Product": "MIG Welder", "Department": "Fabrication", "Section": "Unit-2", "For Date": "2024-02-16", "Create Date": "2024-01-30"},
    ],
    "Electrical Notification": [
        {"Code": "ELN-001", "Details": "Panel Board Fault", "Cost Center": "CC-201", "Location": "Building A", "Description": "Tripping of MCB in panel #3", "Create Date": "2024-01-27"},
        {"Code": "ELN-002", "Details": "UPS Replacement Needed", "Cost Center": "CC-202", "Location": "Server Room", "Description": "Battery backup less than 5 min", "Create Date": "2024-01-29"},
    ],
    "HVAC Notification": [
        {"Code": "HVN-001", "Details": "AC Filter Cleaning", "Cost Center": "CC-301", "Location": "Office Floor 4", "Description": "Quarterly maintenance due", "Create Date": "2024-01-26"},
        {"Code": "HVN-002", "Details": "Chiller Unit Fault", "Cost Center": "CC-302", "Location": "Basement", "Description": "Temperature variance ±5°C", "Create Date": "2024-01-28"},
    ],
    "Paint Notification": [
        {"Code": "PTN-001", "Details": "Wall Repainting", "Cost Center": "CC-401", "Description": "Annual repaint cycle", "For Department": "Admin", "Create Date": "2024-01-25"},
    ],
    "Wastage Notification": [
        {"Code": "WSN-001", "Details": "Fabric Offcuts Disposal", "Wastage Type": "Material", "Wastage Category": "Textile", "Insert by": "Mona L.", "Department": "Production", "Create Date": "2024-01-30"},
        {"Code": "WSN-002", "Details": "Chemical Waste Report", "Wastage Type": "Hazardous", "Wastage Category": "Chemical", "Insert by": "Karim F.", "Department": "QC", "Create Date": "2024-01-31"},
    ],
    "Wastage Forward Notification": [
        {"Code": "WFN-001", "Details": "Forwarded Fabric Disposal", "Wastage Type": "Material", "Wastage Category": "Textile", "Insert by": "Mona L.", "Department": "Production", "Create Date": "2024-01-30"},
    ],
    "Comp & PCB Notification": [
        {"Code": "CPN-001", "Details": "PCB Replacement", "Cost Center": "CC-501", "Description": "Burnt PCB on machine #4", "Create Date": "2024-01-28"},
    ],
    "Carpenter Notification": [
        {"Code": "CRN-001", "Details": "Furniture Repair", "Cost Center": "CC-601", "Description": "Conference table repair", "For Department": "HR", "Create Date": "2024-01-27"},
        {"Code": "CRN-002", "Details": "Partition Installation", "Cost Center": "CC-602", "Description": "New office partition layout", "For Department": "IT", "Create Date": "2024-01-29"},
    ],
    "Permit to Work Notification": [
        {"Code": "PTW-001", "Details": "Roof Access Permit", "Work Title": "Antenna Installation", "Work Place": "Rooftop", "Insert By": "Nasir J.", "Create Date": "2024-01-26"},
        {"Code": "PTW-002", "Details": "Electrical Shutdown", "Work Title": "Panel Maintenance", "Work Place": "Substation", "Insert By": "Reza A.", "Create Date": "2024-01-28"},
    ],
    "Carpenter Forward Notification": [
        {"Code": "CFN-001", "Details": "Forwarded Furniture Repair", "Cost Center": "CC-601", "Description": "Conference table – forwarded to senior carpenter", "For Department": "HR", "Create Date": "2024-01-27"},
    ],
    "Gift Notification": [
        {"Code": "GFN-001", "Details": "Corporate Gift – Eid", "Receiver Name": "Jashim Uddin", "Reference By": "MD Office", "Create Date": "2024-01-20"},
        {"Code": "GFN-002", "Details": "Client Appreciation Gift", "Receiver Name": "Sarah Khan", "Reference By": "Sales Team", "Create Date": "2024-01-22"},
    ],
    "Software Req. Notification": [
        {"SL": 1, "Code": "SRN-001", "Details": "Payroll Module Bug", "Development Team": "Core Dev", "Request Type": "Bug Fix", "Task Title": "Salary slip error", "For Department": "HR", "Create Date": "2024-01-25"},
        {"SL": 2, "Code": "SRN-002", "Details": "New Report Request", "Development Team": "BI Team", "Request Type": "Enhancement", "Task Title": "Monthly MIS Report", "For Department": "Finance", "Create Date": "2024-01-27"},
    ],
    "Policy Approval Notification": [
        {"SL": 1, "Code": "PAN-001", "Details": "Travel Policy Revision", "Doc. Title": "Travel & Expense Policy v3", "Insert By": "HR Head", "Department": "HR", "Create Date": "2024-01-18"},
        {"SL": 2, "Code": "PAN-002", "Details": "IT Security Policy", "Doc. Title": "InfoSec Policy 2024", "Insert By": "CTO", "Department": "IT", "Create Date": "2024-01-20"},
    ],
    "ESM Automation Notification": [
        {"Code": "ESM-001", "Details": "Conveyor Belt Automation", "Cost Center": "CC-701", "Description": "Auto-stop sensor calibration", "For Department": "Production", "Create Date": "2024-01-24"},
    ],
    "Machine Making Req. Notification": [
        {"Code": "MMR-001", "Details": "Fabric Cutting Machine", "Legal Entity": "Apex Garments Ltd.", "Product": "Cutting Machine MK-II", "Cost Center": "CC-801", "Create Date": "2024-01-22", "Approval For": "Capex Committee"},
    ],
    "Service Center Forward Notification": [
        {"SL": 1, "Code": "SCF-001", "Details": "AC Repair Forwarded", "Name(ID)": "Hasan Ali (EMP-441)", "Department": "Facility", "Section": "Block-C", "Date": "2024-01-30"},
    ],
    "Service Center Notification": [
        {"SL": 1, "Code": "SCN-001", "Details": "Generator Service Due", "Name(ID)": "DG Set-01 (GEN-01)", "Department": "Utility", "Section": "Power House", "Date": "2024-02-05"},
        {"SL": 2, "Code": "SCN-002", "Details": "Elevator Maintenance", "Name(ID)": "Lift-03 (ELV-03)", "Department": "Facility", "Section": "Main Building", "Date": "2024-02-08"},
    ],
}


def get_all_notifications() -> dict:
    """
    Returns all notification data.

    TODO: Replace this function body with an API call, e.g.:
        import requests
        response = requests.get('https://api.example.com/notifications/', headers=AUTH_HEADERS)
        return response.json()
    """
    result = {}
    for name, columns in NOTIFICATION_SCHEMA.items():
        result[name] = {
            "columns": columns,
            "data": _STATIC_ROWS.get(name, []),
            "count": len(_STATIC_ROWS.get(name, [])),
        }
    return result


def get_notification_by_type(notification_type: str) -> dict | None:
    """
    Returns a single notification category.

    TODO: Replace with a targeted API call when available.
    """
    all_data = get_all_notifications()
    return all_data.get(notification_type)
