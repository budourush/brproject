from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.


class Top(generic.FormView):
    form_class = ContactForm
    success_url = reverse_lazy('contact:thanks')
    template_name = 'contact/top.html'

    # フォームの内容取得
    # データ検証に問題がない場合に呼ばれるメソッド
    def form_valid(self, form):
        subject = 'お問い合わせがありました'
        message = render_to_string('contact/mail.txt', form.cleaned_data, self.request)

        from_email = 'aa@gmail.com'
        recipient_list = ['aa@gmail.com']
        send_mail(subject, message, from_email, recipient_list)
        return redirect('contact:thanks')

    # クラス汎用ビューをメソッドで上書き
    def get_initial(self):
        return {
            'name': '匿名',
        }


class Thanks(generic.TemplateView):
    template_name = 'contact/thanks.html'
