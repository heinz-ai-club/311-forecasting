"""
Column names of the raw Pittsburgh 311 CSV (data/raw/311_data.csv).

Use these constants instead of typing column names as strings, so the code uses one
set of names everywhere. Descriptions come from the WPRDC data dictionary:
https://data.wprdc.org/dataset/pittsburgh-311-data
Checked November 7, 2026. If the City changes the file, update this list.
"""

ID = "_id"                                  # Row number added by the data portal
CASE_NUMBER = "case_number"                 # Case number for the 311 request
STATUS = "status"                           # New, Open, Closed or In Progress; may have a (Duplicate) flag
CASE_OWNER = "case_owner"                   # Department or organization assigned to the case
SUBJECT = "subject"                         # Category of request (the issue type)
SUBJECT_CODE = "subject_code"               # Internal code for the subject
LEGACY_SUBJECT = "legacy_subject"           # Matches request_type_name in the old 311 dataset
CREATED_ET = "created_date_et"              # When the case was created (Eastern Time)
CREATED_UTC = "created_date_utc"            # When the case was created (UTC)
LAST_MODIFIED_ET = "last_modified_date_et"  # Last update (Eastern Time)
LAST_MODIFIED_UTC = "last_modified_date_utc"  # Last update (UTC)
CLOSED_ET = "closed_date_et"                # When the case was closed (Eastern Time); empty if open
CLOSED_UTC = "closed_date_utc"              # When the case was closed (UTC); empty if open
ORIGIN = "origin"                           # How the request was submitted (Phone, Email, Web, etc.)
STREET = "street"                           # Street name
STREET_ID = "street_id"                     # Street code as a string; may be 0 if no street was entered
CITY = "city"                               # Mailing city of the request location
NEIGHBORHOOD = "neighborhood"               # Neighborhood containing the request location
CENSUS_TRACT = "census_tract"               # Census tract containing the request location
COUNCIL_DISTRICT = "council_district"       # Council district; values look like "D9"
WARD = "ward"                               # Pittsburgh ward containing the request location
POLICE_ZONE = "police_zone"                 # Police zone containing the request location
LATITUDE = "latitude"                       # Latitude (rounded for privacy)
LONGITUDE = "longitude"                     # Longitude (rounded for privacy)
GEO_ACCURACY = "geo_accuracy"               # EXACT (5 decimals, within 1 m) or APPROXIMATE (2 decimals, within 1 km)
UNIQUE_ID = "unique_id"                     # case_number plus the year created

ALL_COLUMNS = [
    ID, CASE_NUMBER, STATUS, CASE_OWNER, SUBJECT, SUBJECT_CODE, LEGACY_SUBJECT,
    CREATED_ET, CREATED_UTC, LAST_MODIFIED_ET, LAST_MODIFIED_UTC, CLOSED_ET, CLOSED_UTC,
    ORIGIN, STREET, STREET_ID, CITY, NEIGHBORHOOD, CENSUS_TRACT, COUNCIL_DISTRICT, WARD,
    POLICE_ZONE, LATITUDE, LONGITUDE, GEO_ACCURACY, UNIQUE_ID,
]
