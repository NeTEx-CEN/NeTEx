NeTEX XML schema
(C) 2009-2018  NeTEX, CEN, Crown Copyright

# Network Timetable EXchange
## Core, Part 1 (Network),  Part 2 (Timetables), Part3 (Fares) Schemas
<<<<<<< HEAD
Version 1.08 - Base version plus minor fixes comprising Norway contributions, plus  the approved 1.1 CRs 1-50
See the NeTEx UML Physical and Conceptual models for an UML view
=======
<<<<<<< HEAD
Version 1.08 - Base version plus minor fixes comprising Norway contributions, plus  the approved 1.1 CRs 1-50
See the NeTEx UML Physical and Conceptual models for an UML view
=======

Version 1.08 - Base version plus minor fixes comprising Norway contributions, plus  the approved 1.1 CRs 1-50

See the NeTEx UML Physical and Conceptual models for an UML view

>>>>>>> f5a5ff0de310736223ba302f0ff70d990ee69dd7
>>>>>>> master
The Part 1, Part 2 & Part3 Schemas include minor  corrections since the issue of the Version 1.0 documents. The Version 1.1 documents cover the changes
----
## Getting Started
There are two main root schemas:
  - **netex_publication** : Embeds NeTEx XML model elements in a bulk output file format for use in asynchronous publication. The intended content scope can be indicated by a filter object.
  - **netex_siri.xsd** : Embeds NeTEx XML model elements in the SIRI protocol  for dynamic exchange of elements between servers. Both Request/response or publish / subscribe is supported

In addition:

  - **nx.xsd** : Embeds NeTeX XML model elements within a simple thematic organisation to facilitate browsing and inspection of NeTEx.   The NX schema is not intended for actual use.

There are **XML examples** of the use of both protocols, see */examples* subdirectory.
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======

>>>>>>> f5a5ff0de310736223ba302f0ff70d990ee69dd7
>>>>>>> master
### Support for XML editors
There is an XMLSpy project file in the root directory  that provides an organised view  of the schema and examples
  - netex-v1.08.spp
 
There is also an Oxygen project file
  - netex-v1.08.xpr

----
# 1.08 Summary of Changes since v1.07

### 2017-12-01  Further revisions & Fixes for v1.1
  * Fix: Add notice assignments to **GroupOfDistanceMatrixElements** [*uml:v96-nk3; doc:v38.04*]
    * netex_distranceMatrixLement_version-v1.1.xsd
  * Fix: Move _alternativeTexts_ up hierarchy to **EntityInVersion** [*uml:v96-nk2; doc:v38.03*]
  * Fix: Move **AlterativeName** to generic framework so Organisation can reference. [uml 96-nk2; doc done v38.03]
    * netex_organisation_version-v1.1.xsd 
    * netex_all_objects_generic_version-v1.0.xsd
  * Fix: Add **ContactDetails** to **Line** as per uml [*uml:v96-nk2; doc:v38.03*]
    * netex_line_version-v1.1.xsd
  * Fix: Update uml diagram for **PropertyOfDay**, **Line** [*uml:v96-nk2; doc:v38.03*]
  * Fix: cd  - **Place** should be typed **Place_VersionStructure**  [*uml:v96-nk2; doc:v38.03*]
    * netex_place_version-v1.1.xsd
  * CR: Cr0019/Cr0013 correct type on  **DayOffSet**  on **CourseOfJourney** and **ReliefOpportunity**, **InterchangeRule**,     [*uml:v96-nk2; doc:v38.03*]
    * netex_vehicleService_version-v1.1.xsd 
    * netex_coupledJourney_version-v1.1.xsd
    * netex_interchange-v1.1.xsd
  * Fix: Add   **DayOffSet**  to JourneyMeeting  [*uml:v96-nk2; doc:v38.03*]
    * netex_interchange-v1.1.xsd
  * CR: Cr0051: Add _infolinks_ to **GroupOfEnNtities** [*uml:v96-nk3; doc:v38.04*]
    * netex_groupin-v1.1.xsd

