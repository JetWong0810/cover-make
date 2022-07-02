#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from config import Config
from render import Render
import os
import csv


def parse_args():
    def add_bool_args(p, name, help):
        p.add_argument('--' + name, dest=name, help=help, action='store_true')
        p.set_defaults(**{name: False})

    parser = ArgumentParser(description='生成书籍封面图片的工具')
    parser.add_argument('-c', '--csv', help='csv 配置文件的路径', required=True)
    parser.add_argument('-o', '--out', help='结果输出文件夹路径', required=True)
    parser.add_argument('-t', '--template', help='模板文件夹路径', required=True)
    add_bool_args(parser, 'show_text_box', '是否显示文本框区域用于调试')

    return parser.parse_args()


def make_output_dir(d):
    if os.path.exists(d):
        if os.path.isdir(d):
            return
        raise Exception('目标输出目录已经存在，但是并非文件夹')
    os.makedirs(d)


def main():
    args = parse_args()
    # 创建输出文件夹
    make_output_dir(args.out)
    # 加载模板配置
    conf = Config(args.template)
    # 加载 csv 文件
    with open(args.csv, 'r') as fp:
        r = csv.DictReader(fp)
        for row in r:
            cover_name = row['cover']
            row.pop('cover')

            render = Render(conf.img.copy())
            for k, v in row.items():
                render.draw(v, conf.get(k), args.show_text_box)

            # 保存图片
            cover_file_path = os.path.join(args.out, cover_name)
            render.save(cover_file_path)


if __name__ == '__main__':
    main()
