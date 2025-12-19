from client import client, model
from language_models_tokens_format import get_response_with_messages


delimiter = "####" # Define a delimiter for separating text segments (uses 1 token only)

system_message = f"""
You will be provided with customer service queries. \
The customer service query will be delimited with \
{delimiter} characters.
Classify each query into a primary category \
and a secondary category. 
Provide your output in json format with the \
keys: primary and secondary.

Primary categories: Billing, Technical Support, \
Account Management, or General Inquiry.

Billing secondary categories:
Unsubscribe or upgrade
Add a payment method
Explanation for charge
Dispute a charge

Technical Support secondary categories:
General troubleshooting
Device compatibility
Software updates

Account Management secondary categories:
Password reset
Update personal information
Close account
Account security

General Inquiry secondary categories:
Product information
Pricing
Feedback
Speak to a human

"""

user_message = f"""\
I want to delete my profile and all of my user data from our system. \
"""

messages = [
    {
        "role": "system",
        "content": system_message,
    },
    {
        "role": "user",
        "content": f"{delimiter}\n{user_message}\n{delimiter}",
    },

    ]


if __name__ == "__main__":
    """
    Example of classifying a customer service query into primary and secondary categories then returning a json.
    """
    content, token_count = get_response_with_messages(messages)

    print("Response:")
    print(content)
    print("Token count:")
    print(token_count)
    # Response:
    # ```json
    # {
    #     "primary": "Account Management",
    #     "secondary": "Close account"
    # }
    # ```