### 2017-11-08  Further revisions & Fixes for V1.1
  * Fix: Add   **DayOffSet** to **JourneyPartCouple**  [*uml:v96-nk2; doc:v38.03*]
    * netex_coupledJourney_version-v1.1.xsd
  * Fix: Correct spelling &  Allow multiple infolinks on **FareProduct** [*uml:v96-nk2; doc:v38.03*]
    * netex_fareProduct_version-v1.1.xsd
  * Fix: Add _MobileApp_  to **MediaType** enumeration [*uml:v96-nk2; doc:v38.03*]		
    * netex_travelDocumentSupport_support-v1.1.xsd 
  * Fix: Allow version of derived view id   [*xsd only*]
    * netex_responsibility_version-v1.1.xsd 
  * Fix: Allow **DistanceMatrixView** on *AccessRightParameter**   [*xsd only*]
    * netex_accessRightParameter_version-v1.1.xsd
  * CR: CR0051 Allow *Line* and _documentlinks_ on **Tariff** [*uml:v96-nk2; doc:v38.03*]
    * netex_fareStructureElement_version-v1.1.xsd
  * CR: CR0051 Add _map_ and _faresheet_ to **InfoLink** types [*uml:v96-nk2; doc:v38.03*]
    * netex_utilityTypes_v1.1.xsd
  * CR: CR0051 Allow **Presentation** details on **TariffZone** [*uml:v96-nk2; doc:v38.03*]
    * netex_zone_version-v1.1.xsd
  * Fix: Add _totalNumberParkingSpaces_  to **ParkingProperties** [*uml:v96-nk2; doc:v38.03*]
    * netex_ifopt_parking_version-1.1,xsd
  * Fix: Update **Facility** - correct _nuisance_ to match XML[*uml:v96-nk2; doc:v38.03*]
    * netex_facility_support-v1.1.xsd 
  * CR: CR0049 Change **PiQuery** to **PiRequest** [*uml:v96-nk2; doc:v38.03*]
    * netex_salesTransaction_support-v1.1.xsd   (replaces 1.0)
  * CR: CR0040  Rework to make **Section** a type of **LinkSequence**  [*uml:v96-nk2; doc:v38.03*]
    * netex_commonSection_support-v1.1.xsd ++
    * netex_commonSection_version-v1.1.xsd ++
    * netex_section_support-v1.1.xsd 
    * netex_section_version-v1.1.xsd 
    * netex_linkSequence_version-v1.1.xsd 
    * netex_lineNetwork_version-v1.1.xsd 
    * netex_fareZone_version-v1.1.xsd  
  * CR: CR0049 TM Change. Move _Description_ to supertype for **LinkSequence** [*uml:v96-nk2; doc:v38.03*]
    * netex_journeyPattern_version-v1.1.xsd 
    * netex_journey_version-v1.1.xsd 
    * netex_ifopt_navigationPath_version-v1.1.xsd 
    * netex_ifopt_parking_version-v1.1.xsd
----
### 2017-10-10 Further revisions & Fixes

  * Fix: Correct **FareStructureElement** to allow Multiple interval support,    Add timeIntervals & geographical intervals to fareElement,  Also allow inlining of DistanceMatrixElements [xml]
    * netex_FareStructureELement_version_-v1.1.xsd
    * netex_all_objects_part3_fares-v1.0.xsd
    * netex_all_objects_part3_fares_FS-v1.1.xsd
    * netex_accessRightParameter_version-v1.1.xsd
  * Fix: **CustomerPurchasPeackageElement**   add **GeographicalIntervalRef** & **TimeIntervalRef** [*uml:v96-nk2; doc:v38.03*]
    * netex_CustomerPurchasePackage_version_-v1.1.xsd 

  * CR: CR0049	TM alignment 
    (i) **CustomerPurchasePackage** element add **TypeOfTravelDocument** to **ProductValidityParametersGroup**   [*uml:v96-nk2; doc:v38.03*]
     * netex_accessRightParameter_version-v1.1.xsd
    
    (ii) Fix Add **TypeOfTravelDocument** to **FareTable** specifics   [*uml:v96-nk2; doc:v38.03*]
    * netex_fareTable_version-v1.1.xsd
    * etex_all_objects_part3_fares_FP-v1.1.xsd
    * netex_distanceMatrixElement_version-v1.0.xsd
  
    (iii) Add **TypeOfTravelDocument** to **FareFrame**  [*uml:v96-nk2; doc:v38.03*]
      * netex_travelDocument_version-v1.1.xsd 
  * Fix: NeTEx **FareFrame** had wrong reference 1.0  [*xsd only*]
    * netx_all_objects_part3_fares-v1.1.xsd
    * netex_fareFrame_version-v1.0.xsd 
    * netex_all-v1.0.xsd 
    *  netex_salesTransactionFrame-v1.1.xsd   	
 * CR: CR0051  Misc small fix - **ParkingArea**  add **NumberOfBaysWithRecharging**,  **RechargingAvailable** [*uml:v96-nk2; doc:v38.03*]
    * netex_parkingTariff_version-v1.1.xsd   
    * netex_siteFrame_version-v1.0.xsd 
    * netex_ifopt_all_objects-v1.0.xsd
 * CR: CR0051- **LostPropertyService**:  add **KeptForDuration**.  **LeftLuggage addMaximumDuration**    [*uml:v96-nk2; doc:v38.03*]
    * netex_ifopt_localService_version-v1.1.xsd
    * netex_ifopt_localServiceCommercial_version-v1.0.xsd
    * netex_Ifopt_equipmentAll-v1.0.xsd
    * netex_assistanceBooking_version-v1.0.xsd
----
## 2017-08-17
 * CR: CR0047 - **RailSubmode** add _AirportLink_  as rail submode [*uml:v96-nk2; doc:v38.03*]
    * netex_submode_version-v1.1.xsd     
 * FIX: Reorganise   project folders   [*xsd only*]
   * Split all_object_part3_fares into four sublists -FP, FS, AR, SD
                                     
