from pypdf import PdfMerger

pdfs = [
    'utils/files/p1-2.pdf',
    'utils/files/p3.pdf',
    'utils/files/p4.pdf',
    'utils/files/p5.pdf'
    ]
pdfs.append('utils/files/p6-15.pdf')
pdfs.append('utils/files/p16.pdf')
pdfs.append('utils/files/p17.pdf')
pdfs.append('utils/files/p18.pdf')
pdfs.append('utils/files/p19.pdf')

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("utils/files/result.pdf")
merger.close()
