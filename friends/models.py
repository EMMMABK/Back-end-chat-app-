from django.db import models

# Create your models here.
from webbrowser import get
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class FriendList(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
	friends = models.ManyToManyField(User, blank=True, related_name="friends") 

	def __str__(self):
		return self.user.username

	def add_friend(self, account):
		if not account in self.friends.all():
			self.friends.add(account)
			self.save()

	def remove_friend(self, account):
		if account in self.friends.all():
			self.friends.remove(account)

	def unfriend(self, removee):
		remover_friends_list = self 
		remover_friends_list.remove_friend(removee)
		friends_list = FriendList.objects.get(user=removee)
		friends_list.remove_friend(remover_friends_list.user)


class FriendRequest(models.Model):
	sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
	receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
	is_active = models.BooleanField(blank=False, null=False, default=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.sender.username
	def accept(self):
		receiver_friend_list = FriendList.objects.get_or_create(user=self.receiver)
		print(receiver_friend_list[0])
		if receiver_friend_list:
			receiver_friend_list[0].add_friend(self.sender)
			sender_friend_list = FriendList.objects.get_or_create(user=self.sender)
			if sender_friend_list:
				sender_friend_list[0].add_friend(self.receiver)
				self.is_active = False
				self.save()

	def decline(self):
		self.is_active = False
		self.save()


	def cancel(self):
		self.is_active = False
		self.save()