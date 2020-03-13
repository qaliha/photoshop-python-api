"""Add slate information dynamically。"""

from datetime import datetime
import os

from photoshop import Session


with Session() as adobe:
    doc = adobe.app.documents.add()
    text_color = adobe.SolidColor()
    text_color.rgb.green = 255
    new_text_layer = doc.artLayers.add()
    new_text_layer.kind = adobe.LayerKind.TextLayer
    new_text_layer.textItem.contents = 'Hello, World!'
    new_text_layer.textItem.position = [160, 167]
    new_text_layer.textItem.size = 40
    new_text_layer.textItem.color = text_color
    options = adobe.JPEGSaveOptions(quality=5)
    jpg = 'd:/hello_world.jpg'
    doc.saveAs(jpg, options, asCopy=True)
    adobe.app.doJavaScript(f'alert("save to jpg: {jpg}")')
