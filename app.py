import pandas as pd

from solution.reader.data_reader import DataReader
from solution.validator.validator_wrapper import ValidatorWrapper

if __name__ == '__main__':
    data_reader = DataReader()

    subjects_ae = data_reader.read_subject_list("ae")

    subjects_cm = data_reader.read_subject_list("cm")

    for subject in subjects_ae:
        ae_df = pd.DataFrame(data_reader.read_data_for_subject("ae", subject))
        cm_df = pd.DataFrame(data_reader.read_data_for_subject("cm", subject))
        for index, row in ae_df.iterrows():
            ValidatorWrapper().validate(ae_df.iloc[index], cm_df.iloc[index], ae_df, cm_df, row["formname"],
                                        row["formid"], row["formidx"],
                                        row["subjectid"])

    for subject in subjects_cm:
        ae_df = pd.DataFrame(data_reader.read_data_for_subject("ae", subject))
        cm_df = pd.DataFrame(data_reader.read_data_for_subject("cm", subject))
        for index, row in ae_df.iterrows():
            print(row['c1'], row['c2'])

print()
