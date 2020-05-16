from django.shortcuts import render
from .forms import PictureForm
from .models import ImagePic
from transfer.settings import BASE_DIR, MEDIA_ROOT
from transferapp.transfer_style.model import *




def name_img(name_style, name_content):
    name_img = str(name_style) + str(name_content)
    return name_img

def load_and_send_pic(style_img_path, content_img_path):
    go = StyleTransferModel()
    img = go.start_learning(style_img_path, content_img_path)
    name = name_img(style_img_path, content_img_path)
    direct_img = MEDIA_ROOT + name
    img.save(direct_img)


def pic_result(request):
    image = ImagePic.objects.all()
    #image.delete()
    #image_result.delete()
    return render(request, 'view_pic.html', {"image": image})


def index(request):
    pictureform = PictureForm()
    if request.method == "POST":
        image = ImagePic()
        pictureform = PictureForm(request.POST, request.FILES)
        if pictureform.is_valid():
            content = pictureform.cleaned_data["content"]
            style = pictureform.cleaned_data["style"]
            image_result_url = name_img(style, content)
            image, created = ImagePic.objects.get_or_create(content=content,
                                                            style=style,
                                                            result=image_result_url)

            print(image.content)
            load_and_send_pic(image.style, image.content)
            print(image_result_url)
        return render(request, 'view_pic.html', {"image": image})
    return render(request, 'index.html', {"pictureform": pictureform})




