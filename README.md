# NeTEx (Network Timetable EXchange) XML schema
(C) 2009-2019  NeTEx, CEN, Crown Copyright

## Core, Part 1 (Network),  Part 2 (Timetables), Part3 (Fares) Schemas

Version 1.10 - Base version plus minor fixes comprising 
   * Norway contributions,  
   * The approved 1.1 CRs 1-50
   * Rollup of fixes  and additional documentation on other fixes. 
   * Corrections to  integration of NK  1.09.

The scema is broken down systematically into small modular files; generally for each functional package in the design model there are two xml schema files
                    netex_xxxx_suppport.xsd   - containing data type  and ref definitions
                    netex_xxxx_version.xsd    - containg the element definitions
See the NeTEx UML Physical and Conceptual models for an UML view 

The Part 1, Part 2 & Part3 Schemas include minor  corrections since the issue of the Version 1.0 documents. 
The Version 1.1 documents cover the changes
----
## Getting Started
There are two main root schemas:
  - **netex_publication** : Embeds NeTEx XML model elements in a bulk output file format for use in asynchronous publication. The intended content scope can be indicated by a filter object.
  - **netex_siri.xsd** : Embeds NeTEx XML model elements in the SIRI protocol  for dynamic exchange of elements between servers. Both Request/response or publish / subscribe is supported

In addition:

  - **nx.xsd** : Embeds NeTeX XML model elements within a simple thematic organisation to facilitate browsing and inspection of NeTEx.   The NX schema is not intended for actual use.

There are **XML examples** of the use of both protocols, see */examples* subdirectory.
 
### Support for XML editors
There is an XMLSpy project file in the root directory  that provides an organised view  of the schema and examples
  - NeTEx.spp

There is also an Oxygen project file
  - NeTEx.xpr
----
# Change Log


## 1.10 Summary of Changes since v1.11 

### 2019.03.08  UK-14 PART2 UK-44 Improve sopport for defining large tariffs in  modular fashion
	* Add additional  __groupsOfOperators__  to __Network__. 
	* Also __UseToExclude__ flag to __GroupOfOperators__'
	* Also add _flexible_ and _urban_ to _TypeOfLine_ enumeration'	 
	* Add __UseToExclude__ flag to __GroupOfLines__
	* Add __UseToExclude__ flag to __GroupOfDistanceMatrixElements__
  * _Updates to xml schema_:  
 	* netex_line_support.xsd 
 	* netex_line_version.xsd 
 	* netex_transportOrganisation_support.xsd 
	* netex_transportOrganisation_version.xsd 
	* netex_distanceMatrixElementVersion_version.xsd 

### 2019.03.08  UK-14 FARES Add extra __ScopingMethod__  attribute to __FareZone__ with enum values  _explicitStops_,   _IimplicitSpatialProjection_, _ImplicitSpatialProjection
		UK-13 FARES  Add extra  ZoneTopologyEnumeration   attribute  enum values   annular,   sequence, overlappingSequence		 
  * _Updates to xml schema_:  
 	* netex_fareZone_support.xsd 
 	* netex_fareZone_version.xsd 

### 2019.03.07 UK-46 FRAMEWORK & FARES Add open   __PaymentMethod__ as first class object  so that user defined methods can be added.
		Add _ePayDevice, ePayAccount and _mileagePoints_ to __PaymentMethod__ enum
		
  * _Updates to xml schema_:  
 	* netex_travelRights_support.xsd 
 	* netex_travelRights_version.xsd 
 	* netex_salesDistribution_support.xsd 


### 2019.03.07 NJSK FARES UK-74 Add enumerations to __TariffBasis__;  _zoneToZone_, _pointToPoint_, _discount_. Also add documentation annotations   to existing annotations
 * _Updates to xml schema_:  
 	* netex_fareStructureElement_support.xsd 

### 2019.03.07 NJSK Fix Make __InfrastructurePointRef__ and __InfrastructureLinkRef__ abstract
 * _Updates to xml schema_:  
 	* netex_networkInfrastructure_support.xsd 

### 2019.03.07 NJSK-Fix Other  Delete spurious references in xmplspy  netext.ssp  file
  * _Updates to other files_:  
 	* netex.spp 

### 2019.03.07  NJSK-Fix FRAMEWORK - Correct Type of __VersionFrameRef__ to be _VersionFrameRefStructure_ , correct substitution group on __ResourceFrameRef__ to be __VersionFrameRef__
  * _Updates to xml schema_:  
 	* netex_resourceFrame_version.xsd 

