import random
R_EATING="I don't like eating anything because I'm a bot obviously!"
I_WEEKS="The difference in the internship duration is to provide you flexibility to accommodate your academic requirements, as many colleges do not allow their students to do internship while the academic sessions are in progress. Such students can contribute more hours and finish their internship early.The problem statement for all the duration for the resp. domain will be same. The excellence awards will categorised based on the duration and projects submitted for 6 weeks will be accessed in relation to the other projects submitted for the same duration"
C_CER="""The participants will get following certificates and letters:
> Appointment letter within 15 days after the interns choose the field of interest
> Industry Training Certificate (further to completing assessment)
> Experience Certificate from Cloud Counselage (on successful completion of internship)
> Appreciation letter/certificate ( For top performers)"""
H_HELP="""Participants will get help related to understanding the problem statement and the project delivery process."""
A="We will be providing appointment letters within 15 days after the interns choose the field of interest."
B="The interns have to complete the tasks as per the instructions within the deadlines."
D="We encourage focusing on one field at a time as this will help yield better results."
E="""Internship and other IAC activities are absolutely FREE.
There is no cost involved for participating in the community activities (including internships) as this is a noble initiative taken up by Cloud Counselage Pvt. Ltd. in association with Gift- A-Career Foundation, to help students, get job-ready, in time! """
F="""This internship is designed for students in higher education courses and any such student aspiring for IT and Management career can participate in this internship."""
G="This internship program is designed for undergraduate students but if graduates and freshers feel it is beneficial for them then they can participate in this internship program."
I="For schedule of internship please refer https://cloudcounselage0-my.sharepoint.com/personal/member_industryacademiacommunity_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fmember%5Findustryacademiacommunity%5Fcom%2FDocuments%2FIP%202023%2FInternship%20Program%202023%20Schedule%2Ejpg&parent=%2Fpersonal%2Fmember%5Findustryacademiacommunity%5Fcom%2FDocuments%2FIP%202023&ga=1.The interns are expected to contribute minimum 1 to 2 hours on a daily basis."
J="A form will be made available to the interns to choose the domain and the duration of the internship."
K="""Industry-Academia Community (IAC) is a part of 'Industry-Academia Connect' initiative of Cloud Counselage Pvt. Ltd. in association with Gift-A-Career Foundation created for Industry & Academia PAN India. This community engages and supports higher education students and freshers by providing them with 360-degree professional development and career growth opportunities through Career Vision, Career Guidance, Industry & Corporate Exposure, and Hands-on experience/remote internships on live projects. All the benefits of the community can be availed from any corner of the world as it is an online community and at no cost to the members."""
L="""1. Industry Exposure Workshops
2. Career Vision
3. Career Guidance
4. Industry Training
5. Internship Program
6. Industry Visits
7. CV & Interview Preparations
8. Soft Skills Workshops
9. Career Assessments
10. Hackathons
11. Job Placements
12. Entrepreneurship Program"""
M="""This is a 6-12 weeks online internship, that will be conducted during the vacation (generally) and you can choose any of one domain from the ones that we offer. This is a guaranteed internship for all the students in the age group of 17-24 years who aspire to IT & Management careers. There will be no interviews or aptitude tests required for participating in this internship. To keep the internship focused and reduce the stress to the students we allow working on only one technology at a time. The interns who have successfully submitted the project, get an experience certificate. The interns who have performed exceptionally well and have delivered high-quality deliverables are provided with ‘letters of appreciation' as well and are facilitated in the ‘Industry Academia Excellence Awards’."""
N="""More than 90% of the community members have rated us 4 & 5 out of 5 for their overall experience of the activities. The reviews of the participant are available on our iReviews page and social media pages. The students have experienced a boost in confidence, especially during the interview, were able to channelize the interview, and have been placed in companies like Oracle, Microsoft, Capgemini, TCS, Wipro, Deloitte, etc. In terms of higher education, they were able to secure places in reputed universities in U.S., Australia, Ireland, etc."""




def unknown():
    response=['You can go through our website for that',
              "go to https://www.industryacademiacommunity.com/faqs",
              "Sorry! I am unable to get it...",
              "I can only answer related to Industry Academia Community(IAC)"][random.randrange(4)]
    return response
