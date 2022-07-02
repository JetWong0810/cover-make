#coding: utf-8
from os import path
from configparser import ConfigParser
from PIL import Image


def _load_conf(template_dir):
    conf = ConfigParser()
    conf_dir = path.join(template_dir, 'conf.ini')
    conf.read(conf_dir)
    return conf


def _load_img(template_dir, section):
    # 加载图片。需要注意转换图片的格式。png调色板将不能正确
    # 绘制调试用的边框
    img_path = path.join(template_dir, section['url'])
    return Image.open(img_path).convert('RGB')


class Box(object):
    def __init__(self, x, y, w, h):
        self.lt = (x, y)  # 左上角
        self.rb = (x + w, y + h)  # 右下角
        self.w, self.h = w, h  # 宽和高


class Section(object):
    def __init__(self, section, imgw, imgh):
        self.font = section['font']  # 字体文件的名字
        self.color = section['color']  # 16进制的字体颜色
        self.trim = section.getboolean('trim')  # 是否自动截断文本。
        self.dir = section['dir']  # 显示方向 h 表示横向，v 表示纵向
        self.line_spacing_factor = section.getfloat('line_height') - 1  # 行间距
        self.letter_spacing_factor = section.getfloat(
            'letter_spacing') - 1  # 字间距
        # 获取文本对齐方式
        align = section['align']
        self.valign = align[0]  # 文本在框内的垂直对齐方式。l/r/c 分别表示 左/右/中
        self.halign = align[1]  # 文本在框内的垂直对齐方式。t/b/c 分别表示 上/下/中
        # 获取文本显示区域
        b = [float(x) for x in section['box'].split(',')]
        self.box = Box(int(b[0] * imgw), int(b[1] * imgh), int(b[2] * imgw),
                       int(b[3] * imgh))


class Config(object):
    '''
    用于加载模板配置
    '''
    def __init__(self, template_dir):
        # 加载模板配置文件
        self._conf = _load_conf(template_dir)
        # 加载图像，用的时候应该从该图像进行拷贝
        self.img = _load_img(template_dir, self._conf['cover'])
        # 加载标题和作者的配置
        self._sections = {}

    def get(self, key):
        v = self._sections.get(key)
        conf = self._conf
        if v is None:
            if not conf.has_section(key):
                raise Exception('配置中不存在 %s 相关的信息' % key)

            v = Section(conf[key], self.img.width, self.img.height)
            self._sections[key] = v
        return v
