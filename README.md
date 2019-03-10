# NeTEx (Network Timetable EXchange) XML schema
(C) 2009-2019  NeTEx, CEN, Crown Copyright

## Core, Part 1 (Network),  Part 2 (Timetables), Part3 (Fares) Schemas

Version 1.10 - Base version plus minor fixes comprising 
   * Norway contributions,  
   * The approved 1.1 CRs 1-50
   * Rollup of fixes  and additional documentation on other fixes. 
   * Corrections to  integration of NK  1.09.
   * 1.10 CRS from Meeting Feb 2019 

### Note on the schema
The schema is broken down systematically into small modular files; generally for each functional package in the design model  (See UML Model) there are two xml schema files
   * netex_xxxx_suppport.xsd   - containing data type  and ref definitions
   * netex_xxxx_version.xsd    - containing the element definitions
See the NeTEx UML Physical and Conceptual models for an UML view 

The Part 1, Part 2. & Part 3 Schemas include minor  corrections and enhancements since the issue of the Version 1.0 documents. 
The Version 1.1 documents cover the changes.
----
## Getting Started
There are two main root schemas:
  - **netex_publication** : Embeds NeTEx XML model elements in a bulk output file format for use in asynchronous publication. The intended content scope can be indicated by a filter object.
  - **netex_siri.xsd** : Embeds NeTEx XML model elements in the SIRI protocol  for dynamic exchange of elements between servers. Both Request/response or publish / subscribe is supported

In addition:

  - **nx.xsd** : Embeds NeTeX XML model elements within a simple thematic organisation to facilitate browsing and inspection of NeTEx.   The NX schema is not intended for actual use.

There are **XML examples** of the use of both protocols, see */examples* subdirectory.
 
### Support for XML editors
There is an XMLSpy project file in the root directory  that provides an organised view  of the schema and examples:
  - NeTEx.spp

There is also an Oxygen project file:
  - NeTEx.xpr
----
# Change Log


## 1.10 Summary of Changes since v1.11 
__

### 2019.03.10 EURA-67 *FARES*    Add _courier_ value to ___FulfilmentMethodType___  enumerations.

  * _Updates to xml schema_:     	  
 	* netex_salesDistribution_support.xsd

### 2019.03.10 EURA-91 *FARES*   Add _sameProductLongerJourney_ and _sameProductShorterJourney_ to enumerated values for ___TypeOfExchange___ attribute on   ___Exchanging___ usage parameter. 

  * _Updates to xml schema_:     	  
 	* netex_usageParameterAfterSales_support.xsd
 	
### 2019.03.10  EURA-87 *FARES* EURA-87 Specify if start  of validity is variable or fixed
  * Add a ___StartConstraint___ attribute to ___UsageValidityPeriod___  to  specify if startday  is variable or fixed. 
  * Add  ___UsageStartConstraintTypeEnumeration___ : _variable_ /  _fixed_. 
  * Add  ___FixedStartDayTypes___  day type so that any required day of week, day of month, month of year can be indicated.
  * Also add _enrolment_ and  _reservation_ enum value to ___UsageTriggerEnumeration___.
  * Also add _eligibilityExpiry_  enum value to ___UsageEndEnumeration___.
  * EURA-94  Add _networks_, _operators_ and c_ountries_ to enum values for ___StepLimit___.
 
  * _Updates to xml schema_:   
   	* netex_usagwParameterTravel_support.xsd
 	* netex_usageParameterTravel_version.xsd

### 2019.03.10  UK-38 *FARES*  Add ___MinimumAccess___ and ___MaximumAccess___ to __FareStructureElementinSequence___.

  * _Updates to xml schema_:     	  
 	* netex_fareStructureElement_version.xsd

### 2019.03.10 EURA-81 *FARES*  Make relationshiop with TypeOfFareProduct many-to-many.

  * _Updates to xml schema_:     	  
 	* netex_fareProduct_version.xsd

### 2019.03.10 UK-8 *FRAMEWORK* Add ___LayerRef___ to ___VersionFrame__ and to ___TypeOfFrame___.

  * _Updates to xml schema_:     	 
 	* netex_layer_support.xsd
 	* netex_versionFrame_version.xsd				 

### 2019.03.10 UK-28 *FARES* Add a ___CustomerAccountRef___ to  ___FareContract___.

  * _Updates to xml schema_:     	 
 	* netex_salesContract_version.xsd
 	* netex_salesTransaction_version.xsd

### 2019.03.09 UK-12 *FARES* Add ___GroupOfOperatorRef___  to ___Tariff___ (ie make relationship many to many)
  * _Updates to xml schema_:   
  	* netex_fareStructureElement_version.xsd
	
