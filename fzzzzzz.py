
import cohere  
co = cohere.Client("m8vMj1QC1zihiYEPEYbnSU4sPwptj61qUKoWXnv4")

prompt = "اخبرني عن حياة البىت اينشتاين."

response = co.generate(  
    model='command-nightly',  
    prompt = prompt,  
    max_tokens=200,  
    temperature=0.750)

intro_paragraph = response.generations[0].text

print(intro_paragraph)
