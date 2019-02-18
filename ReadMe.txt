<<<<<<< HEAD
NeTEX XMl schema
(C) 2009-2017  NeTEX, CEN, Crown Copyright
        
NeTwork EXchange : Core, Part 1 (Network),  Part 2 (Timetables , Part3 (Fares)   Schemas
================================================
version 1.09



Sybtypes of travel sepc
Version 1.08 - Base version plus minor fixes comprising Norway contributions
=======
NeTEx XML schema
(C) 2009-2017  NeTEx, CEN, Crown Copyright
        
NeTwork Exchange : Core, Part 1 (Network), Part 2 (Timetables), Part3 (Fares) Schemas

 
Version 1.09 - Base version plus minor fixes comprising Norway contributions
>>>>>>> c2651736b895a8c248140a36ddccb227e3a13402
Plus most  of the 1.1 CRs
 
See the NeTEx UML Physical and Conceptual models for an UML view

<<<<<<< HEAD
The Part 1, Part 2 & Part3 Schemas include minor  corrections since the issue of the documents, 

There is an XMLSpy project file in the root directory  that provides an organised view  of the schema and examples
    
  - netex-v1.08.spp
  
There is also an Oxygen project file

   - netex-v1.08.xpr
=======
The Part 1, Part 2 & Part3 Schemas include minor corrections since the issue of the documents.

There is an XMLSpy project file in the root directory  that provides an organised view  of the schema and examples
    
  - netex.spp
  
There is also an Oxygen project file

   - netex.xpr
>>>>>>> c2651736b895a8c248140a36ddccb227e3a13402

====================

Getting Started:
  
There are two main root schemas

  - netex_publication : Embeds NeTEx XML model elements in a bulk output file format for use in asynchronous publication. The intended content scope can be indicated by a filter object. 

  - netex_siri.xsd : Embeds NeTEx XML model elements in the SIRI protocol  for dynamic exchange of elements between servers. Both Request/response or publish / subscribe is supported

In addition

<<<<<<< HEAD
  - nx.xsd : Embeds NeTeX XML model elements within a simple thematic organisation to facilitate browsing and inspection of NeTEx. 
=======
  - nx.xsd : Embeds NeTEx XML model elements within a simple thematic organisation to facilitate browsing and inspection of NeTEx. 
>>>>>>> c2651736b895a8c248140a36ddccb227e3a13402
    The NX schema is not intended for actual use. 

There are XML examples  of the use of both protocols. see examples subdirectory.
   
=====================================================================================================================
<<<<<<< HEAD
 
=====================================
TODO
   CheckNameconstraints on Place & Subtypes - e.g. Address & Garage cannot have same id
     
=====================

Generic
      remove LIFECYLE EVENt - to do
      shcmeatic map  diag uml todo
      Add rel to Assignment diag uml doctodo
      Revsie fleixble line / booking arrangements / contact uml diagram to refkec 
      redraw stop place quay
      redraw check constraint, point of interest, topograhic place  TM2 trav sepc mod



      2017.12.20Renamed
=======
      
=====================
   Diagram  updates to do
      schematic map  diag uml todo
      Add rel to Assignment diag uml doctodo
      Revise flexible line / booking arrangements / contact uml diagram to reflect  
      redraw stop place quay
      redraw check constraint, point of interest, topographic place  TM2 trav mod

================================================
     
version 1.09
     2018.03.20  Rename  to align with Transmodel   xsd uml
           PassengerContract ==> FareContract
           PassengerContractEntry ==> FareContractEntry
           PassengerContractSecurityListing ==> FareContractSecurityListing  
           TypeOfPassengerContract ==> TypeOfFareContract 
	    TypeOfPassengerContractEntry ==> TypeOfFareContractEntry
    	 netex_fareContract_support-v1.1.xsd  
	 netex_fareContract_version-v1.1.xsd 
	  netex_salesTransaction_support-v1.1.xsd  
	 netex_salesTransaction_version-v1.1.xsd  
	  netex_salesTransactionFrame_version-v1.1.xsd  
	  netex_publication.xsd  
	 netex_publication_timetable.xsd  
     2017.12.20 Rename  to align with Transmodel
>>>>>>> c2651736b895a8c248140a36ddccb227e3a13402
          SalesPackage ==> SalesOfferPackage
          SalesPackageElement ==> SalesOfferPackageElement
           SalesPackageSubstitition ==> SalesOfferPackageSubstitition
           TypeOfSalesPackage ==> TypeOfSalesOfferPackage
              SalesPackageSubstitition ==> SalesOfferPackageSubstitition
<<<<<<< HEAD
           GroupOfSalesPackages ==> GroupOfSalesOfferPackage

===================================

1.08
=======
           GroupOfSalesPackages ==> GroupOfSalesOfferPackages

          
         netex_salesPackage_support-v1.1.xsd ==>   netex_aalesOfferPackage_support--v1.1.xsd 
	 netex_salesPackage_version-v1.1.xsd ==>   netex_aalesOfferPackage_version-v1.1.xsd 
	     
	     
       2017.12.20  Fix up fare examples

===================================

Version 1.08
>>>>>>> c2651736b895a8c248140a36ddccb227e3a13402

2017-12.01  Further revisions & Fixes
        Fix add notice assignments to GroupOfDIstanceMatrixElements
           netex_distranceMatrixLement_version-v1.1.xsd

        Fix nove alternative Tets up hierarchy to EntityInVersion
         FIX move ALterativeName to genericFramework so Organisation can reference. uml doc done
           netex_organisation_version-v1.1.xsd 
           netex_all_objects_generic_version-v1.0.xsd
           
         FIx add contact details to line as per uml
           netex_line_version-v1.1.xsd
           
         FIX update uml diagram for PropertyOfDay, Line
<<<<<<< HEAD
         
         
=======
                  
>>>>>>> c2651736b895a8c248140a36ddccb227e3a13402
         FIX cd  - Place should be type Place_VersionStructure 
         		  netex_placee_version-v1.1.xsd

	Cr0019/Cr0013 correct type on dayT offsets on COurseOfJourney and ReliefOpportunity Intechange rule
 			netex_vehicleService_version-v1.1.xsd
        			  netex_interchange_version-v1.1.xsd
        			  netex_coupledJourney_version-v1.1.xsd

          Add infolinks to GroupOfENtities
                   netex_groupin-v1.1.xsd
           -   Fix Add  day offset to JourneyMeeting  docdone 
                    netex_interchange-v1.1.xsd
                   
2017-11.08  Further revisions & Fixes

   		 
     -   Fix Add  day offset to Journey Part Couple  docdone
				 netex_coupledJourney_version-v1.1.xsd
	Fix   Correct spelling &  Allow multiple info links of Fare Product 
		netex_fareProduct_version-v1.1.xsd


	 Fix Add MobileApp  to MediaType enumeration Docdone		
		netex_travelDocumentSupport_support-v1.1.xsd 
		
         Fix  Fix allow version of derived view id   xsdonly
            		netex_responsibility_version-v1.1.xsd 
            		
         Fix Allow distance Matrix View on  xsdonly
         		netex_accessRightParameter_version-v1.1.xsd
         		
         Allow line and document links on  tariff details  docdone
		netex_fareStructureElement_version-v1.1.xsd
		Add map and faresheet to infolink types
		netex_utilityTypes_v1.1.xsd
		
	  Allow presentation details on TariffZone umldone Docdone
	  netex_zone_version-v1.1.xsd

          Add total number parking spaces umldone Docdone
    		    netex_ifopt_parking_version-1.1,xsd
    		    
          Fix Update Facility correct nuisance to match XML umldone
         	 netex_facility_support-v1.1.xsd 

        TM Change PiQuery ro PiRequest 
		netex_salesTransaction_support-v1.1.xsd   (replaces 1.0)

	TM Change: Rework so Make Section a type of Link Sequence docDOne
			netex_commonSection_support-v1.1.xsd ++
			netex_commonSection_version-v1.1.xsd ++
			netex_section_support-v1.1.xsd 
			netex_section_version-v1.1.xsd 
			netex_linkSequence_support-v1.1.xsd 
			netex_linkSequence_version-v1.1.xsd 
			netex_lineNetwork_version-v1.1.xsd 
			netex_fareZone_version-v1.1.xsd  
					
	Moved Description to supertype for  docDone
		netex_journeyPattern_version-v1.1.xsd 
		netex_journey_version-v1.1.xsd 
		netex_ifopt_navigationPath_version-v1.1.xsd  (replaces 1.0)
		netex_ifopt_parking_version-v1.1.xsd

		
2017-10.10   Plugging Holes

	(i) Fix     Multiple intervals support DocDONE
	a)  FareSTructureElementFactorGroup docdone
             Add timeIntervals & gerographical intervals to fareElement
             Also allow inling of DistanceMatrixElements
                netex_FareStructureELement_version_-v1.1.xsd
                
                netex_all_objects_part3_fares-v1.0.xsd
                -->netex_all_objects_part3_fares_FS-v1.1.xsd
                -->netex_accessRightParameter_version-v1.1.xsd

	b) CustomerPurchasPackageElementSelection Group  Docdone
    		add GeographicalIntervalRef & TimeIntervalRef

		netex_CustomerPurchasePackage_version_-v1.1.xsd 
	
	
	(ii) Fix  
	
	   (a) CustomerPurchasePackage element Add TypeOfTravelDocument to ProductValidityParametersGroup  DOCTODO3
		netex_accessRightParameter_version-v1.1.xsd
		
	    (b) Fix Add TypeOfTravelDocument to FareTable specifics  doc done
	          netex_fareTable_version-v1.1.xsd
	         ->netex_all_objects_part3_fares_FP-v1.1.xsd
	         -->netex_distanceMatrixElement_version-v1.0.xsd
	         
	    (c) Add TypeOfTravelDocument to FareFrame
	  		  netex_travelDocument_version-v1.1.xsd 
	  		  
	(iii) NeTEx fare frame had wrong reference 1.0 of 
	      netx_all_objects_part3_fares-v1.1.xsd
	-->netex_fareFrame_version-v1.0.xsd 
	-->netex_all-v1.0.xsd 
	-->netex_salesTransactionFrame-v1.1.xsd   		  
	
        Small holes
            ParkingArea  add NumberOfBaysWithRecharging  uml xsd umldone docdone
                       UML add RechachingAvailable (alraed in xsd)
            
            netex_parkingTariff_version-v1.1.xsd   docdone
               -->netex_siteFrame_version-v1.0.xsd 
	       -->netex_ifopt_all_objects-v1.0.xsd
	       
	 CR00xx- LostPropertyService:  add KeptForDuration.  LeftLuggage addMaximumDuration     umldone docdone
	    netex_ifopt_localService_version-v1.1.xsd
	       -->netex_ifopt_localServiceCommercial_version-v1.0.xsd
	       -->netex_Ifopt_equipmentAll-v1.0.xsd
	       -->netex_assistanceBooking_version-v1.0.xsd
	       
	     
	       
2017-08-17 .no CR0047 - RailSubmode add AirportLink  as rail submode umldone docdone
       netex_submode_version-v1.1.xsd    umlp
       
       
       *     revise  project folders        
            Split all_object_part3_fares into four sublists -FP, FS, AR, SD
                                     

2017.08.10 TM6 CR0045 GenericLoggable support  LogENtry  DocDONE
                (i) Add generic Loggable.  Make PassengerCOnrractEvent a tyep of log entry
                 netex_loggable_support-v1.1.xsd  umlp
                          netex_loggable_version-v1.1.xsd  umlp
                     netex_salesContract_support-v1.1.xsd    umlp
           (ii) Rename PassengerContractEVent to PassengerCOntract Entry  NB not back comaptibel for TypeOfPassengerContarctEvent
                         
                     
2017.08.10 TM6 CR0049 Allign with TM6 Changes  DocDone
		(i)  Add Support for SECURITY LISTS & white lists  , revise use of Blacklist
			 NB this is functionally, but not suntatcicaly backwards compatible.
			+netex_securityList_support-v1.1.xsd umlcp
			+netex_securityList_version-v1.1.xsd	umlcp 		
			netex_salesContract_support-v1.1.xsd umlcp
			netex_salesContract_version-v1.1.xsd umlcp
			netex_travelDocument_support-v1.1.xsd umlcp
			netex_travelDocument_version-v1.1.xsd umlcp
			netex_retailConsortium_support-v1.1.xsd umlcp
			netex_retailConsortium_version-v1.1.xsd umlcp
			netex_salesTransactionFrame_version-v1.1.xsd umlcp
                    
                    Still need tosort out Substitution groups (all at DataManagedObejct)

                  (ii)Add CustomerPurchasePackage support  DocDOne
                   CUSTOMER PURCHASE PACKAGE 
                allObjects_part3
             ++   netex_customerPurchasePackage_support-v1.1.xsd umlp
             ++    netex_customerPurchasePackage_version-v1.1.xsd umlp     
                netex_salesTransactionFrame_version-v1.1.xsd umlp   
                
                  (iii) Add CustomerAccount, CustomerAccountStatus, TypeOfCustomerccount DocDOne 
                         netex_salesContract_support-v1.1.xsd    umlp
                              netex_salesContract_support-v1.1.xsd    umlp
                  
                  (iv) Add CustomerEligibility DOCTODO3
                    ++   netex_customerEligibility_support-v1.1.xsd umlp
          	   ++    netex_customerEligibility_version-v1.1.xsd umlp  
<<<<<<< HEAD
            
            
              CRxx   Add Presentation inc graphics to Allowed Line Direction umlp docdone
                netex_line_version-v1.1.xsd umlp


=======
                        
              CRxx   Add Presentation inc graphics to Allowed Line Direction umlp docdone
                netex_line_version-v1.1.xsd umlp

>>>>>>> c2651736b895a8c248140a36ddccb227e3a13402
               CR40  Revise Section: Add GENERAL SECTION distinct from COMMON SECTION  umldone docdone
                  Separate out from point and link package UMLcp
                  NB not strictly compatible just for Section usedIn Sequence
                   	netex_pointAndLinkSequence_support-v1.1.xsd  UMLcp
		   	netex_pointAndLinkSequence_version-v1.1.xsd  UMLcp
		   	netex_pointAndLink_support-v1.1.xsd UMLcp
			netex_pointAndLink_version-v1.1.xsd UMLcp
			netex_lineSection_version-v1.1.xsd UMLcp
			++netex_section_support-v1.1.xsd UMLcp
			++netex_section_version-v1.1.xsd UMLcp
                   

		CR0010 QuayType Add BusPlatform Enum    umldone docdone
			netex_ifopt_stopPlace_support-v1.1.xsd  UMLp
<<<<<<< HEAD
			
			
=======
						
>>>>>>> c2651736b895a8c248140a36ddccb227e3a13402
		CR0030	Add Day Offsets DocDOne
		netex_coupledJourney_version-v1.1.xsd UMLp
		netex_datedPassingTime_version-v1.1.xsd Umlp
		netex_monitoredPassingTime_version-v1.1.xsd UMLP
		netex_passingTimes_version-v1.1.xsd UMLP
		
<<<<<<< HEAD
		CR0010 Add JpOURNEY PART POSITION to JOURNEY PART DocDOne
			netex_coupledJourney_support-v1.1.xsd umlp
			netex_coupledJourney_version-v1.1.xsd umlp
			
			
=======
		CR0010 Add JOOURNEY PART POSITION to JOURNEY PART DocDOne
			netex_coupledJourney_support-v1.1.xsd umlp
			netex_coupledJourney_version-v1.1.xsd umlp
						
>>>>>>> c2651736b895a8c248140a36ddccb227e3a13402
		CR014 Add GroupOfLinesType enum uml DOCDONE
			netex_line_support-v1.1.xsd   umlp
			netex_line_version-v1.1.xsd  umlp
		
<<<<<<< HEAD


=======
>>>>>>> c2651736b895a8c248140a36ddccb227e3a13402
		CR0047  Add Support for tax: self ref on priceRule & stepResult umlDone DOC DONE
			netex_farePrice_version-v1.1.xsd   umlp
			netex_parkingTariff_support-v1.1.xsd umlp
			netex_parkingTariff_version-v1.1.xsd umlp
<<<<<<< HEAD

