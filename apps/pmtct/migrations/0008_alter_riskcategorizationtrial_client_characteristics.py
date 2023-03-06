# Generated by Django 3.2.5 on 2023-03-04 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmtct', '0007_alter_riskcategorizationtrial_client_characteristics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riskcategorizationtrial',
            name='client_characteristics',
            field=models.CharField(choices=[('1. Is the client a newly HIV Positive (<3mnths)', '1. Is the client a newly HIV Positive (<3mnths)'), ('2. (a) Is the client an adolescent <19 years of age?', '2. (a) Is the client an adolescent <19 years of age?'), ('2. (b) Is the client an adolescent @ School>20yrs', '2. (b) Is the client an adolescent @ School>20yrs'), ('3. Is the client’s current VL >200 copies/ml', '3. Is the client’s current VL >200 copies/ml'), ('4. (a) Client has poor adherence : Delayed ART', '4. (a) Client has poor adherence : Delayed ART'), ('4. (b) Client has poor adherence : Missed >1 clinic appointments in the last scheduled 3 visits', '4. (b) Client has poor adherence : Missed >1 clinic appointments in the last scheduled 3 visits'), ('4. (c) Client has poor adherence : LTFU/IIT', '4. (c) Client has poor adherence : LTFU/IIT'), ('4. (d) Client has poor adherence : Declined ART', '4. (d) Client has poor adherence : Declined ART'), ('4. (e) Client has poor adherence : Missed ART doses', '4. (e) Client has poor adherence : Missed ART doses'), ('5. The client NOT disclosed to partner', '5. The client NOT disclosed to partner'), ('6. Does the client have any social family issues and/or severe poverty that could hinder optimal adherence or other related issues', '6. Does the client have any social family issues and/or severe poverty that could hinder optimal adherence or other related issues'), ('7. Is the client experiencing intimate partner violence or at risk of intimate partner violence?', '7. Is the client experiencing intimate partner violence or at risk of intimate partner violence?'), ('8. Does the client have active comorbidities? TB, DM, OIs, painful, swollen/cracked nipples, etc.', '8. Does the client have active comorbidities? TB, DM, OIs, painful, swollen/cracked nipples, etc.'), ('9. Is the client a lost to follow up/IIT who has returned to care', '9. Is the client a lost to follow up/IIT who has returned to care'), ('10. Client has malnourished HEI; SAM, MAM.', '10. Client has malnourished HEI; SAM, MAM.'), ('11. Does the client have a mental disability or require close care? Use PHQ9 to assess', '11. Does the client have a mental disability or require close care? Use PHQ9 to assess')], max_length=200),
        ),
    ]
