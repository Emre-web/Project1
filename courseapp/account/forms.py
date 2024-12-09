from django.contrib.auth.forms import UserCreationForm, AuthenticationForm    
from django.forms import widgets
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = widgets.TextInput(attrs={"class": "form-control"})
        self.fields["password"].widget = widgets.PasswordInput(attrs={"class": "form-control"})
        #bu kod ile formun görünümünü değiştirebiliriz. kod bloğu açıklaması: formun görünümünü değiştirmek için formun alanlarını değiştiriyoruz.
        #form alanlarını değiştirmek için widgets modülünden TextInput ve PasswordInput sınıflarını kullanıyoruz.
        #TextInput sınıfı, bir metin giriş alanı oluştururken PasswordInput sınıfı ise bir şifre giriş alanı oluşturur.
        #attrs parametresi, widget'ın HTML özelliklerini belirtmek için kullanılır. Bu örnekte, form alanlarının class özelliği form-control olarak ayarlanmıştır.
        #Bu, form alanlarının Bootstrap'te tanımlanan form-control sınıfını kullanmasını sağlar.    


    def clean_username(self):
        username = self.cleaned_data.get("username")

        if username == "emrey":
            messages.add_message(self.request, messages.SUCCESS, "Hoş geldin {}".format(username))

        return username  # Ensure all usernames are returned, not just "emrey"
        
    # def confirm_login_allowed(self, user):
    #     if user.username.startswith("a"):
    #         raise forms.ValidationError("Username is not allowed.")
    #eğer kullanıcı adı "a" ile başlıyorsa, bir hata mesajı döndürür. Bu hata mesajı, formun hata mesajları listesine eklenir ve formun temsil edildiği sayfada gösterilir.

class  NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email",)


    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields["password1"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["password2"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["username"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["email"].widget = widgets.EmailInput(attrs={"class":"form-control"}) 
        self.fields["email"].required = True
        

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email = email).exists():
            self.add_error("email", "email daha önce kullanılmış")

        return email 
    

class  UserPasswordChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields["new_password1"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["new_password2"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["old_password"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
  