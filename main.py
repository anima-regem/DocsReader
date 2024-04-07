import pytesseract
import pdf2image
from PIL import Image
import os

# import ollama

# MODEL_NAME = "gemma"


def run():

    input_pdf_path = input("Enter the path of the pdf: ")
    images = pdf2image.convert_from_path(input_pdf_path)
    print(f"Number of pages: {len(images)}")
    if not os.path.exists("outputs"):
        os.mkdir("outputs")
    os.chdir("outputs")
    folder_name = input_pdf_path.split("/")[-1].split(".")[0]
    if not os.path.exists(f"{folder_name}__images"):
        os.mkdir(f"{folder_name}__images")
    os.chdir(f"{folder_name}__images")
    for i in range(len(images) - 1):
        if not os.path.exists(f"page_{i}"):
            os.mkdir(f"page_{i}")
        os.chdir(f"page_{i}")
        images[i].save(f"page_{i}.jpg", "JPEG")
        img = Image.open(f"page_{i}.jpg")
        text = pytesseract.image_to_string(img)

        with open(f"page_{i}.txt", "w") as f:
            f.write(text)

        # print()
        # print("Generating Content...")
        # print()
        # stream = ollama.generate(
        #     model=MODEL_NAME,
        #     prompt=
        #             f"Structure the medical record of the patient to plain text {text}",
        #     stream=True,
        # )
        # print()
        # print("---------------------------------------")
        # print()

        # for chunk in stream:
        #     print(chunk['response'], end='', flush=True)
        # print()
        os.chdir("..")
    print()


def convert_pdf_to_text(filename):
    input_pdf_path = filename
    images = pdf2image.convert_from_path(input_pdf_path)
    print(f"Number of pages: {len(images)}")
    if not os.path.exists("outputs"):
        os.mkdir("outputs")
    os.chdir("outputs")
    folder_name = input_pdf_path.split("/")[-1].split(".")[0]
    if not os.path.exists(f"{folder_name}__images"):
        os.mkdir(f"{folder_name}__images")
    os.chdir(f"{folder_name}__images")
    image_list = []
    for i in range(len(images) - 1):
        if not os.path.exists(f"page_{i}"):
            os.mkdir(f"page_{i}")
        os.chdir(f"page_{i}")
        images[i].save(f"page_{i}.jpg", "JPEG")
        img = Image.open(f"page_{i}.jpg")
        text = pytesseract.image_to_string(img)

        with open(f"page_{i}.txt", "w") as f:
            f.write(text)

        image_list.append(f"{folder_name}__images/page_{i}/page_{i}.txt")
    return image_list


if __name__ == "__main__":
    run()