### 2019.03.07 EURA-40 FARES Add support for  Subscriptions
	Subscriptions Add onlineAccount to enumerations  of DistributionChannelType
	Add _subscriptionOnly_, also _onCheckIn_, _inAdvanceOnly_, _beforeBoardingOnly_ , _onBoardingOnly_  to  __PaymentMoment__ enum.  
	Fix: add __PaymentMoment__ to __PurchaseWindow__
  * _Updates to xml schema_:  
 	* netex_salesDistribution_support.xsd 
 	* netex_travelRights_support.xsd 

### 2019.03.05 UK-24 FRAMEWORK & FARES Add open   __PaymentMethod__ as first class object  so that user defined methods can be added.
		Add _ePayDevice, ePayAccount and _mileagePoints_ to __PaymentMethod__ enum
		
  * _Updates to xml schema_:  
 	* netex_travelRights_support.xsd 
 	* netex_travelRights_version.xsd 
 	* netex_salesDistribution_version.xsd 
 	
### 2019.03.05 UK-96 FRAMEWORK Add   prerequisites relationship to __VersionFrame__
  * _Updates to xml schema_:  
 	* netex_versionFrame_version.xsd 
 	
   * _Updates to examples_:  
     * Many fares exampels updated to indicate prerequisites. 

### 2019.03.05 UK-09 FARES Add TypeOfTariffRef  and FareElementInSequenceRef to TravelSpecification  so that cann correlty specify choices
  * _Updates to xml schema_:  
 	* netex_salesTransaction_version.xsd 

### 2019.03.05 UK-19 FARES Fix __PriceGroup__ should be abstract
  * _Updates to xml schema_:  
 	* netex_farePrice_version.xsd 

### 2019.03.05 NJSK-Fix PART1 Make alternative name and date visible on __Direction__.  
 * _Updates to xml schema_: 
 	* netex_route_version.xsd 

### 2019.03.05 UK-41 FARES Revise __UserProfile_ to allow more than one enum values for __ProofOfEligibilty__
  * _Updates to xml schema_: 
 	* netex_usageParameterEligibility_support.xsd 
 	* netex_usageParameterEligibility_version.xsd 

### 2019.03.02 UK-18 FARES Add values for __TypeOfInterval__ 
 * _Updates to xml schema_: 
 	* netex_geographicalStructureFactor_support.xsd 

### 2019.03.02 UK-00 FARES Add  further values to __GenericParameterAssignment__
__TypeOfConcessionRef__, __TypeOfUsageParameterRef__,  __VehicleType Ref__, __TypeOfLineRef__  
 * _Updates to xml schema_: 
 	* netex_validityCondition_support.xsd
 	* netex_accessRightParameter_version.xsd

### 2019.03.02 UK-41 FARES Add an additional functional operator to __GenericParameterAssignment__ to clarify use of groups :  
_oneOf_ /  _someOf_/  _allOf_
	Also correct documentation on relational operators
 * _Updates to xml schema_: 
 	* netex_validityCondition_support.xsd
 	* netex_accessRightParameter_version.xsd

### 2019.03.01 EURA-(nk) FARES Add __DistanceMatrixInverseRef__ for backwards direction of reference. Revise constraints  
 * _Updates to xml schema_: 
 	* netex_distanceMatriElement_support.xsd
 	* netex_distanceMatriElement_version.xsd
 	* netex_publication.xsd
 
### 2019.02.28 EURA-10 FARES Improve __CustomePurchasePackage__
 * Fix correct case on customerPurchasePackageRefs
 * Allow  inlining of CustomerPurchasePackages in a FareCOntract
 * _Updates to xml schema_:
  	* netex_customerPurchasePackage_support.xsd
 	* netex_customerPurchasePackage_version.xsd
 	* netex_salesTransaction_version.xsd

### 2019.02.21 UK-20 FARES Add contains relationship to __FareZone__
 * _Updates to xml schema_:
 	* netex_fareZone_version.xsd
 * _Updates to xml examples_:
  	* uk_fxc_trip_First_WoE_Line48_stage+Passses.xsd

### 2019.02.21 UK-57 FARES Add Allow list of __MachineReadable__  enumerations, add open ended TYPE OF MACHINE  READABILITY
UK-57 Add Allow list of MachineReadable  enumerations, add open ended TYPE OF MACHINE  READABILITY
 * _Updates to xml schema_:
 	* netex_travelDocument_support.xsd
	* netex_travelDocument_version.xsd

