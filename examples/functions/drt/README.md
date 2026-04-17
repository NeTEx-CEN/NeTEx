# DRT examples and explanations
We expanded for NeTEx 2.1 DRT in serious manner.

## Updates in NeTEX 2.1
- `FlexibleLine` is folden into `Line`. Be aware that an area-oriented services is also a "line".
- There can now exist multiple `ServiceBookingArrangement` and related stuff in a `mobilityService`.
- There can now be also (multiple) `ServiceBookingArrangement` in a `Line`.
- `BookingNote` is now also an object that can be referenced and translated with `AlternativeText`. **TODO**
- `serviceBookingArrangements` can now accept all other elements to describe the services:
  - `ServiceBookingArrangement`: How to book
  - `ServiceCompetitiveCondition`: What to do and what not
  - `ServiceEligibilityCondition`: Who can use the service.
- The interaction of such serviceBookingArrangements is additive. Eg. all elements are within their group connected by OR. E.g. you are a senior or a child you can use the service. Be aware that this MAY result in the need to split a service to do it.

## Examples 

## Regular line that runs and stops only when there are reservations.

- [XML](./CH_DRT_Line_Based_Reservation.xml)
### Switzerland

### ENTUR

**TODO**
- [ ] I am not happy with some parts in the examples. I don't want split files.


