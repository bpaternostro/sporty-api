from django import template

from googletrans import Translator, constants

from ...main.models import Language

register = template.Library()

@register.simple_tag
def translate_day(day, lang):
    """translate day"""
    return day.daylang_set.filter(lang_id=lang).get().translation


@register.simple_tag
def translate_exercise_name(exercise, lang):
    """translate exerciselang"""
    return exercise.exerciselang_set.filter(lang_id=lang).get().translation


@register.simple_tag
def translate_text(text, lang):
    """translate text"""
    if text:
        translator = Translator()
        lang = Language.objects.get(id=lang)
        traslation = translator.translate(text, dest=lang.code)
        return traslation.text