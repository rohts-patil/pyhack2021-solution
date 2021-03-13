from solution.validator.type1_validator import Type1Validator
from solution.validator.type2_validator import Type2Validator
from solution.validator.type3_validator import Type3Validator
from solution.validator.type4_validator import Type4Validator
from solution.validator.type5_validator import Type5Validator
from solution.writer.data_writer import DataWriter


class ValidatorWrapper():
    def __init__(self):
        self.data = {
            "email_address": "rohts.patil@gmail.com",
            "formname": "AE202",
            "formid": "38768",
            "formidx": "43",
            "type": "TYPE1",
            "subjectid": "TYPE1"
        }

        self.data_writer = DataWriter()

    def validate(self, ae, cm, ae_df, cm_df, formname, formid, formidx, subjectid):
        self.data["formname"] = formname
        self.data["formid"] = formid
        self.data["formidx"] = formidx
        self.data["subjectid"] = subjectid

        if Type1Validator().validate(ae, cm, ae_df, cm_df):
            self.data["type"] = "TYPE1"
            self.data_writer.write(self.data)

        if Type2Validator().validate(ae, cm, ae_df, cm_df):
            self.data["type"] = "TYPE2"
            self.data_writer.write(self.data)

        if Type3Validator().validate(ae, cm, ae_df, cm_df):
            self.data["type"] = "TYPE3"
            self.data_writer.write(self.data)

        if Type4Validator().validate(ae, cm, ae_df, cm_df):
            self.data["type"] = "TYPE4"
            self.data_writer.write(self.data)

        if Type5Validator().validate(ae, cm, ae_df, cm_df):
            self.data["type"] = "TYPE5"
            self.data_writer.write(self.data)
