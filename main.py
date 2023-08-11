import requests
import ctypes
from PIL import Image, ImageDraw
import time
from plyer import notification

Image.MAX_IMAGE_PIXELS = None
# user32 = ctypes.windll.user32
# screen_width = user32.GetSystemMetrics(0)
# screen_height = user32.GetSystemMetrics(1)
# print("当前屏幕分辨率为：{}x{}".format(screen_width, screen_height))
# root.mainloop()

# download_image(image_url, file_name)

# 下载卫星图片
def download_jpg(file_name):
    response = requests.get('http://img.nsmc.org.cn/CLOUDIMAGE/FY4B/AGRI/GCLR/FY4B_DISK_GCLR.JPG')
    with open(file_name, "wb") as file:
        file.write(response.content)


# 获取屏幕分辨率
def get_screen():
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)
    info = {
        'width': screen_width,
        'height': screen_height
    }
    return info

# 获取图像像素
def get_imginfo(file_name):
    image = Image.open(file_name)
    width, height = image.size
    return (width, height)

def suofangjpg(file_name):
    jpginfo = get_imginfo(file_name)
    screeninfo = get_screen()
    ratio = min(screeninfo['width'] / jpginfo[0], screeninfo['height'] / jpginfo[1])
    new_weight = int(jpginfo[0]*ratio)
    new_height = int(jpginfo[1] * ratio)
    oldimage = Image.open(file_name)
    newimage = oldimage.resize((new_weight, new_height))
    newimage.save(file_name)


def mubu(screen):
    width = screen['width']
    height = screen['height']

    image = Image.new('RGB',(width, height), (0, 0, 0))
    image.save('img/background.jpg')

# mubu(get_screen())

def heceng_jpg(file_name_1, file_name_2):
    background_img = Image.open(file_name_2)
    foreground_img = Image.open(file_name_1)

    # 计算前景图像放置的位置
    x = (background_img.width - foreground_img.width) // 2
    y = (background_img.height - foreground_img.height) // 2

    # 将前景图像居中放置到背景图像上
    background_img.paste(foreground_img, (x, y))

    # 显示合成后的图像
    # background_img.show()

    # 保存合成后的图像
    background_img.save("img/new.jpg")


def crop_circle(image_path, output_path):
    # 打开图像
    image = Image.open(image_path)

    # 创建一个与图像大小相同的透明图层
    mask = Image.new('L', image.size, 0)

    # 创建一个绘图对象，并在图层上绘制圆形
    width, height = image.size
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, width, height), fill=255)

    # 将图像应用到掩膜上，只保留圆形区域
    result = Image.new('RGB', image.size)
    result.paste(image, mask=mask)

    # 保存结果图像
    result.save(output_path)

# 调用函数来裁剪出圆形图像
# image_path = 'img/image.jpg'  # 输入图像的路径
# output_path = 'img/output.jpg'  # 输出图像的路径
# crop_circle(image_path, output_path)


def set_wallpaper(image_path):
    # 调用 Windows API 函数来设置壁纸
    image = Image.open(image_path)
    image.save("img/wallpaper.bmp", "BMP")
    # ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\Users\guosh\Desktop\FengYunjpg\img\wallpaper.bmp", 3)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\软件\风云壁纸\img\wallpaper.bmp", 3)




# def show_message(state):
#     message_info = {
#         'ok': ['风云4B卫星壁纸', '壁纸切换成功。'],
#         'no': ['风云4B卫星壁纸', '壁纸切换失败。']
#     }
#     notification.notify(
#         title=message_info[state][0],
#         message=message_info[state][1],
#         timeout=2
#     )
#
# message_info = {
#     'ok':['风云4B卫星壁纸', '壁纸切换成功。'],
#     'no':['风云4B卫星壁纸', '壁纸切换失败。']
# }

while True:
    try:
        download_jpg('img/image.jpg')
        suofangjpg('img/image.jpg')
        crop_circle('img/image.jpg', 'img/image.jpg')
        mubu(get_screen())
        heceng_jpg('img/image.jpg', 'img/background.jpg')
        set_wallpaper('img/new.jpg')
        # show_message('ok')
        time.sleep(3600)
    except:
        # show_message('no')
        time.sleep(600)
        continue
