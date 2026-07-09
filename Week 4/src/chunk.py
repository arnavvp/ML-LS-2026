def chunk_documents(
        docs,
        max_chars=300,
        overlap=150
    ):

    chunks = []


    for doc in docs:

        paragraphs = doc["text"].split("\n")


        current_chunk = ""


        for para in paragraphs:

            para = para.strip()


            if not para:
                continue


            if len(current_chunk) + len(para) > max_chars:


                if current_chunk.strip():

                    chunks.append(
                        {
                            "source": doc["source"],
                            "text": current_chunk.strip()
                        }
                    )


                current_chunk = (
                    current_chunk[-overlap:]
                    + "\n"
                    + para
                )


            else:

                current_chunk += (
                    "\n" + para
                )


        if current_chunk.strip():

            chunks.append(
                {
                    "source": doc["source"],
                    "text": current_chunk.strip()
                }
            )


    return chunks