import base64
import pathlib
import os
from template import edm_template
from template_no_rsvp import edm_template_no_rsvp
from string import Template
import requests


parent_path = str(pathlib.Path(__file__).parent)
def get_b64_img():
	get_files_img = list(os.walk(parent_path + "/imgs/"))
	files_img = []
	for _, _, last in get_files_img:
			for file in last:
				files_img.append(file)

	assets = {}
	for file in files_img:
			file_name = file.split(".")
			with open(parent_path + "./imgs/" + file, "rb") as image:
				image_base64 = base64.b64encode(image.read()).decode("utf-8")
				title_one_b64_img = f"data:image/{file_name[-1]};base64,{image_base64}"
				assets[file_name[0]] = title_one_b64_img
	
	return assets

def check_assets_type(arg):
	if arg == "base64" or arg == "url":
		return arg
	else:
		print(f"{arg} not accepted !")
		return None

def get_base64_req(url):
	b64_img = base64.b64encode(requests.get(url).content).decode("utf-8")
	return f"data:image/png;base64,{b64_img}"

def generate_html(item, assets, filetype, asset_type):
	if asset_type == "base64":
		item.update({"date":  get_base64_req(item.get("date"))});
	
	edm_html = Template(edm_template).safe_substitute(**item, **assets)
	with open(parent_path + "/result/" + item["file_name"]+"."+filetype, "w") as html:
		html.write(edm_html)

def generate_html_no_rsvp(item, assets, filetype, asset_type):
	if asset_type == "base64":
		item.update({"date":  get_base64_req(item.get("date"))});
	
	edm_html = Template(edm_template_no_rsvp).safe_substitute(**item, **assets)
	with open(parent_path + "/result_no_rsvp/" + item["file_name"]+"."+filetype, "w") as html:
		html.write(edm_html)
