# Bulk Certificate Generator Python

Python script that can generate bulk certificates for an event. The script takes a XLSX/CSV file as input, which contains the names and other details of the participants. The script then uses a template image and a font file to create personalized certificates for each participant.

## How to use?

### Prerequisites

The latest version of Python should be installed in the system.

### Setup

Install the required packages by running these commands in the terminal.

```bash
pip install pillow
pip install pandas
pip install openpyxl
```

### Post Setup

- Put a designed blank copy of certificate in the `templates` directory.

- Put your desired font in the `fonts` directory.

- Put the Attendee list as XLSX file in the `input` directory <br/>
  _Note: Make sure it has a `Names` field containing the names of the Certificate receivers._

_Note: Make sure to rename the file names to match the demo file names or change the relative file paths in the script to match your file names._

### Run the script

Once the script is executed, the certificates will be generated and saved in the `certficates` directory.