### 2019.03.09 EURA-78 *FARES* Allow more than one reference to a ___GroupsOfSalesOfferPackageRef___  from a ___SalesOfferPackage___ (i.e. make relationship many-to-many.)
  * _Updates to xml schema_:   
  	* netex_salesOfferPackage_version.xsd

### 2019.03.08 EURA-54 *FARES* Add a Seat reference
  * Add a ___PassengerSeatRef___  to ___ServiceValidityParameterGroup___ of  ___accessRightParamaterAssignment___.
  	* Also Add  ___TravelDocumentRef___ and  ___RetailDeviceRef___ parameter to ___SalesTransaction____.
	* Also Fix: make ___RetailingOrgahisationRef___ an ___OrganisationOperatorRefStructure___ and not an ___OperatorRefStructure____.
  * _Updates to xml schema_:   
  	* netex_vehicleSeating_support.xsd (New)
  	* netex_all_objects_reusable_components.xsd
  	* netex.spp
 	* netex_accessRightParameter_version.xsd
 	* netex_salesTransaction_version.xsd
	 
### 2019.03.08 EURA-43 *FARES* Add new relationship to ___FareZone___ to indicate who who manages it: ___AuthorityRef___ / ___OperatorRef___,   ___GroupOfOperatorsRef___.
  * _Updates to xml schema_:   
 	* netex_fareZone_version.xsd
 	
### 2019.03.08 EURA 51 *FARES* Add  enumeration values to ___RoundTripType___ ; _returnOut_, _returnBack_  so as to distinguish legs.
  * _Updates to xml schema_:  
 	* netex_usageParameterTravel_support.xsd 

### 2019.03.08 PART2 UK-44, UK-69 *FARES* Improve support for defining large tariffs in  modular fashion
  * Add additional  ___groupsOfOperators___  to ___Network___. 
	* Also ___UseToExclude___   attribute to ___GroupOfOperators___.
	* Also add _flexible_ and _urban_ to ___TypeOfLine___ enumeration.	 
	* Add ___UseToExclude___ flag to ___GroupOfLines___.
	* Add ___UseToExclude___ flag to ___GroupOfDistanceMatrixElements___.
  * _Updates to xml schema_:  
 	* netex_line_support.xsd 
 	* netex_line_version.xsd 
 	* netex_transportOrganisation_support.xsd 
	* netex_transportOrganisation_version.xsd 
	* netex_distanceMatrixElementVersion_version.xsd 

### 2019.03.08  UK-14 *FARES* Improvements to ___FareZone___:
 * Add new ___ScopingMethod___  attribute to ___FareZone___ with   values  _explicitStops_,   _implicitSpatialProjection_, _implicitSpatialProjection.
 * UK-13 *FARES*  Add extra  ___ZoneTopology___ enumeration  values   _annular_,   _sequence_, _overlappingSequence_.		 
 * UK-18  Specify  fare stages  on a   pattern: Add new ___IsFareStage___ attribute to ___FarePointInPattern___.
 *EURA  Allow stops to be excluded from a routing.    Add new  ___IsForbidden___ attribute  to ___FarePointInPattern___.
  * _Updates to xml schema_:  
 	* netex_fareZone_support.xsd 
 	* netex_fareZone_version.xsd 

### 2019.03.07 UK-46 *FRAMEWORK* & *FARES* Add open   ___PaymentMethod___ as first class object  so that user defined methods can be added. 
		
  * _Updates to xml schema_:  
 	* netex_travelRights_support.xsd 
 	* netex_travelRights_version.xsd 
 	* netex_salesDistribution_support.xsd 

### 2019.03.07 NJSK *FARES* UK-74 Add enumerations to ___TariffBasis__;  _zoneToZone_, _pointToPoint_, _discount_. 
 * Also add documentation annotations   to existing annotations.
 * _Updates to xml schema_:  
 	* netex_fareStructureElement_support.xsd 

### 2019.03.07 NJSK Fix *FRAMEWORK* Make ___InfrastructurePointRef___ and ___InfrastructureLinkRef___ abstract.
 * _Updates to xml schema_:  
 	* netex_networkInfrastructure_support.xsd 

### 2019.03.07 NJSK-Fix *HOUSEKEEPING*  Delete spurious references in xmplspy  netext.ssp  file.
  * _Updates to other files_:  
 	* netex.spp 

### 2019.03.07  NJSK-Fix *FRAMEWORK* - Correct Type of ___VersionFrameRef___ to be _VersionFrameRefStructure_ , correct substitution group on ___ResourceFrameRef___ to be ___VersionFrameRef___.
  * _Updates to xml schema_:  
 	* netex_resourceFrame_version.xsd 

