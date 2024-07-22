from openai import OpenAI
import base64

client = OpenAI(api_key="")
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

base64_image = encode_image("image.png")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that responds in plain text. Help me with my math homework!"},
        {"role": "user", "content": [
            {"type": "text", "text": "What's the area of the shape in this image?"},
            {"type": "image_url", "image_url": {
                "url": f"data:image/png;base64,{base64_image}"}
             }],
        }
        ]
)
print(response.choices[0].message.content)