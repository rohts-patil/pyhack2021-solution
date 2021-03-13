# pyhack2021

## Context

At Saama we work with pharmaceutical compaines to speed up their clinical Trials.
Clinical Trials - For a drug/medicine to get to the market it has to go through certain phases of testing on humans. These trials are done in hospitals(sites) and medicines are administered to selected patients(subjects) by the doctors.

During the trial there can be [Adverse events](https://en.wikipedia.org/wiki/Adverse_event) (a situation when the subject has side effects because of the drug under investigation).

Concomitant medications (CM) are other prescription medications study participant takes because of an Adverse Event.

For Example: Loperamide (Medication) taken for Diarrhea (Adverse event). As it happens usually, The Medication is typically taken only during the Adverse event

## Problem summary

Data from Clinical Trials are collected by the means of various Forms. For example, in this Hackathon, we have the Adverse Event (AE) and Concomitant Medication (CM) Forms and their respective information collected. The Adverse Event (AE) Form captures all the adverse side effects the Patient or Subject may face during a Clinical Trial after enrollment. These effects can then be treated by a medication, called Concomitant Medication and the related data is again captured as a Concomitant Medication (CM) Form. Hence we can see that both Adverse Events (AE) and Concomitant Medications (CM) are interrelated. Here, we will provide two datasets, each of AE and CM Forms samples as CSV files, to access full dataset use the APIs. APIs must be called after referring to the API guide and the goal of this Hackathon is to find specific issues with this data.

## Sample datasets

Below you can take a look at how the data looks like in the backend. This is the data that we will be serving you on the api requests.

| Domain | Link                                                                         |
| ------ | ---------------------------------------------------------------------------- |
| AE     | [Sample](https://www.dropbox.com/s/wg3xi7f9kxr5o4w/AE_data_sample.xlsx?dl=0) |
| CM     | [Sample](https://www.dropbox.com/s/uar0h8pkfxtt2ij/cm_data_sample.xlsx?dl=0) |

You can check what each column means in the [data dictionary](https://www.dropbox.com/s/5s83sveiovzolsh/Hackathon%20Data%20Dictionary.xlsx?dl=0).

## Problems

Common Problems(discrepancies) seen in this dataset are

### TYPE1

Patients and rows for which Medication are given prior to the Adverse Events.
Eg: ![image](https://user-images.githubusercontent.com/16976605/110984096-aaaffe80-8338-11eb-8bb0-d4193ffde67c.png)

### TYPE2

Patients and rows for which days Medications are given and Adverse Event occur don't match.
Eg: ![image](https://user-images.githubusercontent.com/16976605/110984437-23af5600-8339-11eb-97f9-0b099cfad2e7.png)

### TYPE3

Duplicate Adverse events are entered or Adverse Events overlap.
![image](https://user-images.githubusercontent.com/16976605/110985084-fc0cbd80-8339-11eb-86eb-f33f065ba55a.png)

### TYPE4

Patients and rows which have overlapping of Concomitant medications.
![image](https://user-images.githubusercontent.com/16976605/110985591-a1c02c80-833a-11eb-85de-4a17de36ac39.png)

### TYPE5

Patients for which the duration of Adverse Events is not adding up to corresponding concomitant medication.
![image](https://user-images.githubusercontent.com/16976605/110986383-99b4bc80-833b-11eb-9306-5db76834cc45.png)

...

## Resources

- **API Host**: https://pyhack-dot-pharmanlp-177020.uc.r.appspot.com \
  This is where we have hosted the api, play around with a temporary email address initially if you want to test out the api before actual submission.

- **API Docs**: https://pyhack-dot-pharmanlp-177020.uc.r.appspot.com/apidocs \
  This will contain the docs to the endpoints that you will have to connect to to get the data and subimt the result at the end.

## Solution

> Look in the api docuemntation to see how you can communicate with the api and perform these tasks.

- Get a list subjects for the given **study id** + **domain id**
- Get subject data for **study id** + **domain id** + **subject id**
- Process data and find discrepancy (diffent type of discrepancies are defined above)
- Submit discrepancy data to the API (use your email address to submit the discrepancies)

## Bonus Points

- Well written Test Harness for testing your code
