from pypdf import PdfReader
import os


def load_documents(folder):

    docs=[]

    for filename in os.listdir(folder):

        if filename.endswith(".pdf"):

            path=os.path.join(
                folder,
                filename
            )


            reader=PdfReader(path)

            text=""

            for page in reader.pages:

                extracted=page.extract_text()

                if extracted:
                    text += extracted


            docs.append({
                "source":filename,
                "text":text
            })


    return docs