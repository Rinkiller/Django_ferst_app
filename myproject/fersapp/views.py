# Задание
# Создайте пару представлений в вашем первом приложении:
# — главная
# — о себе.

# Внутри каждого представления должна быть переменная html — многострочный текст с HTML-вёрсткой и данными о вашем первом Django-сайте и о вас.

# Сохраняйте в логи данные о посещении страниц.




from django.shortcuts import render
import logging
import random

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename='fersapp.log', filemode='a', format='%(levelname)s %(message)s')


from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world!")
def about(request):
    return HttpResponse("About us")

def coin(request):
    return HttpResponse(random.choice(['орел','решка']))

def kub(request):
    rand_int = random.randrange(1,7)
    logger.info(f'Рандомное число от 1 до 6 равно {rand_int} ')
    return HttpResponse(f'Рандомное число от 1 до 6 равно {rand_int} ')
def main(request):
    return HttpResponse("<center><h1>Main page</h1><p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Veniam odio consectetur eius sit autem totam accusantium labore, quae obcaecati cum dolorem aperiam praesentium corrupti consequuntur maiores, placeat ut quo qui distinctio magni! Modi delectus reprehenderit, voluptatum error aperiam beatae consequuntur nostrum officia neque dolores repudiandae molestias atque, quam porro nihil! Eveniet dignissimos animi, accusantium eos necessitatibus iusto eum similique nihil iure. Quis nemo, ducimus, ab rem necessitatibus rerum, quibusdam ratione quia similique dolore blanditiis eos dignissimos. Ea neque, maxime laudantium maiores veniam praesentium sequi eius porro minima, quam, nemo corrupti at repellat natus aliquid consequatur itaque ex ab reprehenderit laborum repellendus assumenda dolor. Ipsam, earum temporibus consectetur pariatur cumque quaerat ab perferendis corporis enim doloribus repudiandae. Soluta odio adipisci officiis atque fuga sed excepturi neque voluptatum necessitatibus! Numquam veritatis expedita corrupti modi qui temporibus blanditiis veniam! Libero eos, illum temporibus repellendus sapiente iste blanditiis quisquam quasi, ex praesentium dolore. Sapiente distinctio temporibus dolorem quidem voluptatum vero similique praesentium ipsam tempore consectetur delectus quibusdam aspernatur assumenda voluptatem, earum omnis numquam quis, quos eaque corporis eveniet labore. Magnam dignissimos in quaerat earum. Voluptates veniam debitis voluptatum voluptas nihil vero deserunt mollitia iure dolor delectus. Adipisci illo nobis facilis exercitationem quia ut dolorum.</p></center>")


def about_me(request):
    return HttpResponse("<center><h1>about me</h1><p>Илькин Ринат Фирдаусович </p><p>возраст: 38 лет</p><p>по профессии военный(офицер)</p><p>программированием занимаюсь с детства</p><p>воспитываю двоих детей(пацаны)</p></center>")

