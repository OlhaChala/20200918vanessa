from django.contrib.auth.models import User
user = User.objects.create_user(username='chatbotVanessa',
                                 password='UserVanessa')