### 2019.02.21 UK-34 FARES TRAVEL DOCUMENT  should not be in FARE FRAME  - remove  
 * _Updates to xml schema_:
 	* netex_travelDocument_version.xsd
	* netex_fareFame_version.xsd
		 
### 2019.02.21 UK-07 FARES __FareTable__ - Allow direct containment of __FarePriceRef__ 
		
 * _Updates to xml schema_:
	* netex_fareTable_version.xsd
 * _Updates to xml examples_:Various to drop unecessary cel wrappers	

### 2019.02.21 .No-Fix: PART2 Reapply 1.05  Fix Merge in correction  to spelling of AccountingTime. NB THis will break any existing documents that use AccountingTime.
 * _Updates to xml schema_:
		* netex_duty_version.xsd

## 1.10 Summary of Changes since v1.09


### 2019.02.21 .No-Fix PART2 Reapply 1.09  Fix Merge in correction  to spelling of AccountingTime. NB THis will break any existing documents that use AccountingTime.
 * _Updates to xml schema_:
		* netex_duty_version.xsd

### 2019.02.21 .No-Fix FARES  Reapply 1.09  Fix up examples
 * _Updates to xml examples_:  fare examples, Norway examples

### 2019.02.21 NJSK-Fix FRAMEWORK  Make dummy types abstract _TransportOrganisation_ 
		* netex_transportOrganisation_version.xsd

### 2019.02.21 NJSK-Fix FRAMEWORK Reapply 1.09 Make Validity Conditions etc visible   [xsd only] 
 * _Updates to xml schema_:
		* netex_travelRights.xsd
        * netex_trainElement.xsd

### 2019.02.21 NJSK-Fix: FRAMEWORK Reapply 1.09 Constraint changes and further clean up constraints  [xsd only] 
					   (a) Fix keyref constraint on  TimingLinkInJourneyPattern_AnyVersionedKey,   (Drop DropFarePointInPattern. TimingTimingLinkInJournePattern, STopTimingLinkInJourneyPattern)
					   (b) Fix keyref constraint on   ServiceLinkInJourneyPattern_AnyVersionedKey (Drop points)
					   (c) Fix keyref constraint on    FarePointInPattern_AnyVersionedKey - Add Points 
					   (d) Fix keyref constraint on   LinkInJourneyPattern_AnyVersionedKey - drop Points
					   (e) Fix constraint ServiceLinkInJourneyPattern_AnyVersionedKey drop bogus ServiceService selector
					   (f) Fix Fare Point In Pattern Key
					   (g) Fix keyref constraint on StopPointInJourneyPattern - remove bogus DeadRunInPattern and ServiceStopPointInPattern selectors 
					   (h) Fix keyref constraint on TimingPointInPattern - remove bogus DeadRunInPattern and ServiceStopPointInPattern selectors 
					   (i) Fix uniqueness constraint on  HeadwayJourneyGroup - drop RhythmicalJourneyGroup
					   (j) Fix (again) Constraints on SalesOfferPackage and SalesOfferPackagePrice
					   (k) Fix keyref  LinkInJourneyPattern_AnyVersionedKey  correct  LinkInPattern to ServiceLinkInPattern 
					   (l) Fix remove obsolete ParkingTaxRate constraint
					   (m) Fix Reinstate Constraints on StopPointInJourneyPattern, etc  {NB THIS MAY CATCHE EXISTING ERRORS IN EXAMPLES]
					   (n) Fix Add Constraints on SectionInSequence  {NB THIS MAY CATCHE EXISTING ERRORS IN EXAMPLES]
					   (o) Revise key names to emphasise when key is ordered


* _Updates to xml schema_:
      * netex_publication.xsd

### 2019.02.18 NJSK-Fix FRAMEWORK Correct data type of ___LayerRef___ and SubstitutionGroup on ___Layer___  and __Cell_Ref [xsd only] 
   * _Updates to files_: 
        * netex_layer_support.xml 
        * netex_layer_vesrion.xml 

### 2019.02.18 NJSK-Fix OTHER  update XML SPy & Oxygen project files [xsd only]
   * _Updates to files_: 
        * netex.spp 
        * netex.spr 

### 2019.02.18  EXAMPLES - Add new  Fare examples [xsd only]
#### Rail fares