=======
>>>>>>> c2651736b895a8c248140a36ddccb227e3a13402
1.07  2017.06.11 

		CR0042  StopPointInJourneyPattern add StopRequestMethod   umlDone DOCDOne
			netex_servicePattern_support-v1.1.xsd  umlp
			netex_servicePattern_version-v1.1.xsd   umlp

		CR0008 InterchangeRule Allow multiple lines and directions on filter  umlDone DOCTODO2
			netex_interchangeRule_version-v1.0.xsd  umlp

		CR0023  Add BookingArrangements to StopPointInPattern umlDone DOcDOne
  			Netex_servicePattern_version-v1.1.xsd umlp
  			
		CR0005  Add BookingContact to Booking Arrangements umlDone DOcDOne
		  netex_travelRights_version-v1.1.xsd umlp
		  
                CR0002+ - Revise AlternativeTextSupport  umlDone DOcDOne
             	  netex_alternativeText_version-v1.1.xsd umlcp
               
		CR0036+   Add municipality  to Topographical place type - umlp  docDOne
		CR0041 Add support  to associate COMMON SECTIONS with LinkSequences xsd uml  docDOne
			netex_pointAndLinkSequence_support-v1.1.xsd umlcp
			netex_pointAndLinkSequence_version-v1.1.xsd umlcp
			netex_pointAndLink_support-v1.1.xsd umlcp
			netex_pointAndLink_version-v1.1.xsd umlcp

            	   Fix:  make Route ref in TimingPattern optional   
                
                
                CR0041  Add twice daily FREQUENCY OF USE  usage eneum docdone
                         netex_travelUsageParameter_support-v1.1.xsd  umlp

		Change List v 1.04  <Modified>2017-06-095 Fixes to Constraints xsdonly
			CR0038 revise constraints on ResponsibilityRole, REsponsibilitySet
					              
		 	Correct COnstraints for PointOnRoute  
			      Add  Missing Constraints For CommonSectionMember/PointOnSection 	& LinkOnSection 	
			      Add missing constraints for JourneyAccounting
			 Reinstate  Constraints for CAll   Discuss 
			 Fix constraints that were missing namespace on subpart 

 	+- 2017.05.04 v 1.04	CR0041  xsd umldone  docDone
		<Modified>2017-05-25</Modified> Add  contact telephone number and operator / operators associated with Garage.   
                  Add Organisation  & associatedOperators to Garage 
                  netex_vehicleAndCrewPoint_version-v1.1.xsd
                

 	+- 2017.05.04 v 1.04	  Improve packaging of elements  xsdonly
 			CR017 Allow Inlining of NOTICE in NOTICE  ASSIGNMENT
  				netex_noticeAssignment_version-v1.1.xsd
 
 			CR031 Allow inlining of STOP POINT, STOP PLACE, QUAY etc in sSTOP ASSIGNMENT  so as to iimprove packaging  (no semantic change) xml 
 				 Add  NameSuffix attribute to ScheduledStopPoint
  		    	 netex_scheduledSTopPoint_version-v1.1.xsd
  		    	 	 netex_pointAndLink_version-v1.0.xsd

  	Cr0040  Allow linking of POINTS in Section.   UML docdone
			Add PointOnSection  for list of jpoints (RetainCOmmonSectionMember for backwards compatibilit  UML docdone
			Add LinkOnSection  for list of just links.   umlcp
			Add nameOfLinkClass attribute to help implementors.  xsdonly
 
	2017-05-22   CR0xx Integrate Fixes from SV Pull requests xsdOnly

  		

 	+- 2016.08.03 v 1.04 NB the following may have been lost because windows puts CRS in?
 	+    - Replacement of carriage returns with new lines (for e.g. easier file change diff) 

 	+- 2017.08.01 v 1.04 xsdOnly
 	+    - Corrected enumeration values ("noFoodAvailableAvailable" to "noFoodAvailable", "intermational" to "international" and "coffeeSohp" to "coffeeShop")
                     correct intermational to international for rail submode xsd only
                       netex_submode_version-v1.1.xsd
                       
                     correct coffeshop to Coffeeshop   and xsd only
  			netex_facility_support-v1.1.xsd
  			
  	 +- 2017.02.04 v 1.04	  			
  		     Remove duplicate enums from vehicleType enum xsd only
  		    	 netex_facility_support-v1.1.xsd
  		
  	 +- 2017.02.15 v 1.04
  		     Make PassengerEquipment "Gender"  optional  xsd only
  		  	 netex_ifopt_equipmentPassenger_version-v1.0.xsd
  	
  	 +- 2017.02.04 v 1.04
  	  +- 2017.02.23 v 1.04  xsd
  		     documentation corrections; align with specification.
  		         netex_lineNetwork_version-v1.0.xsd
  		         netex_line_equipmentParking_version-v1.0.xsd  		
  		         netex_vehicleJourneyFrequency_version-v1.0.xsd
  		  	 netex_flexibleNetwork_version-v1.0.xsd  
  		         netex_servicePattern_version-v1.0.xsd
  		         netex_flexibleNetwork_version-v1.0.xsd
  		         
  		         netex_serviceJourney_version-v1.1.xsd
  		         netex_vehicleJourney_version-v1.1xsd
  		         netex_line__version-v1.1.xsd
  		         netex_versionSupport-v1.1.xsd
  		         
  	 +- 2017.02.04 v 1.04	         
  		   Remove obsolete file
  		         part1_tacticalPlanning/netex_journeyTimings_version-v1.0.xsd


		NPR Only allow one accessibility Limitation per Assessment, as per Specification.
		netex_accessibility/netex_acsb_accessibility-v1.0.xsd  		     



	2017-05-26   CR0034 Add charter taxi uml  docdone  
			Netex_submode_support-v1.1.xsd umlcp
  		         
	2017-05-22   CR0034 Add routeInstruction   xsd - UML  docDone
			Netex_routeInstruction_support-v1.1.xsd  umlp
			Netex_routeInstruction_version-v1.1.xsd  umlp


   	2017-05-22   CR0035  Add open Type of Congestion to Check Constraint uml  docdone 
   	                     Add CHeck COnstraintref to call
			Netex_ifopt_checkCOnstraint_support-v1.1.xsd
			Netex_ifopt_checkCOnstraint_version-v1.1.xsd
			Netex_call_version-v1.1.xsd

        2017-05-22   Allow timetable pdfs for line uml  docdone 
                add values to Type of Infolink Document, TimetableDocument
                add timetabelLinks to Line
                 	netex_utility_types-v1.1.xsd
				netex_line_version-v1.1.xsd
				
       2017-03-27  XX0000   Add FareManagement to Role Types enum uml  docdone 
                     add  SecurityManager and DataRegistra to data rolis xsdtodo doctodo3
                     
	2017-03-27  CR0001 - Vehicle Type add more Vehicle Dimensions     doc docdone
				netex_vehicleType_version-v1.1.xsd umlp


      - 2017.03.27 CR0003  - Add AlternativeText  to DataManagedObject  uml  docdone   tm
                              new netex_alternativeText_suppor__v1.0.xsd umlcp
                               new netex_alternativeText_support__v1.0.xsd  umlcp
			      Update:  netex_responsibility_version_v1.0.xsd
			   NB in principle version  numbers of all dependent packages (almost the whole of netex should be change dto 1.1

	2017-03-27  CR0004 - Notice: Add Short name   added    docdone
				netex_notice_version-v1.1.xsd umlp

	2017-03-28  CR0006 - Allow reference to FlexibleServiceProperties as choice with embedding xsd only
				netex_serviceJourney_version-v1.1.xsd  
				
	2017-03-28  CR0010  Journey Part - Add order.  dded     DOCTODO2
				netex_coupledJourney_version-v1.1.xsd   umlp
				
	2017-03-27  CR0011 - Print colours: PrintPresentation for    to lines  uml  uml  docdone 
				netex_utility_types-v1.1.xsd  umlp
				netex_line_version-v1.1.xsd   umlp
				
	2017-03-28  CR0012 - External Refs: Add versionRef to ObjectRef so that version can be cited on an external xsd docDOne todo
				 Add modification to version refs to support delta exchange.  xsdOnly
				netex_relationship_support-v1.1.xsd
				
	2017-03-28  CR0015 - Group Of Stop Places added      docdone
				netex_stopPlace_version-v1.1.xsd umlp
				netex_siteFrame_version-v1.1.xsd umlp
				
	2017-03-28  CR0018 - Submode added to Group of lines added  umlp  docdone
				netex_line_version-v1.1.xsd	umlp			
				
	2017-03-28  CR0028 Add accessibility Assessment (Fix)   xsd DOCTODO2
				netex_journey_version-v1.1.xsd   xsdOnly
				
	2017-03-28  CR0030 Vehicle Journey Service Times: add DepartureDayOffset  DOCTODO2
				netex_vehicleJourney_version-v1.1.xsd umlp 
				
	2017-03-28  CCR031 add Countries in Site Frame added  umlp  docdone
		 	     netex_address_version-v1.1.xsd  
			    netex_siteFrame_version-v1.1.xsd umlp
		  
	2017-03-28 CR0031  OCR031 Add Zones to RESOURCE FRAME added  umlp   uml  docdone 
		
			  netex_resourceFrame_version-v1.1.xsd umlp
			  netex_zone_version-v1.1.xsd xsdOnly
			  
	2017-03-28 CR0031  Organisation & Organisation Part Add Own ResponsibilitySet  added    docdone
			netex_organisation_version-v1.1.xsd umlp

	2017-03-28 CR0032  Improve COdespaces added  uml  docdone
	                   Add Type fo Assignment, Start Value, end value maximumLength
			netex_organisation_version-v1.1.xsd umlp
			netex_organisation_version-v1.1.xsd umlp
		
	2017-03-28  CR0036 Fixes: 1a. FareZoneRefs/Ref should be ,multiple, not single 
				1b fareScheduledStopPointRefs/Ref should be multiple, not single
				Also
				Allow COuntry and interegion on types TopographicPlaceType
				Add principality to country ref  
				  netex_topographicPlace_support-v1.1.xsd umlp
				   netex_country_support-v1.1.xsd  umlp
				
	2017-03-28 CR036 Fixes 2)  Make ValidityParameter Assignment not abstract 
			and fix ambiguity with GenericParamete
			netex_accssRightParameterVersion-v1.1.xsd	xsdOnly	
		
	2017-03-28 CR036 Fix CR0038 Correct  ResponsibilitySet to be a substitutiongroup for DataManagedObject so it can appear in a General Frame.
				netex_responsibilitySet_version-v1.1.xsd
			Direction to be a SG for TypeOfValue xsdOnly
			netex_route_version-v1.0.xsd  xsdOnly
			
	2017-05-26 CR036 Fix CR0038 
			Make GeneralFrame Group of entities any type of GroupOfEntities not just GeneralGroup
			netex_grouping_version-v1.1.xsd xsdOnly
			
     2017.04.27 CR0038 Add missing  TypeOfRoleModel  , add PrivateCode ro Responsibility Set umldone docDOne
			netex_responsibilitySet_version-v1.1.xsd umlp
				
     - 2016.07.22 v 1.04
		- Cleaning of the repository (one single version of each file, no more versioned folder, etc.)
		- update of the v1.02 zip file (it was containing the v1.01 version)
		- initialisation of the 1.04 version
		- integration of Norway's contributions:
			- minor fixes for Xerces schema validatation and automated JAX-B generation 
			- replacement of carriage returns with new lines 
			
     - 2015.11.24 v 1.03
			- Add RequiresAccount  to ConditionSummary in NeTEx Fare Condition SUmmary Product 
			      netx_conditionSummary-v1.0.xsd umlp
			- Integrate 10.01 and 1.02 changes

     - 2015.07.30 v 1.02 CD
            - Constraint KeyValuePair Xmlns corrected in NeTEx_publication.xsd and NeTEx_publication_timetable.xsd
            - Constraint on Codespace Xmlns (Codespace_AnyVersionedKey_Xmlns) corrected in NeTEx_publication.xsd and NeTEx_publication_timetable.xsd
            - Added constraint in <KeyList> element in netex_responsibility_version-v1.0.xsd
            - Added LE Corbusier stop place example (French Stop profile compliant) in examples\standards\neptune
            - Add no constraint version of schema for slow XML spy use.
xxx
     - 2015.03.17  v 1.01
            - Add support for GTFS timing interpolated 
                 Add attribute interpolated to CallPart  dx]
            - Tidy up UML
            - Add missing TypeOfLine ref to UML
     
     - 2015.01.02 v 1.01
            - With minor fixes by CD to wdsl files
		in siri_wsProducer-Framework.xsd
		    <xsd:import namespace="http://www.siri.org.uk/siri" schemaLocation="../siriSg.xsd"/>
		Replaced by (no more SIRI SG and NeTEx prefix ....)
		    <xsd:import namespace="http://www.siri.org.uk/siri" schemaLocation="../NeTEx_siri.xsd"/>

		-----------------------------------------
		in NeTEx_wsProducer-Document.wsdl
		move up GetNeTexService and GetNeTexServiceResponse (just under import of "../netex_siri.xsd")
		Add "Request" and "Answer" wrapper (for WSDL RPC compatibility) to GetNeTexService and GetNeTexServiceResponse

		------------------------------------------------------------------------   
		in NeTEx_wsConsumer-Document.wsdl
		move up NotifyNetex (just under import of "../netex_siri.xsd")
		Add "Request" wrapper (for WSDL RPC compatibility) to NotifyNetex

		------------
		In NeTEx_wsProducer-Rpc.wsdl 
		Fix of a namespace issue compared to Document version: in all operation  replace 
				<soap:body use="literal" namespace="http://wsdl.netex.org.uk/netex"/>
		with
				<soap:body use="literal" namespace="http://www.siri.org.uk/siriWS"/>

		Same thing in NeTEx_wsConsumer-Rpc.wsdl



     -       2014.09.20 Turin  Meeting Comments V 1.00
               Release as V1.0
                     
    - Changes affecting existing netex xml docs are marked (MODEL CHANGE),.dx = diagram change.  x xml change
    
         2014.06.16 Stenungsund  Meeting Comments V 97.8
             [Stenungsund ]
            
              [Transmodel] Add VehicleTypeStopAssignment to VehicleJourneyPackage x dx. [TX leave ]
              [Transmodel] Add TrainComponentNumberAssignment to VehicleJourneyPackage x dx. [TX leave ]
              [Transmodel] Add OperationalOrientation attribute to JourneyPart x dx. [TX leave] 
              [Transmodel] Correct definitions on via, AccessRightParameterassignment, usage parameter.  x. dx. [Tx leave ]
              [Transmodel] Add CommonSectionRef to NoticeAssignment. x dx.  (Leave tx)
               [kb] Add ContactDetails to Distribution Assignment  x dx [TX Part3 TODO]
               [Fx] Add PrivateCode to ValidityTrigger so can tie to external event. x.  dx. (Leave tx)
               [fr] Allow POIClassification on validityParameters [Tx toDO]
               [fr] Add UntilPrevious day to PurchaseWhen conditions. x dx  [Tx Part3 toDO]
               [fr] Add BookWhen  to BookingArrangements x dx     [Tx Part3 toDO]
               [fr] Add latestbookingtime to PurchaseWindow. x [Tx Part3 toDO]
               [fr] Add a new Cancelling element  dx [Tx Part3 toDO]
               [fx] Limit SalesPackage to assigning to GenericParameterAssignmment x dx [TX Part3 toDO] MODEL CHANGE
               [fx] Add name to COupledJourney x dx
               [fx] Add LuggageChargingBasis to LuggageALlowance  x dx [TX Part3 toDO]. 
               [fx] Move Reselling and Transferablity types to an AfterSalesPackage. x dx.
               [fx] Add Heated and Airconditined to WaitingRoomEquipment. x dx [TX Part1 Leave]
               [fx] Add Dogs Must be carried to TravelatorEquipment. x dx [TX Part1 Leave]
           
               [fx] Update CELL ASSIGNMENT UML to include GROUP OF SERVICES and type of fare product dx. [TX TODO]
               [fx] Simplify Condition to follow UML  x.              
               [fx] Correct labels in physical model for references dx.
               [fx] Correct SpecialService attributes - add missing attributes  and allow multiple day types  x.
               [fx] Nest temporalValidityParameters inside a wrapper tag x.
	       [Fx] Correct VehicleStopping to use QuayALigment and VehiclePositionALignment elements x. [TX leave part1] MODEL CHANGE
	       [Fx] Add ref  elements for local services and correct idtype names x.
	       [fx] Add ref  elements for passenger equipment and correct idtype names x.
	       [Fx} Simplify  DataObjectService FIltering x dx . Add UML diagrams for SIRI
	       [Fx} Simplify  Add UML diagrams for detaild GTFS Mapping
	       
	       [Fx sj] Correct enumerated values for  days of week on diagrams dx [Part1 leave]
	       [fx sj] Correct enumenumerated valueso n Travel Usage parameters dx [Part3 tx ToDO]
	       [fx sj] COrrect uml for Group of sales packages to reflect xms.  dx [Part3 tx to do]
	                      
	       [fx] Correct physical UML diagram for PStopAssignment/PassengerSTopassignment to link STopPlace to PassengerStopAssignment.
	              NB COnceptual model StopAssignment is more like PassengerSTopAssignment than STop Assignment.
               [fx gtfs] Allow booking arrangemenst on  Call for how to get bus to stop,
               [fx gtfs] Add BookingWhen to Rserving so that can specify whether ticket can be bought on board at stop etc.
               [fx gtfs[ add isAvailable to Daytype Assignment to allow exception.
               [Fx gtfs } Simplify  Add UML diagrams for detaild GTFS Mapping
               
               [Modularisation Corrections] 
               [mod fx] Improve modularisation: move datedJourneyIds, servicejourneyids,  to separate subpackages x.
               [mod fx] Improve modularisation: move equipment ids to separate subpackages x.
               [mod fx] Improve modularisation: move commercial service  ids to separate subpackages x.     
               [mod fx] Improve modularisation:  Separate out type definitions of vehiclejourneyFrequency and dataedvehicleJourney x.
               [mod fx] Move journey folders to journey type folder  x.
               [mod fx[ Make physical attributes optional dx. 
               [mod fx] Move NoticeAssignments up hierachy to Journey x dx. MODEL CHANGE [TX PArt1 LEAve]
               [mod fx] Improve modularisation: move vehicle stopping   ids to separate subpackages x. nodoc

	       [mod fx] remove forward dependency: Move FlexibleLine place referebce -  remove flexiblePlaces from Flexible line and add flexibleLineRef to Felxible Place so that there is not a forward reference x. MODEL CHANGE

               [mod fx] Remove unneeded reference to passenger equipment from TrainElement package. x. nodoc
               
               [Diagram fx] Correct TimingLinkInJourneyPattern and TimingPointInJourneyPattern run times, wait times
               [Diagram fx] Correct Cardinality shown for CallPart in diagrams dx.    [TX PArt2 LEAve]  
               [Diagramfx] Shop TopgraphicPlace on StopPlace diagram  [TX Part1 leave]
               [kb Diagram fx] Align optionality of attributes in UML diagrams dx.  [TX PArt1/2 LEAve]     
		       PART1 FRAMEWORK
			EnityInVersion: status, modification
			Version: status, versiontype
			Pointandlinksequence: Distance  

		       PART1 reusable
			Accessibility: UserNeedname,  Limitations
			Service calendar Name and short name
			Operating Period Name
			OperatingDay : earliest time DayLenth
			DayTypeAssignment: Date  DayTypeRef, OperatingDayRef
			Operator: County, primary mode
			OrganisationalDayType: IsServcieDay
			PlaceEequipment: Units
			VehicleEquipmentProfile: Units
			PassengerCapacity: FareClass
			Accomodation: ClassOfUseREf
			TrainElement: TrainElementType

		       PART1 model

			VehicleTypeAtPoint:  Capacity
			OvertakingPossibility: OvertakingWidth
			LineNetwork: Name
			RouteLink: Distance
			DestinationDisplayVariant: vias
			DisplayAssignment: NumberOfJourneysToShow, DisplayAssignmentType
			RoutePoint: Viaflag, borderpoint
			Route: DirectionType
<<<<<<< HEAD
			SiteElement: NameSuffix, CrossRoad, LandMArk, PublicUse, COvered, Gated, Lighting
=======
			SiteElement: NameSuffix, CrossRoad, LandMArk, PublicUse, Covered, Gated, Lighting
>>>>>>> c2651736b895a8c248140a36ddccb227e3a13402
			EquipmentPosition: Description, PointProjection
			Entrance: IsExternal, IsENtry, IsExit, DroppedKerbOutside, DropOffPointClose
			Accomodation: Gender, Berthtype
			StopPlace: StopPlaceType
			Quay: QuayType
			AccessSpace: AccessSpaceType
			StopPlaceSpace: BoardingUse, ALightingUSe
			PointOfInterestSpace: AcessSpaceType, PointOfInterestSpaceType
			NavigationPath: AccessFeatureType, NavigationType
<<<<<<< HEAD
			PathJunction Label, COvered, gated, Lighting
=======
			PathJunction Label, Covered, gated, Lighting
>>>>>>> c2651736b895a8c248140a36ddccb227e3a13402
			FlexibleSTopPlace: VehicleMode
			CheckCOnstraint: Period, MaxiumPassengers, Average Passengers, WheelchairPassengers 
			Parking: CardsAcceptes, NumberOfParkingLevels, BookingUrl
			CrossingEquipent: CrossingTYpe
			TrolleyStandEequipment: FreetoUsey, FareClass
			ShelterEquipment: ENcosed, DistanceFrom NearestKerb
			StairENd: ContinuingHandrail, TexturedSurface, VisualCOntrast 
			StairGroup: Depth
			EscalatorEquipment: TactileACtuators, EnergySaving, DogsMustBeCarried
			EscalatorEquipment: TactileACtuators, EnergySaving, DogsMustBeCarried, Speed
			HeadingSiIgn: LineMap, LinePublicCOde
			AssistanceService: AccessibilityTrainedStaff
			TicketingService: TiketCounterService
			LeftLuggageService: CouterService, SelfServiceLocker, FeePerBag, LockerFee, MaximumBagWidth, MaximumHeight, MaximumBagDepth
			LuggageService: LuggageTrolleys, FreetoUse, LuggageServiceType, WheelchairLuggageTrolleys
			CustomerService: Email, Phone, InfoLink, PostalAddress
			MeetingPointService: Label
			VehicleStoppingPosition: InfrastuctureElementRef
			TransferRestiction: TransferRestrictionType
			TimeDemandTypeAssignment: TimebandRef, GroupOfTimeBandsRef, TimeDeamndTypeRef
			StopPointInJournetPattern: ForBoarding, For alighting, StopUse
			TimingPointInJourneyPattern: OnwardTimingLinkRef, IsWaitPoint
			FlexibleLine: FlexibleLineType

		       PART2
			Journey: ExternalVehicleJourneyRef
			VehicleJourney: DepatureTime
			StopAssignment: Boarding use
			ServiceJourney: DirectionType
			GroupOfServices: Direction Type
			GroupOfServices: DayTYpeRef
			CoupledJourney: Description
			Journeypart: StartTime, ENdTime
			ServiceJourney - FlexibleService properties
			SpecialService: Client
			JourneyWaitTime: WaitTime
			JourneyRunTime: RunTime
			Journeyfrequenccy; HeadwayInterval
			NormalDatedVehicleJourney ServiceALteration
			TrainBlockPart: Type OF Coupling
			Call/ StopUse  VisitNumber
			Call/ Arrival/Departure:  time, is felxible, ForAlighting 

		       PART3 
			FarePointInPattern: InterchangeAllowed
			FareStructureInterval: TimeIntervalRef
			TimeInterval: StartTime, EndTime
			FareStructureFcator: Factor
			FareProduct: TypeOfFareStucture
			CardCOnditionSUmmary: MustcArry
			Cell: fareClass, CEll SPecifc AssignmentsGroup
			FareTable: EmbargoUntil
			CellSpecificAssignmentsGroup ROutingType, DirectionType
			FarePrice: Ranking
			PricingParameterSet: AllowCUmultaiveDisocunts, PricingMethodName
			RouteValidityParametersGroup: RoutingType, Directions

			TripPlanQuery: UseRealT9ime, MaximumNUmberOfJoruneys, QueryOptimisation
			StopDepartureQueryPolicy: UseRealT9ime, MaximumNUmberOfJoruneys, MaximumResultsANyLine

		       OTHER
			RideInterchange: Duration
			Ride: Duration
               
               
        2014.03.25 Cologne Meeting Comments V 97.7
             [Cologne] 
              	 [Fr feedback]Rename GlobalValidityParametersGroup to OrganisationValidityParametersGroup x. dx. tx.
              	 [Fr feedback]Rename Network Validity Parameters Model to ScopingValidity Parameters Model  x. dx. tx.
    	      	 [Fr feedback]Rename ValidityParameterAssignmentScopeGroup  to ParameterAssignmentScopeGroup x. dx. tx.
              	 [Fr feedback]Rename LimitingUsageParameterGroup to  UsageValidityParameterGroup x. dx. tx.
              	[TransModel] Add AddressablePalce. Make SiteElement and Garage a type of AddressablePlace. x. dx. (Leave TX pt 1)
             	 [Transmodel] Add relationship  for additional countries to TopographicPlace to allow for cross border regions x. dx.  (Leave TX pt1)
              	[Transmodel] Allow ValidityConditions on any object: refactor  validity conditions from  the following: 
              		Point, Link, LinkSequence, Zone, Equioment, FacilitySet, Transfer x. dx. (Leave TX pt 1)
           	  	 StopAssignment, Block, NoticeAssignment, TransferRestriction x. dx. (Leave TX pt 1)
             		 GroupOfDistanceMatrixElements, DistanceMatrix, Price Group, Tariff , FareStructureElement,  x dx
              	FareProduct, DistributionCHannel, FareDemandFactor, ParkingTariff, PriceGroup, InterchangeRule, SalesPackage
             	 CheckConstraint, CheckConstraintDelay, CheckConstraintThroughput
              	QualityStructureFactor, SeriesConstraint, ServiceACcessRight, 
    		[Fr feedback]  Add Additional bus submodes:     highFrequencyBus, dedicatedLaneBus x. dx.  (Leave TX pt 1)
    		  [Fr feedback]  Add Additional coach submodes:     SchoolCoach x. dx.  (Leave TX pt 1)
    		 [Fr feedback]  Add otherModes to LINE   x. dx.  (Leave TX pt 1) 
    		[Fr feedback]  FlexibleLineType and FlexibleRouteType made distinct  x. dx.  (Leave TX pt 1) 
      		 [Fr feedback] Add NameOf member class to GeneralGroup of entities.  x dx  (Leave TX pt 1)              
      
              
              [Fx] Add TopographicalPlace to DistributionAssignment. x. dx. tx.
              [Tap Fx] Add Branding entity  and ref on DataManagedObject x.  (Leave TX pt 1)
              [Fx} Correct Type on MeetingPoint Type x. (Leave TX pt 1 diagrams)
              [Fx} Correct types on Equipment subtypes x. (Leave TX pt 1 diagrams)
              [Fx] Set version numbers to 1.0, improve comments x only.               
          	[Fx] Change to use SIRI 2.0 x only
              [Fx] Corrections to types in DELTA x. (Leave TX pt 1)
              [Fx] Rename ClassInCOntextRef  to CLassInRepositoryRef x dx (Leave TX pt 1)
              [Fx] Update DefautLocation type on frame to be srsName. Add to TypeofFrame x. dx. (Leave TX pt 1)
              [fx] Add AttributeInRepository to allow farme contents to be specified. x  (Leave TX pt 1)
              [Fx] Rename delegatedresponsibilitesSet to delegatedResponsibilitySet  x. (Leave TX pt 1)
              
              [Fx] Revise Constraints
		[Fx} Add constrainst for FrameRefs. x only.
		[Fx] revise constraints so that PointInPatten, LinkInPattern (Timing and Service)  must be unique  on id /order  x dx.
		[Fx] revise constraints so that PathInPatten,    must be unique  on id /order  x dx

		[Fx] Add constraints for SalesNoticeAssignments unique on id /order x  dx
		[Fx] revise constraints so that TrainComponent ,    must be unique  on id /order
		[Fx] revise constraints so that PlaceInSequence ,    must be unique  on id /order
		[Fx] revise constraints so that FareStructureElementInSequence ,    must be unique  on id /order
		[Fx] revise constraints so that ControllableElementInSequence ,    must be unique  on id /order
		[Fx] revise constraints so that AccessRightsInProduct ,    must be unique  on id /order
		[Fx] revise constraints so that GereicParameterAssignment  etc ,    must be unique  on id /order
	      [Fx] Tidy up comments x.
	      [Tap - add bew examples B1 , b2] 
              [Tap fx] Add NightTrain to Travel conditions. x.dx. tx.
              [Tap fx] Add ValidDuring and ValdiBetween  conditions. x.dx. tx.
              [Tap fx] Add either / both to Minimumstay type enum. x.dx. tx.
              [Tap fx] Add none value to daysofweek enumeration, allow days as alternative encoding. x. (Leave TX pt 1)
                [Tap fx] Revise uniqueness constraints on Usage aparameters x.dx. tx.
                 [Fx] Wrap Fare Table refs in a pricesFor tag x 
                 [Tap fx] Add DirectionType to Cell x. dx. tx.
                 [Tap Fx ] Add PriceableObject elements to Group of SalesPackages. x. dx.tx,
                 [Tap fx] Add alternative names to type of Travel document. x. dx. tx.
                 [TapFix Add FareProductRef to Distribution Assignment x dx. tx.
                 [TapFix allow fromANytIme Until ANytime onExchangeabl x. dx tx.
                 [TapFix] Add Alloperators, AllCOuntries, AllDistributionChannels x dx tx.
                 [TapFix] Add GeneralGroupOfEntitiesRef x dx, (Leave TX pt 1)
                 [TapFix] Add GroupOfNotices to NoticAssignment x (Leave TX pt 1)
                 [TapFix Add Private Code to SeriesConstraint  x  dx tx.
                 [TapFix] add FareBAsis to series element x dx. tx.
                 [TapFix] Add presentation order to DeliveryVariant x. (Leave TX pt 1)
                  [FX] Make product uniqueness constraint by product type., price by specific price type, usage parameter by specific parameter type
                  [TapFix] map Series route to SeriesCOnstraint  order  x dx tx
                  [TapFix] B1 use SalesPackage instead of Tariff  (TAPDOC)
                  [TapFix] Add Tariff basis to COnditionSummary   x dx tx
                  [Tapfix] Add salesPackagelemenst to fare frame x dx tx.
                  [Tapfix] Add group of services to service validity parameters x dx tx.
              [Fx} Typeof Frame on object reqyest can eb specifed as weell as parameters. x. NODOC
              [Fx] Add ValidDuring, ValidBetween simple conditions. x  (Leave TX pt 1) 
              [Fx] Make AccessRrightParameterAssignment abstract x NODOC
              [Fx] Shorten FarePointInJourneyPattern to FarePointInPattern so also correct for SeriesCOnstraint x dx.
              [Fx} Add LinkByValue types add DistanceMatrixByValue as optimisation x [tx todo]
              [Fx] Correct types on SalesNoticAssignmentRef
              [Fx] Restrict prices to type of object  x dx  [TX TODO???]
              [Fx] AssistanceBooking should use noticeAssignment, not Notice   x dx  (Leave TX pt 2) 
              [Fx} Make fare structure use Validity Parmeter ass.  x. only allow accessrightparams at Frame level. dx tx.
              [Fx} Add Assignment Abstract type and refactor to use it x dx  tx
              		 NoticeAssignment, DayTypeAssignment x dx [Leave TX pt 1]
              		 DisplayAssignment, x dx [Leave TX pt 1]
                         NetworkRestriction, etc,ActivationAssignment,   x dx  [Leave TX pt 1]
                         TransferRestriction, ServiceExclusion,  x dx  [Leave TX pt 2]
                         TimeDemandTypeAssignment x dx [Leave TX pt 2]
                         StopAssignment etc, PathAssignment,  FlexibleStopAssignment, CheckConstraint, CheckConstraintDelay, CheckCOnstrainthroughput, x dx [Leave TX pt 1]
                         JourneyAccounting,,[Leave TX pt 2]
                      
                         DistributionAssignment, x dx tx
                         AccessRightAssignment,  x  dx TX  
                         SalesPackageSubstitution x dx TX  
             [Fx] Allow train number ref in group of services list x [dx TODO]  [LEAVE TX pt 2]           
             [Fx] Rename SeatClass to FareClass x dx tx.            
                  TO SORT OUT is INTERCHANGE RULE REALLY AN ASSIGNMENT , NOT AN INTERCHANGE - needs relationship to INTERCHANGE. 
             [Fx} Remove AccessRightParameterAssignmentRef so that assignments cant be reused x  only
             [Fx} Remove NoticeAssignmentRef so that assignments cant be reused x  only
             [fx] Correct Timing PointIn pattern to allow notice assignment x. [LEAVE TX pt 2] 
             [Fx[ correct case of photoBooth x. only.
             [Fx] Update Dependency diagrams dx tx
             [fx] Correct types shown as abstract in UML diagrams eg responsibilitySet, Interchangruleparameter
             [Fx] Correct name of DatNamespaceAssignment Codespace asisgnment in diagram dx [LEAVE TX pt1]   
              [Fx] Correct spelling of CheckConstraintThroughputIdType x.    [LEAVE TX pt 1] 
              [Fx] Remove duplicate Order attribute on CHeckCOnstraint x [Leave TX pt 1]
              [Fx] Simplify remove seprate availabilityForPucrahse rela on Sales package - use validity condition on Purchase window  x dx.
              [Fx] Remove accessRightAssignments from accessrightInProduct x dx tx.      
              [Fx] Correct type on InterchangeRuleType x
              [Fx} Correct JourneyAccounting AccountedObjectRef type x. dx   [Leave TX pt 2)
              [Fx] Correct so that compound access right includes  must be of same type, eg generic generic, specific specific  x. dx  
              [fx] Travel specification needs to incldue NoticeAssignments x dx tx
              [Fx] Fix NetworkTRestriction ref types               n x dx [LEAVE TX PT 1 diagrams]
              [Fx] Reorder elements on zone so that geometry is together (Centroid)  x. (Leave TX pt 1)
              [Fx] BookingArrangement should have notice assignments not notices x [Leave TX pt 1)
              [Fx] Correct types on ResponsibilityRoleRef, PointOnLinkRef , PointOnRouteRef LineNetworkRef x. [Leave TX pt 1)
              [Fx] Correct types on SiteRef ACccessSpaceRef,  ServceFacilitySetRef, GroupOfDistributionChannelsRef, JourneyMeetingRef,  x [Leave TX pt 1)
              [Fx] Correct types on FlexibleStopASsignmentRef, FlexibleServicePropertiesRef,  f  x. [Leave TX pt 1)
              [Fx] Correct types on ActivationLinkRef, PassengerCapacityRef  PassingTimeRefs  x. [Leave TX pt 1)
         2014.01.22 Paris Meeting Comments
            [Fx] Make version numbers default, not fixed   x 
            [Paris] Rename ProductParameter model to Eligibility Parameter Model dx x tx
            [Paris] Rename scope and limitation elements dx x tx
            [Paris] Add separate entitlement pparameter package and model dx x tx
            [Fx] Remove wrong elements from TravelSpecification  x dx tx
            [Paris] Align terminology for validity parameters 
            Rename ScopeGrouping Type to ValidityParamaterGroupingType  x dx tx
                    Rename AccessRightAssignmentParameter <Scope> to <validityParameters>  x dx tx
           Rename AccessRightAssignment.for <Scope> to <Limitations> x dx tx
           Rename AccessRightAssignmantParameter <AssignmentType> to <ValidityParametersAssignmentType> x dx tx
           Rename all the xxxxScopeGroup  to xxValidityParamtersGroup   x tx dx
            [Paris] Allow  Multiple DistanceMatrix elements on FareStructureELmenet. 
                Add DistanceMatrixElement & GroupOfDistanceMatrix elements to FarseStructure element  x dx tx
                Add remove DistanceMatrixElement & GroupOfDistanceMatrixElements from AccessPathAssignment              NB this also affects TapTSI
            [Fx} Correct TravelSpecification attributes. 
                    add payment method and creditcard no  and Membershipref to SalesTransaction x dx tx
                    Add DistributionAssignmentRef and RetailingOrganisationRef and collection point to Specific parameter assignment x dx tx
            [Paris] Rename UsageParameterProduct to UsageParameter Eligibility x dx tx
                    Add new UsageParameter Charging with parameters from CappingRule  x dx tx.
            [Paris] Add interchangeallowed to SeriesConstraint.FarePointInJourneyPattern x dx tx.
            [Paris] Revise Capping Rule 
                    Make Capping rule a priceable obejct and allw to assign to it. x dx tx
                    Move Capping rule attributes to a new CHargingPolicy element    SameStatio ReentryPolicy, MinimumTimeBeforeReentry, CreditPolicy
                    remove CappingStartENum x dx tx
                    Add PenaltyPolicy x dx tx
            [Paris] Add topology classification to FareZone and allow adjacent zones to be listed. x dx tx
            [Paris] Remove bogus extra copy of Rounding month offset  dx. only
            [Fx]    Add Start of period to UsageTrigger values x tx
            [Profile] Add ClassRelationshipInFrame, to frame add RelID and  [TX TODO] 
            [Profile] Move metamodel elements to a Proifle Package. x TODO  dx
            [Fx] Add TypeOfValidtyref to ClassInFrame x dx [Leave Part 1] 
            [Fx] Move inheritance  relationship to be between entity not entityinframe
            [Fx] Add Includes to type of version frame   x dx] {Leave Part 1]
       [Transmodel] Add Layer support x. dx tx
            Add VehicleOrientation to compound train x dx {Leave Part 1]
            Add ReversedOrientation to TrainInCImpoundTrain x. dx {Leave Part 1]
         [Fx] Change to use SIR 2.0 
            
   2013.11.17  Delft Meeting comments
      [Fx] Allow in line train  compound train x. 
      [Delft] Make ThirdPartyProduct a type of Product dx x tx. df
      [Delft] Consolidate AccessRightAssignment dx x tx. MDLCHG
      [Delft] Revise pricing structure - separate DiscountingRule Object dx x tx. MDLCHG      
      [Delft] Add PricingRule, DiscountingRule, LimitingRule dx x tx. df MDLCHG
      [Delft] Add default PricingRuleREf to PriceableObject dx x tx. 
      [Delft] Make SERIES PATTERN a priceable Object and add a price   dx x tx. MDLCHG   
       [Delft] Rename  SERIES PATTERN  to SERIES CONSTRAINT dx x tx. MDLCHG  
       [Delft] Add direct relationship from Fare Structure ELement to GeographicalInterval, TimeInterval and DistanceMatrixElement dx x tx.
       [Delft] Link Tariff, FareTable (And othe places ) to ORGANIZATION  rather than just operator  x dx Tx.
       [Delft] Rename Pricing Parameters to PricingParameterSet dx x tx. df  MDLCHG  
       [Delft] Add EndTime and Day Offset to StartTimeAtStopPoint dx  x  tx.
       [Delft] Fix Time Interval values   x  dx tx.
       [Delft] Add units and type to Geographical Interval x dx tx. MDLCHG  
       [De;ft] Add Refund type, Payment Method to Refund so that can cover conditions of carriage x dx tx.
       [Fx] Add uniqueness constraints for GeographicalUnitPrice and TimeUnitPrice and Discounting Rules x
       [Fx] Modularisation Move PriceUnit to FareCalculationParameters Packagae dx x tx.
       [Fx} Allow FareTable to embed other tables dx x tx.
       [Fx] Change capping rule to ref TimeInterval not TimeFactor dx x tx.
       [Fx] Add TravelCreditPolicy  ,  SameStationReentryPolicy and Same StationReentry time to CappedDiscountProduct. x dx tx.
       [Fx] Rename some  package files to be more consistent x.
       [Fx] Add Short trip to RoundTrip. x dx 
       [Fx] Add AllowInverse attribute to DistanceMatrixElement x dx
       [Fx] Rename ParkingTarifPrice to ParkingPrice.  x dx tc.
       [Fx] Rename ParkingTariffChargeBand to ParkingChargBand, PartkingTariffTaxRate to ParkingTaxRate x dx tx.
       [fx] Revise PI QUery model dx tx.
       [Fx] Revise PassengerTrip Model dx tx.
        [Fx] Nest limitations in for kewyord. add operator.  x dx tx. 
       
     2013.10.14  Align with CONCEPtual  099.6 WIP2
        [wkg] Revise prices to be Reference or Discountable.  COllapse Discount/Limit Price x  dx tx. MDLCHG
        [Add] PricingParameters as wrapper  with cumulativeDiscounts. x dx tx. MDLCHG
        [Fx] Add Replacing Usage parameter x dx tx.
        [Fx] Add banknotes, warrant voucher to methods of payment. x dx.
        [Fx] Add extra values to ProofOfIdentity  on UserProfile. x dx tx.
        [Fx] Add extra values to TypeOFfare  on ConditionSUmmary. x dx tx.
        [Fx] SPlit ConditionSummary into smaller groups x dx tx.   
        [Fx] Revise COnditionSummary add OperatorREstrictions, revised train Restrictions x dx. MDLCHG
        [Fx] Add residency condition to UserProfile x dx tx
        [Fx] Revise CappingRule to reference Validable element TimeStructureFactor  x dx  tx.MDLCHG
        [Fx] Rename FarePointInPattern FarePoitsInJouneyPattern x dx tx MDLCHNG
        [Fx} Rename CompanionOrGroupMember to CompanionProfile x dx tx MDLXHG
        [Fx] Rename TypeOfContract into TypeOfPassengerContract x dx tx MDLXHG
        [Fx] Rename TypeOfContractEvent into TypeOfPassengerContractEvet  x dx tx MDLCHG
        [Fx] Add factor value  to common fare structure factor x dx tx
        [Fx] Add TimeUnitPrice and GeographicalUnirPrice. Make FareUnit a PriceableObject x dx tx MDLCHG
        [Fx] Add Uniqueness constraint for ValueSet, PricingParameters,  FareFrame and SalesTransactionfarme  x.
        
    2013.09.14  Align with CONCEPtual
            [Fx] Rename Contract to PassengerContract x dx. MDLCHG 
            [Fx] Rename ContractEvent to PassengerContractEvent x dx. MDLCHG 
            [Fx] Reorder FareFame elements and rename farePrices to farePriceGroups x. MDLCHG
            [Fx] Move ValdiableElement to ControllableElement Package and rename to Validable element 
            [Fx] Regroup and reorder Physical model elements x. MDLCHG.
            [Fx} Correct Series pattern attributes and reorder, add Discrete etc x dx MDLCHG
            [FX] Make FareStrureElement, FareInterval,  FareFactor  SalesPAckageElement subtypes of Priceable objects. x dx
            [FX[ Add Controllable elemntInSequence to FAreSTructure model x dx.
            [Fx] Make TimeInterval a type of FareInterval x.
            [Fx] Move SalesDistribution assignment to SalesPackage package x.
            [Fx] Reorder SalesPackage , DistanceMatrixELement and other elements. x dx. MDL CHG
            [Fx] ADd parameters to Exchanging x dx
            [tx] Rename ReturnAVailable on ROundTrip to TripType  x dx MDL CHG
            [Fx] Make FareTable independent of Price Group x dx MDL CHNG
          
            
        2013.09.15 0.99.5 WIP 3
            [Fx] Add StepLimit x dx 
                 [Fx] Add SlaesNoticeAssignment and revise NoticeAssignment_ x.   
            [WG Turin-pl] Add ServicACcessRight higher ion hierarchy
    [WG Turin-pl] Add GroupOfEntiies GeneralOOrganization  on Entlement Product?
            [Fx]  Correct Validable Element Prices
            [Fx]  Correct Parking Tariif  Element Prices and Tax Rate x  MODEL CHANGE
            [Fx]  Move Notice & Notice Assignments to beginning of FareFram x  MODEL CHANGE
            [Fx] Add stepNegotiation to AssistanceNeeded
             
    [WG Turin-5t] Add ForwardsOnly attribute to Routing - boolean routing x. dx.
    [WG Turin-5t] Add fufilment value to UsageTriggerENum x dx
    [WG Turin-5t] Add dayOffsetBeforeCalendarPeriod value to UsageTriggerENum x dx
    [WG Turin-5t] Add MonthValidityOFfset   to FareFrameDefaults x dx
    [WG Turin]   Add Type of Luggage   to LuggageAlLlowance x dx
    [WG Turin]   Add FromMode and ToMode to Interchanging x dx

    [WG Turin-pl] Add UserType to UserProfile so dog etc can be specified x dx
    [WG Turin-pl] Add Maximum Number of Trips  to Step Limit x dx
    [WG Turin-pl] Refine GroupTicketUser to be  CompanionOrGroupMember and allow for UserPRofile as well as GroupTicket x dx
    [WG Turin]   Add GroupTicketing to CompanionOrGroupMember x dx 
  
      2013.07.10 0.99.5 WIP 2
            [Fx] Add email to fulfilment method
     2013.07.10 0.99.5 WIP 1
            [WG Maribor] Move SpecificParameterAssignment to  SalesTransaction Package x dx.
            [WG Maribor] Add PricingService to Fare Calculation Parameters.  Add DynamicPrice to FarePrice  x dx
            [WG Maribor] Add EntitlementProduct x dx.
            [Fx] Add Sales PackageSubstitution to diagrams dx.
            [Fx] Reorder DistanceMatrixElement attributes and align diagram and xml  x dx. MDLCHG
         
            [B3 Fx] Add TypeOfFacilityRef to ServiceFacilitySet x dx.
            [B3 Fx] Add minimumStayType to MinimumStay. x dx.
            [B3 fx] Add mandatoryProduct to distributionAssignment x dx.   
            [B3] Add AfterEndOfValidityPeriod to Refunding BeforeWhen enumeration x dx.
            [B3} Add MediaType and MachineReadable enums to TypeOfTravelDocument x dx.
    [B3] Add GroupDiscountBasis to allow different types of discount. MDLCHG
            [B3] Allow alternative names of TypeOfConcession x dx.
            [B3] Add QuotaFareFactor  for AvailablePrices x dx.
            [B3] Add tour operator to channel type.
            
            [Fx] Correct constraints on FareZone and ResponsibilityAssignment. x. MDLCHG
            [Fx] Correct type on AccessNumber, Limited Access number  x dx. MDLCHG
            [Fx] Move ValidableElementRef to FareElementInSequnce leaf nodes x.
            [Fx] Add GroupOfLinesRef to RoutingCOnstraintZone x dx.
            [Fx] Correct NoticAssignment to reference PointInPattern for From to Points.  x. MDLCHG
            [Fx] Drop Via on AccessRightAssignment - use series pattern instead dx. MDLCHG
            [Fx] Correct Flexible line to reuse NoticeAssignment from line x dx.MDLCHG
            [Fx} Reorder some parameters on fare model elements to increase consistency   x. MDLCHG
            [Fx] Add TypeOfUsageParameter x dx.
            [Fx] Add XML for Controllable element with price x.
            [fx] Add priceable element as abstract superclass of  FareProduct Etc x dx. MDLCHG
            [Fx] Factor out GroupTicketUser from GroupTicket x. dx. MDLCHG
            [Fx] Add TypeOfFareProduct x dx.
     
            [Fx Remodularise] Split FareStructurePackage into smaller files and linearise dependencies x. dx. MODULARISE
            [Fx Remodularise] Move FareElement in Sequence and FareStructure Factor  to separate FareStructure model package x dx.        [Fx Remodularise] Add SalesTransactionFrame to hold other SalesTransaction elements x. dx. 
            [Fx Remodularise] Merge FareDemandFactor model with Quality Structure Model dx.
            [Fx Remodularise] Rename FareDistributionPackage to SalesDistribution Package. dx.
            [Fx Remodularise] Move NoticeAssignment to resuable components. dx.
    2013.06.07 0.99.4 WIP 3
            [WG Maribor] Revise Fare query - Add Commercial Profile, corrections dx            
            [WG Maribor] Rename DistributionCondition to DistributionAssignment x dx. df
            [WG Maribor] Correction: add missing GenericParameterAssignment and SpecificParameterAssignment x.
            [WG Maribor] Update examples to use GenericParamaterAssignment xm 

            [WG Maribor] Add EntitlementGiven  and  EntitlementUsed   Usage parameters, including minimum qualification  period x dx. df
            [WG Maribor] Revise Fare queries. Separate RepeatedFareQuery, Transaction for results, allow Logical display on StopDeparture.
            [WG Maribor] Add distance based cappping x dx.
            [WG Maribor] Add OrganisationRef (ANd so Address and ContactDetails) to Distribution Channel. 
            
         [Tfl] Add FulfilmentPrice ,  QualityFactorPrice.  x dx.
            [Tfl] Add Distribution ChannelRef to  AccessRightParameterAssignment x dx. 
            [Tfl] Add postal to DistributionChannel enum types x dx.
            [Tfl] Add GroupOfDistributionChannels x dx.
            [Tfl] Allow SalesPackage to refine a sales package. x. ??
            [Tfl] Add Payment methods to distribution Channel  x dx.            
            [Tfl] Add Proof required to UserProfile x dx.
            [Tfl] Add requires email to distribution channel x dx.
            [Tfl] Add renewals to ticketing service facilities x dx.
            [Tfl] Add PaymentMethod and TicketingServiceList to DistributionAssignment x dx.
            [Tfl] Add MobileApp on device to fulfilment method  x dx.
            [Tfl] Add IsPersonal to fare condition x dx            
            [Tfl] Rename ContactlessCreditCard ContactlessPaymentCard x dx. MDLCHG       
            [Tfl] Add ChildUserProfileRef to GroupTicket x dx.
            [Tfl] Add Purchase when to PurchaseWindow DayOfTravel, adnacOnly, AdvanceAndDayOfTravel, timeOfTravel x dx.
            [Tfl] add photo and userid to customer x dx.
            
            [Fx] Add gender to Customer x dx.
            [Fx] Add Specified start date to UsageTrigger enum  x dx.
            [Fx] Add  min max height to user profile, reorder elements x dx.  MDLCHG
            [Fx] Add name uniqueness constraints for fulfilmentmethod, DistributionChannel, DIstributionAsssignment, Cell x. MDLCHG
            [Fx] Add NameOfClass to Geographical unit. x dx.
            [Fx] Add missing unqiueness constraints for GroupOfDistanceMatrix elements x dx.
            [Fx] Add FareDayTypeRef to FareFrame x dx.
            [Fx] Add Description to FareStructure Factor x dx.
            [Fx] Add DistanceMatrixElements  as first class Fare elements x dx.
            [Fx] Add ToSeatClass to Exchanging for upgrades x dx.
            [Fx] Add membership card to prrof required
         Remodularize / Restructure
            [Fx Remodularise:] Move TravelSpecification and SalesTransaction to a separate Package.  x dx.
            [Fx Remodularise:] Code up XML for Contract Events x.
            [Fx Remodularise:] Move FareDay to FareCalculation parameters x dx. 
            [Fx Remodularise:] Revise FareTable / Cell structure to separate price and cell x dx. MDLCHG
            
            
    2013.06.01 0.99.3 Minor changes 

	[Ex] Add trainhotel  example xm
	[Ex] AMinor corrections / oversights

    
    [B3] Add FareClass to Class of Use,  so that can be cross collated x. dx.
    [B3] Add ClassOfUse and Name  to Accommodation x. dx.
    [B3] AAdd  sameSex  of GenderLimitation x. dx.
    [B3] Add Drinks to Meal  facility  Correct to point to single enum Use list for list x dx.
    [B3] Add NoticeAssignments to Usage Parameters and FareStructureElement, FareFrame and Tariff x dx.
    [B3] Add ReturnTrip only to ConditionSummary. x dx.
    [B3] Add  refund and exchange enum values to DistributionRights   x dx.
    
    [Fx] Add Description  element to version frame  x.  dx.
    [Fx] Add Description to DistributionAssignment x. dx.
    [Fx] Add  Add order to NoticeAssignment  x dx.
    [Fx] Allow TypeofAcesssRightAssignment on GroupOfAcesssRightAssignments x dx.
    [Fx] Add PrivateCode to FareProduct, SalesPackage , Tariff , reorder dynamic pricing, x dx.
    [Fx] Correction: Couchette Facility correct type   add site double couchette x dx. 
    [Fx] Correction: FareProduct should  use Notice assignment, not Notice x.
    [Fx] Correction: Add missing constraints for  interval price refs , FareDeamndType x.
    [Fx] Correction  correct camle case on IsAuthorised on RoundTrip  and  AtSTop x.
    [Fx] Correction Allow SalesPackageRef on SalesPackagePrice x.
    [Fx] Correction Allow NoticeAssignment in line in sales package,  also to FareFrame x.
    [Fx] COrrection allow  DistributionAssignment in FareFrame x.
    [Fx] Correction:   Move IsAllowed to common Fare Price element dx x.
    [Fx] Correction:   DistanceMatrixElementPrice  is a DiscuntablePrice x.
    [Fx] Correction Add TypeOfFareProduct to FareProduct x dx.

            Functional:
	[FN] Add IsRequired to RoundTrip dx.
	[FN] Add mustReserveWholecompartment to Reserving Usage Parameter  x dx
	[FN] Add list Points to Distribution channel Exchanging/Refunding  x dx.
	[FN] On FareProduct rename FareProductRef to SupplementToFareProductRef x dx.
	[FN] Add base FareProductRef so that product can be based on another x dx.
	[FN] Add  restricted toChannel  to DistributionAssignment x dx.

             
   2013.04.08
            Add validable elementref to FareStuctureElement   x ti do dx 
           [Tfl} Add TariffZone to network to allow (Shoudl really move TZ to ND package?)
             [Tfl] Add CollectByDate  User parameter to capping to allow rebate
           
            [RJIS] Add MinHolders. MaxPersondsInicount  to GroupTicket x dx
            [Tfl ] Add FareDemandType, StartTimeAtStation x dx.
            [TfL] Add CappedUsageRight x dx.
          
            [Tfl] Add Operator to Line section x dx.
            [Tfl] Add FareSection + directions to access ath assignment x dx.
            [Tfl] Add FareZone  to allow sections in tariff zonesx dx.
            [Tfl} Allow properties on LinseSectionMember x dx.
            [Tfl} Add MonthDaynWhich Age applies to UserProfile x dx.
     
            [Tf;] Add Local resident to UserProfile x dx.
            [TfL] Add BaseProfile   to UserProfile x dx.
            [Fx] Add FareProduct, SalesPackage to SalesTransaction x dx.
            [Fx] Fix Ref subs groups, unique keys for Group of Ops etc x.
            [Fx] Allow NuisancceFacility and Passenger comms on Accomodation, x dx.
            [fx] promote accomodation and onboard stay to be versioned children multiple x dx.
            [Fx] Add MaximumNumberOfNamedTransferees to transferability x dx.
            [fix] Allow multiple l geographical structure factors & time structure factors per    fare structure element x.
            
            [Fx] Add endloop to LineSection enum x dx.
            [Fx] Add FareSections to FareFrame x dx.        
            [Tfl, Tap] Add OperatorRef to Tariff x. dx.
            [SG9 Paris ] Rename FarePoint to FarePointInPattern x. dx.  
            [SG9 Paris ] Add general FareProduct requires/entitles relationship to FareProduct x dx.
            [SG9 Paris ] Rename BackTrip to RoundTrip x. dx.  
             [SG9 Paris ] Allow multiple series per distance Matrix x. dx.  
            [Fx]  Correction: Move DatedSpecialService  to DatedJourney package  x dx.
            [nl Fix]  Add TypeOfResponsibilityRole  x.  dx.
            [nl Fix]  Add Separate arrival/departure ay offset to Passing times  x dx.         
            [nl Fix]  Add Monitoring attribute to Journey  x. dx.
            [nl Fix]  Correction  From and To StopPointRef types on NoticeAssignment to be PointInPattern. x.            
        
   2013.03.27.
            [Tap B1] Revise to make delegation via responsibility set x. dx.
            [Tap B1]  Add Text Font name to presentation Add Presentation to StopPoint x. dx.
            [Tap B3]  Add validityCondition to  equipment x dx.
            [Tap B1,2,3] Add Traces & Deltas to VersionFrame. x dx.
            [Tab 1] Add OperatrRef to FareProduct x dx.
            [Fix Acs] Make WheelchairACcessEquipment and VehicleAccessEquipment types of passenger equient  type and ref from installed. x dx.
            [Fix Acs] Add AssistanceAvailable , Guide dog and WheelchairBoarding to AccessVehicleequipment x dx.
            [Fix Acs] Add  AssistanceAvailablity to AssistanceService x dx            
            [Fix Acs]   Add MobilityNeed as SuitableFor to AccessVehicleEquipment x dx            
            [Tap B2 Code Entity  Add Branding entity to datamanaged object dx dx.
            [Fix Acs] Add AssistanceBooking as a type of LocalService x dx.              
                                        
               
    2013.03.12.
         [Tap B3] Add Rounding parameters to Fare Frame, Discount fare, Sales Package price package new package x dx.
         [Tap B3] Add ALternative names to usage paramter x. dx
         [Tap B3 OFAT] Add ResponsbilityRef to DisctributionScope x. dx.
         [Tap B1] Make BorderPoint a type of TimingPoint x. dx.
         [SG9 Munich]  Rename Charging Method to CHarging Moment x. dx.
    2013.03.05
         [Fix] Correct spelling of connurbation x nx
         [Fix] Correct spelling of EntityLegalOwnership x. nx.
         [Fix] Add additionalTopographicPlaces to SiteGroup x. nx.
         [Fix] VehicleType may include VehicleTypes x. dx.
         [Fix] Vehicle installed ActualEquipmentType x. dx.
         [Fix] Add an overide accessibilityAssesment to Call x dx 
         [Fix[ Replace Seat Class with CLASS OF USE nx. dx.
         [FIX] Correct comment on Longitude x. nx
         [uk] Add mobilityScooter & roadMobilityScooter to mobilityNeed x dx.
         
    2013.03.04
         [Tap B2 Tariff Range ]   Add GroupOFSalesPackages  x dx.
            [Tap B2 Tariff] Add AlternativeNames to SalesPackage x dx.
            [Tap B2 Tariff] Add GroupOfDistanceMatrixElements x dx.
            [Tap B2 Tariff] Add GroupOFSalesPackages  and DistributionChannel & FulfilmentMethod     to FareFrame x dx.
            [Tap B2 Tariff] Add DistributionAssignment   to SalesPackage & GroupOfSales Packages x.  dx.
            [Tap B2 Tariff] Add DistributionChannel x dx.
            [Tap B2 Tariff] Add TrainNumber to access right Assignment x dx.
            [Tap B2 Tariff] Add Group of Timebands to Access Right Assignment x. dx
            [Tap B2 Tariff] Add  Summary to SalesPackageELement and SalesPackagedx x. dx.
            [TAP B2 Sales Conditions] and DistributionScope to SalesPackage x dx
        [TAP B2 After Sales Conditions] Add CappedCell Price x dx.
        [TAP B2 After Sales Conditions] Add Exchanging Usage parameter + attributes  x dx.        
            [Tap B2 Tariff] Add UsageParameters for MinimumStay, Exchangeable and PurchaseWindow  x dx.
        [Tap B2 Price] Add Facility, Accommodation , Night Train  to AccessRightParameterAssignment x dx.
        [Tap B2 Price Train Category] add TypeOfProductCategory to Access Right Assignment x dx.
        [Tap B2 Price] Add IsDirect to SeriesPattern &  AccessRightParameterAssignment x dx.
        [Tap B2 Price] Revise simple validity condition x.nx.
        [Tap B3 add berth level & Gender limitation to Accomodation upper | lower both x. dx.
        [Tap B1 B3] Add DistanceMatrix to AccessRightParameterAssignment x dx.
        2013.02.29
           [FR] Allow NoticeAssignmentRefs on Lines. x dx 
           [FR] Add includes relationship to GroupOfAccessParameterAssignments x dx
           
        2013.02.18 
          [Tap B1, B2 Price ] Add Cell (Combination Price) x dx
          [Tap B1 TCVP-H] Add FareBasis (distance group route) to FareStructureElement x dx
          [TAP B1 TCV-I,H,P] Add FareTablePriceGroup  optimization x dx
          
2013.02.12 Align model with XML
          [FR] Add Group of Assignment parameters and revise model x dx
          [FR] Add Fare Point & Fare section to Fare structure model x dx
          [NL] Add OperatingDays to AvailabilityCOndition x. dx.
          {xx] Add missing elements to Fare Frame. x dx.
                 
        2012.01.24 TAP TSI TCVS
           [Tap TSI B1 TCVS] Add SeriesPattern (for series) x dx.
           zz[Tap TSI B1 TCVS Add notice assignments to DistanceMatrixElement (for series info)
           [Tap TSI B1 TCVS] Add validity conditions to   DistanceMatrixElement x dx
           [Tap TSI B1 TCVS] Add SeriesPattern to Access Right Assignment and Fare Frame x dx.
                
      2013.01.24 TAP TSI TCVO
      [TAP TSI B2 TCVO] Add SupplementProduct  to Product Model  x dx.  
    
     2013.01.20 TAP TSI TCVP
   [Tap TSI B1 TCVP] Add notices to Fare product x dx.
   [Tap TSI B1 TCVP] Add Price Groups to FareProduct x dx.
   [Tap TSI B1 TCVP] Add Alternativee names  es to Fare product  x dx.
   [TAp TSI B1 TCVP] Add Back Trip with IsAuthorised &  ReturnFareIsDOuble x dx
   [Tap TSI B1 TCVP] Factor AlternativeName into separate package and move to RC so it can be reused. x dx.
   [TAP TSI B1 TCVP] Add Alternative names to TARIFF x. dx.
   [TAP TSI B1 TCVP] Add Description & extensible TypeOfTariff to Tariff x dx. 
   [TAP TSI B1 TCVP] Add TypeOfTariff to Tariff to allow for TAP TSI code list b.1.1  x dx.
   [TAP TSI B1 TCVP] Add ReplacesTariffRef to Tariff x dx.
     
2013.01.20 TAP TSI TCVC
   [TAp TSI B1 TCVC] Add ValidityConditions to Organisation  properties x dx
   [TAp TSI B1 TCVC] Add DelegatsToOrganisation to Organisation  properties x dx
   [TAp TSI B1 TCVC] Add CountryName to Address x dx 
   [TAp TSI B1 TCVC] COuntryRef to Operator == domicile Tap.   Add Country as concrete Entity with alt names. x dx
   
2013.01.20 TAP TSI TCVG
   [TAp TSI B1 TCVG] Add  new  routing   package in ND1 )    x dx
   [TAp TSI B1 TCVG] Add FareStopPoint, as  subclass of  ScheduledStopPoint    x dx
   [TAp TSI B1 TCVG] Add AccountingStopPoint  to FareStopPoint  properties x dx
   [TAp TSI B1 TCVG] Add FareStopPointRef to FareStopPoint  properties x   dx.
   [TAp TSI B1 TCVG] Add BorderPointRef  to FareStopPoint  properties x dx.    
   [TAp TSI B1 TCVG] Add NameOnRouting to FareStopPoint  properties x dx.
   [TAp TSI B1 TCVG] Add BorderPoint     (new  routing   package in ND1 )    x  dx.  
   
   [TAp TSI B1] add Constraints for new elements x nx.
   [TAP TSI B1 TCVG] Add CustomsOffice as Financial Facility x dx.
   [Tap Tsi B1 TCVG] Add BaggageCheckInCheck out facility at station x dx.
   
2012.01.07 
   [UK] add buggy and umbrella and passenger cart  to enum for    Accessibility Tools.  x dx 
   [UK] Add Secure to Parking x dx
   [UK] A shoeshiner to SanitaryFacility x dx
   [UK] Add Medical Facility defibrillator & alcohol test x dx
   [UK] Add Parking car service: Facility Facility, Carwash, Oilchange, engineWarming x dx
   [UK] Add Parking User type to Parking Capacity, Parking Tariff x dx.
   [UK] Allow reuse of parking capacity x nx
   [UK] Add van, large van and all passenger vehicles to vehicle types x dx.
   [UK] Add list of vehicle types to parking properties x dx.

        2012.09.03 V099.2  3
   [FR] Correct absolute reference in Infrastructure link file x nx.
   [Fr] Correct FlexibleLine UML to match XSD notes, order of elem.ents stopPlaces, flexiblePlaces  dx. tx.
   [Fr] Change FlexibleLine notice UML to use Notice and allow multiple  dx. tx.
   [Fr] Revise FLexibleService Properties to have CancellationPossible etc x dx tx
   [Fr} COrrect allowed values in flexible network model x. dx. tx.
   [ER] Correct ContactDetail elements to match UML and XSD Fax, Phone Email,Url, and  reorder x. dx. tx.  MODEL CHANGE
           [uk] add mobilityScooter     to mobilityNeed x dx
           
        2012.09.03 V099.2  2
           [FR] Update WSDL files
          [Fr] Add trainTram to Tram submodes   x. dx. tx
          [CH] Clarify use of passingthrough  PointsOnLink to ServiceFrame   x dx 
           [RV] Correct integrity constraints for ValidityCondition ConditionedObjectRef x nx.
           [RV] Rename Namespace to Codespace x dx  tx MODEL CHANGE
           [RV] Add defaut Codespaces to Versionframe  x dx tx    MODEL CHANGE
           [RV] rename SiriLineRef, SiriOperatorRef  etc to ExternalLineRef, etc and make a complex  type x dx  tx.
           [RV] Update definition of AccessEquipment  x dx     
           [RV] Update definition of AssistanceService  x dx     
           [RV] Update definition of CommunicationService  x dx           
           [RV] Update definition of ComplexFeatureProjection x dx   
           [RV] Update definition of ComplaintsService  x dx
           [RV] Update definition of ConnectionEnd  x dx
           [RV] Update definition of Control Centre x dx
           [RV] Update definition of Country x dx               
           [RV] Update definition of CrossingEquipment  x dx   
           [RV] Update definition of CustomerService  x dx           
           [RV] Update definition of CycleStorageEquipment  x dx
           [RV] Update definition of DefaultInterchange x  dx
           [RV] Update definition of DeliveryVariant x   
           [RV] Update definition of DisplayAssignment x  dx
           [RV] Update definition of EntranceEquipment  x dx
           [RV] Update definition of EscalatorEquipment  x dx      
           [RV] Update definition of FlexibleArea  x  d
           [RV] Update definition of FlexibleRoute  x  dx
           [RV] Update definition of HeadingSign  x  dx 
           [RV] Update definition of HeadwayInterval  x  dx            
           [RV] Update definition of HeadwayJourney  x  dx           
           [RV] Update definition of HelpPointEquipment  x dx   
           [RV] Update definition of HireService  x  dx
           [RV] Update definition of JourneyAccounting  x  dx
           [RV] Update definition of JourneyFrequencyGroup  x  dx           
           [RV] Update definition of JourneyHeadway  x dx   
           [RV] Update definition of JourneyPattern x  dx
           [RV] Update definition of JourneyPatternHeadway x  dx            
           [RV] Update definition of JourneyTiming x  dx
           [RV] Update definition of LeftLuggageService  x dx   
           [RV] Update definition of LiftEquipment  x dx
           [RV] Update definition of LinkProjection  x dx
           [RV] Update definition of LostPropertyService  x dx           
           [RV] Update definition of LuggageService  x dx
           [RV] Update definition of LuggageLockerEquipment  x dx
           [RV] Update definition of MeetingPointService  x dx
           [RV] Update definition of MoneyService  x dx           
           [RV] Update definition of NavigationPath  x dx 
           [RV] Update definition of Network  x  
           [RV] Update definition of OtherOrganisation x dx   
           [RV] Update definition of OvertakingPossibility x dx  
           [RV] Update definition of PlaceLightingEquipment  x dx     
           [RV] Update definition of PassengerSafetyEquipment  x dx              
           [RV] Update definition of PointOfInterestClassification  x dx              
           [RV] Update definition of PointOfInterestEntrance  x dx              
           [RV] Update definition of PointOfInterestVehicleEntrance  x dx                           
           [RV] Update definition of PointProjection  x dx    
           [RV] Update definition of QueueingEquipment  x dx   
           [RV] Update definition of RampEquipment  x dx 
           [RV] Update definition of CateringService  x dx     
           [RV] Update definition of RetailService  x dx  
           [RV] Update definition of RoadAddress  x dx       
           [RV] Update definition of RoughSurface  x dx    
           [RV] Update definition of RubbishDisposalEquipment  x dx    
           [RV] Update definition of SanitaryEquipment  x dx    
           [RV] Update definition of SeatingEquipment  x dx    
           [RV] Update definition of ShelterEquipment  x dx 
           [RV] Update definition of SignEquipment  x dx       
           [RV] Update definition of StairEquipment  x dx    
           [RV] Update definition of StaircaseEquipment  x dx             
           [RV] Update definition of StairFlight  x dx       
           [RV] Update definition of StopAssignment  x dx                  
           [RV] Update definition of MoneyService  x dx           
           [RV] Update definition of TemplateVehicleJourney  x dx  
           [RV] Update definition of TicketingEquipment  x dx   
           [RV] Update definition of TicketingService  x dx
           [RV] Update definition of TicketingValidatorEquipment  x dx
           [RV] Update definition of TransferRestriction  x dx    
           [RV] Update definition of Travelator  x dx           
           [RV] Update definition of TrolleyStandEquipment  x dx                         
           [RV] Update definition of TypeOfEqipment  x dx    
           [RV] Update definition of TypeOfHandrail  x dx                  
           [RV] Update definition of TypeOfPaymentMethod  x dx              
           [RV] Update definition of TypeOfStopPlace  x dx                
           [RV] Update definition of TypeOfTransfer  x dx    
           [RV] Update definition of TypeOfValidity  x dx  
           [RV] Update definition of UserNeed  x dx  
           [RV] Update definition of VehicleAccessEquipment  x dx  
           [RV] Update definition of VehicleChargingEquipment  x dx                       
           [RV] Update definition of VehicleEntrance  x dx    
           [RV] Update definition of VehicleJourneyHeadway  x dx    
           [RV] Update definition of Via x dx    
           [RV] Update definition of WaitingRoomEquipment  x dx               
           [RV] Update definition of WheelchairVehicleEquipment  x dx    
           [RV] Update definition of ZoneProjection  x dx  
           
           [TIDY] Rename JourneyTimingsModel to JourneyTimingModel 
           [MTG] Make  ControlCentre a type of Organisation Part  x dx tx,    MODEL CHANGE
           [MTG] Add a Type of Time Demand Type  x dx tx,   
           [RV] Rename OtherSign to GeneralSign x dx  tx     MODEL CHANGE
           [RV] Rename StopPlaceEquipment to SiteEquipment  x dx  tx   
    [RV] Add a GeneralOrganisation & make Other Organisation abstract x dx tx.
    [RV] Add LineRef   DirectionRef DestinationDIsplayRef to HeadignSign x  dx tx
    [RV] Add ClassOfUsSeRef to WaitingRoomEequipment x tx
    [RV] Add SuitableforCycles to Ramp, Lift, Entrance. Crossing, tx
    [RV] Rename StopPlaceSign to PlaceSIgn x dx tx
    [RV] Correct constraints on OverTakingPossibility and Network Restriction x
    [RV] Add RelativePosition to TrainStopAssignment x dx.
    [RV] Correct type of Vehicle Stopping position x
    [RV] Correct types on DataSourceRef x 
    [RV] Allow Topic data source to be ref 
    [Rv] SImplify FrmaeRequestFilter by dropping AbstarctObejctRequestFilter  x
       2012.08.01 V099.2   1 
  [CH] Add SiriLineRef and SiriDirection ref to InterchangeRuleLineFilter x. dx.
  [CH Add Integrity constraints for ControlCentre and TypeOfJourneyPattern x.
  [CH] Add ControlCentre to ResourceFrame  x dx tx,
  [CH] Updated VDV example, revised for latest schema. x
  [UK] Revise and  correct Parking attributes, add Bay  dimensions and power points x dx.
  [FX] Correct Projection/PointOnLink implementation to be a ref not containment, allow by distance ref too x dx
          Note that POINT ON LINk can aslo be  defined as part of a LINK.
  [FX] Revise and simplify dependencies. 
    Modularisation move JourneyTimings from VehicleJourney to JourneyTiming package
     [RV] Correct VehicleEntry comments   x dx
        Correct model for journey daytypes  1:* dx
        Add default sense of Restricted to InfrastructureFrame x tx.
        Correct comments in model  dx
        Correct Dead run diagram. dx
     [RV] Rename TimingPointType to TypingPointStatus  x. tx
     [RV] Add parent to parking capacity x. 
     [RV] Add reverse direction to xml x. tx
     
   20120.07.22 V099.1 6
     [Schaffhausen] Interchange Rule Rename NextStopPoint etc to Adjacent Stop Point x dx tx. MODEL CHANGE
     [Schaffhausen]  Add number to Course of Journeys x dx tx
     [Schaffhausen] Correct some public facing strings to be Multilingual x dx
     [Schaffhausen] Correct comments on Offset to be relative to Start of journey x dx tx
     [Schaffhausen] Add PointNumber to PointGroup  x dx   tx
   
   2012.06.18  v0.99,1  
        [Schaffhausen] Rename NetworkRestriction possible to Restricted x dx MODEL CHANGE
        [Schaffhausen] Revise OvertakingPossibility, MeetingRestriction and Manouevre; allo multimodal combinations and drop Road/Wire/Railway variants 
                            Revise OvertakingPossibility to have overtaking /overtaken VehicleRef         x dx. MODEL CHANGE
                            Rename Manouevre to RestrictedManoeuvre x dx   MODEL CHANGE
        [Schaffhausen] Add request button to help equipment.  x dx 
        [Schaffhausen] Allow default mode and operator on network x dx
        [Other] Correct HelpPointEquipoment in UML model.  x dx MODEL CHANGE
         [Schaffhausen] Correct HelpPointEquipment in model.  x dx
        [VDV]          Add ActivationPointNumber to ActivationPoin  x dx.
        [VDV] Add Privatecode to CourseOfJourney x dx.
        [VDV] Add Real-time alias  codes x
        ScheduledStopPoint  SiriStopCode x tx
       Operator  SiriOrganisationCode  x tx
       Line SiriLineCode x   SiriProductCategoryCode x tx
       Direction SiriDirectionCode x tx
       Connection SiriConnectionCode x tx
       ProductCategory SiriProductCategoryCode x
       VehicleJourney  SiriJourneyCode x tx
       DatedVehicleJourney  SiriDatedVehicleJourneyCode x tx
       InterchangeRule SiriInterchangeCode x
     
        [Init] Make TimeZoneOffset fractional x dx.. tx
        [SE] Make DayOffset relative to start of journey.  x dx. tx.
       [ Other] Add missing TypeOFProductCategory element  x   tx
       [Other] Add SuitabletoCycle to Ramp, x dx tx Entrance x dx tx, Lift x dx tx
    
 2012.03.17  v0.99,1 (5)
    Add  partial value for LimitationStatus  [RATP] x dx tx
     Change to use SIRI 2.0
  
    
    
   2012.03.17  v0.99,1 (4)
 
  - Tidy
  Delete phys relationship 
 Rename IdType to Ref in UML diagrams x dx tx.
 -  Paris 
 Rename OtherSign to GeneralSign x dx tx
 Add a GeneralOrganisation & Make other Oganisation abstract x dx tx
 Add GeneralZone x dx tx.
 Add FareClass to RequiredCapacity and vehicle Passenger  Capacity x dx tx  
 Make Passenge Capacity first class object x dx tx MODEL CHANGE
 - Examples
 Improve flexible stop assignment
  
 
  - Corrections
   Revise  attributes on StopAssignment
   Add Name, ServiceJourneyInterchange Move order of ScheduledStopPoint  x dx MODEL CHANGE
   Add missing NavigationPathAssignment
   Make FlexibleService properties a DataManagedObject so can be reused x dx tx
   Add FlexibleServiceProperties, FlexibleLinkProperties & FlexiblePointProperties to Timetable frame x dx tx 
   Rename FlexibleLinkProperties to Property   x dx MODEL CHANGE
   Add flexiblePointProperties to call x   tx   
   Add reverseMembers to LineSection  x  dx tx
   Add JourneyAccountings to timetable frame x dx tx
   Rename serviceFacilityLists serviceFacilitySets   x dx MODEL CHANGE
   VehicelJourneyHeadway shoudl reference TimingPointInPattern, not timingPoint x tx modelchange
   Move PRivateCode to StopAssignment from PassengerStopAssignment x dx
   Add runtime tp OnwardLink view x tx
   Rename notices to noticeAssignments where relevant x dx MODEL CHANGE
   Correct DatedPassingTime to have DatedJourneyRef x dx
   Correct Model for PassignTtime to use DayOffset dx tx  
   Add missing ControlCentreNotifyThreshold to xml x dx tx
   Change order of Description on JourneyPart x dx MODEL CHANGE
   Add CoupledJourney to Timetable frame x dx tx
   Make TrainBlock a type of Block x dx 
   Add VehicleServceParRef to block x dx tx
   Add CompoundBlockRef to BlockPart x tx
   In CompoundBlock Rename FromPoint & ToPoint to StartPointRef & EndPointRef x dx tx MODEL CHANGE
   For Schematic Map  Change Number of Pixels int to GraphicsUnits float 
   Rename orgisationTypes to typesOfOrganisation  c dx MODEL CHANGE 
   Add length  of access area to WheelchairAccessEquipment  x dx 
   Revise ServceiFacility & SiteFacility order of facilities (Catering, etc)  x dx MODEL CHANGE
   Rename TypeOfAccesibilityTool to ACcessibilityTool x dx
   Revise  FacilitySet to be mroe uniform: allow type of equipment as "other facilitry". x dx MODEL CHANGE
  
 
        - SIRI 
 Make COntrol Centre a Type of ORGANISATIONAL UNIT to match SIRI definition  x dx cx TODO
 
 
 
  2012.01.16  v0.98,9

  - CD Turin: 
  Pathlink; Add Back heading as well as Towards heading x dx.
 Add DriverRef x dx
 Add Control Centre with attributes to TransportOrganisationPackage  (DropControlCentreSupport file)  x dx. CX
 Merge UIC ValidityCondition Daybits into Availability Codition x
 Allow TariffZones in SiteFrame x dx
 - KB Model comparison correcytions
 Drop  Monitored Vehicle Journey from Part2  (Move to separate MonitoredJourney package for future use) x dx
 Drop Estimated & Observed Passing times from Part 2 (Move to separate MonitoredJourney package for future use) x dx
 Make Interchange/ Priority an attribute dx.
 Move ParkingTariff to separate package in part3, Also move to fare frame  x dx MODEL CHANGE
 Rename FootnoteAssignment to NoticeAssignment x dx  CX
 Rename DefaultTransfer to  DefaultConnection  x dx MODEL CHANGE CX
 Rename AccessRighstModel to  FareRelatedRestriction x dx 
 Add TimeDemandType to Interchange Rule  parameter  x dx
 Rename AccessibilityTool to TypeOfAccessibility Tool x dx
 Split TicketingFacility into TicketingService + TicketingFacility x dx  CX
         -  NK xsd /doc Corrections of  Errors and ommisions nk
   Correction : DatedJourney & Journey are types of Journey_ 
  Revise xsd dependencies to be more specific, correct _support only dependencies x
 Correct PARKING: Add enhancements to Areas, x dx MODEL CHANGE
 Rename Refreshments  to Catering  x dx MODEL CHANGE 
       Change Cardinality of  of extensions to be many  x 
         Correct names of local service (equipment) and local service (package) x
         Add meeting point Equipment to xsd x CX   
         Add pointonRouteRef to flexiblePointProperties x 
         Add notices, DestinationDisplayRef and vias to  PointIn Pattern x dx
   Add runTimes to TimingLinkInJourneyPattern x.
   Make ServiceJourneyPattern a Type of JourneyPattern x.
   Align ServicePatternProperties with JourneyPattern  x.
   Move PrivateCode to LinkSequence (from Route, ServcePattern  x dx MODEL CHANGE
   Rename StopPointInJourneyPattern / notices to noticeAssignments  x dx MODEL CHANGE
   Align diagrams to show GroupOfTimingLinks as part of TimingPattern model, not TimeDemand Model  dx
   Add GeneralFrame example  ex
   Add Entity_Entity example .ex
   Allow Enity_Entity in GeneralFrame x dx  CX
   Add TypeOfValidity x. CX
   Add Organisational Unit & Revise OrganisationPart & Dept x dx CX
   Add TypeOfOrganisatrionalPart  x dx    CX
   Add missing attributes to OrganisationalPArt
   Add TypeOfEntity  x dx  CX
   Add OrganisationRef to OrganisationPart x
   Revise ClassRef to be consistent with Ref x
   Add TransportAdministrativeZone with modes  x   dx CX
Add TypeOFLinkSequence GroupOfLinkSequences x CX
Correct LinkInLinkSequence x
Simplify LimitationsStatus x
Move Place,   from ifopt to framework  model x
Move   Accesibility from resuable components to framework  model x
Change order of PriamryMode on Opeartor x dx MODEL CHANGE
Move equipmentPlace, topographicPlace from ifoptto resuable components x dx
Add  TypeOfEquipment   x CX
Add missing constraints for Equipment, LocalService and added entities,  x
Correct id constraint on ResponsibilitySet x 
Add more integrity constraints for Equipment, etc x
 
   - CD  NEPTUNE 
   Add AccessibilityAssesment to Line x dx
         Allow equipment places on site as well as site components x dx
         Allow InverseRef on Route x dx
         Add GeneraGroupOfEntites concrete x dx  CX
   - GD VDV
   Add PrivateCode to TypeOfValue x dx doc
   IntrerchangeRuleTiming corrected to add Timings x dx 
 
 2011.12.10  v0.98,8.
       - Consistency
          - rename TypeOfNavigation to NavigationType x dx MODEL CHANGE  CX
         - rename NavigationPath/  features to NavigationPath/  summaries x dx MODEL CHANGE
         - Corrections to  comments for spelling and grammar
         - Correct type on EntranceRef x
         - Add ServiceSite x dx CX
       - Revise spelling and punctuation on comments
       - Correction:  change order of Block Prep and finish duration  x dx MODEL CHANGE
       
       - UB mapping 
         - V1
 - 1.#48 Add Place Ref to ServiceJourney Origin [ub]  x   
 - 1.#74 Change KeyList to lower case keyList [ub] x   MODEL CHANGE
 - 1.#73 Add ViaType to Via: StopPoint or name [ub] x dx. 
 - 1.#101  Add Service requirement to Call to allow for change [ub] x dx 
 - 2.#15,#16 Add Service CalenderRef to VehicleScheduleFrame [ub] x dx. 
 - 2.#16 Add Service CalenderRef to VehicleScheduleFrame [ub] x dx. 
 - 2.#30, #37 Add Vvalidity Conditions to Block [ub] x dx. 
 - 2. #33, #35 add explicit Start and end time to Block [ub] x dx. 
 - 2. #47, Add lineRef and Direction to designator [ub] x dx. 
 - 2. #57, add ArrivalDayOffset  [ub] x dx 
 - Update Noptis examples
        - V2
           - 1. #35 Add start day offset from current operating day to Block
           
       - CD /KB
           - Add complex feature projection  [cd]  x  dx.
           - Add Train Block, Train Block Part[cd]  x dx.
           - Correct Cardinality on sources/DataSource  [cd]  1:*  x
           - Add TemplateVehicleJourney to XSD  [cd]  x  
           - Align JourneyDesignator [cd]  dx
           - Add VehicleTypeRef to VehicleTypePreferenceGroup [cd]   x
           - 
        - GD/MK VDV Mapping   
 - Add  <PrivateCode>, <ShortName> and <Name> to OperationalContext. [vdv] x dx 
 - Add <DriverDisplayText> to DestinationDisplay:  [vdv]  x dx.
 - Add  PrivateCode> to  Notice. [vdv]  x  dx. 
 - Add  PrivateCode> to   ServicePattern:    [vdv] x dx.
 - Add  PrivateCode> to  Route:  [vdv]   x dx.
 - Add <NextStopPlaceRef> to  InterchangeRule  filtesr  [vdv] x dx.
 - AlLlow multiple timings on InterchangeRule   [vdv] x dx..
      
       
        
 2011.11.25  v0.98,7
       - Berlin meeting decisions
       - Submode/OperationalContext
 - Add OperationalContext and use instead of Submode on TimingLink, JouruneyPattern, ServiceLink, ect x dx MODEL CHANGE CX
 - Add OperationalContext to TimeDemandType x dx MODEL CHANGE
 
   - InterchangeRule
 - Add InterChangeRuleTimings to Interchangerule x dx MODEL CHANGE  CX
 - Add validity condition to interchange rule x dx
 - Add operator to InterchangeRule x dx
 - Allow exclusion on rule x dx
 
 - Rename frequencies to headways on TimeDemandType x dx MODEL CHANGE
 - Simplifications
 - Drop use of _entities
 - modify netex_publication to require the  use of a frame 
 - Wrap frame defaults in a wrapper
 - Revise journey designator and allow use on Blocks
 - Correction: allow journeys in Blocks without course of Journeys
 - Fares
   - Correct use of Transferability x dx FARE MODEL CHANGE
   - Add some validable elemenst and access rights to examples
   - Colour for fare demand type DONE x dx
   - Add CombinationPrice and use where there is a multidemnsional price  x dx MODEL CHANGE 
 - Other Changess
   - Rename NetworkTopology to LineNetwork  [kb]  x dx MODEL CHANGE
   - NPTG Add parts add contact details to organisational [uk]  part  
   - Consistency: Rename Responsibility / Description to Responsibility / Name x dx
   - Correction: correct  type on TypeOfOrgansiationRef x
   - Correction to Topological Place  - Add missing  contained  in rel. Add missing structural types x
   - Correction to CoupledJourney add PurposeOfJoourneyPartition  as open value  x dx

    
 2011.11.01  v0.98,6   
     - Revise Fare model
 - Correction Allow multiple Usage parameters Refs on Usage Parameter Price s  FARE  MODEL CHANGE x dx
  -Correction FareStructureElement shouldl reference GeographicalStructureFactro, not GeographicalUnit
  - Correction FareStructure  allow declaraion of  GeographicalStTructureFactors
  - Add draft Travel Document  and Sales Package x dx  CX
  - Add integrity constraints for TimeIntervals
  - Make order of FareStructure components consistent x dx FARE MODEL CHANGE
 - Add more examples
       -Add  Zone fare with separate availability & Sale package
       -Add Sales packages to some examples
       -Add a return fare product  to simple direct fare model
      - Minor techncial corrections  after Teleconference on model issues
   -Equipment  
        Make  PassengerEquipment a type of InstalledEquipment (Rather than  a type of Place Equiopment CX
        - Simplify: Merge Vehicle Equipment and Actual Vehicle Equipment x dx MODEL CHANGE
          - Correction: Rename PasssengerEquipmenetIdType to PassengerEquipmentIdType
          - Modularisation: Move PassengerEquipment to base Equipment package   x dx.
          - Correction physical model : Each equipment position  points to one Equipment only dx. 
          - Simplify: Make Accommodation and BoardingPermission types of Facility
          - Simplify: Merge PassengerInfoEquipment and PiFacility and VehicleInfoEquipment as PassengerInformationEquipment CX
          - Correction: Rename SanitaryFacilityEquipment to SanitaryEquipment x MODEL CHANGE CX
          - Correction Remove duplication SurfaceEnum
          - Add optional RoutePointRef to Via 
        - Facilities 
             - Rename   xxxList  simpleTypes to xxxxListofEnumerations
             - Rename xxxFacilities elements  to xxxFacilityList  x dx  
             - Rename PtInfoFacility to PassengerInformationFacility
             - RenameTypeOfSanityFacility to SanitaryFacilityList
             - RenameTypeOFSanityFacility TicketingServiceType to TicketingServiceList
             - Rename LuggageServiceType to LuggageServiceFacilutyList
             - RenameAssistanceServiceTyupe to AssistanceFacilityList
             - Add SafetyFacility List  
          - Revise TimeDemandTimings
           - reanme TimeDemandTiming to JourneyTiming 
           - Rename TimeDemandTiming to JourneyTiming x dx MODEL CHANGE
           - Rename TimeDemandRunTime to JourneyRunTime x dx MODEL CHANGE
           - Rename TimeDemandWaitTime to JourneyWaitTime x dx MODEL CHANGE
           - Rename TimeDemandLayover to JourneyLayover x dx MODEL CHANGE
           - Rename TimeDemandHeadwayInterval to JourneyHeadwayInterval x dx MODEL CHANGE
             - Allow TimeBandRef on JourneyTiming x dx
             - Add timedemandtype to TImingdemandProfile xdx
             - Allow TimebandRef as alternative to TimeDemandtypeREf on Call, JourneyPattern etc x dx
             - Move vehicle typePreference from VehicelJourneyTimesPackage to  to JourneyTimesPackage
             
      -  Correction move VehicleTypePreference to JourneyPattarenTiming pacakge
          -Rename Footnotepackage  to NoticePackage  x dx 
      -  Move turnaroundtimelimit to  JoruneyPattern  timings x dx  
        -  CorrectionUse VehicleMode where  relevant 
        _ add equipment ref to check constraint
     
      Changes to Align models from Kb spreadshee
          - JourneyHeadways
          - Allow wait times on Timing point in pattern x dx.
          - Renanme JourneyHeadwayInterval to JourneyHeadway x dx.
          - Correction: Add JourneyPatternHeadway to JourneyPattern x dx.
          - Correction rename headwayIdType to JourneyHeadwayIdType x  .
    - Correction: Add headways to TimingPoints  x dx.
          - TimeDemandTypes
              - Align: Move TimeDemandTyupe package to Part 1 TP  x dx.
              - Align  MoveVehiclePreference to  TimeDemandPackage x dx.
              - Move JourneyTiming to TimeDemandPackage x dx.
              -  Rename JourneyTiming to JourneyDemand x dx.  CX
          - Equipment
              StopPlaceEquipment  diagramRenamed SiteEquipment  dx
          - InterchangeRule   
        - Move Interchange and InterchangeRule support to part2 JourneyTimes package s
             - Rename InterchangeRuleFiler to InterchangeRuleParameter x dx MODEL CHANGE
             - Make InterchangeRule a type of Interchange, refactor attributes x dx MODEL CHANGE
     
     Tidy ups
          Correction allow network to  ref an authrity and a grousp of lines   x 
          Correction Allow NetworkTopology to refercnhe a group of lines  x dx MODEL CHANGE 
          Correction RoutingConstraintsall  ref to  refPointstInPatternbe associated with garage 
          Ccorrection allow crewbases to ref garages x
          Correct type of StopAReaRef x
          Correction add Access ZOne  x
          
 2011.09.16  v0.98,5   
 - Correction Rename WaitPoint PointInJourneyPattern to IsWaitPoint to avoid ambiguity 
 - Correction add referential integrity check forClassOfUSe etc x
 - Correctionn add integrity  constraints to check  PointInPatternRefs
   - Add draft Fare Schema  x dx
       -Add Fare Frame  
         - Add draft fare elements
          - Add fare examples
  - Add CurrencyType to Framex dx     
        - Add not working day
        - Add GroupOfTimebands to enable fares   
   
 
 - Simplification/ Correction to PointsInJourneyPattern: 
        - Make StopPointInJourneyPattern a type of TimingPointInJourneyPattern a type of PointInJourneyPattern     x.dx    
 - Rename LinkInServicePattern  to ServiceLinkInServicePattern, TimingLinkInJourneyPattern  MODEL CHHNGE  x
 - Rename LinkInServicePattern/LinkRef to  ServiceLinkRef, TimingLinkRef MODEL  CHANGE  x
 - Drop Stop point attributes from PointInJourneyPattern, make StTopPoint in JourneyPattern & JTImingPointInJourneypattern more consistent MODEL  CHANGEx
    
 2011.09.16  v0.98,4
 - Allow vias on Destination Display. Wrap Vias as Via element and allow name  x dx **  [ub]   MODEL CHANGE
- Correction rename  StopPlace/ VehicleStoppingPositions, VehicleAlignmentPositions lower camel case   x MODEL CHANGE
- Correction: rename FacilitySet / Available to availabilityConditions x  MODEL CHANGE
- Correction: make topics & policies on request upper camel case - all examples x.
- Correction: Add StopPlaceCompomnent group to StopPlaceEntrance.
- Technical - rename all relations _RelStructure x.
- Add Submode as open type x dx. [vdv /delft]
- Change department ref to SubmodeRef on Line, Route Link, JourneyPattern, ServiceLink, TimedemandTiming , TimingLink , Vehicle Journey   x dx. [vdv /delft]
- Revise Origin Destination on Service Journey to allow name only, and on dead run to allow type x dx.  MODEL CHANGE 
 - Correction - Add integrity  constraint for NextStop on Interchange rule x
 - Add   Day Number to OperatingDay  x @dx. [vdv - delft]
 - Add Bearing to VehicleStoppingPosition, clarify use or bearing x @dx [vdv - delft]
 - Examples :
 add example of feeder / distributor filter on Interchange rule
 add example of Simple flexible service
 add exampke of Hail and ride to Netex_01.4_Bus_SimpleTimetable_WithConnection.xml
 - Add PointRef and PlaceRef to Feeder/Distributor filter  x dx.  [vdv, ub - delft]
 
 - Revise Footnotes /Notices [vdv - delft]
 - Combine Notice & Footnote as Notice  x dx. [delft]
 - Correction - Add noticeAssignmenst to servce frame , revise order to be consistent with tometable frame  x dx MODEL CHANGE
   - Correction - Add referential integrity check for Notice Assignment x
 - Add Driver Display text to Notice  x dx. [delft]
 - Distinguish between Advertised (On assignment) and CanBeAdvertised (on Notice    )  x @dx  [ub]
 - Add PublicCode to Notice x @dx  [vdv - delft]
 - Dependency: Move FootNoteAssignment to from Part2 JT to  Part1 TP 
 - Support Vehicle Loading : [era - delft]
 - Add to StopPlaceType enum : new value of   VehicleRailInterchange, x dx
 - Add to QuayType enum : new value of  VehicleLoadingPlace, x dx
 - Add to BoardingPositionType enum : new value of VehicleLoadingRamp, x dx
 - Add to CheckConstraint Type enum : new value ofvehicle Loading/Unloading to CheckCOnstraint Type 
 - Add VehicleEntrance to SiteModel, with Public attribute.  x dx ** 
 - Add StopPlaceVehicleEntrance, PoiVehicleEntrance, x dx, as typt e of   VehicleEntrance
 - Make existing ParkingVehicleEntrance a type of VehicleEntrance   x dx CX
        - Allow check in times: Add CheckConstraints to ServiceJourney  x dx**  [era - delft] 
- rename Mode value telecabine to cableway as this is more general x dx MODEL CHANGE
- Rename FlexibleService Type enumeratioms mixed, fixed, x. dx. MODEL CHANGE
- Correction add referential integrity check for Flexible Areas etc x
- Add "checkout" value  to  CheckConstraint processes enum  x dx. [ers]
- Add OnboardStay + BoardingPermission enum  to facilitoes  x dx.   [era - delft]
- Add Operator Ref to deadrun x dx [ ub  ]
- Add DeadRunCall    to deadrun x dx [ ub  ] CX
  Add Booking Arrangements: BookingMethod, BookingCOntact, LatestBookingTime, MinimumBookingPeriod, booking notes to Flexible line. x dx. [ub -delft]
 - Add ChangeOfDestinationDisplay to Call etc  [ ub - delft  ]
  - Add ChangeOFServceRequriements  to Call etc  [ ub - delft  ]
- Added Print advertisement to Service Journey & Special Service   x dx. [ ub - delft  ]
- Revise Vehicle Type & Service requirements x dx[  delft  ]
- Add PassengerCarryingRequrementView to ServiceJourney   x dx[ ub - delft  ]
- Correction:  rename PassengerInformationFacilities PassengerInfoFacilities to be consistent x. dx  MODEL CHANGE
- Correction: AccessibilityInfo to  AccessibilityInfoFacilities x. dx  MODEL CHANGE
- Move vehicle passneger equipment from ifopt to Resuable components 
- Correction remove duplicate enum defs for AcecssibilityInfo, PassengerInfo
- Correction : add actualVehicleEquipments to vehicle x. dx,
- Correction : Rename equipment to equipments x. dx  MODEL CHANGE
        - Revise  ValidityTrigger and Validity Rule parameter x. dx  MODEL CHANGE
        - Correction Separate Trigger from rule as COnditions
        - Correction  Make interchange use  validity Condition (was an availability condition)
        - CorrectionMake Parking use  validity Condition (was an availability condition)
        - Add integrity constraints for  ValidityTrigger and Validity Rule parameterx
       
         

 2011.09.06  v0.98,2
   - Further corrections
   - Add explicit inFrame relationships
   - Correction ServiceFrame - de-nest Type of service x MODEL CHANGE
   - Correction make RoutingConstraimntZone a sg of Zone  x
   - Simplification ServiceFrame consolidate notices/footnotes in Frame x MODEL change
  - Correction make all dummy supoertyupe sabstarct x
  - Simplification - SITE frame add separate rel for flexible  x MODEL CHANGE
  - COrrection SITE Frame - add ParkingTarriffs
  - Correction ResourceFrame - Separate out departments, groups of operators x MODEL CHANGE
  - Correction InfrastructureFrame - Change name to activatedEquipment x MODEL CHANGE
    - Correction InfrastructureFrame - Separate out garages, crewbases  x MODEL CHANGE
- Correction: Make PathJunction a point not a   Place x dx MODEL CHANGE
- Correction: various substitution groups
- Add journey acocunting to timetabel defaults x dx [txc]
- Add DayOfYear to Properties of Year,  add RegionalHoliday to HolidayTypes   [x dx txc
- Example:Add new  example of cancellation / extra journey 
- Example: Add  holiday day types example to Bus_SimpleTimetable_withtimings. e
- Example: Add serviced organisation term  holiday day types example to Bus_SimpleTimetable_withConnection. e
- Add classOfuse to check constraint,  sitecomponent x dx  [opl]
- Correction:  add SiteFacilities to SiteFrame x dx  [opk]
- Correction:  add FootnoteAssignments  to TimetableFrame x dx  [opk]
- Correction - Allow ServiceJourneyInterchanges to be associated with Calls. Update examples  x dx.

2011.07.17  v0.98,2
   - Further corrections
    -Technical
   - Fix dependencies in journey version   
   - Update  .sprt file for oxygen
   - Restructurue dependencies to make more modula  and rreuse
   - Add a "Netex Lite"  netex_pubvlication_timetable  schema  to reference just  timetable related elements. 
    - Simplifcation: Drop _Class use ref *all or xx_All with XsiType  
    - Assign one to many relationships to containment etc., uniform ref/version for aggregated elements vs strictContai9nment
   - Add TypeOfLine to LINE for OD support  x dx. [osm]
   - Add TypeOfKey attribute to KeyValue x. 
   - Add Submode to Mode TypeOfValue. x.
   - ServiceCalendar file Correct ServiceCalenderFrameRefs to be ServiceCalendarRefs x.
 _ Correction - Add TypeOfJourneyPattern> use this instead of TypeOfService on JourneyPattern x. dx.
 - Correction - drop empty sequence from JourneyPartStructures [cd]
 - Correction - Add  missing TimingAlgorithmType x [cd] 
 - Correction - Drop spurious sequence from  JourneyPartStructure x [cd] 
 - Revise SITE  PublicUse to allow for  all | disabledUsersOnly | authorisedUsersOnly | staffOnly | publicOnly [naptan dft] x. dx. [Model CHANGE]
 - Correction - Rename  InterchangeRuileFilter.ServiceRef  to  InterchangeRuleFilter.ServiceJourneyRef x. dx  [ub]  [Model CHANGE]
  - Correction NetworkRef should be a subst group of GroupOfLinesRef x. [nk]
  - Corrections - various cardinalities eg on Timings should be 1:0 not 1:*  x.
  - Add DestinationViaGroup to PointInJourneyPattern so that can specify at journey pattern level as well as Journey level  x. dx. [ub txc]
  - Modularity:  For PointOn Link allow inline Point as alternative to PointRef x. [ub]
  - Correction - Drop StopAreaRef from Connection end.  mark mode as derived  x. dx. [ub]
  - Add a From & Tto Visit number to Interchange to handle the case of circular journeys with multiple connections at the same stop  x.  dx.  [ub]
  - Correction -  Add Parking elements to end of SITE CONNECTION x.   
  - Correction ServiceCalendarFrameREf is type of VersionFrameRef x.
  - Correction:  correct  Garage GaragePoints containment x.
  - Add Monitored to Line  to indicate if real-time data available   x. dx. [dl]
  - Correction - Equipment ids. x
  - Correction - Comments on Resource farme  ids. x.
  - Add RubbishDisposal to passenger  Equipment x dx [BVW] ** CX
  - Allow UicOperatingPeriods in Service CalendarFrame x dx [sj-uicj]  **
  - Add contact email to DataSource x. dx.  [ub]
  - Add TransportMode to DeadRun (on Journey)  x. dx. [ub]
    - Make DeadRunTypeOptional  x. [ub]
    
     - Add JourneyAccounting Element x dx [ub] txc ** CX
     - Add PublicityChannel to ServiceElement: all, printed, dynamic, none x, dx, [ub]
     - Add PublicityChannel to FootnoteAssignment:  all, printed, dynamic, none x. dx. [ub]
  - ADd KEYLIST to DestinationDisplayView   x. [ub]
  - Add BookingMethod, BookingCOntact, LatestBookingTime, MinimumBookingPeriod to Flexible line. x dx. [ub]
  - Correction: Add FlexibleLineView so FLEXIBLE LINE Line propertie can be shown on service jour.ney x dx. [ub]
   - Allow  list of notes for Booking note,     x dx. MODEL CHANGE x dx [ub]
  - Allow  list of values for BookingMethod     x dx. MODEL CHANGE
  - Add TrainSize requurements to Train x dx [ub]
   - Add   hasLiftOrRamp  requrements to VehicleType x. dx. [ub]
   - Add VehicleType propertie s to service journey x dx [ub]** 
   - Add frame defaultLocale x dx [era] MODEL CHANGE
   - Reservation added to StakeholderRole x. dx. [uic]
   - Add summer timez zone offset to locale x dx [uic]
   - Correction - Revise  SserviceOrganisation etc to match model. Add OrganisationDayType & Reuse servise Calendar  x. dx. [txc]  ++
   
     
   -Add UicAvailabilitryCondition that allows ValidDayBits  x dx [era] 
   - Reservation facilitie sadded for uic 7037 x. dx. [era]
    
  <xsd:enumeration value="reservationsCompulsory"/>
<xsd:enumeration value="reservationsCompulsoryForGroups"/>
<xsd:enumeration value="reservationsCompulsoryForFirstClass"/>
<xsd:enumeration value="reservationsCompulsoryFromOriginStation"/>
<xsd:enumeration value="reservationsRecommended"/>
<xsd:enumeration value="reservationsPossible"/>
<xsd:enumeration value="reservationsPossibleOnlyInFirstClass"/>
<xsd:enumeration value="reservationsPossibleOnlyInSecondClass"/>
<xsd:enumeration value="reservationsPossibleForCertainClasses"/>
<xsd:enumeration value="groupBookingRestricted"/>
<xsd:enumeration value="noGroupsAllowed"/>
<xsd:enumeration value="noReservationsPossible"/>
<xsd:enumeration value="wheelchairOnlyReservations"/>
<xsd:enumeration value="bicycleReservationsCompulsory"/>
<xsd:enumeration value="reservationsSupplementCharged"/>

  
    -Add BookingProcess  uic 7037  x. dx. [era] 
    <xsd:enumeration value="productNotAvailable"/>
    <xsd:enumeration value="productNotBookable"/>
    <xsd:enumeration value="bookableThroughInternationalSystem"/>
    <xsd:enumeration value="bookableThroughNationalSystem"/>
<xsd:enumeration value="bookableManuallly"/>
  
  -Uic Product Characteristic    UIC 7139 Code list x. dx. [era]  
<xsd:enumeration value="allIInclusivePrice"/>
<xsd:enumeration value="eastWestTariff"/>
<xsd:enumeration value="trainWithTcvAndMarketPrice"/>
<xsd:enumeration value="noPublishedTariff"/> 
 
   - Uic Rate Type UIC 5263Code list.</xsd:documentation> x. dx. [era]  
 
<xsd:enumeration value="normal"/>
<xsd:enumeration value="discountInTrain OtherThanTGV"/>
<xsd:enumeration value="specialFare"/>
<xsd:enumeration value="supplement"/>
<xsd:enumeration value="noPublishedTariff"/>
   
     -Add Meal   x. dx. [era] 
<xsd:enumeration value="breakfast"/>
<xsd:enumeration value="lunch"/>
<xsd:enumeration value="dinner"/>
<xsd:enumeration value="snack"/>
     
    `-Add BoardingPermission   x dx [era] 
<xsd:enumeration value="normal"/>
<xsd:enumeration value="boardingPossible2HoursBeforeDeparture"/>
<xsd:enumeration value="alightingPossible2HoursAfterArrival"/> 
<xsd:enumeration value="boardingPossible30MinutesBeforeDeparture"/>
<xsd:enumeration value="alightingPossible30MinutesAfterArrival"/>
`<xsd:enumeration value="overnightStayOnboardAllowed">


-Add FamilyService   x. dx. [era] 
<xsd:enumeration value="none"/>
<xsd:enumeration value="servicesForChildren"/>
<xsd:enumeration value="servicesForArmyFamilies"/>
<xsd:enumeration value="nurseryService"/>
    -Add DaysOfWeek to UicOperatingPeriod  x dx [era] 
      -Allow negative day offset x dx [era] 
  - Add linksequenceProjection to handle LineString etc x dx   [gtfs]    
      

* The physical schema has a DutyStretchModel which is not in the XSD 
2011.07.04  v0.98,1
   - Further VDV enablement changes
   - Add VehicleMode to TimeDemandTiming [vdv] x dx. 
   - Add VehicleMode to ServiceLink [vdv] x dx.
   - Add VehicleRegistrationNumber & OperatorRef  to Vehicle [vdv] x dx. 
   - Add PrivateCode to TimeDemandType, InterchangeRule [vdv] x dx. 
  - Add ControlCentreRef to  , InterchangeRule [vdv] x dx.  
  - Add MaximumTransferTime  to    InterchangeRule , Interchange [vdv] x dx. 
      - Add DayTypeRef  to   Block [vdv] x dx. 
         - TransportMode added as Explicit type of value to allow reflection. However   [vdv] x dx,.  
         - Add TypeOfServceRef to Journey    [vdv] x dx,  
         - Add Announcement Support dep
         -Add NoticeRef to StopPointInPattern, PointInJourneyPattern, [vdv] x dx. 
         -Add TypeOfNotice to footnote package. x dx.  
         - Add Name to Block, InterchangeRule, etc  x dx.
         - Add DepartmentRef to Line and VehicleJourney, TimeDemandTiming and JourneyPattern [vdv] x dx. dep
         - Add FromPointRef and ToPointRef to DeadRun and ServiceJourney  x dx .
    - Add explict StopArea and TariffZone rels to ScheduledStopPoint x .
   
   - Revise timetable  examples
     - Reorganise folder structure so that examples are not children of schema folder
     0.98 /examples/
          /xml/
   - Reorganize in increasing complexity,  basic, with timings etc 
   - Rrevise  branched and simple route examples
    - Add circular route example
    - Add branching route example 2nd variant
    - Add example of use of  Announcement Notices to basic Example with timimngs 
      - Revise use of run times in  examples
         - Add PI Facility example
         - Make Journey Patterns Service Journey Patterns in examples
 - Add examples of Activation points

   - Make relation names more consistent - drop ise of Refs in names
   - rename ServicePattern/journeyPatternRefs to journeyPatterns x   [Model CHANGE]
   - rename Line/routeRefs  tpo Line/routes  x   [Model CHANGE]
  - rename SpatialFeature/PointRefs to SpatialFeature/points x   [Model CHANGE]
   - rename LocalService/TypeOfServiceFeatureRefs to  LocalService/typesOfServiceFeatures x   [Model CHANGE]
    - rename NavigationPath/TransferRefs to NavigationPath/transfers x   [Model CHANGE]
    - rename Site/AdjacentSiteRefs to Site/AdjacentSiteRefs x   [Model CHANGE]
    - rename TopographicPlace/AdjacentPlaceRefs to TopographhicPlace/AdjacentPlaces x   [Model CHANGE]
    - rename FootnoteAssignment/ValidityCOnditionRefs to FootnoteAssignment/ValidityCOnditionRefs x   [Model CHANGE]
    - rename VehicleJourney/TimeDemandTypeRefs to VehicleJourney/TimeDemandTypeRefs x   [Model CHANGE]
   - Correct substitution  hierarchies for Journey, pattern, LinkSequence, LinkInSequence, PointInSequence etc
   - Add destination display  vias, to PointInPattern,  rename displayVias to Vias  x dx.

   - Correct PI facility, add LINE and DIRECTION filters  x dx.
   - For consistency  Change order of description on ServiceJourneyInterchange  x dx. [Model CHANGE]
   - Correct Point on Link not to be abstract.
   - For consistency, Promote Distance to be on LinkSequence - drop from NavigationPath  x dx. [Model CHANGE]
   - Correct JourneyPattern substitutionGroup to JourneyPattern  x
   - Correct to allow RoutePointRef on PointInJourneyPattern as per MODEL  x 
   - Revise Quay assignment on Call to allow separate assignment for arrival and departure. Rename QuayAssignment to QuayAssignmentView x dx. [Model CHANGE]
   - Correct to allow ParkingPoint etc as RoutePoints x
   - Correct name of RunTimeAttribute on DefaultDeadRunTime and DefaultServiceJourneyRunTime x dx. [Model CHANGE]
   - Correct Infrastructure Frame contents to add activation frame elements so that  activation points etc can be populated  x dx.
    
2011.05.22  v0.98
   - Make id and responsibility set ref an attribute
   - Add more constraints:: unique within object type
   - Add short names to VehicleType, Route,  etc   [vdv] x dx
   - Change order of DirectionType on Route x dx [Model CHANGE]
   - Add Variant to Destination Display x dx.
   - Add Notice to Footnote Packege to support arbitrary ANnouncements x dx.
   - Correct Key List  x  [Model CHANGE]
   - revise examples
   - Revise examples to use constraints
   - Add branching route example
   - Revise use of run times in examples

2011.05.22  v0.97
   - Add Oxygen project.xpr
   - Fix strict validation errors x
   - Examples: Add simple vehicleSchedule example with BLOCKS etc x
   - Add Duty & DriverScheduleFrame x (Add to MODEL?)
   - Correct package dependencies x
   - Correct spelling of WheelchairPassable [MODEL CHANGE] x
   - Corrections to facilities to  remove duplicates
   - Add earliest and latest passing time to TIMETABLED PASSING TIME  x dx.
   - Rename TIMETABLED PASSING TIME elements to drop TimetabledPrefix   (MODEL CHANGE) x
   - Revise INTERCHANGE RULE to align model with xml . Add attributes   X dx (MODEL CHANGE)  
   - Add WheelChairVehicleEquipment and AccessVehicleEequipment  to align with UML  x
   - Examples:Add UIC eurostar stations
   - Examples:Add Train makeup to Eurostar  example 
   - Revise  Stop Assignment to use revised Train Componentes
   - Example add Assignment of boardinng positions to train components for Eurostar example 
   - Add capacity to TrainElement x dx
   - Add LineString to LINK SEQUENCE PROJECTION  and allow on to Vehicle Journey to support  Shape of a specific journey g x
   - Revise Block to drop FrameRef. Add journeys refs to CourseOfJouuneys x dx (MODEL CHANGE) 
   - Drop JourneyPatternFrequency [kb] x dx (MODEL CHANGE) 
   - Add FootnoteVariants to Footnote [kb] x dx
   - Correct ServiceFrame contents: x dx (MODEL CHANGE)
   - Drop direct containment of ALlowedLineDirection. 
   - Drop GroupOfLinks, 
   - TimeDemandAssignment  
   - Add   identity constraints
     - Rename identifier of Versioned ChildCid rather than id so that can have different constraints
   - Add  Id to footnote assignmentView x
   - Add Id to AccessSummary  x
   - Add  genericIDentity Constraints  Eid, Id/version   cid/version/ ,  
          Special cases Namespace  xmlns,  Datasource/Id
          
   -  Revise NameSpace element : rename to Namespace, rename id to Xmlns, rename Xmlnsurl x dx (MODEL CHANGE) 
   - Change order of Namespaces in ResourceFrame x (MODEL CHANGE) 
   - Add Data source & versiouins to resoucre frame  x
   - NavigationPath make children VersionChildSTructure x
  - Revise All example to show name  Id types eg nid:Quay:1234
 - Make responsibility role assignment a versioned child x
 - Revise examples to use  names space:objectType:identifier   
     
    - Rename EquipmentTypeRef to TypeOfEquipment
    - Add DataSource
    - Allow displayVias on Call as well as destination display [txc] dx
    - Allow DutyPartRef on Call [txc] x dx
  
  
    - Rename  ModeRef to TransportMode x dx (MODEL CHANGE)
    - Rename EquipmentType to TypeOfEquiment
    - Rename v_vesrioing to _version_version  and _versionAttributes to _versionSupport x

    - Rename ID on ENitity to Eid to allow for separate identity constraints x   (MODEL CHANGE)
    - Add RoutingConstraint Package
    - Add Short Name & Private code to Operating day  [VDV] dx x 
    - Add  Private code to Day Type [VDV gd]   dx x
    - Add Short Name & Private code to Activation Point day  [VDV gd ] dx x 
    - Add Short Name & Private code to Vehicle  [VDVgd ] dx x 
    - Add DefaultResponsibiltySet to Farem dx x
    - Allow list of vals  roles on responsibility role assignment
    - Correct DutyPart too dutyParts

      

2011.03.20  v0.96
   - Add Key List to DataManagedObject   [Paris mtg] 11.03 dx x 
   - Revise Flexible Models & route  dx 
          Replace FlexibleLink with FlexibleRouteProerties
          Replace FlexiblePoint with FlexiblePointProperties
          Move FlexibleServicePackage to Part2
   - Add SystemOfUnits dx x
   - Add submodes [cd] dx x
   - Add variant text to submodes  dx x
   - Change order of some elements  on service journey  (MODEL CHANGE) x 
   - Allow image Uri on footnote assignment dx x
   - add Equipment to ResourceFrame dx x
   - add Vehicle & VehicelType to Resource Frame dx x
   - Allow multiple types on Organisation (MODEL CHANGE) dx x
   - Allow parent on AdministrativeZone dx x
   - Add nightRail & interregional to enable uic/era lists dx x
   - Add connection certainty to distinguish guarantee types dx x  MODEL CHANGE
   - Add baggage connection to baggage service. [era]
   - Move Service Journey Pattern to ServicePatternPAckage dx  [kb]
     - Move Service Journey Pattern from TimetableFrame to ServiceFrame dx  
   - Revise RoutingConstraintModel, 
   Move to TP dx   
   Rename dx    
   - Add a separate ServiceCalendar element that is distinct from the Frame
        Add new ServiceCalender_version package and   dx x (MODEL CHANGE)
   - Add turistica and prefernte seat Fare classes x dx  [era]
   - Update Sanitary facility to match London data x [nk]
   - Correct TypeOfFrame to be concrete x  x [cd]
   - Change Location coordinates to use gml:Pos x  (MODEL CHANGE)  x [cd]
   - Add LineString to Link, Polygon to ZOne  x [cd]
   - Add CD RATP Neptune XML example   x [cd]
   - Add Purpose of grouping to ServiceFrame  x [cd]
   - In ServiceFrame rename groupOfLines to groupsOfLines  x [cd]
   - Correct spelling of OutputDetailList  to OutputDetailList  x [cd]
   - Revise Facility  x dx [era] (MODEL CHANGE)
       - ALign facility values  xml /uml, break value down 
       - Add ServicefacilitySet and  StopFacilitySet to group facilities
       - Allow association of Facility with journey part
 
   - rename Site frame stopPlaces to StopPlace (MODEL CHANGE)
   - ADD COMPOUND TRAIN and revise TRAIN  to be VEHICLE TYPEx dx [Paris mtg] (MODEL CHANGE)
   - Revise Train Splitting & joining  [Paris mtg] (MODEL CHANGE)  x dx
Add example of train splitting and joining based on SJ example 
        Add TRAIN NUMBER also include in TIMETABLE FRAME
        Drop TRAIN BLOCK and add  COMPOUND BLOCK
        Revise VEHCILE TYPE, TRAIN COMPOUND TRAIN

2011.02.08  v0.95
   - Allow both WGS and non WGS coordinates in Location xx
   - Allow multiple day types per Journey (CHG) TODO
   - allow Topographic place on Scheduled stop Point  dx x
   - Correct PublicCode on StopArea to be optional dx x
   - Correct Presentation info links not mandatory, add colour name dx x
   - Add public code to organisation  [e]  dx x
   - Change character set to is0-8859-1   xx x
   - Revise ParentZoneRef to be a versionRef (CHG)  xx x
   - Allow multiple Service Calendars in a frame.(affects examples) (CHG) dx
   - Default For Alighting and ForBoarding to true so that less coding needed. xx
   - Add name to timing pattern link and timime demand timing  dx x
   - Add timetable defaults to TimetableFrame [e]  dx
   - Add FootnoteAssignments to ServiceJourney, and Group of Services [e]  dx
   - Refine Group of Service member to allow properties dx
   - Add Network Topology package [e] dx
   - Add line . network and operator to timetable frame as defaults dx
   - Add IsAvailable to AvailabilityCOndition to allow for exclusions [e] g dx
   - Reorder OperatingDays & DayAssignment on ServiceCalendarFrame (CHG) dx
   - Add Class of user value for use on check constraint delay. Add name to delay. dx  
   - Allow OrganisationType to be list xx
   - Add AtCentre on STopPlace dx
   - Correction to Capitalize isExit, isEntrance, IsCovered on SiteEntrance (CHG) xx
   - Rename Namespace to NameSpace to be consistent xx
   - Revise CountryRef to be consistent(CHG) xx
   - Add type attribute to PrivateCodes and reuse common definition. xx
   - Add BorderCrossing to StopPlace and to RoutePoint [era] dx x
   - Add ServiceCalendarFrame ref to TimetableFrame  [era] dx x
   - Correct Purpose of grouping not to be abstract xx xx x
   - Allow Operating Period Ref on day type assignment [era] dx 
   - Revise service facilities  [era]  TODOxx
   - Change Frames Move  InterchangeRule to separategroup in Service Frame. (CHG) dx
   - Correct to Drop duplicate JourneyPattern reference from Timetable frame (CHG) xx
   - Add Footnotes assignments to an interchange. dx
   - Add url to SCHEDULED STOP POINT gtfs dx
   - Make Service departure time optional gtfs dx
   - Add IsFlexible to call. gtfs dx
   - Add Stop type to scheduled stop Point gtfs dx
   - Add url to LINE gtfs dx
   - Add OPERATOR REf to line gtfs dx
   - Reqvise Journey Frequency to allow timeband to be stated (CHG) gtfs dx
   - Allow reuse of   CheckCOnstraints (ref on entrance)   dx
   - Allow default coordinate system srsname to frame dx
   - Add Value Set to allow grouping of values dx
   - Add Submode to Line & ServiceJourney dx
   - Add primary mode to operator  txc dx
   - Add contact fact number to operator/contact txc dx
   - Add default timingpoint type to SSP txc xx
   - Add alternative Presentation to Line txc dx
   - Add group of services to ServiceJourney txc dx

2011.01.28  v0.94
   - Make explicit Frames Disjoint so that each element is in only one Frame (CHG)
   - Add CompositeFrame and Resource Frame  (Model Change) dx
   - Make DestinationDisplay a DataManagedObject and move to LineRoutePackage (Model & MODEL Change) dx
   - Simplify and clarify use of Derived Views    dx
          Facade: (ServiceJourney, DeadRun, Call ) 
          Derived View: LineView, ShceduledStopPointView, DestinationDisplayView, FootnoteAssignmentView, OperatorView dx
   - Revise CALL to reflect changes.
   - Revise comments to include TM definitions and numerous corrections. xx
   - Rename LevelCode to PublicCode dx
   - Rename TimeDemand to TimeDemandType dx
   - Correct Footnote Deivery Variant type dx
   - Rename Time Demand to TimeDemand Type Type dx
   - Add PI Facility package dx
   - Revise package dependencies dx
   - Validate against XErces xx
   
2011.01.01  v0.93
   - Add Retail equipment etc, tidy up dependenies
   - Move Address to RC package
   - RefFactor Extensions to be on DataManagedObject, Versioned Child
   - Correct Timing types
   - Correct types of organisations
   - Correct responsibility set id  
   - Make PathLink a type of Link, not SIteCOmponent
   - rename NavigationPath/ PlaceRefInSequence to PlaceInSequence
   - Rename TypeOfStopPlace to StopPlaceType
   - Rename TypeOfTopographicPlace to TopographicPlaceType
   - Correct POI elements
   - Numerous label corrections
   - Rename PathLink  FromToUpdown to Transition
   - Add POI classifcatiosn to Site Frame. Add Poi Classification example
   - Rename accessSpaceEntrances to entrances
   - Revise FlexibleQuay, StopPlace to be simple - just Places.
   - Rename folders to match conceptual and physical model
        netex_general\     ==> netex_reusableComponents\
netex_framework\    ==> netex_genericFramework\
netex_core\   ==> netex_framework\
netex_baseTypes\     ==> netex_utility\
netex_entityversion\     ==>netex_responsibility\
netext_ifopt             ==> netex_part_1/part1_ifopt  etc   
2010.12.01  v0.92
   - Revise Frames: Revise frames Separate package, Split networkFrame into  Infrastructure &  Service , Site  
   - Use list for modes , other modes
   - change encoding to iso-8859-1
   - add capacity
   - Add POI component
   - Make PI facility a type of equipment so it can be located
   - Add course of journey and vehicle service
2010.12.01 v0.91
   - Revise Frames: Add General Frame. Make  Network  Timetable frame explicit
   - Revsie filters to allow frame references
   - Rename Timetable to TimetableFrame, NetworkVersionFrame to NetworkFrame
   - Add mode to vehicle Journey
   - Add views to hold derived data
   - Move Address to be Place not Site
   - revise FlexibleStopPlace to be Place, FlexibleQuay to be SiteElemengt etc
   - rename serve_support to be service_PatternSupport
   - Add frames to examples
   - Revise SIteConnection, ConnectionConstraint
   - Add example of VDV calendar  and simple calndar
   - Add coupled journey example
   - add gtds agency, example, revise stops
   - Add validation condition to transfer etc
   
2010.11.01 v0.90
   - Level is no longer a SiteComponent
   - Add separate XXX_entity wrappers, rename structures _VersionStructure, add separate _entity packages
        eg Quay_entity,  Quay
   - Revise Site TopographicRef to be SIte /TopgraphicView
   - Allow equipment at Site level
   - Remove circular dependency from core organisation  to ifopt address: move address to organisation
   - Add OperatingOrganisation to Site
   - Add PrivateCode to Operatro and Equipment
   - Add flights of stairs, stair end contrast and other attributes
   - Revise Access and Transfer to use AccessEnd, Transfer End 
   - Rename Check to CheckConstraint
   - Revise parking model, support parking costs
   - Move Locale to Site (ie not just StopPlace)
   - Revise Access & Transfer to have separate Accend, TransferEnd elements. ALlow mode on end
   - Add draft SiteConnection
   - Add direction to checkConstraint
   - Add JP frequency to Journeypattern  (CON MODEL TODO?)
   - Add a group of timing links 
   - Allow multiple timedemands per vehiceljourney
   - Add timeDemandProfile to UML and XML
   - Rename ifopt_ and abcs to netex_ifopt_ and netex_acbs_
   - Drop time allowance etc
   - Rename ShortTermDayAssignment DayTypeAssignment
   - DrRop
       Route-TurnStation
       ActualStopEequipment etc
       ActualVehicelEquipment etc
       VehicleStoppingPosition etc
       VehicleService - TimeAllowance etc
   Examples
     versionhistory
     stadium
     uic stations (sweden)
     uic timetable   Add uicOOperting period as tempory experiment
     
2010.09.29
   Added Point to point on lInk
   Added TransportOrganisation, Call, ProductionTimetable Production modules
   Added Footnotes
   Add SimpleTimetable Example
   Added examples of SIRI proptocol & publication proitocol
2010.09.18
   Consolidate in single namespace - drop ifopt, acbs namespaces
   Make StopArea, Place subs  of Zone
   Make Plaze / Zone an association , not inheritance
   Rename GroupOfElements  to Group of Entities
   Add TypeOF Service to Journey

2010.08.06http://www.booking.com/searchresults.html?aid=317836;label=251_searchbox_251withdates;sid=e7fda4f0cfe47a98c7b43435f76686fd;checkin_year_month_monthday=2010-09-28;checkout_year_month_monthday=2010-09-30;class_interval=1;landmark=2028;pr_cur_code=GBP;;radius=100;offset=20;rows=20
   Integrate changes from CD
    
2010.06.29  V086
   General
       Revise VehicleTypePackage  to include Vehicle, VehicleEqipmentProfile etc
       Add AccessRighst support Package
       Add SchematicMapPackage
       Add Train Element Package
   IFOPT
       Revise attributes 
       Add more equipment and attributes
   Part 1
       Add Activation Package
       Addd Flexible Route Package
       Add Vehicle And Crew Point Pacakage

2010.05.21  V085
    
    Add detailed examples 
    Tidy up

2010.05.12  V08
    
    Combine Ifopt & Network hierarchy
    Add Wimbledon  example
    Revise Simple Network Example 
    Extension 


2009.12.31    
    rename NetworkFrame back to NetworkVersion
    split grouping and common object

    rename networkVersion to networkframe
2009.12.31 
   remove Siri dependencies
     create separate folder for base & resuabel netex
    create netex modes etc    
    rename versionedObject to entity in frame
    rename networkVersion to networkframe
