# NeTEx (Network Timetable EXchange) XML schema
**(C) 2009-2024 NeTEx, CEN, Crown Copyright**

## Schemas for:

- Core
- Part 1 (Network)
- Part 2 (Timetables)
- Part 3 (Fares)
- Part 5 (New Modes)

### Overview

- NeTEx (Network Timetable EXchange) XML schema is a standardized format for exchanging network timetable data.

### Folder structure 📁

The individual XML files are organized hierarchically in folders, following the same structure as the UML model and documentation. The architecture is: 

- **Main Folder for Each Part**: There is a main folder for each part of the schema (e.g., Core, Part 1, Part 2, etc.).
- **Subfolders for Functional Areas**: Within each main folder, there are subfolders for each NeTEx functional area, keeping the schema well-structured.

You can find more information about the directory's structure on the [wiki](https://github.com/ITxPT/NeTEx/wiki/Structure-And-Compatibility#netex-directory-structure)
### UML models

- You can refer to the NeTEx UML Physical and Conceptual models (note that NeTEx Conceptual model is Transmodel) for a detailed UML view of the schema packages.
- These models are available in electronic format.
  
## Getting started 🚀

### Main root schemas

1. **netex_publication**
   - Embeds NeTEx XML model elements in a bulk output file format for use in asynchronous publication.
   - The intended content scope can be indicated by a filter object.
   -  **netex_publication_noConstraint**: same as **netex_publication** but without all the XSD constraint that is convenient to speed up the work in development phases (but at the price of a much weaker validation).

2. **netex_siri.xsd**
   - Embeds NeTEx XML model elements in the SIRI protocol for dynamic exchange of elements between servers.
   - Supports both request/response and publish/subscribe.

### Additional information

- **nx.xsd**
   - Embeds NeTeX XML model elements within a simple thematic organisation to facilitate browsing and inspection of NeTEx.
   - The NX schema is not intended for actual use.

### XML examples

- Explore XML examples of the use of both protocols in the */examples* subdirectory.

Further information on the examples is available on the [wiki](https://github.com/ITxPT/NeTEx/wiki/Using-NeTEx#how-to-use-example-files)
### Support for XML editors

- **Altova XMLSpy Project**: Find an organized view of the schema and examples in the root directory.
   - Project file: NeTEx.spp

- **Oxygen Project File**: 
   - Project file: NeTEx.xpr

----

### Note on the schema

The schema is systematically divided into small modular files. Generally, for each functional package in the design model (See UML Model), there are two XML schema files:

- **netex_xxxx_suppport.xsd**: Contains data type and ref structure definitions.
- **netex_xxxx_version.xsd**: Contains the element definitions.

----
## Branches  🌿

| Branch Name | Description                                             | Link                                            |
| ----------- | ------------------------------------------------------- | ----------------------------------------------- |
| `master`    | Current head of the project                            | [GitHub](https://github.com/NeTEx-CEN/NeTEx)    |
| `next`      | Work for the next release                              | [GitHub](https://github.com/NeTEx-CEN/NeTEx/tree/next) |

# Change Log
## Releases
| Release Number | Release Date  | Description                                    | Link | Release Notes                                                                                   |
| -------------- | ------------- | ---------------------------------------------- | ------------- | ----------------------------------------------------------------------------------------------- |
| 1.2            | March 2022    | Latest productive version before new modes merge | [Code](https://github.com/NeTEx-CEN/NeTEx/releases/tag/v1.2) | [Release Notes](https://github.com/NeTEx-CEN/NeTEx/blob/v1.2/README.md) |
| 1.2.2          | August 2023   | First version of new modes                     | [Code](https://github.com/NeTEx-CEN/NeTEx/releases/tag/v1.2.2)  | [Release Notes](https://github.com/NeTEx-CEN/NeTEx/blob/v1.2.2/README.md)       |
| 1.3.1          | May 2024      | European Passenger Information Accessibility Profile (EPIAP) | [Code](https://github.com/NeTEx-CEN/NeTEx/releases/tag/v1.3.1) | [Release Notes](https://github.com/NeTEx-CEN/NeTEx/blob/v1.3.1/README.md) |
| 2.0          | 2024     | Upcoming release   ⏳                            | N/A  | N/A                                                                                             |
## Full Version History 📚
The comprehensive versions history is available in [change_log.md](https://github.com/ITxPT/NeTEx/blob/NeTEx/change_log.md)
