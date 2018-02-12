# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-12 08:08
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('home', '0030_auto_20180125_1931'), ('home', '0031_auto_20180125_2108'), ('home', '0032_auto_20180125_2151'), ('home', '0033_auto_20180125_2152'), ('home', '0034_auto_20180125_2216'), ('home', '0035_auto_20180125_2248'), ('home', '0036_auto_20180125_2301'), ('home', '0037_auto_20180126_2055'), ('home', '0038_auto_20180126_2135'), ('home', '0039_auto_20180126_2137'), ('home', '0040_auto_20180126_2255'), ('home', '0041_employmenttimecommitment_quit_on_acceptance'), ('home', '0042_auto_20180129_1944'), ('home', '0043_auto_20180130_2101'), ('home', '0044_auto_20180131_1346'), ('home', '0045_auto_20180131_1448'), ('home', '0046_auto_20180201_0125'), ('home', '0047_auto_20180201_0153'), ('home', '0048_auto_20180201_0202'), ('home', '0049_auto_20180201_0358'), ('home', '0050_auto_20180202_1312'), ('home', '0051_auto_20180202_1334'), ('home', '0052_auto_20180202_1346'), ('home', '0053_auto_20180202_1415'), ('home', '0054_auto_20180205_1520'), ('home', '0055_auto_20180205_1644'), ('home', '0056_auto_20180205_1645'), ('home', '0057_auto_20180205_1658'), ('home', '0058_auto_20180206_2308'), ('home', '0059_auto_20180206_2311'), ('home', '0060_auto_20180208_2151'), ('home', '0061_comrade_agreed_to_code_of_conduct'), ('home', '0062_auto_20180209_1422'), ('home', '0063_auto_20180209_1427'), ('home', '0064_community_tutorial'), ('home', '0065_finalapplication_community_specific_questions'), ('home', '0066_auto_20180210_1614'), ('home', '0067_auto_20180210_1659')]

    dependencies = [
        ('home', '0029_auto_20180112_2334_squashed_0044_auto_20180116_0251'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantApproval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval_status', models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('W', 'Withdrawn'), ('R', 'Rejected')], default='W', max_length=1)),
                ('reason_denied', models.CharField(blank=True, help_text='\n            Please explain why you are withdrawing this request. This\n            explanation will only be shown to Outreachy organizers and\n            approved people within this community.\n            ', max_length=3000)),
                ('over_18', models.NullBooleanField(verbose_name='Will you be 18 years or older when the Outreachy internship starts?')),
                ('gsoc_or_outreachy_internship', models.NullBooleanField(help_text='Have you been accepted as a Google Summer of Code intern or an Outreachy intern before? Please say yes even if you did not complete the internship.', verbose_name='Previous Google Summer of Code or Outreachy internship?')),
                ('enrolled_as_student', models.NullBooleanField(help_text='Will you be enrolled in a university or college during the Outreachy internship period?')),
                ('employed', models.NullBooleanField(help_text='Will you be an employee (for any number of hours) during the Outreachy internship period?')),
                ('contractor', models.NullBooleanField(help_text='Will you be a contractor during the Outreachy internship period?')),
                ('volunteer_time_commitments', models.NullBooleanField(help_text='Will you have volunteer time commitments that require more than 10 hours a week during the Outreachy internship period?')),
                ('other_time_commitments', models.TextField(blank=True, help_text='(Optional) If you have other time commitments outside of school, work, or volunteer hours, please use this field to let your mentor know. Examples of other time commitments include vacation that lasts longer than a week, coding school time commitments, community or online classes, etc.', max_length=3000)),
                ('us_national_or_permanent_resident', models.NullBooleanField(help_text='Are you a national or permanent resident of the United States of America? Outreachy is open to some people around the world, and additional grpous of people in the U.S.A.')),
                ('living_in_us', models.NullBooleanField(help_text='Please answer yes even if you are a citizen of a country other than USA.', verbose_name='Will you be living for the majority of the Outreachy internship period in the United States of America and be eligible to work in the U.S.A?')),
                ('under_export_control', models.NullBooleanField(help_text='See the <a href="https://www.treasury.gov/resource-center/sanctions/Programs/Pages/Programs.aspx">US export control and sanctions list</a> for more information', verbose_name='Are you a person or entity restricted by United States of America export controls or sanctions programs?')),
                ('us_sanctioned_country', models.NullBooleanField(help_text='If you have citizenship with Cuba, Iran, North Korea, or Syria, please answer yes, even if you are not currently living in those countries.', verbose_name='Are you a citizen, resident, or national of Crimea, Cuba, Iran, North Korea, or Syria?')),
                ('eligible_to_work', models.NullBooleanField(help_text='Are you eligible to work for 40 hours a week in the country (or countries) you will be living in during the Outreachy internship period?</p><p>Student visas: Please note that in some countries, students studying abroad on a student visa may not be eligible to work full-time (40 hours a week). If you are on a student visa, please double check with your school counselors before applying.</p><p>Spouse visas: In some countries, spousal visas may not allow spouses to work. Please contact your immigration officer if you have any questions about whether your visa allows you to work full-time (40 hours a week).')),
                ('us_resident_demographics', models.NullBooleanField(verbose_name='Are you Black/African American, Hispanic/Latin@, Native American, Alaska Native, Native Hawaiian, or Pacific Islander?')),
                ('transgender', models.NullBooleanField(help_text='If you are questioning whether you are transgender, please say yes.', verbose_name='Do you identify as transgender?')),
                ('man', models.NullBooleanField()),
                ('woman', models.NullBooleanField()),
                ('demi_boy', models.NullBooleanField()),
                ('demi_girl', models.NullBooleanField()),
                ('non_binary', models.NullBooleanField()),
                ('demi_non_binary', models.NullBooleanField()),
                ('genderqueer', models.NullBooleanField(help_text='Do you identify as genderqueer, gender non-conforming, gender diverse, gender varient, or gender expansive? If you are questioning whether you identify with any of those terms, please say yes.', verbose_name='Do you identify as genderqueer?')),
                ('genderflux', models.NullBooleanField()),
                ('genderfluid', models.NullBooleanField()),
                ('demi_genderfluid', models.NullBooleanField()),
                ('demi_gender', models.NullBooleanField()),
                ('bi_gender', models.NullBooleanField()),
                ('tri_gender', models.NullBooleanField()),
                ('multigender', models.NullBooleanField()),
                ('pangender', models.NullBooleanField()),
                ('maxigender', models.NullBooleanField()),
                ('aporagender', models.NullBooleanField()),
                ('intergender', models.NullBooleanField()),
                ('mavrique', models.NullBooleanField()),
                ('gender_confusion', models.NullBooleanField()),
                ('gender_indifferent', models.NullBooleanField()),
                ('graygender', models.NullBooleanField()),
                ('agender', models.NullBooleanField()),
                ('genderless', models.NullBooleanField()),
                ('gender_neutral', models.NullBooleanField()),
                ('neutrois', models.NullBooleanField()),
                ('androgynous', models.NullBooleanField()),
                ('androgyne', models.NullBooleanField()),
                ('prefer_not_to_say', models.NullBooleanField()),
                ('self_identify', models.CharField(blank=True, help_text='If your gender identity is not listed above, please let us know how you identify so we can add it to the list.', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContractorInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typical_hours', models.IntegerField(help_text='During the past three months, what is the average number of hours/week you have spent on contracted work and unpaid business development or business marketing? You will be able to enter your known contract hours for the Outreachy internship period on the next page.', verbose_name='Average number of hours spent on contractor business')),
                ('continuing_contract_work', models.NullBooleanField(verbose_name='Will you be doing contract work during the Outreachy internship period?')),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentTimeCommitment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(help_text='Start date of employment period. Use YYYY-MM-DD format.')),
                ('end_date', models.DateField(help_text='End date of employment period. Use YYYY-MM-DD format.')),
                ('hours_per_week', models.IntegerField(help_text='Number of hours per week required by your employment contract')),
                ('quit_on_acceptance', models.BooleanField(help_text='I will quit this job or contract if I am accepted as an Outreachy intern.')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolTimeCommitment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term_name', models.CharField(help_text='If your university uses term names (e.g. Winter 2018 term of your Sophomore year), enter your current term name, year in college, and term year. If your university uses term numbers (e.g. 7th semester), enter the term number.', max_length=100, verbose_name='Term name or term number')),
                ('start_date', models.DateField(help_text='What is the first possible day of classes for all students?<br>If you started this term late (or will start this term late), use the date that classes start for all students, not the late registration date.<br>If students who are in different school years or different semester numbers start classes on different dates, use the first possible date that students in your year or semester start classes.<br>If you do not know when the term will start, use the start date of that term from last year.', verbose_name='Date classes start. Use YYYY-MM-DD format.')),
                ('end_date', models.DateField(help_text='This is the date your university advertises for the last possible date of any exam for any student in your semester. Use the last possible exam date, even if your personal exams end sooner.', verbose_name='Date all exams end. Use YYYY-MM-DD format.')),
                ('typical_credits', models.IntegerField(help_text='How many credits does a typical student register for?<br> If your university has different credit requirements for each semester for students in your major, use the number of credits that are listed on your syllabus or class schedule.', verbose_name='Number of credits for a typical student')),
                ('registered_credits', models.IntegerField(help_text="What is the total number of credits you are enrolled for this term?<br>If you aren't registered yet, please provide an approximate number of credits?", verbose_name="Number of credits you're registered for")),
                ('outreachy_credits', models.IntegerField(help_text='If you are going to seek university credit for your Outreachy internship, how many credits will you earn?', verbose_name='Number of internship or project credits for Outreachy')),
                ('thesis_credits', models.IntegerField(help_text='If you are a graduate student, how many credits will you earn for working on your thesis or research (not including the credits earned for the Outreachy internship)?', verbose_name='Number of graduate thesis or research credits')),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerTimeCommitment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(help_text='Date your volunteer time commitments start. Use YYYY-MM-DD format.')),
                ('end_date', models.DateField(help_text='Date your volunteer time commitments end. Use YYYY-MM-DD format.')),
                ('hours_per_week', models.IntegerField(help_text='Maximum hours per week spent volunteering.')),
                ('description', models.TextField(blank=True, help_text='Please describe what kind of volunteer position and duties you have.', max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolInformation',
            fields=[
                ('applicant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.ApplicantApproval')),
                ('university_name', models.CharField(help_text='University or college name', max_length=100)),
                ('university_website', models.URLField(help_text='University or college website')),
                ('degree_name', models.CharField(help_text='What degree(s) are you pursuing?', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='volunteertimecommitment',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ApplicantApproval'),
        ),
        migrations.AddField(
            model_name='schooltimecommitment',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ApplicantApproval'),
        ),
        migrations.AddField(
            model_name='employmenttimecommitment',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ApplicantApproval'),
        ),
        migrations.AddField(
            model_name='contractorinformation',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ApplicantApproval'),
        ),
        migrations.AddField(
            model_name='applicantapproval',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Comrade'),
        ),
        migrations.AddField(
            model_name='applicantapproval',
            name='application_round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.RoundPage'),
        ),
        migrations.AlterField(
            model_name='project',
            name='intern_tasks',
            field=ckeditor.fields.RichTextField(blank=True, help_text='(Optional) Description of possible internship tasks.', max_length=3000),
        ),
        migrations.AlterModelOptions(
            name='community',
            options={'verbose_name_plural': 'communities'},
        ),
        migrations.AlterModelOptions(
            name='newcommunity',
            options={'verbose_name_plural': 'new communities'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['slug']},
        ),
        migrations.AlterField(
            model_name='comrade',
            name='pronouns_public',
            field=models.BooleanField(default=False, help_text="Mentor, coordinator, and accepted interns' pronouns will be displayed publicly on the Outreachy website to anyone who is not logged in. Sharing pronouns can be a way for people to proudly display their gender identity and connect with other Outreachy participants, but other people may prefer to keep their pronouns private.<br>If this box is unchecked, Outreachy participants will be instructed to use they/them pronouns on public community channels. They will still know what your pronouns are if you check the previous box.", verbose_name='Share pronouns publicly'),
        ),
        migrations.AlterField(
            model_name='comrade',
            name='pronouns_to_participants',
            field=models.BooleanField(default=True, help_text="If this box is checked, applicant pronouns will be shared with coordinators, mentors and volunteers. If the box is checked, coordinator and mentor pronouns will be shared with applicants.<br>If the box is unchecked, no pronouns will be displayed.<br>If you don't want to share your pronouns, all Outreachy organizer email that Cc's another participant will use they/them/their pronouns for you.", verbose_name='Share pronouns with Outreachy participants'),
        ),
        migrations.AddField(
            model_name='comrade',
            name='blog_rss_url',
            field=models.URLField(blank=True, help_text="(Optional) The full URL to the RSS or ATOM feed for your blog.<br>For mentors and coordinators, this is unused. Applicants' blog RSS URLs will be unused. Accepted interns' blog RSS URLs will be used to create an aggregated feed of all Outreachy intern blogs, which will be displayed on the Outreachy website or Outreachy planetaria.", verbose_name='Blog RSS URL'),
        ),
        migrations.AddField(
            model_name='comrade',
            name='blog_url',
            field=models.URLField(blank=True, help_text="(Optional) The full URL to your blog.<br>For mentors and coordinators, this will be displayed to applicants. Applicants' blog URLs will be shared with their mentors and coordinators. Accepted interns' blog URLs will be displayed on the Outreachy website.", verbose_name='Blog URL'),
        ),
        migrations.AddField(
            model_name='comrade',
            name='github_url',
            field=models.URLField(blank=True, help_text="(Optional) The full URL to your profile on GitHub.<br>For mentors and coordinators, this will be displayed to applicants. Applicants' GitHub URLs will be shared with their mentors and coordinators. Accepted interns' GitHub URLs will be displayed on the Outreachy website.", verbose_name='GitHub profile URL'),
        ),
        migrations.AddField(
            model_name='comrade',
            name='gitlab_url',
            field=models.URLField(blank=True, help_text="(Optional) The full URL to your profile on GitLab.<br>For mentors and coordinators, this will be displayed to applicants. Applicants' GitLab URLs will be shared with their mentors and coordinators. Accepted interns' GitLab URLs will be displayed on the Outreachy website.", verbose_name='GitLab profile URL'),
        ),
        migrations.AddField(
            model_name='comrade',
            name='location',
            field=models.CharField(blank=True, help_text="(Optional) Location - city, state/province, and country.<br>This field is unused for mentors and coordinators. Applicant's location will be shared with their mentors. If selected as an intern, this location will be publicly displayed on the Outreachy website.<br>If you are concerned about keeping your location private, you can share less information, such as just the country, or a larger town nearby.", max_length=100),
        ),
        migrations.AddField(
            model_name='comrade',
            name='nick',
            field=models.CharField(blank=True, help_text="(Optional) The username or 'nick' you typically use when communicating on professional channels. If you don't have one yet, leave this blank and update it later.<br>For mentors and coordinators, this will be displayed to applicants. Applicants' username/nick will be shared with their mentors and coordinators. Accepted interns' username/nick will be displayed on the Outreachy website.", max_length=100, verbose_name='Forum, chat, or IRC username'),
        ),
        migrations.AddField(
            model_name='comrade',
            name='twitter_url',
            field=models.URLField(blank=True, help_text="(Optional) The full URL to your Twitter profile.<br>For mentors and coordinators, this will be displayed to applicants, who may try to contact you via Twitter. Applicants' Twitter URLs will be shared with their mentors and coordinators. Accepted interns' Twitter URLs will be used to create an Outreachy Twitter list for accepted interns for that round. Accepted interns' Twitter URLs will not be displayed on the Outreachy website.", verbose_name='Twitter profile URL'),
        ),
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(help_text="A link to the publicly submitted contribution. The contribution can be work in progress. The URL could a link to a GitHub/GitLab issue or pull request, a link to the mailing list archives for a patch, a Gerrit pull request or issue, a contribution change log on a wiki, a review of graphical design work, a posted case study or user experience study, etc. If you're unsure what URL to put here, ask your mentor.", verbose_name='Contribution URL')),
                ('description', models.TextField(help_text='Description of this contribution for review by the Outreachy coordinators and organizers during intern selection. If you used advanced tools to create this contribution, mention them here.', max_length=3000)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ApplicantApproval')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Project')),
                ('date_merged', models.DateField(blank=True, help_text='If this contribution is still in progress, you can leave this field blank and edit it later.', null=True, verbose_name='Date contribution was accepted or merged (in YYYY-MM-DD format)')),
                ('date_started', models.DateField(verbose_name='Date contribution was started (in YYYY-MM-DD format)')),
            ],
        ),
        migrations.AddField(
            model_name='applicantapproval',
            name='project_contributions',
            field=models.ManyToManyField(through='home.Contribution', to='home.Project'),
        ),
        migrations.CreateModel(
            name='FinalApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.TextField(help_text='Please describe your experience with this free software community and project as a user and as a contributor.', max_length=8000, verbose_name='Experience with this community')),
                ('foss_experience', models.TextField(help_text='Please describe your experience with any other free software projects as a user and as a contributor.', max_length=8000, verbose_name='Experience with other communities')),
                ('relevant_projects', models.TextField(help_text='Please describe any relevant projects (either personal, work, or school projects) that helped you gain skills you will use in this project. Talk about what knowledge you gained from working on them. Include links where possible.', max_length=8000, verbose_name='Relevant Projects')),
                ('timeline', models.TextField(blank=True, help_text='Please work with your mentor to provide a timeline of the work you plan to accomplish on the project and what tasks you will finish at each step. Make sure take into account any time commitments you have during the Outreachy internship round. If you are still working on your contributions and need more time, you can leave this blank and edit your application later.', max_length=8000, verbose_name='Outreachy internship project timeline')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ApplicantApproval')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Project')),
                ('community_specific_questions', models.TextField(blank=True, help_text='Some communities or projects may want you to answer additional questions. Please check with your mentor and community coordinator to see if you need to provide any additional information after you save your project application.', max_length=8000, verbose_name='(Optional) Community-specific Questions')),
                ('approval_status', models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('W', 'Withdrawn'), ('R', 'Rejected')], default='W', max_length=1)),
                ('reason_denied', models.CharField(blank=True, help_text='\n            Please explain why you are withdrawing this request. This\n            explanation will only be shown to Outreachy organizers and\n            approved people within this community.\n            ', max_length=3000)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='finalapplication',
            unique_together=set([('applicant', 'project')]),
        ),
        migrations.AlterField(
            model_name='comrade',
            name='pronouns',
            field=models.CharField(choices=[('she', 'she/her/hers'), ('he', 'he/him/his'), ('they', 'they/them/theirs'), ('fae', 'fae/faer/faers'), ('ey', 'ey/em/eirs'), ('per', 'per/per/pers'), ('ve', 've/ver/vis'), ('xe', 'xe/xem/xyrs'), ('ze', 'ze/hir/hirs')], default='they', help_text="Your preferred pronoun. This will be used in emails from Outreachy organizers directly to you. The format is subject/object/possessive pronoun. Example: '__(subject)__ interned with Outreachy. The mentor liked working with __(object)__. The opportunity was __(possessive pronoun)__ to grab.", max_length=4),
        ),
        migrations.AddField(
            model_name='comrade',
            name='agreed_to_code_of_conduct',
            field=models.CharField(max_length=800, verbose_name='Type your legal name to indicate you agree to the Code of Conduct'),
        ),
        migrations.AddField(
            model_name='community',
            name='tutorial',
            field=ckeditor.fields.RichTextField(blank=True, help_text='(Optional) If your applicants need to complete a tutorial before working on their contributions, please provide a description and the URL for the tutorial'),
        ),
    ]