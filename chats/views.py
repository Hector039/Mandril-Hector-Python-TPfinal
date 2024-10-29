from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages as info
from users.models import CustomUser
from .models import Message, ChatRegister
from .forms import MessageForm
from django.db.models import Q
   
@login_required
def getUserMsgs(req, uid=None):
    try:
        fromUser = get_object_or_404(CustomUser, pk=req.user.id)
        messageForm = MessageForm()
        chats = ChatRegister.objects.filter(Q(user1_id=fromUser) | Q(user2_id=fromUser))

        if uid is None:
            return render(req, "msg-detail.html", {"avatar_url": req.session["avatar_path"], "last_login": req.session["last_login"], "channels": chats})
        
        toUser = get_object_or_404(CustomUser, pk=uid)
        chat = ChatRegister.objects.filter(Q(user1_id=fromUser, user2_id=toUser) | Q(user1_id=toUser, user2_id=fromUser))
        
        if len(chat) == 0:
            newChat = ChatRegister.objects.create(user1_id=fromUser, user2_id=toUser)
            chat = ChatRegister.objects.filter(pk=newChat.id)

        if req.method == 'POST':
            Message.objects.create(chat_id=chat[0], to_id=toUser, from_id=fromUser, message=req.POST["message"])
            messages = Message.objects.filter(Q(to_id=fromUser, from_id=toUser) | Q(to_id=toUser, from_id=fromUser)).order_by('date')

            info.success(req, "Message send!")
            return render(req, "msg-detail.html", {"avatar_url": req.session["avatar_path"], "last_login": req.session["last_login"], "form": messageForm, "chats": messages, "to": toUser.id, "to_user": f"{toUser.first_name} {toUser.last_name}:", "channels": chats})
        
        messages = Message.objects.filter(Q(to_id=fromUser, from_id=toUser) | Q(to_id=toUser, from_id=fromUser)).order_by('date')

        Message.objects.filter(Q(chat_id=chat[0], to_id=fromUser, seen=False)).update(seen=True)

        return render(req, "msg-detail.html", {"avatar_url": req.session["avatar_path"], "last_login": req.session["last_login"], "form": messageForm, "chats": messages, "to": toUser.id, "to_user": f"{toUser.first_name} {toUser.last_name}", "channels": chats})
    except Exception as error:
        info.error(req, error)
        return render(req, "msg-detail.html", {"avatar_url": req.session["avatar_path"], "last_login": req.session["last_login"], "channels": chats})