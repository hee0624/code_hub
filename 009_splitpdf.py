#!/usr/bin/env python
# coding=utf-8

from PyPDF2 import PdfFileReader, PdfFileWriter
import fire
import os

# PDF文件分割
def split_pdf(read_file, out_detail):
    try:
        fp_read_file = open(read_file, 'rb')
        pdf_input = PdfFileReader(fp_read_file)
        page_count = pdf_input.getNumPages()
        print(page_count)
        with open(out_detail, 'r') as fp:
            for detail in fp:
                pages, write_file = detail.split()
                write_file, write_ext = os.path.splitext(write_file)
                pdf_file = f'{write_file}.pdf'
                start_page, end_page = pages.split('-')
                try:
                    print(f'开始分割{start_page}页-{end_page}页，保存为{pdf_file}......')
                    pdf_output = PdfFileWriter()
                    for i in range(int(start_page), int(end_page)):
                        pdf_output.addPage(pdf_input.getPage(i))
                    with open(pdf_file, 'wb') as sub_fp:
                        pdf_output.write(sub_fp)
                    print(f'完成分割{start_page}页-{end_page}页，保存为{pdf_file}!')
                except IndexError:
                    print(f'分割页数超过了PDF的页数')
    except Exception as e:
        print(e)
    finally:
        fp_read_file.close()



def main():
    fire.Fire(split_pdf)

if __name__ == '__main__':
    main()