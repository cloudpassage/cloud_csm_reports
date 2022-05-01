# CLOUD_CSM_REPORTS
Cloud CSM Reports script shows the overall pass and fail rates for each CSM policy rule for all csp accounts included in the report's scope.

## Goal:
The main purpose of this script is to generate a report to show the overall pass and fail for each Cloud CSM policy rule. the script exports these results into external CSV file format.

## Requirements:
- CloudPassage Halo API key (with Auditor privileges).
- Python 3.6 or later including packages specified in "requirements.txt".

## Installation:

```
   git clone https://github.com/cloudpassage/CLOUD_CSM_REPORTS.git
   cd CLOUD_CSM_REPORTS
   pip install -r requirements.txt
```

## Configuration:
| Variable | Description | Default Value |
| -------- | ----- | ----- |
| HALO_API_KEY | ID of HALO API Key | ef\*\*ds\*\*fa |
| HALO_API_SECRET_KEY | Secret of HALO API Key | fgfg\*\*\*\*\*heyw\*\*\*\*ter352\*\*\* |
| HALO_API_HOSTNAME | Halo API Host Name | https://api.cloudpassage.com |
| HALO_API_PORT | Halo API Port Number | 443 |
| HALO_API_VERSION | HALO EndPoint Version | v1 |
| OUTPUT_DIRECTORY | Location for generated CSV file | /var/log |

## How the scripts works:
- Checking and validation of the provided configuration parameters and fails in case of missing any required parameter.
- Use HALO API key id/secret to generate access token to be used to access Protected HALO resources.
- Retrieving the whole list if cloud CSM policy rules and their findings details.
- Preparing Cloud CSM Report Statistics (overall_pass, overall_critical_fail, overall_non_critical_fail, total_rows).
- Exporting all retreived Cloud CSM Report data of into CSV file format.

## How to run the tool (stand-alone):
To run the script follow the below steps.

1.  Navigate to the app folder that contains module "runner.py", and run it

```
    cd CLOUD_CSM_REPORTS/app
    python runner.py
```

## How to run the tool (containerized):
Clone the code and build the container:

```
   git clone https://github.com/cloudpassage/CLOUD_CSM_REPORTSgit
   cd CLOUD_CSM_REPORTS
   docker build -t CLOUD_CSM_REPORTS .
```

To run the container interactively:

```
    docker run -it \
    -e HALO_API_KEY=$HALO_API_KEY \
    -e HALO_API_SECRET_KEY=$HALO_API_SECRET_KEY \
    -v $OUTPUT_DIRECTORY:/var/log \
    CLOUD_CSM_REPORTS
```