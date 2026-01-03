import requests
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO
from config import HF_API_KEY

def generate_image_from_text(prompt):
    """
    Generates an image from a text prompt using the Stable Diffusion API.
    """
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": prompt}
    
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        return image
    else:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")


#Def 









def main():
    print("Welcome to the Post-Processing Magic Workshop!")
    print("This program generates an image from text and applies post-processing effects.")
    print("Type 'exit' to quit.\n")
    
    while True:
        user_input = input("Enter a description for the image (or 'exit' to quit):\n")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        try:
            print("\nGenerating image...")
            image = generate_image_from_text(user_input)
            print("Applying post-processing effects...\n")
            processed_image = post_process_image(image)
            processed_image.show()  # Display the processed image
            
            save_option = input("Do you want to save the processed image? (yes/no): ").strip().lower()
            if save_option == 'yes':
                file_name = input("Enter a name for the image file (without extension): ").strip()
                processed_image.save(f"{file_name}.png")
                print(f"Image saved as {file_name}.png\n")
            print("-" * 80 + "\n")
        except Exception as e:
            print(f"An error occurred: {e}\n")

if __name__ == "__main__":
    main()