### 2019.03.07 EURA-40 *FARES* Add support for  Subscriptions
 * Basic steps
	* Subscriptions Add _onlineAccount_ to enumerations  of ___DistributionChannelType___
 	* Add _subscriptionOnly_, also _onCheckIn_, _inAdvanceOnly_, _beforeBoardingOnly_ , _onBoardingOnly_  to  ___PaymentMoment___ enum.  
 	* Fix: add ___PaymentMoment___ to ___PurchaseWindow___
  * _Updates to xml schema_:  
 	* netex_salesDistribution_support.xsd 
 	* netex_travelRights_support.xsd 

### 2019.03.05 UK-24 *FRAMEWORK* & *FARES* Add open   ___PaymentMethod___ as first class object  so that user defined methods can be added.
  * Add _ePayDevice_, _ePayAccount_ and _mileagePoints_ to ___PaymentMethod___ enum
		
  * _Updates to xml schema_:  
 	* netex_travelRights_support.xsd 
 	* netex_travelRights_version.xsd 
 	* netex_salesDistribution_version.xsd 
 	
### 2019.03.05 UK-96 *FRAMEWORK* Add   ___prerequisites___ relationship to ___VersionFrame___.
  * _Updates to xml schema_:  
 	* netex_versionFrame_version.xsd 
 	
   * _Updates to examples_:  
     * Many fares exampels updated to indicate prerequisites. 

### 2019.03.05 UK-09 *FARES* Add ___TypeOfTariffRef___  and ___FareElementInSequenceRef___ to ___TravelSpecification___  so that can  correctly specify choices.
  * _Updates to xml schema_:  
 	* netex_salesTransaction_version.xsd 

### 2019.03.05 UK-19 *FARES* Fix ___PriceGroup___ should be abstract.
  * _Updates to xml schema_:  
 	* netex_farePrice_version.xsd 

### 2019.03.05 NJSK-Fix *PART1* Make alternative name and date visible on ___Direction___.  
 * _Updates to xml schema_: 
 	* netex_route_version.xsd 

### 2019.03.05 UK-41 *FARES* Revise ___UserProfile___ to allow more than one enum values for ___ProofOfEligibilty____.
  * _Updates to xml schema_: ____
 	* netex_usageParameterEligibility_support.xsd 
 	* netex_usageParameterEligibility_version.xsd 

### 2019.03.02 UK-18 *FARES* Add values for ___TypeOfInterval___ 
 * _Updates to xml schema_: 
 	* netex_geographicalStructureFactor_support.xsd 

### 2019.03.02 UK-80 *FARES* Add  further values to ___GenericParameterAssignment____, 
__TypeOfConcessionRef___, ___TypeOfUsageParameterRef___,  ___VehicleType Ref___, ___TypeOfLineRef___.
 * _Updates to xml schema_: 
 	* netex_validityCondition_support.xsd
 	* netex_accessRightParameter_version.xsd

### 2019.03.02 UK-41 *FARES* Add an additional functional operator to ___GenericParameterAssignment___ to clarify use of groups :  
_oneOf_ /  _someOf_/  _allOf_
 * Also correct documentation on relational operators.
 * _Updates to xml schema_: 
 	* netex_validityCondition_support.xsd
 	* netex_accessRightParameter_version.xsd

### 2019.03.01 EURA-(nk) *FARES* Add ___DistanceMatrixInverseRef___ for backwards direction of reference. Revise constraints.  
 * _Updates to xml schema_: 
 	* netex_distanceMatriElement_support.xsd
 	* netex_distanceMatriElement_version.xsd
 	* netex_publication.xsd
 
### 2019.02.28 EURA-10 *FARES* Improve ___CustomerPurchasePackage___.
 * Fix correct case on ___customerPurchasePackageRefs____.
 * Allow  inlining of ___CustomerPurchasePackages___ in a ___FareContract____.
 * _Updates to xml schema_:
  	* netex_customerPurchasePackage_support.xsd
 	* netex_customerPurchasePackage_version.xsd
 	* netex_salesTransaction_version.xsd

### 2019.02.21 UK-20 *FARES* Add contains relationship to ___FareZone___.
 * _Updates to xml schema_:
 	* netex_fareZone_version.xsd
 * _Updates to xml examples_:
  	* uk_fxc_trip_First_WoE_Line48_stage+Passses.xsd

### 2019.02.21 UK-57 *FARES* Add Allow list of ___MachineReadable___  enumerations, 
 * ALso add open ended ___TypeOfMachineRedability___. 
 * _Updates to xml schema_:
 	* netex_travelDocument_support.xsd
	* netex_travelDocument_version.xsd

