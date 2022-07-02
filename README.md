# cover_maker

一个 python 的小工具。可以将文本和图片按照一些排版规则合成通用的封面图。

## 文件功能介绍

* [cover_maker.py](cover_maker.py) 命令行工具入口
* [config.py](config.py) 加载配置模板配置
* [render.py](render.py) 合成图片用的模块
* [layout.py](layout.py) 文本框内文字排版
* [test.csv](test.csv) 测试数据
* fonts 目录，存放字体的目录
* template 存放示例模板配置的目录

## 命令行使用方法

使用python3进行开发，依赖 Pillow，具体版本写在了 [pip-req.txt](pip-req.txt) 中

### 查看命令行帮助
```bash
python3 ./cover_maker.py --help
```

### 使用示例
例如使用 **模板 1** 输出测试结果到 **/tmp/covers/1** 目录
```bash
python3 ./cover_maker.py -o /tmp/covers/1 -t ./template/1 -c test.csv
```

可以选加 **--show_text_box** 参数。加上后可以在合成的图片上看到文本框边框

## 扩展模板

拷贝 **template** 目录下的任意一个模板目录，修改其中的图和 **conf.ini** 文件</br>
中的配置。配置中有详细的说明每个参数的含义。

## 增加字体

将字体放到 **fonts** 目录下，在需要使用的模板配置中指定字体的 basename
