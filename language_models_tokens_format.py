from client import client, model


def get_response_with_messages(
    messages,
    temperature: float = 0,
    max_output_tokens: int = 500,
):
    """
    Envia uma conversa completa (system + user + outros turnos)
    usando o formato canônico da Responses API.
    """

    response = client.responses.create(
        model=model,
        input=[
            {
                "role": msg["role"],
                "content": [
                    {
                        "type": "input_text",
                        "text": msg["content"]
                    }
                ],
            }
            for msg in messages
        ],
        temperature=temperature,
        max_output_tokens=max_output_tokens,
    )

    content = response.output_text

    usage = response.usage
    token_dict = {
        "input_tokens": getattr(usage, "input_tokens", None),
        "output_tokens": getattr(usage, "output_tokens", None),
        "total_tokens": getattr(usage, "total_tokens", None),
    }

    return content, token_dict


if __name__ == "__main__":
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant that explains concepts simply."
        },
        {
            "role": "user",
            "content": "Explain the theory of relativity in simple terms."
        }
    ]

    content, token_count = get_response_with_messages(messages)

    print("Response:")
    print(content)

    print("\nToken usage:")
    print(token_count)
