# from pdz.workers.models import Operator
# from django.contrib.auth.models import Group
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# 
# 
# @receiver(post_save, sender=Operator)
# def assign_expert_group(sender, instance, created, **kwargs):
#     if created:
#         consulenti_group = Group.objects.get_or_create(name="Consulenti")
#         consulenti_group[0].user_set.add(instance)
        
        