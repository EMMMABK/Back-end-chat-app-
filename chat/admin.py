from django.contrib import admin
from .models import ChatRoom, Messages, ChatParticipantsChannel, ChatRoomParticipants
# Register your models here.
admin.site.register(ChatRoomParticipants)
admin.site.register(ChatRoom)
admin.site.register(Messages)
admin.site.register(ChatParticipantsChannel)
