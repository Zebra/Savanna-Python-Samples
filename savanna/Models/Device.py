"""
Device recall report.
"""

class Device:

    def __init__(self, dateTime, firmFEINumber, knumbers, openFDA, 
    otherSubmissionDescription, pmaNumbers, productCode, productResNumber,
    resEventNumber, rootCauseDescription):
        self.dateTime = dateTime
        self.firmFEINumber = firmFEINumber
        self.knumbers = knumbers
        self.openFDA = openFDA
        self.otherSubmissionDescription = otherSubmissionDescription
        self.pmaNumbers = pmaNumbers
        self.productCode = productCode
        self.productResNumber = productResNumber
        self.resEventNumber = resEventNumber
        self.rootCauseDescription = rootCauseDescription

    """
    Date that FDA determined recall actions were completed and terminated the recall. For details about
    termination of a recall see http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfcfr/cfrsearch.cfm?fr=7.55
    """
    @property
    def eventDateTerminated(self):
        return self._dateTime

    """
    Facility identifier assigned to facility by the FDA Office of Regulatory Affairs.
    """
    @property
    def firmFEINumber(self):
        return self._firmFEINumber

    """
    FDA-assigned premarket notification number, including leading letters. Leading letters "BK" indicates
    510(k) clearance, or Premarket Notification, cleared by Center for Biologics Evaluation and Research.
    Leading letters "DEN" indicates De Novo, or Evaluation of Automatic Class III Designation. Leading letter
    "K" indicates 510(k) clearance, or Premarket Notification. `Source`: 510(k)
    """
    @property
    def knumbers(self):
        return self._knumbers

    """
    Information about the recalled medical device.
    """
    @property
    def openFDA(self):
        return self._openFDA

    """
    If 510(k) or PMA numbers are not applicable to the device recalled, the recall may contain other regulatory
    descriptions, such as `exempt`.
    """
    @property
    def otherSubmissionDescription(self):
        return self._otherSubmissionDescription

    """
    FDA-assigned premarket application number, including leading letters. Leading letter "D" indicates Product
    Development Protocol type of Premarket Approval. Leading letters "BP" indicates Premarket Approval by
    Center for Biologics Evaluation and Research. Leading letter "H" indicates Humanitarian Device Exemption
    approval. Leading letter "N" indicates New Drug Application. Early PMAs were approved as NDAs. Leading
    letter "P" indicates Premarket Approval.
    """
    @property
    def pmaNumbers(self):
        return self._pmaNumbers

    """
    A three-letter identifier assigned to a device category. Assignment is based upon the medical device
    classification designated under 21 CFR Parts 862-892, and the technology and intended use of the device.
    Occasionally these codes are changed over time.
    """
    @property
    def productCode(self):
        return self._productCode

    """
    The product's number in the Recall Enterprise System.
    """
    @property
    def productResNumber(self):
        return self._productResNumber

    """
    A five digit, numerical designation assigned by FDA to a specific recall event used for tracking purposes.
    """
    @property
    def resEventNumber(self):
        return self._resEventNumber

    """
    FDA determined general type of recall cause. Per FDA policy, recall cause determinations are subject to
    modification up to the point of termination of the recall.
    """
    @property
    def rootCauseDescription(self):
        return self._rootCauseDescription