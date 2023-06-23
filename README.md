# Hackathon

How to call endpoint?

POST http://127.0.0.1:5000/getResponse
body:
{
    "contact":"\"USER: What is the request from sender for below email? Also what is the issue the sender is facing? Tell in less than 10 words. Hello Team, My name is Vishnu Sharma and I'm reaching out on behalf of Godrej Professional, the largest hair care products manufacturer company in India. Does accept guest post contributions? I'm currently working on an article that I think would be a great fit for your audience. It’s about hair care routine, which I think would be a good resource for your readers. I've written for previous blogs such as timesofindia.com and ndtv.com Please let me know if you're interested so we can discuss this further. Have a Productive Wednesday! \nASSISTANT: \""
}

response
{
    "outputs": [
        "Sender wants to submit guest post related to hair care routine. Interested in publishing it on the blog.\""
    ]
}