----
### 2017-08-10 Allign with TM6 Changes   

 * CR: CR0045 TM6: **GenericLoggable** support  **LogEntry**  [*uml:v96-nk2; doc:v38.03*]
   (i) Add generic **Loggable**.  Make **PassengerContractEvent** a type of **LogENtry**  [*uml:v96-nk2; doc:v38.03*]
   * netex_loggable_support-v1.1.xsd 
   * netex_loggable_version-v1.1.xsd
   * netex_salesContract_support-v1.1.xsd
  (ii) Rename **PassengerContractEvent** to **PassengerContractEntry**  NB not back compatible for **TypeOfPassengerContractEvent**[*uml:v96-nk2; doc:v38.03*]
   * netex_salesContract_support-v1.1.xsd
 
    (iii) Add Support for **SecurityLists** & **WhiteLists*** , revise use of **lacklist**.  NB this is functionally, but not syntactically backwards compatible.  [*uml:v96-nk2; doc:v38.03*]
   * +netex_securityList_support-v1.1.xsd 
   * +netex_securityList_version-v1.1.xsd	  		
   * netex_salesContract_support-v1.1.xsd
   * netex_salesContract_version-v1.1.xsd
   * netex_travelDocument_support-v1.1.xsd
   * netex_travelDocument_version-v1.1.xsd
   * netex_retailConsortium_support-v1.1.xsd
   * netex_retailConsortium_version-v1.1.xsd
   * netex_salesTransactionFrame_version-v1.1.xsd
 
   (iv) Add **CustomerPurchasePackage** support  [*uml:v96-nk2; doc:v38.03*]
   * allObjects_part3
   *  ++ netex_customerPurchasePackage_support-v1.1.xsd 
   *  ++ netex_customerPurchasePackage_version-v1.1.xsd      
   * netex_salesTransactionFrame_version-v1.1.xsd    
   
 (iv) Add **CustomerAccount**, **CustomerAccountStatus**, **TypeOfCustomerccount**  [*uml:v96-nk2; doc:v38.03*] 
   * netex_salesContract_support-v1.1.xsd    umlp
   * netex_salesContract_support-v1.1.xsd    umlp
  
   (v) Add **CustomerEligibility** [*uml:v96-nk2; doc:v38.03*]
   * ++   netex_customerEligibility_support-v1.1.xsd umlp
   * ++    netex_customerEligibility_version-v1.1.xsd umlp  
 * CR: CR00xx   Add **Presentation** including graphics to **AllowedLineDirection** [*uml:v96-nk2; doc:v38.03*] 
   * netex_line_version-v1.1.xsd umlp
 * CR: CR0040  Revise **Section**: Add **GeneralSection** distinct from **CommonSection**.   [*uml:v96-nk2; doc:v38.03*] 
      Separate out section  from point and link package. NB not strictly compatible just for **Section** usedIn **LinkSequence**
   * netex_pointAndLinkSequence_support-v1.1.xsd  UMLcp
   * netex_pointAndLinkSequence_version-v1.1.xsd  UMLcp
   * netex_pointAndLink_support-v1.1.xsd UMLcp
   * netex_pointAndLink_version-v1.1.xsd UMLcp
   * netex_lineSection_version-v1.1.xsd UMLcp
   * ++netex_section_support-v1.1.xsd UMLcp
   * ++netex_section_version-v1.1.xsd UMLcp    
 * CR: CR0010 **QuayType** Add _BusPlatform_ enum value [*uml:v96-nk2; doc:v38.03*] 
   * netex_ifopt_stopPlace_support-v1.1.xsd   			
 * CR: CR0030	Add **DayOffsets** [u*uml:v96-nk2; doc:v38.03*] 
   * netex_coupledJourney_version-v1.1.xsd UM p
   * netex_datedPassingTime_version-v1.1.xsd  
   * netex_monitoredPassingTime_version-v1.1.xsd  
   * netex_passingTimes_version-v1.1.xsd  		
 * CR: CR0010 Add **JourneyPartPoisition**  to **JourneyPart** [*uml:v96-nk2; doc:v38.03*] 
   * netex_coupledJourney_support-v1.1.xsd  
   * netex_coupledJourney_version-v1.1.xsd  			
 * CR: CR014 Add **GroupOfLinesType** enum [*uml:v96-nk2; doc:v38.03*] 
   * netex_line_support-v1.1.xsd    
   * netex_line_version-v1.1.xsd   
 * CR: CR0047  Add support for tax to **FarePrice**: self ref on **PriceRule** & **StepResult** [*uml:v96-nk2; doc:v38.03*] 
   * netex_farePrice_version-v1.1.xsd    
   * netex_parkingTariff_support-v1.1.xsd  
   * netex_parkingTariff_version-v1.1.xsd  
----
<<<<<<< HEAD
1.07  2017.06.11 
=======
<<<<<<< HEAD
1.07  2017.06.11 
=======
1.07  2017.06.11 
>>>>>>> f5a5ff0de310736223ba302f0ff70d990ee69dd7
>>>>>>> master
