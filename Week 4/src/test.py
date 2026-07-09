from src.rag import answer_question


while True:

    q = input("\nAsk: ")


    answer, sources = answer_question(q)


    print(
        "\nANSWER:\n"
    )

    print(answer)


    print(
        "\nSOURCES:"
    )


    for source in sources:

        print(
            "-",
            source
        )