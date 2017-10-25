from .models import SmsPage
from wagtail_modeltranslation.translation import TranslationOptions
from modeltranslation.decorators import register


@register(SmsPage)
class FooTR(TranslationOptions):
    fields = (
        'message',
    )
