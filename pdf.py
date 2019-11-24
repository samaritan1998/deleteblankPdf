from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from PyPDF2 import PdfFileReader, PdfFileWriter
import PyPDF2
#获取文档对象
fp=open("E:/pre.pdf","rb")
#创建一个与文档关联的解释器
parser=PDFParser(fp)

#PDf文档的对象
doc=PDFDocument(parser)

#链接解释器和文档对象
parser.set_document(doc)


#创建PDF资源管理器
resource=PDFResourceManager()

#参数分析器
laparam=LAParams()
#创建一个聚合器
device=PDFPageAggregator(resource,laparams=laparam)
#创建PDF页面解释器
interpreter=PDFPageInterpreter(resource,device)
original_pdf = PyPDF2.PdfFileReader("E:/pre.pdf") # 调用读取功能
page = original_pdf.getPage(0) # 读取第一页内容
pdfWriter = PyPDF2.PdfFileWriter()  # 调用写入功能
pdfWriter.addPage(page)

#使用文档对象得到页面的集合
i=0
pdfWriter = PyPDF2.PdfFileWriter()  # 调用写入功能
for page in PDFPage.create_pages(doc):
    #使用页面解释器来读取
    interpreter.process_page(page)

    #使用聚合器来获得内容
    layout=device.get_result()
    flag=0
    for out in layout:
        if hasattr(out, 'get_text'):  # 需要注意的是在PDF文档中不只有 text 还可能有图片等等，为了确保不出错先判断对象是否具有 get_text()方法
            #print(out.get_text())
            flag=1
            break
    if flag==1:
        page = original_pdf.getPage(i)  # 读取第一页内容
        pdfWriter.addPage(page)
    i+=1
 # 写入新文件
with open("E:/after.pdf", 'wb') as f:
    pdfWriter.write(f)

