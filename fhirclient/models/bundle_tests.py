#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-02-06.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from . import bundle
from .fhirdate import FHIRDate


class BundleTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Bundle", js["resourceType"])
        return bundle.Bundle(js)
    
    def testBundle1(self):
        inst = self.instantiate_from("xds-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle1(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle1(inst2)
    
    def implBundle1(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "urn:uuid:3fdc72f4-a11d-4a9d-9260-a9f745779e1d")
        self.assertEqual(inst.entry[0].request.method, "POST")
        self.assertEqual(inst.entry[0].request.url, "DocumentReference")
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date)
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(inst.entry[1].fullUrl, "http://localhost:9556/svc/fhir/Patient/a2")
        self.assertEqual(inst.entry[1].request.ifNoneExist, "Patient?identifier=http://acme.org/xds/patients!89765a87b")
        self.assertEqual(inst.entry[1].request.method, "POST")
        self.assertEqual(inst.entry[1].request.url, "Patient")
        self.assertEqual(inst.entry[1].resource.id, "a2")
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date)
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(inst.entry[2].fullUrl, "http://localhost:9556/svc/fhir/Practitioner/a3")
        self.assertEqual(inst.entry[2].request.method, "POST")
        self.assertEqual(inst.entry[2].request.url, "Practitioner")
        self.assertEqual(inst.entry[2].resource.id, "a3")
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date)
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(inst.entry[3].fullUrl, "http://localhost:9556/svc/fhir/Practitioner/a4")
        self.assertEqual(inst.entry[3].request.method, "POST")
        self.assertEqual(inst.entry[3].request.url, "Practitioner")
        self.assertEqual(inst.entry[3].resource.id, "a4")
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date)
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(inst.entry[4].fullUrl, "http://localhost:9556/svc/fhir/Binary/1e404af3-077f-4bee-b7a6-a9be97e1ce32")
        self.assertEqual(inst.entry[4].request.method, "POST")
        self.assertEqual(inst.entry[4].request.url, "Binary")
        self.assertEqual(inst.entry[4].resource.id, "1e404af3-077f-4bee-b7a6-a9be97e1ce32")
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date)
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(inst.id, "xds")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2013-07-01T13:11:33Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2013-07-01T13:11:33Z")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.type, "transaction")
    
    def testBundle2(self):
        inst = self.instantiate_from("diagnosticreport-example-lri.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle2(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle2(inst2)
    
    def implBundle2(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "http://test.fhir.org/r4/DiagnosticReport/lri-example")
        self.assertEqual(inst.entry[0].resource.id, "lri-example")
        self.assertEqual(inst.entry[1].fullUrl, "http://test.fhir.org/r4/Observation/lri-gramstain1")
        self.assertEqual(inst.entry[1].resource.id, "gramstain1")
        self.assertEqual(inst.entry[2].fullUrl, "http://test.fhir.org/r4/Observation/lri-gramstain2")
        self.assertEqual(inst.entry[2].resource.id, "gramstain2")
        self.assertEqual(inst.entry[3].fullUrl, "http://test.fhir.org/r4/Observation/lri-gramstain3")
        self.assertEqual(inst.entry[3].resource.id, "gramstain3")
        self.assertEqual(inst.entry[4].fullUrl, "http://test.fhir.org/r4/Observation/lri-gramstain4")
        self.assertEqual(inst.entry[4].resource.id, "gramstain4")
        self.assertEqual(inst.entry[5].fullUrl, "http://test.fhir.org/r4/Observation/lri-growth1")
        self.assertEqual(inst.entry[5].resource.id, "growth1")
        self.assertEqual(inst.entry[6].fullUrl, "http://test.fhir.org/r4/Observation/lri-growth2")
        self.assertEqual(inst.entry[6].resource.id, "growth2")
        self.assertEqual(inst.entry[7].fullUrl, "http://test.fhir.org/r4/Observation/lri-growth3")
        self.assertEqual(inst.entry[7].resource.id, "growth3")
        self.assertEqual(inst.entry[8].fullUrl, "http://test.fhir.org/r4/Observation/lri-org2-amp")
        self.assertEqual(inst.entry[8].resource.id, "org2-amp")
        self.assertEqual(inst.entry[9].fullUrl, "http://test.fhir.org/r4/Observation/lri-org2-cip")
        self.assertEqual(inst.entry[9].resource.id, "org2-cip")
        self.assertEqual(inst.id, "lri-example")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2017-06-27T00:52:51Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2017-06-27T00:52:51Z")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.meta.versionId, "1")
        self.assertEqual(inst.type, "collection")
    
    def testBundle3(self):
        inst = self.instantiate_from("diagnosticreport-example-f202-bloodculture.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle3(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle3(inst2)
    
    def implBundle3(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "https://example.com/base/DiagnosticReport/f202")
        self.assertEqual(inst.entry[0].resource.id, "f202")
        self.assertEqual(inst.entry[1].fullUrl, "https://example.com/base/ServiceRequest/req")
        self.assertEqual(inst.entry[1].resource.id, "req")
        self.assertEqual(inst.id, "f202")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.type, "collection")
    
    def testBundle4(self):
        inst = self.instantiate_from("bundle-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle4(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle4(inst2)
    
    def implBundle4(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "https://example.com/base/MedicationRequest/3123")
        self.assertEqual(inst.entry[0].resource.id, "3123")
        self.assertEqual(inst.entry[0].search.mode, "match")
        self.assertEqual(inst.entry[0].search.score, 1)
        self.assertEqual(inst.entry[1].fullUrl, "https://example.com/base/Medication/example")
        self.assertEqual(inst.entry[1].resource.id, "example")
        self.assertEqual(inst.entry[1].search.mode, "include")
        self.assertEqual(inst.id, "bundle-example")
        self.assertEqual(inst.link[0].relation, "self")
        self.assertEqual(inst.link[0].url, "https://example.com/base/MedicationRequest?patient=347&_include=MedicationRequest.medication&_count=2")
        self.assertEqual(inst.link[1].relation, "next")
        self.assertEqual(inst.link[1].url, "https://example.com/base/MedicationRequest?patient=347&searchId=ff15fd40-ff71-4b48-b366-09c706bed9d0&page=2")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2014-08-18T01:43:30Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2014-08-18T01:43:30Z")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.total, 3)
        self.assertEqual(inst.type, "searchset")
    
    def testBundle5(self):
        inst = self.instantiate_from("endpoint-examples-general-template.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle5(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle5(inst2)
    
    def implBundle5(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "http://hl7.org/fhir/Endpoint/71")
        self.assertEqual(inst.entry[0].resource.id, "71")
        self.assertEqual(inst.entry[1].fullUrl, "http://hl7.org/fhir/Endpoint/72")
        self.assertEqual(inst.entry[1].resource.id, "72")
        self.assertEqual(inst.entry[2].fullUrl, "http://hl7.org/fhir/Endpoint/73")
        self.assertEqual(inst.entry[2].resource.id, "73")
        self.assertEqual(inst.entry[3].fullUrl, "http://hl7.org/fhir/Endpoint/74")
        self.assertEqual(inst.entry[3].resource.id, "74")
        self.assertEqual(inst.entry[4].fullUrl, "http://hl7.org/fhir/Endpoint/75")
        self.assertEqual(inst.entry[4].resource.id, "75")
        self.assertEqual(inst.entry[5].fullUrl, "http://hl7.org/fhir/Endpoint/76")
        self.assertEqual(inst.entry[5].resource.id, "76")
        self.assertEqual(inst.entry[6].fullUrl, "http://hl7.org/fhir/Endpoint/77")
        self.assertEqual(inst.entry[6].resource.id, "77")
        self.assertEqual(inst.entry[7].fullUrl, "http://hl7.org/fhir/Endpoint/78")
        self.assertEqual(inst.entry[7].resource.id, "78")
        self.assertEqual(inst.entry[8].fullUrl, "http://hl7.org/fhir/Endpoint/79")
        self.assertEqual(inst.entry[8].resource.id, "79")
        self.assertEqual(inst.entry[9].fullUrl, "http://hl7.org/fhir/Endpoint/80")
        self.assertEqual(inst.entry[9].resource.id, "80")
        self.assertEqual(inst.id, "b0a5e4277-83c4-4adb-87e2-e3efe3369b6f")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.type, "collection")
    
    def testBundle6(self):
        inst = self.instantiate_from("diagnosticreport-genetics-example-2-familyhistory.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle6(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle6(inst2)
    
    def implBundle6(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "https://example.com/base/DiagnosticReport/dg2")
        self.assertEqual(inst.entry[0].resource.id, "dg2")
        self.assertEqual(inst.entry[1].fullUrl, "https://example.com/base/FamilyMemberHistory/f1-genetics")
        self.assertEqual(inst.entry[1].resource.id, "f1-genetics")
        self.assertEqual(inst.id, "dg2")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.type, "collection")
    
    def testBundle7(self):
        inst = self.instantiate_from("practitioner-examples-general.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle7(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle7(inst2)
    
    def implBundle7(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "http://hl7.org/fhir/Practitioner/1")
        self.assertEqual(inst.entry[0].resource.id, "1")
        self.assertEqual(inst.entry[1].fullUrl, "http://hl7.org/fhir/Practitioner/13")
        self.assertEqual(inst.entry[1].resource.id, "13")
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[2].fullUrl, "http://hl7.org/fhir/Practitioner/14")
        self.assertEqual(inst.entry[2].resource.id, "14")
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[3].fullUrl, "http://hl7.org/fhir/Practitioner/15")
        self.assertEqual(inst.entry[3].resource.id, "15")
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[4].fullUrl, "http://hl7.org/fhir/Practitioner/16")
        self.assertEqual(inst.entry[4].resource.id, "16")
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[5].fullUrl, "http://hl7.org/fhir/Practitioner/17")
        self.assertEqual(inst.entry[5].resource.id, "17")
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[6].fullUrl, "http://hl7.org/fhir/Practitioner/18")
        self.assertEqual(inst.entry[6].resource.id, "18")
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[7].fullUrl, "http://hl7.org/fhir/Practitioner/19")
        self.assertEqual(inst.entry[7].resource.id, "19")
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[8].fullUrl, "http://hl7.org/fhir/Practitioner/20")
        self.assertEqual(inst.entry[8].resource.id, "20")
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[9].fullUrl, "http://hl7.org/fhir/Practitioner/21")
        self.assertEqual(inst.entry[9].resource.id, "21")
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.id, "3ad0687e-f477-468c-afd5-fcc2bf897809")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.type, "collection")
    
    def testBundle8(self):
        inst = self.instantiate_from("patient-examples-general.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle8(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle8(inst2)
    
    def implBundle8(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "http://hl7.org/fhir/Patient/1")
        self.assertEqual(inst.entry[0].resource.id, "1")
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[1].fullUrl, "http://hl7.org/fhir/Patient/2")
        self.assertEqual(inst.entry[1].resource.id, "2")
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[2].fullUrl, "http://hl7.org/fhir/Patient/3")
        self.assertEqual(inst.entry[2].resource.id, "3")
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[3].fullUrl, "http://hl7.org/fhir/Patient/4")
        self.assertEqual(inst.entry[3].resource.id, "4")
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[4].fullUrl, "http://hl7.org/fhir/Patient/5")
        self.assertEqual(inst.entry[4].resource.id, "5")
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[5].fullUrl, "http://hl7.org/fhir/Patient/6")
        self.assertEqual(inst.entry[5].resource.id, "6")
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[6].fullUrl, "http://hl7.org/fhir/Patient/7")
        self.assertEqual(inst.entry[6].resource.id, "7")
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[7].fullUrl, "http://hl7.org/fhir/Patient/8")
        self.assertEqual(inst.entry[7].resource.id, "8")
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[8].fullUrl, "http://hl7.org/fhir/Patient/9")
        self.assertEqual(inst.entry[8].resource.id, "9")
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.entry[9].fullUrl, "http://hl7.org/fhir/Patient/10")
        self.assertEqual(inst.entry[9].resource.id, "10")
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.id, "b248b1b2-1686-4b94-9936-37d7a5f94b51")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.type, "collection")
    
    def testBundle9(self):
        inst = self.instantiate_from("diagnosticreport-example-ghp.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle9(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle9(inst2)
    
    def implBundle9(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "https://example.com/base/DiagnosticReport/ghp")
        self.assertEqual(inst.entry[0].resource.id, "ghp")
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.date, FHIRDate("2015-08-16T10:35:23Z").date)
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.as_json(), "2015-08-16T10:35:23Z")
        self.assertEqual(inst.entry[1].fullUrl, "https://example.com/base/Specimen/rtt")
        self.assertEqual(inst.entry[1].resource.id, "rtt")
        self.assertEqual(inst.entry[2].fullUrl, "https://example.com/base/Specimen/ltt")
        self.assertEqual(inst.entry[2].resource.id, "ltt")
        self.assertEqual(inst.entry[3].fullUrl, "https://example.com/base/Specimen/urine")
        self.assertEqual(inst.entry[3].resource.id, "urine")
        self.assertEqual(inst.entry[4].fullUrl, "https://example.com/base/Observation/p2")
        self.assertEqual(inst.entry[4].resource.id, "p2")
        self.assertEqual(inst.entry[5].fullUrl, "https://example.com/base/Observation/r1")
        self.assertEqual(inst.entry[5].resource.id, "r1")
        self.assertEqual(inst.entry[6].fullUrl, "https://example.com/base/Observation/r2")
        self.assertEqual(inst.entry[6].resource.id, "r2")
        self.assertEqual(inst.entry[7].fullUrl, "https://example.com/base/Observation/r3")
        self.assertEqual(inst.entry[7].resource.id, "r3")
        self.assertEqual(inst.entry[8].fullUrl, "https://example.com/base/Observation/r4")
        self.assertEqual(inst.entry[8].resource.id, "r4")
        self.assertEqual(inst.entry[9].fullUrl, "https://example.com/base/Observation/r5")
        self.assertEqual(inst.entry[9].resource.id, "r5")
        self.assertEqual(inst.id, "ghp")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.type, "collection")
    
    def testBundle10(self):
        inst = self.instantiate_from("questionnaire-profile-example-ussg-fht.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")
        self.implBundle10(inst)
        
        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle10(inst2)
    
    def implBundle10(self, inst):
        self.assertEqual(inst.entry[0].fullUrl, "http://hl7.org/fhir/us/sdc/Questionnaire/54127-6")
        self.assertEqual(inst.entry[0].request.method, "PUT")
        self.assertEqual(inst.entry[0].request.url, "http://hl7.org/fhir/us/sdc/Questionnaire/54127-6")
        self.assertEqual(inst.entry[0].resource.id, "54127-6")
        self.assertEqual(inst.entry[0].resource.meta.profile[0], "http://hl7.org/fhir/us/sdc/StructureDefinition/sdc-questionnaire")
        self.assertEqual(inst.entry[1].fullUrl, "http://hl7.org/fhir/us/sdc/ValueSet/LL1-9")
        self.assertEqual(inst.entry[1].request.method, "PUT")
        self.assertEqual(inst.entry[1].request.url, "http://hl7.org/fhir/us/sdc/ValueSet/LL1-9")
        self.assertEqual(inst.entry[1].resource.id, "LL1-9")
        self.assertEqual(inst.entry[1].resource.meta.profile[0], "http://hl7.org/fhir/us/sdc/StructureDefinition/sdc-valueset")
        self.assertEqual(inst.entry[2].fullUrl, "http://hl7.org/fhir/us/sdc/ValueSet/LL623-0")
        self.assertEqual(inst.entry[2].request.method, "PUT")
        self.assertEqual(inst.entry[2].request.url, "http://hl7.org/fhir/us/sdc/ValueSet/LL623-0")
        self.assertEqual(inst.entry[2].resource.id, "LL623-0")
        self.assertEqual(inst.entry[2].resource.meta.profile[0], "http://hl7.org/fhir/us/sdc/StructureDefinition/sdc-valueset")
        self.assertEqual(inst.entry[3].fullUrl, "http://hl7.org/fhir/us/sdc/ValueSet/LL361-7")
        self.assertEqual(inst.entry[3].request.method, "PUT")
        self.assertEqual(inst.entry[3].request.url, "http://hl7.org/fhir/us/sdc/ValueSet/LL361-7")
        self.assertEqual(inst.entry[3].resource.id, "LL361-7")
        self.assertEqual(inst.entry[3].resource.meta.profile[0], "http://hl7.org/fhir/us/sdc/StructureDefinition/sdc-valueset")
        self.assertEqual(inst.entry[4].fullUrl, "http://hl7.org/fhir/us/sdc/ValueSet/LL629-7")
        self.assertEqual(inst.entry[4].request.method, "PUT")
        self.assertEqual(inst.entry[4].request.url, "http://hl7.org/fhir/us/sdc/ValueSet/LL629-7")
        self.assertEqual(inst.entry[4].resource.id, "LL629-7")
        self.assertEqual(inst.entry[4].resource.meta.profile[0], "http://hl7.org/fhir/us/sdc/StructureDefinition/sdc-valueset")
        self.assertEqual(inst.entry[5].fullUrl, "http://hl7.org/fhir/us/sdc/ValueSet/LL628-9")
        self.assertEqual(inst.entry[5].request.method, "PUT")
        self.assertEqual(inst.entry[5].request.url, "http://hl7.org/fhir/us/sdc/ValueSet/LL628-9")
        self.assertEqual(inst.entry[5].resource.id, "LL628-9")
        self.assertEqual(inst.entry[5].resource.meta.profile[0], "http://hl7.org/fhir/us/sdc/StructureDefinition/sdc-valueset")
        self.assertEqual(inst.entry[6].fullUrl, "http://hl7.org/fhir/us/sdc/ValueSet/LL626-3")
        self.assertEqual(inst.entry[6].request.method, "PUT")
        self.assertEqual(inst.entry[6].request.url, "http://hl7.org/fhir/us/sdc/ValueSet/LL626-3")
        self.assertEqual(inst.entry[6].resource.id, "LL626-3")
        self.assertEqual(inst.entry[6].resource.meta.profile[0], "http://hl7.org/fhir/us/sdc/StructureDefinition/sdc-valueset")
        self.assertEqual(inst.entry[7].fullUrl, "http://hl7.org/fhir/us/sdc/ValueSet/LL619-8")
        self.assertEqual(inst.entry[7].request.method, "PUT")
        self.assertEqual(inst.entry[7].request.url, "http://hl7.org/fhir/us/sdc/ValueSet/LL619-8")
        self.assertEqual(inst.entry[7].resource.id, "LL619-8")
        self.assertEqual(inst.entry[7].resource.meta.profile[0], "http://hl7.org/fhir/us/sdc/StructureDefinition/sdc-valueset")
        self.assertEqual(inst.entry[8].fullUrl, "http://hl7.org/fhir/us/sdc/ValueSet/LL621-4")
        self.assertEqual(inst.entry[8].request.method, "PUT")
        self.assertEqual(inst.entry[8].request.url, "http://hl7.org/fhir/us/sdc/ValueSet/LL621-4")
        self.assertEqual(inst.entry[8].resource.id, "LL621-4")
        self.assertEqual(inst.entry[8].resource.meta.profile[0], "http://hl7.org/fhir/us/sdc/StructureDefinition/sdc-valueset")
        self.assertEqual(inst.entry[9].fullUrl, "http://hl7.org/fhir/us/sdc/ValueSet/LL624-8")
        self.assertEqual(inst.entry[9].request.method, "PUT")
        self.assertEqual(inst.entry[9].request.url, "http://hl7.org/fhir/us/sdc/ValueSet/LL624-8")
        self.assertEqual(inst.entry[9].resource.id, "LL624-8")
        self.assertEqual(inst.entry[9].resource.meta.profile[0], "http://hl7.org/fhir/us/sdc/StructureDefinition/sdc-valueset")
        self.assertEqual(inst.id, "ussg-fht")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.type, "transaction")

