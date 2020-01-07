from twitter.models import *
from twitter.views import views
import  random
import string

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def generate_like_id(instance):
    new_like_id=random_string_generator()
    klass=instance.__class__
    qs_exists = Klass.objects.filter(like_id=order_new_id).exists()
    if qs_exists:
        return random_order_id_generator(instance)
    return like_id