* Example: Distance rail tariff:  
    * Netex_era_distance_ro.xml
* Example: Point to Point Multi-operator National tariff and  single operator regional products: 
    * Netex_era_toc_uk.xml
* Example: Cross-border National tariff : 
    * Netex_crossborder_de.xml
#### Bus fares
* Example: Zone-to-zone bus fares:  
    * uk_fxc_trip_Metrobus_1.xml.xml
* Example: Zonal day & season pass fares:  
    * uk_fxc_pass_Metrobus_metrorider.xml
* Example: Stage trip fares:  
    * uk_fxc_trip_First_WoE_stage-distance_minimal1.xml
 

### 2019.02.18 UK-006 FARES - Add missing FARE TABLE  price references  [DOCTODO]
   * Fix: Add ___CellSpecificNetworkGroup___   to Fare Table Specifics, 
   * Fix: Add ___TariffZoneRef , LineRef,, FareZoneRef,  TariffRef,  LineRef, ScheduledStopPointRef___ and   ___FareStructureElementInSequenceRef___. ___SectionRef__ to  ___CellSpecificNetworkGroup___
   * _Updates to xml schema_: 
        * netex_fareTable_version.xsd 

### 2019.01.11 1.09  NJSK-Fix FARES Constraints  [xsd only] x
 * Fix: Correction to constraints
     1. Fix keyref constraint on ___TimingLinkInJourneyPattern_KeyRef___ - drop points.
     2. Fix keyref constraint on ___ServiceLinkInJourneyPattern_AnyVersionedKey___ -d rop points.
     3. Fix keyref constraint on ___FarePointInPattern_AnyVersionedKey___ - add Points
     4. Fix keyref constraint on ___LinkInJourneyPattern_AnyVersionedKey___ - drop ___FarePointInPattern___
     5. Fix constraint ___ServiceLinkInJourneyPattern_UniqueBy_Id_Version_Order___ drop ___ServiceServiceLinkInJourneyPattern___
     6. Fix ___FarePointInPattern___ Key constraint
        
* _Updates to xml schema_:
      * netex_publication.xsd
 
 
### 2019.01.10 OTHER Migrate to Github Rename all  schema files to remove version numbers 
* _Updates to xml schema_: 
                * All NeTEx files changed.
                
### 2018.06.02  GITHUBBER  FRAMEWORK Add Centroid to GroupOfSTopPlaces  [uml_diagram, doctodo]
   * _Updates to xml schema_: 
	   * netex_stopPlace_version.xsd
   
----
# 1.09 Summary of Changes since v1.08

### 2018.06.06  CR057 NJSK add URL to Priceable object [DOCTODO]
   * _Updates to xml schema_: netex_farePrice_version-v1.1.xsd
			
### 2018.06.02  1.09 BUG Fix ___UsageParameterRef___  - should be abstract to prevent use  [xsd only]
   * _Updates to xml schema_: netex_usageParameter_Support-v1.1.xsd  

### 2018.06.02 ServiceDesignator & JourneyDesignator - Make fromPoint value optional  [DOCTODO]
   * _Updates to xml schema_: netex_vehicleJourney_Support-v1.1.xsd  
   
### 2018.06.02  1.10 BUG Fix Substitution group  ___PointInJourneyPattern___  -  [xsd only]
   * _Updates to xml schema_: netex_journeyPattern-v1.1.xsd  

### 2018.06.02 Add ServiceDesignator to GroupOfServices Member [DOCTODO]
   * _Updates to_:netex_serviceJourney_Version-v1.1.xsd  

### 2018.06.01 CR049 Rename  to align with Transmodel  Fix case  [xsd only]
   * TM Alignment: Rename Sales Package to SALES OFFER PACKAGE 
   * Fix: Correct the camel casing of  groupsOfsaleOfffPackages ==>  groupsOfSaleOfferPackages 
   * Fix: Correct constraint names
   * _Updates to xml schema_: 
        * netex_SalesOfferPackage_version-v1.1.xsd 
        * NeTEx_publication.xsd
        * NeTEx_publication_timetable.xsd	*
        * Nx.xsd
    * _Updates to examples_: 
        * Netex_tap_tsi_B3+more.xml
        * Netex_tap_tsi_B2.xml
        * Netex_tap_tsi_B2-71.xml
        * Netex_tap_tsi_B2-1181.xml
        * Netex_tap_tsi_B2-1180.xml
        * Netex_tap_tsi_tcvs_irt_1.xml
        * Netex_tap_tsi_B3.xml
        * Netex_tap_Train_Hotel_SalesPackage_2.xml
        * Netex_101.21_TflGeographicFares_UnitZone_MultipleProducts
         
 			
