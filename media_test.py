import base64
import json
from django.core.files.base import ContentFile
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db.models import *


class City(Model):
    name = CharField(max_length=30, primary_key=True, unique=True)
    img = ImageField(upload_to='city/', max_length=225, blank=True, null=True)
    tag_choices = (
        ('food', '美食'),
        ('sea', '海边'),
        ('landform', '地貌'),
        ('hiking', '爬山'),
        ('hillfort', '古城'),
        ('village', '小镇'),
        ('big_city', '都市'),
        ('normal', '普通')
    )
    tag = CharField(max_length=10, choices=tag_choices, blank='normal')


@require_http_methods(['POST'])
def upload_image(request):
    # 获取 JSON 数据
    city_name = request.POST.get('city_name')
    data = request.POST.get('data')

    # 解码 Base64 图片数据
    format, imgstr = data.split(';base64,')
    ext = format.split('/')[-1]
    image = ContentFile(base64.b64decode(imgstr), name=f"{city_name}.{ext}")

    city = City.objects.get(name=city_name)
    city.img.save(image.name, image)
    city.save()

    return JsonResponse({'image_url': city.img.url})


@require_http_methods(['POST'])
def get_image_file(request):
    # 获取 JSON 数据
    city_name = request.POST.get('city_name')
    city = City.objects.get(name=city_name)
    # 读取图片文件并进行 base64 编码
    with open(city.img.path, 'rb') as file:
        image_data = file.read()
        base64_encoded = base64.b64encode(image_data).decode('utf-8')
        image_file_json = json.loads(base64_encoded)

    # 返回 base64 编码后的图片数据给前端
    return JsonResponse({'image_file': image_file_json})


@require_http_methods(['POST'])
def get_image_url(request):
    city_name = request.POST.get('city_name')
    city = City.objects.get(name=city_name)
    return JsonResponse({'image_url': city.img.url})