### 2019.02.21 UK-34 *FARES* TRAVEL DOCUMENT  should not be in FARE FRAME  - remove.
 * _Updates to xml schema_:
 	* netex_travelDocument_version.xsd
	* netex_fareFame_version.xsd
		 
### 2019.02.21 UK-07 *FARES* ___FareTable___ - Allow direct containment of ___FarePriceRef___.
		
 * _Updates to xml schema_:
	* netex_fareTable_version.xsd
 * _Updates to xml examples_:Various to drop unecessary ___cells__ wrapper tags	

 
## 1.10 Summary of Changes since v1.09


### 2019.02.21 .No-Fix *PART2* Reapply 1.09  Fix Merge in correction  to spelling of ___AccountingTime___. NB THis will break any existing documents that use ___AccountingTime___.
 * _Updates to xml schema_:
		* netex_duty_version.xsd

### 2019.02.21 .No-Fix *FARES*  Reapply 1.09  Fix up examples
 * _Updates to xml examples_:  fare examples, Norway examples

### 2019.02.21 NJSK-Fix *FRAMEWORK*  Make dummy types abstract ___TransportOrganisation___ .
  * _Updates to xml schema_:
		* netex_transportOrganisation_version.xsd

### 2019.02.21 NJSK-Fix *FRAMEWORK* Reapply 1.09 Make ___ValidityCondition___ etc visible   [xsd only] 
 * _Updates to xml schema_:
		* netex_travelRights.xsd
        * netex_trainElement.xsd

### 2019.02.21 NJSK-Fix: *FRAMEWORK* Reapply 1.09 Constraint changes and further clean up constraints  [xsd only] 
    *Changes includee
	* (a) Fix keyref constraint on ___TimingLinkInJourneyPattern_AnyVersionedKey___,   (Drop ___DropFarePointInPattern___. ___TimingTimingLinkInJournePattern___, ___StopTimingLinkInJourneyPattern___).
	* (b) Fix keyref constraint on ___ServiceLinkInJourneyPattern_AnyVersionedKey___ (Drop ___xxxPoints___).
	* (c) Fix keyref constraint on ___FarePointInPattern_AnyVersionedKey___ - Add ___xxxPoints___.
	* (d) Fix keyref constraint on ___LinkInJourneyPattern_AnyVersionedKey___ - Ddrop ___xxxPoints____.
	* (e) Fix constraint ___ServiceLinkInJourneyPattern_AnyVersionedKey___ drop bogus ___ServiceService___ selector.
	* (f) Fix ___FarePointInPattern___ Key
	* (g) Fix keyref constraint on StopPointInJourneyPattern - remove bogus ___DeadRunInPattern___ and ___ServiceStopPointInPattern___ selectors.
	* (h) Fix keyref constraint on TimingPointInPattern - remove bogus ___DeadRunInPattern___ and ___ServiceStopPointInPattern___ selectors.
	* (i) Fix uniqueness constraint on  ___HeadwayJourneyGroup___ - drop ___RhythmicalJourneyGroup____.
	* (j) Fix (again) ___Constraints on SalesOfferPackage___ and ___SalesOfferPackagePrice____.
	* (k) Fix keyref  ___LinkInJourneyPattern_AnyVersionedKey___  correct  ___LinkInPattern___ to ___ServiceLinkInPattern___.
	* (l) Fix remove obsolete ___ParkingTaxRate___ constraint
	* (m) Fix Reinstate Constraints on StopPointInJourneyPattern, etc  {NB THIS MAY CATCHE EXISTING ERRORS IN EXAMPLES].
	* (n) Fix Add Constraints on ___SectionInSequence ___. {NB THIS MAY CATCHE EXISTING ERRORS IN EXAMPLES].
	* (o) Revise key names to emphasise when key is ordered separate.
	* (b) Fix Make uniqueness of ___PriceGroup___ and  ___FareTable___.


* _Updates to xml schema_:
      * netex_publication.xsd

### 2019.02.18 NJSK-Fix *FRAMEWORK* Correct data type of ___LayerRef___ and substitution group on ___Layer___  and ___CellRef___ [xsd only] 
   * _Updates to files_: 
        * netex_layer_support.xml 
        * netex_layer_vesrion.xml g

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
 

