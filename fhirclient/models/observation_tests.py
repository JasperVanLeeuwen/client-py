#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-02-06.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from . import observation
from .fhirdate import FHIRDate


class ObservationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Observation", js["resourceType"])
        return observation.Observation(js)
    
    def testObservation1(self):
        inst = self.instantiate_from("observation-example-phenotype.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation1(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation1(inst2)
    
    def implObservation1(self, inst):
        self.assertEqual(inst.code.coding[0].code, "79716-7")
        self.assertEqual(inst.code.coding[0].display, "CYP2C9 gene product metabolic activity interpretation")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/observation-geneticsGene")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].code, "2623")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].display, "CYP2C9")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].system, "http://www.genenames.org")
        self.assertEqual(inst.id, "example-phenotype")
        self.assertEqual(inst.issued.date, FHIRDate("2013-04-03T15:30:10+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-04-03T15:30:10+01:00")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueCodeableConcept.coding[0].code, "LA25391-6")
        self.assertEqual(inst.valueCodeableConcept.coding[0].display, "Normal metabolizer")
        self.assertEqual(inst.valueCodeableConcept.coding[0].system, "http://loinc.org")
    
    def testObservation2(self):
        inst = self.instantiate_from("observation-example-head-circumference.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation2(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation2(inst2)
    
    def implObservation2(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "vital-signs")
        self.assertEqual(inst.category[0].coding[0].display, "Vital Signs")
        self.assertEqual(inst.category[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/observation-category")
        self.assertEqual(inst.category[0].text, "Vital Signs")
        self.assertEqual(inst.code.coding[0].code, "9843-4")
        self.assertEqual(inst.code.coding[0].display, "Head Occipital-frontal circumference")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Head Circumference")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("1999-07-02").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "1999-07-02")
        self.assertEqual(inst.id, "head-circumference")
        self.assertEqual(inst.meta.profile[0], "http://hl7.org/fhir/StructureDefinition/vitalsigns")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueQuantity.code, "cm")
        self.assertEqual(inst.valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.valueQuantity.unit, "cm")
        self.assertEqual(inst.valueQuantity.value, 51.2)
    
    def testObservation3(self):
        inst = self.instantiate_from("observation-example-unsat.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation3(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation3(inst2)
    
    def implObservation3(self, inst):
        self.assertEqual(inst.code.coding[0].code, "15074-8")
        self.assertEqual(inst.code.coding[0].display, "Glucose [Moles/volume] in Blood")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.dataAbsentReason.coding[0].code, "125154007")
        self.assertEqual(inst.dataAbsentReason.coding[0].display, "Specimen unsatisfactory for evaluation")
        self.assertEqual(inst.dataAbsentReason.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.effectivePeriod.end.date, FHIRDate("2013-04-05T09:30:10+01:00").date)
        self.assertEqual(inst.effectivePeriod.end.as_json(), "2013-04-05T09:30:10+01:00")
        self.assertEqual(inst.effectivePeriod.start.date, FHIRDate("2013-04-02T09:30:10+01:00").date)
        self.assertEqual(inst.effectivePeriod.start.as_json(), "2013-04-02T09:30:10+01:00")
        self.assertEqual(inst.id, "unsat")
        self.assertEqual(inst.identifier[0].system, "http://www.bmc.nl/zorgportal/identifiers/observations")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "6323")
        self.assertEqual(inst.issued.date, FHIRDate("2013-04-03T15:30:10+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-04-03T15:30:10+01:00")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.note[0].text, "Tube broken in transit and sample leaked")
        self.assertEqual(inst.referenceRange[0].high.code, "mmol/L")
        self.assertEqual(inst.referenceRange[0].high.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.referenceRange[0].high.unit, "mmol/l")
        self.assertEqual(inst.referenceRange[0].high.value, 6.2)
        self.assertEqual(inst.referenceRange[0].low.code, "mmol/L")
        self.assertEqual(inst.referenceRange[0].low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.referenceRange[0].low.unit, "mmol/l")
        self.assertEqual(inst.referenceRange[0].low.value, 3.1)
        self.assertEqual(inst.status, "cancelled")
        self.assertEqual(inst.text.status, "generated")
    
    def testObservation4(self):
        inst = self.instantiate_from("observation-example-glasgow-qa.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation4(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation4(inst2)
    
    def implObservation4(self, inst):
        self.assertEqual(inst.code.coding[0].code, "9269-2")
        self.assertEqual(inst.code.coding[0].display, "Glasgow coma score total")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Glasgow Coma Scale , (GCS)")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2014-12-11T04:44:16Z").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2014-12-11T04:44:16Z")
        self.assertEqual(inst.id, "gcs-qa")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.referenceRange[0].high.code, "{score}")
        self.assertEqual(inst.referenceRange[0].high.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.referenceRange[0].high.value, 8)
        self.assertEqual(inst.referenceRange[0].type.text, "Severe TBI")
        self.assertEqual(inst.referenceRange[1].high.code, "{score}")
        self.assertEqual(inst.referenceRange[1].high.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.referenceRange[1].high.value, 12)
        self.assertEqual(inst.referenceRange[1].low.code, "{score}")
        self.assertEqual(inst.referenceRange[1].low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.referenceRange[1].low.value, 9)
        self.assertEqual(inst.referenceRange[1].type.text, "Moderate TBI")
        self.assertEqual(inst.referenceRange[2].low.code, "{score}")
        self.assertEqual(inst.referenceRange[2].low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.referenceRange[2].low.value, 13)
        self.assertEqual(inst.referenceRange[2].type.text, "Mild TBI")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueQuantity.code, "{score}")
        self.assertEqual(inst.valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.valueQuantity.value, 13)
    
    def testObservation5(self):
        inst = self.instantiate_from("observation-example-haplotype2.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation5(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation5(inst2)
    
    def implObservation5(self, inst):
        self.assertEqual(inst.code.coding[0].code, "55233-1")
        self.assertEqual(inst.code.coding[0].display, "Genetic analysis master panel-- This is the parent OBR for the panel holding all of the associated observations that can be reported with a molecular genetics analysis result.")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/observation-geneticsGene")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].code, "2623")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].display, "CYP2C9")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].system, "http://www.genenames.org")
        self.assertEqual(inst.id, "example-haplotype2")
        self.assertEqual(inst.issued.date, FHIRDate("2013-04-03T15:30:10+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-04-03T15:30:10+01:00")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "unknown")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueCodeableConcept.coding[0].code, "PA16581679")
        self.assertEqual(inst.valueCodeableConcept.coding[0].display, "*4")
        self.assertEqual(inst.valueCodeableConcept.coding[0].system, "http://pharmakb.org")
    
    def testObservation6(self):
        inst = self.instantiate_from("observation-example-bloodgroup.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation6(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation6(inst2)
    
    def implObservation6(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "laboratory")
        self.assertEqual(inst.category[0].coding[0].display, "Laboratory")
        self.assertEqual(inst.category[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/observation-category")
        self.assertEqual(inst.category[0].text, "Laboratory")
        self.assertEqual(inst.code.coding[0].code, "883-9")
        self.assertEqual(inst.code.coding[0].display, "ABO group [Type] in Blood")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Blood Group")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2018-03-11T16:07:54+00:00").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2018-03-11T16:07:54+00:00")
        self.assertEqual(inst.id, "bloodgroup")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueCodeableConcept.coding[0].code, "112144000")
        self.assertEqual(inst.valueCodeableConcept.coding[0].display, "Blood group A (finding)")
        self.assertEqual(inst.valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.valueCodeableConcept.text, "A")
    
    def testObservation7(self):
        inst = self.instantiate_from("observation-example-f205-egfr.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation7(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation7(inst2)
    
    def implObservation7(self, inst):
        self.assertEqual(inst.code.coding[0].code, "33914-3")
        self.assertEqual(inst.code.coding[0].display, "Glomerular filtration rate/1.73 sq M.predicted [Volume Rate/Area] in Serum or Plasma by Creatinine-based formula (MDRD)")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.component[0].code.coding[0].code, "48643-1")
        self.assertEqual(inst.component[0].code.coding[0].display, "Glomerular filtration rate/1.73 sq M predicted among blacks [Volume Rate/?Area] in Serum or Plasma by Creatinine-based formula (MDRD)")
        self.assertEqual(inst.component[0].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.component[0].referenceRange[0].age.low.code, "a")
        self.assertEqual(inst.component[0].referenceRange[0].age.low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.component[0].referenceRange[0].age.low.unit, "yrs")
        self.assertEqual(inst.component[0].referenceRange[0].age.low.value, 18)
        self.assertEqual(inst.component[0].referenceRange[0].appliesTo[0].text, "non-black/african-american")
        self.assertEqual(inst.component[0].referenceRange[0].low.code, "mL/min/{1.73_m2}")
        self.assertEqual(inst.component[0].referenceRange[0].low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.component[0].referenceRange[0].low.unit, "mL/min/1.73m2")
        self.assertEqual(inst.component[0].referenceRange[0].low.value, 60)
        self.assertEqual(inst.component[0].valueQuantity.code, "mL/min/{1.73_m2}")
        self.assertEqual(inst.component[0].valueQuantity.comparator, ">")
        self.assertEqual(inst.component[0].valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.component[0].valueQuantity.unit, "mL/min/1.73m2")
        self.assertEqual(inst.component[0].valueQuantity.value, 60)
        self.assertEqual(inst.component[1].code.coding[0].code, "48642-3")
        self.assertEqual(inst.component[1].code.coding[0].display, "Glomerular filtration rate/1.73 sq M predicted among non-blacks [Volume Rate/Area] in Serum or Plasma by Creatinine-based formula (MDRD)")
        self.assertEqual(inst.component[1].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.component[1].referenceRange[0].age.low.code, "a")
        self.assertEqual(inst.component[1].referenceRange[0].age.low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.component[1].referenceRange[0].age.low.unit, "yrs")
        self.assertEqual(inst.component[1].referenceRange[0].age.low.value, 18)
        self.assertEqual(inst.component[1].referenceRange[0].low.code, "mL/min/{1.73_m2}")
        self.assertEqual(inst.component[1].referenceRange[0].low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.component[1].referenceRange[0].low.unit, "mL/min/1.73m2")
        self.assertEqual(inst.component[1].referenceRange[0].low.value, 60)
        self.assertEqual(inst.component[1].valueQuantity.code, "mL/min/{1.73_m2}")
        self.assertEqual(inst.component[1].valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.component[1].valueQuantity.unit, "mL/min/1.73m2")
        self.assertEqual(inst.component[1].valueQuantity.value, 60)
        self.assertEqual(inst.id, "f205")
        self.assertEqual(inst.identifier[0].system, "https://intranet.aumc.nl/labvalues")
        self.assertEqual(inst.identifier[0].value, "1304-03720-eGFR")
        self.assertEqual(inst.interpretation[0].text, "interpretation of results should be assigned based upon the level of kindey function")
        self.assertEqual(inst.issued.date, FHIRDate("2013-04-04T14:34:00+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-04-04T14:34:00+01:00")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.method.coding[0].code, "702668005")
        self.assertEqual(inst.method.coding[0].display, "MDRD")
        self.assertEqual(inst.method.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.note[0].text, "GFR estimating equations developed by the Modification of Diet in Renal Disease (MDRD) Study Group and the Chronic Kidney Disease Epidemiology Collaboration (CKD-EPI)....")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testObservation8(self):
        inst = self.instantiate_from("observation-example-abdo-tender.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation8(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation8(inst2)
    
    def implObservation8(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "exam")
        self.assertEqual(inst.category[0].coding[0].display, "Exam")
        self.assertEqual(inst.category[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/observation-category")
        self.assertEqual(inst.code.coding[0].code, "43478001")
        self.assertEqual(inst.code.coding[0].display, "Abdominal tenderness (finding)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Abdominal tenderness")
        self.assertEqual(inst.effectivePeriod.start.date, FHIRDate("2018-04-02T10:30:10+01:00").date)
        self.assertEqual(inst.effectivePeriod.start.as_json(), "2018-04-02T10:30:10+01:00")
        self.assertEqual(inst.id, "abdo-tender")
        self.assertEqual(inst.interpretation[0].coding[0].code, "A")
        self.assertEqual(inst.interpretation[0].coding[0].display, "Abnormal")
        self.assertEqual(inst.interpretation[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation")
        self.assertEqual(inst.interpretation[0].text, "Abnormal")
        self.assertEqual(inst.issued.date, FHIRDate("2018-04-03T15:30:10+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2018-04-03T15:30:10+01:00")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertTrue(inst.valueBoolean)
    
    def testObservation9(self):
        inst = self.instantiate_from("observation-example-rhstatus.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation9(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation9(inst2)
    
    def implObservation9(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "laboratory")
        self.assertEqual(inst.category[0].coding[0].display, "Laboratory")
        self.assertEqual(inst.category[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/observation-category")
        self.assertEqual(inst.category[0].text, "Laboratory")
        self.assertEqual(inst.code.coding[0].code, "883-9")
        self.assertEqual(inst.code.coding[0].display, "ABO group [Type] in Blood")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Blood Group")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2018-03-11T16:07:54+00:00").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2018-03-11T16:07:54+00:00")
        self.assertEqual(inst.id, "rhstatus")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueCodeableConcept.coding[0].code, "112144000")
        self.assertEqual(inst.valueCodeableConcept.coding[0].display, "Blood group A (finding)")
        self.assertEqual(inst.valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.valueCodeableConcept.text, "A")
    
    def testObservation10(self):
        inst = self.instantiate_from("observation-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation10(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation10(inst2)
    
    def implObservation10(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "vital-signs")
        self.assertEqual(inst.category[0].coding[0].display, "Vital Signs")
        self.assertEqual(inst.category[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/observation-category")
        self.assertEqual(inst.code.coding[0].code, "29463-7")
        self.assertEqual(inst.code.coding[0].display, "Body Weight")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.coding[1].code, "3141-9")
        self.assertEqual(inst.code.coding[1].display, "Body weight Measured")
        self.assertEqual(inst.code.coding[1].system, "http://loinc.org")
        self.assertEqual(inst.code.coding[2].code, "27113001")
        self.assertEqual(inst.code.coding[2].display, "Body weight")
        self.assertEqual(inst.code.coding[2].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.coding[3].code, "body-weight")
        self.assertEqual(inst.code.coding[3].display, "Body Weight")
        self.assertEqual(inst.code.coding[3].system, "http://acme.org/devices/clinical-codes")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2016-03-28").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2016-03-28")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueQuantity.code, "[lb_av]")
        self.assertEqual(inst.valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.valueQuantity.unit, "lbs")
        self.assertEqual(inst.valueQuantity.value, 185)