### 2018.03.20 1.09  CR047 Fix SupplementToFareProductRef .  Fix ResultStepIdType[xsd only]
   * _Updates to xml schema_: 
        * netex_farePrice_version & netex_FarePrice_support   

### 2018.03.20 1.09  Fix Inheritance Companion ProfileRef a type of UserProfileRef  [xsd only]
   * _Updates to xml schema_: 
        * netex_usageParameterEligibility_support-v1.0 make Companion ''

### 2018.03.20  CR049 Rename  to align with Transmodel - Fix Capitalisation  [xsd only] x
   * Fix Capitalisation of wrapper tags 
        * TM Alignment: ___salesOfferPackages___  should be lower ca.mel case.
        * TM Alignment: ___salesOfferPackageElements___  should be lower camel case.
        * TM Alignment: ___saleslesOfferPackageSubstitutions___ should be lower camel case.
        * TM Alignment: ___salesOfferPackagePrices___ should be lower camel case
        * TM Alignment: ___salesOfferPackageRefs___ should be lower camel case.
     * _Updates to xml schema_: 
        * netex_SalesOfferPackage_support-v1.1.xsd 
        * netex_SalesOfferPackage_version-v1.1.xsd 
        * netex_FareTable_version-v1.1.xsd 
        * nete_AccessRight_Parameters_version-v1.1.xsd 
        * netex_FareProduct_version-v1.1.xsd 
     * _Updates to multiple Examples_.
     	                
   * Fix;  restricted alternate Names on some elements
        * _Updates to xml schema_: 
            * netex_trainElement_version.xsd
 
### 2018.03.20  CR049 Rename  to align with Transmodel    [*uml:v96-nk4; doc:v39*]
* TM Alignment: Rename ___PassengerContract___ ==> ___FareContract___
* TM Alignment: Rename ___PassengerContractEntry___ ==> ___FareContractEntry___
* TM Alignment: Rename ___PassengerContractSecurityListing___ ==> ___FareContractSecurityListing___
* TM Alignment: Rename ___TypeOfPassengerContract___ ==> ___TypeOfFareContract___
* TM Alignment: Rename ___TypeOfPassengerContractEntry___ ==> ___TypeOfFareContractEntry___

* _Updates to xml schema_: 
    * netex_fareContract_support-v1.1.xsd  
    * netex_fareContract_version-v1.1.xsd 
    * netex_salesTransaction_support-v1.1.xsd  
    * netex_salesTransaction_version-v1.1.xsd  
    * netex_salesTransactionFrame_version-v1.1.xsd  
    * netex_publication.xsd  
    * netex_publication_timetable.xsd   

### 2017.12.20 CR049 Rename  to align with Transmodel [*uml:v96-nk4; doc:v39*]
* TM Alignment: Rename ___SalesPackage___ ==> ___SalesOfferPackage___
* TM Alignment: Rename ___SalesPackageElement___ ==> ___SalesOfferPackageElement___
* TM Alignment: Rename ___SalesPackageSubstitition___ ==> ___SalesOfferPackageSubstitition___
* TM Alignment: Rename ___TypeOfSalesPackage___ ==> ___TypeOfSalesOfferPackage___
* TM Alignment: Rename ___SalesPackageSubstitition___ ==> ___SalesOfferPackageSubstitition___
* TM Alignment: Rename ___GroupOfSalesPackages___ ==> ___GroupOfSalesOfferPackages___


* _Updates to xml schema_: 
  * netex_salesPackage_support-v1.1.xsd ==>   netex_aalesOfferPackage_support--v1.1.xsd 
  * netex_salesPackage_version-v1.1.xsd ==>   netex_aalesOfferPackage_version-v1.1.xsd 
	     
### 2017.12.20  Fix up fare examples


## 1.08 Summary of Changes since v1.07

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
<<<<<<< HEAD
1.07  2017.06.11 
=======
1.07  2017.06.11 
>>>>>>> f5a5ff0de310736223ba302f0ff70d990ee69dd7
=======
1.07  2017.06.11
>>>>>>> c2651736b895a8c248140a36ddccb227e3a13402