### 2019.02.18 UK-006 *FARES* - Add missing FARE TABLE  price references  [DOCTODO]
   * Fix: Add ___CellSpecificNetworkGroup___   to Fare Table Specifics, 
   * Fix: Add ___TariffZoneRef , LineRef,, FareZoneRef,  TariffRef,  LineRef, ScheduledStopPointRef___ and   ___FareStructureElementInSequenceRef___. ___SectionRef__ to  ___CellSpecificNetworkGroup____
   * _Updates to xml schema_: 
        * netex_fareTable_version.xsd 

### 2019.01.11 1.09  NJSK-Fix *FARES* Constraints  [xsd only] x
 * Fix: Correction to constraints
     1. Fix keyref constraint on ___TimingLinkInJourneyPattern_KeyRef___ - drop ___xxxPoints___.
     2. Fix keyref constraint on ___ServiceLinkInJourneyPattern_AnyVersionedKey___ - drop ___xxxPoints___.
     3. Fix keyref constraint on ___FarePointInPattern_AnyVersionedKey___ - add ___xxxPoints____
     4. Fix keyref constraint on ___LinkInJourneyPattern_AnyVersionedKey___ - drop ___FarePointInPattern____
     5. Fix constraint ___ServiceLinkInJourneyPattern_UniqueBy_Id_Version_Order___ drop ___ServiceServiceLinkInJourneyPattern____
     6. Fix ___FarePointInPattern___ Key constraint
        
* _Updates to xml schema_:
      * netex_publication.xsd
 
 
### 2019.01.10 HOUSEKEEPING  Migrate to Github. Rename all  schema files to remove version numbers 
* _Updates to xml schema_: 
                * All NeTEx files changed.
                
### 2018.06.02  GITHUBBER  FRAMEWORK Add ___Centroid___ to ___GroupOfStopPlaces___  [uml_diagram, doctodo]
   * _Updates to xml schema_: 
	   * netex_stopPlace_version.xsd
   
----
# 1.09 Summary of Changes since v1.08

### 2018.06.06  CR057 NJSK add URL to Priceable object [DOCTODO]
   * _Updates to xml schema_: netex_farePrice_version-v1.1.xsd
			
### 2018.06.02  1.09 *BUG* Fix ___UsageParameterRef___  - should be abstract to prevent use  [xsd only]
   * _Updates to xml schema_: netex_usageParameter_Support-v1.1.xsd  

### 2018.06.02 *BUG* Fix ___ServiceDesignator___ & ___JourneyDesignator___ - Make fromPoint value optional  [DOCTODO]
   * _Updates to xml schema_: netex_vehicleJourney_Support-v1.1.xsd  
   
### 2018.06.02  1.10 *BUG* Fix Substitution group  ___PointInJourneyPattern___  -  [xsd only]
   * _Updates to xml schema_: netex_journeyPattern-v1.1.xsd  

### 2018.06.02 Add ServiceDesignator to GroupOfServices Member [DOCTODO]
   * _Updates to_:netex_serviceJourney_Version-v1.1.xsd  

### 2018.06.01 CR049 Rename  to align with Transmodel.  Fix case of names  [xsd only]
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
* TM Alignment: Rename ___PassengerContract___ ==> ___FareContract____
* TM Alignment: Rename ___PassengerContractEntry___ ==> ___FareContractEntry____
* TM Alignment: Rename ___PassengerContractSecurityListing___ ==> ___FareContractSecurityListing____
* TM Alignment: Rename ___TypeOfPassengerContract___ ==> ___TypeOfFareContract____
* TM Alignment: Rename ___TypeOfPassengerContractEntry___ ==> ___TypeOfFareContractEntry____

* _Updates to xml schema_: 
    * netex_fareContract_support-v1.1.xsd  
    * netex_fareContract_version-v1.1.xsd 
    * netex_salesTransaction_support-v1.1.xsd  
    * netex_salesTransaction_version-v1.1.xsd  
    * netex_salesTransactionFrame_version-v1.1.xsd  
    * netex_publication.xsd  
    * netex_publication_timetable.xsd   

### 2017.12.20 CR049 Rename  to align with Transmodel [*uml:v96-nk4; doc:v39*]
* TM Alignment: Rename ___SalesPackage___ ==> ___SalesOfferPackage____
* TM Alignment: Rename ___SalesPackageElement___ ==> ___SalesOfferPackageElement____
* TM Alignment: Rename ___SalesPackageSubstitition___ ==> ___SalesOfferPackageSubstitition____
* TM Alignment: Rename ___TypeOfSalesPackage___ ==> ___TypeOfSalesOfferPackage____
* TM Alignment: Rename ___SalesPackageSubstitition___ ==> ___SalesOfferPackageSubstitition____
* TM Alignment: Rename ___GroupOfSalesPackages___ ==> ___GroupOfSalesOfferPackages____


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
