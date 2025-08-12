import os
import gradio as gr
from pycrucible import CrucibleClient, SecureInput

def greet(name):
    return "Hello " + name + "!"

client = CrucibleClient(api_url = 'https://crucible.lbl.gov/testapi/', api_key = os.getenv('CRUCIBLE_API_KEY'))

def list_datasets(sample_id: str):
	ds = client.list_datasets(sample_id)
	print(ds)
	return(ds)

def show_thumbnails(crucible_dataset_id):
    from PIL import Image
    import base64
    import io
    tns = client.get_thumbnails(crucible_dataset_id)
    images = []
    for tn in tns:
        image_bytes = base64.b64decode(tn['thumbnail_b64str'])
        image_stream = io.BytesIO(image_bytes)
        image = Image.open(image_stream)
        images.append(image)
    return(images)


demo = gr.Interface(fn=show_thumbnails, inputs="text", outputs=gr.Gallery())
demo.launch()   
