from django import template
import re

register = template.Library()

# Список нежелательных слов, которые нужно заменить
UNWANTED_WORDS = ['Плохой', 'Ужасный']

@register.filter
def censor(value):
    # Проход по списку нежелательных слов и их замена на '*'
    for word in UNWANTED_WORDS:
        value = re.sub(word, '*' * len(word), value, flags=re.IGNORECASE)
    return value
