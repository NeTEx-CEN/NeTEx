# NeTEx (Network Timetable EXchange) XML schema
(C) 2009-2021  NeTEx, CEN, Crown Copyright

## Schemas for: Core, Part 1 (Network),  Part 2 (Timetables), Part3 (Fares) and Part5 (NewModes).
                            
See the NeTEx UML Physical and Conceptual models for an UML view of the packages. (This is available in electronic format).

The individual  XML files  are arranged hierarchically in folders, in a similar arrangement to that of the UML model and documentation. Thus there is a main folder for each part, and subfolders for each NeTEx functional area.

----
## Getting Started
There are two main root schemas:
 - **netex_publication** : Embeds NeTEx XML model elements in a bulk output file format for use in asynchronous publication. The intended content scope can be indicated by a filter object.
 - **netex_siri.xsd** : Embeds NeTEx XML model elements in the SIRI protocol for dynamic exchange of elements between servers. Both Request/response or publish / subscribe is supported

In addition:

 - **nx.xsd** : Embeds NeTeX XML model elements within a simple thematic organisation to facilitate browsing and inspection of NeTEx.   The NX schema is not intended for actual use.

There are **XML examples** of the use of both protocols, see */examples* subdirectory.

### Support for XML editors
There is an _Altova XMLSpy_ project file in the root directory  that provides an organised view  of the schema and examples:
 - NeTEx.spp

There is also an _Oxygen_ project file:
  - NeTEx.xpr
----
### Note on the schema
The schema is broken down systematically into small modular files; generally for each functional package in the design model  (See UML Model) there are two xml schema files
 - netex_xxxx_suppport.xsd - containing data type  and ref structure definitions.
 - netex_xxxx_version.xsd - containing the element definitions.
----
# Changelog

See [CHANGELOG](CHANGELOG.md)

